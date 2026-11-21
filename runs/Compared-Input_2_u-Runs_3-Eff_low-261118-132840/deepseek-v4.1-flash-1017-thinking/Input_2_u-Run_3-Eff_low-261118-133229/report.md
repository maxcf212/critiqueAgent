# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 90 / 100 (90%)**

Your ZYZZsat report is a strong, well-evidenced design that addresses every required element. You justify the single-spacecraft concept, launch and orbit choices, ground segment, duration and EOL with STK evidence and hand calculations. To reach the top of Accomplished, close the X-band link-budget gap, tighten pass-duration assumptions, and address Vega C/Falcon 9 trajectory sensitivity.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You address all introduction requirements in §1: mission need, single-spacecraft rationale, AIMS as operator and customers, and Australian benefits. Referencing is strong and the rationale persuasive. To reach 10/10, evidence customer uses more directly rather than asserting them, and make the link from mission need to design requirements explicit.

*Assessor reasoning:* All required introduction elements are addressed in detail: mission need, single-spacecraft rationale, operator/customers, and benefits to Australia. Referencing is strong and mission rationale is persuasive. Minor room remains because some customer uses are asserted rather than fully evidenced.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Your §2.2–2.5 and Appendix A cover launch, orbit, manoeuvres, ground station, communications, duration and EOL with STK screenshots, trade tables and hand calculations. To reach 10/10, add the missing X-band link budget in §2.4, justify the 50 Mbit/s and usable-contact assumptions, and address Vega C schedule risk and Falcon 9 fallback coverage sensitivity in §2.2.

*Assessor reasoning:* Launch, orbit, manoeuvres, ground station, communications, duration and EOL are all covered with STK evidence, hand calculations and trade tables. Technical work is largely correct and well justified. Minor gaps are the absent X-band link budget and reliance on an unflown Vega C, both acknowledged.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "No orbital manoeuvres are required."  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  

### C3 Conclusion (9/10, Accomplished)

Your §3 conclusions are specific and tied to quantitative results, including four limitations. To reach 10/10, frame those limitations explicitly as design risks with likelihood/impact and mitigation, and state which next steps would retire each risk.

*Assessor reasoning:* Conclusions are specific, tied to quantitative results, and include limitations and next steps. They are not generic. Slight deduction because some limitations could be framed more explicitly as design risks.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "The design has four limitations."  

### C4 Report presentation (18/20, Accomplished)

Your report is clearly structured and readable; the Executive Summary is concise, Figure 1 is labelled, and citations match the bibliography. To reach 10/10, tighten long tables and clarify summary-node-time wording, and ensure every figure/table is referenced in text before it appears.

*Assessor reasoning:* Report is clearly structured, readable, and professionally presented. Executive summary is concise; figures and tables are labelled; citations match the bibliography. Minor presentation imperfections remain, such as some long tables and summary-node-time wording, but they do not impede reading.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite"  
> Figure 1: "Figure 1: STK 3D view of the ZYZZsat orbit at two times 12 hours apart"  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit and Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents; Bibliography |

## Technical issues

- 2.4 Ground Control & Communications: No full X-band link budget is calculated; 50 Mbit/s downlink and usable contact time are assumed, and Mount Pleasant must be fitted with S/X-band equipment.
- Executive Summary / 2.4: The quoted 9.7 min mean pass is horizon-to-horizon including low-elevation contact; usable contact is shorter, though the data budget later uses a discounted 34 min/day.
- 2.2 Launch: Baseline depends on Vega C, which the report states has not yet flown; the Falcon 9 fallback is sensible, but a different rideshare altitude requires the SSO inclination and coverage analysis to be redone.

## Next steps

1. In §2.4, add a full X-band link budget (EIRP, G/T, path loss, modulation/coding, margin) to support the 50 Mbit/s downlink and assumed usable contact time; state Mount Pleasant S/X-band fit-out as a requirement or trade.
2. Reconcile the 9.7 min mean pass in the Executive Summary/§2.4 with usable contact: define the elevation mask and show how the 34 min/day data budget follows; update the relevant figure or table.
3. In §2.2, treat Vega C availability as a schedule risk and quantify the Falcon 9 fallback: redo the SSO inclination and coverage analysis for the different rideshare altitude, or justify why coverage is insensitive.

---
<sub>Run Input_2_u-Run_3-Eff_low-261118-133229 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14105/11069 | cost $0.006865 (incl. $0.001387 for the reused reference rubric+task structure) | 48.09s</sub>
