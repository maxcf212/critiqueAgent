# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 41 / 100 (41%)**

You present a clear Australian reef-monitoring rationale, justify using one spacecraft, and include useful STK outputs within a recognisable engineering report structure. However, errors in the orbit design undermine key mission claims, while payload feasibility, communications, ground-station capability and end-of-life disposal need stronger evidence. Your conclusion and presentation would also benefit from more precise, consistent reporting and referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You explain the reef-monitoring need and justify one spacecraft, and you identify scientists as users. To reach Accomplished, name the operating organisation and customers, describe the sensor and its suitability for reef imaging, and support the rationale with appropriate references.

*Assessor reasoning:* The mission purpose and Australian reef rationale are explained, and the choice of one spacecraft is justified. Scientists are identified as users, but the operating organisation and paying or operational customers are not clearly named. The mission concept also lacks detail on the payload and its suitability for the proposed observations.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Executive Summary: "The satellite, nicknamed ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), is operated and accessed from Australia ground facilities"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

You cover launch, orbit, ground access and EOL, with useful STK outputs. However, the Orbit section’s 600 km altitude implies a semi-major axis near 6971 km and a sun-synchronous inclination near 97.8°, not the values stated; the Launch section also gives Kourou’s latitude incorrectly. To reach Accomplished, correct these and substantiate payload, communications, station capability and disposal performance with calculations, sources and project evidence.

*Assessor reasoning:* The report addresses launch, orbit elements, nominal manoeuvres, ground access and EOL, and includes STK imagery and an access report. However, the central orbit calculation is incorrect, and several design claims are unsupported or inconsistent. No STK project files are supplied, and there is little payload, coverage, communications-link or disposal analysis. These significant errors and omissions limit the design evidence.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Image 1  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved, in addition to the already frequent amount of passes."  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (4/10, Adequate)

Your Conclusion recaps the selected design, but repeats claims about consistent illumination and ground-station access that are not established. To reach Accomplished, draw specific conclusions from validated orbit, access and mission-lifetime results, and explain their implications for the mission.

*Assessor reasoning:* The conclusion summarises the selected launch, orbit and ground facility and relates them to the mission aim. It is mostly a recap rather than a detailed conclusion drawn from validated results; in particular, it repeats inaccurate claims about illumination and ground-station access.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Your executive summary, contents and engineering sections provide a clear structure. To reach Accomplished, improve grammar and consistent figure captions, complete and standardise reference details, ensure citations match the bibliography, and exclude Wikipedia as required.

*Assessor reasoning:* The report has an executive summary, contents and recognisable engineering sections, but grammar and wording errors, inconsistent figure labelling/captions and incomplete reference formatting reduce professionalism. Wikipedia is used as a source despite the task excluding it, and the bibliography does not consistently provide full reference details.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite – specifically for coral reef and ocean monitoring."  
> Launch: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: A 600 km altitude with Earth radius 6371 km gives a semi-major axis of about 6971 km, not 7171 km. The listed semi-major axis therefore conflicts with the stated altitude.
- Orbit: At approximately 600 km, a sun-synchronous orbit requires a retrograde inclination near 97.8°, not 87.79°. The stated inclination is prograde and cannot produce the claimed sun-synchronous nodal precession.
- Orbit: The stated RAAN does not follow from the launch-site location. RAAN depends on the selected orbital plane and epoch; launch-site latitude alone does not determine it.
- Launch: Kourou is at approximately 5.2° N, not 45.05° N. The stated latitude is wrong, and launch-window availability cannot be inferred from comparing that latitude with the target inclination alone.
- Ground Control & Communications: The reported mean access duration of 580.786 seconds is about 9.68 minutes, not almost twenty minutes. The report also gives no link budget or data-rate analysis to substantiate that contacts can transfer the collected imagery.
- Orbit: Sun-synchronous orbit gives a consistent local solar time, not constant sunlight. The claim that the satellite is constantly sunlit on its descending path is not demonstrated and is generally not assured.
- Introduction: No sensor specifications, spatial resolution, spectral bands or swath are given to show that an orbital payload can perform the proposed reef imaging or fluid-lensing analysis. The image-formation and underwater-visibility constraints are not assessed.
- Ground Control & Communications: Mt Pleasant Radio Observatory is identified, but the report does not establish that its radio astronomy facilities provide satellite TT&C capability, suitable antennas, frequencies or operational ground-control services.
- Mission Duration & EOL: A drag sail is proposed without sizing, deployment details or an estimated decay time at the stated altitude. The report therefore does not demonstrate that the disposal plan meets a debris-mitigation lifetime.

## Next steps

1. Rework the Orbit and Launch sections: calculate and cross-check the semi-major axis and sun-synchronous inclination for the stated altitude, determine RAAN from the selected plane and epoch, and correct Kourou’s latitude. Support launch-window and illumination claims with appropriate analysis.
2. Strengthen the mission evidence: specify the payload and assess whether it can image reefs; verify the ground facility’s TT&C capability; add a link budget and data-rate analysis, clarify that the reported 580.786-second access is about 9.68 minutes, and size the drag sail and estimate disposal time.
3. To reach the next rubric level, identify the operator and customers, draw evidence-based conclusions from validated results, and polish figure captions, grammar and references. Provide complete, consistent citations, exclude Wikipedia as required, and include the STK project files or equivalent supporting evidence. 

---
<sub>Run Input_2_d-Run_1-Eff_high-261116-112003 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15339/8892 | cost $0.006362 (incl. $0.001387 for the reused reference rubric+task structure) | 63.95s</sub>
