# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 66 / 100 (66%)**

A well-evidenced mission design for GBR coral monitoring covering all major requirements, with good STK support and a clear structure. To reach higher marks, resolve internal contradictions (resolution vs altitude, EOL thruster logic), replace Wikipedia with proper sources, complete your reference formatting, and add critical evaluation to the conclusion.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

Accomplished (8/10). You addressed all required elements: mission concept (GBR coral monitoring via fluid lensing), rationale, single-spacecraft justification, and users/operator/funding (CSIRO, BOM), supported with literature. To reach the top band, deepen some claims with more specific detail and additional references.

*Assessor reasoning:* Mission (GBR coral monitoring via fluid lensing), rationale, single-spacecraft justification and users/operator/funding all addressed with literature references. Detail is good though some claims lack depth.
> Introduction: "Thus, only one satellite is required"  
> Introduction: "likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

Accomplished (7/10). You covered launch (Vega E from Kourou), a full COE table with J2 sun-synchronous reasoning, STK access analysis, ground stations, duration and EOL. The 'Accomplished' top level requires error-free, persuasive content: resolve the altitude/resolution contradiction, the thruster/EOL confusion, the vague contact-duration claim, and include STK files as evidence.

*Assessor reasoning:* Launch (Vega E, Kourou), full COE table, J2 sun-sync reasoning, STK access report, ground station choice, duration and EOL all covered with evidence. Weakened by internal contradictions (e.g. 'low resolution images which is also desirable', thruster confusion) and no explicit STK files in appendix.
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods"  
> Mission Duration & EOL: "A span of five years is a sound estimate"  

### C3 Conclusion (6/10, Adequate)

Adequate (6/10). Your conclusion summarises each segment and notes risks (Vega E availability), but is largely a recap. The 'Accomplished' level requires detailed conclusions drawn from your evidence: include quantitative outcomes (orbit parameters, access statistics, margin) and critical evaluation of design trade-offs.

*Assessor reasoning:* Conclusion summarises each segment and notes risks (Vega E availability), but is largely a recap without critical evaluation or quantitative outcomes.
> Conclusion: "a fully described satellite configuration has been constructed"  

### C4 Report presentation (10/20, Adequate)

Adequate (5/10). Your structure and headings are clear, but the bibliography uses bare URLs and Wikipedia (explicitly disallowed), figures lack consistent numbering/captions, and there are grammar slips ('the purposed of', 'current owned'). The 'Accomplished' level requires consistent formatting, polished writing, and properly cited, complete references.

*Assessor reasoning:* Clear structure and headings, but bibliography is bare URLs (no titles/authors/dates), Wikipedia used despite being disallowed, figures lack consistent numbering/captions, and minor grammar slips ('the purposed of', 'current owned').
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Ground Control & Communications: "DN path for orbits 1-15"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design - Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit (COE table) |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit / EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit / Ground Control (STK) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit, Ground Control (screenshots present; STK files not evidenced) |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography (Wikipedia cited; bare URLs) |

## Technical issues

- Orbit: Statement 'A very high altitude would yield low resolution images which is also desirable' contradicts the resolution requirement.
- Mission Duration & EOL: Confused reasoning: first says uncontrolled descent chosen, then says satellite is 'without thrust capability' so must use passive drag sail; also graveyard orbit discussion irrelevant for LEO smallsat.
- Bibliography: Wikipedia cited despite task explicitly disallowing it; references lack titles, authors and access dates.
- Ground Control & Communications: Claim that inclination 'maintains a significant contact for the vast majority of passes' is vague and unsupported.

## Next steps

1. Fix the contradiction in the Orbit section where 'low resolution images which is also desirable' conflicts with your resolution requirement, and clarify the EOL reasoning (uncontrolled descent vs 'without thrust capability' vs drag sail; remove the irrelevant graveyard-orbit discussion for a LEO smallsat).
2. Replace the Wikipedia citation, expand all bare-URL references with titles, authors and access dates, and ensure every in-text citation matches the reference list.
3. Add your STK scenario files to the appendix, support the ground-contact claim ('vast majority of passes') with quantitative access data, and strengthen the conclusion with quantitative outcomes and critical evaluation rather than a recap.

---
<sub>Run Input_2-Run_3-Eff_low-261118-113701 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15087/3900 | cost $0.002372 (incl. $0.001387 for the reused reference rubric+task structure) | 42.23s</sub>
