"""Run the pipeline N times per data folder with the default model config.
Run 1 structures the rubric/task; runs 2..N reuse run 1's structure (--reuse-structured)."""
import sys
from pathlib import Path

import pipeline

DATA_DIRS = [Path("Data/Input_1"), Path("Data/Input_2")]
REPEATS = 3


def main():
    results = []
    for data_dir in DATA_DIRS:
        first_run = None
        for i in range(1, REPEATS + 1):
            try:
                run_dir, s = pipeline.run(data_dir, tag=f"run{i}", reuse_structured=first_run, out_root="runs/gemini-3.5-flash-lite")
            except Exception as e:
                results.append((data_dir.name, i, None, f"FAILED: {e}"))
                if first_run is None:  # no structure to reuse; skip remaining repeats for this dataset
                    break
                continue
            first_run = first_run or run_dir
            m = s["metrics"]
            results.append((data_dir.name, i, s["percent"],
                            f"{s['total']:g}/{s['total_max']:g}  tokens={m['total_tokens']:g}  cost=${m['cost_usd']}"))

    print("\nDataset   Run  Percent  Details")
    for name, i, pct, info in results:
        print(f"{name:<9} {i:<4} {'-' if pct is None else f'{pct:g}%':<8} {info}")
    return 1 if any(r[2] is None for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
