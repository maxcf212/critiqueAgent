# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 84 / 100 (84%)**

You present a strong, well-structured preliminary mission design, with a clear rationale, substantial orbital analysis, useful STK evidence and a conclusion that acknowledges limitations. To make the performance claims more persuasive, validate the downlink, regional coverage and 5 m imaging capability with complete engineering analyses rather than simplified estimates.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Your Introduction clearly identifies the bleaching-imaging mission, its need, the single-spacecraft approach, AIMS as operator and the Great Barrier Reef Marine Park Authority as a customer. Specific detail and citations support an accomplished response. To strengthen it further, qualify benefit claims carefully and connect them to evidence.

*Assessor reasoning:* Clearly explains the mission need, direct bleaching detection, single-spacecraft choice, operator, customers and public-service rationale. The discussion is specific and supported with citations; a few claims about the mission’s benefits could be more carefully qualified.
> Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> Introduction: "One satellite is therefore used."  
> Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  
> Introduction: "The customers are the Great Barrier Reef Marine Park Authority"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Sections 2.2–2.5 address launch choice, orbit and manoeuvres, ground access, mission duration and EOL. STK outputs and Appendix A provide useful design evidence. To strengthen this accomplished design, validate the 50 Mbit/s downlink, regional coverage estimates and 5 m imaging performance with complete engineering analyses.

*Assessor reasoning:* A thorough preliminary design covers launch selection, orbital elements and calculations, manoeuvres, access opportunities, data volume, mission duration and disposal. STK figures, access outputs and an appendix listing software files provide useful evidence. The missing X-band link budget and approximate, not regionally validated, coverage estimates limit confidence in key performance claims.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "The orbit is circular, so it has no perigee and two of the six classical orbital elements, the argument of perigee and the true anomaly, are undefined."  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  
> 2.5 Mission Duration & EOL: "The mission lasts five years."  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  
> Image 1  

### C3 Conclusion (9/10, Accomplished)

Your Conclusion draws specific findings from the design and identifies four limitations, giving readers a suitably qualified takeaway. Keep this evidence-led approach, and update the conclusions as you validate the link budget, coverage and imaging-performance estimates.

*Assessor reasoning:* The conclusion draws specific results from the design and openly identifies four material limitations, including launch availability, imaging assumptions, ground-station upgrades and revisit performance. It reaches an appropriate, qualified conclusion rather than merely restating the mission concept.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps that current temperature-based monitoring cannot."  

### C4 Report presentation (18/20, Accomplished)

The report has a logical engineering structure, concise Executive Summary, readable prose, labelled figures and tables, and in-text citations with a substantial bibliography. To make the presentation even more professional, refine minor stylistic awkwardness and complete bibliographic details consistently.

*Assessor reasoning:* The report has a logical engineering structure, concise executive summary, readable prose, labelled figures and tables, and a substantial bibliography with in-text citations. Minor stylistic awkwardness and some incomplete bibliographic detail remain, but do not materially impede reading.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite)"  
> Contents: "2 Mission Design"  
> 2.4 Ground Control & Communications: "Table 5: STK access report, ZYZZsat to Mount Pleasant Radio Observatory (elevation above 0°)."  
> Bibliography: "[11] D. A. Vallado, Fundamentals of Astrodynamics and Applications, 4th ed."  

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
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents |

## Technical issues

- 2.4 Ground Control & Communications: The 50 Mbit/s downlink capacity is assumed rather than demonstrated: the report explicitly omits a full X-band link budget, so link margin, antenna gain, power and achievable rate are unverified.
- 2.3 Orbit: The approximately five-day access and 45-day complete-mosaic estimates derive from simplified, uniform equatorial track spacing and pointing geometry. They do not demonstrate actual Great Barrier Reef coverage or account for off-nadir image-quality effects, so these should be treated as preliminary estimates.
- 2.1 Spacecraft overview: The 0.10 m aperture is justified by a diffraction-limit calculation alone. Detector sampling, optical performance, signal-to-noise and atmospheric effects are not assessed, so the stated 5 m imaging performance is not yet established.

## Next steps

1. Complete an X-band link budget in Section 2.4, documenting antenna gains, transmit power, link margin and assumptions to demonstrate whether the 50 Mbit/s rate is achievable.
2. In Section 2.3, model coverage of the actual Great Barrier Reef area and account for off-nadir image quality; report validated coverage, revisit and mosaic-completion estimates.
3. In Section 2.1, support the 5 m imaging claim with detector sampling, optical performance, signal-to-noise and atmospheric analysis, then carry the validated performance and remaining caveats into your conclusion.

---
<sub>Run Input_2_u-Run_2-Eff_high-261116-125638 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 14986/9054 | cost $0.005201 (incl. $0.001387 for the reused reference rubric+task structure) | 185.18s</sub>
