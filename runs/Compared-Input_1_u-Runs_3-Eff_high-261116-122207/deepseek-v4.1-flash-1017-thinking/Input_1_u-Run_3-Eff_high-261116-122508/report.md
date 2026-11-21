# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 87 / 100 (87%)**

Your reef-monitoring mission is well argued and clearly structured. You name users and needs, justify an STK-based plan with contingencies and sources, and your orbit calculations correctly expose a coverage shortfall. To reach the top of the Accomplished band, show the inclination working, quantify the revisit shortfall, derive requirement values, and fix the [6] citation and Gantt Week 10 inconsistency.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 9 / 10 | 36 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Accomplished | 9 / 10 | 27 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (36/40, Accomplished)

You give a clear goal, four numbered objectives and named users (AIMS, GBRMPA) with distinct needs, grounded in bleaching evidence and cited literature. To secure full marks, derive the 10 m GSD, weekly revisit and 24 h delivery values from your sources or a sensor trade, rather than asserting them, and tie each requirement explicitly back to the user need it serves.

*Assessor reasoning:* Clear goal, four numbered objectives/requirements, named users with distinct needs, and rationale grounded in bleaching evidence and cited literature. Objectives are traced back to user needs. Slight weakness: requirement values (10 m, weekly, 24 h) are asserted rather than derived from sources.
> Mission Concept & Rationale: "Give reef managers direct, repeatable observations of coral colour over the whole Great Barrier Reef, so that bleaching is detected within days"  
> Mission Concept & Rationale: "The satellite would be operated by the Australian Institute of Marine Science (AIMS). Its customers are the Great Barrier Reef Marine Park Authority"  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (27/30, Accomplished)

Your Gantt (Figure 1) has dated weeks, per-task descriptions and mission-driven sequencing, plus a risk/contingency table with triggers and a source table; STK is justified against mission questions. For full marks, align the Gantt with your text: the STK Simulations bar runs to Week 10 although you state design and simulation finish by Week 9. Clarify whether Week 10 is float only.

*Assessor reasoning:* Gantt chart with dated weeks, per-task descriptions, sequencing justified by mission logic, a risk/contingency table with triggers and responses, and a source table. Software choice (STK) justified against mission questions. Minor: STK Simulations bar runs into Week 10 despite text saying completion by Week 9.
> Project Plan: "The order follows the mission: the imaging requirements (objectives 1 and 2) fix the orbit altitude and local time"  
> Project Plan: "Week 10 is float as well as editing time: no new design work is planned in it."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (8/10, Accomplished)

Your hand calculations for a, T, orbits/day, SSO inclination, ground-track shift and swath are numerically correct and interpreted, and they honestly expose a coverage shortfall that feeds your contingency plan. To reach full marks, show the J2 nodal-precession working behind the 97.8° inclination, and quantify the revisit failure by counting required swaths/passes against daylight passes per week rather than concluding qualitatively.

*Assessor reasoning:* Hand calculations for a, T, orbits/day, SSO inclination, ground-track shift and swath are numerically correct and interpreted, exposing a genuine coverage shortfall that feeds the contingency plan. Inclination is stated without working, and the coverage conclusion is qualitative rather than quantified.
> Preliminary Progress: "the reef is up to about 250 km wide, so a 60 km swath needs at least five neighbouring passes"  
> Preliminary Progress: "A first STK scenario with this orbit has been set up, and its period agrees with the hand calculation."  

### C4 Report presentation (16/20, Accomplished)

The report is logically structured with clear headings, readable prose, labelled Figure 1 and Tables 2–3, consistent formatting, and in-text citations that match the reference list. For full marks, correct reference [6]: it is a NOAA climate-change page cited for BoM sea-surface-temperature products, so add the actual BoM source. Consider replacing news article [4] with the primary method source.

*Assessor reasoning:* Logical structure, clear headings, readable prose, labelled figure and tables, consistent formatting, and in-text citations matching the reference list. Deductions: reference [6] (NOAA climate-change page) is cited for BoM sea-surface-temperature products, and [4] is a news article rather than the primary method source.
> Image 1  
> Project Plan: "Figure 1: Project Gantt chart, Weeks 2 to 10 (gold = completed, blue = planned, red lines = report deadlines)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | yes | Project Plan |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan / Image 1 |
| R5 | List the information sources you plan to use. | yes | Project Plan (Table 2) |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | yes | Preliminary Progress |

## Technical issues

- Preliminary Progress (Table 3): Sun-synchronous inclination of 97.8° is stated without the J2 nodal-precession working, so the key orbit assumption cannot be checked.
- Preliminary Progress: Coverage conclusion is qualitative; no explicit swath-count or revisit calculation (e.g. passes needed vs daylight passes per week) is shown to prove weekly coverage fails.
- Mission Concept & Rationale: Requirement values (10 m GSD, weekly revisit, 24 h delivery) are asserted rather than derived from the cited sources or sensor trade.
- References: Reference [6] is a NOAA climate-change page but is cited as the source of BoM sea-surface-temperature products; no BoM source is listed.
- Project Plan (Image 1): Gantt shows STK Simulations running through Week 10, contradicting the text that final design and simulation finish by end of Week 9.

## Next steps

1. In Preliminary Progress, add the J2 nodal-precession calculation that yields the 97.8° sun-synchronous inclination, so the key orbit assumption can be checked.
2. Quantify the coverage shortfall: count required swaths/passes versus daylight passes per week to show explicitly why weekly revisit fails, rather than concluding qualitatively.
3. Reconcile the Gantt (Image 1) with the text: STK Simulations runs to Week 10 while the text says design and simulation finish by Week 9; also replace reference [6] with a BoM sea-surface-temperature source.

---
<sub>Run Input_1_u-Run_3-Eff_high-261116-122508 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8962/7436 | cost $0.00508 (incl. $0.001072 for the reused reference rubric+task structure) | 32.25s</sub>
