# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 100 / 100 (100%)**

You submitted an outstanding, professional engineering report that met all rubric requirements to the highest standard. Your mission concept, technical justifications, orbital mechanics calculations, and software verification were exceptionally detailed, cohesive, and clearly documented.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 10 / 10 | 10 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 10 / 10 | 60 / 60 |
| C3 Conclusion | Accomplished | 10 / 10 | 10 / 10 |
| C4 Report presentation | Accomplished | 10 / 10 | 20 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (10/10, Accomplished)

You achieved the Accomplished level by clearly establishing the ZYZZsat mission rationale, defining user roles (AIMS and stakeholders), and thoroughly justifying your single-satellite architecture in Section 1. To maintain this high standard, continue supporting user operational requirements with direct quantitative data needs.

*Assessor reasoning:* All required introductory elements are thoroughly addressed. The rationale is clearly established, user roles (operator and end users) are explicitly defined, and the single-spacecraft architecture is well justified.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (60/60, Accomplished)

You reached the Accomplished level through exceptional technical rigour in Section 2. You supported your launch vehicle selection, analytical J2 orbital hand calculations, STK modelling, and passive deorbit drag-sail strategy with clear evidence and verification. For future work, consider modelling stochastic atmospheric drag variations during deorbit.

*Assessor reasoning:* The mission design demonstrates an exceptional standard of technical rigour. Launch vehicle and site selection, orbit determination (verified via J2 hand calculations and STK), ground communications access analysis, data budgeting, and end-of-life decay mechanics are comprehensively covered and supported by clear figures and data tables.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "cos i = −(1.991 × 10⁻⁷) / (1.5 × 1.0826 × 10⁻³ × 0.8354 × 1.0831 × 10⁻³) = −0.1355, so i = 97.79°"  
> 2.5 Mission Duration & EOL: "The EOL plan is therefore passive: a drag sail is deployed at the end of the mission."  

### C3 Conclusion (10/10, Accomplished)

You achieved Accomplished in Section 3 by providing a concise synthesis of mission objectives alongside an honest, critical appraisal of key design limitations (such as Vega C flight heritage). To build on this, include high-level cost or schedule risk mitigations in future work.

*Assessor reasoning:* The conclusion provides an excellent, nuanced synthesis of the mission outcomes alongside a critical appraisal of technical limitations and concrete pathways for future work.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown, so the Falcon 9 rideshare service is kept as a fallback"  

### C4 Report presentation (20/20, Accomplished)

Your presentation reached the Accomplished level through a clear engineering layout, a concise executive summary, consistent tabular and graphical presentation, immaculate referencing, and complete STK model documentation in Appendix A. Continue using this professional formatting standard for future engineering deliverables.

*Assessor reasoning:* The presentation is exemplary. It contains a well-structured executive summary, clear figure/table labelling, immaculate IEEE-style citation formatting, and detailed documentation of software models in the appendix.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite"  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

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

## Next steps

1. Consider conducting sensitivity analyses on drag-sail deployment reliability to further robustify your end-of-life plan.
2. Develop the secondary payload or Falcon 9 fallback operational profile to mitigate primary launch vehicle uncertainty.
3. Explore multi-ground-station networks to evaluate whether downlink latency could be reduced during peak reef-monitoring seasons.

---
<sub>Run Input_2_u-Run_3-Eff_low-261118-134018 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18904/3763 | cost $0.011409 (incl. $0.001387 for the reused reference rubric+task structure) | 23.97s</sub>
