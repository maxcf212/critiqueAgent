# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 100 / 100 (100%)**

You have produced an outstanding, professionally presented mission design for ZYZZsat. Your technical analyses, hand calculations, and STK integrations are rigorous, and your clear justification of mission requirements and critical evaluation of design constraints demonstrate exemplary engineering maturity. Excellent work across all report sections.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 10 / 10 | 10 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 10 / 10 | 60 / 60 |
| C3 Conclusion | Accomplished | 10 / 10 | 10 / 10 |
| C4 Report presentation | Accomplished | 10 / 10 | 20 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (10/10, Accomplished)

You did an excellent job in Section 1 establishing the operational need for monitoring Great Barrier Reef coral bleaching. You clearly justified the single-satellite architecture over constellations and accurately mapped Australian end-users with strong literature backing. To maintain this Accomplished standard, continue integrating specific stakeholder operational requirements directly into your mission objectives.

*Assessor reasoning:* The introduction excellently details the mission concept and rationale, addressing Australian coral reef monitoring needs. The choice of a single satellite is clearly justified against constellation alternatives, and specific Australian operators and end-users are identified with literature citations.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (60/60, Accomplished)

Your mission design in Section 2 is comprehensive, featuring exceptional alignment between your analytical orbital calculations and STK simulations. To refine your calculations to professional fidelity, adjust the launch azimuth equation in Section 2.2 to account for Earth's tangential surface velocity, which differentiates the inertial trajectory from the vehicle's actual burnout heading.

*Assessor reasoning:* Mission design is exemplary. Launch vehicle trades, sun-synchronous orbital mechanics, lack of manoeuvres, ground access via Mount Pleasant, data budgeting, and passive drag-sail de-orbiting are thoroughly analysed. Hand calculations perfectly align with STK outputs and software files are clearly documented.
> 2.3 Orbit: "With J2 = 1.0826 × 10⁻³, R = 6,378 km, a = 6,978 km and mean motion n = √(μ/a³) = 1.0831 × 10⁻³ rad/s:"  

### C3 Conclusion (10/10, Accomplished)

In Section 3, you provided a mature synthesis of mission outcomes and effectively identified four genuine technical limitations, including launcher readiness and revisit intervals. To sustain this top-tier Accomplished level, ensure future work recommendations outline concrete engineering mitigation pathways and verification milestones for each identified limitation.

*Assessor reasoning:* The conclusion synthesises all primary findings effectively and demonstrates high critical maturity by identifying four genuine engineering limitations (launcher readiness, optical technology readiness, ground station modifications, and nadir repeat cycle) alongside future work.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  

### C4 Report presentation (20/20, Accomplished)

Your presentation was flawless throughout, featuring a concise Executive Summary, cleanly formatted tables, and well-integrated STK figures. Your consistent report structure and accurate IEEE referencing make the document easy to follow. To maintain this standard, continue ensuring all technical figures and tables are explicitly discussed in the main narrative.

*Assessor reasoning:* The submission follows a flawless engineering report structure. The executive summary is thorough and concise, tables and STK figures are cleanly integrated and captioned, grammar is professional, and IEEE citations are accurately matched.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite for monitoring coral bleaching"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Bibliography |

## Technical issues

- 2.2 Launch: The launch azimuth formula sin(beta) = cos(i)/cos(phi) determines the inertial velocity azimuth; computing the vehicle's actual burnout heading requires correcting for the Earth's tangential surface velocity.

## Next steps

1. In Section 2.2, refine the launch azimuth analysis by correcting the inertial azimuth for Earth's tangential surface velocity to determine the vehicle's true burnout heading.
2. Develop the technology readiness level (TRL) discussions in Section 3 into a concrete risk-mitigation timeline for the optical payload and launch options.
3. Carry forward this exemplary practice of dual-verifying numerical derivations against software simulations in your future aerospace engineering projects.

---
<sub>Run Input_2_u-Run_3-Eff_high-261116-131321 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18804/9882 | cost $0.034281 (incl. $0.001387 for the reused reference rubric+task structure) | 51.46s</sub>
