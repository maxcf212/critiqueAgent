# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 66 / 100 (66%)**

A well-structured, mostly complete mission design for GBR reef monitoring with good STK evidence and sound orbit/launch choices. To reach the top band: remove the Wikipedia citation and fix bare-URL references, show your hand calculations (e.g. J2 inclination), include software files, label figures consistently, and clarify the garbled EOL and resolution passages.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Strong work: your Introduction clearly covers the primary mission (fluid-lensing reef monitoring), why it is needed, the single-spacecraft justification, and users/operator/funding (CSIRO, BOM). To reach the top of the Accomplished band, deepen the customer definition - e.g. how reef managers would actually access and use the imagery.

*Assessor reasoning:* Primary mission (reef monitoring via fluid lensing), rationale, single-spacecraft justification, and users/operator/funding all addressed with reasonable detail and references. Could be deeper on customer definition.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

All major requirements are addressed with good STK screenshots and access reports, and your SSO/launch rationale is sound. The next level requires higher-quality supporting evidence: include software files, show hand-calculation derivations (e.g. the J2 inclination result), fix the low-resolution contradiction, and discuss the Vega E availability risk in the design body, not just the conclusion.

*Assessor reasoning:* All major requirements addressed: launch site/vehicle with rationale, SSO with full COEs, manoeuvres (EOL only), ground station, access durations, 5-year mission and drag-sail EOL. STK screenshots and access reports included. Weaknesses: no software files mentioned, no hand-calculation derivations shown, error claiming low resolution 'is also desirable', Vega E not yet flown risk acknowledged only in conclusion.
> Mission Design - Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Mission Design - Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (6/10, Adequate)

Your conclusion summarises each segment and flags the Vega E risk, which is good. To move to Accomplished, go beyond restatement: critically evaluate results - is the achieved access duration adequate for the reef-monitoring requirement? What coverage or orbit trade-offs would you revisit?

*Assessor reasoning:* Conclusions summarise each segment and note risks (Vega E availability), but remain largely a restatement of the design rather than critical evaluation of results (e.g. access adequacy, coverage trade-offs).
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Clear structure with headings and TOC, and figures have captions. For Accomplished: add consistent figure numbers (Figure 1, 2...) referenced in text, replace bare-URL references with properly formatted citations (no Wikipedia), and proofread for errors like 'is current owned' and stray parentheses.

*Assessor reasoning:* Clear structure with headings and TOC; figures have captions but are inconsistently labelled (no figure numbers). References are bare URLs with no titles/dates, and Wikipedia is cited, which is disallowed. Minor grammar errors ('is current owned', stray parenthesis).
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Ground Control & Communications: "the Mount Pleasant Radio Observatory). This station is current owned"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Introduction/Executive Summary |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Mission Design - Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Mission Design - Orbit |
| R8 | Identify any orbital manoeuvres required. | yes | Mission Design - Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | partial | Mission Design - Orbit/Ground Control |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Orbit/Ground Control sections |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Report structure |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Images 1-5 |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Mission Design - Orbit: States low resolution from high altitude 'is also desirable' – contradicts resolution requirement for reef imaging.
- Bibliography: Wikipedia cited as source [6], explicitly disallowed; references are bare URLs without titles/access dates.
- Mission Duration & EOL: Text garbled/contradictory: 'without thrusters... choose an uncontrolled descent... However, the ZYZZsat is without thrust capability' – repetitive and unclear; drag sail description incomplete.
- Mission Design - Orbit: Inclination-vs-altitude plot presented without showing the underlying J2 hand calculation or equation.
- Ground Control & Communications: Claim that vertical inclination 'maintains a significant contact for the vast majority of passes' is vague and unsupported.

## Next steps

1. Replace the Wikipedia source [6] with a citable primary source, and format all references with titles, authors and access dates so in-text citations match the list
2. Show the J2 hand calculation (equation and working) behind your inclination-vs-altitude plot, and attach your STK scenario/software files in an appendix
3. Rewrite the Mission Duration & EOL section to resolve the contradictory 'without thrusters' statements and fully describe the drag sail deorbit plan; also correct the claim that low resolution 'is also desirable' for reef imaging

---
<sub>Run 20261112-074907-205_Input_2_md_r1 | rubric=z-ai/glm-5.3-flash, task=z-ai/glm-5.3-flash, marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 13478/1653 | cost $0.001843 | 46.37s</sub>
