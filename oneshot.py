"""Single-prompt version of critiqueagent: one model call takes input task, rubric and submission and returns marks and feedback as JSON.
The marks and total are the model's own; Python only checks them.

Output: runs_oneshot/Input_X-Run_Y-Eff_Z-TIMESTAMP/{01_oneshot/, graded_rubric.json, report.md, metrics.json, run.json, run.log}"""
import argparse
import json
import time
from datetime import datetime
from pathlib import Path

import config
import docs
import llm
import pipeline

STEP = "01_oneshot"

PROMPT = """You are marking a student submission. Below are the assessment task, the marking rubric and the student's submission.
Mark the submission against every rubric criterion and give the student feedback.
Reply with one JSON object only (no prose, no markdown) in this form:
{"criteria":[{"name":str,"level":str,"mark":num,"max":num,"feedback":str}],"total":num,"total_max":num,"summary":str,"next_steps":[str]}
List the criteria in rubric order. "mark" and "max" are the marks awarded and available for that criterion as they count
toward the total (apply any weighting), so "total" is the sum of the marks and "total_max" the sum of the maxima."""


def resolve(model=None, effort=None):
    cfg = dict(config.ONESHOT)
    if model:
        cfg["model"] = model
    if effort:
        cfg["reasoning_effort"] = effort
    return {"oneshot": cfg}


def _criterion_row(index, criterion, flags):
    cid = f"C{index}"
    max_marks = pipeline.to_number(criterion.get("max"), 0) or 0.0
    raw = pipeline.to_number(criterion.get("mark"))
    mark = min(max(raw or 0.0, 0.0), max_marks) if max_marks else (raw or 0.0)
    if raw is None:
        flags["missing_criteria"].append(cid)
    elif mark != raw:
        flags["clamped"].append(cid)
    return {"id": cid, "name": str(criterion.get("name", "")), "weight": None,
            "level": str(criterion.get("level") or "").strip(), "mark": mark, "scale": max_marks,
            "points": round(mark, 2), "max": max_marks, "reasoning": str(criterion.get("feedback", "")),
            "evidence": []}


def grade(out):
    """Put the model's reply in the same shape as pipeline.grade(), clamping impossible marks and
    flagging a total that does not match the sum of the criteria."""
    flags = {"missing_criteria": [], "unknown_criteria": [], "clamped": [], "level_mismatch": [], "total_mismatch": []}
    criteria = [c for c in out.get("criteria") or [] if isinstance(c, dict)]
    rows = [_criterion_row(i, c, flags) for i, c in enumerate(criteria, 1)]
    if not rows:
        raise RuntimeError("model reply contains no criteria")

    sum_points = round(sum(row["points"] for row in rows), 2)
    sum_max = sum(row["max"] for row in rows)
    total, total_max = pipeline.to_number(out.get("total")), pipeline.to_number(out.get("total_max"))
    reported = {"total": total, "total_max": total_max}
    if total is None or not total_max:
        flags["total_mismatch"].append("total missing; sum of criterion marks used")
        total, total_max = sum_points, sum_max
    elif abs(total - sum_points) > 0.01 or abs(total_max - sum_max) > 0.01:
        flags["total_mismatch"].append(
            f"model total {total:g}/{total_max:g} != sum of criteria {sum_points:g}/{sum_max:g}")

    percent = total / total_max * 100 if total_max else 0.0
    next_steps = out.get("next_steps")
    next_steps = [str(s) for s in next_steps or []] if isinstance(next_steps, list) else []
    summary = str(out.get("summary", ""))
    return {"method": "oneshot", "total": round(total, 2), "total_max": total_max, "percent": round(percent, 2),
            "criteria": rows, "requirements": [], "technical_issues": [], "overall": summary,
            "flags": flags, "quote_check": {"status": "n/a (one-shot: no evidence quotes requested)"},
            "model_reported": reported, "sum_of_criteria": {"total": sum_points, "total_max": sum_max},
            "feedback": {"summary": summary, "next_steps": next_steps,
                         "criteria": {row["id"]: row["reasoning"] for row in rows}}}


def build_report(run_id, dataset, cfg, graded, totals):
    fb = graded["feedback"]
    lines = [f"# {dataset}: Graded Feedback (one-shot)", "",
             f"**Total: {graded['total']:g} / {graded['total_max']:g} ({graded['percent']:g}%)**", "",
             fb["summary"], "",
             "## Marks", "", "| Criterion | Level | Points |", "|---|---|---|"]
    for row in graded["criteria"]:
        lines.append(f"| {row['id']} {row['name']} | {row['level'] or '-'} | {row['points']:g} / {row['max']:g} |")

    lines += ["", "## Feedback by criterion"]
    for row in graded["criteria"]:
        lines += ["", f"### {row['id']} {row['name']} ({row['points']:g}/{row['max']:g}, {row['level'] or '-'})", "",
                  row["reasoning"]]

    if fb["next_steps"]:
        lines += ["", "## Next steps", ""] + [f"{i}. {step}" for i, step in enumerate(fb["next_steps"], 1)]
    if graded["flags"]["total_mismatch"]:
        lines += ["", f"*Check: {'; '.join(graded['flags']['total_mismatch'])}*"]

    cost = totals["cost_usd"] if totals["cost_usd"] is not None else "n/a"
    lines += ["", "---",
              f"<sub>Run {run_id} | oneshot={cfg['oneshot']['model']} | tokens in/out "
              f"{totals['input_tokens']:g}/{totals['output_tokens']:g} | cost ${cost} | {totals['wall_s']}s</sub>", ""]
    return "\n".join(lines)


def _prompt_parts(doc):
    return [llm.text_block("ASSESSMENT TASK:\n"), *doc["task"]["parts"],
            llm.text_block("\n\nMARKING RUBRIC:\n"), *doc["rubric"]["parts"],
            llm.text_block("\n\nSTUDENT SUBMISSION:\n"), *doc["solution"]["parts"]]


def run(data_dir, model=None, out_root=None, run_no=1, effort=None):
    """One single-prompt grading run. Returns (run_dir, summary) like pipeline.run()."""
    data_dir, out_root = Path(data_dir), Path(out_root or config.ONESHOT_RUNS_DIR)
    inputs = {kind: pipeline.find_input(data_dir, kind.capitalize()) for kind in ("task", "rubric", "solution")}
    cfg = resolve(model, effort)
    model_id = cfg["oneshot"]["model"]
    dataset = data_dir.name
    run_dir = pipeline.new_dir(out_root, pipeline.run_name(dataset, cfg, run_no))
    run_id = run_dir.name
    log = pipeline.run_logger(run_id, run_dir / "run.log")
    calls, error, start = [], None, time.perf_counter()
    try:
        doc = {kind: docs.load(path, config.IMAGE_CACHE_DIR, log) for kind, path in inputs.items()}
        images_failed = pipeline.count_failed_images(doc)
        llm.dump(run_dir / "run.json", {
            "run_id": run_id, "dataset": dataset, "method": "oneshot", "started": datetime.now().isoformat(),
            "agents": cfg, "reuse_structured": None,
            "inputs": {kind: {"file": str(path), "sha256": pipeline.sha256(path), "images": doc[kind]["images"]}
                       for kind, path in inputs.items()}})

        llm.load_pricing(log)
        has_images = any(image["ok"] for d in doc.values() for image in d["images"])
        llm.check_models({model_id}, {model_id} if has_images else set(), log)

        try:
            out, metrics = llm.call("oneshot", cfg["oneshot"], PROMPT, _prompt_parts(doc), run_dir / STEP, log)
        except llm.LLMError as e:
            calls.append(e.metrics)
            raise
        calls.append(metrics)

        graded = grade(out)
        if any(graded["flags"].values()):
            log.warning(f"Grading flags: {graded['flags']}")
    except Exception as e:
        error = f"{type(e).__name__}: {e}"[:300]
        log.error(error)
        raise
    finally:
        totals = pipeline.write_metrics(run_dir, out_root, run_id, dataset, calls, time.perf_counter() - start,
                                        error, log)
        log.info(f"TOTAL in={totals['input_tokens']:g} out={totals['output_tokens']:g} cost=${totals['cost_usd']} "
                 f"wall={totals['wall_s']}s")
        pipeline.close_logger(log)

    llm.dump(run_dir / "graded_rubric.json", graded)
    (run_dir / "report.md").write_text(build_report(run_id, dataset, cfg, graded, totals), encoding="utf-8")
    return run_dir, pipeline.run_summary(run_id, run_dir, graded, images_failed, totals)


def main():
    parser = argparse.ArgumentParser(description="Single-prompt (one-shot) rubric grader baseline (NanoGPT, markdown inputs)")
    parser.add_argument("data_dir", help="Folder containing Rubric*.md, Task*.md, Solution*.md")
    parser.add_argument("--model", help=f"Model id (default: {config.ONESHOT['model']})")
    parser.add_argument("--effort", help="reasoning_effort, e.g. none/low/high/max "
                                         f"(default: config, currently {config.ONESHOT['reasoning_effort']})")
    parser.add_argument("--run-no", type=int, default=1, help="Run number Y used in the folder name (Run_Y)")
    parser.add_argument("--out", help=f"Output root folder (default: {config.ONESHOT_RUNS_DIR})")
    args = parser.parse_args()
    _, summary = run(args.data_dir, args.model, args.out, args.run_no, args.effort)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
