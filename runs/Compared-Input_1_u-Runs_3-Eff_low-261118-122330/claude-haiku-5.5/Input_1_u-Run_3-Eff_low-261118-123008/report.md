# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 85 / 100 (85%)**

You have written a strong Part 1 report. Your mission concept links the Great Barrier Reef monitoring goals to named users, and your Gantt chart and risk table show careful planning. Your hand calculations for the candidate orbit check out, and you identified a real coverage trade-off between swath width and weekly full-reef coverage. The main gaps are the unaddressed launch work, a Week 10 inconsistency between the Gantt chart and the text, and a few presentation points.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 8 / 10 | 24 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Your mission goals, four quantified objectives and named users (GBRMPA, CSIRO/universities, BoM) are clearly linked, and you support the rationale with references [1]-[6]. To strengthen this further, tighten the acidification claim to its precise meaning and give a firmer justification for the provisional ground sample distance in objective 2.

*Assessor reasoning:* Clear mission goal, four quantified objectives, and named users (GBRMPA, CSIRO/universities, BoM) each linked to specific objectives. Rationale is referenced to sources [1]-[6]. Minor weakness: the 'Oceans 30 percent more acidic' claim is loosely phrased and objective 2's GSD is only provisionally justified.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS)."  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (24/30, Accomplished)

Your Gantt chart, the ordering logic (imaging requirements fix orbit before ground control), and the risk table with triggers and responses make the plan feasible and well referenced. The Week 10 Gantt entry contradicts your text on the final week, so correcting this would make the plan internally consistent.

*Assessor reasoning:* Gantt chart with task descriptions, ordering justified by the mission logic, a risk table with triggers and responses, and planned information sources. The Gantt shows STK Simulations running into Week 10, which contradicts the text saying Week 10 has no new design work and design ends in Week 9.
> Project Plan: "the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time, so orbit work comes before ground control"  
> Contingencies: "Week 10 is float as well as editing time: no new design work is planned in it."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (9/10, Accomplished)

Your hand calculations (orbital period, orbits per day, sun-synchronous inclination and Earth-rotation track shift) are verified, and your swath-versus-resolution interpretation is insightful and feeds into your contingency plan. Extending the work to launch aspects would show progress across the whole mission.

*Assessor reasoning:* Hand calculations are checked: period 5,801 s, 14.9 orbits/day, sun-synchronous inclination ~97.8°, and Earth-rotation track shift ~24.2° all verify. The swath-versus-resolution interpretation is insightful and feeds directly into the contingency plan and STK setup.
> Preliminary Progress: "I have also made first hand calculations for a candidate orbit, a circular sun-synchronous orbit at 600 km altitude"  
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution."  

### C4 Report presentation (16/20, Accomplished)

Your report has a logical sectioned structure, consistent formatting, labelled figure and tables, and citations that match the reference list. Address the Week 10 Gantt inconsistency, add an author or proper source for reference [11], and rephrase the acidity sentence to improve precision.

*Assessor reasoning:* Logical sectioned structure, consistent formatting, labelled figure and tables, and citations matching the reference list. Deductions for the Week 10 Gantt inconsistency with the text, a weakly sourced reference [11] lacking an author, and the 'Oceans 30 percent more acidic' phrasing.
> References: "[11] "Monitoring coral reefs from space," ResearchGate publication 231179724."  
> Figure 1: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | partial | Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan |
| R5 | List the information sources you plan to use. | yes | Information sources (Table 2) |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress |

## Technical issues

- Preliminary Progress: Hand calculations verified (period, orbits/day, SSO inclination, track shift). The 'Ground-track shift per orbit' row is correct, but the 60 km swath need of five passes is not reconciled with weekly full-reef coverage across ~2,300 km.
- Project Plan / Figure 1: Gantt shows STK Simulations active in Week 10, but text states final design ends Week 9 and Week 10 has no new design work.
- Mission Concept: 'Oceans have become 30 percent more acidic' is imprecise; the acidity rise is about 30% in hydrogen-ion concentration (pH drop ~0.1).
- Preliminary Progress: Launch vehicle, trajectory and launch site work (Launch Specifics) is not yet addressed, limiting R2 coverage of launch.

## Next steps

1. Reconcile the Gantt chart (Figure 1) with your text: either remove the STK Simulations bar from Week 10 or update the text to explain the Week 10 work.
2. Reconcile the five-pass swath requirement with the weekly full-reef coverage target across roughly 2,300 km, and state how your contingency plan addresses this.
3. Begin the launch specifics (launch vehicle, trajectory, launch site) so that the preliminary progress covers the full mission, and fix the acidity statement to say the hydrogen-ion concentration rose about 30% (pH fell about 0.1).

---
<sub>Run Input_1_u-Run_3-Eff_low-261118-123008 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 13299/6344 | cost $0.004503 (incl. $0.001072 for the reused reference rubric+task structure) | 28.59s</sub>
