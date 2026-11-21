# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 52 / 100 (52%)**

A readable preliminary design with a clear Introduction and useful STK access work. The main design is Adequate but lacks payload, swath, link-budget and EOL calculations, and contains conceptual errors on launch, RAAN and sunlight. Referencing and figure/table labelling need work. The Conclusion is generic. Use the next steps to add quantitative evidence, correct the design statements, and professionalise presentation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction clearly establishes the coral-reef monitoring need, the one-spacecraft rationale and likely government/science users, with references. To strengthen within Accomplished, sharpen the operator versus customer distinction and improve citation quality; the current references are thin. Keep the mission purpose and user discussion as detailed as your opening paragraphs.

*Assessor reasoning:* Introduction clearly states coral-reef monitoring need, one-spacecraft rationale and likely government/science users, with references. However operator/customer distinction is vague and citations are poor.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground station and EOL with STK access evidence and orbital elements, which is a solid Adequate base. To reach Accomplished, add payload/swath/link/EOL calculations and software files, and correct the launch, RAAN and sunlight statements. Support the 600 km altitude and 250 km reef coverage with sensor FOV, GSD, swath and data-rate evidence, and check the access table inconsistencies.

*Assessor reasoning:* Covers launch, orbit, ground station and EOL with STK access evidence and orbital elements, but lacks payload/swath/link calculations and software files, and contains conceptual errors on RAAN, sunlight and equatorial launch.
> Ground Control & Communications: "The first fifteen access periods are listed above. An average contact duration of almost ten minutes was achieved"  
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion summarises launch, orbit and ground station, but it is generic and omits mission duration/EOL and specific orbital/contact values. To reach Accomplished, tie conclusions directly to your evidence: state the chosen orbit and key elements, average contact duration, five-year life and drag-sail EOL outcome. Avoid broad claims like 'fully described satellite configuration' unless the report substantiates them.

*Assessor reasoning:* Conclusion summarises launch, orbit and ground station, but is generic, omits mission duration/EOL and specific orbital/contact values.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your report has clear headings and is readable, but figures/tables are unnumbered and uncaptioned (e.g., Image 1), and the Bibliography includes Wikipedia and bare URLs. To reach Accomplished, use consistent engineering-report formatting, number and caption every figure/table, and cite properly formatted sources that match in-text citations. Check spelling and formatting consistency throughout.

*Assessor reasoning:* Required sections and headings are present and readable, but figures/tables are unnumbered, bibliography uses bare URLs and Wikipedia, formatting and spelling are inconsistent.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 1: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | partial | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Executive Summary; Introduction |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | partial | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | partial | Orbit; Mission Duration & EOL |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | partial | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | partial | Orbit; Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Orbit; Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary; Contents; Bibliography |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Orbit; Ground Control & Communications |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | no | Bibliography |

## Technical issues

- Launch: Report states equatorial launch maximises rotational velocity; this applies to prograde orbits, not retrograde SSO, so Kourou choice is not justified.
- Orbit: Initial RAAN 27.33° is described as indicating launch facility location; RAAN is an inertial node angle, not a ground-site coordinate.
- Orbit: Text says very high altitude yields low resolution images which is also desirable; for fluid-lensing reef imaging low resolution is undesirable.
- Orbit: Assumes descending passes are constantly sunlit; SSO is continuously sunlit only for dawn-dusk LTAN, which is not specified.
- Orbit: No sensor FOV, ground sample distance, swath or data-rate calculation supports 600 km altitude or 250 km reef coverage.
- Ground Control & Communications: Selects Mt Pleasant radio observatory without showing compatible comms band, antenna gain, link budget or data rate; radio astronomy suitability unproven.
- Ground Control & Communications: Access table has access 6 start/stop spanning about a day but duration 365 s, and access 15 duplicates access 14; access results need checking.
- Mission Duration & EOL: EOL section says satellite has no thrusters, yet orbit section calls EOL an orbital manoeuvre; passive drag sail is not a manoeuvre.
- Mission Duration & EOL: Drag-sail deorbit from 600 km not sized or timed; no demonstration of 25-year rule or complete burn-up.
- Mission Duration & EOL: No orbit maintenance or drag analysis over five-year life; replacement plan is generic.
- Bibliography: Uses Wikipedia [6] as a source and lists bare URLs/malformed entries, contrary to referencing requirements.
- Orbit; Ground Control & Communications: Figures and tables lack figure/table numbers and full captions, so cross-referencing is incomplete.

## Next steps

1. Add supporting calculations for sensor FOV/GSD/swath/data rate, a link budget for Mt Pleasant, and drag-sail deorbit sizing; correct the launch, RAAN and sunlight statements.
2. Number and caption every figure and table (e.g., Image 1), and replace Wikipedia/bare URLs with properly formatted references that match in-text citations.
3. Revise the Conclusion to include specific orbital/contact values and mission duration/EOL outcomes rather than generic claims.

---
<sub>Run 20261112-082722-794_Input_2_md_r1 | rubric=deepseek/deepseek-v4.1-flash-1017, task=deepseek/deepseek-v4.1-flash-1017, marking=deepseek/deepseek-v4.1-flash-1017, feedback=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 12723/12476 | cost $0.008757 | 131.04s</sub>
