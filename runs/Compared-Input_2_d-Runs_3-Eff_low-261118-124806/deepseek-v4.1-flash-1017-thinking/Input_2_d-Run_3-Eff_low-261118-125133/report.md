# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 54 / 100 (54%)**

Your report is well structured and covers most mission-design elements, with a clear rationale and useful STK screenshots. However, key technical errors (SSO inclination, Kourou latitude, contact duration) and missing software files weaken the design evidence. References and figure formatting also need work. The feedback below is specific and actionable; marks are unchanged.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 6 / 10 | 12 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

You clearly explain the reef-monitoring need, justify a single spacecraft, and identify user groups with references. To reach the top of Accomplished, make the operator and customer roles explicit (e.g., who tasks the spacecraft and who receives data) and support each claim with specific literature rather than general statements.

*Assessor reasoning:* Mission need, rationale, single-spacecraft choice and user groups are described with references. Operator/customer roles are only implicit, so not top of range.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "allow marine and conservation scientists to more accurately predict and react to coral bleaching events"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground control, communications, duration and EOL with STK screenshots, but several technical errors undermine the design: the 600 km SSO inclination should be ~97.8° retrograde, Kourou is ~5.2°N not 45.05°N, and 580.786 s is ~9.7 min not 'almost twenty'. Correct these, explain RAAN and eclipse, remove the low-resolution-desirable contradiction, and include STK/PIGI files. That evidence is needed for Accomplished.

*Assessor reasoning:* All major design areas are covered with STK screenshots, but the SSO inclination is wrong, Kourou latitude is wrong, contact duration is misread, and STK files are absent. Design logic is therefore only adequate.
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Launch: "with a latitude of $ 45.05^{\circ} $N"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods"  

### C3 Conclusion (5/10, Adequate)

Your conclusion summarises the launch vehicle, orbit and ground station, but it omits EOL, mission duration, the single-satellite rationale and users, and some statements are generic. To move to Accomplished, tie each conclusion directly to your evidence and cover all major design decisions, including limitations and why the design benefits Australia.

*Assessor reasoning:* Conclusion summarises launch, orbit and ground station, but omits EOL, duration, single-satellite rationale and users; some statements are generic.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination"  

### C4 Report presentation (12/20, Adequate)

Your structure, headings and executive summary are clear, but figure/table numbering is inconsistent, Image 3 lacks a caption, and the bibliography includes Wikipedia and bare URLs. For Accomplished, use consistent formatting, caption and number every figure/table, and ensure in-text citations match a properly formatted reference list without prohibited sources.

*Assessor reasoning:* Structure, headings and executive summary are clear, but figures/tables are inconsistently numbered, one plot lacks a caption, and references are bare URLs including prohibited Wikipedia.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 3  

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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Images 1-5 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: 600 km SSO inclination is stated as 87.79°, but should be about 97.8° retrograde; 87.79° is prograde and not sun-synchronous.
- Launch: Kourou latitude is given as 45.05°N; actual latitude is about 5.2°N, invalidating the launch-window reasoning.
- Ground Control & Communications: Mean access duration 580.786 s is about 9.7 minutes, not 'almost twenty minutes'.
- Orbit: RAAN 27.33° is said to indicate launch-site location; RAAN depends on launch time and azimuth, not site alone.
- Orbit: SSO is described as having constant sunlight; sun-synchronous orbits still experience eclipse periods.
- Orbit: Text says high altitude gives low resolution 'which is also desirable', contradicting the design aim.
- Report: No STK/PIGI files are supplied, and the bibliography uses Wikipedia and bare URLs.

## Next steps

1. Correct the orbital and launch-site errors: change the 600 km SSO inclination from 87.79° to about 97.8° retrograde, fix Kourou's latitude to ~5.2°N, and revise the launch-window reasoning accordingly.
2. Recheck STK outputs: report mean access duration as ~9.7 min (580.786 s), not 'almost twenty minutes'; explain that RAAN depends on launch time and azimuth, note SSO eclipse periods, and remove the claim that low resolution is desirable.
3. Strengthen evidence and presentation: supply STK/PIGI files, number and caption every figure and table (including Image 3), and replace Wikipedia and bare URLs with properly cited references.

---
<sub>Run Input_2_d-Run_3-Eff_low-261118-125133 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14230/8659 | cost $0.005419 (incl. $0.001387 for the reused reference rubric+task structure) | 49.12s</sub>
