# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

Your single-satellite reef-monitor concept is well motivated and you covered all mission segments with STK evidence. To reach Accomplished you need to correct key orbital-mechanics numbers, sharpen operator/customer definition and conclusions, and improve referencing and figure presentation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You described your primary reef-monitoring mission and need well and justified one satellite in Introduction. For Accomplished, explicitly name operator versus customers and how each uses data from Australian facilities.

*Assessor reasoning:* Primary mission and need well described with refs. Single-sat rationale given. Operator vs customers not distinguished; operated from Australia facilities vague. Missing clear operator/customer identification.
> Introduction: "only one satellite is required"  
> Introduction: "allow marine and conservation scientists to more accurately predict"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You covered launch from Guiana, 600km orbit, manoeuvres and ground contacts with STK screenshots in Mission Design and Orbit. For Accomplished, fix inclination to SSO, sma, Kourou latitude, 580s access and RAAN logic, and include STK files.

*Assessor reasoning:* All sub-sections covered with STK screenshots and access table. Multiple technical errors: inclination 87.79 not SSO, sma 7171km wrong, Kourou latitude 45.05N, contact duration misread, RAAN logic flawed. No STK files evidenced.
> Mission Design: "launched from the Guiana Space Centre Spaceport"  
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924°"  

### C3 Conclusion (5/10, Adequate)

You summarised launch, orbit and ground station benefit in Conclusion. For Accomplished, draw detailed conclusions directly from your evidence with quantified performance rather than restating design.

*Assessor reasoning:* Summarises launch, orbit, ground station and benefit. Largely restates design with caveat on Vega E. Lacks detailed evidence-based conclusions or quantified performance.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

Your headings, executive summary and writing are clear and readable. For Accomplished, add informative captions and consistent numbering, and use proper full references instead of bare URLs and Wikipedia.

*Assessor reasoning:* Clear headings, exec summary, readable writing. Figures have minimal captions, inconsistent numbering. References use bare URLs and include Wikipedia which brief forbids. Formatting inconsistent.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 4  

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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: SSO inclination at 600km quoted as 87.79 deg; correct ~97.8 deg as per own plot. 87.79 deg is prograde and not sun-synchronous.
- Orbit: Semi-major axis 7171km for 600km altitude; 6371+600=6971km, 200km error.
- Launch: Kourou latitude quoted as 45.05 deg N; actual ~5.2 deg N. Invalidates two-windows-per-day argument detail.
- Ground Control & Communications: Mean access 580.786s (~9.7 min) described as almost twenty minutes; misinterpretation by factor 2.
- Orbit: RAAN 27.33 deg claimed to indicate launch facility location; RAAN does not equal launch longitude and explanation of J2 precession incomplete.

## Next steps

1. Recalculate and verify your orbit numbers in Orbit (inclination ~97.8 deg, sma 6971 km) and Kourou latitude and access-duration interpretation before finalising.
2. Clearly separate operator versus customers in Introduction and link each to Australia benefit with literature references.
3. Upgrade Conclusion to quantified evidence-based claims and fix Bibliography to full citations without Wikipedia plus consistent figure captions.

---
<sub>Run Input_2_d-Run_2-Eff_low-261118-124840 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14837/4857 | cost $0.002028 (incl. $0.001387 for the reused reference rubric+task structure) | 32.22s</sub>
