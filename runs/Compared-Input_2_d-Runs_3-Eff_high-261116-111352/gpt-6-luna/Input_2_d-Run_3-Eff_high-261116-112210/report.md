# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a clear coral-reef monitoring concept and cover most mission elements, with a logical report structure and STK access figures. The main limitation is that key orbit values and interpretations are inconsistent, weakening confidence in the design. Strengthen the technical evidence, clarify who operates the mission and who uses its data, and make your conclusions reflect what the analysis does—and does not—demonstrate.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the coral-reef monitoring need, identifies marine and conservation scientists as users, and justifies using one spacecraft. To reach the next level, clearly name the mission operator and distinguish it from customer or user groups, with complete supporting references.

*Assessor reasoning:* The report gives a clear coral-reef monitoring mission, explains the need, and justifies using one spacecraft. It identifies scientists as users and mentions Australian ground facilities, but does not clearly name the mission operator or distinguish operator from customers. The rationale is detailed, although referencing is incomplete.
> Introduction: "Thus, only one satellite is required."  
> Executive Summary: "operated and accessed from Australia ground facilities"  
> Introduction: "marine and conservation scientists"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Launch, Orbit and Ground Control & Communications sections cover the main design elements, and Images 1–5 provide STK access evidence. However, the stated 87.79° inclination cannot provide sun-synchronous precession; correct the orbit elements and support payload, link and EOL performance. Clarify access timing and provide the relevant STK files.

*Assessor reasoning:* The report covers launch, orbit, ground access, mission duration and EOL, and includes STK screenshots and access data. However, major orbit calculations are inconsistent or incorrect, and several conclusions overstate what the evidence establishes. Ground-station link performance and payload imaging capability are not demonstrated. Relevant STK files are not evident in the submission.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Image 1  
> Image 4  

### C3 Conclusion (5/10, Adequate)

Your Conclusion usefully recaps the proposed design, but mostly summarizes it and presents consistent illumination too definitively. To reach the next level, draw specific conclusions from validated orbit and performance evidence, and identify limitations where the analysis does not establish mission capability.

*Assessor reasoning:* The conclusion recaps the proposed launch, orbit and ground facility and notes that the launcher choice may need adjustment. It is relevant but mainly summarizes the design; conclusions are not critically qualified against the orbit errors or the limited evidence for mission performance.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (8/20, Adequate)

Your report has an Executive Summary, logical headings and a generally understandable structure. For a more professional standard, edit recurring grammar and wording issues, present the Bibliography consistently, and ensure every in-text citation matches a suitable listed source; the launch citations and Wikipedia reference need attention.

*Assessor reasoning:* The report has a logical structure, executive summary, headings and a generally understandable style. Grammar and wording have recurring flaws, and the bibliography is not professionally presented. Wikipedia is cited despite being disallowed, and launch-table citations such as [49]–[55] do not match the listed bibliography.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite – specifically for coral reef and ocean monitoring."  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary; Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications; Images 1–5 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: The stated 87.79° inclination is prograde and cannot provide the required positive sun-synchronous nodal precession. A circular orbit near 600 km requires a retrograde inclination of roughly 97.8° under the usual J2 model.
- Orbit: The orbital-element table gives a = 7171 km, but with the stated 6371 km Earth radius and 600 km altitude, a should be approximately 6971 km.
- Orbit: RAAN is not determined by the launch facility's location as claimed. The selected launch time and orbital-plane geometry determine the achievable RAAN.
- Launch: Kourou is at approximately 5° N, not 45.05° N. The reported latitude is incorrect.
- Ground Control & Communications: The reported mean access duration of 580.786 seconds is about 9.7 minutes, not almost 20 minutes.
- Orbit; Ground Control & Communications: A sun-synchronous orbit does not inherently provide continuous sunlight to the spacecraft, nor does it guarantee that the descending orbit segment is sunlit. Local time of node and eclipse geometry are not specified.
- Launch: The report generalizes that launch vehicles inject passenger satellites into the same orbit. Rideshare deployments may use different orbits through separate deployment stages or propulsion.
- Mission Duration & EOL: The drag-sail EOL proposal lacks sail sizing, decay-time analysis and demonstration that the satellite will meet a disposal timescale or reliably burn up.
- Ground Control & Communications: Access windows alone do not establish communications performance. No link budget, radio-frequency compatibility, antenna constraints or confirmation that the observatory is configured as a spacecraft ground station is provided.
- Orbit: The report does not give payload resolution, swath or viewing geometry to show that the proposed instrument can conduct the required fluid-lensing imaging from the selected orbit.

## Next steps

1. Rework the Orbit section using a consistent set of orbital elements: check the 600 km semi-major axis, use a retrograde inclination of about 97.8° for sun-synchronous precession, and explain how launch timing and orbital-plane geometry set RAAN. Verify the launch-site latitude and distinguish access duration from the number of daily contacts.
2. Build evidence that the mission will work: add payload resolution, swath and viewing geometry; a communications link budget and frequency/antenna compatibility; and a sized drag sail with a disposal-time analysis. Correct the interpretation of the 580.786-second access duration, and include relevant STK project files if available.
3. Revise the Introduction, Conclusion and presentation together: explicitly identify the operator and customer groups, qualify conclusions against the orbit and performance evidence, and check grammar, citation matching and bibliography quality. Replace unsupported or unsuitable references with appropriate sources.

---
<sub>Run Input_2_d-Run_3-Eff_high-261116-112210 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15180/8044 | cost $0.00471 (incl. $0.001387 for the reused reference rubric+task structure) | 57.07s</sub>
