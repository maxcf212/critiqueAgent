# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 73 / 100 (73%)**

You delivered a strong, well-evidenced GBR monitoring mission with a clear purpose, SSO design, and good STK support. Your Introduction and Main Body are accomplished, and Conclusion is specific. Presentation is adequate - structure is clear but figure labelling and referencing limited your score.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

You did well in Introduction: primary mission of reef monitoring with fluid lensing, need with 30% loss, single spacecraft for simplicity, and users CSIRO/BOM. To reach 10/10, add more detailed literature and deeper discussion of why one spacecraft meets temporal resolution.

*Assessor reasoning:* Primary mission (reef monitoring with fluid lensing) and need (bleaching, 30% loss) clearly described. Single spacecraft justified by temporal resolution. Operator/customers identified. References included though limited.
> Introduction: "Earth observation satellite – specifically for coral reef and ocean monitoring"  
> Introduction: "only one satellite is required. This also just allows for simplicity in communications"  
> Introduction: "would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Strong work in Mission Design: you justified Vega E from Guiana Space Centre with alternatives, defined 600 km SSO with i=97.79°, a=6971 km in your COEs table, and used STK Images 4-5 and access stats with Tasmania Mount Pleasant station. For 10/10, add launch performance calculations and complete maneuver analysis.

*Assessor reasoning:* Launch site/vehicle justified with alternatives (Vega VV18, Falcon 9), equator benefit. SSO polar retrograde 600 km, i=97.79°, COEs table with argument of latitude for circular orbit, J2 explanation, period. Maneuver noted as EOL only. Ground station access report with stats ~580s mean, ground tracks Images 4-5. Duration 5 years STK 2025-2030, drag-sail deorbit. STK screenshots support design.
> Launch: "will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport"  
> Orbit: "Semi-major axis (a) 6971km Earth radius of 6371km plus a proposed altitude of 600km"  
> Ground Control & Communications: "Tasmanian facility is selected – the Mount Pleasant Radio Observatory"  
> Image 3  

### C3 Conclusion (7/10, Accomplished)

Your Conclusion effectively synthesizes your evidence: Vega E fallback to Vega C, polar SSO for illumination, Mt Pleasant for long contacts, and deorbit with drag sail. To strengthen to 9-10, expand why this meets the GBR need and note limitations or future work.

*Assessor reasoning:* Conclusion synthesizes launch (Vega E fallback Vega C), orbit, ground station, and mission goal (prevent bleaching). Specific to evidence presented, not generic, though brief.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle"  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations"  

### C4 Report presentation (10/20, Adequate)

Report structure is logical with Executive Summary and TOC and readable writing. To move from Adequate to Accomplished, ensure all figures/tables are consistently numbered and labelled (e.g., STK 3D views, access table), and replace Wikipedia in Bibliography with primary sources with consistent citation format.

*Assessor reasoning:* Clear engineering structure with exec summary, TOC, sections. Figures/tables present but numbering inconsistent (STK 3D view, unlabeled tables). Grammar readable. Fails R15 - Wikipedia cited as source. References formatting inconsistent.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Image 1  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Executive Summary |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | yes | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Image 1 |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Orbit: Uses Argument of Latitude u=0° instead of standard ω and ν for circular orbit; RAAN 27.33° justified as launch facility longitude is non-standard definition (RAAN should be inertial, not launch longitude).
- Launch: Selects Vega E (first flight planned 2024, not yet built at report time - acknowledges risk) but does not compute required performance or piggyback mass.
- Ground Control & Communications: Access report duplicates entry at 13:00:32 and typo start time '9:38:38.911' on wrong date (Feb 2025 vs 4 Feb) indicates STK table artefact; mean duration calculation includes duplicate.

## Next steps

1. Fix reference quality: replace Wikipedia link in Bibliography with peer-reviewed or agency sources and ensure in-text citations match reference list.
2. Standardize all figures/tables with consecutive numbers, titles, and source notes - especially Images 1-5 and access report - and check Executive Summary overview is concise.
3. For future designs, add quantitative launch performance and clearer orbital element definitions (use ω and ν for circular orbit) to fully support vehicle and orbit choices.

---
<sub>Run 20261112-055808-543_Input_2_md_r2 | rubric=meta/muse-spark-1.3-contributor, task=meta/muse-spark-1.3-contributor, marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 13204/2604 | cost $0.001841 | 39.6s</sub>
