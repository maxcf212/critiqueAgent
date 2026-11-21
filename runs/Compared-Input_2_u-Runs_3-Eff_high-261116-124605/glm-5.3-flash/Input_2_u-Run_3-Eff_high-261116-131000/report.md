# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 90 / 100 (90%)**

An excellent, comprehensive mission design for ZYZZsat. All required elements are addressed with verified hand calculations, STK evidence (Images 1-5, Appendix A), well-justified trade-offs, and honest acknowledgement of limitations. To reach the very top of the Accomplished band, strengthen the link budget, eclipse/beta-angle treatment, decay sensitivity, and GSD analysis, and consider discussing alternative mission concepts in Section 1.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Accomplished (9/10). Section 1 addresses all requirements: primary mission (5 m GSD imaging of the Great Barrier Reef), need (bleaching statistics, gaps in existing products), single-spacecraft justification, and users (AIMS as operator, multiple customers), all well referenced [1]-[6]. To reach full marks, add a brief discussion of alternative mission concepts considered and why the single-spacecraft approach was preferred over, say, a small constellation.

*Assessor reasoning:* All required elements addressed: primary mission, need (bleaching statistics, limitations of existing products), single-spacecraft justification, operator and multiple customers, funding. Detailed, well-referenced ([1]-[6]). Only minor gap: no discussion of alternative mission concepts.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  
> 1 Introduction: "One satellite is therefore used."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Accomplished (54/60). Section 2 is comprehensive: launch trade table with azimuth calculation (2.2), hand-derived orbit elements verified in STK including i = 97.79° (2.3, Table 4), explicit manoeuvres, ground station access analysis with six daily passes (2.4, Table 5), data budget, and a five-year mission with drag-sail EOL and decay calculations (2.5). Screenshots, tables, references and Appendix A files are all present. Full marks require closing the missing X-band link budget, treating eclipse duration as beta-angle dependent, bounding the decay estimate, and analysing GSD beyond the diffraction/pixel-count argument.

*Assessor reasoning:* Launch site/vehicle justified with trade table and azimuth calculation; orbit elements derived by hand and verified in STK; manoeuvres explicitly addressed; ground station chosen with STK access report; data budget; five-year mission and drag-sail EOL with decay calculations. Screenshots, tables, references and appendix files all present. Link budget admittedly missing; eclipse duration treated as fixed.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "cos i = −0.1355, so i = 97.79°" *(quote not found in submission)*  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission."  

### C3 Conclusion (9/10, Accomplished)

Accomplished (9/10). Section 3 reaches specific, quantitative conclusions (revisit times, pass rates, decay lifetime) and honestly identifies four limitations with proposed next steps, showing genuine design insight. To reach full marks, tie each limitation to a concrete, prioritised action with expected impact on the design (e.g. which analysis would most change the orbit or EOL choice).

*Assessor reasoning:* Conclusions are specific and quantitative (revisit times, pass rates, decay lifetimes) and honestly identify four limitations with proposed next steps, showing genuine design insight rather than generic summary.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown"  

### C4 Report presentation (18/20, Accomplished)

Accomplished (18/20). The report has a clear structure with executive summary, numbered sections, consistently labelled figures and tables, matched citations [1]-[15] in IEEE style, and concise professional writing. Minor deductions relate to some low-resolution figures and a table of contents without page numbers; ensure all figures are high-resolution and formatting is fully consistent throughout.

*Assessor reasoning:* Clear structure with executive summary, numbered sections, consistently labelled figures/tables, all citations [1]-[15] matched to reference list, professional IEEE-style referencing, concise writing. Figures are legible STK outputs with captions. Minor: some figures low resolution; no table of contents page numbers shown.
> Executive Summary: "This report presents the design of ZYZZsat"  
> Bibliography: "[11] D. A. Vallado, *Fundamentals of Astrodynamics and Applications*, 4th ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction (Number of spacecraft) |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction (Users) |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit (Manoeuvres) |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications, Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3/2.4 (STK 11 plus hand calculations) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Images 1-5, Appendix A (ZYZZsat_STK.zip file list) |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Whole report; Bibliography |

## Technical issues

- 2.1 Table 1: Eclipse duration quoted as a fixed ~34 min per orbit without considering beta-angle variation; actual eclipse time varies over the year.
- 2.4 Table 6: X-band link budget (margin, antenna gains, data rates achievable) not performed, only data-volume budget; acknowledged by student.
- 2.5 Table 7: Decay analysis uses single mean density and scale height; sensitivity acknowledged but lifetime estimate is crude.
- 2.2 Launch: Vega C unflown at time of writing; fallback given, but rideshare orbit compatibility (altitude/injection) not guaranteed.
- 2.3 Orbit: GSD driven only by diffraction limit and pixel count; detector IFOV/sampling and pointing jitter effects on 5 m GSD not analysed.

## Next steps

1. Add an X-band link budget to Section 2.4 (margin, antenna gains, achievable data rates) to complement the data-volume budget in Table 6, closing the gap you honestly flagged.
2. In Section 2.1/Table 1, present eclipse duration as a function of beta angle over the year rather than a fixed ~34 min per orbit, e.g. a plot of eclipse time versus beta angle from STK.
3. Extend the Section 2.5 decay analysis with a sensitivity study (varying density/scale height or running multiple STK cases) to bound the re-entry date, and analyse detector IFOV/sampling and pointing jitter effects on the 5 m GSD in Section 2.3.
4. In Section 2.2, quantify the rideshare orbit compatibility risk for Vega C (altitude/injection tolerances) and state explicit acceptance criteria for the fallback option.
5. In Section 1, briefly discuss alternative mission concepts (e.g. constellation vs single spacecraft, alternative payloads) and why they were rejected; also improve figure resolution and add page numbers to the table of contents.

---
<sub>Run Input_2_u-Run_3-Eff_high-261116-131000 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15220/6121 | cost $0.002975 (incl. $0.001387 for the reused reference rubric+task structure) | 93.52s</sub>
