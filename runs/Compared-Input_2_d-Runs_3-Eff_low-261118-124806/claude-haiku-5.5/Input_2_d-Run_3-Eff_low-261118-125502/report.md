# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 41 / 100 (41%)**

You have a clear mission concept, with the primary mission, the need for it and the single-spacecraft choice explained. The main gaps are technical accuracy in the Launch and Orbit sections, incomplete identification of users, and weak EOL and ground-station content. Your sourcing also needs to meet the requirement to avoid Wikipedia.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

Your introduction clearly states the primary mission, why it is needed and why one spacecraft is sufficient. To reach Accomplished, name the operator and customers explicitly rather than implying them through ground facilities, and support your rationale with stronger, properly cited literature instead of web links.

*Assessor reasoning:* Mission purpose, rationale and single-spacecraft choice are given with some background. Users (operator and customers) are only implied via 'operated and accessed from Australia ground facilities'; no explicit operator/customer identification. Referencing is largely web links, some Wikipedia-sourced, weakening support.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "Hundreds of millions of humans rely on reefs for food, natural protection, jobs, and tourism."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

Your design covers launch, orbit, ground access with STK evidence, and EOL, supported by ground-track figures. Accuracy is the main barrier: correct the Kourou latitude and its equatorial-launch reasoning, justify the 27.33° RAAN, and give the epoch for the argument of latitude. Verify the Mount Pleasant description and justify choosing the Vega E. Quantify uncontrolled deorbit at 600 km.

*Assessor reasoning:* Covers launch, orbit, COE table, ground station and STK access, EOL. However, the launch site latitude (45.05°N) is wrong for Kourou (about 5°N), the 'equator' rationale is inconsistent, Vega E is unbuilt, RAAN of 27.33° is unjustified, and the 'Argument of Latitude' is set to 0 with no epoch. Access listing has duplicated numbering (13). Mount Pleasant is not a radio observatory with two telescopes as stated; EOL section lacks a clear decision and has a truncated sentence.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  

### C3 Conclusion (4/10, Adequate)

You reach some conclusions, including the launch risk and the benefit of a polar sun-synchronous orbit for consistent illumination. These are generic. To reach Accomplished, tie your conclusions directly to specific STK access results, contact durations and EOL analysis, and explain how they justify the final design.

*Assessor reasoning:* Conclusions summarise the design and note launch risk, but are generic and do not draw quantitative conclusions from the STK results or EOL analysis.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (8/20, Adequate)

The report is well structured, with clear headings and labelled STK figures. Marks are held back by the Wikipedia citation despite the prohibition, inconsistent reference style, typos, and a broken EOL sentence. Make the executive summary more concise, check spelling and grammar throughout, and ensure every in-text citation matches a consistent reference list.

*Assessor reasoning:* Clear headings and labelled STK figures, but Wikipedia is cited despite prohibition, reference style is inconsistent, there are typos and a broken sentence in EOL, and the executive summary is not concise, with a truncated drag-sail sentence.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary |
| R4 | State the launch site and launch vehicle. | partial | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Launch: Kourou latitude given as 45.05°N; actual is about 5.2°N, and the equatorial-launch argument is then inconsistent.
- Orbit: Ω = 27.33° is said to indicate the launch facility location, which is not justified for a sun-synchronous RAAN, and the 1°/day precession claim is misstated (sun-synchronous precession is about 0.9856°/day, not 360°/year as a requirement phrased that way).
- Orbit: Retrograde orbit claim 'passes over almost the entire Earth' and 'frequent orbital period' are vague; no period or revs/day given.
- Mission Duration & EOL: Drag sail alternative sentence is truncated; uncontrolled deorbit at 600 km would not burn up fully and is not evaluated quantitatively.
- Ground Control & Communications: Mount Pleasant described as having two radio telescopes with receivers; claim unsupported and ground station selection reasoning contradicts 'close to poles' rule.

## Next steps

1. Correct the Kourou launch-site latitude (about 5.2°N) and revise your equatorial-launch argument so the launch choice is consistent.
2. In the Orbit section, justify the 27.33° RAAN, state sun-synchronous precession as about 0.9856°/day, and give the orbital period and revolutions per day for the retrograde orbit.
3. Replace Wikipedia sources with authoritative references, complete the truncated drag-sail EOL sentence, and state a clear EOL decision supported by quantitative reasoning.

---
<sub>Run Input_2_d-Run_3-Eff_low-261118-125502 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 20921/6005 | cost $0.005148 (incl. $0.001387 for the reused reference rubric+task structure) | 41.54s</sub>
