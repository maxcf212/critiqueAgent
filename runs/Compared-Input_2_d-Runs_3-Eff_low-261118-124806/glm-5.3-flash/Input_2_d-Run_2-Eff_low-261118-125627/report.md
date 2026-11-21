# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 53 / 100 (53%)**

A well-structured report addressing nearly all requirements with good STK evidence (screenshots, access reports, ground tracks). However, a fundamental orbital-mechanics error (SSO inclination), a factual launch-site error, weak referencing, and vague user identification hold the mark at Adequate. Fixing these specific issues would lift the design work substantially.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly state the primary mission, justify its need for Australian coral-bleaching monitoring, and give a solid single-spacecraft rationale (simplicity, cost, communications). To reach Accomplished, explicitly identify the operator and the customers — 'operated and accessed from Australian ground facilities' is too vague; name who owns, runs, and buys the data, with supporting references.

*Assessor reasoning:* Mission, rationale and single-spacecraft justification are well covered with references. However, users (operator and customers) are only vaguely implied ('operated and accessed from Australia ground facilities'); no explicit operator/customer identification.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost"  
> Introduction: "would allow marine and conservation scientists to more accurately predict and react to coral bleaching events"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

All major requirements are addressed with good STK evidence, including a ~20-minute average contact duration and clear launch/EOL discussion. However, key errors undermine persuasiveness: the SSO inclination at 600 km should be ~97.8° (retrograde), not 87.79°, contradicting your own plot; Kourou's latitude is ~5.2°N, not 45.05°N, invalidating your launch-window reasoning; RAAN does not directly indicate launch-site location; and 'low resolution... is also desirable' contradicts your imaging goal. Also resolve the thruster-vs-EOL-manoeuvre contradiction. Correcting these and tightening the design logic would move you to Accomplished.

*Assessor reasoning:* All major requirements addressed with STK evidence (screenshots, access report, ground tracks). But critical errors: SSO inclination at 600 km should be ~97.8° (retrograde), not 87.79°, contradicting their own plot; Kourou latitude stated as 45.05°N (actually ~5°N); contradictory swath/resolution discussion. Design logic otherwise sound.
> Orbit: "an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $"  
> Launch: "situated very close to the equator, with a latitude of $ 45.05^{\circ} $N"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  

### C3 Conclusion (7/10, Accomplished)

Your conclusions are specific and evidence-based, including honest risk acknowledgement (Vega E not yet built) and fallback options — well done. To strengthen further, extend the same specificity to the other mission segments (orbit, ground segment) rather than focusing mainly on launch risk.

*Assessor reasoning:* Conclusions are specific and tied to report evidence, including risk acknowledgement (Vega E availability) and fallback options. Not fully detailed on all segments, so lower end of Accomplished.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet"  

### C4 Report presentation (10/20, Adequate)

The report has clear structure, headings, contents, and labelled figures. To reach Accomplished: replace bare URLs and Wikipedia (not permitted) with full citations (author, title, year) matched to in-text references; fix garbled sentences such as the low-resolution contradiction; and make figure captions and formatting consistent throughout.

*Assessor reasoning:* Clear structure with headings and contents; figures labelled. But references are bare URLs without titles/authors, Wikipedia used (explicitly disallowed), some garbled sentences ('which is also desirable' for low resolution), and figure captions inconsistent.
> Bibliography: "[1] https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification. [Online]."  
> Introduction: "https://en.wikipedia.org/wiki/2021_in_spaceflight"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: Sun-synchronous inclination at 600 km should be ~97.8° (retrograde, >90°), not 87.79°; contradicts their own inclination-vs-altitude plot and the stated 'retrograde' orbit.
- Launch: Kourou's latitude stated as 45.05°N; it is ~5.2°N. The claim that two launch windows occur daily because latitude is smaller than target inclination is built on this error.
- Orbit: RAAN of 27.33° said to 'indicate the location of the launch facility' — RAAN is not directly set by launch site longitude without further argument.
- Orbit: Contradictory statement: 'A very high altitude would yield low resolution images which is also desirable' — low resolution is not desirable.
- Mission Duration & EOL: Contradictory: satellite described as 'without thrusters' yet earlier an orbital manoeuvre at EOL is mentioned; drag sail choice is consistent but reasoning is muddled.

## Next steps

1. Correct the sun-synchronous inclination at 600 km to ~97.8° (retrograde, >90°) and reconcile it with your own inclination-vs-altitude plot and orbit description.
2. Fix the Kourou latitude (~5.2°N, not 45.05°N) and rebuild the launch-window argument on the corrected value; clarify how RAAN relates to launch site longitude.
3. Replace bare URLs and Wikipedia with proper citations (author, title, year) and ensure every in-text citation matches the reference list; explicitly name the operator and customer groups in the Introduction.

---
<sub>Run Input_2_d-Run_2-Eff_low-261118-125627 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15178/4130 | cost $0.003238 (incl. $0.001387 for the reused reference rubric+task structure) | 47.63s</sub>
