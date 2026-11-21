# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 88 / 100 (88%)**

Your ZYZZsat report is a strong, well-evidenced preliminary design: launch, SSO orbit and elements, manoeuvres, ground segment, duration and drag-sail EOL are all covered with verified hand calculations, STK outputs and submitted files. The introduction and conclusion are detailed and quantitative. To reach the top of the Accomplished band, close the X-band link budget, justify the imaging plan, and tighten referencing and figure provenance.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You address all C1 requirements to a high standard: the primary mission, need, single-spacecraft rationale and users (AIMS operator; GBRMPA, CSIRO, BoM customers) are clear and cited [1]–[6]. To secure full marks within Accomplished, replace the vague Nature news citation [4] with a specific source and add one or two sentences on why one spacecraft meets revisit needs.

*Assessor reasoning:* Mission, need, spacecraft count and users (operator AIMS; customers GBRMPA, CSIRO, BoM) all covered with reasoning and citations [1]-[6]. Rationale for direct bleaching detection is well argued. Minor: source [4] is vaguely cited (Nature news article).
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution, so that bleaching is mapped directly"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

All major design elements are covered with strong evidence: launch azimuth and inclination checks, Table 4 elements, manoeuvres, Table 5 access, decay rates and the drag-sail EOL, plus STK files in Appendix A. To reach the top of Accomplished, add the missing X-band link budget, reconcile Table 6's 60,000 km²/day with the pushbroom swath, and state the revisit assumptions.

*Assessor reasoning:* All major elements addressed with STK screenshots, access reports, hand calculations and file list. Checks verified: inclination, azimuth, period, aperture, decay rates (0.40 m/orbit, 2.2 km/yr; sail 5.8 m/orbit), data budget (115 Gbit → 29 Gbit vs 100 Gbit). Gaps: no X-band link budget (acknowledged); revisit estimate approximate; only one 60,000 km² strip/day is conservative.
> 2.2 Launch: "sin β = cos 97.79° / cos 5.2° = −0.1355 / 0.9959 = −0.136, so β = −7.8°"  
> 2.3 Orbit: "cos i = −(1.991 × 10⁻⁷) / (1.5 × 1.0826 × 10⁻³ × 0.8354 × 1.0831 × 10⁻³) = −0.1355, so i = 97.79°"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission."  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

### C3 Conclusion (9/10, Accomplished)

Your conclusion is quantitative and drawn directly from the design, with a candid four-point limitations list. To strengthen within Accomplished, add specific recommendations (e.g., link-budget validation, ground-station hardware and licensing path, fluid-lensing maturity) and tie each limitation to a concrete next action or risk.

*Assessor reasoning:* Conclusions are quantitative, drawn directly from the design sections, and include a candid limitations list (Vega C maturity, unproven fluid lensing at 5 m, ground-station equipment, 45-day mosaic). Slight improvement possible on recommendation detail.
> 3 Conclusion: "A 600 km sun-synchronous orbit at 97.79° inclination gives the same morning lighting on every pass, a 5 m image with a 60 km swath"  
> 3 Conclusion: "The design has four limitations."  

### C4 Report presentation (16/20, Accomplished)

Clear engineering structure, concise prose, numbered captioned figures/tables, executive summary and consistent [1]–[15] citation. To move from 8 to the top of Accomplished, state how Figure 2 was generated and reference its data file, sharpen vague references [4] and [15], fix unit/factor-of-ten typography, and add a table of figures.

*Assessor reasoning:* Clear structure, concise prose, well-captioned numbered figures/tables, executive summary, all references [1]-[15] cited in text. Deductions: vague references [4] and [15], Figure 2 generation method not stated, minor formatting/typographic slips (factor-of-ten expressions, unit style) and no table of figures.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite"  
> 2.3 Orbit: "Table 4: Orbital elements of ZYZZsat at the scenario epoch, 3 Feb 2025 00:00:00 UTCG (mean elements, J2000 frame)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction, Executive Summary |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit (Manoeuvres) |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications, Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit, 2.4, Appendix A (STK 11) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Figures 1, 3, 4; Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents, Bibliography |

## Technical issues

- 2.4 Ground Control & Communications: X-band link budget not performed; 50 Mbit/s downlink and ground-station sizing are asserted rather than demonstrated.
- Table 6: Imaging plan assumes only 60,000 km² per day (one 1,000 km strip), far below the satellite's actual capability; revisit/mosaic logic is therefore conservative but internally inconsistent with a pushbroom imager.
- 2.3 Orbit: Revisit calculation (2,698 km / 560 km ≈ 5 days) ignores latitude convergence and assumes single-pass access; real coverage at 18°S uses ~2,570 km track spacing, giving ~4.6 days - acceptable but not stated.
- 2.2 Launch: Vega C status ('has not yet flown, first flight planned 2021') is accurate for 2020 but should be flagged as time-dependent; rideshare injection accuracy and exact release altitude are not specified.
- Figure 2: Inclination-vs-altitude curve has no stated source or generation method (STK/MATLAB) and no data file reference.
- 2.4 Ground Control & Communications: Mount Pleasant is a VLBI/geodesy facility; addition of S/X-band hardware, licensing and cost are assumed rather than designed, with no elevation mask used in the access report.

## Next steps

1. Add an X-band link budget in 2.4 (EIRP, G/T, path loss, modulation/coding, margin) to demonstrate the 50 Mbit/s downlink and ground-station sizing, and state the elevation mask used in the access report.
2. Revisit Table 6: reconcile the 60,000 km²/day imaging plan with the pushbroom swath and actual daily access, show the mosaic/revisit logic, and state the ~2,570 km track spacing giving ~4.6 days at 18°S.
3. Tighten presentation: give a source/generation method and data file for Figure 2, replace vague references [4] and [15] with specific sources, fix unit/factor-of-ten typography, and consider adding a table of figures.

---
<sub>Run Input_2_u-Run_1-Eff_high-261116-124903 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14556/7439 | cost $0.005749 (incl. $0.001387 for the reused reference rubric+task structure) | 45.95s</sub>
