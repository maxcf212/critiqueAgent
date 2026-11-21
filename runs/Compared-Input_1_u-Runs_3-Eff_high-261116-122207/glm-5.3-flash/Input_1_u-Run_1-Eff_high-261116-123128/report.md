# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 90 / 100 (90%)**

An excellent preliminary report. Your reef-monitoring mission concept is clearly justified with quantified objectives, named users (AIMS, GBRMPA, CSIRO, BoM) and literature support. Your Gantt chart, contingencies table and information sources make a robust, mission-integrated plan, and your hand-calculated orbit results are correct and well interpreted. Presentation is professional and consistently referenced. To reach the very top of each rubric, address the minor feasibility and justification gaps noted below.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Accomplished (9/10). Your mission goal, four quantified objectives, explicit users and their needs, and references [1]-[6] are all strong. To fully consolidate this level, add a brief quantitative argument for why a new satellite outperforms existing sensors, and check the 10 m GSD at 600 km against realistic payload sizing.

*Assessor reasoning:* Clear mission goal, four quantified objectives/requirements, explicit users (AIMS, GBRMPA, CSIRO, BoM) with needs traced to objectives, and literature support [1]-[6]. Only minor gap: no discussion of why a new satellite beats existing sensors quantitatively.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS). Its customers are the Great Barrier Reef Marine Park Authority"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Accomplished (9/10). Your Figure 1 Gantt chart, Table 1 contingencies with triggers and responses, and Table 2 information sources form a robust plan clearly tied to the mission logic (orbit before comms). Strengthen it further by tying contingency triggers to the cloud/revisit risk you identified in the concept section.

*Assessor reasoning:* Gantt chart with weeks 2-10, task descriptions, explicit contingencies table with triggers/responses, and rationale linking task order to mission logic (orbit before comms). Information sources table included. Robust and mission-integrated.
> Project Plan / Image 1: "Project work is divided into weeks in the Gantt chart in Figure 1"  
> Project Plan: "The main risks and the planned responses are listed in Table 1."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (9/10, Accomplished)

Accomplished (9/10). Your Table 3 hand calculations are verified (T = 5801 s, 14.9 orbits/day, 97.8° sun-synchronous inclination, 24.2° ground-track shift) and you interpreted the swath-resolution trade and its impact on objective 1. Next level: extend this analysis into preliminary payload/link sizing to show even more technical depth.

*Assessor reasoning:* Hand calculations verified: a=6978 km gives T=5801 s (correct), 14.9 orbits/day, sun-sync inclination 97.8° at 600 km (correct), ground-track shift 24.2° (correct). Results interpreted (swath vs resolution trade) and linked to contingencies; STK tutorials done.
> Preliminary Progress: "T = 2π√(a³/μ) | 5,801 s = 96.7 min"  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution."  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has a logical structure, labelled figures and tables, consistent IEEE-style citations matching the reference list, and a professional tone. Minor polish: reword the 'MECH lab 204 licence' phrasing and simplify the dense Gantt chart legend so all formatting reads cleanly at a glance.

*Assessor reasoning:* Logical structure with headings, labelled figures/tables, consistent IEEE-style citations matching the reference list, professional tone, good grammar. Minor quibbles: 'MECH lab 204 licence' phrasing and slightly dense Gantt legend, but presentation is professional overall.
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds.,"  
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan / Preliminary Progress — orbit, launch, ground segment tasks and orbit hand calculations |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan — 'The design will be completed in STK'; PIGI fallback notes registration |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan — Figure 1 Gantt chart |
| R5 | List the information sources you plan to use. | yes | Project Plan — Table 2 planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress — Table 3 orbit calculations and STK setup |

## Technical issues

- Mission Concept & Rationale: 10 m GSD at 600 km in visible bands is ambitious for a 'simple' mission (WorldView-class optics); no payload sizing check yet.
- Mission Concept & Rationale: Weekly 'cloud-free' imaging of tropical Queensland is optimistic given persistent cloud; revisit requirement may be unachievable in practice.
- Mission Concept & Rationale: Minor inconsistency: 'near-real-time relay' vs objective 3's 24-hour delivery window.

## Next steps

1. Add a quantitative comparison showing why a new 10 m GSD satellite is needed over existing sensors (e.g. Sentinel-2, WorldView), and sanity-check the payload mass/aperture implied by 10 m GSD at 600 km.
2. Revisit the weekly cloud-free imaging requirement for tropical Queensland: quantify expected cloud statistics and consider whether revisit or delivery requirements should be relaxed or met another way.
3. Resolve the inconsistency between 'near-real-time relay' and objective 3's 24-hour delivery window, and clarify the 'MECH lab 204 licence' phrasing and Gantt legend readability.

---
<sub>Run Input_1_u-Run_1-Eff_high-261116-123128 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 9564/3983 | cost $0.002512 (incl. $0.001072 for the reused reference rubric+task structure) | 53.9s</sub>
