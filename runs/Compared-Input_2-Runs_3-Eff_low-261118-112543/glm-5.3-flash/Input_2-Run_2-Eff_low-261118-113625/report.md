# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 66 / 100 (66%)**

A well-structured, mostly complete mission design for GBR coral monitoring with good STK evidence and justified launch/orbit/ground-segment choices. To reach the top band, resolve internal contradictions in the orbit and EOL reasoning, show the hand calculations behind your inclination plot, explain the RAAN, and fix referencing (no Wikipedia, full bibliography entries).

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

Accomplished (8/10). Your Introduction clearly covers the mission (GBR coral monitoring via fluid lensing), rationale, single-spacecraft justification, and users/operator/funding with literature support. To reach the very top, add more depth on customer specifics and operational needs.

*Assessor reasoning:* Mission (GBR coral monitoring via fluid lensing), rationale, single-spacecraft justification, and users/operator/funding all addressed with literature references. Some depth lacking on customer specifics, but overall high standard.
> Introduction: "Thus, only one satellite is required"  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

Accomplished (7/10). Strong coverage: Vega E from Kourou justified, orbit elements tabulated, STK screenshots and access reports included, contact frequency quantified, duration and EOL addressed. Next level requires error-free reasoning: fix the resolution contradiction, the circular drag-sail logic, the unexplained RAAN, and include the hand calculation behind the inclination plot.

*Assessor reasoning:* Launch site/vehicle (Vega E from Kourou) justified, orbit elements tabulated, STK screenshots and access reports included, ground station and contact frequency quantified, duration and EOL (drag sail) covered. Minor errors: contradictory resolution statement, muddled drag-sail rationale, RAAN value unexplained, inclination plot lacks shown hand calculation.
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods"  
> Mission Duration & EOL: "A span of five years is a sound estimate"  

### C3 Conclusion (6/10, Adequate)

Adequate (6/10). Your Conclusion summarises key choices and notes Vega E availability risk, but is largely a recap. Higher marks require deeper critical evaluation and quantitative outcomes drawn from your evidence.

*Assessor reasoning:* Conclusion summarises key design choices (launch, orbit, ground station, EOL) and notes risks (Vega E availability), but is largely a recap without deeper critical evaluation or quantitative outcomes.
> Conclusion: "a fully described satellite configuration has been constructed"  

### C4 Report presentation (10/20, Adequate)

Adequate (5/10). Clear structure, labelled figures/tables and an executive summary are strengths. To reach Accomplished: use a consistent referencing style (no Wikipedia, no bare URLs), fix stray characters/typos, and make figure captions consistent.

*Assessor reasoning:* Clear structure with headings, labelled figures and tables, executive summary present. However bibliography is bare URLs (no titles/dates), Wikipedia cited despite being disallowed, stray characters/typos, and figure captions are inconsistent (some text-only captions).
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Ground Control & Communications: "the Mount Pleasant Radio Observatory)."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design - Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit / Ground Control (STK use) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Images 1-5 and access table present; no explicit appendix listing STK files |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Structure clear, but Wikipedia cited and bibliography poorly formatted |

## Technical issues

- Orbit: Statement 'A very high altitude would yield low resolution images which is also desirable' contradicts the design logic (low resolution is undesirable).
- Mission Duration & EOL: Confused reasoning: first says uncontrolled descent makes sense, then says satellite is 'without thrust capability' so must use passive strategy; drag sail deployment itself implies some mechanism, and the logic is circular.
- Orbit: RAAN of 27.33° claimed to indicate launch facility location, but Kourou is at ~5°N; RAAN is not set by launch-site latitude, and no LTAN/local time of descending node is given for the SSO.
- Orbit: Inclination-altitude plot presented without the underlying hand calculation or equation (J2 nodal precession formula).
- Ground Control & Communications: Claim that contact duration is 'ensured by the proposed satellite's orbital inclination, which – because of its verticality' is loosely worded; also duplicate access number 13 in STK table.

## Next steps

1. Correct the contradictory statement that low-resolution images are 'desirable', and rework the EOL section so the drag-sail rationale is logically consistent (e.g. explain the sail as a passive deorbit mechanism deployed once, not implying thrust).
2. Show the J2 nodal precession equation and hand calculation behind your inclination-altitude plot, state the LTAN/local time of descending node for your SSO, and correct or remove the claim that RAAN 27.33° reflects Kourou's latitude.
3. Replace Wikipedia and bare URLs with proper references (author, title, date, source), and make in-text citations match the bibliography exactly.
4. Deepen the Conclusion beyond a recap: add quantitative outcomes (contact statistics, mass/power margins) and a critical evaluation of risks and design trade-offs.

---
<sub>Run Input_2-Run_2-Eff_low-261118-113625 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15202/3829 | cost $0.002362 (incl. $0.001387 for the reused reference rubric+task structure) | 36.48s</sub>
