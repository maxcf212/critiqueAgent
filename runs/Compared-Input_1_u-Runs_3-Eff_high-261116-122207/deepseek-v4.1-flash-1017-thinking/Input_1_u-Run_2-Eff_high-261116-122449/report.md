# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 87 / 100 (87%)**

Your report presents a well-motivated reef-bleaching mission for Australia, with quantified objectives, named users, a justified Gantt plan including contingencies, and correct preliminary orbit calculations that expose the coverage-versus-resolution trade. To reach the top of the rubric, replace secondary sources with primary literature, derive rather than assert the 10 m GSD, show the J2 calculation behind 97.8°, and justify the 6000-pixel assumption.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

A clear goal, four quantified objectives, and users (AIMS, GBRMPA) explicitly mapped to needs, supported by [1]–[6]. To secure the top band, replace secondary/news sources with primary literature, derive the 10 m GSD rather than asserting it, and correct the '30 percent more acidic' phrasing to a pH fall of about 0.1.

*Assessor reasoning:* Clear goal, four quantified objectives, named users with needs explicitly mapped to objectives, and literature support [1]-[6]. Minor weaknesses: some sources are secondary/news items and the 10 m GSD is asserted rather than derived.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef, so that bleaching is detected within days"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS). Its customers are the Great Barrier Reef Marine Park Authority"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Your Gantt chart, risk/contingency table and source table form a robust plan, explicitly justified against the mission narrative (orbit altitude and local time fixed by imaging objectives), with Week 10 float. To strengthen further, make the generic task descriptions more specific and link each information source to the task it supports.

*Assessor reasoning:* Gantt chart with task descriptions, risk/contingency table, and a source table. Plan is explicitly justified against the mission narrative and includes float and fallbacks. Slightly generic task descriptions in places.
> Project Plan: "The order follows the mission: the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time"  
> Project Plan: "Week 10 is float as well as editing time: no new design work is planned in it."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Correct hand calculations for semi-major axis, period, orbits/day, inclination, track spacing and swath, with the coverage-versus-resolution trade clearly identified and an STK period check. Next: show the J2 calculation behind 97.8°, justify the 6000-pixel assumption, correct track spacing at 20°S, and extend beyond one orbit case with a link budget or coverage simulation.

*Assessor reasoning:* Hand calculations for a, T, orbits/day, inclination, track spacing and swath are correct and interpreted, identifying the key coverage trade. Limited to one orbit case; no link budget or coverage simulation results yet.
> Preliminary Progress: "Weekly coverage (objective 1) is therefore not guaranteed by one satellite at this altitude and resolution."  
> Preliminary Progress: "A first STK scenario with this orbit has been set up, and its period agrees with the hand calculation."  

### C4 Report presentation (16/20, Accomplished)

Logical structure, consistent headings, labelled Figure 1 and Tables 2–3, and in-text citations matching the reference list. To reach the top band, strengthen weak references: replace the news article and the author-less ResearchGate entry, and fix [6], which does not support the BoM SST fusion claim.

*Assessor reasoning:* Logical structure, consistent headings, labelled figure and tables, in-text citations matching the reference list. Some references are weak (news article, ResearchGate entry without authors) and [6] does not really support the BoM claim.
> Figure 1: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  
> References: "[7] J. R. Wertz, D. F. Everett, and J. J. Puschell, Eds., Space Mission Engineering: The New SMAD."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan (Launch Specifics, Orbit Specifics) |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan, first paragraph |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Figure 1 |
| R5 | List the information sources you plan to use. | yes | Table 2 |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress, Table 3 |

## Technical issues

- Preliminary Progress, Table 3: Inclination of 97.8° is stated without showing the J2 nodal precession calculation that produces it.
- Preliminary Progress, Table 3: 6000 pixels across-track is assumed without justification; the 60 km swath and hence the coverage conclusion depend on it.
- Preliminary Progress, interpretation: Track spacing of 2,700 km is equatorial; at ~20°S latitude it is ~2,540 km, and the conclusion that weekly coverage fails is understated rather than overstated.
- Mission Concept & Rationale: '30 percent more acidic' is imprecise; ocean pH has fallen ~0.1 (≈30% rise in H+ concentration).
- Mission Concept & Rationale, objective 2: 10 m GSD is to be 'refined against the method in [4]', but [4] is a news article, not the primary method paper, and no derivation is given.
- References [6]: Cited to support BoM SST fusion, but the source is a general NOAA page that does not address this.

## Next steps

1. In Preliminary Progress, show the J2 nodal precession calculation that produces the 97.8° inclination, and justify the 6000-pixel across-track detector assumption that drives the 60 km swath and your coverage conclusion; also correct the 2,700 km track spacing to about 2,540 km at 20°S so the weekly-coverage shortfall is stated accurately.
2. In Mission Concept & Rationale, replace the news article [4] with the primary method paper and derive the 10 m GSD explicitly against it; rephrase '30 percent more acidic' as a pH fall of about 0.1 (roughly a 30% rise in H+ concentration).
3. In the reference list, replace [6] (a general NOAA page) with a source that actually supports the BoM SST fusion claim, and add author details to the ResearchGate entry; in the Project Plan, sharpen the generic task descriptions and tie each information source to a specific task.

---
<sub>Run Input_1_u-Run_2-Eff_high-261116-122449 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8972/5834 | cost $0.003642 (incl. $0.001072 for the reused reference rubric+task structure) | 19.58s</sub>
