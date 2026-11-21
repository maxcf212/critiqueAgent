# Input_1_d - what was changed (NOT sent to any model)

DEGRADED / poisoned ("_d") variant of `Input_1`. `Rubric_1.md`, `Task_1.md` are byte-identical copies of the originals; only the solution differs (`Solution_1_d.md`, derived from `Input_1/Solution_1.md`).

Four defects were injected into the original report. Nothing else is changed (same Gantt chart image).

**Basis for the edits:** Defects cover false claims, an omitted requirement and a text-versus-figure inconsistency, and are all checkable from the submission, the task and general engineering knowledge.

**Expected effect on marking:** Lower than the original (human mark 89/100): C1 loses for the impossible statistics, C2 for the missing source list and the plan that contradicts its own Gantt chart, C3/C1 for the geostationary error.

| ID | Type | Where | Change | Why / what a marker should notice |
|---|---|---|---|---|
| P1 | false claim (impossible figures) | Mission Concept & Rationale, paragraph 2 | Bleaching losses changed from 30% (2016) and 20% (2017) to 60% and 50% | 60% + 'another 50 percent' of the reef's coral is 110%, which is impossible; the cited source gives 30% and 20% |
| P2 | false claim (technical) | Project plan, 'Orbit Specifics' task | Added a statement that the chosen orbit is 'a geostationary orbit at an altitude of 600 km' that keeps the satellite fixed above the reef | A geostationary orbit is at about 35,786 km altitude over the equator; a 600 km orbit has a period of about 97 minutes and cannot stay fixed over the reef |
| P3 | inconsistency with figure | Project plan, 'Editing & Finalisation' task | 'Week 10 is reserved for review' changed to 'Weeks 7 and 8 are reserved for review' | The Gantt chart (image) shows Editing & Finalisation in Weeks 9 and 10, and the text still says design and simulation finish at the end of Week 9, i.e. after the review weeks. Needs the figure to be read |
| P4 | omitted requirement | end of report | The whole 'Useful Links' section (list of nine planned information sources) deleted | Task: 'list the sources of information you plan to use'; rubric C2: 'information sources you plan to use'. Only the four footnotes that support the rationale remain |

## Exact text changes

### P1 - Mission Concept & Rationale, paragraph 2

Original:

> In 2016, a bleaching killed 30 percent of the reef’s coral. In 2017, another 20 percent perished.²

Changed to:

> In 2016, a bleaching killed 60 percent of the reef’s coral. In 2017, another 50 percent perished.²

### P2 - Project plan, 'Orbit Specifics' task

Original:

> **Orbit Specifics:** I will need to choose an optimal orbit path and altitude, and also calculate COEs & AOEs.

Changed to:

> **Orbit Specifics:** My current choice is a geostationary orbit at an altitude of 600 km, which keeps the satellite fixed above the reef at all times. I will also calculate COEs & AOEs.

### P3 - Project plan, 'Editing & Finalisation' task

Original:

> **Editing & Finalisation:** Week 10 is reserved for review, amendments, final simulations, and reflection.

Changed to:

> **Editing & Finalisation:** Weeks 7 and 8 are reserved for review, amendments, final simulations, and reflection.

### P4 - end of report

Original:

> ## Useful Links https://coralreefwatch.noaa.gov/satellite/publications/nim_skirving_reef_vulnerability.pdf https://wwf.panda.org/our_work/our_focus/oceans_practice/coasts/coral_reefs/ http://www.gbrmpa.gov.au/the-reef/reef-facts https://oceanservice.noaa.gov/facts/coralreef-climate.html https://www.nationalgeographic.com/magazine/2018/08/explore-atlas-great-barrier-reef-coral-b [...] 6b-6fb6-443e-b84b-86b0bbdb53ac

Changed to:

> (deleted)
