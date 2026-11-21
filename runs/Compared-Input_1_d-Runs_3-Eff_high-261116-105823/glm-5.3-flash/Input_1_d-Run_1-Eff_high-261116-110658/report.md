# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 59 / 100 (59%)**

You presented a well-motivated reef-monitoring mission with clearly identified users, a detailed week-by-week Gantt chart, and evidence of STK tutorial progress. To reach the accomplished level, you need explicit mission objectives and requirements, a corrected orbit concept, contingency planning, a dedicated source list, and preliminary technical results with interpretation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Adequate | 6 / 10 | 24 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Adequate | 6 / 10 | 18 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 6 / 10 | 12 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (24/40, Adequate)

Your concept clearly states purpose, users (marine and conservation scientists) and need, supported by four literature citations. To reach Accomplished, add explicit mission goals, objectives and requirements (payload, resolution, coverage, lifetime), resolve the imaging-vs-relay architecture ambiguity, and correct the orbit description.

*Assessor reasoning:* Clear purpose, users (marine/conservation scientists) and need, with four literature citations. However, no explicit mission objectives/requirements (payload, resolution, coverage, lifetime), and the orbit concept contains a fundamental error, so not fully accomplished.
> Mission Concept & Rationale: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (18/30, Adequate)

Your Gantt chart with weekly tasks tied to mission stages is detailed and feasible. To reach Accomplished, add provision for variations and contingencies, explain why the plan is structured this way in the mission context, and include a dedicated list of planned information sources.

*Assessor reasoning:* Detailed Gantt chart with week-by-week tasks tied to mission stages (launch, orbit, ground, comms, end-of-life). Lacks contingency/variations provision and no dedicated list of planned information sources; sources only appear as concept footnotes.
> Project Plan & Preliminary Progress: "Project work will be divided into weeks via a Gantt Chart. Detailed task descriptions can be found on the next page."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (5/10, Adequate)

You show genuine progress: concept drafted, background research on Asner's imaging approach, and STK tutorials 1–4 completed. To reach Accomplished, present a preliminary set of technical results (e.g. orbit parameters, coverage or simulation outputs) with brief description and interpretation.

*Assessor reasoning:* Evidence of progress: mission concept drafted, background research on Asner's imaging approach, STK tutorials completed. However, no preliminary technical results (orbit parameters, coverage calcs, simulations) are presented or interpreted.
> Project Plan & Preliminary Progress: "completed STK tutorials 1, 2, 3 & 4"  

### C4 Report presentation (12/20, Adequate)

Your report is well-written with a logical structure, clear headings and a labelled Gantt chart. To reach Accomplished, replace footnote URLs with a proper reference list matching in-text citations, and expand the report with more figures and tables presented consistently.

*Assessor reasoning:* Well-written, logical structure with headings, clear labelled Gantt chart. But references are footnote URLs with no reference list, and the report is brief (~2 pages) with limited figures/tables, so not at the accomplished professional level.
> Mission Concept & Rationale: "¹ https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | partial | Project Plan & Preliminary Progress — Launch/Orbit Specifics tasks relate to space segment, but 'geostationary orbit at an altitude of 600 km' is technically wrong |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan & Preliminary Progress — 'STK Design' and 'STK Simulations' tasks; STK tutorials completed |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Image 1 — Gantt chart with weekly schedule and task descriptions |
| R5 | List the information sources you plan to use. | partial | Mission Concept & Rationale — four source URLs cited, but no list of planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | partial | Project Plan & Preliminary Progress — research and STK tutorials done, but no preliminary technical results shown |

## Technical issues

- Project Plan & Preliminary Progress (Orbit Specifics): States 'geostationary orbit at an altitude of 600 km, which keeps the satellite fixed above the reef' — geostationary orbit requires ~35,786 km altitude; 600 km is LEO and cannot remain fixed over the reef. Also, GEO would give poor resolution for reef imaging.
- Mission Concept & Rationale: Concept conflates an imaging satellite (Asner-style seafloor colour detection) with a near-real-time communications relay; payload/mission architecture is not defined.

## Next steps

1. Correct the orbit error: a geostationary orbit requires ~35,786 km altitude; 600 km is LEO and cannot keep the satellite fixed above the reef. Reconsider orbit choice against imaging resolution and coverage needs.
2. Define explicit mission objectives and requirements (payload type, resolution, coverage, revisit rate, lifetime) and clarify whether the mission is imaging, communications relay, or both.
3. Add contingency provisions to your Gantt chart and a dedicated list of planned information sources and software, replacing footnote URLs with a proper reference list.
4. Include preliminary technical results — e.g. orbit parameters, coverage or link-budget calculations, or initial STK simulation outputs — with brief interpretation.

---
<sub>Run Input_1_d-Run_1-Eff_high-261116-110658 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 7711/3925 | cost $0.002309 (incl. $0.001072 for the reused reference rubric+task structure) | 68.08s</sub>
