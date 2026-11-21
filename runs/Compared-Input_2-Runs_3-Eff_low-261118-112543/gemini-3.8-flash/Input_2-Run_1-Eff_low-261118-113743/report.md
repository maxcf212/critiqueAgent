# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 59 / 100 (59%)**

You presented a clear mission concept and strong STK modelling for monitoring the Great Barrier Reef. While the Introduction effectively justified the single-satellite architecture, the technical design contained a conceptual error regarding retrograde launch physics, an incomplete sentence in the EOL section, and generic conclusions. Addressing orbital mechanics nuances, submitting software files, and adopting professional referencing standards will bring your report to an Accomplished level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You clearly defined the fluid lensing mission, single-satellite rationale, and user base in the Introduction. To reach the top of Accomplished, integrate deeper literature citations directly supporting your mission requirements.

*Assessor reasoning:* The student clearly articulates the primary mission (coral reef monitoring via fluid lensing), rationale, constellation size (single satellite justified), and potential users/operators.
> Introduction: "The satellite, nicknamed ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), is operated and accessed from Australia ground facilities, and is designed specifically for use above the Great Barrier Reef."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Your STK simulation and orbital selections in 'Orbit' were well executed. To attain Accomplished, resolve the orbital mechanics inaccuracy regarding equatorial launches for retrograde SSO, supply the STK software files, and complete truncated text in 'Mission Duration & EOL'.

*Assessor reasoning:* Most design elements are addressed with STK outputs and orbital calculations. However, no software files are provided, equatorial launch benefit rationale is misapplied to retrograde SSO, and the EOL drag sail discussion cuts off abruptly mid-sentence.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion successfully recaps the core subsystems. To advance to Accomplished, synthesize your findings into detailed, quantitative conclusions that critically evaluate mission trade-offs, performance margins, and key design limitations.

*Assessor reasoning:* The conclusion summarises the findings and mission architecture across subsystems, but remains relatively brief and generic without discussing quantitative trade-offs or key limitations.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (10/20, Adequate)

Headings and figures were applied well, but reaching Accomplished requires avoiding prohibited sources like Wikipedia, replacing bare URL entries with standard engineering bibliographic formats, and thoroughly proofreading to eliminate broken sentences.

*Assessor reasoning:* The report includes headings and STK figures, but relies directly on Wikipedia despite explicit rubric instructions prohibiting it. Furthermore, several sentences are broken/incomplete (e.g., EOL section) and references consist merely of raw URLs.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design: The report claims launching near the equator provides maximum velocity benefit, but for a retrograde SSO (i = 97.8°), Earth's rotational velocity opposes or does not assist the launch azimuth, incurring an energy penalty.
- Mission Duration & EOL: The sentence describing the drag sail cuts off unfinished ('to ‘ and is suitable...').

## Next steps

1. Correct launch site rationale for retrograde orbits by accounting for Earth's rotational velocity penalty at inclinations greater than 90°.
2. Proofread technical descriptions carefully to ensure sentences in the EOL section are fully completed and attach your STK scenario files.
3. Replace raw URL and Wikipedia citations with peer-reviewed literature formatted consistently according to standard engineering styles.

---
<sub>Run Input_2-Run_1-Eff_low-261118-113743 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18113/3527 | cost $0.018198 (incl. $0.001387 for the reused reference rubric+task structure) | 21.74s</sub>
