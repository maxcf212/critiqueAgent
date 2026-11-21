# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 89 / 100 (89%)**

An excellent preliminary report. Your reef-monitoring mission concept is well justified with quantified objectives tied to named users, your Gantt plan is robust with contingencies, and your orbit hand calculations are correct and interpreted against your objectives. Presentation is professional. To reach the very top of the rubric, address latitude dependence in your coverage analysis and add a requirements table.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Accomplished (9/10). Your mission goal is clear, your four objectives are quantified, and users (GBRMPA, AIMS, CSIRO, BoM) are explicitly tied to their needs, supported by references [1]–[6]. To fully reach the top of the Accomplished band, add an explicit requirements table with verification approach linking objectives to mission requirements.

*Assessor reasoning:* Clear goal, four quantified objectives, users (AIMS, GBRMPA, CSIRO, BoM) tied to needs, and literature cited [1]-[6]. Objectives explicitly traced to user needs. Minor gap: no explicit requirements table/verification, but essentially complete.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "Its customers are the Great Barrier Reef Marine Park Authority, which needs up-to-date bleaching maps"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Accomplished (9/10). Your Gantt chart (Figure 1) is well structured with task logic tied to the mission (orbit before comms), a risk/contingency table (Table 1), float, and a planned-sources table (Table 2) including SMAD and lecture notes. This is a robust, mission-aligned plan; little is missing at this level.

*Assessor reasoning:* Gantt chart with task descriptions, explicit logic linking plan order to mission (orbit before comms), contingencies/risk table, float, and a planned-sources table (Table 2) including SMAD and lecture notes. Robust and mission-aligned.
> Project Plan: "Project work is divided into weeks in the Gantt chart in Figure 1"  
> Project Plan: "The main risks and the planned responses are listed in Table 1."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Accomplished (8/10). Your hand calculations (a=6978 km, T=5801 s, 14.9 orbits/day, i≈97.8° SSO, 24.2° track shift) are correct and interpreted against your objectives, with a swath trade identified and STK setup completed. Strengthen the coverage analysis by accounting for latitude dependence at the reef, and note the aperture implications of 10 m GSD at 600 km.

*Assessor reasoning:* Hand calculations verified correct (a=6978 km, T=5801 s, 14.9 orbits/day, i≈97.8° SSO, 24.2° track shift). Results interpreted against objectives, swath trade identified, STK tutorials done and scenario set up. On track.
> Preliminary Progress: "T = 2π√(a³/μ) | 5,801 s = 96.7 min"  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution."  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has a logical structure, clear writing, labelled figures and tables with explained legends, and consistent IEEE-style citations matching the reference list. Presentation is professional; maintain this standard in the full report.

*Assessor reasoning:* Logical structure, clear writing, labelled figures/tables, consistent IEEE-style citations matching the reference list, colour legend explained. Very professional presentation.
> References: "[1] NOAA, "Ocean acidification," 2020. [Online]."  
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Preliminary Progress — orbit hand calculations, launch/orbit tasks in plan |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan — 'The design will be completed in STK' |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan — Figure 1 Gantt chart |
| R5 | List the information sources you plan to use. | yes | Project Plan — Table 2 planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress — Table 3 calculations and STK setup |

## Technical issues

- Preliminary Progress: Ground-track shift quoted at the equator is fine, but the reef sits at ~18-20°S where track spacing is smaller; the coverage conclusion is conservative but could note latitude dependence.
- Mission Concept & Rationale: 10 m GSD at 600 km implies a demanding telescope/aperture; feasibility not yet addressed (acceptable at this stage).

## Next steps

1. In Preliminary Progress, note that your 24.2° equatorial track shift overstates spacing at the reef's latitude (~18–20°S), where ground-track spacing is smaller — discuss how this changes your weekly-coverage conclusion and consider computing spacing at 18°S.
2. Add a table of mission requirements (derived from your four objectives) with a brief note on how each will be verified, to close the gap between objectives and requirements in C1.
3. Briefly flag the feasibility of 10 m GSD at 600 km (aperture/telescope sizing) as a design question to resolve in the full assignment, so the swath trade is framed early.

---
<sub>Run Input_1_u-Run_1-Eff_low-261118-123037 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 9477/3350 | cost $0.002313 (incl. $0.001072 for the reused reference rubric+task structure) | 29.69s</sub>
