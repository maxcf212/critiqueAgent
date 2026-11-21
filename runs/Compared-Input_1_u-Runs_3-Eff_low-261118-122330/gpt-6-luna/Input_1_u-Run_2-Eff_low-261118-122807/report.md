# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 87 / 100 (87%)**

You present a compelling Australian reef-monitoring mission, a mission-linked project plan with contingencies, and useful initial orbit calculations. To strengthen the report, validate that the proposed satellite sensor can detect bleaching and substantiate coverage assumptions with sensor and access analysis. Clear structure and references support a professional presentation; more complete source details and precise citations would improve it further.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

Mission Concept & Rationale clearly defines the Reef-monitoring purpose, users and measurable objectives, supported by literature. To make the concept more defensible, validate bleaching detection for the proposed satellite sensor, including spectral bands and water and atmospheric effects; clarify the cited 30% acidity claim.

*Assessor reasoning:* Defines a clear Australian reef-monitoring mission, explains the environmental need, identifies operational users and their purposes, and sets measurable preliminary objectives for coverage, resolution, delivery, and lifetime. Literature is cited throughout. The sensing approach and requirements remain preliminary and need validation, but the mission concept is complete and specific.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef"  
> Mission Concept & Rationale: "Its customers are the Great Barrier Reef Marine Park Authority"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Your week-by-week Gantt chart (Figure 1), information sources (Table 2) and contingencies (Table 1) make a robust, mission-linked plan. To strengthen it further, specify key milestones and keep the planned analysis tied to validating sensor performance and usable Reef coverage.

*Assessor reasoning:* The week-by-week Gantt plan is tied to mission dependencies, identifies intended information sources and software, and includes specific risks, triggers, and responses. Float and contingency planning support feasibility. Some tasks and milestones could be more tightly specified, but the plan is robust for this preliminary assignment.
> Project Plan: "Project work is divided into weeks in the Gantt chart in Figure 1"  
> Project Plan: "The order follows the mission: the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time"  
> Contingencies: "The main risks and the planned responses are listed in Table 1."  
> Information sources: "Table 2 lists the sources I plan to use and what each is for."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Preliminary Progress includes candidate-orbit calculations and an STK scenario checked against the hand-calculated period. Build on this by specifying the assumed sensor and testing usable swath and Reef access; distinguish the approximate 2,700 km equatorial track displacement from demonstrated imaging coverage.

*Assessor reasoning:* Includes a useful candidate-orbit calculation set, interprets the coverage implications, and reports an initial STK scenario checked against the period calculation. The work demonstrates progress and identifies a design trade, though no coverage or access simulation results are presented. The assumed swath derived from pixel count and ground sampling distance is an instrument assumption, not a demonstrated sensor design.
> Preliminary Progress: "I have also made first hand calculations for a candidate orbit, a circular sun-synchronous orbit at 600 km altitude"  
> Preliminary Progress: "A first STK scenario with this orbit has been set up, and its period agrees with the hand calculation."  

### C4 Report presentation (16/20, Accomplished)

Your report is logically structured, readable, and uses labelled figures and tables with in-text citations. Improve the professional finish by giving complete bibliographic details for sources such as the Nature and NOAA items and precise references for technical claims.

*Assessor reasoning:* The report has a clear structure, readable prose, labelled figures and tables, and a substantial reference list with in-text citations. Its presentation is consistent and generally professional. Some references are described vaguely rather than fully bibliographically (for example, the Nature and NOAA items), and several technical claims would benefit from more precise sourcing.
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  
> Information sources: "Table 2: Planned information sources."  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds.,"  

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

- Mission Concept & Rationale: A 10 m ground sample distance alone does not establish that coral bleaching can be detected by colour imagery. The report should validate spectral bands, water depth/turbidity effects, atmospheric correction, and the applicability of the cited airborne method to a satellite sensor.
- Preliminary Progress: The 60 km swath follows arithmetically from 6,000 pixels at 10 m sampling, but assumes a 6,000-pixel-wide imager without specifying a sensor or accounting for usable swath, viewing geometry, or image quality.
- Preliminary Progress: The 2,700 km ground-track separation is an approximate equatorial longitudinal displacement per orbit, not a direct calculation of the separation between adjacent usable imaging tracks over the Great Barrier Reef. Coverage also depends on orbit geometry, sensor field of view, and latitude.
- Mission Concept & Rationale: The stated ocean-acidification increase of 30 percent is ambiguous and does not by itself quantify the relevant change in acidity; the cited source and wording should be checked.

## Next steps

1. In Mission Concept & Rationale, verify that the proposed spectral bands can distinguish bleaching, and discuss water depth, turbidity and atmospheric correction. Check that the cited airborne method applies to a satellite sensor, and clarify the source and meaning of the stated 30% ocean-acidification increase.
2. In Preliminary Progress, identify a plausible imager and justify its usable swath, viewing geometry and image quality. Treat the 2,700 km figure as approximate equatorial track displacement, then use orbit geometry and sensor field of view to assess usable coverage over the Reef.
3. In Information Sources and References, provide complete bibliographic details and precise citations for technical claims. In the project plan, continue tying tasks and contingencies to mission dependencies, and specify milestones where this would make progress easier to assess.

---
<sub>Run Input_1_u-Run_2-Eff_low-261118-122807 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 9553/4078 | cost $0.002539 (incl. $0.001072 for the reused reference rubric+task structure) | 30.64s</sub>
