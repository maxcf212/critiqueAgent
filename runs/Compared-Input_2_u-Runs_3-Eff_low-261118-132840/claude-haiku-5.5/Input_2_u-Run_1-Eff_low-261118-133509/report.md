# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 81 / 100 (81%)**

You have covered every required element of the report, with clear structure, STK evidence, hand calculations and a full bibliography. Your introduction and conclusion are specific and well tied to your results. The main gaps are technical: the launch azimuth for your retrograde orbit is described inconsistently, the contact-time and data-budget figures do not reconcile with each other, and the X-band downlink is not supported by a link budget. Correcting these would strengthen an already strong report.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You clearly state the primary mission, why it is needed, the single-spacecraft configuration and the operator and customers, with literature cited for the bleaching problem. The single-satellite rationale relies mainly on assertion. A brief quantified trade-off against multi-satellite options would make this section more persuasive.

*Assessor reasoning:* All four required items (mission, why needed, number of spacecraft with justification, operator and customers) are addressed in detail, with literature cited for the bleaching problem and fluid-lensing context. Minor weakness: the rationale for using one satellite leans on assertion rather than quantified trade.
> 1 Introduction, Primary mission: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction, Users: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

This is a thorough design, supported by STK figures, access tables, hand calculations and an appendix file list. Your launch, orbit and end-of-life sections are well evidenced. Inaccuracies to fix are the retrograde launch azimuth wording, the 66% versus 60% contact figure, the one-strip-per-day imaging assumption, and the unbudgeted X-band link. Sourcing the Mount Pleasant and Vega C claims would also help.

*Assessor reasoning:* Covers every required element with hand calculations that largely check out (J2 RAAN rate, diffraction aperture, swath, drag decay), supported by STK figures, access tables and an appendix file list. Deductions for: retrograde launch azimuth described as 'west of north' which conflicts with a retrograde orbit; the 510/771 s (66%) versus 60% contact figure; an unbudgeted X-band link; and a one-strip-per-day imaging assumption that does not match six passes.
> 2.2 Launch: "The launch azimuth β needed to reach the inclination i from latitude φ is found from sin β = cos i / cos φ"  
> 2.3 Orbit, Table 3: "Days to reach any point of the reef | 2,698 km / 560 km | about 5 days"  
> 2.5 Mission Duration & EOL, Table 7: "Sail deployed (4 m² sail plus body) | 4.3 m² | 5.8 m | 31 km per year | about 2.2 years"  

### C3 Conclusion (8/10, Accomplished)

Your conclusions are specific and link back to quantified results such as the 5-day revisit, the 3.5 margin and the roughly 2-year decay. You also identify concrete limitations with fallback options. Claims such as the weekly coverage reef managers prefer need a source, and the conclusions would be stronger if they reflected the corrected contact and data figures.

*Assessor reasoning:* Conclusions are specific, tie back to quantified results (5-day revisit, 3.5x margin, 2-year decay) and identify concrete limitations with next steps. Some claims, such as the 'weekly coverage reef managers prefer', are not sourced.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown, so the Falcon 9 rideshare service is kept as a fallback"  

### C4 Report presentation (16/20, Accomplished)

The report follows a clear engineering structure, with an executive summary, numbered and captioned tables and figures, and in-text citations matching the 15-entry bibliography. Writing is easy to follow. Harmonise the elevation mask: the access report uses 0° while the data budget uses 10°, and a single consistent setting would remove this inconsistency.

*Assessor reasoning:* Clear engineering structure with an executive summary, numbered and captioned tables and figures, and in-text numbered citations matching the 15-entry bibliography. Writing is clear. Minor inconsistency: the access report uses a 0° mask while the data budget uses 10°.
> Contents and section structure: "Executive Summary; 1 Introduction; 2 Mission Design; 3 Conclusion; Bibliography; Appendix A" *(quote not found in submission)*  
> 2.4 Ground Control & Communications, Table 5: "Table 5: STK access report, ZYZZsat to Mount Pleasant Radio Observatory (elevation above 0°)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Executive Summary; 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction, Number of spacecraft |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction, Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit, Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit, Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit, Figure 1 (STK 11) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Bibliography |

## Technical issues

- 2.2 Launch: A retrograde orbit (i = 97.79°) requires a launch heading with a westward component relative to the eastward direction. Describing it as launched 'slightly west of north' with β = −7.8° is inconsistent and the azimuth convention is unclear.
- 2.4 Ground Control & Communications: Contact-time fraction is inconsistent: 510 s of 771 s is about 66%, not 60%, and 6 passes × 510 s would give about 51 min, not the 34 min used in Table 6.
- Table 6: Daily data budget: Daily imaging assumes one 60 km × 1,000 km strip per day, which conflicts with about 14.9 orbits per day and six passes; the imaged area and raw data volume are not clearly derived from the orbit and access results.
- 2.4 Ground Control & Communications: The downlink margin of 3.5 is computed without a link budget; the claim that all images reach the ground in a day is therefore unsupported.
- 2.2 Launch: Claim that Mount Pleasant is at a 'similar latitude' commercial alternative and that Vega C launch-readiness timing is fixed are asserted without sourcing.

## Next steps

1. Restate the launch azimuth for your retrograde orbit (i = 97.79°) using a consistent convention, and check β against the sin β = cos i / cos φ relation you cite.
2. Recalculate the contact fraction (510 s of 771 s is about 66%) and the daily contact time (6 × 510 s is about 51 min), then align Table 6 with these values.
3. Derive the imaged area and raw data volume from your orbit and access results, and add a link budget for the X-band downlink before claiming all images reach the ground in a day.

---
<sub>Run Input_2_u-Run_1-Eff_low-261118-133509 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21060/9748 | cost $0.007034 (incl. $0.001387 for the reused reference rubric+task structure) | 55.43s</sub>
