# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 71 / 100 (71%)**

You produced a solid SSO mission for GBR reef monitoring with clear STK evidence. You justified a single spacecraft, CSIRO/BOM users, Guiana launch on Vega E, 600km/97.79deg SSO, Mount Pleasant contacts and 5-year EOL with drag sail. Well-structured work, limited by launch source credibility and missing propulsion/deorbit analysis.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Accomplished | 7 / 10 | 14 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You clearly defined primary mission for coral reef fluid-lensing monitoring, rationale on bleaching and GBR value, and justified single satellite simplicity. Users CSIRO/BOM identified well. To reach top of Accomplished, add detailed payload requirements and peer-reviewed references instead of URLs.

*Assessor reasoning:* Primary mission (reef/ocean monitoring with fluid lensing), rationale (bleaching, acidification, GBR value) and single-spacecraft justification explained. Users/operators identified (CSIRO, BOM, university/government). References included, though some are non-academic URLs.
> Introduction: "coral reef and ocean monitoring. The satellite must provide images for a fluid lensing tool"  
> Introduction: "Only one satellite is required. This also just allows for simplicity in communications"  
> Introduction: "would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

You provided launch (Vega E, Guiana), 600km/97.7924° SSO, a=6971km, ground station Mount Pleasant with access stats and STK Figures like Image 4. For higher Accomplished, fix RAAN interpretation, justify launch vehicle with primary sources, and add calculations for manoeuvres and drag-sail EOL.

*Assessor reasoning:* Launch site, vehicle, orbit type (SSO retrograde polar), characteristics, Keplerian elements, maneuver (direct injection, EOL drag sail), ground station and access statistics with STK screenshots provided. Some technical inaccuracies (RAAN as launch site, Vega E not yet flown) and reliance on Wikipedia timeline limit depth.
> Launch: "Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport"  
> Orbit: "altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous" *(quote not found in submission)*  
> Orbit: "Semi-major axis (a) 6971km Earth radius of 6371km plus a proposed altitude of 600km"  
> Ground Control & Communications: "Mount Pleasant Radio Observatory"  
> Image 4  

### C3 Conclusion (7/10, Accomplished)

Your conclusion summarises launch, polar SSO for illumination, ground station trade and Vega C contingency linked to bleaching need. To strengthen, synthesize quantitative results from orbit access and duration analysis and state explicit outcomes rather than general statements.

*Assessor reasoning:* Summarises launch, orbit, ground station and EOL trade, links back to mission need and notes contingency if Vega E unavailable. Not generic.
> Conclusion: "fully described satellite configuration has been constructed. The initial problem of not catching coral bleaching"  
> Conclusion: "Alternatives include the earlier Vega C launcher. A polar sun-synchronous orbit allows for consistent illumination"  

### C4 Report presentation (14/20, Accomplished)

Clear engineering structure with Executive Summary, contents, labelled STK 3D views and access tables, readable writing. To reach top of Accomplished, use consistent citation style throughout, replace Wikipedia/NOAA URLs with academic sources, and ensure reference list matches in-text citations.

*Assessor reasoning:* Clear engineering structure with executive summary, contents, sections, figures labelled, access table. Grammar readable; OCR artefacts not penalised. References listed but citation style inconsistent and URLs used, including Wikipedia.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Mission Design: "STK 3D view of orbit: 12 hours apart"  
> Bibliography: "https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification"  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Executive Summary |

## Technical issues

- Orbit: Claims RAAN initial value indicates launch facility location; RAAN defined by inertial frame, not launch latitude. Inclination-altitude relation plot correct but argument of latitude used instead of true anomaly without full Keplerian set.
- Launch: Selected Vega E whose first launch planned 2024 and relies on future 2025 SSMS mission; justification based on Wikipedia 'Timeline of spaceflight' not primary source; piggyback orbit matching assumed.
- Mission Duration & EOL: No delta-v or drag-sail sizing calculation; uncontrolled deorbit from 600km with drag sail needs analysis of deorbit time <25yr rule; small-sat without propulsion claimed but drag sail deployment still requires system.

## Next steps

1. Replace Wikipedia timeline with ESA/Arianespace primary sources and validate Vega E availability; assess Vega C backup with orbit-matching constraints.
2. Correct orbital mechanics: show full Keplerian set with true anomaly, and clarify RAAN is inertial, not launch latitude. Size drag sail and show deorbit <25yr with delta-v/drag budget.
3. Upgrade referencing format and strengthen literature support for fluid-lensing requirements and SSO lighting rationale.

---
<sub>Run Input_2-Run_2-Eff_high-261115-165113 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14989/4554 | cost $0.002106 (incl. $0.001387 for the reused reference rubric+task structure) | 13.98s</sub>
