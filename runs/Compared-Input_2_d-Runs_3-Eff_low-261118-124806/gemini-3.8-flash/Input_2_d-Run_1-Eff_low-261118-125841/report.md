# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 57 / 100 (57%)**

You developed a strong, relevant mission concept monitoring the Great Barrier Reef with fluid lensing, supported by solid STK modeling. To reach higher bands, you must address critical technical inaccuracies—such as your orbital inclination and launch site coordinates—and strengthen your professional reporting by avoiding prohibited sources like Wikipedia.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly articulated the mission rationale and single-satellite selection in the Introduction. To reach Accomplished, identify specific primary operators and end-user organisations rather than general user groups.

*Assessor reasoning:* The mission rationale, benefits to Australia (Great Barrier Reef monitoring), and use of a single satellite are clearly articulated. However, user identification is superficial.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Your STK access and deorbit analyses were well chosen. To achieve Accomplished, resolve core technical blunders: fix the SSO inclination to ~97.79° retrograde, correct Kourou's latitude, and report mean access durations accurately from your data tables.

*Assessor reasoning:* The student addresses launch, orbit, communications (STK access report), and passive deorbit via drag sail. However, there are major technical blunders: French Guiana latitude is listed as 45°N instead of ~5.2°N, and sun-synchronous inclination at 600 km is retrograde (~97.8°), but the student claims 87.79° despite their own plot correctly showing ~97.8°.
> Orbit: "altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  

### C3 Conclusion (5/10, Adequate)

You successfully recapped the mission parameters in the Conclusion. To reach Accomplished, avoid generic summaries and provide a detailed synthesis evaluating how well the design criteria and mission requirements were satisfied.

*Assessor reasoning:* The conclusion summarizes main elements (Vega E, sun-synchronous orbit, Mt Pleasant ground station) but is somewhat generic and reiterates errors without deeper synthesis.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (10/20, Adequate)

The report features a clear engineering structure and abstract. To reach Accomplished, adhere strictly to sourcing guidelines by eliminating Wikipedia references and fixing formatting issues in your reference list.

*Assessor reasoning:* The report includes an executive summary and standard headings, but relies on Wikipedia (explicitly prohibited in the brief) and has minor formatting/truncation issues (e.g. broken reference formatting).
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Stated Kourou latitude as 45.05° N; it is actually ~5.2° N.
- Orbit: Stated SSO inclination at 600 km altitude is 87.79°, which is prograde; true SSO at 600 km is ~97.79° retrograde (which matches the student's own graph Image 3, showing a transcription error of 87.79°).
- Ground Control & Communications: Claimed the mean access duration is almost 20 minutes, but the STK table explicitly states mean duration is 580.786 seconds (~9.7 minutes).

## Next steps

1. Verify orbital calculations and software outputs carefully, ensuring your stated SSO inclination aligns with your STK plots (~97.79° retrograde rather than 87.79°).
2. Double-check geographic inputs and STK report data, correcting Kourou's latitude (~5.2° N) and accurately converting access duration seconds to minutes.
3. Replace general sources like Wikipedia with peer-reviewed literature or official space agency technical documentation, properly defining primary operators and end-users.

---
<sub>Run Input_2_d-Run_1-Eff_low-261118-125841 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18109/3596 | cost $0.018453 (incl. $0.001387 for the reused reference rubric+task structure) | 21.32s</sub>
