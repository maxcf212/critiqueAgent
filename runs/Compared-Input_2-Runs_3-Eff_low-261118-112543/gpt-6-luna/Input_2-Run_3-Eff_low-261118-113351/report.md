# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent coral-monitoring concept, explain the value of a single spacecraft, and include STK access results. To reach the next rubric level, strengthen the evidence behind key design choices, resolve inconsistencies in orbit and communications claims, and provide a more complete, professionally presented report with reliable references.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the coral-monitoring purpose, its public and scientific value, and why one satellite is proposed; you also name likely customers. For the next level, clearly identify the operator and operating arrangement, and strengthen the rationale and supporting references.

*Assessor reasoning:* The report explains the coral-monitoring mission, its public and scientific value, and why one spacecraft is proposed. It identifies likely customers but does not clearly identify the spacecraft operator or establish a specific operating arrangement; the rationale and supporting references are also uneven.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit elements, STK access, a ground facility, mission duration, and drag-sail disposal. The STK output is useful evidence. For the next level, correct and substantiate orbit claims, validate launch feasibility, connect orbit to imaging performance, reconcile access results with communications claims, and provide software files or reproducible evidence.

*Assessor reasoning:* The report covers launch, an SSO orbit with several elements, STK access results, a ground facility, mission duration, and a passive drag-sail disposal concept. However, important choices are speculative or insufficiently justified, the orbital description has errors and omissions, and there is no clear validated coverage analysis or supplied software project file. Communication-rate claims are not reconciled with the access results.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the main design choices and acknowledges launch uncertainty. To reach the next level, draw conclusions from demonstrated results: assess coverage, revisit, imaging, and data-transfer capability, and explain the effect of unresolved limitations on mission feasibility.

*Assessor reasoning:* The conclusion recaps the major design choices and acknowledges launch uncertainty, but it mostly restates the proposal. It does not assess whether the evidence demonstrates mission performance or resolve key limitations such as revisit, imaging, and data-transfer capability.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognisable structure, an executive summary, labelled visuals, and a bibliography. For the next level, improve grammar and consistency in figure and table presentation, complete and standardise references, remove the disallowed Wikipedia source, and cite design claims adequately.

*Assessor reasoning:* The report has a recognisable structure, an executive summary, labelled visual material, and a bibliography. Presentation is weakened by grammatical errors, inconsistent figure/table labelling and formatting, incomplete reference details, and use of Wikipedia despite the task explicitly disallowing it. Several claims and design decisions are not adequately cited.
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
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit; Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: The report says RAAN's initial value indicates the launch facility location. RAAN defines the inertial orientation of the ascending node; it is not determined by the launch site's location alone.
- Orbit: The report calls the orbit retrograde but later describes its paths as near-polar without giving a selected local solar time or node-time requirement. A sun-synchronous orbit provides a consistent local solar time, but does not by itself guarantee the claimed imaging illumination conditions.
- Ground Control & Communications: The claim that a near-polar orbit gives significant contact for the vast majority of passes is not established. Access depends on station latitude, geometry, elevation mask, and orbit; the listed access windows instead show intermittent contacts.
- Ground Control & Communications: The text claims an average contact duration of almost ten minutes, while the stated mean is 580.786 seconds, approximately 9.68 minutes. The table also has inconsistent access numbering and reports only a subset of the access periods.
- Orbit: The 600 km altitude and 250 km reef width are not connected to a sensor field of view, ground sampling distance, or imaging performance calculation, so the proposed coverage and resolution trade is unsupported.
- Mission Duration & EOL: The five-year lifetime is asserted without spacecraft reliability, power, propellant, or orbital-decay analysis. A drag sail is a plausible passive disposal concept, but its deployment and compliance with applicable disposal limits are not demonstrated.
- Launch: Vega E is presented as a planned option for a 2025 launch despite being a future launcher in the report's timeframe; the proposed rideshare, orbit compatibility, and launch date are not confirmed.
- Bibliography: Reference [6] cites Wikipedia, which the assignment explicitly disallows; several other entries are incomplete and do not provide consistent author, title, date, or access information.

## Next steps

1. In Orbit and Ground Control & Communications, correct the RAAN explanation and clarify the selected orbit’s local solar time. Use the actual station geometry and access windows to support contact frequency and duration, and connect altitude and reef width to sensor field of view, ground sampling distance, and imaging performance.
2. In Launch and Mission Duration & EOL, verify that the launch vehicle, date, rideshare, and target orbit are feasible. Support the five-year lifetime and drag-sail disposal plan with relevant reliability, power, propellant, orbital-decay, and disposal-compliance evidence; include the software project files or reproducible design evidence.
3. In the Introduction, Conclusion, and Bibliography, identify the operator and clarify the operating arrangement, evaluate whether the evidence supports mission performance, and replace Wikipedia with complete, consistent, credible references. Proofread grammar and standardise figure and table labels and formatting. 

---
<sub>Run Input_2-Run_3-Eff_low-261118-113351 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15200/4288 | cost $0.002827 (incl. $0.001387 for the reused reference rubric+task structure) | 28.37s</sub>
