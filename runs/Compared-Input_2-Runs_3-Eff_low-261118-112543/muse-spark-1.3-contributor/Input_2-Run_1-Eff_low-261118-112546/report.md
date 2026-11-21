# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 59 / 100 (59%)**

You proposed a well-motivated single-satellite GBR fluid-lensing mission with plausible SSO and STK access analysis. Your introduction and structure are strong, but launch rationale and orbital mechanics contain errors and quantitative support is limited. Focus on correcting mechanics, adding calculations, and synthesising conclusions with proper referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You did well in your Executive Summary and Introduction to define coral reef monitoring, justify need with bleaching statistics, explain why only one satellite is required, and identify CSIRO/BOM users with literature refs. To reach top of Accomplished, clarify vague funding detail.

*Assessor reasoning:* Primary mission, need with bleaching statistics, single-sat rationale, operator/customers all addressed with literature refs. Detail good though funding vague.
> Executive Summary: "specifically for coral reef and ocean monitoring"  
> Introduction: "only one satellite is required"  
> Introduction: "used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You covered launch from Guiana Space Centre, 600km 97.7924° SSO in Image 1, manoeuvres, and ground access well with STK views. To reach Accomplished, fix equatorial benefit for retrograde SSO, RAAN 27.33 deg and Argument of Latitude errors, and add FOV, delta-V, link and drag-sail decay estimates.

*Assessor reasoning:* All subtopics covered with STK views, access table, SSO plot. Weaknesses: RAAN justification wrong, equatorial benefit misapplied to SSO, no delta-V/link calc, Vega-E speculative, no STK files shown.
> Image 1  
> Mission Design - Launch: "launched from the Guiana Space Centre Spaceport"  
> Mission Design - Orbit: "altitude of 600km requires a mean inclination of 97.7924°"  

### C3 Conclusion (5/10, Adequate)

You summarised launch, polar SSO illumination, ground station and Vega C alternative in your Conclusion. To reach Accomplished, move beyond repetition to detailed conclusions drawn from your evidence with specific quantitative outcomes and residual risks.

*Assessor reasoning:* Summarises launch, orbit, ground station and risk. Largely repeats design, limited synthesis of evidence or quantitative outcomes.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans"  
> Conclusion: "Alternatives include the earlier Vega C launcher"  

### C4 Report presentation (10/20, Adequate)

You used clear headings, executive summary, and labelled STK plots/tables in Images 1 and 4. To reach Accomplished, ensure consistent formatting, formal language, matching in-text and list references, complete all entries, and use only approved sources.

*Assessor reasoning:* Clear headings, exec summary, labelled STK plots/tables. OCR table breaks, inconsistent refs, truncated [10], Wikipedia used despite ban, some informal language.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 4  

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

- Mission Design - Launch: Claims equatorial launch saves fuel for retrograde SSO; ignores large plane-change penalty from 5deg site to 97.8deg orbit.
- Mission Design - Orbit: RAAN 27.33 deg said to indicate launch facility; RAAN is time-dependent, not site latitude. Argument of Latitude mis-presented as static element.
- Mission Design - Orbit: 600km altitude vs 250km reef swath trade stated qualitatively; no sensor FOV, resolution, revisit calculation.
- Mission Duration & EOL: Proposes uncontrolled passive drag-sail deorbit but provides no area, mass, decay time or 25-year compliance estimate.

## Next steps

1. Correct your SSO launch and RAAN reasoning in Mission Design and add sensor, delta-V, link and deorbit sizing calculations with STK files.
2. Strengthen your Conclusion to synthesise quantitative outcomes from your evidence rather than repeating the design.
3. Fix referencing and professional style in Bibliography and throughout by completing reference [10] and replacing non-approved sources.

---
<sub>Run Input_2-Run_1-Eff_low-261118-112546 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14888/5244 | cost $0.003261 (incl. $0.001387 for the reused reference rubric+task structure) | 55.67s</sub>
