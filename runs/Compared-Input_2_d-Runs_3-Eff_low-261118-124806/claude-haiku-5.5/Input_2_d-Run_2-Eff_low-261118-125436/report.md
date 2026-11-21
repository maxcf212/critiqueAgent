# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 48 / 100 (48%)**

You have produced a clearly structured report with a coherent single-satellite sun-synchronous concept, supported by STK access tables, orbital elements and screenshots. The main weaknesses are factual and technical errors in the launch, orbit and ground-station sections, an unresolved launch vehicle and end-of-life (EOL) choice, and a non-academic reference. Correcting these would strengthen the design's credibility considerably.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You state the primary mission and the reason for using one satellite clearly, which is a strength. To reach the Accomplished level, explicitly name the operator and the customers (for example, the agencies and scientists who will use the data) rather than describing users only in general terms. Also support key claims, such as the reef-dependence statistic, with appropriate references.

*Assessor reasoning:* Mission purpose and single-satellite rationale are given, and users are only vaguely identified (no explicit operator or customers named beyond Australian monitoring scientists). Rationale is well motivated with references, but the users requirement is weakly addressed and some claims lack support.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "Hundreds of millions of humans rely on reefs for food, natural protection, jobs, and tourism."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit with a classical orbital elements table, STK access results, ground station and EOL, and you include screenshots, which is good. Accuracy is the main issue: the Kourou latitude is wrong, the RAAN explanation does not follow from the launch site, and the sunlight claim ignores eclipses. The manoeuvre plan and EOL choice are also unresolved. Correcting these and justifying the ground station choice more fully would move this towards Accomplished.

*Assessor reasoning:* Covers launch, orbit with COE table, STK access tables, ground station and EOL, with screenshots. However, launch site latitude 45.05N is wrong (Kourou ~5N), Vega E is not yet built and the launch-from-equator logic is contradictory, RAAN explanation is inconsistent, and the orbit is described as retrograde yet sun-synchronous claims lack checks. Manoeuvre and EOL plan are muddled, and the chosen EOL is unresolved. Results are present but accuracy issues reduce confidence.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "a Tasmanian facility is selected – the Mount Pleasant Radio Observatory)"  

### C3 Conclusion (4/10, Adequate)

Your conclusion summarises the segments and acknowledges launch risk, which is a reasonable start. However, it largely restates earlier content in generic terms, such as the claim about consistent illumination. To reach Accomplished, draw specific conclusions from your STK results, such as contact time and coverage, and state a clear EOL conclusion with supporting evidence.

*Assessor reasoning:* Conclusion summarises segments and notes launch risk, but largely restates content with generic statements and no quantitative outcome evaluation or EOL conclusion.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (8/20, Adequate)

Your report has clear headings, a contents list and numbered figures, which supports readability. Improve consistency by completing all figure captions and applying one citation style throughout. Replace the Wikipedia reference, which is not acceptable as a source, and make sure every in-text citation matches a reference list entry. Tightening the EOL section's wording would also help the reader.

*Assessor reasoning:* Clear headings and structure, with a contents list and numbered figures. However there are truncated sentences, a Wikipedia source explicitly disallowed, inconsistent citation style, figure captions incomplete, and a broken EOL sentence. Executive summary and language are reasonable but errors impede reading.
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’ – a drag-enhancing deorbit device that deploys at the EOL. It acts like a regular sail, utilising a large surface area to ‘ and is suitable"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | partial | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Launch: Kourou latitude given as 45.05°N; it is about 5.2°N, and the equator argument for launch efficiency is then inconsistent with the chosen site.
- Orbit: RAAN stated as 27.33° and described as the launch facility location, which does not follow from a launch-site longitude/latitude; also states RAAN rate of 360° per year as the sun-synchronous condition, which is incorrect (about 0.9856°/day eastward).
- Orbit: Says 'retrograde' and 'near-polar' with 'constant supply of sunlight' from the sun-synchronous orbit, but a 600 km SSO has eclipses; claim of constant sunlight is incorrect.
- Mission Duration & EOL: Says the satellite is 'without thrusters' yet a graveyard or drag-sail choice is unresolved; uncontrolled re-entry at 600 km is not justified against debris-risk requirements.
- Ground Control & Communications: Mount Pleasant is a Tasmanian radio observatory, not an ideal polar station; the statement that polar sites maximise passes for a 600 km SSO is only partly correct and the 20-minute average contact is from a 15-row subset.

## Next steps

1. Verify the launch site coordinates (Kourou is about 5.2°N, not 45.05°N) and rework the launch-efficiency argument so it is consistent with the chosen site and launch vehicle.
2. Correct the orbit description: the RAAN rate for sun-synchronous orbit is about 0.9856° per day eastward, and a 600 km sun-synchronous orbit does experience eclipses, so address power and thermal implications.
3. Replace the Wikipedia source with peer-reviewed or official references, make citation style consistent, complete the figure captions, and commit to a single EOL option (for example, a drag sail or a controlled disposal) justified against debris-mitigation requirements.

---
<sub>Run Input_2_d-Run_2-Eff_low-261118-125436 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21120/5535 | cost $0.004933 (incl. $0.001387 for the reused reference rubric+task structure) | 25.74s</sub>
