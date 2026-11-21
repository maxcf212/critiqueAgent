# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 68 / 100 (68%)**

You present a clear, well-motivated reef-monitoring mission with explicit users and a strong Australian rationale, supported by a readable Gantt-based plan and a sensible STK software choice. Presentation is clean and professional. To progress, you need quantified mission requirements, a corrected orbit statement (600 km is LEO, not geostationary), fuller source details, contingency planning, and actual preliminary design results rather than tutorial completion alone.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Accomplished | 8 / 10 | 32 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Adequate | 6 / 10 | 18 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Accomplished | 7 / 10 | 14 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (32/40, Accomplished)

You clearly explain the mission purpose, name the users (marine and conservation scientists, ground stations) and give a compelling Australian rationale with referencing. To reach the top of Accomplished, add quantified requirements (resolution, revisit, latency, lifetime) and an explicit objectives statement. Also correct the 2017 coral-loss claim and reframe '30 percent more acidic' as a pH change (~0.1 unit).

*Assessor reasoning:* Clear mission purpose (reef monitoring: SST, thermal stress, bathymetry, colour-change detection), explicit users (marine/conservation scientists, ground stations) and compelling Australian rationale with data (60%/50% mortality, acidification). Referenced. Lacks quantified mission requirements (resolution, revisit, latency, lifetime) and objective statement.
> Mission Concept & Rationale: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (18/30, Adequate)

Your Gantt chart has weekly columns, task rows, deadlines and descriptions, and the sequence is feasible and tied to launch, orbit, ground, comms and end-of-life. The next level requires contingency provision, a planned information-source list linked to tasks, and fixing the inconsistency where your text schedules editing in weeks 7–8 but the chart shows weeks 9–10.

*Assessor reasoning:* Gantt chart with weekly columns, task rows, deadlines and per-task descriptions; feasible sequence tied to launch, orbit, ground, comms, EOL. But no contingency allowance, no planned-source list linked to the plan, and internal inconsistency (text says editing in weeks 7–8; chart shows weeks 9–10).
> Project Plan & Preliminary Progress: "Project work will be divided into weeks via a Gantt Chart. Detailed task descriptions can be found on the next page."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (4/10, Adequate)

Your reported progress is background reading and completion of STK tutorials 1–4. To move beyond Adequate, present actual preliminary design results, calculations or simulation output with brief interpretation. Note that the orbit claim as written (600 km geostationary) is incorrect, so it cannot yet count as evidence of useful design work.

*Assessor reasoning:* Only progress is background reading and completion of four STK tutorials; no design results, calculations or simulation output are presented. The single technical claim made (orbit choice) is incorrect, so it cannot count as evidence of useful design work.
> Project Plan & Preliminary Progress: "researched into how coral bleaching occurs and its severity, and also completed STK tutorials 1, 2, 3 & 4."  

### C4 Report presentation (14/20, Accomplished)

Your report is logically structured with clear headings, readable professional prose, consistent formatting and a labelled, explained Gantt figure; superscript citations match your numbered source list. To reach the top of Accomplished, replace bare URLs with full references (author, title, date, source) in a consistent standard format and ensure every in-text citation matches.

*Assessor reasoning:* Logical structure with clear headings, readable professional prose, consistent formatting and a labelled, explained Gantt figure. In-text superscripts match the numbered source list, but sources are bare URLs with no author/title/date, and no reference list in standard format.
> Mission Concept & Rationale: "These bleaching events are destructive enough to wipe out entire reefs, displacing billions of animals in the process."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | partial | Project Plan & Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan & Preliminary Progress |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Image 1 |
| R5 | List the information sources you plan to use. | partial | Mission Concept & Rationale |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | partial | Project Plan & Preliminary Progress |

## Technical issues

- Project Plan & Preliminary Progress: 'geostationary orbit at an altitude of 600 km' is contradictory: GEO altitude is ~35,786 km; 600 km is LEO and cannot be geostationary or continuously stare at the reef.
- Project Plan & Preliminary Progress: End-of-life options include 'leaving it where it is', which conflicts with space-debris mitigation practice; 'graveyard orbit' is inapplicable to the stated altitude.
- Mission Concept & Rationale: Claims a further 50% of coral perished in 2017; literature attributes roughly half of shallow-water coral loss to the combined 2016–2017 events.
- Mission Concept & Rationale: No quantified mission requirements (ground sample distance, revisit time, data latency, swath, design lifetime) derived from the stated user needs.
- Project Plan & Preliminary Progress: Gantt/text contradiction: prose reserves editing for weeks 7–8 while the chart schedules Editing & Finalisation in weeks 9–10.
- Mission Concept & Rationale: '30 percent more acidic' should be expressed as pH change (~0.1 unit) or hydrogen-ion increase; the framing is misleading.

## Next steps

1. Convert your user needs into quantified mission requirements (ground sample distance, revisit time, data latency, swath, design lifetime) and add an explicit objectives statement in the Mission Concept & Rationale section.
2. Correct the orbit claim in the Project Plan: 600 km is low Earth orbit and cannot be geostationary or provide continuous reef stare; revisit your end-of-life options to align with debris-mitigation practice.
3. Produce and interpret at least one preliminary technical result (e.g. an STK coverage/revisit or link-budget output) and resolve the Gantt/text editing-week inconsistency, adding contingency allowance and a planned-source list.

---
<sub>Run Input_1_d-Run_2-Eff_high-261116-110130 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 7185/5340 | cost $0.003645 (incl. $0.001072 for the reused reference rubric+task structure) | 26.72s</sub>
