# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 64.5 / 100 (64.5%)**

You presented a well-motivated mission concept benefiting Australia, supported by STK orbit modelling and an effective synthesis in the Conclusion. To reach higher marks across all sections, address technical misconceptions regarding orbital mechanics, thoroughly proofread to remove unfinished text, replace non-academic sources like Wikipedia with primary literature, and standardise your figure and table numbering.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8.5 / 10 | 8.5 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6.5 / 10 | 39 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8.5/10, Accomplished)

You clearly defined the primary mission, justified using a single satellite for coral bleaching monitoring, and identified relevant stakeholders like CSIRO and BOM. To reach the top of Accomplished, integrate literature references more deeply when establishing operational requirements.

*Assessor reasoning:* The primary mission (Great Barrier Reef monitoring via fluid lensing) and rationale are clearly articulated. The choice of a single satellite is justified, and operators/end-users (CSIRO, BOM, Australian Government) are explicitly identified.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (39/60, Adequate)

You effectively utilised STK to model the 600 km orbit and evaluate ground station access. However, stating an equatorial launch maximises efficiency is incorrect for a retrograde SSO ($i = 97.8^\circ$), where Earth's rotation opposes the launch. To achieve Accomplished, ensure orbital dynamics principles are accurate and avoid truncated sentences in your EOL section.

*Assessor reasoning:* Major mission elements are addressed with STK access reports and orbit plots. However, claiming equatorial launch maximizes efficiency via Earth rotation is incorrect for a retrograde sun-synchronous orbit (inclination 97.8°), where eastward rotational velocity penalizes retrograde delta-v. The EOL text also contains an unfinished sentence.
> Mission Design: "The most efficient rocket launches are from locations close to the equator as this is where maximum rotational velocity can be experienced"  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 97.7924^{\circ} for the satellite to remain sun-synchronous."  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

### C3 Conclusion (7/10, Accomplished)

Your conclusion synthesised the major elements of the report well, directly linking your mission architecture to the Great Barrier Reef monitoring objectives. Ensure all concluding statements are reinforced with specific numerical findings from your analysis.

*Assessor reasoning:* The conclusion draws appropriate summaries from the preceding sections, synthesizing the launch vehicle choice, orbital regime, and ground station capability.
> Conclusion: "The initial problem of not catching coral bleaching events in time can be minimised, if not solved, by the initiation of the ZYZZsat in 2025."  

### C4 Report presentation (10/20, Adequate)

Your report layout follows a clear engineering flow. To move from Adequate to Accomplished, ensure all visual assets include formal captions and numbers (e.g., 'Figure 1: STK 3D View...'), and replace direct Wikipedia content and raw wiki citations with verified primary academic and industry literature.

*Assessor reasoning:* Formatting and presentation have notable flaws. Figures and tables lack formal numbering and captions (e.g., 'Figure 1: ...'). Tables are copied directly from Wikipedia with raw bracketed wiki citations intact, violating the strict prohibition against using Wikipedia.
> Mission Design: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Introduction |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Mission Design |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | yes | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Orbit |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Mission Design: Claiming equatorial launch is most efficient due to Earth's rotational speed is technically invalid for a retrograde SSO (i = 97.8°), where Earth's rotation opposes the launch direction.
- Mission Duration & EOL: Incomplete sentence: 'utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10].'

## Next steps

1. Revisit your launch site selection analysis in 'Mission Design' to account for retrograde orbital mechanics, noting that Earth's eastward rotation incurs a delta-v penalty at inclinations greater than 90°.
2. Complete the truncated sentence in 'Mission Duration & EOL' detailing drag sail mechanics ('utilising a large surface area to...').
3. Replace all Wikipedia tables and citations throughout the report with peer-reviewed literature or official launch provider user manuals, and add formal numbered captions to all figures.

---
<sub>Run 20261112-062546-530_Input_2_md_r2 | rubric=google/gemini-3.8-flash, task=google/gemini-3.8-flash, marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 16502/3186 | cost $0.018814 | 58.14s</sub>
