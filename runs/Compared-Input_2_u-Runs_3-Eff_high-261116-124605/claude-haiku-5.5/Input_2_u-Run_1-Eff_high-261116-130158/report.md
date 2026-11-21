# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 82 / 100 (82%)**

You have produced a strong, well-structured mission design for ZYZZsat. Your introduction answers the required questions clearly, and your orbit, launch and drag work is well supported by STK and hand calculations. Your conclusions are specific and tied to the evidence. The main improvements are numerical consistency: the contact-time fraction, the eclipse duration, the daily imaging area against the 45-day mosaic, and the unclosed X-band link budget. Some claims also need citations and a more formal tone.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You answer all four required questions clearly. The mission need is built from the limits of current bleaching monitoring, you justify using a single satellite, and you name AIMS as operator and identify the customers. References [1]-[6] support the rationale. To strengthen it further, cite the claims about human reliance on reefs and government funding, and use a more formal tone in places.

*Assessor reasoning:* All four required questions are answered with justification: mission need is built from the limits of existing bleaching monitoring, single-satellite choice is argued, and operator and customers are named. References [1]-[6] support the rationale. Minor gaps: some claims are uncited (reliance of humans on reefs, government funding), and the tone is informal in places.
> 1 Introduction, Primary mission: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction, Number of spacecraft: "One satellite is therefore used."  
> 1 Introduction, Users: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Your launch azimuth, J2 inclination, pass statistics, drag decay and data budget are largely verified and well supported by STK. Some key figures need correcting. 510 s of a 771 s pass is about 66 percent, not 60 percent, which changes the daily contact time and downlink margin. The 34-minute eclipse does not fit an 08:45 node, and the daily imaging area in Table 6 conflicts with the 45-day mosaic. Close the X-band link budget to support the downlink conclusion.

*Assessor reasoning:* Strong, largely verified calculations: launch azimuth, J2 inclination, 771 s maximum pass, access statistics, drag decay and data budget all check out. Accuracy is reduced by errors and inconsistencies: 510 s of 771 s is about 66 percent, not 60; the 34-minute eclipse looks high for an 08:45 node; the 60,000 km² daily area conflicts with the 45-day mosaic; the link budget is unclosed.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit, Inclination: "This agrees with the STK value of 97.7924°."  
> 2.4 Ground Control & Communications: "so about 60 percent of the contact time, or 34 minutes per day, is counted."  
> 2.3 Orbit: "it is in the Earth's shadow for about 34 minutes of each orbit"  
> Table 6 (2.4): "One strip over the reef: 60 km × 1,000 km"  
> 2.3 Orbit, Table 3: "A complete map of the reef directly from overhead takes about 45 days."  
> 2.4 Ground Control & Communications: "A full link budget for the X-band downlink has not been calculated in this report"  
> 2.5 Mission Duration & EOL: "Without the sail the satellite would stay in orbit for about 32 years"  

### C3 Conclusion (9/10, Accomplished)

Your conclusions are specific and tied to the evidence, restating revisit times, pass statistics, downlink margin and decay lifetime with numbers. Identifying four limitations with their consequences and next steps is a clear strength. To make the conclusion fully robust, ensure the figures it restates match the corrected values in Sections 2.3 and 2.4, and cite the claim that reef managers prefer weekly coverage.

*Assessor reasoning:* Conclusions are specific and tied to the evidence: revisit times, pass statistics, downlink margin and decay lifetime are restated with numbers. Four named limitations are identified with consequences and next steps. Minor weakness: the claim that managers prefer weekly coverage is uncited.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "the 45-day complete map is slower than the weekly coverage that reef managers would prefer"  

### C4 Report presentation (16/20, Accomplished)

Your report has a clear structure, an executive summary, numbered and captioned tables and figures, and consistent IEEE-style references. To improve polish, remove informal phrasing and make the downlink margin consistent between the Executive Summary (about three times) and Section 2.4 (3.5). Also check the facility file extension in Table A1, since STK normally uses .fac.

*Assessor reasoning:* Clear report structure with executive summary, numbered sections, numbered and captioned tables and figures, and consistent IEEE-style references. Weaknesses: informal phrasing in places, some uncited claims, and a downlink margin given as about three times in the summary but 3.5 in Section 2.4.
> Executive Summary: "The design is supported by STK simulations and by hand calculations of the orbit, coverage, data budget and orbital decay."  
> 1 Introduction: "but this is not even the full extent of their nurture"  
> 2.3 Orbit, Figure 2: "Figure 2: Inclination required for a sun-synchronous orbit as a function of altitude."  
> Executive Summary: "this gives about three times the downlink capacity the imaging plan needs"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction, Primary mission |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction, Number of spacecraft; Table 1 |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction, Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit, Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications, Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit, 2.4, Appendix A (STK 11) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Figures 1, 3, 4; Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography; body text |

## Technical issues

- 2.4 Ground Control & Communications: 510 s of 771 s is about 66 percent of a pass, not 60 percent. Using 66 percent gives about 38 min/day, changing the 34-min figure and the downlink margin.
- 2.3 Orbit (eclipse statement) and Table 1: A 34-minute eclipse implies a beta angle near 10 degrees. An 08:45 node time gives roughly 28 min by estimate (beta about 49 degrees). Verify in STK or correct the figure.
- Table 6 vs Table 3 and 1 Introduction: One 60 km x 1,000 km strip per day gives about 6 days to image the 344,400 km2 reef, conflicting with the 45-day nadir mosaic and the reef-coverage narrative. The daily imaging assumption is not reconciled with track geometry.
- 2.5 Mission Duration & EOL, Table 7: Lifetime is estimated as scale height divided by a constant decay rate using one density, which is crude. Decay rates change strongly with altitude, so the 32-year and 2.2-year figures need numerical propagation or a caveat.
- 2.4 Ground Control & Communications, Table 6: The 50 Mbit/s X-band downlink margin is presented as adequate without a link budget. This is acknowledged but weakens the conclusion.
- Appendix A, Table A1: The facility file extension is given as .f; STK facility files normally use .fac. Check that the submitted files open in STK.

## Next steps

1. Correct the contact-time fraction (510 s of 771 s is about 66 percent, not 60 percent) and recalculate the daily contact time and downlink margin in Section 2.4 and the Executive Summary.
2. Verify the eclipse duration in STK or correct the beta-angle statement, and reconcile the daily imaging area in Table 6 with the 45-day mosaic in Table 3.
3. Close the X-band link budget, check the 32-year lifetime with numerical propagation, cite the uncited claims, and confirm that the Appendix A facility files open in STK.

---
<sub>Run Input_2_u-Run_1-Eff_high-261116-130158 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21489/27413 | cost $0.015909 (incl. $0.001387 for the reused reference rubric+task structure) | 121.68s</sub>
