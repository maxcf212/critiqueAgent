# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

You developed a solid preliminary design for Great Barrier Reef monitoring, featuring well-chosen orbital parameters and effective STK access simulations. Your introduction articulated the Australian context and user base clearly. To improve, correct technical misconceptions regarding launch site kinematics for retrograde orbits, provide quantitative decay calculations for end-of-life deorbiting, and maintain professional presentation by replacing informal sources like Wikipedia and proofreading for incomplete sentences.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You articulated the Great Barrier Reef mission rationale, user community (e.g., CSIRO, BOM), and single-satellite trade-offs clearly. To reach the top of Accomplished, integrate deeper literature benchmarking against existing Earth observation missions.

*Assessor reasoning:* The mission concept, justification for Australia (GBR monitoring), single-satellite architecture rationale, and end-users/operators are clearly articulated with relevant background references.
> Introduction: "Reef-monitoring satellites could also be used to report sea surface temperatures, thermal stress on coral, and bathymetry"  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You effectively applied STK and defined your sun-synchronous orbital elements. To reach Accomplished, ensure your launch site justification correctly accounts for retrograde inclination physics, fully detail required orbital maneuvers, and provide quantitative lifetime sizing for your drag sail.

*Assessor reasoning:* Major design areas are covered using STK and MATLAB/orbital elements. However, the launch selection misapplies the benefit of equatorial launch sites for a retrograde polar orbit (where Earth's rotation works against the launch vehicle). Furthermore, the deorbit analysis lacks quantitative decay time calculations for the drag sail at 600 km, and orbital manoeuvre requirements are treated superficially.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (6/10, Adequate)

Your conclusion adequately recaps the primary architecture selections. To reach Accomplished, synthesize key quantitative design metrics—such as access durations, required delta-V, and calculated decay timelines—into your final summary rather than relying on qualitative statements.

*Assessor reasoning:* The conclusion provides an adequate summary of the selected systems and findings, but remains somewhat generic without summarizing key quantitative design metrics (e.g., total access time, specific decay metrics).
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Headings and figures provide a readable structure. To achieve Accomplished, remove informal citations such as Wikipedia ([6]), resolve incomplete text fragments like the truncated sentence in the EOL section, and ensure full bibliographic formatting.

*Assessor reasoning:* The report structure is clear and readable, but relies heavily on raw Wikipedia data and includes an explicit Wikipedia citation ([6]), violating task formatting instructions. There is an incomplete sentence in the EOL section, and raw pasted tables/URLs in the bibliography detract from professional presentation.
> Launch: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
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
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Launch |

## Technical issues

- Launch: The author argues that launching near the equator from Kourou saves fuel/weight via Earth's rotational velocity. For a retrograde sun-synchronous orbit (inclination ~97.8°), launching eastward with Earth's rotation cannot be fully exploited, and high-latitude sites are often preferred for polar/retrograde launches to avoid severe dogleg manoeuvres or payload penalties.
- Mission Duration & EOL: A truncated sentence appears: 'utilising a large surface area to ‘ and is suitable...'. No quantitative analysis (drag area, ballistic coefficient, or orbital lifetime) is provided to verify compliance with the 25-year rule from 600 km.

## Next steps

1. Re-evaluate launch mechanics for retrograde sun-synchronous orbits (inclination ~97.8°), accounting for payload penalties and azimuth restrictions from equatorial versus high-latitude sites.
2. Perform quantitative orbital lifetime and drag-area calculations in the EOL section to mathematically prove compliance with the 25-year deorbit rule from 600 km.
3. Replace general sources and Wikipedia citations with peer-reviewed literature or official vehicle handbooks, ensuring all sentences and references are fully completed.

---
<sub>Run Input_2-Run_3-Eff_low-261118-113827 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18386/3869 | cost $0.014174 (incl. $0.001387 for the reused reference rubric+task structure) | 27.55s</sub>
