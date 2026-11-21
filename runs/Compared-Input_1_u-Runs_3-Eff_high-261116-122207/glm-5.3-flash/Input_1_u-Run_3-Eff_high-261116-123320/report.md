# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 89 / 100 (89%)**

A strong preliminary report for your reef-monitoring mission. You clearly defined goals, quantified objectives and users, built a robust Gantt plan with contingencies and sources, and showed genuine technical progress through correct orbit calculations and STK tutorials. To reach the very top, strengthen payload feasibility discussion, justify the choice over existing missions, and complete reference entries.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Accomplished (9/10). Your mission concept is clear and complete: quantified objectives, explicit users (AIMS, GBRMPA, CSIRO, BoM) with needs traced to requirements, and 11 literature references. To fully secure the top level, briefly explain why a new satellite mission is preferable to existing Earth-observation sources — this justification is currently missing.

*Assessor reasoning:* Clear goal, four quantified objectives/requirements, explicit users (AIMS, GBRMPA, CSIRO, BoM) with needs traced to objectives, and 11 literature references. Only minor gap: no discussion of why a new satellite beats existing missions.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "Its customers are the Great Barrier Reef Marine Park Authority, which needs up-to-date bleaching maps"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Accomplished (9/10). Your plan is robust and mission-integrated: the Gantt chart in Figure 1 has weekly tasks and deadlines, task ordering is justified by mission logic (orbit before comms), Table 1 lists four contingencies with triggers and responses, and Table 2 plans your information sources. Slightly more specific task descriptions would make it even stronger.

*Assessor reasoning:* Gantt chart with task descriptions, explicit rationale linking task order to mission logic (orbit before comms), four contingencies with triggers/responses, and a planned-sources table. Robust and mission-integrated; only slightly generic task descriptions.
> Project Plan: "Project work is divided into weeks in the Gantt chart in Figure 1"  
> Project Plan: "The main risks and the planned responses are listed in Table 1"  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Accomplished (8/10). Your hand calculations (period 96.7 min, sun-synchronous inclination ~97.8°, ground-track shift) are correct and well interpreted, and you honestly identified the swath–revisit trade limiting weekly coverage. Completed STK tutorials and a first scenario show you are on track. Next: move from first-pass results toward addressing the payload feasibility question.

*Assessor reasoning:* Correct hand calculations (period, sun-sync inclination ~97.8°, ground-track shift) with interpretation of the swath–revisit trade, plus completed STK tutorials and a first scenario. Good progress, though results are still first-pass.
> Preliminary Progress: "T = 2π√(a³/μ) | 5,801 s = 96.7 min"  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution"  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has a logical structure, consistent IEEE-style citations matching the reference list, labelled figures and tables with captions, and a professional tone with clean grammar. Minor improvements: complete reference entries that lack titles, and make captions more self-contained so readers can understand each figure or table without reading the body text.

*Assessor reasoning:* Logical structure, consistent IEEE-style citations matching the reference list, labelled figures/tables with captions, professional tone and clean grammar. Minor: some reference entries lack titles, and figure/table numbering within sections is fine but captions could be more self-contained.
> Figure 1: "Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)"  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds., Space Mission Engineering: The New SMAD"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan / Preliminary Progress — orbit, launch, ground segment tasks tied to course material and preliminary orbit calculations |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan — 'The design will be completed in STK (Systems Tool Kit), accessed remotely through the MECH lab 204 licence' |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Figure 1 Gantt chart with weekly tasks and deadlines |
| R5 | List the information sources you plan to use. | yes | Table 2: Planned information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress — Table 3 hand calculations and completed STK tutorials |

## Technical issues

- Preliminary Progress, Table 3: 10 m GSD from a 600 km orbit implies a very demanding optical payload (~6000-pixel swath assumption); payload feasibility is not yet addressed, though flagged as a trade.
- Preliminary Progress: Sun-synchronous 600 km orbit gives ~14.9 orbits/day but equatorial cross-track spacing of ~2700 km means weekly reef coverage claim needs constellation or off-nadir options; student correctly identifies this.
- Mission Concept & Rationale: Statement 'Oceans have become 30 percent more acidic' is a simplification (≈30% rise in H+ concentration from ~0.1 pH drop); acceptable but imprecise wording.

## Next steps

1. Address the payload feasibility trade you flagged: assess whether a 10 m GSD optical payload from 600 km is achievable within a smallsat budget, or show how off-nadir pointing or a constellation closes the weekly-coverage gap you identified.
2. Add a short comparison with existing missions (e.g. Sentinel-2, Landsat) to justify why a new satellite is needed rather than relying on current data sources.
3. Complete your reference list: some entries lack titles or full details, and make captions more self-contained so figures and tables can be read standalone.
4. Refine imprecise wording such as 'oceans have become 30 percent more acidic' — state it as roughly a 30% increase in hydrogen ion concentration from a ~0.1 pH drop.

---
<sub>Run Input_1_u-Run_3-Eff_high-261116-123320 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 9600/4060 | cost $0.002539 (incl. $0.001072 for the reused reference rubric+task structure) | 24.4s</sub>
