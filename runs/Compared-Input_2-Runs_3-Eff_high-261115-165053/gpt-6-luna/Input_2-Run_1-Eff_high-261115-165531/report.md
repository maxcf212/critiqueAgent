# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent Australian reef-monitoring concept and cover the main mission-design sections, with STK access outputs supporting the report. To strengthen the work, make the operator and payload capability specific, verify key orbit and ground-link assumptions, quantify end-of-life disposal, and improve evidence, referencing and presentation so your conclusions follow from demonstrated performance.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the Australian reef-monitoring need, the one-spacecraft concept and likely science and government customers. To reach Accomplished, identify a specific operator and clarify the operator/customer roles, which currently remain vague.

*Assessor reasoning:* The reef-monitoring purpose, Australian benefit, rationale for one spacecraft, and likely science/government customers are explained. The discussion of bleaching and monitoring need is detailed. However, no specific organisation is identified as the spacecraft operator, and the customer/operator roles remain vague.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  
> Executive Summary: "The satellite, nicknamed ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), is operated and accessed from Australia ground facilities"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, access, duration and EOL, and STK access outputs support the design. To reach Accomplished, demonstrate sensor, resolution, swath and revisit feasibility for the reef areas; specify node local time and epoch and correct the RAAN interpretation; verify Mount Pleasant TT&C capability; quantify drag-sail re-entry against disposal guidance; and include STK project files.

*Assessor reasoning:* The report covers launch, orbit, ground access, duration, and disposal, with STK images and access results. The orbital inclination is plausible for a 600 km sun-synchronous orbit. However, payload capability and reef imaging performance are not established; the local-time-of-node assumption is missing; ground-station compatibility is unverified; and the drag-sail disposal performance is not quantified. STK project files are not provided in the submission.
> Launch: "the proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved, in addition to the already frequent amount of passes."  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  
> Image 1  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the launch, orbit and ground facility and connects the concept to reef protection. To reach Accomplished, draw more detailed conclusions from demonstrated imaging and operational performance, rather than mainly restating design choices.

*Assessor reasoning:* The conclusion recaps the selected launch, orbit, and ground facility and relates the mission to reef protection. It is relevant, but mostly summarizes earlier choices rather than drawing detailed conclusions from demonstrated imaging or operational performance.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognisable structure, executive summary, headings, conclusion and supporting figures. To reach Accomplished, use consistent numbered captions, improve grammar, complete and cross-check references (including table citations), and replace the Wikipedia source with authoritative references.

*Assessor reasoning:* The report has a recognisable engineering structure, executive summary, headings, conclusion, and bibliography, and the figures support the discussion. Presentation is not fully professional: figures and tables lack consistent numbered captions, several text and grammar issues remain, the bibliography entries are incomplete, and table citations such as [49]–[74] do not match the listed references. Wikipedia is also used despite the task disallowing it.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Image 4  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: A sun-synchronous orbit provides a consistent local solar time, but does not keep the spacecraft continuously illuminated. The claim that the descending path is constantly in sunlight is unsupported because the local time of the ascending or descending node is not specified.
- Orbit: The report says RAAN indicates the launch-facility location. RAAN describes the inertial orientation of the orbital plane; achieving the desired plane requires launch timing and injection geometry. The stated elements also lack a clear epoch.
- Orbit: No sensor, spatial or spectral resolution, swath, or revisit analysis demonstrates that a 600 km satellite can produce useful fluid-lensing reef images or cover the proposed areas at the stated cadence.
- Ground Control & Communications: Mount Pleasant is identified as a radio observatory, but the report does not establish spacecraft TT&C/data-link capability, compatible frequencies, antenna availability, or operational support there.
- Mission Duration & EOL: The drag sail is proposed without sizing, a predicted decay/re-entry time, or evidence that the disposal plan meets an applicable debris-mitigation timeline.
- Mission Design: The report presents STK outputs but does not include the requested relevant STK project files in the submitted material.

## Next steps

1. In the Introduction, name a specific spacecraft operator and distinguish its responsibilities from those of science or government customers. In the Orbit section, justify the proposed reef-imaging capability with sensor, resolution, swath and revisit analysis.
2. Validate the orbit geometry by specifying the orbital-element epoch and node local time, and accurately explain RAAN and launch-plane targeting. Confirm Mount Pleasant’s compatible TT&C and data-link capability, include the STK project files, and quantify drag-sail sizing and re-entry time against disposal guidance.
3. Revise the Conclusion to draw specific findings from your imaging and access analyses. Standardise numbered figure and table captions, correct writing issues, and complete and cross-check the bibliography; replace the Wikipedia reference with suitable authoritative sources.

---
<sub>Run Input_2-Run_1-Eff_high-261115-165531 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15189/8819 | cost $0.006307 (incl. $0.001387 for the reused reference rubric+task structure) | 58.9s</sub>
