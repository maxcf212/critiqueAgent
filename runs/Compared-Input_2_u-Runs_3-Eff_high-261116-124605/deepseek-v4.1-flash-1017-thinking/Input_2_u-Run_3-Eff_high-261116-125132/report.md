# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 84 / 100 (84%)**

Overall, this is a strong, well-structured mission design. You address all major elements and support them with STK screenshots, access data and hand calculations. The main improvements are the optimistic revisit calculation, missing X-band link budget/ground-segment verification, the rideshare release-orbit assumption, and Table 5 UTC/local wording. Embedding the STK files will make your evidence fully verifiable.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You address all C1 requirements clearly in Section 1: mission need, single-spacecraft rationale, operator AIMS and customers GBRMPA, with appropriate citations. To move toward the top of Accomplished, sharpen the rationale by distinguishing bathymetric mapping [3] from satellite imagery rather than conflating them at 100 m/pixel.

*Assessor reasoning:* Mission need, rationale, spacecraft count and users are all clearly and specifically addressed, with appropriate literature citations and a convincing Australian-benefit framing.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  
> 1 Introduction: "The customers are the Great Barrier Reef Marine Park Authority"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

You cover all major design elements with STK screenshots, access data and hand calculations (Sections 2.2-2.5). To strengthen: revise the Section 2.3 revisit calculation using the ~134 km daily track shift and ~280 km half-swath; add an X-band link budget and verify the Mount Pleasant 12 m ground-segment assumption in Section 2.4; clarify the rideshare release orbit/trim in Section 2.2; correct Table 5 UTC/local wording; embed STK files.

*Assessor reasoning:* All major design elements are covered with STK screenshots, access data and hand calculations. Some technical weaknesses remain, notably the optimistic revisit calculation and missing link budget/ground-segment verification, so not top of level.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "No orbital manoeuvres are required."  
> 2.4 Ground Control & Communications: "There are six passes each day"  
> 2.5 Mission Duration & EOL: "The mission lasts five years."  
> 2.5 Mission Duration & EOL: "a drag sail is deployed at the end of the mission"  

### C3 Conclusion (9/10, Accomplished)

Your Section 3 conclusion is specific and quantitative, and you record four limitations, which is strong. To move toward the top of Accomplished, explicitly link each limitation to the affected design choice and state the next verification step, so the conclusion reads as a clear evidence-based close rather than a list.

*Assessor reasoning:* Conclusion is specific, quantitative and clearly derived from the design evidence; it also records key limitations and next steps.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "The design has four limitations."  

### C4 Report presentation (18/20, Accomplished)

Your report has a clear engineering structure, a concise executive summary, labelled figures/tables and consistent citations. To move toward the top of Accomplished, polish minor awkward phrasing and resolve small labelling ambiguities; ensure every figure/table is explicitly referenced in text and that listed STK files are accessible so presentation evidence is fully verifiable.

*Assessor reasoning:* Clear engineering-report structure, concise executive summary, labelled figures/tables and consistent citations. Writing is generally professional, with only minor awkward phrasing and small labelling ambiguities.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite for monitoring coral bleaching on the Great Barrier Reef."  
> Table 1: "Table 1: ZYZZsat spacecraft summary."  
> Bibliography: "Bibliography"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction; 2.1 Spacecraft overview |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit; Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications; Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit; 2.4 Ground Control & Communications; Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Appendix A; Figures 1–4 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents; 1–3; Bibliography |

## Technical issues

- 2.3 Orbit: Revisit calculation divides 2,698 km track spacing by the full 560 km roll-swath width to give about 5 days. The daily track shift is only about 134 km at the equator and the half-swath is about 280 km, so maximum revisit is likely longer (order 8–20 days depending target). The 5-day claim is optimistic.
- 2.4 Ground Control & Communications: No X-band link budget is provided, and the design assumes S-band/X-band equipment can be added to the Mount Pleasant 12 m radio telescope. This is an unverified ground-segment implementation assumption and a gap in communications design.
- 1 Introduction: The statement that existing satellite products/depths are mapped at 100 m/pixel conflates a bathymetry model [3] with satellite imagery; the rationale should distinguish bathymetric mapping from satellite remote sensing.
- 2.2 Launch: The design assumes rideshare release directly into the 600 km, 97.79° operational orbit, while also noting a possible lower release. A lower release would require a different SSO inclination and likely orbit trim, which is not designed.
- 2.4 Ground Control & Communications; Table 5: Passes are described as 'three in evening and three in morning (UTC)', but the UTC times correspond to evening/morning in Hobart local time, not UTC; the wording is misleading.

## Next steps

1. Revise Section 2.3: use the ~134 km daily equatorial track shift and ~280 km half-swath rather than dividing 2,698 km by 560 km; report a realistic maximum revisit (order 8-20 days) or justify the 5-day claim with target-specific access results.
2. Add an X-band link budget in Section 2.4 and verify the Mount Pleasant 12 m ground-segment modification; correct Table 5's UTC/local-time wording and clarify the rideshare release orbit/trim in Section 2.2.
3. Make the STK evidence fully verifiable by embedding key screenshots and including the software files in Appendix A, and refine the Introduction's bathymetry-versus-satellite-imagery rationale.

---
<sub>Run Input_2_u-Run_3-Eff_high-261116-125132 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14286/24028 | cost $0.014658 (incl. $0.001387 for the reused reference rubric+task structure) | 182.83s</sub>
