# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 88 / 100 (88%)**

You produced a strong, concise mission design that meets all requirements. STK and hand calculations support launch, orbit, coverage, downlink and EOL. Your Introduction and Conclusion are clear and well referenced. Main improvements: strengthen the revisit calculation, add an X-band link budget, address Vega C/rideshare and ground-station assumptions, and polish bibliography formatting.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

Your Introduction clearly states the GBR imaging mission, direct-detection rationale, single-spacecraft choice, AIMS operator and customers, with references. This is Accomplished. To secure the top of the band, tighten the link between customer needs and the 5 m visible requirement and ensure every rationale claim has a specific citation.

*Assessor reasoning:* Mission need, direct-detection rationale, single-spacecraft choice, operator and customers are all clearly explained with appropriate references. Strong introduction.
> 1 Introduction / Primary mission: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction / Number of spacecraft: "One satellite is therefore used."  
> 1 Introduction / Users: "The operator is the Australian Institute of Marine Science (AIMS)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Your §2.2–2.5 and Appendix A give strong evidence for launch, orbit, coverage, communications, manoeuvres and EOL. To strengthen within Accomplished, add an STK coverage/revisit analysis for Table 3, an X-band link budget for Table 6’s 50 Mbit/s and 34 min contact, and evidence/risk treatment for Vega C unflown status, rideshare dispersion without propulsion, and Mount Pleasant S/X-band capability.

*Assessor reasoning:* Launch, orbit elements, coverage, communications, manoeuvres, duration and EOL are comprehensively addressed with STK screenshots, tables and hand calculations. Minor weaknesses in revisit estimate and link budget do not prevent Accomplished.
> 2.3 Orbit: "The most suitable orbit is a low-Earth sun-synchronous orbit"  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  
> 2.5 Mission Duration & EOL: "The mission lasts five years."  

### C3 Conclusion (9/10, Accomplished)

Your Conclusion is specific and evidence-based: it restates one 50 kg satellite meeting the need and candidly lists four limitations. This is Accomplished. To reach the top of the band, tie each limitation to a concrete risk or next design step and avoid introducing any new material not already supported in the main body.

*Assessor reasoning:* Conclusion summarises specific achieved performance and candidly identifies limitations and next steps. Detailed and evidence-based.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "The design has four limitations."  

### C4 Report presentation (16/20, Accomplished)

Your report has a clear engineering structure, concise Executive Summary, labelled figures/tables and matching citations. At 8/10 in Accomplished, the main gap is bibliography quality: several entries are incomplete or weakly formatted. To move toward the top of the band, standardise all references and check every in-text citation matches the list exactly.

*Assessor reasoning:* Clear engineering-report structure, concise writing, labelled figures/tables and matching citations. Some bibliography entries are incomplete or weakly formatted, so not top of range.
> Executive Summary: "This report presents the design of ZYZZsat"  
> Appendix A: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction / Primary mission |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction / Number of spacecraft |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction / Users |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit / Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit / Manoeuvres |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit / 2.4 / Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Report structure / Bibliography |

## Technical issues

- 2.3 Orbit, Table 3: Revisit-time calculation is a simple division of track spacing by roll-access width and is not demonstrated with an STK coverage/revisit analysis; it may be conservative or ambiguous.
- 2.4 Ground Control & Communications, Table 6: No X-band link budget is presented; the 50 Mbit/s downlink and 34 min usable contact give an unverified 3.5 data margin.
- 2.2 Launch / 2.3 Orbit: Baseline Vega C was unflown at the report date, and rideshare injection dispersion cannot be corrected without propulsion; the delivered orbit may differ from 600 km and 97.79°.
- 2.4 Ground Control & Communications: Mount Pleasant is a radio astronomy/geodesy site; adding S-band and X-band capability is assumed without supporting evidence.

## Next steps

1. In §2.3/Table 3, replace or support the track-spacing/roll-width revisit estimate with an STK coverage/revisit analysis, stating assumptions and reporting revisit statistics.
2. In §2.4/Table 6, add an X-band link budget (EIRP, path loss, G/T, modulation/coding, margin) to verify the 50 Mbit/s downlink and 34 min usable contact.
3. In §2.2–2.4, add a risk/evidence note for the unflown Vega C baseline and rideshare dispersion without propulsion, and provide evidence or mitigation for assuming S/X-band at Mount Pleasant; also standardise bibliography entries.

---
<sub>Run Input_2_u-Run_2-Eff_low-261118-133125 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14083/14555 | cost $0.008954 (incl. $0.001387 for the reused reference rubric+task structure) | 64.11s</sub>
