# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 75 / 100 (75%)**

You delivered a technically robust preliminary space mission design for Australia, featuring clear justifications for your single-spacecraft architecture, orbital parameters, and ground access simulations. Your technical logic and orbital mechanics analysis are accomplished. To reach professional engineering standards, ensure complete editorial review to eliminate broken text, formally number and caption all figures and tables, and replace non-academic sources such as Wikipedia with authoritative primary literature.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (9/10, Accomplished)

You provided an accomplished introduction, clearly detailing the fluid lensing coral reef monitoring mission, justifying the single spacecraft constellation, and identifying target users such as CSIRO and BOM.

*Assessor reasoning:* The student thoroughly explains the primary mission (coral reef/Great Barrier Reef bleaching detection via fluid lensing), clear rationale for a single spacecraft, and identifies the operators and end customers.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Your technical design is accomplished, featuring rigorous orbital mechanics calculations for a sun-synchronous orbit, sound trade-offs, and STK ground access simulations. To improve, ensure you specify the epoch for your orbital elements.

*Assessor reasoning:* Addresses all major technical requirements: launch site/vehicle choice with good trade rationale, full orbital elements and J2 sun-synchronous logic, communication access via STK reports, and a passive drag sail EOL strategy.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (8/10, Accomplished)

You reached an accomplished conclusion, delivering an effective summary that synthesised your findings across launch, orbital design, ground architecture, and national environmental impact.

*Assessor reasoning:* Draws sound and specific conclusions summarising launch vehicle, orbit selection, ground observatory choice, and the mission's environmental benefit to Australia.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (10/20, Adequate)

To reach the Accomplished level, ensure figures and tables have numbered, consistent captions rather than plain text labels, remove broken sentences in the EOL section, and avoid prohibited sources like Wikipedia.

*Assessor reasoning:* Figures and tables lack formal numbering (e.g. Figure 1, Table 1). Wikipedia was explicitly prohibited by the prompt instructions but is cited directly as reference [6]. Bibliography formatting has broken lines.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Introduction |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | yes | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Contents |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Mission Duration & EOL: Sentence cut off in EOL discussion: 'utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10].'
- Orbit: In classical Keplerian orbital elements for a circular orbit, True Anomaly is undefined; while Argument of Latitude (u) is appropriately stated, Epoch is missing.

## Next steps

1. Implement standard, numbered captions (e.g., 'Figure 1: STK 3D orbit view') and cross-reference them directly within the body text.
2. Replace Wikipedia citations with primary technical documentation, such as launch vehicle user manuals or peer-reviewed literature.
3. Proofread all narrative sections carefully to resolve incomplete sentences, broken formatting lines, and missing orbital parameters like Epoch.

---
<sub>Run 20261112-075105-880_Input_2_md_r1 | rubric=google/gemini-3.8-flash, task=google/gemini-3.8-flash, marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 16397/1518 | cost $0.01799 | 22.97s</sub>
