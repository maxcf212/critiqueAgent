# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 48 / 100 (48%)**

You have produced a well-organised report that covers every mission segment and supports it with STK screenshots and an access table. Its main weaknesses are factual errors in the orbit and launch sections, a prohibited Wikipedia source, a mission duration that contradicts your STK run, and an unfinished end-of-life discussion. Correcting these would substantially improve accuracy and referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly state the primary mission, explain why one satellite is needed, and identify government and science users such as CSIRO and BOM. To reach the higher level, name the operator explicitly, make the customers more specific, and justify the single-satellite choice in greater depth. Replace the unreliable source in the introduction with well-referenced literature.

*Assessor reasoning:* Mission purpose, single-satellite choice and users are addressed with some rationale and references. Operator is not clearly identified, customers are vague, and rationale for one satellite is thin. Introduction contains a Wikipedia-sourced claim-level reference issue. Detail is adequate rather than high standard.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your report covers launch, orbit, ground control and EOL, supported by STK screenshots and an access table, which gives a solid base. Factual errors undermine the design, including the precession rate, the RAAN given as a launch location, and the contradictory launch-site logic. To reach the next level, correct these, justify the Vega E choice and the Tasmanian ground station with quantified access, and complete the EOL and manoeuvre analysis.

*Assessor reasoning:* Covers launch, orbit, ground station and EOL with STK screenshots and access table. However, Vega E is not built and launch-site logic is contradictory (equator claim, 5.05N latitude stated as close). RAAN 27.33 deg described as launch location is incorrect. The 360 deg/year precession statement is wrong (it should be about 0.9856 deg/day), ground station selection reasoning is weak, and the 'drag sail' and EOL plan are incomplete. Mission duration is contradictory (5 years vs 2030 STK run). Orbit uses 97.79 with 6971 km semi-major axis, which is consistent but the manoeuvre and EOL analysis is shallow.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "the ascending node experiencing a $ 1^{\circ} $ east-ward precession every day [8]."  
> Ground Control & Communications: "a Tasmanian facility is selected – the Mount Pleasant Radio Observatory)"  

### C3 Conclusion (4/10, Adequate)

You summarise the design and note launch vehicle risk, which is a useful start. However, the conclusion is generic and does not draw specific findings from your evidence. To reach the next level, state concrete conclusions about access performance, mission lifetime and EOL outcome, linking each back to a figure or table in your report.

*Assessor reasoning:* Conclusion summarises the design and notes launch vehicle risk, but is largely generic and does not draw specific evidenced conclusions about access performance or EOL outcome.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (8/20, Adequate)

Your report follows the required structure, with headings and labelled figures and tables. Presentation is held back by the Wikipedia citation despite the prohibition, bare URLs, a truncated drag-sail paragraph, and typos. Proofread carefully, format references consistently, and ensure every in-text citation matches the reference list.

*Assessor reasoning:* Structure follows the required headings with labelled figures and tables. However Wikipedia is cited despite prohibition, some references are bare URLs, sentences are broken (e.g. drag sail paragraph cut off), and there are typos and stray characters. Contents page is missing some sections, and it is not consistently formatted.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Design: "The Vega E launcher is an evolution of Vega C"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | partial | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | partial | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Orbit: Stated RAAN precession rate of 360 deg per year is incorrect; sun-synchronous precession is about 0.9856 deg per day (about 360 deg per year)
- Launch: Claims equatorial launch is best and that Kourou's 5.05N latitude is close to equator, yet inclination 97.8 deg means launch-window logic is not justified; RAAN 27.33 deg described as launch facility location is unexplained
- Mission Duration & EOL: Five-year lifespan conflicts with STK run to 2030 and with the claim that replacement is needed; drag-sail discussion is truncated
- Ground Control & Communications: Claims near-polar ground station maximises pass frequency but selects a Tasmanian site without quantifying access; access table notes 13 duplicated but numbering error
- Introduction: Reference [6] is Wikipedia, which the brief prohibits; several claims cite news or unreliable sources

## Next steps

1. Correct the RAAN precession rate in the Orbit section to about 0.9856 deg/day, and remove the claim that RAAN 27.33 deg is the launch location. Rework the Launch section so the equatorial-launch argument is consistent with the 5.05N latitude and 97.8 deg inclination.
2. Replace Wikipedia reference [6] and other news or unreliable sources with peer-reviewed or official agency sources. Complete the bibliography so that every in-text citation matches a reference and vice versa.
3. Reconcile the mission duration (five years versus the 2030 STK run) and finish the drag-sail and EOL discussion. Quantify access for the Tasmanian ground station before drawing your conclusions.

---
<sub>Run Input_2-Run_2-Eff_low-261118-113450 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21078/6035 | cost $0.005179 (incl. $0.001387 for the reused reference rubric+task structure) | 28.07s</sub>
