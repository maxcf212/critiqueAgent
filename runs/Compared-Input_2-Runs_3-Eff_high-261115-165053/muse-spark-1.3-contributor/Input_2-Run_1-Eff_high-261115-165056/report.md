# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 75 / 100 (75%)**

You produced a solid preliminary SSO reef-monitoring design with clear Australian benefit. Your single-satellite rationale, STK-supported orbit and ground-station analysis, and defined users/operators are strong. To strengthen the report, correct orbital-mechanics details, justify launch vehicle choice with proven flight history, add quantitative EOL decay, and improve referencing and figure numbering.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 6 / 10 | 12 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You did well framing the primary mission as fluid lensing reef monitoring for bleaching, and clearly justifying one satellite and users like CSIRO, BOM and government. Your literature links support the rationale. For full Accomplished, add more specific user data needs and cite peer-reviewed sources consistently.

*Assessor reasoning:* Primary mission reef/ocean monitoring with fluid lensing, rationale bleaching, single-sat justification, users CSIRO/BOM/University/Gov clearly stated with literature links.
> Introduction: "fluid lensing has been used in combination with AI analysis to detect colour/tone changes"  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity"  
> Introduction: "likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

You provided detailed launch from Guiana on Vega E, SSO parameters a=6971km, 600 km, i=97.79deg, e=0, STK 3D views and ground tracks, and 580s mean access via Mount Pleasant. To reach top of Accomplished, provide decay calculations for drag-sail deorbit, correct RAAN and launch-window reasoning, and quantify swath coverage.

*Assessor reasoning:* Launch site Guiana, vehicle Vega E/Vega C evaluated; SSO orbit defined with altitude 600km, i=97.79deg, e=0, a=6971km, RAAN drifting, argument of latitude; STK 3D views, ground tracks, access report 580s mean; EOL drag sail discussed. Detailed and software-supported.
> Mission Design - Launch: "proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Mission Design - Orbit: "Semi-major axis (a) 6971km Earth radius of 6371km plus a proposed altitude of 600km"  
> Ground Control & Communications: "Mount Pleasant Radio Observatory). This station is current owned"  
> Image 1  

### C3 Conclusion (7/10, Accomplished)

Your Conclusion synthesises launch, polar SSO with constant sun angle, ground station, and EOL, linking back to bleaching monitoring and 2025 launch risk. To strengthen to higher Accomplished, explicitly evaluate trade-offs and key performance against mission requirements with numbers from your design.

*Assessor reasoning:* Synthesizes launch, orbit, ground station and EOL findings, restates 2025 launch and Vega E risk mitigation, links design back to bleaching monitoring goal.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  
> Conclusion: "polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle"  

### C4 Report presentation (12/20, Adequate)

You used a clear structure with Executive Summary, TOC and headed sections; writing is readable. To move from Adequate to Accomplished, number all figures/tables consistently for cross-reference, format references in-text with a consistent style instead of raw URLs, and proofread for grammar.

*Assessor reasoning:* Logical headings, TOC, abstract present; figures labelled but not numbered consistently, some table OCR artefacts, reference list uses raw URLs not consistent citation style, minor grammar errors.
> Executive Summary: "Key features of this satellite configuration include a direct launch into a retrograde sun-synchronous polar orbit"  
> Mission Design - Launch: "Small Satellites Mission Service (SSMS) piggyback mission."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design - Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design - Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design - Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Executive Summary |

## Technical issues

- Mission Design - Orbit: States RAAN initial value indicates launch facility location - RAAN determined by launch time/ascending node crossing, not site latitude; also Argument of Latitude u=0 listed as static rather than time-varying.
- Mission Design - Launch: Selects Vega E (first flight 2024 unproven in 2020 report) and claims two launch windows per day because latitude 5.05deg N < target inclination, conflates inclination constraint with RAAN window.
- Mission Design - Orbit: Altitude 600 km drag-sail passive deorbit within 25-year guideline plausible but no decay calculation shown; swath vs reef width discussion qualitative.

## Next steps

1. In Mission Design - Orbit, correct that RAAN is set by launch time not facility latitude, and show argument of latitude u as time-varying; remove static u=0 from elements table.
2. In Mission Design - Launch, justify Vega vehicle selection against 2020 flight heritage (Vega C vs unproven Vega E) and fix the two-windows-per-day explanation to address RAAN alignment, not just latitude < inclination.
3. In Mission Duration & EOL and Ground Control, add a hand calculation or STK lifetime run for the drag sail at 600 km and quantify swath vs reef coverage and contact budget to support your 580s mean access claim.

---
<sub>Run Input_2-Run_1-Eff_high-261115-165056 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14907/4511 | cost $0.003116 (incl. $0.001387 for the reused reference rubric+task structure) | 16.63s</sub>
