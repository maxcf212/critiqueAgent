# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 87 / 100 (87%)**

You have produced a strong, coherent preliminary report, with a clear Australian mission rationale, a feasible project plan and useful early orbital work. You are already at the Accomplished level across the criteria; there is no higher rubric band. The next steps will make your imaging, coverage and delivery claims more rigorously supported and strengthen the report further.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

In Mission Concept & Rationale, you clearly connect reef monitoring to Australian users, including AIMS, and state measurable objectives. To strengthen this Accomplished work, substantiate the 10 m requirement by addressing sensor bands, water-column effects, turbidity and validation against the cited mapping method.

*Assessor reasoning:* The mission purpose, Australian benefit, intended operational and research users, and preliminary measurable objectives are clear and well connected to user needs. The rationale is supported by references. Some claims and the proposed 10 m imaging requirement would benefit from stronger qualification or validation.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS)."  
> Mission Concept & Rationale: "Deliver each image to an Australian ground station within 24 hours of capture."  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Your Project Plan and Image 1 provide a mission-linked sequence, deadlines and contingencies; Information Sources identifies relevant resources. Strengthen the plan by defining completion criteria for tasks and showing how orbit, sensor and downlink feasibility results will inform later design decisions.

*Assessor reasoning:* The Gantt chart and task descriptions give a feasible, mission-linked sequence, with deadlines, contingency actions, and appropriate planned information sources. The plan includes useful responses to schedule and software-access risks. A little more detail on task completion criteria would strengthen it further.
> Image 1  
> Project Plan: "The order follows the mission: the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time"  
> Contingencies: "Week 10 is float as well as editing time: no new design work is planned in it."  
> Information sources: "Table 2 lists the sources I plan to use and what each is for."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Preliminary Progress shows useful hand calculations and an initial STK scenario, and you identify the swath-versus-coverage trade. Show the J2 derivation and assumptions for the 97.8° inclination, then simulate coverage and assess daylight, cloud constraints, data volume and downlink before treating weekly coverage and 24-hour delivery as feasible.

*Assessor reasoning:* Useful preliminary orbit calculations, an initial STK scenario, and an interpretation of the swath-versus-coverage challenge demonstrate progress. The period, approximate sun-synchronous inclination, and ground-track shift are reasonable. The inclination calculation is not shown, and the coverage conclusion remains a preliminary estimate rather than a simulated result.
> Preliminary Progress: "I have also made first hand calculations for a candidate orbit, a circular sun-synchronous orbit at 600 km altitude"  
> Preliminary Progress: "T = 2π√(a³/μ) | 5,801 s = 96.7 min"  
> Preliminary Progress: "A first STK scenario with this orbit has been set up, and its period agrees with the hand calculation."  

### C4 Report presentation (16/20, Accomplished)

Your logical structure, readable prose, labelled tables and figure, and matching reference list make the report easy to follow. For an even more polished presentation, revise awkward phrasing and describe sources precisely while keeping citations and formatting consistent.

*Assessor reasoning:* The report has a logical structure, readable prose, clearly labelled tables and figure, and a matching reference list. Presentation is generally consistent and professional. Some phrasing is awkward, and a few sources are described imprecisely, but these do not impede understanding.
> Image 1  
> Preliminary Progress: "Table 3: Preliminary hand calculations for the candidate orbit."  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan; Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan; Image 1 |
| R5 | List the information sources you plan to use. | yes | Information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress |

## Technical issues

- Mission Concept & Rationale: The 10 m ground-sample-distance requirement is not yet demonstrated to detect bleaching reliably. Sensor spectral bands, water-column effects, turbidity, and validation against the cited mapping method need consideration.
- Preliminary Progress: Weekly full-reef coverage and delivery within 24 hours are not yet established. The approximate ground-track spacing and swath discussion identifies a trade, but coverage needs orbit-access simulations that account for latitude, revisit, daylight, and cloud availability; data volume and downlink capacity also need assessment.
- Preliminary Progress: The 97.8° sun-synchronous inclination is plausible at 600 km, but the report gives the target nodal precession without showing the J2 calculation or assumptions used to obtain that inclination.

## Next steps

1. Assess whether 10 m imagery can reliably identify bleaching: specify relevant sensor bands, consider water-column effects and turbidity, and explain how you will validate performance against the cited mapping method.
2. Use orbit-access simulations to test weekly reef coverage and 24-hour delivery, accounting for latitude, revisit, daylight and cloud availability; estimate data volume and downlink capacity.
3. Show the J2 calculation and assumptions behind the 97.8° inclination, and add task completion criteria to the Gantt plan so progress and feasibility can be checked.

---
<sub>Run Input_1_u-Run_2-Eff_high-261116-122643 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 9482/7355 | cost $0.004169 (incl. $0.001072 for the reused reference rubric+task structure) | 59.92s</sub>
