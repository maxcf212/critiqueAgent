# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You developed a solid concept for reef monitoring with effective STK coverage and ground station analyses. However, critical orbital calculation errors, launch site discrepancies, and unfinished text kept the work at an Adequate level. To reach Accomplished, ensure all orbital parameters are physically accurate and consistent, explicitly identify end-users, and proofread carefully to eliminate truncated sentences and informal references.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You clearly established the reef-monitoring mission and single-satellite rationale. To reach Accomplished, explicitly differentiate the operational entities and paying customers rather than referencing marine scientists broadly.

*Assessor reasoning:* Primary mission, rationale (monitoring Great Barrier Reef bleaching via fluid lensing), and constellation size (1 spacecraft) are clearly stated. However, specific users, including commercial/government operators and paying customers, are vaguely addressed.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your STK simulation provided good access insight. However, stating a prograde 87.79° inclination for an SSO, misidentifying Kourou's latitude, and truncating the drag sail discussion in Mission Duration & EOL limited the score. Ensure technical calculations and parameters are verified and consistent.

*Assessor reasoning:* Launch details and ground station access are reasonably simulated using STK. However, major technical errors exist: Kourou's latitude is stated as 45.05°N (actually ~5.2°N), and SSO inclination at 600 km is given as 87.8° (prograde, physically impossible; SSO requires ~97.8°). EOL section cuts off mid-sentence.
> Mission Design: "The Vega VV flights launch from the Guiana Space Centre’s Spaceport, in Kourou, French Guiana."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 87.7924^{\circ} for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "a Tasmanian facility is selected – the Mount Pleasant Radio Observatory)."  

### C3 Conclusion (5/10, Adequate)

You successfully summarized the main mission parameters. To achieve Accomplished, write a detailed conclusion that evaluates mission trade-offs, limitations, and operational feasibility rather than generic reiterations.

*Assessor reasoning:* The conclusion summarizes the main body findings but remains fairly generic and reiterates basic design choices without addressing limitations or technical trade-offs.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

The document followed a logical layout with helpful plots. To attain Accomplished, repair incomplete sentences such as the drag sail description, correct bibliography formatting, and replace Wikipedia citations with peer-reviewed literature.

*Assessor reasoning:* The layout has standard headings and STK visuals, but suffers from broken text (e.g. cut-off sentence in EOL), malformed bibliography entries, and explicitly prohibited sources (Wikipedia cited as source [6]).
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Mission Design: Stated Kourou latitude as 45.05°N instead of ~5.23°N.
- Orbit: Incorrect SSO inclination: 87.79° is prograde; a 600 km circular SSO requires approximately 97.79° retrograde inclination (even though MATLAB plot correctly shows ~97.8°).
- Mission Duration & EOL: Sentence terminates prematurely in the drag sail description.

## Next steps

1. Correct the orbital mechanics in the Orbit section: recalculate the sun-synchronous inclination to the retrograde value (~97.8°), aligning your text with your MATLAB figure.
2. Verify geographical parameters across the report, correcting Kourou’s latitude from 45.05°N to approximately 5.23°N.
3. Replace non-peer-reviewed sources such as Wikipedia with authoritative aerospace references and complete all truncated sentences before submission.

---
<sub>Run Input_2_d-Run_3-Eff_low-261118-125927 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18205/3529 | cost $0.012764 (incl. $0.001387 for the reused reference rubric+task structure) | 22.37s</sub>
