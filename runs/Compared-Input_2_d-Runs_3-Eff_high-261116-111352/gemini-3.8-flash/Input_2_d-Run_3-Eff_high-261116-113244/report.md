# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 51 / 100 (51%)**

You developed a compelling mission concept for Great Barrier Reef monitoring with well-reasoned architecture and STK modelling. However, technical analysis contains key discrepancies in orbital parameters, launch coordinates, and access durations, alongside presentation and referencing oversights. By verifying core orbital mechanics, directly aligning written claims with simulation data, and completing thorough technical proofreading, you will significantly improve the rigor of your space mission proposals.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly justified the coral reef monitoring concept and single-satellite architecture in the Introduction. To reach Accomplished, explicitly identify the specific operational entities and customer organisations (such as Australian marine research agencies or government stakeholders) who will operate the spacecraft and utilise payload data, supporting these selections with citations.

*Assessor reasoning:* The mission rationale, objectives, and single-satellite architecture are well justified. However, specific operational entities and customer organisations are not clearly defined.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You applied STK simulation effectively to design your orbit. To reach Accomplished, ensure orbital parameters are accurate: an SSO at 600 km altitude requires a retrograde inclination (~97.8°, not 87.79°) and a 6971 km semi-major axis. Additionally, correct Kourou's latitude (~5.2°N) and match your access duration text to STK output data.

*Assessor reasoning:* STK simulation is utilised, but significant technical errors exist: Kourou's latitude is ~5.2°N, not 45.05°N; SSO inclination is ~97.8°, not prograde 87.79°; semi-major axis math is wrong; STK mean duration is 9.7 min, not 20.
> Mission Design: "Guiana Space Centre Spaceport, in Kourou, French Guiana... situated very close to the equator, with a latitude of 45.05°N." *(quote not found in submission)*  
> Mission Design: "altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved, in addition to the already frequent amount of passes."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion successfully restates key mission parameters and sensor objectives. For Accomplished, move beyond restating design parameters by synthesising how well your design satisfies operational requirements, evaluating mission trade-offs, and drawing deeper conclusions directly from your STK simulation results.

*Assessor reasoning:* The conclusion reiterates design parameters and mission goals, but lacks critical synthesis or deeper evaluation of mission constraints and performance outcomes.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

You structured the report well and included an executive summary. To achieve Accomplished, replace informal sources like Wikipedia with peer-reviewed literature, number and label every figure, complete broken sentences (such as in Mission Duration & EOL), and ensure uniform citation formatting across your bibliography.

*Assessor reasoning:* The report has a workable structure and an executive summary. However, it violates instructions by citing Wikipedia, has unnumbered figures, an incomplete sentence, and bibliography formatting defects.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design: Kourou spaceport latitude is incorrectly identified as 45.05°N instead of approximately 5.23°N.
- Mission Design: A sun-synchronous orbit at 600 km requires a retrograde inclination of ~97.8°, whereas 87.79° is prograde.
- Mission Design: Semi-major axis is given as 7171 km instead of 6971 km for a 600 km altitude above an Earth radius of 6371 km.
- Ground Control & Communications: STK access table reports a mean duration of 580.8 s (9.7 min), contradicting the student's claim of 'almost twenty minutes'.
- Mission Duration & EOL: The text terminates abruptly mid-sentence: 'utilising a large surface area to ‘ and is suitable'.

## Next steps

1. Recalculate baseline orbital parameters in Mission Design: set the semi-major axis to 6971 km, adopt a retrograde inclination (~97.8°) for the 600 km sun-synchronous orbit, and correct Kourou's coordinates (~5.2°N).
2. Align Ground Control & Communications descriptions directly with STK simulation outputs to resolve data discrepancies (e.g., mean pass duration of 9.7 minutes versus 20 minutes).
3. Upgrade report presentation by replacing Wikipedia citations with academic or industry sources, captioning and numbering all figures, and completing truncated text in Mission Duration & EOL.

---
<sub>Run Input_2_d-Run_3-Eff_high-261116-113244 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18276/8224 | cost $0.030423 (incl. $0.001387 for the reused reference rubric+task structure) | 41.78s</sub>
