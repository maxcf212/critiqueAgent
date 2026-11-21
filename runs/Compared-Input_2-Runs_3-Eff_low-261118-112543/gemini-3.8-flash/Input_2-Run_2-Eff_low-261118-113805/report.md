# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 63 / 100 (63%)**

You produced a well-motivated preliminary design for ZYZZsat with clear mission rationale and appropriate software tools like STK. Your introduction and conclusion successfully synthesised mission objectives and trade-offs. To reach higher marks, provide quantitative engineering calculations for end-of-life deorbiting and orbital manoeuvres, and address presentation flaws such as incomplete sentences, truncated captions, and non-academic citations.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You provided a comprehensive rationale for ZYZZsat, clearly identifying stakeholders (CSIRO, BOM) and justifying the single-satellite architecture. Your literature context was well integrated.

*Assessor reasoning:* The mission concept, justification, single-satellite rationale, and user/customer identification are thoroughly and clearly addressed with good literature context.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You covered core mission aspects using STK, but reached Adequate because orbital manoeuvres and deorbit mechanics lacked quantitative depth. To reach Accomplished, calculate drag sail sizing and orbital decay timelines from 600 km, address propulsion needs, and accurately evaluate launch trajectory physics.

*Assessor reasoning:* Covers all key aspects: launch vehicle, site, SSO elements, ground station access, and passive deorbit sail. However, orbital maneuvers are essentially omitted by assuming direct injection without onboard propulsion, and no deorbit timeline or drag area sizing is calculated.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (8/10, Accomplished)

Your conclusion concisely synthesised major design selections and trade-offs, appropriately acknowledging external risks such as the development timeline of the Vega E launch vehicle.

*Assessor reasoning:* The conclusion concisely summarises key findings, trade-offs, and design selections across the segments.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet. Thus, launch may need to be adjusted"  

### C4 Report presentation (10/20, Adequate)

The report follows a logical engineering structure with an executive summary. To reach Accomplished, remove prohibited sources like Wikipedia from your bibliography, resolve truncated figure captions, and fix incomplete sentences such as the trailing quote in Mission Duration & EOL.

*Assessor reasoning:* The report structure is clear and has an executive summary. However, Wikipedia is explicitly cited in violation of instructions, figure captions are cut off/unformatted, and an incomplete sentence appears under EOL.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Launch: SSO launches from Kourou typically require dogleg maneuvers or southerly trajectories rather than benefiting from equatorial prograde velocity gain.
- Mission Duration & EOL: No technical decay calculation or sail area sizing provided to verify compliance with the 25-year LEO disposal guideline from a 600 km altitude.

## Next steps

1. Include explicit calculations for end-of-life disposal (such as drag sail area sizing and lifetime decay models) to prove compliance with the 25-year LEO guideline.
2. Detail required orbital manoeuvres or injection tolerances, accounting for specific launch constraints such as dogleg manoeuvres for SSO from Kourou.
3. Audit your bibliography and formatting to eliminate non-peer-reviewed sources like Wikipedia, fix incomplete sentences, and properly format all figure captions.

---
<sub>Run Input_2-Run_2-Eff_low-261118-113805 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18177/3741 | cost $0.013538 (incl. $0.001387 for the reused reference rubric+task structure) | 22.35s</sub>
