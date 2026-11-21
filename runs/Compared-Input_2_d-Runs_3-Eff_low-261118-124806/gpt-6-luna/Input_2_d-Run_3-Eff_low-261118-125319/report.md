# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent Australian reef-monitoring concept and cover the main mission segments, including STK access analysis. To reach the next rubric level, strengthen the design’s technical evidence: correct the launch-site and orbit details, substantiate communications and end-of-life plans, and identify users and support claims with reliable references. Your conclusion and report presentation would also benefit from clearer evaluation and more consistent editing and citations.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the Australian conservation rationale and justifies using one spacecraft. To reach the next level, clearly name the operator and customer groups, describe their roles, and support the rationale and user discussion with relevant literature.

*Assessor reasoning:* The mission purpose and Australian conservation rationale are explained, and a single spacecraft is justified in terms of coverage needs, simplicity and cost. The operator and customer groups are not clearly identified, and the rationale and user discussion are not supported consistently by formal literature citations.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Launch, Orbit, and Ground Control & Communications sections cover key design elements and include STK access outputs. To reach the next level, correct the site coordinates and sun-synchronous inclination, verify the launcher and schedule, define orbital elements with epoch and frame, and provide evidence for coverage, link capacity, maneuvers, and quantified end-of-life disposal; include software files and assumptions.

*Assessor reasoning:* The report covers launch, orbit, STK access analysis, ground station, duration and disposal, with useful simulation outputs. However, the stated inclination is inconsistent with a 600 km sun-synchronous orbit: it should be about 97.8°, not 87.79°. The launch-site latitude is also wrong, launch timing is inconsistent, and the maneuver/EOL discussion lacks a quantified disposal plan. No software files are supplied.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan"  

### C3 Conclusion (5/10, Adequate)

Your Conclusion summarizes the proposed design and notes launch uncertainty. To reach the next level, use the report’s evidence to assess whether the design meets its aims, address key limitations and uncertainties, and avoid repeating the unsupported claim that the stated orbit provides consistent illumination.

*Assessor reasoning:* The conclusion summarizes the proposed launcher, orbit and ground station and notes launch uncertainty. It is relevant but mostly restates design choices, does not assess key limitations or uncertainties in the evidence, and repeats the incorrect characterization of the orbit as suitable for consistent illumination.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognizable structure, executive summary, figures, tables, and bibliography. To reach the next level, improve editing and completeness, standardize figure/table presentation and citations, and provide complete, reliable references; remove Wikipedia and replace bare or incomplete URLs.

*Assessor reasoning:* The report has a recognizable structure, executive summary, figures, tables and bibliography. However, grammar and editing problems remain, the EOL sentence is incomplete, and figure/table presentation and citations are inconsistent. The bibliography is mostly bare URLs and includes Wikipedia, which the task explicitly disallows. These issues reduce professionalism and traceability.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | partial | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Kourou is approximately 5.2° N, not 45.05° N. The latitude comparison and launch-window reasoning therefore rely on an incorrect site coordinate.
- Launch: The report proposes a 2025 launch using Vega E, while also stating its first launch will occur in 2024. Vega E was not an established available launcher for the proposed schedule; the launch choice and schedule require verification and contingency planning.
- Orbit: At 600 km altitude, a circular sun-synchronous orbit requires a retrograde inclination near 97.8°. The reported 87.7924° is not sun-synchronous and conflicts with the claim of a retrograde orbit.
- Orbit: RAAN does not indicate the launch facility's location; it specifies the inertial direction of the ascending node at a stated epoch. The orbital elements omit an epoch and use argument of latitude without specifying the reference frame or epoch.
- Orbit: A 600 km orbit does not by itself establish adequate imaging resolution or swath coverage. No instrument resolution, swath, pointing, spectral requirements or coverage analysis is provided to substantiate reef-monitoring performance.
- Ground Control & Communications: The reported access durations depend on the modeled ground-station coordinates, antenna masks and link assumptions, none of which are supplied. Pass access alone does not establish communications capacity or data downlink sufficiency.
- Mission Duration & EOL: A drag sail is proposed but its area, deployment reliability, post-mission orbit lifetime and compliance with disposal guidance are not quantified. A passive sail does not guarantee prompt re-entry from 600 km.
- Bibliography: The report cites Wikipedia, which is explicitly unacceptable under the task instructions; several references are incomplete bibliographic entries.

## Next steps

1. In Introduction, identify the spacecraft operator and customer groups explicitly, explain their roles, and support the mission rationale with appropriate literature.
2. Recheck the Launch and Orbit sections: verify Kourou’s latitude and launcher availability for the proposed schedule, and use an approximately 97.8° inclination for a 600 km sun-synchronous orbit. State the orbital-element epoch and reference frame; quantify instrument performance and coverage, maneuver needs, communications capacity, and drag-sail disposal lifetime. Provide the STK files and underlying ground-station and link assumptions.
3. Revise the Conclusion to weigh the evidence, limitations, and uncertainties rather than mainly restating choices. Edit the report for clarity and completeness, make figure/table presentation and citations consistent, and replace Wikipedia and bare or incomplete URLs with reliable, complete references.

---
<sub>Run Input_2_d-Run_3-Eff_low-261118-125319 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15133/4789 | cost $0.003076 (incl. $0.001387 for the reused reference rubric+task structure) | 31.61s</sub>
