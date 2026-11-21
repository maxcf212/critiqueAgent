"""Old batch script: run the pipeline several times per data folder with the default model.
The first run structures the rubric and task; later runs reuse it."""
import sys
from pathlib import Path

import config
import pipeline

DATA_DIRS = sorted(Path("Data").glob("*_md"))
REPEATS = 3
OUT_ROOT = f"runs/{config.DEFAULT_MODEL.split('/')[-1]}"


def run_dataset(data_dir, results):
    first_run = None
    for run_no in range(1, REPEATS + 1):
        try:
            run_dir, summary = pipeline.run(data_dir, run_no=run_no, reuse_structured=first_run, out_root=OUT_ROOT)
        except Exception as e:
            results.append((data_dir.name, run_no, None, f"FAILED: {e}"))
            if first_run is None:
                break
            continue
        first_run = first_run or run_dir
        metrics = summary["metrics"]
        details = (f"{summary['total']:g}/{summary['total_max']:g}  tokens={metrics['total_tokens']:g}  "
                   f"cost=${metrics['cost_usd']}  quotes={summary['quote_check'].get('found_rate')}  "
                   f"img_failed={summary['images_failed']}")
        results.append((data_dir.name, run_no, summary["percent"], details))


def main():
    results = []
    for data_dir in DATA_DIRS:
        run_dataset(data_dir, results)

    print("\nDataset        Run  Percent  Details")
    for name, run_no, percent, details in results:
        shown = "-" if percent is None else f"{percent:g}%"
        print(f"{name:<14} {run_no:<4} {shown:<8} {details}")
    return 1 if any(percent is None for _, _, percent, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
