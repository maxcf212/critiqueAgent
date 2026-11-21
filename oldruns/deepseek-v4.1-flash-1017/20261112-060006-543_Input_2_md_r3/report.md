# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

Your ZYZZsat concept is coherent and well organised, with STK evidence and hand calculations across all major requirements. The main limits are technical slips in the orbit and EOL sections, missing software files, unlabelled figures and weak referencing. Fixing these would move the design and presentation criteria from Adequate toward Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Strong introduction: mission purpose, rationale, single-spacecraft justification and users are all covered with references. To reach the top of Accomplished, sharpen the operator/customer ownership and funding arrangements so the user chain is unambiguous.

*Assessor reasoning:* Mission purpose, rationale, single-spacecraft justification and users (operator/customers) all addressed with literature references. Rationale is detailed and persuasive; minor weakness is vague funding/operator ownership.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

All major requirements are covered with STK screenshots and hand calculations, but several errors hold this at Adequate. Correct the resolution logic in Orbit, justify or remove the RAAN 27.33° claim, address the Vega E schedule risk, complete the truncated EOL drag-sail analysis with area/altitude/deorbit time, add explicit manoeuvre analysis, fix the duplicate row 15 in the access table, and include the software files.

*Assessor reasoning:* All major requirements covered with STK screenshots and hand calc. But errors: 'very high altitude would yield low resolution which is also desirable' (contradiction), RAAN 27.33° claimed to indicate launch site without derivation, Vega E not yet built, EOL drag-sail text truncated, no software files included.
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (6/10, Adequate)

Conclusions restate each segment and note the launch risk, but are not yet evidence-driven. To reach Accomplished, synthesise the key findings (orbit, contact cadence, EOL outcome) into specific conclusions tied to your results, including the drag-sail disposal outcome.

*Assessor reasoning:* Conclusions summarise each segment and note launch risk, but are largely restatement rather than evidence-driven synthesis; EOL outcome not concluded.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Structure, headings and executive summary are clear and the writing is readable. To reach Accomplished, add numbered captions to all figures and tables, replace Wikipedia and bare URLs with proper citations, and clean the reference list so in-text citations match it exactly.

*Assessor reasoning:* Structure and headings clear, executive summary present. But references are bare URLs with OCR/typo artefacts, Wikipedia used as a source, figures lack numbered captions, and some tables are unlabelled. Writing generally readable.
> Bibliography: "[5] f. https://www.qrg.northwestern.edu/projects/vss/docs/navigation/2-why-launch-from-equator.html"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Orbit: "[Image 1]"  

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
| R8 | Identify any orbital manoeuvres required. | partial | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Orbit |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Contents |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Orbit: Text states a very high altitude would yield low resolution 'which is also desirable' – contradicts the stated need for sufficient resolution.
- Orbit: RAAN 27.33° asserted to indicate launch facility location without derivation; RAAN is epoch-dependent and not simply a launch-site indicator.
- Launch: Vega E first launch 2024 is unbuilt/uncertain; relying on it for a 2025 launch is a schedule risk not fully mitigated.
- Mission Duration & EOL: EOL paragraph truncated ('utilising a large surface area to ‘'); drag-sail area/altitude/deorbit-time calculation absent.
- Ground Control & Communications: Access table has duplicate row 15 and inconsistent numbering; mean/total durations not cross-checked.
- Orbit: No explicit orbital manoeuvre analysis (e.g. inclination/altitude adjustment from injection); only EOL disposal mentioned.

## Next steps

1. Revise the Orbit section: correct the resolution-versus-altitude statement, derive or remove the RAAN 27.33° launch-site claim, and add an explicit injection manoeuvre analysis.
2. Complete the Mission Duration & EOL section with a drag-sail area, altitude and deorbit-time calculation, and conclude the EOL outcome in the Conclusion.
3. Improve presentation: number all figure/table captions, include the STK/software files, and replace Wikipedia and bare-URL references with properly formatted citations that match the in-text list.

---
<sub>Run 20261112-060006-543_Input_2_md_r3 | rubric=deepseek/deepseek-v4.1-flash-1017, task=deepseek/deepseek-v4.1-flash-1017, marking=deepseek/deepseek-v4.1-flash-1017, feedback=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 12516/1489 | cost $0.001177 | 31.56s</sub>
