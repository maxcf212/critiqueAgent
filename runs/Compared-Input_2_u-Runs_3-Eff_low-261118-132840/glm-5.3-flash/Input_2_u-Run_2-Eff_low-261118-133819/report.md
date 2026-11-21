# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 90 / 100 (90%)**

An excellent, comprehensive mission design report for ZYZZsat. All task requirements are addressed with hand calculations verified in STK, submitted scenario files, and honest treatment of risks and limitations. Presentation is professional throughout. To reach the very top of the rubric, strengthen the link budget, launch-vehicle risk baseline, and reference precision.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Accomplished (9/10). Your introduction addresses all requirements: primary mission (5 m GBR imaging), rationale, single-spacecraft justification, and operator/customers, all referenced. To reach full marks, add depth on funding arrangements and user agreements with AIMS and customers.

*Assessor reasoning:* All required information addressed: primary mission, rationale (bleaching threat, limitations of existing monitoring), single-spacecraft justification, and operator/customers clearly identified, with literature references throughout. Only minor depth missing on funding/user agreements.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Accomplished (9/10). Your design procedure is strong: launch trade table with azimuth calculation, hand-derived orbit elements verified in STK (e.g. i = 97.79°), manoeuvres, six daily passes, data budget, duration and EOL, all supported by screenshots and Appendix A files. The missing X-band link budget and unverified Mount Pleasant assumption are the main gaps to the top level.

*Assessor reasoning:* Launch site/vehicle justified with trade table and azimuth calculation; orbit elements derived by hand and verified in STK; manoeuvres, ground station, pass frequency, data budget, duration and EOL all covered with screenshots and submitted STK files. Link budget admittedly absent, a minor gap.
> 2.3 Orbit: "cos i = −0.1355, so i = 97.79°" *(quote not found in submission)*  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning"  
> Appendix A: STK files and settings: "ZYZZsat_Mission.sc | Scenario, 3 Feb 2025 00:00:00 to 3 Feb 2030"  

### C3 Conclusion (9/10, Accomplished)

Accomplished (9/10). Your conclusions are detailed and evidence-based, summarising quantitative results and candidly identifying four limitations with next-phase actions (e.g. Vega C flight status, drag-sail disposal). Full marks would follow from tying each limitation to a concrete mitigation plan.

*Assessor reasoning:* Conclusions summarise quantitative results from the report and candidly identify four specific limitations and next-phase actions — detailed and evidence-based, not generic.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown"  
> 3 Conclusion: "a 4 m² drag sail removes the satellite in about two years"  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has a clear structure, executive summary, consistently labelled figures/tables, matching citations and an STK appendix, with precise professional writing. Minor looseness in some references (e.g. [9], [15]) is what keeps this from the very top of the band.

*Assessor reasoning:* Clear logical structure with executive summary, numbered sections, consistently labelled figures/tables, in-text citations matching the bibliography, and an appendix of STK files. Writing is precise and professional. Minor: some references (e.g. [9], [15]) are loosely specified.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite)"  
> 2.3 Orbit: "Figure 2: Inclination required for a sun-synchronous orbit as a function of altitude."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction (Number of spacecraft) |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction (Users) |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit (Table 4) |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit (Manoeuvres) |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit / 2.4 (STK plus hand calculations) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Figures 1–4 and Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Whole report; Bibliography |

## Technical issues

- 2.2 Launch: Vega C had not flown at time of writing; fallback acknowledged, so risk is handled, but baseline depends on an unflown vehicle.
- 2.4 Ground Control & Communications: X-band link budget not performed (e.g. antenna gains, margin); assumption that Mount Pleasant can host S/X-band equipment is unverified.
- 2.5 Mission Duration & EOL: Decay calculation uses a single mean density; solar-cycle variation acknowledged but lifetime estimate is coarse.

## Next steps

1. Add an X-band link budget for Section 2.4 (antenna gains, path loss, data rates, link margin) and verify that Mount Pleasant can actually host the assumed S/X-band ground equipment.
2. Strengthen the launch baseline in Section 2.2 by quantifying schedule risk for the unflown Vega C and comparing at least one flown alternative in your trade table.
3. Refine the Section 2.5 decay analysis by propagating lifetime across solar-cycle density variations rather than a single mean density.
4. Tighten reference specificity (e.g. [9], [15]) so every citation pinpoints the exact source and page/section.

---
<sub>Run Input_2_u-Run_2-Eff_low-261118-133819 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15104/4058 | cost $0.003208 (incl. $0.001387 for the reused reference rubric+task structure) | 38.51s</sub>
