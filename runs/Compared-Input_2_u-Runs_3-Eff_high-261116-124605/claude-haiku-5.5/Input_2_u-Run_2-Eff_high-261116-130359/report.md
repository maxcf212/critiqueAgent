# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 87 / 100 (87%)**

Your report presents a strong, technically grounded preliminary design, with a clear structure, verified orbit and drag calculations, and STK support. The main gaps are unexplained assumptions in the data budget and contact-time figures, a mismatch between the Vega 700 km orbit and your 600 km design altitude, and some uncited claims. Addressing these would considerably strengthen the technical justification.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You clearly set out the primary mission of imaging the whole Great Barrier Reef at 5 m resolution, why it is needed, why one spacecraft suffices, and who the operator and customers are, including the Marine Park Authority's use of bleaching maps. Your claims are supported by references [1]–[6]. To reach the top band, reference the remaining background claims, such as reef reliance for food and tourism, and tighten the wording of the introduction.

*Assessor reasoning:* Covers primary mission, rationale against existing aerial and satellite monitoring, single-spacecraft justification, and operator and customers in detail. Claims are referenced to literature [1]-[6]. Minor gaps: some background claims (e.g. reliance on reefs) are uncited, and the introduction is a little verbose.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The customers are the Great Barrier Reef Marine Park Authority, which uses bleaching maps to direct in-water surveys and management responses"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Your design is thorough and largely accurate. Launch options are compared, the J2 inclination and period are verified, drag decay is reproduced, and the sin β calculation in Section 2.2 is shown. To reach the top band, show working for the 510 s of 771 s contact figure, justify the eclipse duration and battery sizing, explain the 1,000 km strip assumption, and consider more than one ground station.

*Assessor reasoning:* Thorough, largely accurate design: launch options compared, J2 inclination and period verified, drag decay reproduced, access report and STK figures supplied, and EOL justified. Weaknesses: the 510 s/10° contact calculation and the 34-minute eclipse are asserted without working, the daily data volume assumes an unexplained 1,000 km strip, and only one ground station is considered.
> 2.2 Launch: "sin β = cos 97.79° / cos 5.2° = −0.1355 / 0.9959 = −0.136, so β = −7.8°"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission."  
> Figure 1: "STK 3D view of the ZYZZsat orbit at two times 12 hours apart (generated in STK 11)."  
> 2.4 Ground Control & Communications: "the part of an overhead pass above 10° is 510 s of 771 s"  

### C3 Conclusion (8/10, Accomplished)

Your conclusions recap the key results and identify specific limitations, including Vega C status, 5 m fluid-lensing resolution, the missing X-band link budget and the 45-day mapping time, along with sensible next steps. To reach the top band, link each conclusion more explicitly to your evidence and analyse trade-offs, such as the halving of mapping time with a second satellite in the same plane, rather than largely summarising the body.

*Assessor reasoning:* Recaps key quantitative results and draws appropriate conclusions. It identifies specific limitations (Vega C status, fluid lensing at 5 m, missing X-band link budget, 45-day mapping) and next steps. It is somewhat summary-heavy, with less analysis of trade-offs beyond what the body already gives.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "a second satellite in the same orbit plane would halve it."  

### C4 Report presentation (16/20, Accomplished)

The assessment record for this criterion does not include a full rationale, so no specific strengths or gaps can be confirmed here. The Accomplished descriptor expects a clear engineering structure, consistent formatting, labelled figures and tables, a concise executive summary, and in-text citations that match the reference list. Check your report against each of these points.

*Assessor reasoning:* Placeholder duplicate; see C4 above.
> 1 Introduction: "Hundreds of millions of humans rely on reefs for food, natural protection, jobs, and tourism."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction: Number of spacecraft |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction: Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit: Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit; Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | 1 Introduction; Figure 2 |

## Technical issues

- 2.2 Launch: Vega is quoted for a 700 km polar orbit, but the design uses 600 km. The mismatch is not addressed, and the dispenser release altitude is unconfirmed.
- 2.4 Ground Control & Communications: The 10° elevation contact fraction is stated as 510 s of 771 s (about 66%), not the 'about 60 percent' claimed, and no working is shown.
- Table 6: The daily data budget assumes one 60 km × 1,000 km strip per day without justification, and 2,000 s is used for '34 minutes' (2,040 s).
- 2.3 Orbit: The 34-minute eclipse duration and battery sizing are asserted without calculation, despite the eclipse depending on beta angle at the 08:45 node.
- 2.5 Mission Duration & EOL: Lifetime ≈ H/rate is a crude estimate, and the stated range of months to years is not derived from the density variation.

## Next steps

1. Show full working for the ground-contact fraction. 510 s of 771 s is about 66%, not the 'about 60 percent' stated, so correct either the claim or the figure.
2. Justify the assumptions in Table 6 and Section 2.3. Explain the single 60 km × 1,000 km strip per day, use 2,040 s rather than 2,000 s for the 34-minute eclipse, and calculate eclipse duration and battery sizing from the beta angle at the 08:45 node.
3. Resolve the Vega altitude mismatch by explaining the 600 km design altitude against the 700 km polar orbit and confirming the dispenser release altitude. Also add references for uncited claims, and derive the lifetime range from the density variation rather than from H/rate alone.

---
<sub>Run Input_2_u-Run_2-Eff_high-261116-130359 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 20808/20700 | cost $0.011142 (incl. $0.001387 for the reused reference rubric+task structure) | 88.31s</sub>
