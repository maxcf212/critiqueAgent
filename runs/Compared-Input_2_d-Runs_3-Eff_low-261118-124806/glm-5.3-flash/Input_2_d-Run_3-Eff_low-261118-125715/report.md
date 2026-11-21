# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 59 / 100 (59%)**

A well-structured report on a coral-reef monitoring mission that addresses nearly all requirements with good STK evidence. However, the inclination value (87.79° vs ~97.8° for SSO at 600 km), the Kourou latitude error, internal contradictions about thrusters, and weak referencing (bare URLs, Wikipedia) hold the design back from the top rubric levels.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Accomplished (7/10). Your Introduction clearly presents the mission (Great Barrier Reef monitoring), the rationale, the single-spacecraft justification and the users. To reach the top of the range, define the operator and customer segments more explicitly and deepen the referenced background discussion.

*Assessor reasoning:* Mission, rationale, single-spacecraft justification and users (marine/conservation scientists, Australian operators) are all addressed with referenced background. Users could be more explicitly defined, so not top of range.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Adequate (6/10). You addressed all major requirements with STK screenshots, access reports and ground tracks, which is good evidence. However, the inclination (87.79° vs ~97.8° for SSO at 600 km), the Kourou latitude (~5.2°N, not 45.05°N), and contradictory thruster statements are significant technical errors. The Accomplished level requires accurate, internally consistent design supported by quality evidence.

*Assessor reasoning:* All major requirements addressed with STK evidence (screenshots, access report, ground tracks). However inclination is wrong (SSO at 600 km needs ~97.8°, not 87.79°, contradicting 'retrograde'), Kourou latitude misstated (~5°N), and thruster statements contradict. Good breadth, technical errors prevent Accomplished.
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924°"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods"  
> Launch: "latitude of 45.05°N" *(quote not found in submission)*  

### C3 Conclusion (6/10, Adequate)

Adequate (6/10). Your Conclusion summarises each segment and notes risks such as Vega E availability, but it largely recaps the report. The Accomplished level requires detailed conclusions drawn from your evidence — include quantitative outcomes and a critical evaluation of trade-offs.

*Assessor reasoning:* Conclusions summarise each segment and note risks (Vega E availability), but remain largely a recap without quantitative outcomes or critical evaluation.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

Adequate (5/10). Your report has a clear structure, executive summary and labelled figures. To reach Accomplished: format references properly (no bare URLs, no Wikipedia), fix typos ('nurture', 'complied'), and make figure captions and formatting consistent throughout.

*Assessor reasoning:* Clear structure with headings, executive summary and labelled figures. But references are bare URLs, Wikipedia used (explicitly disallowed), some grammar/typo issues ('nurture', 'complied'), and figure captions inconsistent.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit / Ground Control |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: Sun-synchronous inclination at 600 km should be ~97.8° (retrograde); report states 87.79°, contradicting its own plot and 'retrograde' claim.
- Launch: Kourou's latitude is ~5.2°N, not 45.05°N as stated.
- Orbit: 'A very high altitude would yield low resolution images which is also desirable' – contradicts the resolution requirement.
- Mission Duration & EOL: Contradictory statements: satellite 'without thrusters' yet discusses manoeuvre options, then says 'without thrust capability'.
- Bibliography: Wikipedia cited despite being disallowed; references are unformatted bare URLs.

## Next steps

1. Correct the sun-synchronous inclination: at 600 km an SSO requires ~97.8° (retrograde); verify against your own STK plot and ground tracks.
2. Fix the Kourou latitude (~5.2°N, not 45.05°N) and re-check any launch-vehicle performance implications that depend on it.
3. Resolve contradictions: state clearly whether the spacecraft has thrusters, and align manoeuvre/EOL discussion with that; also fix the statement that high altitude/low resolution is 'desirable'.
4. Replace Wikipedia and bare URLs with properly formatted citations to primary/technical sources, and ensure every in-text citation matches the reference list.
5. Strengthen the Conclusion with quantitative outcomes (orbit elements, access statistics, mission lifetime) and a brief critical evaluation of design trade-offs.

---
<sub>Run Input_2_d-Run_3-Eff_low-261118-125715 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 25804/5483 | cost $0.003113 (incl. $0.001387 for the reused reference rubric+task structure) | 86.42s</sub>
