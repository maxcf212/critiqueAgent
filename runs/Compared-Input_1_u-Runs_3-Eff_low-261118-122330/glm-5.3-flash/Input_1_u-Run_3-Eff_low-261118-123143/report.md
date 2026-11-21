# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 89 / 100 (89%)**

An excellent preliminary report on your Great Barrier Reef coral-bleaching monitoring mission. Your quantified objectives, user-driven rationale, robust Gantt plan with contingencies, and verified orbit hand calculations all reached the Accomplished level. You are clearly on track for the full assignment; the main next steps are a top-level requirements table and addressing latitude-dependent coverage and payload demands.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Accomplished (9/10). Your mission goal is clear, with four quantified objectives explicitly traced to users (AIMS, GBRMPA, CSIRO, BoM) and their needs, supported by literature [1]–[6]. To reach the very top, add an explicit top-level requirements table linking requirements to objectives and users, and begin addressing the payload demand implied by 10 m GSD from 600 km.

*Assessor reasoning:* Clear goal, four quantified objectives, users (AIMS, GBRMPA, CSIRO, BoM) tied to needs, and literature cited [1]-[6]. Objectives explicitly traced to user needs. Only minor gap: no explicit top-level requirements table, but essentially complete.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "Its customers are the Great Barrier Reef Marine Park Authority, which needs up-to-date bleaching maps"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Accomplished (9/10). Your Gantt chart (Figure 1) is well structured, with Week 10 float, an explicit contingencies table with triggers and responses, and plan logic justified by the mission (orbit work before ground control because imaging requirements fix altitude and local time). Table 2 identifies information sources well. Next level: deepen contingency quantification and link each source to specific analysis tasks.

*Assessor reasoning:* Gantt chart with task descriptions, explicit contingencies table with triggers/responses, and plan logic tied to mission objectives. Information sources table included. Robust and well-justified.
> Project Plan: "Week 10 is float as well as editing time: no new design work is planned in it"  
> Project Plan: "the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time, so orbit work comes before ground control"  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Accomplished (8/10). Your hand calculations are correct (a = 6978 km, T = 5801 s, i = 97.8° SSO, 24.2° track shift), STK tutorials are complete, and you interpreted results and identified the weekly-coverage trade. To strengthen further, extend the coverage analysis to latitude-dependent revisit across the GBR and include cloud constraints, not just the equatorial shift.

*Assessor reasoning:* Hand calculations verified correct (a=6978 km, T=5801 s, i=97.8° SSO, 24.2° track shift), STK tutorials done, scenario set up, and results interpreted with a design trade identified. Strong progress with interpretation.
> Preliminary Progress: "Period | T = 2π√(a³/μ) | 5,801 s = 96.7 min"  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution"  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has a logical structure, clearly labelled figures and tables (e.g., Figure 1 with a descriptive caption), consistent IEEE-style citations matching the reference list, and professional writing. Minor improvement: complete the few reference entries missing titles and dates for full consistency.

*Assessor reasoning:* Logical structure, labelled figures/tables, consistent IEEE-style citations matching reference list, professional writing. Minor: some references lack titles/dates, but overall presentation is professional.
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Preliminary Progress — orbit hand calculations, launch/orbit tasks in plan |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan — 'The design will be completed in STK' |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan — Figure 1 Gantt chart |
| R5 | List the information sources you plan to use. | yes | Project Plan — Table 2 planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress — Table 3 hand calculations and STK setup |

## Technical issues

- Preliminary Progress: Ground-track shift quoted at equator only; swath/coverage analysis ignores latitude dependence and cloud constraints on weekly revisit, though this is acknowledged as an open trade.
- Mission Concept & Rationale: 10 m GSD for colour-based bleaching detection from a 600 km orbit implies a demanding payload not yet addressed; acceptable at this stage.

## Next steps

1. Add an explicit top-level requirements table in the Mission Concept section, tracing each requirement to an objective and user need, to close the one gap in C1.
2. Extend your coverage analysis beyond the 24.2° equatorial ground-track shift: quantify revisit as a function of latitude for the GBR's range and incorporate cloud-cover constraints into the weekly-revisit trade you identified.
3. Address the payload implications of 10 m GSD colour imaging from 600 km — begin a payload sizing trade (aperture, SNR, alternative altitude/GSD combinations) to show the imaging objective is feasible.
4. Complete the reference entries that lack titles and dates so all citations are fully professional.
5. Use your Week 10 float strategically: if the coverage trade shows one satellite cannot meet objective 1, plan time to evaluate a constellation option.

---
<sub>Run Input_1_u-Run_3-Eff_low-261118-123143 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 9490/3395 | cost $0.001906 (incl. $0.001072 for the reused reference rubric+task structure) | 35.87s</sub>
