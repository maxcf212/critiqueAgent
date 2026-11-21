# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a clear Australian reef-monitoring rationale, a single-spacecraft concept, and a recognizable report supported by STK access evidence. To reach the next rubric level, make the operational and payload assumptions testable, resolve inconsistencies in the orbit and disposal plans, and use design evidence to support your conclusions. Completing the references and improving figure and table presentation will also strengthen the report.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the reef-monitoring purpose, Australian rationale and single-spacecraft concept, and names likely science and government customers. The operator is not clearly designated. The Accomplished level requires detailed coverage of all required roles and rationale, supported by appropriate references.

*Assessor reasoning:* The report explains the coral-monitoring mission, its Australian environmental rationale, and why one spacecraft is considered sufficient. It identifies likely science and government customers, but does not clearly designate a spacecraft operator. The concept is understandable, though the user and operational roles are not developed in detail.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Launch, Orbit, Ground Control & Communications, and Mission Duration & EOL sections cover the main design topics and include STK imagery, access data and an inclination calculation. The Accomplished level requires a complete, evidenced design: payload performance, epoch-specific orbital elements, validated ground-service capability, and consistent illumination and disposal plans.

*Assessor reasoning:* The report covers launch, orbit, ground access, mission duration and disposal, and includes STK imagery, access data and an inclination calculation. However, the design is not fully substantiated: payload performance and coverage are not specified, orbital elements are incomplete, the ground-station capability is assumed, and sunlight and EOL claims are inconsistent. No STK project files are supplied.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved, in addition to the already frequent amount of passes."  
> Image 1  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the selected launch, orbit and ground facility and connects the mission to reef protection. To reach Accomplished, draw detailed conclusions from the design evidence and state its limitations; for example, qualify the illumination claim and address the uncertainty about the proposed launcher.

*Assessor reasoning:* The conclusion recaps the selected launch, orbit and ground facility, and notes uncertainty about the proposed launcher. It connects the concept to reef protection, but mainly summarizes choices rather than drawing detailed conclusions from the design evidence or acknowledging its limitations.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "Thus, launch may need to be adjusted if the rocket is still not constructed by the proposed date."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognizable structure, summary, conclusion and bibliography, and is generally readable. The Accomplished level requires consistent, clearly labelled figures and tables, polished writing, and complete, properly matched citations. Address the missing bibliography entries and replace the prohibited Wikipedia source.

*Assessor reasoning:* The report has a recognizable structure, contents, summary, conclusion and bibliography, and is generally readable. However, grammar and wording errors remain; figures and tables are not consistently numbered and captioned; references are incomplete, and some in-text citations have no matching bibliography entries. The cited Wikipedia source is not acceptable under the task instructions.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Ground Control & Communications: "DN path for orbits 1-15"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit; Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 1; Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Contents; Bibliography |

## Technical issues

- Orbit: RAAN is not determined by the launch facility location alone; its value must be tied to a specified epoch and target orbital plane. The listed elements also omit an epoch, so the initial orbit is not fully specified.
- Orbit: A sun-synchronous orbit does not keep the spacecraft continuously sunlit. Eclipse periods can occur, and the descending portion is not inherently the sunlit portion; local solar time and season determine illumination.
- Orbit: The report does not specify sensor spectral bands, ground resolution, swath, pointing, or revisit performance, so it does not demonstrate that a 600 km orbit and the proposed imaging concept can support the required reef monitoring.
- Launch: The equatorial launch advantage is overstated for a near-polar retrograde orbit, and the claimed two daily launch windows are not established by comparing launch-site latitude with inclination alone; target-plane alignment and launch azimuth matter.
- Ground Control & Communications: The Mount Pleasant Radio Observatory is identified, but the report does not establish that it has compatible spacecraft TT&C equipment, frequencies, or operational arrangements. The access results alone do not establish a functioning ground-control service.
- Mission Duration & EOL: The report first calls EOL the only orbital manoeuvre, then says the spacecraft has no thrusters and proposes a passive drag sail. A drag sail is a passive deorbit device, not a commanded orbital manoeuvre; its size and expected deorbit time are not calculated.
- Launch; Bibliography: The report relies on a Wikipedia spaceflight calendar despite the task explicitly prohibiting Wikipedia, and launch-table citations such as [49] and [50]–[74] have no corresponding bibliography entries.

## Next steps

1. In the Introduction, identify the spacecraft operator explicitly and explain how the proposed government and science customers will use the data. Develop the single-spacecraft rationale with evidence about the mission’s coverage and revisit needs.
2. In Orbit and Ground Control & Communications, specify the sensor bands, resolution, swath, pointing and revisit performance; give the orbital elements with an epoch and justify the RAAN and launch-plane alignment. Verify Mount Pleasant’s TT&C capability, then reconcile illumination claims and calculate the drag sail’s size and expected deorbit time. Include STK project files and supporting evidence.
3. In the Conclusion, draw specific findings from your design evidence and acknowledge unresolved limitations. For presentation, number and caption figures and tables consistently, correct grammar and wording, remove the prohibited Wikipedia source, and ensure every in-text citation—including [49] and [50]–[74]—has a matching bibliography entry.

---
<sub>Run Input_2-Run_3-Eff_high-261115-165712 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15245/7533 | cost $0.004455 (incl. $0.001387 for the reused reference rubric+task structure) | 46.61s</sub>
