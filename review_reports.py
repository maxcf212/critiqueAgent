"""Score every report.md from 1 to 5 on clarity, usability, fairness and relevance, one LLM call per report.
Each call gets the report and the original Rubric*.md the run used. The result is written to report_review.md."""
import argparse
import hashlib
import json
from pathlib import Path

import config
import llm

CRITERIA = ("clarity", "usability", "fairness", "relevance")

SYSTEM = """You are first-year university student getting feedback from an LLM instead of an actual university tutor.
You will receive the assessment rubric and one feedback report (which were based on an assignment you submitted). Rate the FEEDBACK REPORT (not the
rubric, not your own work) on each criterion from 1 to 5:
- clarity: is the feedback easy to understand, specific and unambiguous?
- usability: can the student act on it - does it give concrete, actionable steps to improve?
- fairness: are the marks deducted justifiable and not over-weighed in the context of what the assignment is actually about?
- relevance: does the feedback address the rubric's criteria and standards, without filler or generic advice?
Scale: 1 = very poor, 2 = poor, 3 = adequate, 4 = good, 5 = excellent.

Return ONLY this JSON object, no other text:
{"clarity": {"score": <int 1-5>, "justification": "<1-2 sentences>"},
 "usability": {"score": <int 1-5>, "justification": "<1-2 sentences>"},
 "fairness": {"score": <int 1-5>, "justification": "<1-2 sentences>"},
 "relevance": {"score": <int 1-5>, "justification": "<1-2 sentences>"}}"""


def is_valid(review):
    for criterion in CRITERIA:
        entry = review.get(criterion)
        if not isinstance(entry, dict):
            return False
        score = entry.get("score")
        if type(score) is not int or not 1 <= score <= 5:
            return False
    return True


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def original_rubric(report_path):
    """The Rubric*.md recorded in the run's run.json. If that path no longer exists (e.g. a renamed data folder),
    use the file with the same name and hash under Data/."""
    recorded = json.loads(report_path.with_name("run.json").read_text(encoding="utf-8"))["inputs"]["rubric"]
    path = Path(recorded["file"])
    if not path.exists():
        candidates = Path("Data").glob(f"*/{path.name}")
        path = next((p for p in candidates if sha256(p) == recorded["sha256"]), None)
        if path is None:
            raise FileNotFoundError(f"original rubric {recorded['file']} not found")
    return path.read_text(encoding="utf-8")


def review(model, rubric, report):
    user = f"# ASSESSMENT RUBRIC\n\n{rubric}\n\n# FEEDBACK REPORT TO REVIEW\n\n{report}"
    payload = {"model": model, "max_tokens": 4000, "temperature": 0, "reasoning_effort": "low",
               "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]}
    for _ in range(2):
        try:
            result = llm.parse_json(llm.response_text(llm.post_chat(payload)[0]))
            if is_valid(result):
                return {criterion: result[criterion] for criterion in CRITERIA}
        except ValueError:
            pass
    raise ValueError("invalid JSON twice")


def find_reports(roots, overwrite):
    return [path for root in roots for path in sorted(Path(root).rglob("report.md"))
            if overwrite or not path.with_name("report_review.md").exists()]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("roots", nargs="*", default=[config.RUNS_DIR, config.ONESHOT_RUNS_DIR])
    parser.add_argument("--model", default="openai/gpt-6-luna")
    parser.add_argument("--overwrite", action="store_true", help="re-review reports that already have report_review.md")
    args = parser.parse_args()

    reports = find_reports(args.roots, args.overwrite)
    for i, path in enumerate(reports, 1):
        progress = f"[{i}/{len(reports)}] {path}"
        try:
            result = review(args.model, original_rubric(path), path.read_text(encoding="utf-8"))
        except Exception as e:  # one failed report must not stop the batch
            print(f"{progress} -> FAILED: {e}")
            continue
        path.with_name("report_review.md").write_text(json.dumps(result, indent=2, ensure_ascii=False),
                                                      encoding="utf-8")
        print(f"{progress} -> " + " ".join(f"{c}={result[c]['score']}" for c in CRITERIA))


if __name__ == "__main__":
    main()
