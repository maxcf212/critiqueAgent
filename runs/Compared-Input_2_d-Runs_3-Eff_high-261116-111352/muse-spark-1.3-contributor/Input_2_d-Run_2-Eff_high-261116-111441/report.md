# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 44 / 100 (44%)**

You developed a clear coral reef monitoring concept with STK screenshots supporting launch, SSO, and Mount Pleasant ground station choices. To reach Accomplished, you must correct fundamental orbit and ground-contact numbers, name your operator/users explicitly, and provide quantified conclusions with proper referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You did well in Introduction and Executive Summary to define coral reef monitoring need with the 2016 bleaching evidence and justify one satellite. For Accomplished, explicitly name your operator and customers beyond implied scientists, with detailed roles and literature references.

*Assessor reasoning:* Primary mission, need with refs, and single-satellite rationale given. Users partially addressed: customers implied as scientists, operator only vague as Australia facilities, no named operator. Lacks specific detail for operator/customers.
> Executive Summary: "construction of a Earth observation satellite – specifically for coral reef and ocean monitoring"  
> Introduction: "In 2016, a bleaching killed 30 percent of the reef’s coral"  
> Introduction: "Thus, only one satellite is required"  
> Introduction: "would allow marine and conservation scientists to more accurately predict and react"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

You covered launch with Vega E, SSO choice, Mount Pleasant station and 5-year life with STK screenshots well. For Accomplished, correct semi-major axis to ~6971km, inclination to ~97.8deg, Kourou latitude, 580s contact interpretation and RAAN reasoning, and quantify manoeuvres/EOL with STK files and hand calculations.

*Assessor reasoning:* All major design areas addressed with STK screenshots and tables, but contains major technical errors in semi-major axis, inclination, latitude, and contact duration interpretation. Manoeuvres and EOL only qualitatively described, no STK files evidenced.
> Launch: "will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "The most suitable orbit for this task would be a low-earth sun-synchronous orbit"  
> Ground Control & Communications: "a Tasmanian facility is selected – the Mount Pleasant Radio Observatory"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan"  

### C3 Conclusion (5/10, Adequate)

Your Conclusion usefully summarises polar SSO, Vega E with availability caveat, ground station and reef benefit. For Accomplished, move beyond restating design to give detailed, evidence-based conclusions with quantitative synthesis and critical evaluation of performance against mission needs.

*Assessor reasoning:* Conclusion summarises launch, orbit, ground station and benefit, with caveat on Vega E availability. Drawn from report evidence but generic, restates design without new quantitative synthesis or critical evaluation.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle"  

### C4 Report presentation (10/20, Adequate)

Your report reads well with clear headings, contents and Executive Summary and logical flow. For Accomplished, number and title all figures/tables consistently like Image 4, format in-text citations properly, and replace Wikipedia with allowed sources in a correct bibliography.

*Assessor reasoning:* Clear headings, contents, executive summary and logical flow, readable writing. Figures/tables lack numbers and consistent titles, bibliography malformed, Wikipedia used despite prohibition, in-text citations loosely formatted.
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

- Orbit: Semi-major axis 7171km for 600km altitude wrong; should be ~6971km (6371+600).
- Orbit: Inclination 87.7924 deg for 600km SSO wrong; should be ~97.8 deg as in Image 3 plot; <90 deg is prograde not retrograde SSO.
- Launch: Kourou latitude stated as 45.05 deg N, actual ~5.2 deg N; invalidates two-windows-per-day claim logic.
- Ground Control & Communications: Mean duration 580s (~9.7min) misreported as almost twenty minutes; max only 770s.
- Orbit: RAAN 27.33 deg claimed to indicate launch facility location; RAAN selection reasoning incorrect.
- Bibliography: Uses Wikipedia for launch manifest despite task ban; reference list malformed.

## Next steps

1. Recalculate and fix your Orbit values: semi-major axis for 600km altitude, 97.8deg SSO inclination, and correct RAAN reasoning, checking Image 3 against your table.
2. Correct Launch and Ground Control numbers: Kourou latitude and two-windows logic, and report mean 580s as ~9.7min not almost twenty minutes with correct interpretation.
3. Name operator and customers in Introduction and replace Wikipedia in Bibliography with allowed sources, numbering figures/tables and formatting citations.

---
<sub>Run Input_2_d-Run_2-Eff_high-261116-111441 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14955/9669 | cost $0.003001 (incl. $0.001387 for the reused reference rubric+task structure) | 54.54s</sub>
