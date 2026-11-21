# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 69 / 100 (69%)**

You present a strong, well-structured preliminary mission report with a clear Australian environmental purpose, defined users, STK-supported design elements and an EOL plan. Your main improvement area is validating the coverage and communications claims: these currently limit confidence in the mission’s mapping schedule and feasibility.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Section 1 clearly explains ZYZZsat’s reef-imaging mission, its Australian environmental rationale, why you selected one spacecraft, and the operator and customer groups. To strengthen this already detailed discussion further, support key claims with more authoritative sources alongside your existing citations.

*Assessor reasoning:* Clearly explains the mission, its Australian environmental need, the choice of a single spacecraft, and specific operator and customer groups. The rationale is detailed and supported with citations. A few claims rely on relatively general or secondary sources, preventing a top mark.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Sections 2.2–2.5 address launch choice, orbit elements, ground access and EOL, with STK evidence in Image 1, Table 5 and Appendix A. For the accomplished level, validate revisit and mosaic timing with time-based coverage analysis, reconcile imaging capacity with reef area, and substantiate downlink capacity with a link budget.

*Assessor reasoning:* The design is comprehensive and uses STK outputs, calculations, orbital elements, access data and an EOL analysis to address the major requirements. However, the claimed five-day revisit and 45-day nadir mosaic derive days by dividing track spacing in km by a footprint width in km; this is dimensionless and does not establish revisit time without ground-track drift or coverage analysis. The daily imaging plan also does not reconcile with full-reef coverage, and the assumed downlink rate lacks a link budget.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "With J2 = 1.0826 × 10⁻³, R = 6,378 km, a = 6,978 km and mean motion n = √(μ/a³) = 1.0831 × 10⁻³ rad/s:"  
> 2.4 Ground Control & Communications: "STK 11 was used to calculate when the satellite is above the horizon at Mount Pleasant."  
> 2.4 Ground Control & Communications: "A full link budget for the X-band downlink has not been calculated in this report and is the main item of further work for this segment."  
> 2.5 Mission Duration & EOL: "The EOL plan is therefore passive: a drag sail is deployed at the end of the mission."  

### C3 Conclusion (8/10, Accomplished)

Section 3 draws useful, specific conclusions and identifies limitations and future work. Make sure its coverage conclusions rely on validated time-based results rather than the unsupported revisit calculations, so the conclusions follow directly from your evidence.

*Assessor reasoning:* The conclusion draws specific results from the design and candidly identifies limitations and next steps. It is appropriate and useful, although some of its coverage conclusions repeat the unsupported revisit calculations.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown, so the Falcon 9 rideshare service is kept as a fallback"  
> 3 Conclusion: "With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps that current temperature-based monitoring cannot."  

### C4 Report presentation (16/20, Accomplished)

Your executive summary, numbered sections, labelled figures and tables, and bibliography create a clear engineering-report structure. To improve presentation further, polish some prose and reference entries, and present the coverage results with analysis that makes their basis and limitations clear.

*Assessor reasoning:* The report has a clear engineering structure, executive summary, numbered sections, labelled tables and figures, and a substantial bibliography with in-text citations. It is readable and generally consistent. Some prose and reference entries could be more polished, and the central coverage presentation is not adequately substantiated, which limits confidence in the presentation of results.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite for monitoring coral bleaching on the Great Barrier Reef."  
> 2.4 Ground Control & Communications: "Table 5: STK access report, ZYZZsat to Mount Pleasant Radio Observatory (elevation above 0°)."  
> Bibliography: "[11] D. A. Vallado, Fundamentals of Astrodynamics and Applications, 4th ed. Hawthorne, CA, USA: Microcosm Press, 2013."  

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
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Image 1; Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Bibliography |

## Technical issues

- 2.3 Orbit: The claimed revisit and nadir-mosaic periods divide ground-track spacing (km) by reachable width or swath (km), producing a dimensionless ratio rather than days. A repeat-ground-track or time-dependent coverage analysis is needed to support these periods.
- 2.4 Ground Control & Communications: The daily plan budgets 60,000 km² of imaging, while the reef area is stated as 344,400 km². Covering the entire reef within five days would require at least 68,880 km²/day even with no overlap; the coverage and data-volume plan are not reconciled.
- 2.4 Ground Control & Communications: The 50 Mbit/s X-band rate and resulting capacity are assumed rather than verified with a link budget. The report acknowledges this, so achievable downlink capacity remains unestablished.

## Next steps

1. In Section 2.3, replace the distance-to-swath calculations with a time-based coverage analysis, such as repeat-ground-track or STK coverage analysis. Show how the evidence supports the five-day revisit and 45-day mosaic claims, with units and assumptions.
2. In Section 2.4, reconcile the 60,000 km²/day imaging plan with the 344,400 km² reef area (at least 68,880 km²/day for full coverage in five days, before overlap). Account for overlap and data volume, then verify the assumed 50 Mbit/s X-band rate and capacity with a link budget.
3. Strengthen the report’s evidence and polish: support key claims with appropriate sources, refine prose and reference entries, and ensure the conclusion reflects only coverage and communications results established by your analysis.

---
<sub>Run Input_2_u-Run_3-Eff_high-261116-125943 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15142/15004 | cost $0.008196 (incl. $0.001387 for the reused reference rubric+task structure) | 134.88s</sub>
