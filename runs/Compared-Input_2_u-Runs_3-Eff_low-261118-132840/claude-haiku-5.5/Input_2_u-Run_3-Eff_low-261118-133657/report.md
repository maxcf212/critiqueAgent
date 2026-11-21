# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 73 / 100 (73%)**

You have produced a thorough, well-supported preliminary design that addresses every requirement. Your introduction clearly sets out the mission, the single-spacecraft rationale, and the operator and users. The main design is backed by hand calculations and STK evidence, and the report is well structured. The main areas to strengthen are numerical consistency in the downlink and eclipse analysis, one mismatched citation, and a few unsupported design statements.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 7 / 10 | 14 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Your introduction is a strong, well-argued section. It states the primary mission, the reason for it, the single-spacecraft choice, and the operator and customers, with supporting context and references. To reach the top band consistently, cite a source for the claims in the rationale and give the users section more referenced support rather than assertion.

*Assessor reasoning:* Covers mission, rationale, single-spacecraft justification, operator and customers with supporting context and references. Rationale is well argued. Minor gaps: some claims in the rationale lack citation, and the user section is largely asserted rather than referenced.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

Your main design is comprehensive, and your hand calculations for inclination, decay and imaging geometry, together with the STK support, are strong. Accuracy is the main limit: the pass durations and percentages in the communications section, the eclipse timing against the crossing time, and the one-strip daily data volume need to be reconciled. Fixing these would move this section to the top band.

*Assessor reasoning:* Thorough design with strong hand calculations (inclination, decay, imaging geometry) and STK support. Technical errors reduce accuracy: six passes at 510 s give about 51 min, not 34 min, and 510/771 is about 66%, not 60%. A 34-minute eclipse is inconsistent with an 08:45 crossing time. The data budget also assumes one 1000 km strip per day without justification.
> 2.4 Ground Control & Communications: "Daily data budget table: 50 Mbit/s × 2,000 s (34 minutes)" *(quote not found in submission)*  
> 2.4 Ground Control & Communications: "the part of an overhead pass above 10° is 510 s of 771 s"  
> 2.3 Orbit: "with this node time it is in the Earth's shadow for about 34 minutes of each orbit"  

### C3 Conclusion (8/10, Accomplished)

Your conclusions are specific and tied to your quantitative results. You list four limitations with clear next steps, which is a good approach. Some restated figures, such as the 3.5× margin, depend on the downlink numbers in Section 2.4, so correcting those will also make the conclusions fully consistent.

*Assessor reasoning:* Conclusions are specific, tied to the quantitative results and lucidly list four limitations with next steps. Some figures restated (for example 3.5× margin) inherit the earlier downlink inconsistency.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "a second satellite in the same orbit plane would halve it"  

### C4 Report presentation (14/20, Accomplished)

The report is well structured, with an executive summary, labelled tables and figures, and an appendix of STK files. Citation [13] does not support the Mount Pleasant claims it is attached to, so correct that reference. The spacecraft name in the report reads oddly, so check it. Some sections are dense, so consider breaking them up for readability.

*Assessor reasoning:* Well-structured with executive summary, labelled tables and figures, and an appendix of STK files. Citation [13] does not support the Mount Pleasant claims it is attached to. The name 'Z-axis/Y-axis Zeroed Zoning Satellite' is odd. Some sections are dense.
> 2.4 Ground Control & Communications: "it has a 26 m and a 12 m antenna [13]"  
> Bibliography: "[13] J. E. J. Lovell et al., "The AuScope geodetic VLBI array,""  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction, Number of spacecraft |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction, Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit, Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit; Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Figures 1-5; Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | 2.4 Ground Control & Communications; Bibliography |

## Technical issues

- 2.4 Ground Control & Communications, Table 6: Six passes at 510 s each give about 51 min/day, not the 34 min (2,000 s) used for downlink capacity. The 510/771 fraction is also about 66%, not 60%.
- 2.3 Orbit / Table 1: A descending crossing at about 08:45 local mean solar time is inconsistent with a 34-minute eclipse per orbit; an eclipse of that length implies a near-noon-midnight orbit.
- 2.4 Ground Control & Communications, Table 6: The 115 Gbit/day raw volume assumes one 60 km × 1,000 km strip per day, which is not reconciled with about 15 orbits per day and the revisit analysis.
- 2.4 Ground Control & Communications: Reference [13] (AuScope VLBI array) does not support the claims about Mount Pleasant's antennas and status.
- 2.2 Launch: The stated condition that launch latitude must be less than 180° minus inclination is not a correct general requirement for direct insertion; it is unsupported.

## Next steps

1. Recheck the ground-pass arithmetic in Table 6: six passes of 510 s give about 51 minutes per day, and 510/771 is about 66%. Reconcile these with the 2,000 s downlink figure used in the data budget.
2. Make the eclipse timing consistent with the orbit: a 34-minute eclipse implies a near-noon-midnight orbit, which conflicts with the 08:45 crossing in Table 1.
3. Replace or verify reference [13] for the Mount Pleasant antenna claims, and support or remove the launch-latitude condition in 2.2 with a correct source.

---
<sub>Run Input_2_u-Run_3-Eff_low-261118-133657 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 20862/9273 | cost $0.006776 (incl. $0.001387 for the reused reference rubric+task structure) | 43.83s</sub>
