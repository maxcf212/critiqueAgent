# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

Your report presents a solid preliminary mission with clear STK evidence and a logical structure. The introduction and conclusion are strong; the main design addresses most requirements but has technical errors (RAAN justification, missing LTAN), no link budget, and weak referencing (Wikipedia, bare URLs). Presentation is readable but figures/tables and bibliography need consistent formatting. Files are not evident.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

You address the primary mission, need, single-spacecraft rationale and users, with good references. The operator/customers are somewhat implied (e.g. CSIRO, BOM) rather than fully explicit. To strengthen toward upper Accomplished, state the operator and customer roles explicitly and support the mission need with more specific literature.

*Assessor reasoning:* Addresses primary mission, need, single-spacecraft rationale, and users. Users are somewhat implied rather than fully explicit, but overall a strong introduction with references.
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You present STK screenshots and tables and address launch, orbit, ground control, duration and EOL. However, RAAN is incorrectly tied to launch-site longitude, LTAN is missing, no link budget supports contact claims, and the drag-sail deorbit is unquantified. Wikipedia weakens the launch comparison. For Accomplished, correct these technical points, add quantitative evidence and include software files.

*Assessor reasoning:* Major requirements addressed with STK screenshots and tables. Technical errors (RAAN justification), missing LTAN, no link budget, and reliance on Wikipedia reduce quality; files not provided.
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Orbit: "The initial value indicates the location of the launch facility."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  

### C3 Conclusion (7/10, Accomplished)

Your conclusion draws specific points from the design (Vega E, Mt Pleasant, orbit type) and is reasonably detailed. To strengthen within Accomplished, tie each conclusion explicitly to the evidence presented and acknowledge key limitations or assumptions (e.g. unbuilt launch vehicle, link budget absent) without introducing new material.

*Assessor reasoning:* Conclusions are clearly drawn from the design evidence, with specific references to launch, orbit, and ground station. Reasonably detailed.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (10/20, Adequate)

The report has clear headings, but figures/tables lack numbers and consistent labelling, and the bibliography uses bare URLs and Wikipedia. Writing is generally readable. For Accomplished, use a consistent engineering report format, number and caption all figures/tables, provide a concise executive summary, and ensure all references are properly formatted and matched in text.

*Assessor reasoning:* Clear section structure but inconsistent formatting: figures/tables lack numbers, bibliography is bare URLs, and Wikipedia is used. Writing is generally readable but referencing is weak.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: RAAN initial value incorrectly stated to indicate launch facility location; RAAN is an inertial node, not site longitude.
- Orbit: No local time of ascending node (LTAN) specified, critical for sun-synchronous lighting and daytime descending imaging.
- Ground Control & Communications: No communication link budget or data rate analysis to support the claimed data transfer feasibility.
- Launch: Relies on Wikipedia's '2021 in spaceflight' for launch comparison; Wikipedia is explicitly unacceptable.
- Bibliography: References are bare URLs with missing titles, authors, and dates; inconsistent formatting.
- Launch: Launch comparison tables appear copied from Wikipedia with footnotes not included in the bibliography, raising attribution concerns.
- Mission Duration & EOL: Drag sail deorbit strategy is not quantified (e.g., estimated time to deorbit from 600 km).
- Orbit: Epoch time for argument of latitude 0° is not stated.

## Next steps

1. Correct the orbit section: explain RAAN as an inertial node rather than launch-site longitude, add LTAN and the epoch for argument of latitude 0°, and support the sun-synchronous design with a clear lighting/imaging rationale.
2. Add a communication link budget/data-rate analysis for the Mt Pleasant contact windows, and quantify the drag-sail deorbit time from 600 km; include STK/software files in an appendix.
3. Replace Wikipedia and bare URLs with properly cited peer-reviewed/agency sources; number and label all figures/tables and ensure in-text citations match the reference list.

---
<sub>Run Input_2-Run_2-Eff_low-261118-113017 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14258/9498 | cost $0.006011 (incl. $0.001387 for the reused reference rubric+task structure) | 66.03s</sub>
