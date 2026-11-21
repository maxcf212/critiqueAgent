# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 90 / 100 (90%)**

An excellent preliminary report. Your Great Barrier Reef monitoring mission is clearly justified with quantified objectives, explicit users, and good referencing. Your Gantt plan is robust, with contingency triggers and a clear rationale tied to mission logic. Your verified orbit calculations and STK start show strong progress, and presentation is polished. To reach the very top, strengthen trade justification (why a new mission over existing satellites) and quantify downlink/data-volume needs.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Accomplished (9/10). Your mission goal, four quantified objectives, users (AIMS as operator, GBRMPA as customer) and their needs are clearly stated and traced back to user requirements, with good literature support ([1]-[6]). To fully secure the top level, briefly argue why a new satellite is needed compared with existing missions such as Sentinel-2.

*Assessor reasoning:* Clear mission goal, four quantified objectives, explicit users and their needs, and objectives traced back to user requirements. Well referenced to literature ([1]-[6]). Only minor gap: no discussion of why a new satellite beats existing missions (e.g. Sentinel-2).
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS). Its customers are the Great Barrier Reef Marine Park Authority"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Accomplished (9/10). Your Gantt chart (Figure 1) with task descriptions, float, and the risk/contingency table (Table 1) with triggers and responses is robust, and you clearly explain why tasks are ordered by mission logic (imaging requirements fix orbit before ground control). Information sources are tabulated (Table 2). Adding a weekly hour budget would complete the plan.

*Assessor reasoning:* Gantt chart with task descriptions, explicit rationale linking plan order to mission logic, float, and a risk/contingency table with triggers and responses. Information sources table included. Robust and mission-integrated; only slight weakness is no stated weekly hour budget.
> Project Plan: "Project work is divided into weeks in the Gantt chart in Figure 1, and each task is described below it."  
> Project Plan: "The order follows the mission: the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time, so orbit work comes before ground control"  
> Project Plan: "Table 1: Project risks and contingency plans."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (9/10, Accomplished)

Accomplished (9/10). Your hand calculations are verified: a=6978 km gives T=5801 s, 14.9 orbits/day, sun-sync inclination 97.8° at 600 km, and a 24.2° ground-track shift using the sidereal day. You interpret the swath-vs-revisit trade, tie results to contingencies, and have started an STK scenario that agrees with your hand calculation. Clearly on track for completion.

*Assessor reasoning:* Verified hand calculations: a=6978 km gives T=5801 s (correct), 14.9 orbits/day, sun-sync inclination 97.8° at 600 km (correct), 24.2° ground-track shift using the sidereal day (correct). Results are interpreted (swath vs revisit trade) and tied to contingencies; STK tutorials and a scenario started. Clearly on track.
> Preliminary Progress: "Table 3: Preliminary hand calculations for the candidate orbit."  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution."  
> Preliminary Progress: "A first STK scenario with this orbit has been set up, and its period agrees with the hand calculation."  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has a logical structure with clear headings, labelled figures and tables with captions (e.g. Figure 1, Table 3), consistent formatting, professional tone, and in-text citations ([1]-[11]) matching the reference list. Writing is clear and concise. Minor improvement: complete full titles and author details for some references.

*Assessor reasoning:* Logical structure with clear headings, labelled figures and tables with captions, consistent formatting, professional tone, and in-text citations ([1]-[11]) matching the reference list. Writing is clear and concise throughout. Very minor: some references lack full titles/author detail.
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds., Space Mission Engineering: The New SMAD."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan / Preliminary Progress — launch, orbit and ground segment stages tied to course astrodynamics material and orbit calculations |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan — 'The design will be completed in STK (Systems Tool Kit), accessed remotely through the MECH lab 204 licence.' |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan — Gantt chart (Figure 1) with task descriptions and deadlines |
| R5 | List the information sources you plan to use. | yes | Project Plan — Table 2: Planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress — orbit hand calculations, STK tutorials, and swath/revisit interpretation |

## Technical issues

- Mission Concept & Rationale: 10 m GSD weekly imaging of a 2300 km reef is a demanding requirement; data volume and downlink rate needed to meet the 24-hour delivery objective are not yet quantified (acknowledged as future work via contingencies).
- Preliminary Progress: Sun-synchronous orbit choice is not yet justified against local time of node, which matters for consistent illumination of colour-change detection.

## Next steps

1. Justify the sun-synchronous orbit choice against local time of node, since consistent illumination matters for coral colour-change detection.
2. Quantify the data volume and downlink rate needed to meet your 24-hour delivery objective for 10 m GSD weekly imaging of the 2300 km reef.
3. Add a brief comparison with existing missions (e.g. Sentinel-2) to explain why a new satellite is needed, and complete reference details (titles/author info) where missing.

---
<sub>Run Input_1_u-Run_2-Eff_high-261116-123222 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 9665/4060 | cost $0.002122 (incl. $0.001072 for the reused reference rubric+task structure) | 57.22s</sub>
