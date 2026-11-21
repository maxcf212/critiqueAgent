# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 88 / 100 (88%)**

Excellent, comprehensive mission design report for ZYZZsat. All task requirements are met, with verified hand calculations, STK screenshots and files, honest discussion of limitations, and professional presentation. Minor deductions arise from the missing link budget, reliance on the unflown Vega C, and two incomplete references. A very strong submission overall.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Accomplished (9/10). Your Introduction addresses all four requirements in detail: the 5 m GBR imaging mission, need supported by bleaching literature [1]-[3], clear single-spacecraft justification, and identified operator (AIMS) and customers. To reach the very top, quantify the revisit-time trade-off between one satellite and a small constellation, even briefly, rather than relying on Section 2.3 to cover it.

*Assessor reasoning:* All four required items addressed in detail: primary mission, need (bleaching statistics, [1]-[3]), single-spacecraft justification, and operator/customers clearly identified. Well referenced with literature. Only minor point: rationale for one satellite could quantify revisit trade vs constellation, but Section 2.3 covers this.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Accomplished (9/10). Your mission design addresses every requirement: justified Vega C/Kourou launch with azimuth calculation, correct J2-derived sun-synchronous elements (Table 4), explicit no-manoeuvre statement, STK access analysis (Table 5), data budget, and drag-sail EOL. Hand calculations were verified correct and STK evidence is complete. The next level requires closing the acknowledged gap: a link budget supporting the Mount Pleasant communications assumption.

*Assessor reasoning:* All major requirements addressed: launch site/vehicle with justified trade table and azimuth calculation, orbit elements (Table 4) with correct J2 sun-synchronous derivation, explicit no-manoeuvre statement, STK access table for ground station, data budget, 5-year duration and drag-sail EOL. Hand calculations verified correct (decay, azimuth, spacing, data volume). STK screenshots and files provided. Link budget admittedly missing.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "cos i = −0.1355, so i = 97.79°" *(quote not found in submission)*  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission"  

### C3 Conclusion (9/10, Accomplished)

Accomplished (9/10). Your conclusions are specific and quantitative, summarising orbit, coverage, communications and EOL outcomes, and honestly identify four limitations with concrete next-phase actions (e.g. Vega C flight status, drag-sail re-entry in ~2 years vs ~32 years). This is well beyond generic; little further improvement is needed at this level.

*Assessor reasoning:* Conclusions are specific and quantitative, summarising orbit, coverage, communications and EOL results, and honestly identify four limitations with concrete next-phase actions. Well beyond generic.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown"  
> 3 Conclusion: "a 4 m² drag sail removes the satellite in about two years, compared with about 32 years without it"  

### C4 Report presentation (16/20, Accomplished)

Accomplished (8/10). Your report has a clear structure with executive summary, numbered sections, consistently labelled figures/tables, and in-text citations [1]-[15] matching the bibliography. Writing is professional. To reach the top of the band, complete references [4] and [15] with titles/authors, and replace or annotate the low-information STK 3D views so every figure carries design content.

*Assessor reasoning:* Clear logical structure with executive summary, numbered sections, consistently labelled figures/tables, and all in-text citations [1]-[15] matching the reference list. Writing is professional. Minor flaws: references [4] and [15] lack proper article titles/authors, and some figures (STK 3D views) are low-information content.
> Executive Summary: "This report presents the design of ZYZZsat"  
> Bibliography: "The Space Review, article 3887 on drag sails for de-orbiting satellites."  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3/2.4 (STK 11 plus hand calculations) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Images 1-5; Appendix A lists STK files in ZYZZsat_STK.zip |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Whole report; Bibliography |

## Technical issues

- 2.4 Ground Control & Communications: Assumes S-band/X-band equipment can be added to the Mount Pleasant radio astronomy antenna; no link budget performed (acknowledged by student).
- 2.2 Launch: Vega C unflown at time of writing; fallback considered, but release altitude uncertainty propagates to orbit design (acknowledged).
- Bibliography: References [4] and [15] incompletely specified (no article title/author).
- 2.3 Orbit: Eclipse duration of ~34 min stated without shown calculation, though plausible for 600 km SSO.

## Next steps

1. Perform a full link budget for the S-band/X-band link to Mount Pleasant (Section 2.4), showing margin, to substantiate the six-passes-per-day communications claim.
2. Strengthen the launch justification by quantifying how release-altitude uncertainty for Vega C propagates into your orbit design (Section 2.3), and state explicit fallback orbit elements for the backup vehicle.
3. Complete references [4] and [15] with full article titles and authors, and consider replacing low-information STK 3D views with annotated figures that highlight key design parameters.

---
<sub>Run Input_2_u-Run_2-Eff_high-261116-130833 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15217/5404 | cost $0.002856 (incl. $0.001387 for the reused reference rubric+task structure) | 86.83s</sub>
