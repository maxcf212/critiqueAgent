# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 100 / 100 (100%)**

You have produced an exemplary preliminary report that thoroughly addresses all deliverables. In Mission Concept & Rationale, you clearly linked quantitative mission objectives to stakeholder needs (AIMS, GBRMPA). Your Project Plan features an effective Gantt chart and robust risk contingencies (Table 1), while Preliminary Progress demonstrates sound orbital analysis and trade-off insights. Addressing a minor technical nuance in your orbit model will position you well for the final report.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 10 / 10 | 40 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 10 / 10 | 30 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 10 / 10 | 10 / 10 |
| C4 Report presentation | Accomplished | 10 / 10 | 20 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (40/40, Accomplished)

Excellent work in Mission Concept & Rationale. You articulated clear, measurable objectives and directly linked satellite capabilities to end users such as AIMS and GBRMPA with relevant literature citations. To maintain this Accomplished standard in the final design report, ensure that all detailed subsystem requirements trace directly back to these primary mission and user needs.

*Assessor reasoning:* The mission goal, objectives, and quantitative requirements are clearly defined and directly tied to end-user needs (AIMS, GBRMPA, CSIRO, BoM). Relevant literature is thoroughly cited.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef, so that bleaching is detected within days"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (30/30, Accomplished)

Your Project Plan is robust and integrates cleanly with your mission narrative. You provided clear task sequencing, a readable Gantt chart, and a thorough contingency matrix in Table 1. To maintain this Accomplished level in Part 2, track your actual task completion against these planned milestones and document any contingency plans you trigger.

*Assessor reasoning:* The project plan includes a well-structured Gantt chart, task narratives explaining design sequencing, a comprehensive contingency table, and a detailed list of planned information sources.
> Project Plan: "The main risks and the planned responses are listed in Table 1."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (10/10, Accomplished)

You demonstrated strong technical progress with your 600 km sun-synchronous orbit calculations and clear interpretation of the swath-to-reef-width trade-off. To refine your Accomplished work for the final submission, adjust your nodal ground-track shift calculations to reference the solar day (86,400 s) instead of the sidereal day (86,164 s), correcting the minor ~8 km discrepancy.

*Assessor reasoning:* Preliminary hand calculations for a 600 km sun-synchronous orbit are technically sound. The interpretation insightfully identifies the core coverage-swath trade-off against mission requirements.
> Preliminary Progress: "Interpretation: the reef is up to about 250 km wide, so a 60 km swath needs at least five neighbouring passes"  

### C4 Report presentation (20/20, Accomplished)

The presentation is exemplary. The report follows a logical structure with clean formatting, professional tables and charts, and accurate citations that consistently match the reference list. To maintain this Accomplished standard in your final assignment, ensure that complex subsystem schematics, budget tables, and simulation figures match this high level of clarity and consistent styling.

*Assessor reasoning:* The report is professionally written and structured, with clean formatting, clear tables, an effective Gantt chart, and accurate, consistently formatted reference citations.
> References: "[1] NOAA, "Ocean acidification," 2020. [Online]. Available: https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification. [Accessed: 28 Sep. 2020]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan |
| R5 | List the information sources you plan to use. | yes | Project Plan |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress |

## Technical issues

- Preliminary Progress: For a sun-synchronous orbit, ground-track shift between consecutive nodal crossings is relative to the sun-pointing frame, which corresponds to the solar day (86,400 s) rather than the sidereal day (86,164 s), though the resulting difference is minor (~8 km).

## Next steps

1. In your full mission orbital analysis, calculate the sun-synchronous ground-track shift using the solar day (86,400 s) rather than the sidereal day (86,164 s) to resolve the ~8 km difference.
2. Expand your swath-width trade-off analysis in Preliminary Progress by evaluating constellation or off-nadir pointing options to cover the 250 km reef width within the required revisit time.
3. Maintain your project momentum by tracking progress and updating mitigation outcomes directly against the milestones and contingencies defined in Table 1.

---
<sub>Run Input_1_u-Run_2-Eff_high-261116-123426 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 9166/7775 | cost $0.026658 (incl. $0.001072 for the reused reference rubric+task structure) | 44.41s</sub>
