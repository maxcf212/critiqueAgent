"""The four agents. Prompts are deliberately terse; inter-agent JSON is minified to save tokens."""
from llm import call, minify, pdf_content, text_block

_JSON = "Reply with one JSON object only. No prose, no markdown."

RUBRIC_SYS = f"""Convert the attached marking rubric into JSON. Keep descriptor meaning; condense wording.
- ids C1..Cn in rubric order. Marks are numbers; a single mark gives min=max.
- level min/max = the score range exactly as printed for that level (may be a common band scale, e.g. 0-10).
- weight = % of total if printed, else null. max = marks for the criterion if printed, else null. total = printed total marks, else null. Never infer or rescale numbers.
- If only % bands are given, use 0-100 for level min/max.
Schema: {{"title":str,"total":num|null,"criteria":[{{"id":"C1","name":str,"weight":num|null,"max":num|null,"levels":[{{"label":str,"min":num,"max":num,"desc":str}}]}}],"notes":str}}
{_JSON}"""

TASK_SYS = f"""Summarise the attached assessment task into compact JSON for a marker.
Capture everything the student must do or submit, including requirements a rubric may omit
(length, format, sections, calculations, drawings, standards, units). Omit admin (dates, submission portals).
Schema: {{"title":str,"overview":str(<=80 words),"deliverables":[str],"format":{{"length":str,"structure":str,"other":str}},"requirements":[{{"id":"R1","text":str}}]}}
{_JSON}"""

MARK_SYS = f"""You are an expert engineering-design assessor. Mark the attached student submission against every rubric criterion.
- Choose the level whose descriptor best fits, then a mark within that level's range.
- Judge technical correctness (calculations, assumptions, units, standards, design logic) with your own engineering knowledge.
- Evidence: page = the [Page N] label / PDF page number (1-based), not the printed page number; quote = exact contiguous text, <=25 words, no ellipses. Never invent quotes; if evidence is missing say so in reasoning.
- Check each task requirement.
Schema: {{"criteria":[{{"id":str,"level":str,"mark":num,"evidence":[{{"page":int,"quote":str}}],"reasoning":str(<=60 words)}}],"requirements":[{{"id":str,"met":"yes|partial|no","page":int|null}}],"technical_issues":[{{"page":int,"issue":str}}],"overall":str(<=50 words)}}
{_JSON}"""

FEEDBACK_SYS = f"""Write formative feedback for a student from the assessor's marking. Address the student as "you".
Be specific, supportive and actionable: cite their pages, name what they did well, and state what the next rubric level requires. Do not change marks.
Schema: {{"summary":str(<=80 words),"criteria":{{"<criterion id>":str(<=70 words)}},"next_steps":[str,str,str]}}
{_JSON}"""


def structure_rubric(pdf, cfg, step_dir, log):
    return call("rubric", cfg, RUBRIC_SYS, [*pdf_content(pdf, cfg["pdf_mode"]), text_block("Rubric attached.")],
                step_dir, log)


def structure_task(pdf, cfg, step_dir, log):
    return call("task", cfg, TASK_SYS, [*pdf_content(pdf, cfg["pdf_mode"]), text_block("Task attached.")],
                step_dir, log)


def mark(pdf, rubric, task, cfg, step_dir, log):
    ctx = f"Student submission attached.\nRUBRIC:{minify(rubric)}\nTASK:{minify(task)}"
    return call("marking", cfg, MARK_SYS, [*pdf_content(pdf, cfg["pdf_mode"]), text_block(ctx)], step_dir, log)


def feedback(graded, rubric, task, cfg, step_dir, log):
    ctx = (f"TASK:{minify({k: task.get(k) for k in ('title', 'overview')})}\n"
           f"RUBRIC:{minify(rubric.get('criteria', []))}\n"
           f"MARKING:{minify(graded)}")
    return call("feedback", cfg, FEEDBACK_SYS, [text_block(ctx)], step_dir, log)
