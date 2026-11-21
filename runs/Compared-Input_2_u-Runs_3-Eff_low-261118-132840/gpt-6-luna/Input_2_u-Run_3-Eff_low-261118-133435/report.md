# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 81 / 100 (81%)**

You present a strong, well-structured preliminary design for an Australian reef-monitoring mission. Your clear rationale, orbit and access analysis, and useful STK imagery support the report. To make the design more convincing, distinguish demonstrated performance from estimates and validate key communications and coverage claims with operational constraints and reproducible evidence.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Section 1 clearly explains the mission need, Australian benefit, single-spacecraft choice, operator and customers, with supporting citations. To strengthen the rationale further, qualify whether 5 m multispectral imagery can reliably identify bleaching.

*Assessor reasoning:* Clearly explains the mission need and rationale, specifies a single spacecraft and why it is sufficient, and identifies the operator and several customers. The environmental context and intended public benefit are well described and supported with citations. A little more qualification of whether 5 m multispectral imagery can reliably identify bleaching would strengthen the case.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  
> 1 Introduction: "The customers are the Great Barrier Reef Marine Park Authority"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Sections 2.2–2.5 cover launch, orbit, manoeuvres, ground contacts, mission duration and EOL, supported by calculations and STK imagery. For stronger validation, add the Section 2.4 link budget, test Section 2.3 coverage under operational constraints, and provide verifiable STK files in Appendix A.

*Assessor reasoning:* The design covers launch selection and fallback, orbit elements and J2 sun-synchronous calculation, manoeuvres, STK access analysis, contact frequency, data budget, mission duration and disposal. Screenshots and hand calculations provide useful evidence. The analysis is substantial but not fully validated: the assumed 50 Mbit/s link lacks a link budget, imager performance and operational constraints are lightly treated, and the one-station operations case is an assumption.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "The orbit is circular, so it has no perigee"  
> 2.3 Orbit: "No orbital manoeuvres are required."  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  
> 2.5 Mission Duration & EOL: "The mission lasts five years."  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

### C3 Conclusion (8/10, Accomplished)

Section 3 draws specific conclusions and acknowledges important limitations. Make the distinction between demonstrated results and preliminary estimates even clearer, particularly for coverage and communications performance.

*Assessor reasoning:* The conclusion draws specific findings from the design and openly identifies consequential limitations, including launch uncertainty, unproven fluid-lensing benefit, missing link budget and revisit limitations. It could more explicitly distinguish demonstrated performance from preliminary estimates, but it is appropriately evidence-based.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps"  

### C4 Report presentation (16/20, Accomplished)

The executive summary, contents, numbered sections, labelled tables and figures, and bibliography make the report easy to navigate. For a more polished engineering report, clarify assumptions and validation alongside dense calculations and tables, and improve incomplete or less authoritative source entries.

*Assessor reasoning:* The report has a logical structure, executive summary, numbered sections, labelled tables and figures, and generally clear professional writing. References are cited throughout and a bibliography is provided. Some source entries are incomplete or less authoritative than ideal, and the many dense calculations and tables could be more consistently supported with assumptions and validation. The STK appendix lists files, but their contents cannot be assessed from the report text alone.
> Executive Summary: "This report presents the design of ZYZZsat"  
> Contents: "3 Conclusion"  
> 2.4 Ground Control & Communications: "Table 5: STK access report, ZYZZsat to Mount Pleasant Radio Observatory (elevation above 0°)."  
> Bibliography: "[11] D. A. Vallado, Fundamentals of Astrodynamics and Applications"  

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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents |

## Technical issues

- 2.4 Ground Control & Communications: The proposed 50 Mbit/s X-band downlink is not substantiated by a link budget. The report acknowledges this; therefore the claimed daily capacity and margin are preliminary rather than demonstrated.
- 2.3 Orbit: The five-day reach estimate divides equatorial ground-track spacing by the maximum roll-reach width. This is an idealized geometric estimate; it does not establish actual five-day coverage of every reef location once imaging geometry, pointing limits, sunlight, clouds and acquisition scheduling are considered.
- Appendix A: STK files and settings: The report says the STK files are submitted in a ZIP, but the files themselves are not present in the supplied submission text, so their completeness and reproducibility cannot be verified.

## Next steps

1. In Section 2.4, add a complete X-band link budget for the proposed 50 Mbit/s downlink, including assumptions, link margin and resulting data capacity; label current capacity estimates as preliminary until verified.
2. In Section 2.3, test the five-day coverage estimate against imaging geometry, pointing limits, sunlight, cloud effects and acquisition scheduling, and report what coverage is achievable under those constraints.
3. In Appendix A, ensure the referenced STK ZIP is included and reproducible, with the relevant files and settings; strengthen the report’s evidence by explaining how the analysis supports its performance claims.

---
<sub>Run Input_2_u-Run_3-Eff_low-261118-133435 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15018/4570 | cost $0.002964 (incl. $0.001387 for the reused reference rubric+task structure) | 34.55s</sub>
