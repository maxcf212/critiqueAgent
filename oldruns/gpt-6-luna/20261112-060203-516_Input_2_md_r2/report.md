# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 51 / 100 (51%)**

You present a coherent Australian reef-monitoring concept and use STK outputs to support parts of the orbit and communications design. Your report covers the main mission topics, but incomplete design validation, an underdeveloped end-of-life plan, and citation and presentation issues limit how persuasive and reliable the overall design is.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Your Introduction explains the reef-monitoring purpose, Australian benefit, rationale for one spacecraft, and likely users, including CSIRO and BOM. To strengthen this already accomplished work, explicitly name the mission operator—the ground facility is not itself an operator—and support the mission rationale and user roles more consistently with literature.

*Assessor reasoning:* Explains the reef-monitoring mission and its Australian benefit, gives a rationale for using one spacecraft, and identifies likely users and funding. The operator is not explicitly named, and the rationale and user discussion are not supported with literature consistently, so this falls short of the highest standard.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  
> Executive Summary: "The satellite, nicknamed ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), is operated and accessed from Australia ground facilities"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Launch, Orbit, Ground Control & Communications, and Mission Duration & EOL sections address the required topics and use STK outputs. To reach the accomplished level, validate launch and rideshare compatibility, specify a complete orbit including epoch and ascending-node local solar time, demonstrate sensor feasibility, and reconcile and evaluate the EOL plan. Image 1 and the access table do not provide sufficient reliable evidence for all claims.

*Assessor reasoning:* Addresses launch, orbit, manoeuvres, ground control and access periods, duration, and EOL, with STK-derived results and orbit screenshots. However, orbital elements and mission operations are incomplete, the launch choice is speculative, sensor feasibility is not established, and EOL is underdeveloped. No software project files are evident in the submission.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved, in addition to the already frequent amount of passes."  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  
> Image 1  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (5/10, Adequate)

Your Conclusion links the sun-synchronous orbit and Mt Pleasant facility to the mission. To reach the accomplished level, draw specific conclusions from your design evidence, especially the access analysis, and explain how unresolved orbit, imaging, and disposal uncertainties affect mission feasibility.

*Assessor reasoning:* The conclusion summarizes the principal design choices and connects them to the mission purpose. It is brief and largely restates the report; it does not draw detailed conclusions from the access analysis or resolve the design uncertainties.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Your report has an Executive Summary, contents, headings, figures, and tables, giving it a recognizable structure. To reach the accomplished level, improve grammar and consistency, give figures and tables clear numbering and titles, and ensure in-text citations match complete references. The bibliography includes Wikipedia and citation numbers such as [50]–[74] that do not match the listed entries.

*Assessor reasoning:* The report has a recognizable structure, executive summary, contents, headings, figures, and tables. Presentation is weakened by grammar and typographical errors, tables and figures without consistent numbering and titles, incomplete bibliography details, inconsistent citation numbering, and use of Wikipedia as a source.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Launch: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Ground Control & Communications: "The first fifteen access periods are listed above."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Introduction |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | partial | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | partial | Orbit |
| R8 | Identify any orbital manoeuvres required. | yes | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Image 1 |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | partial | Executive Summary |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Image 1 |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Introduction: The report names likely customer agencies but does not explicitly identify a mission operator; the Australian ground facility is not itself an operator.
- Launch: The proposed Vega E launch and rideshare arrangement are speculative rather than a confirmed mission opportunity. Compatibility of the spacecraft and deployment into the specified orbit is not demonstrated.
- Orbit: The reported RAAN does not by itself indicate the launch facility's location; RAAN is an inertial orbital orientation. An epoch and a more complete state specification are needed to interpret the orbital elements.
- Orbit: The ascending-node local solar time is not specified. Sun-synchronism alone does not establish that the satellite will image the reef in daylight or on the descending leg.
- Orbit: The claim that the near-polar orbit passes over almost the entire Earth is overstated: at 97.79° inclination, the ground track reaches only about 82.21° latitude.
- Orbit: The sensor's swath, ground sample distance, spectral capability, and ability to detect bleaching through water are not established. The proposed 600 km altitude and fluid-lensing application therefore lack a demonstrated imaging-feasibility basis.
- Ground Control & Communications: The access table includes a duplicated access period and inconsistent access numbering, which weakens confidence in the reported mean and total contact statistics.
- Ground Control & Communications: The assertion that access frequency is maximized by selecting a facility close to the poles is not generally valid for this mission; access depends on orbit geometry, site latitude, elevation mask, and operational constraints.
- Mission Duration & EOL: The report first describes an EOL manoeuvre, then states the spacecraft has no thrusters and proposes a drag sail. Drag-sail sizing, deorbit time, and compliance with disposal guidance are not evaluated.
- Bibliography: The report cites Wikipedia as a source despite the task's explicit exclusion, and its references are largely bare URLs without complete bibliographic information. Table citations such as [50]–[74] do not correspond to the listed bibliography.

## Next steps

1. Name the mission operator in the Introduction and distinguish the operator, ground-control facility, customers, and other users; add appropriate sources to support the mission need and user roles.
2. Strengthen the Mission Design with evidence: confirm launch and deployment compatibility, fully specify and interpret the orbit, establish sensor capability for the reef-monitoring task, and resolve the conflicting EOL manoeuvre and drag-sail descriptions with disposal-time analysis.
3. Audit the Ground Control & Communications results and the report presentation: correct duplicated or inconsistently numbered access periods, qualify claims about access frequency, and make figure/table labels and citations consistent with a complete, appropriate bibliography.

---
<sub>Run 20261112-060203-516_Input_2_md_r2 | rubric=openai/gpt-6-luna, task=openai/gpt-6-luna, marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 13650/3564 | cost $0.002236 | 54.76s</sub>
