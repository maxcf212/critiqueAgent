# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You present a relevant Australian reef-monitoring concept, explain why one spacecraft could serve the mission, and support the design with useful STK imagery and access data. To move the overall work forward, strengthen technical evidence for launch, orbit, communications and end-of-life choices, then draw more specific conclusions and polish referencing and presentation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction explains the reef-monitoring purpose, environmental rationale and choice of one spacecraft, and identifies potential agency users. To strengthen this accomplished work, distinguish the spacecraft operator from customer/user agencies and specify their roles and needs.

*Assessor reasoning:* The report explains the reef-monitoring mission, its environmental rationale, and why one spacecraft is considered sufficient. It identifies likely agency users and public funding, but does not clearly distinguish the spacecraft operator from its customers or provide detailed user roles.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Launch, Orbit, Ground Control & Communications, and Mission Duration & EOL sections, supported by STK imagery and access data, cover many design elements. For the accomplished level, substantiate launcher and injection feasibility, correct the RAAN and access rationale, document manoeuvres, and quantify communications and disposal; include relevant software files.

*Assessor reasoning:* The report includes substantial STK-derived orbit and access material, orbital elements, a selected launch site and vehicle, ground facility, mission duration, and a disposal concept. However, the launch plan remains speculative, the maneuver and EOL discussion is not fully engineered, and some orbit/ground-access reasoning is inaccurate. Screenshots are supplied, but no relevant software files are included.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the main design choices and acknowledges uncertainty about the launcher. To reach the accomplished level, draw explicit conclusions from your analyses, explain what the access and orbit results mean for mission performance, and identify how unresolved feasibility and disposal issues affect confidence in the design.

*Assessor reasoning:* The conclusion summarizes the principal design choices and acknowledges uncertainty about the proposed launcher. It is relevant but largely recaps the report and does not draw detailed conclusions from the analysis or address its limitations.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognizable structure, executive summary, figures, tables and bibliography. For the accomplished level, make figure and table presentation consistent, correct grammar and wording, and ensure citations are complete and consistent; replace the Wikipedia entry with appropriate authoritative sources.

*Assessor reasoning:* The report has a recognizable structure, executive summary, figures, tables, and bibliography. However, figure/table presentation and labelling are inconsistent, references are incomplete and include Wikipedia despite the task excluding it, and prose contains noticeable grammar and wording errors. These issues reduce the report's professional polish.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: The report names Vega E for a 2025 launch even though it states Vega E's first launch is planned for 2024; the schedule and launcher availability are speculative. It does not establish a committed rideshare or demonstrate that a compatible 600 km SSO injection is available.
- Orbit: The RAAN value is not determined by the launch facility's location. Launch latitude constrains achievable inclination, while RAAN at injection depends on launch time and the desired orbital plane.
- Orbit: A circular orbit has undefined argument of perigee and true anomaly, but the argument of latitude is not an independent classical element that resolves both generally; specifying argument of latitude is sufficient for the spacecraft's position in this circular orbit, with epoch and RAAN convention still needed for a reproducible state.
- Ground Control & Communications: The claim that access frequency is maximized by a ground station close to the poles is not generally valid for a single station; access depends on station latitude, orbit geometry, elevation mask, and the ground track. The reported passes are not reconciled with the claim of near-constant contact.
- Ground Control & Communications: A polar/near-polar orbit does not maintain significant contact for the vast majority of passes at a station; contact duration depends on elevation limits and geometry. The report gives durations but no elevation mask or link-budget/data-volume demonstration.
- Mission Duration & EOL: A drag sail is a plausible passive disposal concept at 600 km, but no sail area, spacecraft mass, predicted decay time, or compliance analysis is provided. The discussion also describes an uncontrolled descent as an option without establishing its acceptability under applicable debris-mitigation guidance.
- Bibliography: Wikipedia is used as a source despite the task explicitly stating that Wikipedia is not acceptable; most entries also lack complete bibliographic details and access dates.

## Next steps

1. Make the launch plan verifiable: support Vega E availability and a compatible 600 km sun-synchronous injection with evidence, or assess a feasible alternative and explain any required manoeuvres.
2. Make the orbit and communications reproducible: clarify the orbital elements and epoch, distinguish RAAN from launch latitude, and support access claims with station geometry, elevation mask and link/data-volume analysis.
3. Engineer and document disposal, including drag-sail area, spacecraft mass, predicted decay time and applicable debris guidance; replace Wikipedia with complete authoritative references and use your findings to develop specific conclusions.

---
<sub>Run Input_2-Run_2-Eff_low-261118-113324 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15183/4144 | cost $0.002754 (incl. $0.001387 for the reused reference rubric+task structure) | 27.04s</sub>
