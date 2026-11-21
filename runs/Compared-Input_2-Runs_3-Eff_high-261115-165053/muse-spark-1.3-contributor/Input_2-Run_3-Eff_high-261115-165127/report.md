# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 74 / 100 (74%)**

You produced a solid SSO EO mission for GBR monitoring with clear concept, justified Vega E launch from Kourou, correct 600km SSO geometry, and STK-supported ground analysis. All task elements are completed. To lift your report, strengthen quantitative conclusions and professional referencing and presentation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 6 / 10 | 12 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You clearly defined your primary mission (coral reef EO for fluid lensing) in Introduction, justified need (bleaching/acidification), argued single spacecraft for simplicity, and identified users (CSIRO, BOM). Well-cited. To maintain Accomplished, keep this level of specific detail and referencing.

*Assessor reasoning:* Primary mission (coral reef EO with fluid lensing), rationale (bleaching, acidification), single spacecraft justification, and users/operator clearly stated with citations. Adequately detailed for Accomplished.
> Introduction: "coral reef and ocean monitoring. The satellite must provide images for a fluid lensing tool"  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity"  
> Introduction: "likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

You justified Vega E from Guiana Space Centre for polar piggyback capability, set a 600km SSO with inclination 97.79 deg, explained J2-driven precession, and provided STK evidence Images 1-5 and Mt Pleasant access report with EOL drag sail. Next level requires retaining evidence but adding explicit RAAN/LTAN calculation.

*Assessor reasoning:* Launch site/vehicle (Vega E, Kourou), rationale (piggyback, polar capability), SSO polar retrograde orbit with a,i,Ω,e and altitude, J2-driven precession explained, EOL maneuver identified as drag sail, ground station selected with STK access stats and ground tracks. Software evidence present via Images 1-5 and tables.
> Mission Design - Launch: "Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport"  
> Mission Design - Orbit: "altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "Satellite-ZYZZsat-To-Facility-Mt_Pleasant_Radio_Observatory: Access Summary Report"  

### C3 Conclusion (6/10, Adequate)

Your Conclusion in Conclusion recaps launch, orbit, ground station, and EOL benefit but is short and generic versus your body data. For Accomplished you need detailed conclusions drawn from your own results - e.g., revisit altitude-inclination table, access statistics, and Vega E risk.

*Assessor reasoning:* Conclusion summarizes launch, orbit, ground station and EOL and notes risks (Vega E not yet built) and benefit. Appropriate but relatively generic and short compared to body, lacks quantitative recap.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle"  

### C4 Report presentation (12/20, Adequate)

You used clear engineering structure, Executive Summary overview, and labeled tables/screenshots. To reach Accomplished, use fully professional writing, consistent formatting throughout, and replace Wikipedia (Timeline of spaceflight) with acceptable primary references and consistent in-text citations.

*Assessor reasoning:* Clear engineering structure with contents, exec summary, headings, labeled tables and STK screenshots. Some formatting inconsistencies (OCR table breaks, typos, Wikipedia cited as source contrary to task note) and informal nicknaming, keeping it Adequate rather than fully professional.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction"  
> Image 3  

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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Executive Summary |

## Technical issues

- Bibliography: Uses Wikipedia (Timeline of spaceflight) as primary source for launch selection despite task stating Wikipedia not acceptable.
- Mission Design - Orbit: RAAN value 27.33° stated as location of launch facility without calculation; RAAN description oversimplified and Argument of Latitude used but not fully explaining SSO LTAN.

## Next steps

1. Replace Wikipedia with primary sources for launch and orbit trade-offs and add hand calculations for RAAN/LTAN selection to fully justify your SSO.
2. Expand conclusion with quantitative recap from your tables and Images 1-5 and explicit risk mitigations to move from generic to detailed evidence-based conclusions.
3. Tighten report presentation: consistent figure/table labeling, formal tone, and IEEE/Cite referencing to meet Accomplished professional standard.

---
<sub>Run Input_2-Run_3-Eff_high-261115-165127 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14825/4171 | cost $0.002013 (incl. $0.001387 for the reused reference rubric+task structure) | 15.16s</sub>
