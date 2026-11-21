# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 65 / 100 (65%)**

You produced a good reef-monitoring SSO concept with credible STK work. Your Introduction and mission design are strong, but orbit detail errors, an unproven Vega E baseline, a generic Conclusion and referencing flaws limit you. Fixing these will lift you to the top of each rubric band.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You did well in Introduction stating your Earth observation mission for coral reef and ocean monitoring, justifying one satellite for simplicity, and naming users like CSIRO and BOM with literature refs. To reach the top of Accomplished, make your operator role explicit.

*Assessor reasoning:* Primary mission, need, single-spacecraft rationale and users all addressed with literature refs. Operator role less explicit but adequate for high standard.
> Introduction: "Earth observation satellite – specifically for coral reef and ocean monitoring"  
> Introduction: "only one satellite is required. This also just allows for simplicity"  
> Introduction: "used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

You did well in Mission Design - Launch/Orbit and Ground Control & Communications covering Vega E from Guiana, 600km 97.7924 deg SSO, manoeuvres, Mean Duration accesses in Image 4, and 5-yr drag-sail EOL with STK screenshots. For higher Accomplished, fix RAAN-site confusion, static Argument of Latitude, missing LTAN, and mitigate Vega E risk.

*Assessor reasoning:* Launch, SSO elements, manoeuvre, ground station accesses via STK and 5-yr EOL with drag sail covered with screenshots and calculations, though some technical slips remain.
> Mission Design - Launch: "Vega E rocket as a launch vehicle – launched from the Guiana"  
> Mission Design - Orbit: "altitude of 600km requires a mean inclination of 97.7924"  
> Ground Control & Communications: "Mean Duration"  
> Image 4  

### C3 Conclusion (5/10, Adequate)

Your Conclusion summarises launch, orbit, ground station and benefit starting 'fully described satellite configuration...'. For Accomplished, move beyond generic summary to detailed conclusions directly synthesised from your STK results, calculations and trade-offs.

*Assessor reasoning:* Summarises launch, orbit, ground station and benefit but generic, adds caveat on Vega E, lacks detailed evidence-based synthesis.
> Conclusion: "fully described satellite configuration has been constructed. The initial problem"  

### C4 Report presentation (10/20, Adequate)

Your Executive Summary 'This report outlines...' and headings make the report readable. For Accomplished, give all figures numbers/titles, format tables consistently, and fix Bibliography 'https://en.wikipedia.org...' bare URLs and banned Wikipedia use with proper citations.

*Assessor reasoning:* Clear headings and readable writing, but figures lack numbers/titles, tables poorly formatted, Wikipedia used despite ban, referencing inconsistent.
> Executive Summary: "This report outlines the intended designs and procedures involved"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Mission Design |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design - Orbit: RAAN 27.33 deg claimed to indicate launch facility location; RAAN is orbit plane orientation, not site, and will not equal site longitude.
- Mission Design - Orbit: Circular orbit described with Argument of Latitude as static element; u varies rapidly and LTAN/local time not specified for SSO.
- Mission Design - Launch: Baseline Vega E in 2025 was unflown/developmental; reliance on future SSMS replication adds schedule risk, acknowledged but weakly mitigated.
- Bibliography: Wikipedia cited for launch manifest despite explicit ban; reference list is bare URLs without proper citation style.

## Next steps

1. In Mission Design - Orbit, correct RAAN 27.33 deg and Argument of Latitude: explain RAAN/LTAN properly and give LTAN/local time for your 600km SSO.
2. Strengthen your Vega E from Guiana baseline with flight status and a backup launcher/SSMS option to address schedule risk you noted.
3. In Conclusion and throughout, add numbered figure titles, clean table formatting, and replace bare URLs/Wikipedia with proper in-text citations and reference list.

---
<sub>Run Input_2-Run_2-Eff_low-261118-112642 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 25535/6843 | cost $0.003606 (incl. $0.001387 for the reused reference rubric+task structure) | 78.1s</sub>
