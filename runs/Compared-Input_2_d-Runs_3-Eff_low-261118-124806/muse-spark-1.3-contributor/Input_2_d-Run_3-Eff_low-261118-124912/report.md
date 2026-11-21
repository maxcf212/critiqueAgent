# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 48 / 100 (48%)**

You proposed a clear single-satellite reef-monitoring concept with STK-supported SSO and ground-station analysis. Your strength is covering all required topics, but critical orbit-mechanics errors and vague users and referencing keep you at Adequate. Fixing those will lift you toward Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You did well in your Introduction stating your fluid lensing mission, bleaching need, and that only one satellite is required. For Accomplished, distinguish your operator versus customers beyond Australian facilities and add detailed, referenced descriptions.

*Assessor reasoning:* Primary mission, need with bleaching statistics, and single-spacecraft rationale given. Users only vague: Australian facilities and marine scientists mentioned, no clear operator vs customers distinction, lacking detail and specific references.
> Introduction: "fluid lensing has been used in combination with AI analysis"  
> Introduction: "only one satellite is required"  
> Executive Summary: "is operated and accessed from Australia ground facilities"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You covered launch with Vega E, 600 km orbit, maneuvers and ground control with STK screenshots and Image 4. For Accomplished, you must correct your 87.7924 deg to ~97.8 deg, Kourou 45.05 deg N error, and RAAN logic with accurate evidence.

*Assessor reasoning:* All sub-topics covered with STK screenshots, access table and plots. Significant technical errors: 87.79 deg not SSO at 600km, Kourou latitude 45.05N, RAAN logic flawed, future vehicle speculative. Design inconsistent but adequate.
> Launch: "will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924°"  
> Image 4  

### C3 Conclusion (5/10, Adequate)

Your Conclusion usefully summarises your Vega E selection, orbit, ground station and Vega E risk. For Accomplished, move beyond repeating your proposal to detailed conclusions drawn from your evidence with quantified performance.

*Assessor reasoning:* Summarises orbit, launch, ground station and benefit, notes Vega E risk. Generic, short, repeats proposal without detailed evidence-based findings or quantified performance conclusions.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected"  

### C4 Report presentation (8/20, Adequate)

You used clear headings and an executive summary with readable writing. For Accomplished, consistently caption figures/tables like your DN path plots, fix formatting, and use proper in-text citations without Wikipedia URLs.

*Assessor reasoning:* Clear headings and executive summary, readable. Figures/tables inconsistently captioned, formatting uneven. References bare URLs, includes Wikipedia explicitly prohibited, citation style poor.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Design: "DN path for orbits 1-15"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: Inclination 87.79 deg for 600km SSO is wrong; should be ~97.8 deg as own Image 3 shows ~97.8 deg at 600km.
- Launch: Kourou latitude stated as 45.05 deg N, actual ~5.2 deg N; invalidates two-windows-per-day claim.
- Orbit: RAAN 27.33 deg tied to launch facility location misunderstands RAAN/LSTAN for SSO.
- Bibliography: Uses Wikipedia Timeline of spaceflight despite task banning Wikipedia.

## Next steps

1. Correct your 600 km SSO to ~97.8 deg as your Image 3 shows and fix Kourou latitude to ~5.2 deg N and RAAN/LSTAN logic with textbook references.
2. Clarify in your Introduction who operates you spacecraft versus who are customers, adding specific Australian agencies and literature on bleaching and fluid lensing.
3. Upgrade presentation: caption all figures/tables consistently, replace bare URLs and prohibited Wikipedia with proper cited sources.

---
<sub>Run Input_2_d-Run_3-Eff_low-261118-124912 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14805/4701 | cost $0.001992 (incl. $0.001387 for the reused reference rubric+task structure) | 31.33s</sub>
