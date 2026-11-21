# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 66 / 100 (66%)**

You produced a competent single-satellite SSO concept for coral reef and ocean monitoring with strong STK evidence. Your launch, orbit and ground-contact analysis is coherent, but operator definition, orbital formalism, EOL quantification and referencing need strengthening to lift your report.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You described reef monitoring need and why only one satellite is required well. To reach Accomplished, separate you as operator from customers CSIRO/BOM and detail funding and operations with literature support.

*Assessor reasoning:* Primary mission, need and single-spacecraft rationale well described with refs. Operator vs customers conflated, funding vague, no clear operator. Meets most but lacks specific detail.
> Introduction: "specifically for coral reef and ocean monitoring"  
> Introduction: "only one satellite is required"  
> Introduction: "used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

You did well with Guiana launch choice, 600km 97.7924 deg SSO and ten-minute contacts with STK plots. To stay securely Accomplished, fix equatorial SSO benefit, RAAN 27.33 deg claim, u=0 deg set, Mt Pleasant compatibility and EOL calculations.

*Assessor reasoning:* All major requirements addressed with STK 3D, ground tracks, access table and SSO plot. Design coherent and justified, though some technical simplifications/errors remain.
> Launch: "launched from the Guiana Space Centre Spaceport"  
> Orbit: "altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "average contact duration of almost ten minutes was achieved"  

### C3 Conclusion (5/10, Adequate)

You linked launch, polar SSO illumination, ground station and benefit. For Accomplished, expand beyond generic summary to detailed conclusions synthesising your quantified performance and design evidence.

*Assessor reasoning:* Summarises launch, orbit, ground station and benefit, linked to evidence. Brief and partly generic with caveat on Vega E, lacks quantified performance synthesis.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans"  

### C4 Report presentation (8/20, Adequate)

Your headings and writing are readable with useful data displays. For Accomplished, add figure numbers/titles, consistent table formatting, executive summary, and replace Wikipedia with properly matched citations.

*Assessor reasoning:* Clear headings and readable writing with figures/tables, but figures lack numbers/titles, tables poorly formatted, Wikipedia used despite ban and refs incomplete/inconsistent.
> Image 4  
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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Equatorial launch advantage claimed for retrograde SSO; high-inclination launch from Kourou needs plane change/dogleg, benefit minimal.
- Orbit: RAAN 27.33 deg stated to indicate launch facility location is incorrect; RAAN defined by LTAN/time, not launch longitude.
- Orbit: Circular orbit described via Argument of Latitude u=0 deg without epoch/LTAN; incomplete classical set, no period/repeat cycle.
- Ground Control & Communications: Mt Pleasant Radio Observatory radio-astronomy facility assumed suitable for TT&C without link, frequency or compatibility analysis.
- Mission Duration & EOL: Uncontrolled drag-sail deorbit from 600 km SSO within 25-year guideline not quantified; no delta-v, area, or lifetime calculation.

## Next steps

1. Clarify in your Introduction who operates and funds you versus customers like CSIRO/BOM, replacing vague governmental use with a named operator model.
2. Correct your Orbit section: explain RAAN/LTAN properly, give full epoch elements plus period/repeat, and quantify your drag-sail deorbit lifetime from 600 km.
3. Fix presentation by numbering and titling all figures/tables, removing Wikipedia and completing consistent in-text citations and reference list.

---
<sub>Run Input_2-Run_3-Eff_low-261118-112800 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 25559/6805 | cost $0.00245 (incl. $0.001387 for the reused reference rubric+task structure) | 75.34s</sub>
