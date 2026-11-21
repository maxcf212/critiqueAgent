# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 59 / 100 (59%)**

You developed a well-structured mission concept targeting Australian coral reef monitoring, appropriately supported by an Executive Summary, conclusion, and STK access reports. To reach higher rubric levels, you need to eliminate critical astrodynamics errors in your orbital mechanics and launch parameters, explicitly identify your mission operators and paying customers, reconcile reported communication statistics with raw software output data, and replace non-peer-reviewed sources like Wikipedia with credible engineering literature.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly outlined the coral reef monitoring rationale and justified a single satellite. To reach Accomplished, avoid vague descriptions of stakeholders by explicitly identifying the specific spacecraft operator and paying customer organizations.

*Assessor reasoning:* The rationale and mission (coral reef monitoring) are clearly outlined, and using a single satellite is justified. However, specific operators and paying customers are only vaguely mentioned.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You addressed launch, orbit, STK communication access, and passive deorbiting. To reach Accomplished, ensure your technical design is accurate: correct the prograde 87.79° inclination to a valid retrograde SSO (~97.8° at 600 km), fix Kourou's latitude, and align contact duration claims with your STK output.

*Assessor reasoning:* Covers launch, orbit, ground communication (STK access report), duration, and passive deorbit. However, retrograde SSO inclination is incorrect (reported ~87.8° instead of ~97.8°), and Kourou latitude is wrong.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  

### C3 Conclusion (7/10, Accomplished)

You successfully reached Accomplished by delivering an appropriate and detailed conclusion that directly connected your chosen orbital elements, launch vehicle, and ground stations back to resolving the coral bleaching monitoring problem.

*Assessor reasoning:* Provides an appropriate summary of findings, linking orbital choices, launch vehicle, and ground station selection directly back to mission goals.
> Conclusion: "The initial problem of not catching coral bleaching events in time can be minimised, if not solved, by the initiation of the ZYZZsat"  

### C4 Report presentation (10/20, Adequate)

Your report layout includes clear sections and an executive summary. To achieve Accomplished, remove prohibited Wikipedia citations from your Bibliography in favor of reliable technical sources, resolve citation formatting errors, and proofread for incomplete sentences.

*Assessor reasoning:* Report follows a standard layout with an executive summary, but relies on Wikipedia (explicitly prohibited in task instructions) and features incomplete sentences and citation formatting errors.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design: Kourou latitude is stated as 45.05 deg N; Kourou is actually at ~5.2 deg N.
- Orbit: An altitude of 600 km in sun-synchronous orbit requires an inclination of ~97.8 deg, not 87.79 deg (which is prograde, not retrograde).
- Ground Control & Communications: Mean contact duration is reported as 'almost twenty minutes', but STK output mean duration is 580.78 s (~9.7 minutes).

## Next steps

1. Correct orbital mechanics and geographical parameters in the 'Orbit' and 'Mission Design' sections, ensuring the Sun-Synchronous Orbit inclination is properly calculated as retrograde (~97.8° for 600 km) and Kourou's latitude is accurately stated (~5.2° N).
2. Align textual descriptions in 'Ground Control & Communications' with your STK data reports, such as correcting the mean pass duration from 'almost twenty minutes' to the actual 580.78 seconds (~9.7 minutes).
3. Replace all Wikipedia entries in the Bibliography with peer-reviewed literature or authoritative technical sources, and explicitly define your primary spacecraft operator and customer base in the Introduction.

---
<sub>Run Input_2_d-Run_2-Eff_low-261118-125902 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18032/3620 | cost $0.012975 (incl. $0.001387 for the reused reference rubric+task structure) | 25.09s</sub>
