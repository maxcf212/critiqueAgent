"""Orchestrates: rubric+task structuring -> marking -> feedback -> graded_rubric.json + report.md + metrics."""
import argparse
import csv
import hashlib
import json
import logging
import re
import shutil
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

import agents
import config
import llm

STEPS = {"rubric": "01_rubric", "task": "02_task", "marking": "03_marking", "feedback": "04_feedback"}
CSV_FIELDS = ["run_id", "dataset", "agent", "model", "input_tokens", "output_tokens", "total_tokens",
              "reasoning_tokens", "cache_read_tokens", "cache_creation_tokens", "cost_usd", "latency_s",
              "wall_s", "attempts", "stop_reason", "json_ok", "request_id", "error"]
SUM_FIELDS = ["input_tokens", "output_tokens", "total_tokens", "reasoning_tokens",
              "cache_read_tokens", "cache_creation_tokens", "latency_s", "attempts"]


# ---------- helpers ----------

def _num(x, default=None):
    try:
        return float(str(x).strip().rstrip("%"))
    except (TypeError, ValueError):
        return default


def _find(data_dir, prefix):
    hits = sorted(Path(data_dir).glob(f"{prefix}*.pdf"))
    if not hits:
        raise FileNotFoundError(f"No {prefix}*.pdf in {data_dir}")
    return hits[0]


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _logger(run_id, path):
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%H:%M:%S")
    parent = logging.getLogger("critique")
    if not parent.handlers:
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        parent.addHandler(sh)
        parent.setLevel(logging.INFO)
    log = logging.getLogger(f"critique.{run_id}")
    fh = logging.FileHandler(path, encoding="utf-8")
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log


def resolve_agents(models=None, pdf_mode=None):
    """models: {"all": id} and/or {"<agent>": id | {model, max_tokens, temperature, pdf_mode}}.
    pdf_mode overrides every agent's PDF input mode (images | native | text)."""
    cfg = {k: {"pdf_mode": config.PDF_MODE, **v} for k, v in config.AGENTS.items()}
    models = models or {}
    for c in cfg.values():
        if models.get("all"):
            c["model"] = models["all"]
        if pdf_mode:
            c["pdf_mode"] = pdf_mode
    for k, v in models.items():
        if k in cfg and v:
            cfg[k].update(v if isinstance(v, dict) else {"model": v})
    return cfg


# ---------- deterministic post-processing (no tokens) ----------

def grade(rubric, marking):
    """Merge marking into rubric rows, clamp marks, compute totals in Python, and flag inconsistencies."""
    by_id = {str(c.get("id")): c for c in marking.get("criteria") or []}
    flags = {"missing_criteria": [], "unknown_criteria": [], "clamped": [], "level_mismatch": []}
    rows = []
    for c in rubric.get("criteria") or []:
        cid, mx = str(c.get("id")), _num(c.get("max"), 0)
        levels = c.get("levels") or []
        # The marker scores on the level-band scale (e.g. 0-10), which may differ from the
        # criterion's contribution to the total (max/weight, e.g. 40). Scale = top of the bands.
        scale = max([_num(l.get("max"), 0) for l in levels] or [0]) or mx
        m = by_id.get(cid)
        if m is None:
            flags["missing_criteria"].append(cid)
            m = {}
        raw = _num(m.get("mark"))
        mark = min(max(raw or 0.0, 0.0), scale) if scale else (raw or 0.0)
        if raw is not None and mark != raw:
            flags["clamped"].append(cid)
        level = str(m.get("level") or "").strip()
        lv = next((l for l in levels if str(l.get("label", "")).strip().lower() == level.lower()), None)
        if lv and not (_num(lv.get("min"), 0) <= mark <= _num(lv.get("max"), scale)):
            flags["level_mismatch"].append(cid)
        frac = mark / scale if scale else 0.0
        rows.append({"id": cid, "name": c.get("name", ""), "weight": _num(c.get("weight")), "level": level,
                     "mark": mark, "scale": scale, "frac": frac, "points": 0.0, "max": mx,
                     "reasoning": m.get("reasoning", ""),
                     "evidence": [e for e in m.get("evidence") or [] if isinstance(e, dict)]})
    flags["unknown_criteria"] = sorted(set(by_id) - {r["id"] for r in rows})

    # Contribution per criterion: printed weights win (LLM-inferred totals/max are unreliable);
    # otherwise the criterion's max marks; otherwise its band scale.
    use_weights = bool(rows) and all(r["weight"] for r in rows)
    for r in rows:
        r["max"] = r["weight"] if use_weights else (r["max"] or r["scale"])
        r["points"] = round(r.pop("frac") * r["max"], 2)
    total, total_max = sum(r["points"] for r in rows), sum(r["max"] for r in rows)
    percent = total / total_max * 100 if total_max else 0.0
    return {"total": round(total, 2), "total_max": total_max, "percent": round(percent, 2), "criteria": rows,
            "requirements": marking.get("requirements") or [], "technical_issues": marking.get("technical_issues") or [],
            "overall": marking.get("overall", ""), "flags": flags}


def _norm(s):
    s = unicodedata.normalize("NFKC", str(s)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def verify_quotes(pdf, graded):
    """Check every evidence quote exists in the submission text; annotates evidence with 'verified'."""
    try:
        pages = [_norm(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]
    except Exception as e:
        return {"status": f"error: {e}"}
    if not any(pages):
        return {"status": "n/a (no extractable text)"}
    joined = " ".join(pages)
    total = found = on_page = 0
    for r in graded["criteria"]:
        for e in r["evidence"]:
            q = _norm(e.get("quote", ""))
            if not q:
                continue
            total += 1
            idx = int(_num(e.get("page"), 0)) - 1
            e["verified"] = q in joined
            found += e["verified"]
            on_page += 0 <= idx < len(pages) and q in pages[idx]
    return {"status": "ok", "quotes_total": total, "quotes_found": found, "quotes_on_cited_page": on_page,
            "found_rate": round(found / total, 3) if total else None}


# ---------- outputs ----------

def build_report(run_id, cfg, rubric, task, graded, fb, totals):
    title = task.get("title") or rubric.get("title") or "Assessment"
    fbc = fb.get("criteria") or {}
    L = [f"# {title}: Graded Feedback", "",
         f"**Total: {graded['total']:g} / {graded['total_max']:g} ({graded['percent']:g}%)**", "",
         fb.get("summary", ""), "", "## Marks", "", "| Criterion | Level | Score | Points |", "|---|---|---|---|"]
    L += [f"| {r['id']} {r['name']} | {r['level'] or '-'} | {r['mark']:g} / {r['scale']:g} | {r['points']:g} / {r['max']:g} |"
          for r in graded["criteria"]]
    L += ["", "## Feedback by criterion"]
    for r in graded["criteria"]:
        L += ["", f"### {r['id']} {r['name']} ({r['points']:g}/{r['max']:g}, {r['level'] or '-'})", "",
              fbc.get(r["id"], ""), "", f"*Assessor reasoning:* {r['reasoning']}"]
        for e in r["evidence"]:
            warn = " *(quote not found in PDF)*" if e.get("verified") is False else ""
            L.append(f"> p.{e.get('page')}: \"{e.get('quote')}\"{warn}  ")
    if graded["requirements"]:
        req_text = {str(q.get("id")): q.get("text", "") for q in task.get("requirements") or []}
        L += ["", "## Task requirements", "", "| ID | Requirement | Met | Page |", "|---|---|---|---|"]
        L += [f"| {q.get('id')} | {req_text.get(str(q.get('id')), '')} | {q.get('met')} | {q.get('page') or '-'} |"
              for q in graded["requirements"]]
    if graded["technical_issues"]:
        L += ["", "## Technical issues", ""] + [f"- p.{t.get('page')}: {t.get('issue')}" for t in graded["technical_issues"]]
    if fb.get("next_steps"):
        L += ["", "## Next steps", ""] + [f"{i}. {s}" for i, s in enumerate(fb["next_steps"], 1)]
    models = ", ".join(f"{k}={v['model']}" for k, v in cfg.items())
    L += ["", "---", f"<sub>Run {run_id} | {models} | tokens in/out {totals['input_tokens']}/{totals['output_tokens']}"
          f" | cost ${totals['cost_usd'] if totals['cost_usd'] is not None else 'n/a'} | {totals['wall_s']}s</sub>", ""]
    return "\n".join(L)


def write_metrics(run_dir, out_root, run_id, dataset, calls, wall, error):
    calls = sorted(calls, key=lambda m: list(STEPS).index(m["agent"]))
    costs = [m["cost_usd"] for m in calls if m.get("cost_usd") is not None]
    totals = {k: round(sum(m.get(k) or 0 for m in calls), 2) for k in SUM_FIELDS}
    totals.update(agent="TOTAL", model="+".join(sorted({m["model"] for m in calls})), wall_s=round(wall, 2),
                  cost_usd=round(sum(costs), 6) if costs else None,
                  cost_complete=len(costs) == len(calls), json_ok=all(m["json_ok"] for m in calls),
                  stop_reason="ok" if not error else "failed", error=error)
    llm.dump(run_dir / "metrics.json", {"calls": calls, "total": totals})
    csv_path = Path(out_root) / "metrics.csv"
    new = not csv_path.exists()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, CSV_FIELDS, extrasaction="ignore")
        if new:
            w.writeheader()
        for row in calls + [totals]:
            w.writerow({**row, "run_id": run_id, "dataset": dataset})
    return totals


# ---------- pipeline ----------

def run(data_dir, models=None, out_root="runs", tag="", reuse_structured=None, pdf_mode=None):
    """Run the full pipeline on one data folder. Returns (run_dir, summary). Safe to call from a parent script."""
    data_dir, out_root = Path(data_dir), Path(out_root)
    inputs = {k: _find(data_dir, k) for k in ("Rubric", "Task", "Solution")}
    cfg = resolve_agents(models, pdf_mode)
    dataset = data_dir.name
    run_id = "_".join(filter(None, [datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3], dataset,
                                    re.sub(r"[^\w.-]+", "-", tag)]))
    run_dir = out_root / run_id
    run_dir.mkdir(parents=True)
    log = _logger(run_id, run_dir / "run.log")
    llm.dump(run_dir / "run.json", {"run_id": run_id, "dataset": dataset, "started": datetime.now().isoformat(),
                                    "inputs": {k: {"file": str(p), "sha256": _sha(p)} for k, p in inputs.items()},
                                    "agents": cfg, "reuse_structured": str(reuse_structured or "") or None})
    llm.load_pricing(out_root / "_pricing.json", log)
    llm.check_models({c["model"] for c in cfg.values()}, log)

    calls, error, t0 = [], None, time.perf_counter()

    def step(fn, *args):
        try:
            out, m = fn(*args)
        except llm.LLMError as e:
            calls.append(e.metrics)
            raise
        calls.append(m)
        return out

    try:
        if reuse_structured:
            src = Path(reuse_structured)
            for k in ("rubric", "task"):
                shutil.copytree(src / STEPS[k], run_dir / STEPS[k])
            rubric, task = (json.loads((run_dir / STEPS[k] / "output.json").read_text(encoding="utf-8"))
                            for k in ("rubric", "task"))
            log.info(f"Reused structured rubric/task from {src}")
        else:
            with ThreadPoolExecutor(2) as ex:
                fr = ex.submit(step, agents.structure_rubric, inputs["Rubric"], cfg["rubric"], run_dir / STEPS["rubric"], log)
                ft = ex.submit(step, agents.structure_task, inputs["Task"], cfg["task"], run_dir / STEPS["task"], log)
                rubric, task = fr.result(), ft.result()

        marking = step(agents.mark, inputs["Solution"], rubric, task, cfg["marking"], run_dir / STEPS["marking"], log)
        graded = grade(rubric, marking)
        graded["quote_check"] = verify_quotes(inputs["Solution"], graded)
        if any(graded["flags"].values()):
            log.warning(f"Grading flags: {graded['flags']}")

        fb_input = {**{k: graded[k] for k in ("requirements", "technical_issues", "overall")},
                    "criteria": [{**{k: r[k] for k in ("id", "level", "mark", "scale", "points", "max", "reasoning")},
                                  "evidence": [{"page": e.get("page"), "quote": e.get("quote")} for e in r["evidence"]]}
                                 for r in graded["criteria"]]}
        fb = step(agents.feedback, fb_input, rubric, task, cfg["feedback"], run_dir / STEPS["feedback"], log)
    except Exception as e:
        error = f"{type(e).__name__}: {e}"[:300]
        log.error(error)
        raise
    finally:
        totals = write_metrics(run_dir, out_root, run_id, dataset, calls, time.perf_counter() - t0, error)
        log.info(f"TOTAL in={totals['input_tokens']} out={totals['output_tokens']} "
                 f"cost=${totals['cost_usd']} wall={totals['wall_s']}s")
        for h in log.handlers[:]:
            h.close()
            log.removeHandler(h)

    graded["feedback"] = fb
    llm.dump(run_dir / "graded_rubric.json", graded)
    (run_dir / "report.md").write_text(build_report(run_id, cfg, rubric, task, graded, fb, totals), encoding="utf-8")
    summary = {"run_id": run_id, "run_dir": str(run_dir), "total": graded["total"], "total_max": graded["total_max"],
               "percent": graded["percent"], "flags": graded["flags"], "quote_check": graded["quote_check"],
               "metrics": totals}
    return run_dir, summary


def main():
    ap = argparse.ArgumentParser(description="Multi-agent rubric grader (NanoGPT)")
    ap.add_argument("data_dir", help="Folder containing Task_*.pdf, Rubric_*.pdf, Solution_*.pdf")
    ap.add_argument("--model-all", help="Use this model for every agent")
    for a in config.AGENTS:
        ap.add_argument(f"--model-{a}", help=f"Model for the {a} agent")
    ap.add_argument("--tag", default="", help="Label appended to the run folder name")
    ap.add_argument("--out", default="runs", help="Output root folder")
    ap.add_argument("--reuse-structured", help="Prior run folder whose rubric/task JSON to reuse (skips steps 1-2)")
    ap.add_argument("--pdf-mode", choices=["images", "native", "text"], help="Override PDF input mode for all agents")
    a = ap.parse_args()
    models = {"all": a.model_all, **{k: getattr(a, f"model_{k}") for k in config.AGENTS}}
    _, summary = run(a.data_dir, models, a.out, a.tag, a.reuse_structured, a.pdf_mode)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
