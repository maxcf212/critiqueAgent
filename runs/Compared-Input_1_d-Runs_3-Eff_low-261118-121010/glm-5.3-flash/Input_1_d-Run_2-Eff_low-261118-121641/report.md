# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 51 / 100 (51%)**

Your Great Barrier Reef monitoring mission is well motivated, with clear users and a solid week-by-week Gantt plan. To reach the next level, state explicit quantitative mission requirements, correct the orbit altitude error, add contingencies to your plan, present preliminary technical results from STK, and adopt a formal referencing style.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Adequate | 5 / 10 | 20 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Adequate | 5 / 10 | 15 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 6 / 10 | 12 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (20/40, Adequate)

You clearly describe the mission purpose (GBR bleaching monitoring), users (marine and conservation scientists) and need, supported by literature. To reach Accomplished, state explicit mission goals, objectives and requirements — e.g. resolution, revisit time, swath, data latency — and connect each requirement to user needs, with referenced justification.

*Assessor reasoning:* Clear mission purpose (GBR bleaching monitoring), users (marine/conservation scientists) and need are described with literature citations. However, no explicit mission objectives or requirements are stated, and details of the mission architecture are thin.
> Mission Concept & Rationale: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (15/30, Adequate)

Your week-by-week Gantt chart with detailed task descriptions fits the mission narrative well. To reach Accomplished, add contingency and variation provisions (schedule buffers, fallback tasks) and a consolidated, referenced list of information sources and software, explaining why the plan is structured this way.

*Assessor reasoning:* Detailed week-by-week Gantt chart with task descriptions covering launch, orbit, ground control, comms and STK work; plan fits the mission narrative. No provision for contingencies/variations, and information sources are only the four URLs plus implied course/STK material.
> Project Plan & Preliminary Progress: "Project work will be divided into weeks via a Gantt Chart. Detailed task descriptions can be found on the next page."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (4/10, Adequate)

Progress is currently limited to research and STK tutorials 1–4, with no technical results. To reach Accomplished, present preliminary outputs — e.g. candidate orbit parameters, coverage or revisit analysis, or a link budget — with brief description and interpretation showing you are on track.

*Assessor reasoning:* Progress is limited to background research and completing STK tutorials; no preliminary technical results (orbit parameters, coverage, link budgets) are presented or interpreted. On track, but only minor technical work demonstrated.
> Project Plan & Preliminary Progress: "completed STK tutorials 1, 2, 3 & 4"  

### C4 Report presentation (12/20, Adequate)

Your report is well written with clear headings and a labelled Gantt figure. To reach Accomplished, use a consistent formal citation style with a reference list matching in-text citations, replace bare footnoted URLs, and strengthen figure captions and formatting consistency throughout.

*Assessor reasoning:* Clear headings, readable and well-written prose, labelled Gantt figure with legend. References are cited as bare URLs in footnotes with no formal reference list, and figure caption/labelling is minimal — not professional level but adequate.
> Mission Concept & Rationale: "¹ https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | partial | Project Plan & Preliminary Progress — launch/orbit tasks planned, but orbit description contains a major technical error |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan & Preliminary Progress — 'STK Design & Simulations' indicates STK selected |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Image 1 Gantt chart with weekly schedule |
| R5 | List the information sources you plan to use. | partial | Footnoted URLs in Mission Concept & Rationale; no consolidated list of planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | partial | Project Plan & Preliminary Progress — STK tutorials and research only, no technical results |

## Technical issues

- Project Plan & Preliminary Progress: 'geostationary orbit at an altitude of 600 km, which keeps the satellite fixed above the reef' — geostationary altitude is ~35,786 km; 600 km is LEO and cannot be fixed above the reef. Also GEO is poor for high-resolution reef imaging.
- Mission Concept & Rationale: No quantitative mission requirements or objectives (resolution, revisit time, swath) despite citing a 100 m/pixel mapping gap.

## Next steps

1. Add a requirements table with quantitative values (e.g. spatial resolution, revisit time, swath, latency) linked to the 100 m/pixel mapping gap you cite, and derive mission objectives from them.
2. Correct the orbit description: geostationary altitude is ~35,786 km; 600 km is LEO and cannot keep the satellite fixed above the reef. Justify an orbit choice suited to high-resolution reef imaging (e.g. LEO with appropriate revisit).
3. Extend your Gantt plan with contingency provisions (delays, software issues, task slippage) and add a consolidated list of planned information sources.
4. Produce preliminary STK results — orbit parameters, coverage/revisit analysis or link budget — with brief interpretation, beyond tutorial completion.
5. Replace footnoted bare URLs with a formal citation style and a matching reference list, and improve figure captions and labelling.

---
<sub>Run Input_1_d-Run_2-Eff_low-261118-121641 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 7660/3290 | cost $0.001825 (incl. $0.001072 for the reused reference rubric+task structure) | 47.69s</sub>
