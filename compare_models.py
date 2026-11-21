"""Compare models on one data folder: each model is run N times against the same frozen reference rubric and task.

Output: runs/Compared-Input_X-Runs_Y-Eff_Z-TIMESTAMP/<model>/<run folders> plus compare.csv.
cost_usd and tokens in compare.csv cover the whole pipeline, including the reused reference calls
(given separately as reused_cost_usd and reused_tokens).

Usage:
  python compare_models.py Data/Input_3 --structured runs/_reference/REF-Input_3-... [--repeats 3] [--models a b] [--effort low]
  python compare_models.py Data/Input_3 --method oneshot [--repeats 3] [--models a b] [--effort low]"""
import argparse
import csv
import json
import re
import statistics
import sys
from pathlib import Path

import config
import llm
import oneshot
import pipeline

BASE_FIELDS = ["method", "model", "rep", "run_id", "status", "effort", "percent", "total", "total_max"]
METRIC_FIELDS = ["cost_usd", "reused_cost_usd", "input_tokens", "output_tokens", "reused_tokens", "wall_s",
                 "quote_found_rate", "n_flags", "images_failed", "error", "reference"]


def natural_key(criterion_id):
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", criterion_id)]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("data_dir")
    parser.add_argument("--method", choices=["agents", "oneshot"], default="agents",
                        help="agents = multi-agent pipeline on a frozen reference (default); "
                             "oneshot = single-prompt baseline, no reference needed")
    parser.add_argument("--structured", help="[agents] Run folder with the reference 01_rubric/ and 02_task/")
    parser.add_argument("--models", nargs="+", default=config.MODELS)
    parser.add_argument("--repeats", type=int, default=1)
    parser.add_argument("--effort", help="reasoning_effort for every agent, e.g. none/low/high/max "
                                         f"(default: config, currently {config.REASONING})")
    parser.add_argument("--out", help=f"Output root (default: {config.RUNS_DIR}, or {config.ONESHOT_RUNS_DIR} "
                                      "for oneshot)")
    args = parser.parse_args()
    if args.method == "oneshot" and args.structured:
        parser.error("--structured is not used with --method oneshot")
    if args.method == "agents" and not args.structured:
        parser.error("--structured is required with --method agents")
    return args


def load_reference(reference):
    """Check the reference folder and return its criterion ids."""
    for step in ("01_rubric", "02_task"):
        if not (reference / step / "output.json").exists():
            sys.exit(f"{reference / step / 'output.json'} not found")
    rubric = json.loads((reference / "01_rubric" / "output.json").read_text(encoding="utf-8"))
    return [str(c["id"]) for c in rubric.get("criteria", [])]


def write_compare_csv(path, rows, criterion_ids):
    """One-shot runs have no frozen rubric, so extra criterion columns are whatever ids the models returned."""
    extra_ids = sorted({cid for row in rows for cid in row.get("_marks", {})} - set(criterion_ids), key=natural_key)
    fields = BASE_FIELDS + criterion_ids + extra_ids + METRIC_FIELDS
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows({**row, **row.get("_marks", {})} for row in rows)


def run_once(args, model, rep, model_dir, reference):
    if args.method == "oneshot":
        _, summary = oneshot.run(args.data_dir, model=model, out_root=model_dir, run_no=rep, effort=args.effort)
    else:
        _, summary = pipeline.run(args.data_dir, models={"all": model}, out_root=model_dir, run_no=rep,
                                  reuse_structured=reference, effort=args.effort)
    metrics = summary["metrics"]
    return {"_marks": summary["marks"], "status": "ok", "run_id": summary["run_id"], "percent": summary["percent"],
            "total": summary["total"], "total_max": summary["total_max"], "cost_usd": metrics["cost_usd"],
            "reused_cost_usd": metrics["reused_cost_usd"], "input_tokens": metrics["input_tokens"],
            "output_tokens": metrics["output_tokens"], "reused_tokens": metrics["reused_tokens"],
            "wall_s": metrics["wall_s"], "quote_found_rate": summary["quote_check"].get("found_rate"),
            "n_flags": sum(map(len, summary["flags"].values())), "images_failed": summary["images_failed"]}


def mean_text(values):
    values = [v for v in values if v is not None]
    return str(round(statistics.mean(values), 4)) if values else "-"


def print_summary(rows, models, repeats, oneshot_mode, csv_path):
    scope = "" if oneshot_mode else " of the whole pipeline, incl. the reused reference rubric/task calls"
    print("\nCost$ = mean cost per run" + scope)
    print(f"{'Model':<36} {'OK':<6} {'Mean%':<8} {'SD%':<7} {'Cost$':<10} Quotes")
    for model in models:
        ok = [row for row in rows if row["model"] == model and row["status"] == "ok"]
        percents = [row["percent"] for row in ok]
        sd = str(round(statistics.stdev(percents), 2)) if len(percents) > 1 else "-"
        print(f"{model:<36} {f'{len(ok)}/{repeats}':<6} {mean_text(percents):<8} {sd:<7} "
              f"{mean_text([row['cost_usd'] for row in ok]):<10} {mean_text([row['quote_found_rate'] for row in ok])}")
    print(f"\nResults: {csv_path}")


def main():
    args = parse_args()
    oneshot_mode = args.method == "oneshot"
    data_dir = Path(args.data_dir)

    reference, criterion_ids = None, []
    if oneshot_mode:
        effort = pipeline.effort_label(oneshot.resolve(effort=args.effort))
    else:
        reference = Path(args.structured)
        criterion_ids = load_reference(reference)
        effort = pipeline.effort_label(pipeline.resolve_agents(effort=args.effort), ("marking", "feedback"))

    out_root = args.out or (config.ONESHOT_RUNS_DIR if oneshot_mode else config.RUNS_DIR)
    batch_name = f"Compared-{data_dir.name}-Runs_{args.repeats}-Eff_{effort}-{pipeline.stamp()}"
    batch_dir = pipeline.new_dir(out_root, batch_name)
    llm.load_pricing(pipeline.base_logger(), refresh=True)
    csv_path = batch_dir / "compare.csv"

    rows = []
    for model in args.models:
        model_dir = batch_dir / pipeline.short_model(model)
        for rep in range(1, args.repeats + 1):
            row = {"method": args.method, "model": model, "rep": rep, "effort": effort,
                   "reference": str(reference or "")}
            try:
                row.update(run_once(args, model, rep, model_dir, reference))
            except Exception as e:  # one failing model must not stop the comparison
                row.update(status="failed", error=f"{type(e).__name__}: {e}"[:300])
            rows.append(row)
            write_compare_csv(csv_path, rows, criterion_ids)

    print_summary(rows, args.models, args.repeats, oneshot_mode, csv_path)
    return 1 if any(row["status"] != "ok" for row in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
