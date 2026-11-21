# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent Australian reef-monitoring concept, justify using one spacecraft, and include STK access outputs. To reach the next rubric level, strengthen the design evidence and technical accuracy—especially the sun-synchronous orbit—identify the mission users explicitly, and draw more evidence-based conclusions. Your report structure is recognizable, but presentation and referencing need greater consistency.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the reef-monitoring need and justifies a single spacecraft. To reach Accomplished, explicitly identify the operator and customer groups rather than referring generally to Australian ground facilities, and strengthen the supporting references.

*Assessor reasoning:* The mission purpose and need are explained with relevant context, and the single-spacecraft choice is justified. However, the operator and customer groups are not identified explicitly; saying the satellite is operated and accessed from Australian ground facilities does not name its operator or customers. Referencing is present but uneven.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You address launch, orbit, manoeuvres, ground access, mission duration and disposal, with useful STK outputs. The stated 87.7924° inclination is not sun-synchronous at 600 km; correct it to about 97.8° retrograde. Also correct the launch-site latitude, complete the orbit specification, define the access-analysis interval, and quantify EOL compliance to reach Accomplished.

*Assessor reasoning:* The report covers launch, orbit, manoeuvres, ground access, duration and disposal, and includes STK-derived figures and access data. But the SSO inclination is technically incorrect: at 600 km, a sun-synchronous orbit requires roughly 97.8° retrograde, not 87.79°. Launch-site latitude is also misstated, orbital elements are incomplete, and the disposal plan lacks quantified compliance or decay time. Software files are not evidenced.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion summarizes the selected design and notes launch-vehicle uncertainty. To reach Accomplished, interpret what the evidence establishes, address key uncertainties—including the corrected orbit and imaging performance—and explain how these affect mission feasibility.

*Assessor reasoning:* The conclusion summarizes the selected launch, orbit and ground station and acknowledges launch-vehicle uncertainty. It is relevant but mostly restates design choices and does not draw detailed conclusions from the evidence or address key uncertainties such as imaging performance and the incorrect SSO inclination.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognizable structure, executive summary, figures and bibliography. To reach Accomplished, make writing and formatting consistent, give Images 1–5 formal numbers and titles with clear in-text references, and provide a complete, consistently formatted bibliography using appropriate sources.

*Assessor reasoning:* The report has a recognizable structure, contents, executive summary, figures and bibliography. However, the writing and formatting are inconsistent, figures lack formal numbering/titles in the text, and the bibliography is incomplete and inconsistently formatted. It relies on Wikipedia despite the task explicitly disallowing it. These weaknesses prevent professional-level presentation.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Launch: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Images 1–5; Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: A 600 km circular sun-synchronous orbit requires a retrograde inclination near 97.8°; the stated 87.7924° is not sun-synchronous at this altitude.
- Launch: Guiana Space Centre is near 5° N latitude, not 45.05° N. Its latitude is lower than the target inclination, but the report's stated value is erroneous.
- Orbit: The explanation that the orbit passes over almost the entire Earth is overstated: a near-polar orbit does not provide coverage to all latitudes, and the stated inclination also excludes latitudes beyond about 87.8°.
- Orbit: The COE set is incomplete as an epoch and a defined position/phase are needed to specify the orbit. Argument of latitude is a valid alternative for a circular orbit, but the stated RAAN rationale does not establish that its value is the launch-site location.
- Ground Control & Communications: The access table appears to cover only a short, selected interval; the reported mean contact time should not be interpreted as an average daily contact duration without specifying the analysis interval and access assumptions.
- Mission Duration & EOL: A passive drag sail is proposed, but no sail sizing, expected deorbit time, or demonstration that the disposal approach meets applicable debris-mitigation guidelines is provided.

## Next steps

1. In Introduction, name the spacecraft operator and customer groups, and explain their roles and how they will use the data. Support the rationale with consistently cited sources.
2. In Orbit, correct the 600 km sun-synchronous inclination to approximately 97.8° retrograde, verify the launch-site latitude, and provide a complete orbit specification including epoch and a defined position or phase. Clarify coverage limits. In Ground Control & Communications, define the access-analysis interval and assumptions before interpreting average contact time; include the software files or sufficient reproducible analysis evidence.
3. In Mission Duration & EOL, quantify the drag-sail design and expected deorbit time, and show how the disposal plan meets applicable debris-mitigation guidance. In Conclusion, draw specific findings from the design evidence and acknowledge remaining uncertainties. Number and title Images 1–5 consistently, and revise the bibliography to use complete, consistent, appropriate sources.

---
<sub>Run Input_2_d-Run_1-Eff_low-261118-125222 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15098/4188 | cost $0.00398 (incl. $0.001387 for the reused reference rubric+task structure) | 26.2s</sub>
