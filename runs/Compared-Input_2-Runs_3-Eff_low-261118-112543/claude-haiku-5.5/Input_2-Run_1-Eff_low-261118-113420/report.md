# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You have built a coherent sun-synchronous Earth-observation concept, and your STK access results and ground track give useful software evidence. Your introduction clearly explains the mission and the single-satellite choice. The report is currently at Adequate overall. Correcting the orbital elements, completing the end-of-life plan, and strengthening references and presentation will move it towards Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly state the primary mission, why it is needed, the single-satellite choice, and government and science users such as CSIRO and BOM. To reach Accomplished, name the operator explicitly, separate operator from customers, and support claims with stronger literature. Remove weakly sourced statements, such as the 30% acidity claim, unless you can reference them properly.

*Assessor reasoning:* Mission, rationale, single-satellite choice and users are addressed, but user/operator identification is vague and not clearly separated. Rationale is well argued but some references are weak (Wikipedia-sourced claims, unsupported 30% acidity statement). Operator not explicitly named.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost"  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your orbit analysis, STK access results and ground track provide good software evidence. The orbital elements contain errors, the Vega E choice and launch-site logic need clearer justification, and the end-of-life section is incomplete. Give delta-v for any maneuvers, and justify ground stations in line with your Australian focus. Accomplished work needs accurate, fully justified decisions supported by quantitative evidence throughout.

*Assessor reasoning:* Orbit, COE table, STK access and ground track are provided, but the COE table has errors (semi-major axis, RAAN explanation, argument of latitude misdefined as zero). Launch vehicle Vega E is not yet built and launch-site latitude/equator logic is inconsistent. EOL section is incomplete (drag sail sentence truncated) and contradicts the no-thrust claim. Maneuvers stated as only EOL but no delta-v given. Ground control facility is selected but only one station, and the stated 'Tasmanian facility' contradicts later Australia-focused claims.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Mission Duration & EOL: "However, the ZYZZsat is without thrust capability and so must use a ‘passive’ strategy."  

### C3 Conclusion (4/10, Adequate)

You reach sensible conclusions, such as the illumination benefit of a polar sun-synchronous orbit, and you acknowledge launch uncertainty. These largely restate the design. Add quantified outcomes, critically weigh trade-offs such as a single satellite against a constellation, and assess end-of-life risk to reach a detailed, evidence-based conclusion.

*Assessor reasoning:* Conclusion summarises the design and notes launch uncertainty, but largely restates content without quantified outcomes or critical evaluation of trade-offs and EOL risks.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

Your clear headings and labelled figures give the report a logical structure. Improve consistency by correcting the duplicated table entry and contents page errors, fixing typos and grammar, completing truncated sentences, and using one citation style with access dates for web sources. Replacing the Wikipedia reference will also help meet the brief.

*Assessor reasoning:* Clear headings and figure labels, but mixed formatting, table with duplicated/mislabelled access numbers (13 repeated), typos and grammar errors, truncated sentences, and a Wikipedia source breaching the brief. Reference style is inconsistent and cites web links without dates.
> Contents: "Executive Summary ..... 2"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | partial | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Orbit: Argument of latitude is stated as 0° while also described as undefined; RAAN of 27.33° is attributed to launch site without justification; sun-synchronous RAAN rate described as 360° per year is correct but phrasing of 1°/day should be stated as 0.9856°/day.
- Launch: Kourou latitude (~5.2°N) is cited to justify maximising launch efficiency, but a 97.8° inclination orbit is retrograde; the claim that the launch window count depends on latitude versus inclination is muddled.
- Mission Duration & EOL: Claims uncontrolled descent needs least energy yet notes no thrust; drag sail discussion is truncated and no quantitative decay/ballistic analysis given for 600 km altitude.
- Ground Control & Communications: Claims near-polar ground station maximises passes, but contact durations and pass counts are inconsistent with the 15-access table (access 13 duplicated).

## Next steps

1. Correct the classical orbital elements table: define the argument of latitude properly rather than stating 0° while calling it undefined, justify the RAAN from the launch site, and state the sun-synchronous precession as 0.9856°/day.
2. Complete the end-of-life section by finishing the truncated drag-sail sentence and adding a quantitative decay estimate for 600 km that reconciles it with the no-thrust constraint. Replace the Wikipedia source with authoritative references and cite them consistently.
3. Resolve the launch and ground-station inconsistencies: explain the launch-site latitude against the 97.8° retrograde inclination, name the operator explicitly, and make pass counts and contact durations match the access table, removing the duplicated access 13.

---
<sub>Run Input_2-Run_1-Eff_low-261118-113420 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21049/6030 | cost $0.005173 (incl. $0.001387 for the reused reference rubric+task structure) | 29.9s</sub>
