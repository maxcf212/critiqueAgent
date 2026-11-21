# AERO9500 Preliminary Report (Part 1): Graded Feedback

**Total: 52 / 100 (52%)**

You have established a compelling, well-motivated mission rationale for monitoring the Great Barrier Reef and presented an organised project schedule. To elevate your work for the final submission, focus on defining quantified technical requirements, resolving key astrodynamics principles in your orbit design, incorporating concrete preliminary calculations or simulations, and polishing your academic presentation with complete formal references and consistent scheduling.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Mission concept and rationale — What will it do, who are the users, why is it needed? | Adequate | 6 / 10 | 24 / 40 |
| C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use | Adequate | 5 / 10 | 15 / 30 |
| C3 Preliminary progress — Technical content and evidence of sufficient work done to date | Deficient | 3 / 10 | 3 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Mission concept and rationale — What will it do, who are the users, why is it needed? (24/40, Adequate)

In 'Mission Concept & Rationale', you articulated a strong environmental need and clearly identified marine scientists as end users. To achieve 'Accomplished', define quantitative mission requirements—such as spatial resolution, spectral bands, and revisit frequency—and replace bare URLs with formal academic citations to support your mission goals.

*Assessor reasoning:* The rationale and target users (marine scientists) are well articulated with clear environmental context. However, the proposal lacks formal quantitative mission requirements (such as spectral bands, revisit frequency, and spatial resolution), and references are provided only as bare web links.
> Mission Concept & Rationale: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  

### C2 Project plan — How you plan to complete the assignment, including either a Gantt chart or a timetable and information sources you plan to use (15/30, Adequate)

Your weekly Gantt chart and task breakdown in 'Project Plan & Preliminary Progress' clearly show project feasibility. To reach 'Accomplished', add explicit contingency plans for potential technical delays, clarify how individual tasks connect directly to your mission narrative, and identify specific literature and software sources you plan to use.

*Assessor reasoning:* A clear weekly Gantt chart and task descriptions demonstrate project feasibility. However, the plan lacks provisions for contingencies or schedule variations, and future information sources are not explicitly listed.
> Project Plan & Preliminary Progress: "Project work will be divided into weeks via a Gantt Chart."  

### C3 Preliminary progress — Technical content and evidence of sufficient work done to date (3/10, Deficient)

While you identified orbit selection as a priority, claiming a 600 km geostationary orbit violates fundamental orbital mechanics (GEO requires ~35,786 km over the equator). To reach 'Adequate' or 'Accomplished', conduct viable preliminary trade-offs (e.g., LEO vs. GEO), and include concrete technical calculations or preliminary STK simulation results.

*Assessor reasoning:* No preliminary technical calculations, orbital trade-offs, or STK outputs are included. Furthermore, the only engineering choice proposed—a 600 km geostationary orbit—violates basic astrodynamics, as GEO exists solely at ~35,786 km over the equator.
> Project Plan & Preliminary Progress: "My current choice is a geostationary orbit at an altitude of 600 km, which keeps the satellite fixed above the reef"  

### C4 Report presentation (10/20, Adequate)

Your report has a clear, readable structure with helpful subheadings. To attain 'Accomplished', ensure visual figures include descriptive captions, eliminate scheduling discrepancies between your text (Weeks 7–8) and Gantt chart (Weeks 9–10), and adopt consistent, standard bibliographic referencing instead of bare URLs.

*Assessor reasoning:* The document is readable and logically organised with clear subheadings. However, formatting is weakened by raw URL citations, an uncaptioned figure, and a contradiction between the Gantt chart (editing in Weeks 9–10) and narrative text (Weeks 7–8).
> Mission Concept & Rationale: "¹ https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a simple space-mission concept that benefits Australia; explain its purpose, intended users and rationale. | yes | Mission Concept & Rationale |
| R2 | Relate the preliminary plan to the mission’s space segment, applying relevant course material such as launch and orbits. | partial | Project Plan & Preliminary Progress |
| R3 | Select the software package to use for the mission design. If using software other than STK, PIGI or flightclub, contact Naomi before starting; PIGI users must register for its competition to obtain a software licence. | yes | Project Plan & Preliminary Progress |
| R4 | Provide a project plan explaining how you intend to complete the assignment, using either a Gantt chart or a timetable. | yes | Project Plan & Preliminary Progress |
| R5 | List the information sources you plan to use. | partial | Mission Concept & Rationale |
| R6 | Include preliminary technical content that demonstrates sufficient work has been completed to date. | no | - |

## Technical issues

- Project Plan & Preliminary Progress: Claiming a geostationary orbit at 600 km altitude is physically impossible. Geostationary orbits exist only near 35,786 km in the equatorial plane, whereas 600 km is Low Earth Orbit (LEO) with an orbital period of roughly 96 minutes.
- Project Plan & Preliminary Progress: Text states editing and finalisation occur in Weeks 7 and 8, but the Gantt chart depicts this task in Weeks 9 and 10.

## Next steps

1. Redesign your orbital architecture to reflect correct astrodynamics, replacing the 600 km geostationary concept with a physically viable LEO constellation or repeating ground-track orbit, verified via preliminary calculations or STK.
2. Define formal, quantitative engineering requirements in your concept section, detailing parameters such as ground sample distance (resolution), spectral bands for coral monitoring, and required revisit frequency.
3. Refine report consistency and formatting by aligning your narrative text with your Gantt chart milestones, adding figure captions, and converting bare URL links into formal bibliographic citations.

---
<sub>Run Input_1_d-Run_2-Eff_high-261116-111113 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 7365/7516 | cost $0.026743 (incl. $0.001072 for the reused reference rubric+task structure) | 45.01s</sub>
