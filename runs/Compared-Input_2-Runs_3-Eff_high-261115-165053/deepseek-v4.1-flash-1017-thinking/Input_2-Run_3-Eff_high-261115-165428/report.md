# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 52 / 100 (52%)**

You present a coherent single-satellite coral-reef mission and address most required elements with STK evidence. The main weaknesses are launch-vehicle feasibility, orbital-element justification, EOL/manoeuvre consistency, communications sizing, missing STK files, and referencing/formatting. The feedback below is formative only and identifies what each criterion needs for the next level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You cover the primary mission, Australian benefit, single-spacecraft rationale and likely users in the Introduction. To reach Accomplished, separate the operator and customer roles explicitly (your CSIRO/BOM sentence mixes them), give more detailed mission rationale, and support claims with specific literature rather than weak/inappropriate sources.

*Assessor reasoning:* Primary mission, Australian benefit, single-spacecraft rationale and likely users are covered, but operator/customer roles are not clearly separated and referencing is weak/inappropriate, limiting to adequate.
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You address launch, orbit, ground access, duration and EOL with STK screenshots and calculations. To reach Accomplished: replace/justify the non-operational Vega E and 2021 manifest; correct RAAN 27.33° and the low-resolution-desirable contradiction; make EOL consistent with no thrusters by calculating passive drag-sail deorbit lifetime; add link/data-rate and ground-station compatibility; include STK files.

*Assessor reasoning:* Launch, orbit, ground access, duration and EOL are addressed with STK screenshots and some calculations. However, launch choice, RAAN justification, resolution logic, manoeuvre/EOL consistency and lack of link budget/software files reduce persuasiveness.
> Mission Design – Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Mission Design – Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved, in addition to the already frequent amount of passes."  
> Mission Design – Orbit: "A very high altitude would yield low resolution images which is also desirable."  

### C3 Conclusion (6/10, Adequate)

Your Conclusion summarises the Vega E launch, SSO and ground station and links them to reef monitoring, but it is generic and omits limitations and performance evidence. To reach Accomplished, make each conclusion traceable to your design evidence (orbit, access, link budget, EOL) and state key risks/limitations, including that Vega E is not yet built.

*Assessor reasoning:* Conclusion summarises the selected launch, SSO orbit and ground station and links them to the reef-monitoring aim, but is somewhat generic and omits key limitations and performance evidence.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your headings and writing are generally clear, but figures/tables lack consistent numbering and captions (e.g. Image 1-2), references are bare URLs including Wikipedia, and cited entries such as [50] are missing from the list. To reach Accomplished, use consistent figure/table formatting and a complete, correctly cited reference list with quality sources.

*Assessor reasoning:* Structure, headings and writing are generally clear, but figures/tables lack consistent numbering, references are bare URLs with Wikipedia and missing cited entries, so presentation is not fully professional.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Image 1-2: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design – Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design – Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design – Launch: Vega E is not operational for the proposed launch; relying on a future vehicle and 2021 manifest is weak justification.
- Mission Design – Orbit: RAAN 27.33° is said to indicate the launch facility; RAAN is not simply set by launch-site location.
- Mission Design – Orbit: Statement that high altitude yielding low resolution is 'desirable' is contradictory.
- Mission Duration & EOL: Claims only an EOL orbital manoeuvre but the satellite has no thrusters; a passive drag sail is not a manoeuvre and no deorbit lifetime is calculated.
- Ground Control & Communications: No link/data-rate or ground-station compatibility analysis; access duration alone does not prove communications capacity.
- Ground Control & Communications: STK screenshots are included but relevant STK software files are not provided.
- Bibliography: Wikipedia is used and references are bare URLs; citations such as [50] are absent from the list.

## Next steps

1. Revise Mission Design – Launch and Orbit: replace or strongly justify Vega E with an operational launch vehicle and current manifest evidence; correct the RAAN 27.33° claim, remove the contradictory low-resolution-desirable statement, and show orbital-element derivation.
2. Reconcile Mission Duration & EOL and Ground Control & Communications: state a thruster-free EOL plan using the passive drag sail, calculate deorbit lifetime, and add a link/data-rate and ground-station compatibility analysis; include your STK software files.
3. Improve C1, C3 and C4: separate operator and customer roles in the Introduction, make the Conclusion evidence-specific including limitations, and replace Wikipedia/bare URLs, add missing [50], and number/caption figures and tables consistently.

---
<sub>Run Input_2-Run_3-Eff_high-261115-165428 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14293/9873 | cost $0.006251 (incl. $0.001387 for the reused reference rubric+task structure) | 63.56s</sub>
