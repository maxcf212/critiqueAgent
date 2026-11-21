# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

You developed a well-rationalised Australian reef-monitoring mission for CSIRO and BoM with solid STK access analysis. To elevate your work, resolve technical inconsistencies between your propulsion and manoeuvre plans, support orbital mechanics claims with verified hand calculations rather than relying on qualitative assumptions, and adopt rigorous academic presentation by replacing Wikipedia tables and citations with primary technical literature and standard captions.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

You articulated a clear, compelling rationale in your Introduction, effectively establishing the need for Great Barrier Reef monitoring using fluid lensing. Your decision to deploy a single satellite was well-justified for CSIRO and BoM operational needs. To maintain top performance across future deliverables, ensure every cited operational constraint links directly to verifiable technical requirements.

*Assessor reasoning:* All introductory requirements are clearly satisfied. The primary mission (monitoring Great Barrier Reef bleaching using fluid lensing) is well articulated, the choice of a single spacecraft is justified, and specific Australian end-users (CSIRO, BoM) are identified.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You presented thorough STK access modelling in Mission Design. To reach Accomplished, eliminate contradictions—such as planning an EOL manoeuvre while stating you lack thrusters—and correct orbital claims regarding equatorial assistance for retrograde SSOs. Include explicit hand calculations, complete the truncated drag-sail description in Mission Duration & EOL, and quantitatively prove compliance with the 25-year deorbit guideline.

*Assessor reasoning:* Covers launch, Keplerian elements, STK access analysis, and EOL. However, hand calculations are absent, and there are conceptual flaws: claiming equatorial launch assists a retrograde SSO, contradicting manoeuvre needs between sections (no thrusters vs EOL manoeuvre), and leaving the drag sail text truncated.
> Launch: "The most efficient rocket launches are from locations close to the equator as this is where maximum rotational velocity can be experienced"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (6/10, Adequate)

In the Conclusion, you effectively recapped the baseline architecture, including your launch vehicle and orbital regime. To reach Accomplished, draw detailed, evidence-based conclusions rather than generic summaries. Synthesise your quantitative STK outputs—such as ground access duration and revisit frequency—and critically reflect on mission feasibility and deorbit timeframes against design requirements.

*Assessor reasoning:* The conclusion recaps the satellite configuration, launch vehicle, orbit choice, and ground station. However, it remains generic, omitting quantitative mission performance metrics (e.g., access statistics, revisit frequency, or deorbit timeframe) and technical critical reflection.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (10/20, Adequate)

Your report maintains a logical flow with an executive summary and table of contents. To reach Accomplished, replace unformatted Wikipedia tables and citations with primary aerospace literature. Ensure all figures and tables feature formal numbering and captions, clean up formatting in your Bibliography, and thoroughly proofread your text to prevent incomplete sentences.

*Assessor reasoning:* Report structure is clear with an executive summary and table of contents. However, figures and tables lack standard numbering and formal captions. Unedited Wikipedia tables and citations are pasted directly into the body, Wikipedia is cited as a source, and reference formatting contains stray characters.
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
| R8 | Identify any orbital manoeuvres required. | partial | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | partial | Orbit |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Contents |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Launch: Incorrectly states that launching near the equator assists retrograde sun-synchronous orbits; Earth's rotational velocity penalises retrograde inclinations (i = 97.79°).
- Orbit: Claims an orbital manoeuvre occurs at EOL, but subsequent EOL section states the spacecraft has no thrusters and relies on a passive drag sail.
- Mission Duration & EOL: The sentence explaining the drag sail operation is cut off mid-sentence without completing the technical explanation.
- Mission Duration & EOL: No deorbit or drag-sail sizing calculations are provided to verify compliance with LEO 25-year disposal guidelines from 600 km.

## Next steps

1. Resolve propulsion contradictions by deciding between passive deorbit or active thrusters, backing your choice with drag-sail sizing and 25-year LEO disposal calculations.
2. Verify launch and orbit mechanics using hand calculations, correcting the misconception regarding equatorial launch assistance for retrograde Sun-Synchronous Orbits.
3. Replace all Wikipedia citations and raw tables with primary aerospace references, ensuring every table and figure includes consistent numbering and descriptive captions.

---
<sub>Run 20261112-084844-923_Input_2_md_r1 | rubric=google/gemini-3.8-flash, task=google/gemini-3.8-flash, marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 16499/7518 | cost $0.040567 | 72.55s</sub>
