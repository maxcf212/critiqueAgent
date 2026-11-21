# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 79 / 100 (79%)**

You have produced a technically strong preliminary design. Your introduction clearly sets out ZYZZsat's purpose, single-spacecraft configuration and users, and your orbit, geometry, data and drag calculations are verifiable and supported by STK outputs in Appendix A. Your conclusions tie back to your evidence and identify specific limitations. The main areas to strengthen are the missing link budget, the unsupported site-selection claim, and several uncited or weakly sourced statements in the introduction.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 7 / 10 | 14 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You cover the mission purpose, the rationale for a single spacecraft, and the operator and customers in good detail, with literature support. The opening biodiversity and human-reliance claims are uncited, and the bleaching-loss statistics rely on a magazine source. Citing authoritative sources for these points would make the rationale more persuasive.

*Assessor reasoning:* Covers mission, rationale, single-spacecraft choice with justification, and operator and customers in detail, with literature support. Minor gaps: the opening biodiversity and human-reliance claims are uncited, and the bleaching-loss statistics rest on a magazine source.
> 1 Introduction, Primary mission: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction, Users: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Your hand calculations for RAAN drift, inclination, period, swath, revisit, data budget and drag decay are clear and check out, and your STK screenshots and files support them well. Table 7 on lifetime is a useful summary. The link budget is not yet done, the ground-station choice needs stronger justification, and the 'most southerly suitable site' claim needs comparison evidence. The lifetime estimate uses a single constant density and scale height, so it would benefit from a note on its limitations.

*Assessor reasoning:* Strong, verifiable hand calculations: RAAN drift giving i=97.79°, period, swath, revisit, data budget and drag decay all check out. Screenshots and STK files are provided. Deductions: the link budget is explicitly not done, the ground-station choice is weakly justified, and the 'most southerly suitable site' claim is unsupported.
> 2.2 Launch: "sin β = cos i / cos φ = −0.1355 / 0.9959 = −0.136, so β = −7.8°" *(quote not found in submission)*  
> 2.5 Mission Duration & EOL, Table 7: "Operational, no sail | 0.3 m² | 0.40 m | 2.2 km per year | about 32 years"  

### C3 Conclusion (8/10, Accomplished)

Your conclusions draw on your quantitative results and name specific limitations, such as Vega C not yet having flown, with remedies such as a second satellite in the same plane. Keep linking each conclusion to a specific figure or table in the body to make the evidence trail even clearer.

*Assessor reasoning:* Conclusions tie back to quantitative evidence and identify specific limitations and remedies. The summary of results is specific and well supported by the body.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown"  
> 3 Conclusion: "a second satellite in the same orbit plane would halve it"  

### C4 Report presentation (14/20, Accomplished)

Your report has a clear structure, an executive summary, labelled tables and figures, and a consistent reference style. To reach a more professional level, reduce informal wording and make sure every factual claim is cited, particularly in the introduction. Replace weaker sources such as the magazine and news references with more authoritative ones where possible.

*Assessor reasoning:* Clear structure, executive summary, labelled tables and figures, and a consistent reference style. Deductions: several factual claims are uncited, some sources are weak (magazine, news article), and a few terms are informal.
> 1 Introduction: "Hundreds of millions of humans rely on reefs for food, natural protection, jobs, and tourism."  
> Bibliography: "[2] National Geographic, "Great Barrier Reef coral bleaching map," Aug. 2018."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction, Number of spacecraft |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction, Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit, Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Figures 1,3,4; Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | 1 Introduction |

## Technical issues

- 2.4 Ground Control & Communications: The claim that Mount Pleasant is the most southerly suitable Australian site is unsupported by any comparison of candidate sites.
- 2.4 Ground Control & Communications: The X-band downlink and 50 Mbit/s rate are assumed without a link budget, so the 3.5× data margin rests on unverified assumptions.
- 2.5 Mission Duration & EOL: Lifetime is estimated as H/decay rate with a single constant density and scale height; this is crude and the stated 2.2-year sail lifetime is only approximate.

## Next steps

1. Add a link budget for the X-band downlink at 50 Mbit/s, so that the 3.5× data margin in Section 2.4 rests on calculated values rather than assumptions.
2. Compare the candidate Australian ground sites, or remove the claim that Mount Pleasant is the most southerly suitable site, so that the choice is justified.
3. Cite a peer-reviewed or authoritative source for the biodiversity and human-reliance statements in the introduction, and replace the magazine source for bleaching statistics with a scientific reference.

---
<sub>Run Input_2_u-Run_2-Eff_low-261118-133605 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 20588/9888 | cost $0.007056 (incl. $0.001387 for the reused reference rubric+task structure) | 51.9s</sub>
