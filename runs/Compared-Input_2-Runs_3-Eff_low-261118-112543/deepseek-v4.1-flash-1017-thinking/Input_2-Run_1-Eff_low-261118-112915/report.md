# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

Your report presents a coherent single-satellite coral-monitoring mission with STK screenshots and a quantified ground-station access table. The concept and Australian benefit are clear. To move from adequate to accomplished, strengthen launch/orbit justification, add operational and link/coverage analysis, provide software files, correct the EOL description, and improve referencing and figure/table formatting.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You clearly explain the coral-reef monitoring mission, Australian benefit, need for fluid-lensing observation, single-spacecraft choice and likely users in the Introduction. To sustain the Accomplished standard, sharpen the distinction between operator and customer roles and ensure every claim is referenced.

*Assessor reasoning:* The introduction clearly explains the coral-reef monitoring mission, its Australian benefit, the need for fluid-lensing observation, the single-spacecraft choice, and likely users. References are included. Minor weakness: operator versus customer roles are not sharply distinguished.
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You address launch, orbit, ground station, duration and EOL with STK screenshots and an access table. To reach Accomplished, provide STK/PIGI files, justify Vega E and the 600 km orbit with alternatives and calculations (RAAN, link budget, data rate, swath/revisit), correct the passive drag-sail EOL description, and describe operations, power, thermal and attitude.

*Assessor reasoning:* Launch, orbit, ground station, duration and EOL are addressed with STK screenshots and an access table. However, launch/orbit justification is limited, Vega E is speculative, operations and link/coverage analysis are thin, and STK files are missing. Errors and weak support fit Adequate.
> Mission Design: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  

### C3 Conclusion (6/10, Adequate)

Your Conclusion draws specific launch, orbit and ground-station outcomes, but it is brief and somewhat generic and overstates how fully the configuration is described. For Accomplished, tie each conclusion explicitly to evidence in the main body, include key quantitative results and limitations, and avoid claims not supported by the design.

*Assessor reasoning:* Conclusions are drawn from the design and mention key launch, orbit and ground-station outcomes. They are specific but brief and somewhat generic, and overstate how fully the configuration has been described.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

Your report has headings, an executive summary and a bibliography, but presentation is not yet professional. For Accomplished, number and caption all figures/tables consistently (e.g. Image 1), replace Wikipedia with credible sources, format references with titles/authors, ensure in-text citations match the list, and revise informal language.

*Assessor reasoning:* The report has headings, executive summary and bibliography, but presentation is not professional. Figures/tables lack consistent numbering, references are poorly formatted and include Wikipedia, and some text is informal. Writing remains readable and structure is present.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 1: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 1 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design: Vega E is selected although not yet flown; rideshare availability and launch date are speculative.
- Orbit table: RAAN of 27.33° is claimed to indicate launch facility location, which is unclear and not properly derived.
- Orbit: 600 km altitude is justified qualitatively; no swath, resolution, revisit or link calculation is shown.
- Ground Control & Communications: No link budget, data rate, downlink capacity or detailed revisit statistics are presented.
- Mission Duration & EOL: EOL is called an orbital manoeuvre, but the chosen passive drag sail has no thrust capability.
- Bibliography: Wikipedia is used as source [6]; references lack titles/authors and formatting is inconsistent.
- Image 1: Relevant STK/PIGI files are not provided; only screenshots and tables are included.
- Mission Design: Operations, power, thermal, attitude and detailed coverage planning are not sufficiently described.

## Next steps

1. For C2, add STK/PIGI files and supporting calculations: justify Vega E against alternatives and availability, derive the RAAN value, include link budget/data rate/swath/revisit analysis, and correct the EOL drag sail as a passive device rather than an orbital manoeuvre.
2. For C2, expand operations and coverage: describe power, thermal, attitude and detailed coverage planning, and quantify communication statistics beyond average contact duration.
3. For C3/C4, tighten conclusions to the evidence and improve presentation: number/caption all figures and tables consistently, replace Wikipedia with credible sources, format references with titles/authors, and revise informal language.

---
<sub>Run Input_2-Run_1-Eff_low-261118-112915 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14308/9035 | cost $0.006658 (incl. $0.001387 for the reused reference rubric+task structure) | 61.18s</sub>
