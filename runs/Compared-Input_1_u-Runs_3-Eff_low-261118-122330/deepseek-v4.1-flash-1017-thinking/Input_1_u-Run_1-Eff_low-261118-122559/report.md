# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 98 / 100 (98%)**

Your preliminary report is strong and concise: a well-argued Australian-benefit mission, clear users and requirements, a Gantt chart with contingencies and sources, and correct orbit hand calculations feeding a real coverage trade. Minor weaknesses are referencing and an optimistic revisit analysis. You are at Accomplished for C1, C2 and C4, and solidly Accomplished for C3.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 10 / 10 | 40 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 10 / 10 | 30 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 10 / 10 | 20 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (40/40, Accomplished)

You clearly state the mission goal, four numbered objectives with quantitative requirements, named operator/users, and trace needs to objectives with citations. To consolidate at Accomplished, replace the Nature news item behind the 10 m GSD with a satellite or bleaching-sensitivity study, and correct the 100 m/pixel satellite claim by citing [3] as a compiled depth model.

*Assessor reasoning:* Clear goal, four numbered objectives with quantitative requirements, explicitly named operator and users with needs traced back to objectives, and literature citations throughout. Weakness: the 10 m GSD requirement rests on a Nature news item about airborne mapping rather than a satellite-derived sensitivity study.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef, so that bleaching is detected within days"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS). Its customers are the Great Barrier Reef Marine Park Authority"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (30/30, Accomplished)

Your Gantt chart, task descriptions sequenced by mission logic, risk/contingency table with triggers, and information-source table are strong; software choice is justified. To stay at the top of Accomplished, tie specific orbit and launch numbers to the schedule, closing the minor gap where the plan lacks those concrete inputs.

*Assessor reasoning:* Gantt chart plus task descriptions sequenced by mission logic (imaging requirements drive orbit, then ground/comms, EOL after orbit), a risk/contingency table with triggers, and an information-source table. Software choice justified. Minor gap: no specific orbit/launch numbers yet tied to the schedule.
> Project Plan: "Project work is divided into weeks in the Gantt chart in Figure 1, and each task is described below it"  
> Project Plan: "Week 10 is float as well as editing time: no new design work is planned in it."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Your hand calculations are correct (T=5,801 s, 14.9 orbits/day, 97.8° SSO, 2,700 km spacing, 60 km swath) and interpreted against coverage, feeding a contingency. To move toward the top of Accomplished, add an aperture/IFOV and diffraction check plus a data-rate/downlink budget, and revise the optimistic five-pass/one-week coverage interpretation.

*Assessor reasoning:* Hand calculations are correct (T = 5,801 s, 14.9 orbits/day, 97.8 deg SSO, 2,700 km track spacing, 60 km swath) and are interpreted against the coverage requirement, feeding a contingency. Depth is modest — one orbit only, no optical/aperture check — but clearly on track.
> Preliminary Progress: "a circular sun-synchronous orbit at 600 km altitude (Table 3), using μ = 398,600 km³/s² and an Earth radius of 6,378 km"  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution."  

### C4 Report presentation (20/20, Accomplished)

Logical structure, concise professional prose, labelled consistent figures/tables, and an IEEE-style reference list with matching in-text citations. To secure Accomplished, give reference [11] an author and replace news article [4] with a technical source; these are small lapses rather than structural issues.

*Assessor reasoning:* Logical structure, concise professional prose, labelled and consistent figures/tables, IEEE-style reference list whose entries all appear in text and vice versa. Small lapses: reference [11] has no author, and [4] is a news article cited as a technical source.
> Project Plan: "Table 1: Project risks and contingency plans."  
> Preliminary Progress: "Table 3: Preliminary hand calculations for the candidate orbit."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan / Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan, Figure 1 |
| R5 | List the information sources you plan to use. | yes | Project Plan, Table 2 |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress, Table 3 |

## Technical issues

- Mission Concept & Rationale: 10 m GSD requirement justified by a Nature news piece on airborne (CAO) mapping, not a satellite performance or bleaching-detection sensitivity study.
- Mission Concept & Rationale: Statement that satellites map GBR depths only to 100 m/pixel misreads source [3], which is a compiled depth model (gbr100), not a satellite product.
- Preliminary Progress: Coverage interpretation understates the problem: with ~2,700 km between same-day tracks and a 60 km swath, five passes across a 250 km-wide reef would take weeks, not one week.
- Preliminary Progress: No aperture/IFOV, diffraction, data-rate or downlink budget check to confirm 10 m GSD from 600 km is achievable with the stated 6,000-pixel swath.

## Next steps

1. Replace the Nature news item supporting the 10 m GSD with a satellite performance or bleaching-detection sensitivity study, and correct the statement that satellites map the GBR only to 100 m/pixel by citing [3] as a compiled depth model.
2. Strengthen Preliminary Progress by adding an aperture/IFOV and diffraction check, plus a data-rate/downlink budget, to confirm 10 m GSD from 600 km with a 6,000-pixel swath; revisit the five-pass coverage claim—2,700 km track spacing and 60 km swath imply weeks, not one week.
3. Tighten presentation: give reference [11] an author and replace news article [4] with a technical source; in the Project Plan, tie specific orbit/launch numbers to the schedule to close the minor gap noted.

---
<sub>Run Input_1_u-Run_1-Eff_low-261118-122559 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8943/6042 | cost $0.004082 (incl. $0.001072 for the reused reference rubric+task structure) | 27.31s</sub>
