# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 51 / 100 (51%)**

You have a clear report structure and a well-motivated coral-bleaching mission, with launch, orbit, ground station, duration and EOL covered and STK screenshots/access table included. To reach Accomplished, correct the SSO inclination and Kourou latitude, reconcile contact-duration claims with your access data, justify Mt Pleasant as TT&C, include STK files, and strengthen referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly explain the mission need, rationale and why one spacecraft suffices, with references. To move from Adequate to Accomplished, explicitly identify the operator and customers (e.g., marine/conservation scientists and Australian facilities) and add specific literature support for the user/operations model.

*Assessor reasoning:* Mission need, rationale, and single-spacecraft choice are well explained with references. Users are implied as marine/conservation scientists and Australian facilities, but operator and customers are not explicitly identified, so not all C1 requirements are fully met.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground control, duration and EOL with STK screenshots and an access table. However, the SSO inclination (87.79° prograde vs ~97.8°), Kourou latitude (45.05°N vs ~5.2°N) and contact duration (~9.7 min mean, not ~20 min) are major errors. Accomplished requires corrected, reconciled calculations, STK files and justified ground-station choice.

*Assessor reasoning:* Launch, orbit, ground station, duration and EOL are covered with STK screenshots and an access table. However, major technical errors exist: SSO inclination is wrong/prograde, Kourou latitude is wrong, and mean contact is ~9.7 min not ~20 min. STK files are not evident.
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Launch: "with a latitude of $ 45.05^{\circ} $N"  

### C3 Conclusion (5/10, Adequate)

You reach conclusions linked to launch, orbit and ground-station choices. To reach Accomplished, make them specific to your results, include mission duration and EOL outcomes, and avoid repeating unresolved design errors (e.g., SSO/polar wording). Tie each conclusion back to evidence in the main body.

*Assessor reasoning:* Conclusions are reached and linked to launch, orbit and ground station choices, but they are somewhat generic and omit EOL and mission-duration outcomes. Some claims repeat design errors rather than resolving them.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

Your report has clear headings, an executive summary and labelled figures/tables. To reach Accomplished, professionalise presentation: number tables, make captions consistent, fix grammar/typos, replace bare-URL and Wikipedia references with properly formatted sources, and ensure in-text citations match the reference list.

*Assessor reasoning:* Report has clear structure, headings, executive summary and figures. Presentation is not professional: bare-URL references, Wikipedia source, unnumbered tables, inconsistent figure captions, and several grammar/typo errors. References are cited but poorly formatted.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Kourou latitude is stated as 45.05°N; actual latitude is about 5.2°N.
- Orbit: SSO inclination at 600 km is stated as 87.79°, which is prograde; correct SSO inclination is about 97.8° and the graph contradicts the text.
- Ground Control & Communications: Mean access duration 580.786 s is about 9.7 min, not 'almost twenty minutes'; maximum is about 12.8 min.
- Orbit: Text says 'A very high altitude would yield low resolution images which is also desirable'; likely should be undesirable.
- Launch: Claim of two launch windows per day because site latitude is less than inclination is not adequately justified.
- Ground Control & Communications: Mt Pleasant Radio Observatory is a radio astronomy facility; its use as a satellite TT&C/data ground station needs justification.
- Bibliography: Wikipedia is used as a source and references are bare URLs without titles/authors.

## Next steps

1. Revisit the orbital mechanics: recompute SSO inclination for 600 km (about 97.8°, retrograde) and correct the Kourou latitude to about 5.2°N; update the orbit graph/text so they agree and justify the launch-window claim.
2. Recalculate and rewrite the communications section from your access table: mean 580.786 s is ~9.7 min (max ~12.8 min), not 'almost twenty minutes'; explain the Mt Pleasant Radio Observatory TT&C justification or choose an appropriate ground station.
3. Add the STK software files (or appendix links) and replace bare-URL/Wikipedia references with properly cited, authoritative sources; also correct the high-altitude/low-resolution sentence and ensure conclusions cover EOL and mission duration.

---
<sub>Run Input_2_d-Run_2-Eff_low-261118-125038 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14270/8817 | cost $0.00645 (incl. $0.001387 for the reused reference rubric+task structure) | 55.12s</sub>
