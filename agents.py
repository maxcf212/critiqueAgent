"""Prompts and calls for the four pipeline agents: rubric, task, marking and feedback."""
from llm import call, minify, text_block

JSON_ONLY = "Reply with one JSON object only. No prose, no markdown."
OCR_NOTE = ("The document was converted to markdown by OCR: odd characters, broken LaTeX/tables and split paragraphs "
            "are usually conversion artefacts, not the author's errors.")

RUBRIC_SYS = f"""Convert the marking rubric below into JSON. {OCR_NOTE}
- ids C1..Cn in rubric order. Name stores title of criterion as well as any additional description. Marks are numbers; a single mark gives min=max.
- level min/max = the score range exactly as printed for that level (may be a common band scale, e.g. 0-10).
- weight = % of total if printed, else null. max = marks for the criterion if printed, else null. total = printed total marks, else null. Never infer or rescale numbers.
- If only % bands are given, use 0-100 for level min/max.
Schema: {{"title":str,"total":num|null,"criteria":[{{"id":"C1","name":str,"weight":num|null,"max":num|null,"levels":[{{"label":str,"min":num,"max":num,"desc":str}}]}}],"notes":str}}
{JSON_ONLY}"""

TASK_SYS = f"""Summarise the assessment task below into compact JSON for a marker. {OCR_NOTE}
Capture everything the student must do or submit, including requirements a rubric may omit
(length, format, sections, calculations, drawings, standards, units). Omit admin (dates, submission portals).
Schema: {{"title":str,"overview":str(<=80 words),"deliverables":[str],"format":{{"length":str,"structure":str,"other":str}},"requirements":[{{"id":"R1","text":str}}]}}
{JSON_ONLY}"""

MARK_SYS = f"""You are an expert engineering-design professor. Mark the student submission below against every rubric criterion.
- Choose the level whose descriptor best fits, then a whole-number mark within that level's range (no half marks).
- Judge technical correctness (calculations, assumptions, units, standards, design logic) with your own engineering knowledge.
- Figures appear as [Image N] followed by the image; assess them too.
- {OCR_NOTE} Don't penalise them unless clearly the student's error.
- Evidence: where = nearest section heading or "Image N"; quote = exact contiguous text, <=25 words, no ellipses ("" for an image). Never invent quotes; if evidence is missing say so in reasoning.
- Check each task requirement.
Schema: {{"criteria":[{{"id":str,"level":str,"mark":num,"evidence":[{{"where":str,"quote":str}}],"reasoning":str(<=80 words)}}],"requirements":[{{"id":str,"met":"yes|partial|no","where":str|null}}],"technical_issues":[{{"where":str,"issue":str}}],"overall":str(<=60 words)}}
{JSON_ONLY}"""

FEEDBACK_SYS = f"""Write formative feedback for a student from the assessor's marking. Address the student as "you".
Be specific, supportive and actionable: cite their sections/figures, name what they did well, and state what the next rubric level requires.
Do not change marks. Do not comment on document-conversion artefacts. Do not make up explanations for reasoning given by the marking agent, that is unclear or incomplete.
Schema: {{"summary":str(<=80 words),"next_steps":[str,str,str],"criteria":{{"<criterion id>":str(<=70 words)}}}}
{JSON_ONLY}"""


def structure_rubric(doc, cfg, step_dir, log):
    parts = [text_block("RUBRIC:\n"), *doc["parts"]]
    return call("rubric", cfg, RUBRIC_SYS, parts, step_dir, log)


def structure_task(doc, cfg, step_dir, log):
    parts = [text_block("TASK:\n"), *doc["parts"]]
    return call("task", cfg, TASK_SYS, parts, step_dir, log)


def mark(doc, rubric, task, cfg, step_dir, log):
    context = f"RUBRIC:{minify(rubric)}\nTASK:{minify(task)}\nSTUDENT SUBMISSION:\n"
    parts = [text_block(context), *doc["parts"]]
    return call("marking", cfg, MARK_SYS, parts, step_dir, log)


def feedback(graded, rubric, task, cfg, step_dir, log):
    task_summary = {key: task.get(key) for key in ("title", "overview")}
    context = (f"TASK:{minify(task_summary)}\n"
               f"RUBRIC:{minify(rubric.get('criteria', []))}\n"
               f"MARKING:{minify(graded)}")
    return call("feedback", cfg, FEEDBACK_SYS, [text_block(context)], step_dir, log)
