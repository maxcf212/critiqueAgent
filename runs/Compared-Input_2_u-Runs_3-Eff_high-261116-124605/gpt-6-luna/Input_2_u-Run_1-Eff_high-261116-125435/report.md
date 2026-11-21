# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 75 / 100 (75%)**

You present a clear mission with an Australian benefit, a well-structured report, and useful STK evidence in Images 1, 3, 4 and 5 and Appendix A. Your strongest opportunity is to verify key performance claims: the revisit and mosaic timings in Table 3 are not established by the calculations, while payload, downlink and end-of-life assumptions need stronger supporting analysis.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Section 1 clearly explains the bleaching-mapping mission, its Australian need, the choice of one spacecraft, and AIMS and its customers. To strengthen this accomplished work, prioritize authoritative primary scientific sources for key claims.

*Assessor reasoning:* Clearly explains the mission need, direct bleaching-mapping concept, rationale for using one spacecraft, and named operator and customers. The discussion is detailed and supported by relevant citations; a few cited sources are less authoritative than primary scientific literature.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

Sections 2.2–2.5 address launch, orbit, manoeuvres, ground communications, duration and EOL, supported by STK figures and Appendix A. To strengthen this accomplished design, substantiate Table 3’s coverage timings, the payload-performance claim and the downlink capacity with appropriate analyses.

*Assessor reasoning:* Addresses launch choice, orbit and elements, manoeuvres, ground-station accesses, data volume, mission duration and disposal, with STK views, access data and hand calculations. The coverage-time derivation is dimensionally invalid and unsupported by a target-access simulation; the link budget is also absent. These significant limitations prevent a higher mark.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> Table 3: "Days to reach any point of the reef | 2,698 km / 560 km | about 5 days"  
> 2.4 Ground Control & Communications: "A full link budget for the X-band downlink has not been calculated in this report"  
> Image 1  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

### C3 Conclusion (8/10, Accomplished)

Section 3 draws specific conclusions, identifies limitations and proposes next steps. Make those conclusions more persuasive by basing coverage and performance statements on validated simulations and calculations, and by reporting the uncertainty in the EOL estimate.

*Assessor reasoning:* The conclusion draws specific outcomes from the design, recaps performance and EOL estimates, and openly identifies limitations and next steps. Some results it relies on, especially revisit and mosaic timing, are not securely established by the calculations.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps that current temperature-based monitoring cannot."  

### C4 Report presentation (16/20, Accomplished)

The Executive Summary, contents, numbered sections, labelled figures and tables, and bibliography give the report a clear engineering structure. To refine the presentation, polish occasional awkward wording, check source completeness and authority, and ensure that each stated result is supported by the evidence presented.

*Assessor reasoning:* Uses a clear engineering-report structure, concise executive summary, numbered sections, labelled tables and figures, and an identifiable bibliography with in-text citations. The writing is generally readable, though occasionally awkward; some sources are incomplete or less authoritative, and the unsupported coverage claims weaken the presentation of results.
> Executive Summary: "The design is supported by STK simulations and by hand calculations of the orbit, coverage, data budget and orbital decay."  
> 2.3 Orbit: "Figure 1: STK 3D view of the ZYZZsat orbit at two times 12 hours apart (generated in STK 11)."  
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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit; Appendix A: STK files and settings |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Images 1, 3, 4 and 5; Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Executive Summary; Contents; Bibliography |

## Technical issues

- Table 3: The estimates 2,698 km / 560 km ≈ 5 and 2,698 km / 60 km ≈ 45 are dimensionless ratios, not days. They use adjacent-track spacing without establishing how the ground-track pattern shifts or repeats over time. The stated five-day access and 45-day mosaic are therefore unsupported; the STK figures show ground tracks, not sensor access or coverage of the reef.
- 2.4 Ground Control & Communications: A 50 Mbit/s downlink capacity is assumed without a link budget. Antenna gains, transmit power, frequency allocation, modulation/coding, losses and link margin are not established, so the claimed daily capacity margin is unverified.
- 2.1 Spacecraft overview: The 0.10 m aperture is compared only with an ideal diffraction limit at 0.5 µm. That calculation alone does not establish 5 m multispectral image resolution or GSD; focal length, detector sampling, optical performance and signal-to-noise are not demonstrated.
- 2.5 Mission Duration & EOL: The drag-sail lifetime estimate uses a simplified constant-density, scale-height model. The report acknowledges large solar-cycle variation, but does not provide a bounded lifetime analysis that verifies disposal within 25 years across environmental uncertainty.

## Next steps

1. In §2.3 and Table 3, replace the distance-ratio estimates with a justified revisit and reef-mosaic analysis. Use target-access or coverage simulations, explain the ground-track repeat pattern, and distinguish revisit time from the time to image the whole reef.
2. In §2.1 and §2.4, substantiate the 5 m multispectral resolution and 50 Mbit/s downlink. Show the optical and detector parameters needed to establish GSD and image performance, and provide a link budget covering antenna gains, transmit power, frequency, losses and link margin.
3. In §2.5, test drag-sail disposal lifetime across plausible atmospheric-density and solar-cycle conditions, and show whether the 25-year disposal requirement is met with margin. Use the resulting bounds when stating your EOL conclusion in §3.

---
<sub>Run Input_2_u-Run_1-Eff_high-261116-125435 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15069/15330 | cost $0.009547 (incl. $0.001387 for the reused reference rubric+task structure) | 123.07s</sub>
