# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 87 / 100 (87%)**

You present a clear Australian reef-monitoring mission, a feasible project plan and useful early orbit work. Your strongest next step is to test whether the proposed imaging and orbit coverage can actually meet the mission requirements. Sharper technical validation, more detailed work-package outputs and a final language and referencing polish would strengthen the report further.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Your Mission Concept & Rationale connects the GBRMPA and other users to a clear need, with quantified requirements and supporting sources. To strengthen this further, validate optical bleaching detection through water at the proposed resolution; correct the acidity claim to refer to hydrogen-ion concentration and define bathymetry separately if retained.

*Assessor reasoning:* The mission purpose, need, operational objectives, intended operator and user groups are clearly connected. Quantified revisit, resolution, delivery and lifetime requirements add useful specificity, and the rationale is supported by sources. The concept would be stronger with validation that satellite visible-band imagery at the proposed resolution can distinguish bleaching through the water column.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef, so that bleaching is detected within days instead of after a seasonal aerial survey."  
> Mission Concept & Rationale: "Its customers are the Great Barrier Reef Marine Park Authority, which needs up-to-date bleaching maps to decide where to send survey and response teams"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Your Project Plan and Figure 1 provide a sequenced Gantt chart, explain key dependencies and include contingencies and information sources. To make the plan more robust, break broad work packages into specific deliverables and decision points, especially for resolving sensor feasibility and orbit coverage risks.

*Assessor reasoning:* The Gantt chart gives a sequenced schedule, and the narrative explains dependencies between imaging, orbit, ground control and communications. Planned information sources are identified, and specific schedule, software-access and coverage contingencies are provided. Some work packages remain broad, but the plan is robust and feasible.
> Project Plan: "STK was chosen because its access and coverage tools answer the two questions this mission depends on"  
> Image 1  
> Project Plan: "Week 10 is float as well as editing time: no new design work is planned in it."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Your Preliminary Progress includes a hand-calculated orbital period, a preliminary STK scenario and interpretation of the coverage challenge. Next, justify the assumed 6,000 pixels and 60 km swath with instrument design, and use orbit simulation to test actual coverage and revisit rather than inferring them from swath width alone.

*Assessor reasoning:* The submission contains useful preliminary orbit calculations, a coverage-versus-swath assessment, an interpretation of the main design challenge and a stated STK scenario. The work demonstrates progress. The coverage inference is preliminary and does not establish revisit performance; sensor feasibility and a more complete orbit-coverage analysis remain open.
> Preliminary Progress: "Period | T = 2π√(a³/μ) | 5,801 s = 96.7 min"  
> Preliminary Progress: "A first STK scenario with this orbit has been set up, and its period agrees with the hand calculation."  

### C4 Report presentation (16/20, Accomplished)

Your report is logically structured, readable and uses a clearly captioned Figure 1, labelled tables and in-text citations with a substantial reference list. For stronger professional polish, replace informal phrases, make source details more consistent and check that every cited source and reference-list entry is complete and matched.

*Assessor reasoning:* The report has a logical structure, readable prose, clearly labelled tables and figure, and a substantial reference list with in-text citations. A few informal phrases and some uneven source detail keep it short of exemplary professional polish, but presentation is clear and consistent overall.
> Image 1  
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds., Space Mission Engineering: The New SMAD."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan; Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Image 1 |
| R5 | List the information sources you plan to use. | yes | Information sources |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress |

## Technical issues

- Mission Concept & Rationale: The central concept assumes visible-band satellite imagery can detect coral colour changes through water at 10 m ground sample distance. Water depth, turbidity, atmospheric effects, cloud cover, spectral bands and water-column correction can strongly limit this; the report does not establish sensor feasibility or validate the requirement against the cited airborne method.
- Preliminary Progress: The 60 km swath estimate assumes 6,000 across-track pixels at 10 m sampling, but no sensor field of view or instrument design supports that assumption. Five swaths could geometrically span 250 km, but the stated approximately 2,700 km equatorial ground-track separation means adjacent orbital passes will not simply provide those neighbouring strips; revisit and coverage need orbit simulation.
- Mission Concept & Rationale: The statement that oceans have become 30 percent more acidic is imprecise: the commonly cited increase is in hydrogen-ion concentration, not a linear percentage change in a general measure of acidity.
- Mission Concept & Rationale: The introduction mentions bathymetry as a potential product, but the objectives and preliminary design focus on bleaching imagery. Bathymetry would require its own performance requirements and feasibility assessment.

## Next steps

1. In Mission Concept & Rationale, assess whether visible-band imagery can detect bleaching at the proposed resolution through realistic water depths and turbidity. Specify relevant spectral bands and corrections, and compare the performance with the cited airborne method.
2. In Preliminary Progress, support the 60 km swath estimate with a sensor field of view and instrument assumptions, then simulate orbit coverage and revisit. Account for the stated approximately 2,700 km ground-track separation rather than assuming five adjacent strips.
3. In Project Plan, add concrete outputs and decision points to broad work packages, linked to the mission’s key risks. In the final edit, clarify whether bathymetry is in scope and check the acidity wording, professional tone and completeness of source details.

---
<sub>Run Input_1_u-Run_1-Eff_high-261116-122541 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 9550/7587 | cost $0.004944 (incl. $0.001072 for the reused reference rubric+task structure) | 62.33s</sub>
