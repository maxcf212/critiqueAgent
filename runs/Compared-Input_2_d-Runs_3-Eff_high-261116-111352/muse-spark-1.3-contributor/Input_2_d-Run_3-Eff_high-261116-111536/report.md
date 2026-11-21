# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 48 / 100 (48%)**

You proposed a well-motivated single-satellite GBR fluid-lensing mission with good STK coverage of launch, orbit and ground contacts. To reach Accomplished you need to fix orbit maths, clarify operator/customers and operations, and improve presentation, referencing and evidence files.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You described well in Introduction your fluid-lensing GBR mission need and why 'only one satellite is required' for scientists to predict bleaching. For Accomplished, explicitly name operator versus customers instead of vague Australia facilities and implied scientists, with literature support.

*Assessor reasoning:* Primary mission, need and single-spacecraft rationale well described with literature. Users only vague: customers implied as scientists, operator only as Australia ground facilities, no clear operator/customer split.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "allow marine and conservation scientists to more accurately predict and react"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You covered in Launch, Orbit and Ground Control & Communications your Vega E choice, orbit elements with STK views, ground-tracks and access table. For Accomplished, correct 7171 km to 6971 km, resolve 87.79 deg vs 97.8 deg retrograde in Image 4, fix Kourou 45.05 N and RAAN, correct ~20 min claim vs 580.8 s mean, and include STK files.

*Assessor reasoning:* All major design areas addressed with STK views, ground-tracks and access table. Design undermined by major technical errors in sma, inclination/retrograde, latitudes and durations, and no STK/PIGI files evidenced.
> Launch: "will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of"  
> Image 4  

### C3 Conclusion (5/10, Adequate)

You recapped in Conclusion launch, polar sun-synchronous orbit for 'consistent illumination of the oceans' and bleaching benefit. For Accomplished, expand beyond brief generic summary to detailed conclusions fully tied to evidence, addressing Vega E uncertainty implications.

*Assessor reasoning:* Recaps launch, orbit, ground station and benefit for bleaching. Appropriate and linked to body but brief, generic, and notes Vega E uncertainty without full implications.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans"  

### C4 Report presentation (8/20, Adequate)

You used logical headings and executive summary, which aids readability. For Accomplished, number/title figures including Image 4, format tables consistently, proofread grammar, fix malformed Bibliography entries and replace Wikipedia e.g. 2021_in_spaceflight with proper sources cited correctly.

*Assessor reasoning:* Logical headings and executive summary present, but figures lack numbers/titles, tables poorly formatted, grammar errors, malformed refs, and prohibited Wikipedia used as design source.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 4  

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

- Orbit: Semi-major axis 7171 km for 600 km altitude wrong; should be 6971 km. Inclination 87.79 deg not SSO retrograde; plot shows ~97.8 deg, text contradicts retrograde claim.
- Launch: Kourou latitude quoted as 45.05 N; actual ~5.2 N. RAAN 27.33 deg justified as launch facility location is incorrect.
- Ground Control & Communications: Mean access 580.8 s (~9.7 min), max 770 s (~12.8 min), so claim of almost twenty minutes average is false, overstating link by ~2x.

## Next steps

1. Recalculate and correct your Orbit semi-major axis to 6971 km, reconcile 87.79 deg vs 97.8 deg in Image 4 for true retrograde SSO, and fix Kourou latitude and RAAN justification in your Launch section.
2. Clarify in your Introduction operator versus customers and in Ground Control & Communications use your access table mean 580.8 s and max 770 s to justify realistic contact frequency, not almost twenty minutes.
3. Number and title all your figures including Image 4, tidy tables, replace Wikipedia in your Bibliography with primary sources, and attach your STK files to strengthen evidence.

---
<sub>Run Input_2_d-Run_3-Eff_high-261116-111536 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14795/8659 | cost $0.002784 (incl. $0.001387 for the reused reference rubric+task structure) | 52.15s</sub>
