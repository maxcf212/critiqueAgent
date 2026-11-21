# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 89 / 100 (89%)**

Excellent, technically sound mission design report for ZYZZsat. All required elements are addressed with verified hand calculations, STK evidence and proper referencing. To reach the very top of the rubric, add an elevation-constrained access analysis, an X-band link budget, and a solar-cycle-aware decay analysis.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Accomplished (9/10). Your Introduction covers all requirements: primary mission (5 m imaging of the Great Barrier Reef), rationale with cited context, single-spacecraft justification, and operator/customers (AIMS). Next level needs slightly more depth on rationale and funding context, with fuller referencing of the mission-need discussion.

*Assessor reasoning:* All required items addressed: primary mission, rationale with cited context, single-spacecraft justification, operator and multiple customers. Detailed and well referenced; only slightly brief on funding/rationale depth.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Accomplished (9/10). Your launch (Vega C rideshare from Kourou), orbit design (verified J2 sun-sync hand calculation, i = 97.79°), manoeuvres, ground control, access frequency, duration and EOL are all well supported by STK screenshots, tables and hand calculations. To reach the top band, add the missing X-band link budget and re-run accesses with an elevation constraint.

*Assessor reasoning:* Launch, orbit (with correct J2 sun-sync hand calc verified), elements, manoeuvres, ground station, access frequency, duration and EOL all covered with STK screenshots, access tables, hand calculations and references. Link budget admittedly missing, a minor gap.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "cos i = −(1.991 × 10⁻⁷) / (1.5 × 1.0826 × 10⁻³ × 0.8354 × 1.0831 × 10⁻³) = −0.1355, so i = 97.79°"  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  

### C3 Conclusion (8/10, Accomplished)

Accomplished (8/10). Your conclusions follow directly from the evidence and honestly identify four limitations and further work. They are specific and useful, but brief; expanding each conclusion with quantitative support would lift this criterion further.

*Assessor reasoning:* Conclusions follow directly from the evidence and honestly identify limitations and further work; specific and useful, though brief.
> 3 Conclusion: "A 600 km sun-synchronous orbit at 97.79° inclination gives the same morning lighting on every pass"  
> 3 Conclusion: "The design has four limitations."  

### C4 Report presentation (18/20, Accomplished)

Accomplished (9/10). Your report has clear structure, an executive summary, labelled figures/tables, consistent IEEE-style citations matching the bibliography, and good grammar. Minor improvement: make references like [15] more specific, and keep formatting consistency throughout.

*Assessor reasoning:* Clear structure, executive summary, numbered/labelled figures and tables, consistent IEEE-style citations matching the bibliography, good grammar. Minor: some references (e.g. [15]) are vague.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite"  
> 2.3 Orbit: "Figure 2: Inclination required for a sun-synchronous orbit as a function of altitude."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction (Number of spacecraft) |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction (Users) |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit (Manoeuvres) |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications, Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3/2.4 STK use plus hand calculations |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Figures 1–4, Appendix A (ZYZZsat_STK.zip file list) |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Whole report; Bibliography |

## Technical issues

- 2.4 Ground Control & Communications: Accesses computed with no elevation constraint; usable-time estimate above 10° is approximated rather than re-run in STK.
- 2.4 Ground Control & Communications: No X-band link budget, acknowledged by the author.
- 2.5 Mission Duration & EOL: Decay analysis uses a single mean density; solar-cycle variation only discussed qualitatively.
- 2.2 Launch: Vega C flight record stated as of 2020; by a 2025 launch the comparison would need updating (minor).

## Next steps

1. Re-run STK access analysis with a 10° elevation constraint and report usable pass durations instead of approximating them from unconstrained accesses.
2. Add an X-band link budget (EIRP, path loss, data rate, margin) to Section 2.4 to close the acknowledged gap.
3. Refine the Section 2.5 decay analysis by propagating across solar-cycle density variation rather than a single mean density, and update the Vega C flight record comparison for a 2025 launch.
4. Tighten vague references (e.g. [15]) so every citation is specific and traceable.
5. Slightly deepen the Introduction's rationale/funding discussion and expand the Conclusion beyond its current brevity.

---
<sub>Run Input_2_u-Run_1-Eff_low-261118-133740 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15120/4105 | cost $0.003243 (incl. $0.001387 for the reused reference rubric+task structure) | 38.61s</sub>
