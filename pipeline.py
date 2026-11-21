"""Multi-agent pipeline: rubric and task structuring, marking, feedback, then graded_rubric.json, report.md and metrics.

Output folders (TIMESTAMP = YYMMDD-HHMMSS, Eff = reasoning effort, "default" when the parameter is omitted):
  run        <out>/Input_X-Run_Y-Eff_Z-TIMESTAMP
  reference  runs/_reference/REF-Input_X-RefModel_Y-RefEff_Z--TIMESTAMP
  compare    runs/Compared-Input_X-Runs_Y-Eff_Z-TIMESTAMP/<model>/<run>"""
import argparse
import csv
import hashlib
import itertools
import json
import logging
import re
import shutil
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import agents
import config
import docs
import llm

STEPS = {"rubric": "01_rubric", "task": "02_task", "marking": "03_marking", "feedback": "04_feedback"}
CSV_FIELDS = ["run_id", "dataset", "agent", "model", "input_tokens", "output_tokens", "total_tokens",
              "reasoning_tokens", "cached_tokens", "n_images", "cost_usd", "latency_s", "wall_s", "attempts",
              "stop_reason", "json_ok", "request_id", "error", "reused", "reused_cost_usd", "reused_tokens"]
SUM_FIELDS = ["input_tokens", "output_tokens", "total_tokens", "reasoning_tokens", "cached_tokens", "n_images",
              "latency_s", "attempts"]
LOG_FORMAT = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%H:%M:%S")


def to_number(value, default=None):
    try:
        return float(str(value).strip().rstrip("%"))
    except (TypeError, ValueError):
        return default


def find_input(data_dir, prefix):
    matches = sorted(Path(data_dir).glob(f"{prefix}*.md"))
    if not matches:
        raise FileNotFoundError(f"No {prefix}*.md in {data_dir}")
    return matches[0]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def base_logger():
    """Console logger shared by all runs."""
    parent = logging.getLogger("critique")
    if not parent.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(LOG_FORMAT)
        parent.addHandler(handler)
        parent.setLevel(logging.INFO)
    return parent


def run_logger(run_id, path):
    base_logger()
    log = logging.getLogger(f"critique.{run_id}")
    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(LOG_FORMAT)
    log.addHandler(handler)
    return log


def close_logger(log):
    for handler in log.handlers[:]:
        handler.close()
        log.removeHandler(handler)


def resolve_agents(models=None, effort=None):
    """models: {"all": id} and/or {"<agent>": id or a settings dict}. effort applies to every agent."""
    cfg = {name: dict(settings) for name, settings in config.AGENTS.items()}
    models = models or {}
    for settings in cfg.values():
        if models.get("all"):
            settings["model"] = models["all"]
        if effort:
            settings["reasoning_effort"] = effort
    for name, override in models.items():
        if name in cfg and override:
            cfg[name].update(override if isinstance(override, dict) else {"model": override})
    return cfg


def stamp():
    return datetime.now().strftime("%y%m%d-%H%M%S")


def _folder_safe(text):
    return re.sub(r"[^\w.-]+", "-", str(text))


def short_model(model):
    """Model name without the provider, safe for folder names ("x/y:thinking" -> "y-thinking")."""
    return _folder_safe(str(model).split("/")[-1])


def effort_label(cfg, agent_names=None):
    """The reasoning effort shared by these agents: "default" if unset, "mixed" if they differ."""
    efforts = {_folder_safe(cfg[name].get("reasoning_effort") or "default") for name in agent_names or cfg}
    return efforts.pop() if len(efforts) == 1 else "mixed"


def run_name(dataset, cfg, run_no=1, reference=False, reused=False):
    if reference:
        structuring = ("rubric", "task")
        model = "+".join(dict.fromkeys(short_model(cfg[name]["model"]) for name in structuring))
        return f"REF-{dataset}-RefModel_{model}-RefEff_{effort_label(cfg, structuring)}--{stamp()}"
    effort = effort_label(cfg, ("marking", "feedback") if reused else None)
    return f"{dataset}-Run_{run_no}-Eff_{effort}-{stamp()}"


def new_dir(root, name):
    """Create root/name, adding -2, -3, ... if it already exists."""
    for i in itertools.count(1):
        path = Path(root) / (name if i == 1 else f"{name}-{i}")
        try:
            path.mkdir(parents=True)
            return path
        except FileExistsError:
            continue


def _grade_criterion(criterion, marks_by_id, flags):
    cid = str(criterion.get("id"))
    max_marks = to_number(criterion.get("max"), 0)
    levels = criterion.get("levels") or []
    # The marker scores on the level band scale (e.g. 0-10), not on the criterion's share of the total.
    scale = max([to_number(level.get("max"), 0) for level in levels] or [0]) or max_marks

    marked = marks_by_id.get(cid)
    if marked is None:
        flags["missing_criteria"].append(cid)
        marked = {}

    raw = to_number(marked.get("mark"))
    mark = min(max(raw or 0.0, 0.0), scale) if scale else (raw or 0.0)
    if raw is not None and mark != raw:
        flags["clamped"].append(cid)

    level = str(marked.get("level") or "").strip()
    band = next((b for b in levels if str(b.get("label", "")).strip().lower() == level.lower()), None)
    if band and not (to_number(band.get("min"), 0) <= mark <= to_number(band.get("max"), scale)):
        flags["level_mismatch"].append(cid)

    return {"id": cid, "name": criterion.get("name", ""), "weight": to_number(criterion.get("weight")),
            "level": level, "mark": mark, "scale": scale, "frac": mark / scale if scale else 0.0, "points": 0.0,
            "max": max_marks, "reasoning": marked.get("reasoning", ""),
            "evidence": [e for e in marked.get("evidence") or [] if isinstance(e, dict)]}


def grade(rubric, marking):
    """Merge the marking into the rubric, clamp marks, compute totals and flag inconsistencies."""
    marks_by_id = {str(c.get("id")): c for c in marking.get("criteria") or []}
    flags = {"missing_criteria": [], "unknown_criteria": [], "clamped": [], "level_mismatch": []}
    rows = [_grade_criterion(c, marks_by_id, flags) for c in rubric.get("criteria") or []]
    flags["unknown_criteria"] = sorted(set(marks_by_id) - {row["id"] for row in rows})

    # Printed weights take priority, then the criterion's max marks, then its band scale.
    use_weights = bool(rows) and all(row["weight"] for row in rows)
    for row in rows:
        row["max"] = row["weight"] if use_weights else (row["max"] or row["scale"])
        row["points"] = round(row.pop("frac") * row["max"], 2)

    total = sum(row["points"] for row in rows)
    total_max = sum(row["max"] for row in rows)
    percent = total / total_max * 100 if total_max else 0.0
    return {"total": round(total, 2), "total_max": total_max, "percent": round(percent, 2), "criteria": rows,
            "requirements": marking.get("requirements") or [],
            "technical_issues": marking.get("technical_issues") or [],
            "overall": marking.get("overall", ""), "flags": flags}


def _normalise(text):
    text = unicodedata.normalize("NFKC", str(text)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text).split())


def verify_quotes(plain, graded):
    """Check each evidence quote appears in the submission and mark it as verified or not."""
    submission = _normalise(plain)
    if not submission:
        return {"status": "n/a (empty submission)"}
    total = found = 0
    for row in graded["criteria"]:
        for evidence in row["evidence"]:
            quote = _normalise(evidence.get("quote", ""))
            if not quote:
                continue
            total += 1
            evidence["verified"] = quote in submission
            found += evidence["verified"]
    return {"status": "ok", "quotes_total": total, "quotes_found": found,
            "found_rate": round(found / total, 3) if total else None}


def _report_criterion(row, criterion_feedback):
    lines = ["", f"### {row['id']} {row['name']} ({row['points']:g}/{row['max']:g}, {row['level'] or '-'})", "",
             criterion_feedback, "", f"*Assessor reasoning:* {row['reasoning']}"]
    for evidence in row["evidence"]:
        warning = " *(quote not found in submission)*" if evidence.get("verified") is False else ""
        quote = f": \"{evidence['quote']}\"" if evidence.get("quote") else ""
        lines.append(f"> {evidence.get('where') or '-'}{quote}{warning}  ")
    return lines


def _report_footer(run_id, cfg, totals):
    reused_agents = totals["reused_agents"].split("+")
    models = ", ".join(f"{name}={settings['model']}" for name, settings in cfg.items() if name not in reused_agents)
    cost = totals["cost_usd"] if totals["cost_usd"] is not None else "n/a"
    reused = ""
    if totals["reused_agents"]:
        reused = (f" (incl. ${totals['reused_cost_usd']} for the reused reference "
                  f"{totals['reused_agents']} structure)")
    return ["", "---",
            f"<sub>Run {run_id} | {models} | tokens in/out {totals['input_tokens']:g}/{totals['output_tokens']:g}"
            f" | cost ${cost}{reused} | {totals['wall_s']}s</sub>", ""]


def build_report(run_id, cfg, rubric, task, graded, fb, totals):
    title = task.get("title") or rubric.get("title") or "Assessment"
    criterion_feedback = fb.get("criteria") or {}
    lines = [f"# {title}: Graded Feedback", "",
             f"**Total: {graded['total']:g} / {graded['total_max']:g} ({graded['percent']:g}%)**", "",
             fb.get("summary", ""), "",
             "## Marks", "", "| Criterion | Level | Score | Points |", "|---|---|---|---|"]
    for row in graded["criteria"]:
        lines.append(f"| {row['id']} {row['name']} | {row['level'] or '-'} | {row['mark']:g} / {row['scale']:g} "
                     f"| {row['points']:g} / {row['max']:g} |")

    lines += ["", "## Feedback by criterion"]
    for row in graded["criteria"]:
        lines += _report_criterion(row, criterion_feedback.get(row["id"], ""))

    if graded["requirements"]:
        requirement_text = {str(req.get("id")): req.get("text", "") for req in task.get("requirements") or []}
        lines += ["", "## Task requirements", "", "| ID | Requirement | Met | Where |", "|---|---|---|---|"]
        for req in graded["requirements"]:
            lines.append(f"| {req.get('id')} | {requirement_text.get(str(req.get('id')), '')} | {req.get('met')} "
                         f"| {req.get('where') or '-'} |")

    if graded["technical_issues"]:
        lines += ["", "## Technical issues", ""]
        lines += [f"- {issue.get('where') or '-'}: {issue.get('issue')}" for issue in graded["technical_issues"]]

    if fb.get("next_steps"):
        lines += ["", "## Next steps", ""]
        lines += [f"{i}. {step}" for i, step in enumerate(fb["next_steps"], 1)]

    lines += _report_footer(run_id, cfg, totals)
    return "\n".join(lines)


def _reused_call(step_dir, agent, log):
    """Metrics of a rubric/task call copied from a reference run, marked as reused."""
    metrics_file = Path(step_dir) / "metrics.json"
    if metrics_file.exists():
        return {**json.loads(metrics_file.read_text(encoding="utf-8")), "reused": True}
    log.warning(f"{metrics_file} not found: the reused {agent} step has no recorded tokens/cost "
                "(totals will be incomplete)")
    return {"agent": agent, "model": "unknown", "cost_usd": None, "json_ok": True, "reused": True}


def _csv_path(out_root, log):
    """metrics.csv in out_root, or metrics_v2.csv, metrics_v3.csv, ... if an existing file has another header."""
    for i in itertools.count(1):
        path = Path(out_root) / ("metrics.csv" if i == 1 else f"metrics_v{i}.csv")
        if not path.exists():
            return path
        with open(path, encoding="utf-8") as f:
            if f.readline().strip().split(",") == CSV_FIELDS:
                return path
        log.warning(f"{path} has a different header; not appending to it")


def _step_order(metrics):
    return list(STEPS).index(metrics["agent"]) if metrics["agent"] in STEPS else len(STEPS)


def write_metrics(run_dir, out_root, run_id, dataset, calls, wall, error, log):
    """Write metrics.json and append to metrics.csv. Totals include calls reused from a reference run;
    reused_cost_usd and reused_tokens give that share. wall_s is this run's own time only."""
    calls = sorted(calls, key=_step_order)
    costs = [m["cost_usd"] for m in calls if m.get("cost_usd") is not None]
    reused = [m for m in calls if m.get("reused")]
    totals = {field: round(sum(m.get(field) or 0 for m in calls), 2) for field in SUM_FIELDS}
    totals.update(agent="TOTAL",
                  model="+".join(sorted({m["model"] for m in calls})),
                  wall_s=round(wall, 2),
                  cost_usd=round(sum(costs), 6) if costs else None,
                  cost_complete=len(costs) == len(calls),
                  json_ok=all(m["json_ok"] for m in calls),
                  stop_reason="ok" if not error else "failed",
                  error=error,
                  reused_agents="+".join(m["agent"] for m in reused),
                  reused_cost_usd=round(sum(m.get("cost_usd") or 0 for m in reused), 6),
                  reused_tokens=sum(m.get("total_tokens") or 0 for m in reused))
    llm.dump(run_dir / "metrics.json", {"calls": calls, "total": totals})

    csv_path = _csv_path(out_root, log)
    is_new = not csv_path.exists()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, CSV_FIELDS, extrasaction="ignore")
        if is_new:
            writer.writeheader()
        for row in calls + [totals]:
            writer.writerow({**row, "run_id": run_id, "dataset": dataset})
    return totals


def log_totals(log, totals):
    reused = ""
    if totals["reused_agents"]:
        reused = (f" (of which ${totals['reused_cost_usd']} / {totals['reused_tokens']:g} tokens reused from "
                  f"the reference {totals['reused_agents']})")
    log.info(f"TOTAL in={totals['input_tokens']:g} out={totals['output_tokens']:g} cost=${totals['cost_usd']}"
             f"{reused} wall={totals['wall_s']}s")


def run_summary(run_id, run_dir, graded, images_failed, totals):
    return {"run_id": run_id, "run_dir": str(run_dir), "total": graded["total"], "total_max": graded["total_max"],
            "percent": graded["percent"], "marks": {row["id"]: row["points"] for row in graded["criteria"]},
            "flags": graded["flags"], "quote_check": graded["quote_check"],
            "images_failed": images_failed, "metrics": totals}


def count_failed_images(doc):
    return sum(not image["ok"] for d in doc.values() for image in d["images"])


def _has_images(document):
    return any(image["ok"] for image in document["images"])


def _feedback_input(graded):
    """The marking as passed to the feedback agent."""
    criteria = [{**{key: row[key] for key in ("id", "level", "mark", "scale", "points", "max", "reasoning")},
                 "evidence": [{"where": e.get("where"), "quote": e.get("quote")} for e in row["evidence"]]}
                for row in graded["criteria"]]
    return {**{key: graded[key] for key in ("requirements", "technical_issues", "overall")}, "criteria": criteria}


def run(data_dir, models=None, out_root=None, run_no=1, reuse_structured=None, effort=None, reference=False):
    """Run the full pipeline on one data folder. Returns (run_dir, summary).
    reuse_structured: earlier run folder whose rubric/task output to reuse.
    reference: name the folder REF-... and write it to config.REFERENCE_DIR."""
    if reference and reuse_structured:
        raise ValueError("a reference run structures the rubric/task itself; it cannot reuse another run's")
    data_dir = Path(data_dir)
    out_root = Path(out_root or (config.REFERENCE_DIR if reference else config.RUNS_DIR))
    inputs = {kind: find_input(data_dir, kind.capitalize()) for kind in ("rubric", "task", "solution")}
    cfg = resolve_agents(models, effort)
    dataset = data_dir.name
    run_dir = new_dir(out_root, run_name(dataset, cfg, run_no, reference, bool(reuse_structured)))
    run_id = run_dir.name
    log = run_logger(run_id, run_dir / "run.log")
    calls, error, start = [], None, time.perf_counter()

    def step(agent_fn, *args):
        try:
            output, metrics = agent_fn(*args)
        except llm.LLMError as e:
            calls.append(e.metrics)
            raise
        calls.append(metrics)
        return output

    try:
        needed = ("solution",) if reuse_structured else ("rubric", "task", "solution")
        doc = {kind: docs.load(inputs[kind], config.IMAGE_CACHE_DIR, log) for kind in needed}
        images_failed = count_failed_images(doc)
        llm.dump(run_dir / "run.json", {
            "run_id": run_id, "dataset": dataset, "started": datetime.now().isoformat(), "agents": cfg,
            "reuse_structured": str(reuse_structured or "") or None,
            "inputs": {kind: {"file": str(path), "sha256": sha256(path),
                              "images": doc[kind]["images"] if kind in doc else None}
                       for kind, path in inputs.items()}})

        llm.load_pricing(log)
        document_sent_to = {"rubric": "rubric", "task": "task", "marking": "solution"}
        vision_models = {cfg[agent]["model"] for agent, kind in document_sent_to.items()
                         if kind in doc and _has_images(doc[kind])}
        llm.check_models({settings["model"] for settings in cfg.values()}, vision_models, log)

        if reuse_structured:
            source = Path(reuse_structured)
            for kind in ("rubric", "task"):
                shutil.copytree(source / STEPS[kind], run_dir / STEPS[kind])
                calls.append(_reused_call(run_dir / STEPS[kind], kind, log))
            rubric, task = (json.loads((run_dir / STEPS[kind] / "output.json").read_text(encoding="utf-8"))
                            for kind in ("rubric", "task"))
            log.info(f"Reused structured rubric/task from {source}")
        else:
            with ThreadPoolExecutor(2) as pool:
                rubric_future = pool.submit(step, agents.structure_rubric, doc["rubric"], cfg["rubric"],
                                            run_dir / STEPS["rubric"], log)
                task_future = pool.submit(step, agents.structure_task, doc["task"], cfg["task"],
                                          run_dir / STEPS["task"], log)
                rubric, task = rubric_future.result(), task_future.result()

        marking = step(agents.mark, doc["solution"], rubric, task, cfg["marking"], run_dir / STEPS["marking"], log)
        graded = grade(rubric, marking)
        graded["quote_check"] = verify_quotes(doc["solution"]["plain"], graded)
        if any(graded["flags"].values()):
            log.warning(f"Grading flags: {graded['flags']}")

        fb = step(agents.feedback, _feedback_input(graded), rubric, task, cfg["feedback"],
                  run_dir / STEPS["feedback"], log)
    except Exception as e:
        error = f"{type(e).__name__}: {e}"[:300]
        log.error(error)
        raise
    finally:
        totals = write_metrics(run_dir, out_root, run_id, dataset, calls, time.perf_counter() - start, error, log)
        log_totals(log, totals)
        close_logger(log)

    graded["feedback"] = fb
    llm.dump(run_dir / "graded_rubric.json", graded)
    report = build_report(run_id, cfg, rubric, task, graded, fb, totals)
    (run_dir / "report.md").write_text(report, encoding="utf-8")
    return run_dir, run_summary(run_id, run_dir, graded, images_failed, totals)


def main():
    parser = argparse.ArgumentParser(description="Multi-agent rubric grader (NanoGPT, markdown inputs)")
    parser.add_argument("data_dir", help="Folder containing Rubric*.md, Task*.md, Solution*.md")
    parser.add_argument("--model-all", help="Use this model for every agent")
    for agent in config.AGENTS:
        parser.add_argument(f"--model-{agent}", help=f"Model for the {agent} agent")
    parser.add_argument("--effort", help="reasoning_effort for every agent, e.g. none/low/high/max "
                                         f"(default: config, currently {config.REASONING})")
    parser.add_argument("--run-no", type=int, default=1, help="Run number Y used in the folder name (Run_Y)")
    parser.add_argument("--out", help=f"Output root folder (default: {config.RUNS_DIR}, or {config.REFERENCE_DIR} "
                                      "with --reference)")
    parser.add_argument("--reuse-structured", help="Earlier run folder whose rubric/task JSON to reuse (skips steps 1-2)")
    parser.add_argument("--reference", action="store_true",
                        help="Make a reference run for compare_models.py, written to the reference folder as "
                             "REF-Input_X-RefModel_Y-RefEff_Z--TIMESTAMP")
    args = parser.parse_args()
    models = {"all": args.model_all, **{agent: getattr(args, f"model_{agent}") for agent in config.AGENTS}}
    _, summary = run(args.data_dir, models, args.out, args.run_no, args.reuse_structured, args.effort, args.reference)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
