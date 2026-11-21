# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 61 / 100 (61%)**

You presented a well-motivated mission concept addressing Great Barrier Reef coral monitoring, supported by effective STK access modeling and a clear operational rationale. Your proposal addresses key Australian stakeholder needs well. To raise your design to the highest level, correct the orbital mechanics misconception regarding equatorial launches for retrograde orbits, substantiate your end-of-life disposal with quantitative calculations, and refine presentation standards by adding figure captions, fixing truncated text, and replacing prohibited sources like Wikipedia.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You clearly established a well-justified concept targeting Great Barrier Reef coral bleaching using fluid lensing. You effectively rationalised using a single satellite and identified key stakeholders like CSIRO and BOM. To reach the top of Accomplished, provide deeper quantitative mission rationale supporting your coverage requirements.

*Assessor reasoning:* The introduction establishes a strong, well-justified mission concept addressing coral bleaching on the Great Barrier Reef using fluid lensing. It explains why dedicated monitoring is needed, justifies using a single spacecraft, and identifies relevant Australian stakeholders and operators (CSIRO, BOM, universities).
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You addressed key elements well, including orbital parameters, rideshare choices, and STK ground-access analysis. To achieve Accomplished, correct the orbital mechanics misconception regarding equatorial launch assistance for a retrograde Sun-Synchronous Orbit (i = 97.79°), and provide supporting quantitative sizing or delta-V calculations for the EOL drag sail.

*Assessor reasoning:* All key design segments are addressed, including orbital elements, launch rideshare, STK access analysis, and EOL disposal. However, claiming an equatorial launch assists a retrograde Sun-Synchronous Orbit is an orbital-mechanics error. Additionally, EOL drag sail claims lack quantitative sizing or delta-V calculations.
> Launch: "The most efficient rocket launches are from locations close to the equator as this is where maximum rotational velocity can be experienced"  

### C3 Conclusion (7/10, Accomplished)

You successfully synthesised your design selections—including orbit type, launch vehicle, and ground stations—linking them back to operational utility. To improve within Accomplished, summarize the quantitative performance outcomes of your STK analysis and explicitly state how these confirm mission success criteria.

*Assessor reasoning:* The conclusion summarizes the core mission design selections—launch vehicle, orbit type, ground station, and operational utility—synthesizing the evidence presented in the report into appropriate final remarks.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

You structured the report logically with a clear executive summary. To reach Accomplished, ensure all figures and tables in Orbit include formal numbering and captions, resolve the truncated sentence in Mission Duration & EOL, format references professionally, and remove non-academic sources like Wikipedia (Reference [6]).

*Assessor reasoning:* The report follows a clear structure with an executive summary. However, presentation suffers from unnumbered and uncaptioned figures, an incomplete sentence in the EOL section, poorly formatted raw URLs, and citing Wikipedia against explicit instructions.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Equatorial launch sites provide a positive velocity boost only for prograde orbits; for a retrograde SSO (i = 97.79 deg), Earth rotation must be overcome.
- Mission Duration & EOL: Truncated text / incomplete sentence: 'utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10].'
- Bibliography: Reference [6] cites Wikipedia, explicitly prohibited in the assignment brief.
- Orbit: Figures and tables lack standard academic numbering and formal captions.

## Next steps

1. Re-evaluate the launch site analysis by accounting for the velocity penalty incurred when launching into a retrograde Sun-Synchronous Orbit (i = 97.79°).
2. Substantiate the end-of-life disposal section with quantitative engineering calculations, such as required drag sail surface area or de-orbit delta-V.
3. Standardise report presentation by formally numbering and captioning all figures and tables, completing the truncated sentence in Mission Duration & EOL, and replacing Wikipedia with peer-reviewed references.

---
<sub>Run Input_2-Run_3-Eff_high-261115-170758 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18138/9463 | cost $0.032527 (incl. $0.001387 for the reused reference rubric+task structure) | 55.45s</sub>
