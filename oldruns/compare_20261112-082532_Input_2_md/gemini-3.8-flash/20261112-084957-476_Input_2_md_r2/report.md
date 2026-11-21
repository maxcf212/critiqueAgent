# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 61 / 100 (61%)**

You developed a compelling mission concept for Great Barrier Reef monitoring using fluid lensing, with clear stakeholder identification and effective STK simulations. Your introduction and conclusion successfully frame the mission requirements. To reach higher marks, focus on technical accuracy in orbital mechanics (specifically launch physics and RAAN definition), clean up duplicate STK access data and incomplete sentences, and adopt professional reporting standards by replacing Wikipedia references and adding formal captions to all figures and tables.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

You articulated an excellent, well-rationalised mission concept in the Introduction, clearly justifying a single spacecraft for coral reef monitoring and identifying operators like CSIRO and BOM. To reach the top mark, continue backing operational assumptions with deeper literature references.

*Assessor reasoning:* The student clearly articulates the primary mission (coral reef monitoring with fluid lensing), justifies why it is needed, explains why a single satellite suffices, and specifies both operators and customers. Relevant background references are integrated appropriately.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You addressed the required design elements using STK effectively. To achieve Accomplished, ensure your technical explanations are accurate: equatorial rotation penalises retrograde Sun-synchronous orbits rather than boosting them, and RAAN is an inertial reference, not launch longitude. Also, resolve duplicate entries in the STK access table and finish the truncated sentence in your EOL discussion.

*Assessor reasoning:* Major requirements are addressed using STK simulations and orbital parameter derivations. However, the work contains notable technical errors: claiming equatorial launch provides rotational velocity benefits for a retrograde SSO orbit, misidentifying RAAN as launch site location, an identical duplicate entry in the STK access table, and an unfinished sentence in the EOL discussion.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "The initial value indicates the location of the launch facility."  
> Mission Duration & EOL: "utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

### C3 Conclusion (7/10, Accomplished)

Your conclusion neatly synthesised your major mission decisions, linking the Vega E launcher, orbital regime, and ground station capability directly back to reef monitoring goals. To strengthen it further, you could briefly highlight key trade-offs and suggest specific operational contingency plans if launch vehicle availability shifts.

*Assessor reasoning:* The conclusion concisely summarizes the key engineering decisions, including the selected launcher, orbit rationale, and ground station capability, linking the outcomes directly to the mission's Great Barrier Reef monitoring objectives.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet. Thus, launch may need to be adjusted"  

### C4 Report presentation (10/20, Adequate)

You maintained a logical structure with clear headings. To progress to Accomplished, assign formal captions and numbers (e.g., Table 1, Figure 1) to all graphics and tables. Avoid pasting raw web tables with unformatted footnote brackets, and replace non-academic sources like Wikipedia with primary technical literature or launch manifest documentation.

*Assessor reasoning:* The document uses an appropriate structure, but formatting lacks professional polish. Figures and tables lack proper formal numbering (e.g., Figure 1, Table 1). Unformatted Wikipedia tables with raw bracketed footnotes are pasted directly, and Wikipedia is cited as a primary reference despite explicit task instructions prohibiting it.
> Launch: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

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
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Orbit |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | - |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Launch |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Launch: Claiming that launching near the equator provides a rotational velocity boost for a retrograde Sun-synchronous orbit (i = 97.79°) is incorrect; Earth's eastward rotation opposes retrograde orbital velocity.
- Orbit: The report states RAAN's initial value 'indicates the location of the launch facility', confusing an inertial celestial reference with terrestrial longitude.
- Ground Control & Communications: Access rows 14 and 15 in the STK access table are duplicate entries with identical start and stop times.
- Mission Duration & EOL: Incomplete sentence in text: 'utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10].'

## Next steps

1. Correct core orbital mechanics concepts: revise the launch physics to account for Earth's rotational penalty on retrograde SSO orbits, and correctly define RAAN as an inertial celestial reference rather than terrestrial launch longitude.
2. Proofread and verify simulated data: eliminate duplicate entries in your Ground Control STK access table (rows 14 and 15) and complete the truncated sentence in your Mission Duration & EOL section.
3. Professionalise report presentation: format all figures and tables with standard numbering and captions, remove raw pasted web tables, and replace Wikipedia citations with authoritative technical sources.

---
<sub>Run 20261112-084957-476_Input_2_md_r2 | rubric=google/gemini-3.8-flash, task=google/gemini-3.8-flash, marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 16582/6152 | cost $0.029995 | 86.97s</sub>
