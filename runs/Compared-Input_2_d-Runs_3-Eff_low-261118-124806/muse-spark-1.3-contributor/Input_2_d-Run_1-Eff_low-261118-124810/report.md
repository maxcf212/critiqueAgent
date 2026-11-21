# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You produced a complete single-satellite GBR fluid-lensing concept with STK evidence across launch, orbit and ground segments. Your Introduction, Orbit, Launch, Ground Control & Communications and Conclusion cover all required areas. To reach Accomplished you need to correct critical technical errors and add detail, quantitative synthesis and consistent referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You did well defining coral reef monitoring need and justifying only one satellite is required. For Accomplished, clearly separate operator from customers and add detail on who operates and who uses data.

*Assessor reasoning:* Primary mission, need with refs, and single-sat rationale given. Users partly addressed as scientists and Australia facilities but operator vs customers not clearly distinguished, lacking detail.
> Introduction: "specifically for coral reef and ocean monitoring"  
> Introduction: "only one satellite is required"  
> Introduction: "allow marine and conservation scientists to more accurately predict"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You did well covering Vega E launch, 600 km orbit elements, STK views and Mt Pleasant accesses. For Accomplished, correct 87.79 deg to ~97.8 deg, Kourou latitude, RAAN claim and 20-min vs 9.7-min contacts, and strengthen coverage.

*Assessor reasoning:* All sub-topics covered with STK views, ground-track, access table and elements. Design undermined by major technical errors: SSO inclination, launch latitude, and weak swath/coverage analysis.
> Launch: "use the Vega E rocket as a launch vehicle"  
> Orbit: "altitude of 600km requires a mean inclination"  
> Image 4  

### C3 Conclusion (5/10, Adequate)

You summarised polar SSO, ground station location and Vega E risk well. For Accomplished, add specific quantitative synthesis from your evidence and clear forward recommendations, not generic statements.

*Assessor reasoning:* Summarises launch, orbit, ground station and benefit, notes Vega E risk. Generic, no quantitative synthesis or forward recommendations from evidence.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining"  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data"  

### C4 Report presentation (10/20, Adequate)

You used clear headings, abstract and labelled STK figures/tables with readable writing. For Accomplished, remove Wikipedia, make referencing consistent, and number all captions consistently.

*Assessor reasoning:* Clear headings, abstract, labelled STK figures/tables, readable writing. Downgraded for prohibited Wikipedia source, inconsistent ref formatting and some unnumbered captions.
> Executive Summary: "This report outlines the intended designs and procedures involved in the"  
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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 4 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: 600 km SSO inclination quoted as 87.7924 deg / 87.79 deg; correct J2 SSO ~97.8 deg. Plot shows 97-98 deg, contradicting table.
- Launch: Kourou latitude quoted as 45.05 deg N; actual ~5.2 deg N, invalidates two-windows-per-day claim reasoning.
- Ground Control & Communications: Claims average contact almost twenty minutes but STK table mean 580.786 sec (~9.7 min); misinterpretation.
- Orbit: RAAN 27.33 deg claimed to indicate launch facility location; RAAN is orbit plane orientation, not site latitude.

## Next steps

1. Correct Orbit table to ~97.8 deg SSO inclination, fix Kourou latitude to ~5.2 deg N, and align RAAN and contact-time interpretation with your STK plots and Image 4 access table.
2. Clearly distinguish operator vs customers in Introduction and strengthen swath/revisit analysis to justify single-satellite coverage of the GBR.
3. Replace Wikipedia source, fix reference formatting and caption numbering, and add quantitative conclusions and forward recommendations in Conclusion.

---
<sub>Run Input_2_d-Run_1-Eff_low-261118-124810 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14818/4967 | cost $0.003198 (incl. $0.001387 for the reused reference rubric+task structure) | 29.73s</sub>
