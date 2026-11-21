# CritiqueAgentv3 (ver OCT. 2026)

Marks student submissions against a rubric using LLMs through the NanoGPT API. There are two methods: a multi-agent pipeline and a single-prompt baseline.

## Data

Data/ holds the input datasets. Each folder has a Task, Rubric and Solution markdown file.

- Input_1: preliminary engineering design report (aerospace), medium length. Converted from PDF. The originals are in source_pdf/
- Input_2: final engineering design report (aerospace), long.
- Input_3: engineering and business ethics report (QA, manufacturing), long.
- Input_4: synthetic short-answer assignment on software architecture, six questions, short

Each base set has two variants with the same rubric and task but a different solution:

- Input_X_u: solution fixed to address what the marking criticised. Should score higher.
- Input_X_d: solution with 4-5 planted defects. Should score lower.

Each variant folder has a CHANGES.md listing the edits. Because the rubric and task are identical, a base set and its variants use the same reference. Only the Rubric, Task and Solution files are sent to the models.

Images in the markdown can be web links (downloaded once into runs/\_img_cache) or files relative to the markdown file.

## Code

- pipeline.py: the multi-agent pipeline. Structures the rubric and task, marks the submission, writes feedback, then saves graded_rubric.json, report.md and metrics. Also builds the output folder names.
- agents.py: prompts for the rubric, task, marking and feedback agents. The feedback agent currently mostly rewords the marking agent's reasoning.
- llm.py: API client with retries, token and cost metrics, pricing and model checks.
- docs.py: loads a markdown input, strips HTML clutter and embeds its images.
- oneshot.py: single-prompt baseline. One call gets the task, rubric and submission and returns marks and feedback as JSON. The marks and total are the model's own; Python only checks the sum. Output goes to runs_oneshot/ in the same layout as the pipeline.
- compare_models.py: runs each model N times on one dataset. With the agents method, the rubric and task are taken from a frozen, human-checked reference run, so only the marking and feedback agents run.
- review_reports.py: asks an LLM (openai/gpt-6-luna by default) to score each report.md from 1 to 5 on clarity, usability, fairness and relevance, given the original rubric. Writes report_review.md next to each report and skips reports that already have one unless --overwrite is set.
- batch_runs.py: old, don't use.
- config.py: API settings, paths, models and agent settings.

## Commands

Run from the CritiqueAgentv3 folder. All of these call the API.

    python pipeline.py Data/Input_3 [--effort low] [--run-no 1] [--model-all <id>]
    python pipeline.py Data/Input_3 --reference [--model-all <id>] [--effort high]
    python compare_models.py Data/Input_3 --structured runs/_reference/REF-Input_3-... --repeats 3 [--effort low] [--models <id> <id>]
    python compare_models.py Data/Input_3_u --structured runs/_reference/REF-Input_3-... --repeats 3
    python oneshot.py Data/Input_3 [--model <id>] [--effort low] [--run-no 1]
    python compare_models.py Data/Input_3 --method oneshot --repeats 3 [--effort low] [--models <id> <id>]
    python review_reports.py [runs/<folder> ...] [--model <id>] [--overwrite]

--effort sets the reasoning effort for every agent (none, low, high or max, if the model supports it). Without it, REASONING in config.py is used.

## Output

runs/ holds pipeline and compare runs, runs_oneshot/ holds one-shot runs.

- Run folder: Input_X-Run_Y-Eff_Z-TIMESTAMP
- Compare folder: Compared-Input_X-Runs_Y-Eff_Z-TIMESTAMP, with one folder per model and a compare.csv
- Reference folder: runs/\_reference/REF-Input_X-RefModel_Y-RefEff_Z--TIMESTAMP

TIMESTAMP is YYMMDD-HHMMSS. Y is the run number (or runs per model), Z the reasoning effort. Model names drop the provider and replace characters Windows doesn't allow.

Each run folder has run.json, run.log, metrics.json, graded_rubric.json and report.md. The one-shot compare.csv has the same columns as the agents one; the reused columns are 0 and quote_found_rate is empty.

runs/\_pricing.json is the model pricing cache. compare_models.py refreshes it once per invocation; pipeline.py refreshes it when it is missing or older than 24 hours.

## Costs

Cost per call is the billed cost from the API response. If a response has no cost, it is estimated from the pricing cache.

Totals cover the whole pipeline for one submission, including the rubric and task calls reused from the reference. reused_cost_usd and reused_tokens give that reused share, so the money actually spent in a run is cost_usd minus reused_cost_usd. wall_s only covers the run itself.

legacy*pdf/ and oldruns/ are earlier attempts kept for reference. The older compare*\* folders in runs/ use the previous folder layout.
