# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 90 / 100 (90%)**

You present a strong, coherent ZYZZsat mission design: all required elements are addressed, STK evidence and hand calculations support the orbital, coverage, data-budget and decay work, and the report is well structured. The main gaps are the absent full X-band link budget and the assumed Mount Pleasant ground-station fit-out; launch dispersion and revisit claims are minor uncertainties.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 9 / 10 | 18 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

In Section 1 you clearly state the primary mission, need, single-spacecraft rationale and AIMS operator/customers, with an Australia focus and references. To secure full marks within Accomplished, strengthen the evidence base with more scholarly/peer-reviewed sources and explicitly link each rationale point to a design requirement or performance driver.

*Assessor reasoning:* All required introduction elements are present: mission, rationale, single-spacecraft justification, and operator/customers. It is detailed, Australia-focused and well referenced, though some sources are non-scholarly.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Sections 2.2–2.5 give a comprehensive design with STK screenshots/files and sound orbital and decay checks. For full marks, add a complete X-band link budget, substantiate the Mount Pleasant S/X-band fit-out, replace the fixed 60% contact-time assumption in Table 6 with elevation-dependent pass scheduling, and address Vega C/rideshare dispersion and the 'any reef within five days' revisit claim more rigorously.

*Assessor reasoning:* Comprehensive mission design: launch choice, SSO elements, coverage, ground station, data budget, duration and EOL are supported by STK evidence and hand checks. Orbital and decay calculations are sound. Missing link budget and assumed ground-segment fit-out prevent full marks.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "No orbital manoeuvres are required."  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC), and the mean pass lasts 580.8 s"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission."  
> Appendix A: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  
> Image 1  

### C3 Conclusion (9/10, Accomplished)

Your conclusion follows the evidence, summarises key performance values and identifies four limitations. To reach full marks, link each limitation explicitly to the affected design decision or requirement and quantify its impact where possible, so the reader can see priorities for future work.

*Assessor reasoning:* Conclusions follow directly from design evidence, summarise key performance values, and identify concrete limitations and next steps. Detailed and appropriate.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "The design has four limitations."  

### C4 Report presentation (18/20, Accomplished)

The report has a clear engineering structure, a concise executive summary, labelled figures/tables and citations that match the bibliography. For full marks, polish the remaining presentation/reference-quality issues—ensure all sources are appropriate and formatting is fully consistent throughout—so the document reads at a professional standard.

*Assessor reasoning:* Clear engineering-report structure, concise executive summary, readable prose, labelled figures/tables and consistent citation style. In-text citations match the bibliography. Minor presentation/reference-quality issues only.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite for monitoring coral bleaching on the Great Barrier Reef."  
> Table 1: "Table 1: ZYZZsat spacecraft summary."  
> Appendix A: "Appendix A: STK files and settings"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction / Primary mission |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction / Number of spacecraft |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction / Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch / Table 2 |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit / Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit / Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications / Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit / Image 1 / Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A / Figures 1–4 / Table 5 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents / Bibliography |

## Technical issues

- 2.4 Ground Control & Communications: No full X-band link budget is presented; downlink feasibility is supported only by a simplified data-capacity calculation.
- 2.4 Ground Control & Communications: The design assumes S-band and X-band equipment can be added to the Mount Pleasant 12 m antenna, but this is not established.
- 2.4 / Table 6: Usable contact time is approximated as a fixed 60% of pass duration; actual elevation-dependent link capacity and pass scheduling are not modelled.
- 2.2 Launch: Vega C was unflown at the report date, and rideshare injection dispersion may not deliver exactly 600 km and 97.79° without propulsion.
- 2.3 Orbit / Table 3: The 'any reef within five days' claim uses equatorial track spacing and roll access; it is not a rigorous latitude/daylight/cloud coverage analysis.

## Next steps

1. Add a complete X-band link budget in Section 2.4 (EIRP, G/T, path loss, modulation/coding, Eb/N0 margin) and substantiate whether the Mount Pleasant 12 m antenna can support the assumed S/X-band fit-out, or propose a verified alternative.
2. Replace the fixed 60% usable-contact-time assumption in Table 6 with elevation-dependent pass modelling and scheduling, and use it to quantify realistic data throughput and latency.
3. Strengthen the launch and revisit arguments: justify Vega C/rideshare injection dispersion to 600 km and 97.79° without propulsion, and support the 'any reef within five days' claim with latitude, daylight and cloud coverage analysis.

---
<sub>Run Input_2_u-Run_2-Eff_high-261116-124949 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14265/11814 | cost $0.007328 (incl. $0.001387 for the reused reference rubric+task structure) | 102.64s</sub>
