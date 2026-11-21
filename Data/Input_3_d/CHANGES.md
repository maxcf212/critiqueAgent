# Input_3_d - what was changed (NOT sent to any model)

DEGRADED / poisoned ("_d") variant of `Input_3`. `Rubric_3.md`, `Task.md` are byte-identical copies of the originals; only the solution differs (`Solution_3_d.md`, derived from `Input_3/Solution_3.md`).

Five defects were injected into the original report. All of its original weaknesses (no visuals, typos, incomplete references) are still present.

**Basis for the edits:** Defects cover an omitted requirement, false claims, a calculation error and a logical contradiction; each is checkable from the task sheet, the report's own text or common knowledge.

**Expected effect on marking:** Lower than the original (mean 76/100): C5 loses for the missing abstract, C4 for the false and invented evidence, C2/C3 because recommendation 1 contradicts the conclusion.

| ID | Type | Where | Change | Why / what a marker should notice |
|---|---|---|---|---|
| P1 | omitted requirement | Abstract | The whole abstract (heading and paragraph) deleted | Task format: 'The report must include an abstract of around 150 words'; rubric C5: appropriate sections including abstract |
| P2 | false claim (case fact) | Discussion, first argument for shipping | 'six-month product release cycle' changed to 'two-year product release cycle' | The task scenario says a new server is released about every six months, and the report itself later says 'short six-month product cycle' |
| P3 | calculation error | Discussion, risk of harm paragraph | Inserted sentence: 'If even 1 percent of the 5,000 servers in the contract failed, that would be 500 failed servers in hospitals.' | 1 percent of 5,000 is 50, not 500. The figure of 5,000 servers is also invented: the task gives no contract size |
| P4 | false claim (external case) | The Most Ethical Path, Volkswagen paragraph | 'diesel vehicles ... to manipulate emissions tests' changed to 'electric vehicles ... to manipulate crash-safety tests' | The Volkswagen scandal concerned diesel emissions tests; the report's own reference [4] is titled 'Diesel Emissions Cheating Scheme' |
| P5 | contradiction (recommendation vs conclusion) | Recommendation 1 | 'Rachel should refuse the contract' changed to 'Rachel should accept the contract' | The abstract (removed), discussion and conclusion all argue 'Not to Ship'; recommendation 1 now says the opposite, and recommendations 2-4 no longer follow from it |

## Exact text changes

### P1 - Abstract

Original:

> #### ABSTRACT This report examines an ethical dilemma for a quality assurance engineer who must choose whether or not to ship out potentially defective products. The case is first analysed from both sides ‘To Ship’ and ‘Not to Ship’, using examples of real-world case studies and the Engineers Australia Code of Ethics. After analysis of the pros (competitive advantage, revenue i [...] nt communication with clients.

Changed to:

> (deleted)

### P2 - Discussion, first argument for shipping

Original:

> If the six-month product release cycle is maintained

Changed to:

> If the two-year product release cycle is maintained

### P3 - Discussion, risk of harm paragraph

Original:

> defective servers could lead to disruptions in emergency services and patient care in hospitals.

Changed to:

> defective servers could lead to disruptions in emergency services and patient care in hospitals. If even 1 percent of the 5,000 servers in the contract failed, that would be 500 failed servers in hospitals.

### P4 - The Most Ethical Path, Volkswagen paragraph

Original:

> in a large amount of its diesel vehicles worldwide to manipulate emissions tests [4]

Changed to:

> in a large amount of its electric vehicles worldwide to manipulate crash-safety tests [4]

### P5 - Recommendation 1

Original:

> 1. Rachel should refuse the contract with the government health department.

Changed to:

> 1. Rachel should accept the contract with the government health department.
