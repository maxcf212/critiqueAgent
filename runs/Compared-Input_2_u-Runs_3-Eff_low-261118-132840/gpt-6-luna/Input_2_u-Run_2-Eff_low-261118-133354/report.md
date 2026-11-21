# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 68 / 100 (68%)**

You present a clear Australian reef-imaging mission with a strong rationale, useful STK evidence and a logical report structure. The main issue is a factor-of-ten error in the orbital-decay calculations in Section 2.5, which means the report does not establish that the drag sail meets the 25-year EOL guideline. The revisit estimate and assumed downlink rate also need validation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

In Section 1, you clearly explain the reef-imaging mission, its Australian benefit, the single-spacecraft choice, and AIMS as operator. References support the rationale. To sustain the accomplished level, keep the rationale well evidenced and ensure sources are fully specified.

*Assessor reasoning:* The mission, Australian benefit, rationale, single-spacecraft choice, operator, customers, and public-service funding are clearly explained. References support the rationale, although some sources are secondary or incompletely detailed.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Sections 2.2–2.5 and Appendix A address launch, orbit, ground control, communications and EOL, with STK evidence. However, the factor-of-ten decay error undermines the EOL claim; the revisit estimate and 50 Mbit/s downlink also lack validation. The accomplished level requires accurate, comprehensive design evidence supporting these requirements.

*Assessor reasoning:* The report addresses launch, orbit and elements, access calculations, station, communications, duration, and disposal, with STK figures and detailed calculations. However, the orbital-decay calculation is wrong by about a factor of ten, undermining its EOL compliance claim; a link budget is also absent, and the orbit/revisit and payload assumptions are preliminary.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "The orbit is circular, so it has no perigee"  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission."  

### C3 Conclusion (8/10, Accomplished)

Your conclusion draws together the mission’s results and identifies limitations and follow-up work. Its positive EOL conclusion depends on the incorrect decay calculation. To maintain the accomplished level, update the conclusion after correcting the analysis and ensure each conclusion follows from validated evidence.

*Assessor reasoning:* The conclusion synthesizes key design results and identifies meaningful limitations and follow-up work. It is specific to the evidence, though its positive EOL conclusion relies on the erroneous decay calculation.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps"  

### C4 Report presentation (16/20, Accomplished)

The contents, executive summary, labelled figures and tables, readable technical prose and bibliography give the report a clear, professional structure. To sustain the accomplished level, fully specify sources and make sure figures and claims are traceable to appropriate evidence, including the submitted STK files.

*Assessor reasoning:* The report has a logical structure, concise executive summary, labelled figures and tables, readable technical prose, and a substantial bibliography with in-text citations. Presentation is generally professional. Some sources are weakly specified and some figures are not accompanied by underlying software outputs in the report, but the appendix identifies submitted STK files.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite)"  
> Contents: "Executive Summary
1 Introduction
2 Mission Design
2.1 Spacecraft overview"  
> Bibliography: "[11] D. A. Vallado, *Fundamentals of Astrodynamics and Applications*"  
> Image 1  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents |

## Technical issues

- 2.5 Mission Duration & EOL: The stated orbital-decay values are approximately ten times too large for the given equation and inputs. At 600 km, Δa per orbit is about 0.040 m for 0.3 m² and 0.57 m for 4.3 m², not 0.40 m and 5.8 m. Corresponding initial decay rates are about 0.22 km/year and 3.1 km/year; the H/rate estimates are about 320 years and 23 years, respectively, not 32 and 2.2 years. Thus the report does not establish that a 4 m² sail meets the 25-year guideline.
- 2.5 Mission Duration & EOL: The claim of about 11 km altitude loss over five years follows the same factor-of-ten error; the stated inputs imply about 1.1 km using the report's approximation.
- 2.3 Orbit: The five-day access estimate divides equatorial ground-track spacing by the maximum roll-reachable width. It is a simplified upper-bound argument and does not demonstrate actual reef-specific revisit or imaging opportunities, which depend on ground-track geometry, pointing, lighting, and cloud conditions.
- 2.4 Ground Control & Communications: A 50 Mbit/s downlink is assumed without a link budget. The report acknowledges this gap, so the stated capacity margin is not yet verified against transmitter power, antenna gains, range, coding, and losses.

## Next steps

1. Recalculate the Section 2.5 orbital decay and drag-sail lifetime using the stated inputs, then revise the five-year altitude-loss estimate and EOL conclusion. Show evidence that the selected sail meets the 25-year guideline.
2. Validate the five-day access estimate in Section 2.3 using reef-specific ground-track, pointing, lighting and cloud considerations. In Section 2.4, add a link budget supporting the 50 Mbit/s assumption, including transmitter power, antenna gains, range, coding and losses.
3. To reach the accomplished level for mission design, support all major design choices with accurate calculations and evidence. Retain the STK files identified in Appendix A, and strengthen the supporting sources and traceability between claims, figures and references.

---
<sub>Run Input_2_u-Run_2-Eff_low-261118-133354 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15060/5126 | cost $0.003246 (incl. $0.001387 for the reused reference rubric+task structure) | 40.75s</sub>
