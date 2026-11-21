# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 45 / 100 (45%)**

You present a clear Great Barrier Reef monitoring concept, explain why one spacecraft is proposed, and use STK visualisations to cover key mission segments. The main limitation is that errors in the orbit design undermine the mission analysis, while the operator, customer organisations, and ground-station capability need clearer definition. Correcting these points and strengthening the supporting evidence will make your conclusions more dependable.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction clearly explains the reef-monitoring purpose and environmental rationale, and justifies using one spacecraft for simplicity and cost. You identify marine and conservation scientists as users. To reach the next rubric level, name the responsible operator and specific customer organisations, and support the discussion with appropriate references.

*Assessor reasoning:* The Great Barrier Reef monitoring mission and its environmental rationale are explained in detail, and the single-spacecraft choice is justified. Marine and conservation scientists are identified as users, but the responsible operator and specific customer organisations are not clearly named.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

Your Launch and mission-segment sections cover the requested topics and include useful STK visualisations. However, the stated 87.79° inclination, 7171 km semi-major axis, and Kourou latitude of 45.05° are incorrect; the ground-station capability is also unsubstantiated. The next rubric level requires corrected, verifiable design results and stronger evidence, including STK files.

*Assessor reasoning:* The report covers launch, orbit, ground access, mission duration and disposal, and includes STK imagery and access results. However, major orbital-element errors undermine the central design; the ground-station communications claim is not adequately substantiated, and no STK project files are provided. The work shows some design understanding but is not a reliable, comprehensive mission design.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved, in addition to the already frequent amount of passes."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the launch, orbit, and proposed ground facility, and notes a launch-vehicle risk. Its conclusions about orbit and illumination are not adequately supported by the design results. To reach the next rubric level, draw specific conclusions from corrected calculations and evidence for mission, imaging, and communications performance.

*Assessor reasoning:* The conclusion summarises the proposed launch, orbit and ground facility, and acknowledges a launch-vehicle risk. It is mostly a recap, however, and its positive conclusions are not well supported given the orbit calculation errors and limited evidence for imaging and communications performance.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "Thus, launch may need to be adjusted if the rocket is still not constructed by the proposed date."  

### C4 Report presentation (10/20, Adequate)

Your report has a logical structure, contents list, executive summary, headings, figures, and bibliography. To reach the next rubric level, make prose and formatting consistent, number figures and tables clearly, complete and check references, and use sources appropriate to the task.

*Assessor reasoning:* The report has a logical structure, contents list, executive summary, headings, figures, and bibliography. Presentation is not fully professional: prose and formatting are inconsistent, figures and tables lack clear numbering, references are incomplete, and Wikipedia is used despite the task excluding it as an acceptable source.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit (Images 1–5); Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: At 600 km altitude, a sun-synchronous orbit requires a retrograde inclination of approximately 97.8°, not 87.79°. The stated inclination is prograde and would not produce the claimed sun-synchronous nodal precession; the plotted curve itself is near 97.8° at 600 km.
- Orbit: The semi-major axis is inconsistent with the stated Earth radius and altitude: 6371 km + 600 km = 6971 km, not 7171 km.
- Launch: Kourou is near 5.2° N, not 45.05° N. This also invalidates the stated comparison of the launch-site latitude with the target inclination.
- Orbit: RAAN is not determined by the launch facility's location as stated; it is an inertial orbital orientation that depends on launch timing and epoch.
- Ground Control & Communications: The reported mean access duration of 580.786 seconds is about 9.7 minutes, not almost twenty minutes.
- Ground Control & Communications: The report assumes Mount Pleasant Radio Observatory can provide spacecraft communications without establishing suitable TT&C antennas, frequencies, or link performance. A sun-synchronous orbit also does not guarantee continuous sunlight or a daylight descending track; local solar time and eclipse conditions are not specified.

## Next steps

1. Recheck the orbit calculations and update the STK model and figures: at 600 km, the sun-synchronous inclination is approximately 97.8° retrograde, and the semi-major axis is 6971 km using the stated Earth radius. Define RAAN in relation to launch timing and epoch, and provide the STK project files so your results can be checked.
2. Verify the launch and communications assumptions. Use Kourou’s approximate latitude of 5.2° N, and substantiate Mount Pleasant’s suitability with TT&C antenna, frequency, and link-performance evidence. Reconcile the 580.786-second access duration with your text, and specify local solar time and eclipse conditions.
3. Name the responsible spacecraft operator and specific customer organisations. Strengthen evidence for imaging and communications performance, then use that evidence in your conclusion. Review figure and table numbering, consistency of prose and formatting, and reference completeness; replace Wikipedia with an appropriate source.

---
<sub>Run Input_2_d-Run_2-Eff_high-261116-112107 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15071/8742 | cost $0.005045 (incl. $0.001387 for the reused reference rubric+task structure) | 63.12s</sub>
