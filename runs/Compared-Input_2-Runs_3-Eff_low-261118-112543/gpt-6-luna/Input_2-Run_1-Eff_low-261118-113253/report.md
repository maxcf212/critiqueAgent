# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You present a relevant Australian reef-monitoring concept, explain why one spacecraft is proposed, and use STK screenshots and access analysis to develop the design. To strengthen the report, substantiate the imaging and communications claims, verify the launch and end-of-life plans, and draw more evidence-based conclusions. Clearer figure presentation and complete, consistent references will also improve the report’s professionalism.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction explains the reef-monitoring purpose, Australian relevance and rationale for one spacecraft, and identifies likely science and government users. To strengthen this, distinguish the spacecraft operator from customers and support the specific mission need and user roles with stronger references.

*Assessor reasoning:* The report explains the reef-monitoring mission and its public and scientific rationale, justifies using one spacecraft, and identifies likely users and funding sources. The concept is relevant to Australia and reasonably detailed. However, the operator is not clearly distinguished from customers, and mission need and user roles would benefit from stronger specificity and better-supported references.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Orbit and Ground Control & Communications sections use STK screenshots and access analysis to present a preliminary design. For the next level, demonstrate feasibility: verify the speculative Vega E choice, fully define the orbital state, quantify imaging performance and communications assumptions, provide STK files, and calculate whether the drag sail achieves safe disposal.

*Assessor reasoning:* The report presents STK-derived orbit views and access results, orbit elements, a launch option, a ground facility, mission duration, and an EOL concept. Important design aspects remain weak or inaccurate: the launch choice is speculative, no STK project files are provided, imaging coverage and resolution are not quantified, and the proposed passive drag-sail deorbit is not analysed. Some operational claims are inconsistent with SSO geometry.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the proposed launch, orbit and ground station. To reach the next level, draw specific conclusions from your analyses and address key uncertainties, including imaging capability, contact assumptions and end-of-life feasibility.

*Assessor reasoning:* The conclusion summarizes the selected launch, orbit, and ground station and acknowledges uncertainty around Vega E. It is relevant but mostly recaps the proposal rather than drawing detailed conclusions from the analysis; it also does not address important limitations such as imaging performance, contact assumptions, or EOL feasibility.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognizable structure, executive summary, figures, tables and bibliography. For the next level, use consistent figure and table numbering and captions, edit grammatical errors, and provide complete, consistently formatted references that correspond to in-text citations.

*Assessor reasoning:* The report has a recognizable structure, executive summary, figures, tables, and bibliography. However, several figures and tables lack consistent numbering and captions; the writing contains grammatical and editing errors; and references are incomplete and inconsistently formatted. It cites Wikipedia despite the task explicitly disallowing it, and the bibliography does not provide proper bibliographic details.
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

- Orbit: A sun-synchronous orbit does not provide a constant supply of sunlight to the spacecraft; it experiences eclipses depending on orbital geometry and season.
- Ground Control & Communications: The claim that the selected Tasmanian station provides near-polar access frequency is overstated. At about 42°S it is not close to a pole, and access frequency depends on station latitude, orbit geometry, antenna elevation mask, and the analysed time span.
- Ground Control & Communications: The claim that imaging occurs on the descending part because it is constantly in sunlight is not generally valid. SSO local solar time and ascending/descending illumination must be specified; either branch may be sunlit depending on the orbit.
- Orbit: The orbital-element table does not fully define the initial spacecraft state: for a circular orbit, argument of perigee and true anomaly are undefined, but argument of latitude alone is insufficient without a reference epoch and the remaining element values such as RAAN and inclination.
- Launch: The report presents Vega E as the selected launch vehicle despite describing it as not yet built, and does not establish that its payload interface, launch date, injection orbit, or rideshare availability suit this mission.
- Mission Duration & EOL: A drag sail can increase atmospheric drag but does not itself guarantee a safe disposal time or complete demise. The report gives no sail area, spacecraft ballistic coefficient, decay-time estimate, or assessment against applicable debris-mitigation limits.
- Orbit: The stated 250 km reef width and 600 km altitude are not connected to sensor swath, ground sampling distance, or revisit/coverage calculations, so the claimed imaging capability is unsubstantiated.

## Next steps

1. In Orbit, define the spacecraft’s initial state with a reference epoch and complete orbital elements; clarify SSO illumination and quantify sensor swath, ground resolution and coverage for the reef-monitoring task.
2. In Launch, verify that the selected vehicle, interface, schedule and injection orbit are feasible. In Ground Control & Communications, support access and contact claims with the station geometry, elevation mask and analysis period; include the STK project files.
3. In Mission Duration & EOL, calculate drag-sail decay time and assess disposal against applicable limits. In Conclusion, use these results and limitations to reach specific findings; improve figure numbering and captions, and provide complete, consistent references.

---
<sub>Run Input_2-Run_1-Eff_low-261118-113253 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15249/4652 | cost $0.004231 (incl. $0.001387 for the reused reference rubric+task structure) | 31.29s</sub>
