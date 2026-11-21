# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 90 / 100 (90%)**

Excellent work on the ZYZZsat mission design report. All required elements are addressed with strong justification, verified hand calculations, and clear STK evidence. Your honest treatment of limitations is a real strength. To reach the top band, close the remaining analytical gaps: complete the X-band link budget, extend the access analysis beyond two days, and tighten reference details.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Your introduction addresses all four requirements in detail: the 5 m GBR imaging mission, the bleaching-detection rationale, the single-satellite choice with cost/communications justification, and clearly named operator (AIMS) and customers. Literature references [1]-[6] support the discussion well. For full marks, deepen the user needs analysis - e.g. quantify how the 5 m resolution and revisit meet AIMS and GBRMPA monitoring requirements.

*Assessor reasoning:* All four required items (primary mission, rationale, spacecraft number, users) are addressed in detail with specific facts and literature references [1]-[6]. Rationale links bleaching detection gap to mission need. Only minor further depth on user needs analysis would raise it to 10.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)... The customers are the Great Barrier Reef Marine Park Authority" *(quote not found in submission)*  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

A comprehensive, well-evidenced design: justified Vega C/Kourou trade (Table 2), orbit elements (Table 4), hand-verified sun-synchronous inclination, a clear no-manoeuvre argument, STK access statistics, data budget, and drag-sail EOL. Screenshots and appendix STK files support the work. The uncalculated X-band link budget and the two-day access sample are the main gaps preventing full marks; also note the Vega C flight-record caveat is handled acceptably via your fallback.

*Assessor reasoning:* All major requirements addressed: launch site/vehicle with justified trade (Table 2), orbit type, elements (Table 4), hand-verified J2 sun-synchronous inclination, no-manoeuvre justification, STK access analysis, data budget, 5-year duration and drag-sail EOL. STK screenshots and appendix files provided. Hand calculations (decay, swath, azimuth) check out. Link budget explicitly deferred, a minor gap.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "cos i = −(1.991 × 10⁻⁷) / (1.5 × 1.0826 × 10⁻³ × 0.8354 × 1.0831 × 10⁻³) = −0.1355, so i = 97.79°"  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC), and the mean pass lasts 580.8 s"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission."  

### C3 Conclusion (9/10, Accomplished)

Your conclusions are specific and quantitative, tracing directly to the evidence (e.g. the 600 km, 97.79 degree orbit giving consistent morning lighting), and you honestly identify four limitations with mitigation paths. This is well above generic. To reach full marks, tie each limitation to a concrete next action or design iteration step, showing how the design would be refined.

*Assessor reasoning:* Conclusions are specific and quantitative, drawn directly from the report's evidence, and honestly identify four limitations with mitigation paths (fallback launcher, unproven fluid lensing, missing link budget, coverage rate). Not generic.
> 3 Conclusion: "A 600 km sun-synchronous orbit at 97.79° inclination gives the same morning lighting on every pass"  
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown"  

### C4 Report presentation (18/20, Accomplished)

The report is professionally structured with an executive summary, numbered sections, consistently labelled figures and tables, and IEEE-style citations [1]-[15] that match in-text usage. Writing is precise throughout. The barrier to full marks is reference completeness: several entries are loosely specified, so tighten them to full bibliographic standard. Otherwise, formatting and presentation are exemplary.

*Assessor reasoning:* Clear structure with executive summary, numbered sections, consistently labelled and referenced figures/tables, IEEE-style citations [1]-[15] all matching in-text usage. Writing is precise and professional. Some references are loosely specified (e.g. 'Nature, news article', 'The Space Review, article 3887'), preventing a 10.
> Executive Summary: "This report presents the design of ZYZZsat... a single Earth observation microsatellite for monitoring coral bleaching" *(quote not found in submission)*  
> 2.3 Orbit: "Figure 2: Inclination required for a sun-synchronous orbit as a function of altitude."  
> Bibliography: "[11] D. A. Vallado, Fundamentals of Astrodynamics and Applications, 4th ed."  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3/2.4 (STK 11) plus hand calculations |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Images 1-5; Appendix A lists STK files in ZYZZsat_STK.zip |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Whole report; Bibliography [1]-[15] |

## Technical issues

- 2.4 Ground Control & Communications: Link budget for the X-band downlink is not calculated (acknowledged by the student); the 50 Mbit/s rate and 3.5x margin are asserted without link closure.
- 2.5 Mission Duration & EOL: Decay calculation uses a single mean density and constant scale height; solar-cycle variability acknowledged but lifetime figures are order-of-magnitude only.
- 2.4 Ground Control & Communications: Access statistics derived from only two days of STK data; pass frequency claim generalised from a short sample.
- 2.2 Launch: Vega C flight record stated as of 2020; baseline relies on a vehicle not yet flown at time of writing (fallback provided, so acceptable).

## Next steps

1. Complete the X-band downlink link budget in Section 2.4 so the 50 Mbit/s rate and 3.5x margin are demonstrated by link closure rather than asserted.
2. Extend the STK access analysis beyond the two-day sample (e.g. a full repeat cycle or season) before generalising the six-passes-per-day claim in Table 5.
3. Refine loosely specified bibliography entries (e.g. 'Nature, news article', 'The Space Review, article 3887') with full author, title, date and URL/DOI details.

---
<sub>Run Input_2_u-Run_1-Eff_high-261116-130719 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15389/5089 | cost $0.003565 (incl. $0.001387 for the reused reference rubric+task structure) | 74.45s</sub>
