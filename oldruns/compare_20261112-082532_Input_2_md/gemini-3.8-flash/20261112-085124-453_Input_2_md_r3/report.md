# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 54 / 100 (54%)**

You have developed a well-justified mission concept for Australian coral reef monitoring, clearly detailing user needs and core STK orbit parameters. To advance your engineering reports, focus on technical rigour by eliminating physical misconceptions regarding retrograde launch mechanics, resolving design contradictions in your propulsion and deorbit strategies, backing design choices with hand calculations, and maintaining strict academic referencing and figure captioning standards.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

In the Introduction, you effectively established a compelling rationale for monitoring coral bleaching, clearly justifying the single-spacecraft architecture and identifying key stakeholders like CSIRO and the Bureau of Meteorology. To sustain top-tier work across all requirements, ensure every operational constraint introduced here directly links to the technical trade-offs discussed in later subsystems.

*Assessor reasoning:* The introduction clearly identifies the primary mission, necessity for reef monitoring, satellite count justification, and key users and operators including CSIRO and BOM. The contextual rationale is strong and well explained.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You applied STK effectively to model the baseline orbit. To reach Accomplished, verify astrodynamics principles—equatorial launch assist opposes retrograde sun-synchronous orbits (i=97.8°)—and provide supporting hand calculations for J2 precession and drag-sail sizing. Additionally, resolve the contradiction in Mission Duration & EOL between performing manoeuvres and having no thrusters, ensuring all sentences are complete.

*Assessor reasoning:* While key parameters are presented with STK outputs, technical depth is lacking. No hand calculations for J2 precession or drag-sail sizing are provided. Launching into a retrograde SSO from Kourou misapplies equatorial velocity advantages. Furthermore, there is an unresolved contradiction regarding whether an EOL maneuver occurs given the satellite has no propulsion, alongside a truncated sentence.
> Launch: "The most efficient rocket launches are from locations close to the equator as this is where maximum rotational velocity can be experienced"  

### C3 Conclusion (6/10, Adequate)

Your Conclusion effectively links back to the mission's coral bleaching objectives. To achieve Accomplished, move beyond a generic narrative summary by providing a detailed synthesis of your engineering results. Critically evaluate system performance, highlight specific quantitative parameters (such as revisit rates and deorbit timelines), and candidly discuss design limitations and critical trade-offs encountered in the mission design.

*Assessor reasoning:* Conclusions summarize the chosen space segment elements and link back to the mission objectives. However, the discussion remains generic, lacking quantitative synthesis, trade-off review, or critical evaluation of design limitations.
> Conclusion: "The initial problem of not catching coral bleaching events in time can be minimised, if not solved, by the initiation of the ZYZZsat in 2025."  

### C4 Report presentation (10/20, Adequate)

The report maintains a clear engineering structure. To reach Accomplished, ensure all figures and tables feature standardized numbering and descriptive captions. Replace Wikipedia citations with authoritative academic or industry literature, remove raw copied table formatting, complete truncated sentences, and verify that all bibliography entries are properly formatted and cited consistently in the text.

*Assessor reasoning:* The report follows a standard structure but exhibits notable presentation shortcomings. Figures and tables lack standard numbering and captions. Raw tables copied from Wikipedia retain footnote anchors, and Wikipedia is explicitly cited contrary to instructions. A truncated sentence and malformed reference entries further degrade quality.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

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
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | partial | Orbit |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Launch: Claiming an equatorial launch site (Kourou) provides maximum velocity benefit is incorrect for a retrograde SSO (i=97.8 deg), where Earth rotation opposes the launch direction.
- Mission Duration & EOL: Contradiction between stating an orbital manoeuvre occurs at EOL and stating the satellite lacks thrusters, coupled with an incomplete truncated sentence describing the drag sail.
- Mission Duration & EOL: No quantitative drag sail area sizing or re-entry orbital lifetime calculations were conducted to prove compliance with space debris mitigation requirements.

## Next steps

1. Re-evaluate launch dynamics in the Launch section to correctly account for velocity penalties when inserting into a retrograde sun-synchronous orbit (i = 97.8°).
2. In Mission Duration & EOL, add hand calculations sizing the drag sail area for orbital lifetime compliance and resolve the contradiction regarding thrusterless manoeuvres.
3. Standardise report presentation by adding formal numbers and captions to all figures and tables, and replace Wikipedia citations with peer-reviewed or industry sources.

---
<sub>Run 20261112-085124-453_Input_2_md_r3 | rubric=google/gemini-3.8-flash, task=google/gemini-3.8-flash, marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 16417/7297 | cost $0.034166 | 70.21s</sub>
