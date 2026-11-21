# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 52 / 100 (52%)**

Your report presents a well-structured GBR-monitoring mission with genuine STK evidence covering launch, SSO orbit, ground station and EOL. However, a critical inclination error (87.79° vs your own plot's ~97.9°), an incorrect Kourou latitude, a misread access statistic, and citation/labelling weaknesses held the design and presentation criteria at Adequate. Fixing these factual and presentation issues is your clearest path to Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your mission rationale (Great Barrier Reef monitoring) and single-spacecraft justification are well argued and referenced. To reach Accomplished, explicitly identify the operator (which organisation runs the spacecraft?) and the customer groups (e.g. reef researchers, agencies), rather than leaving users implied by 'accessed from Australian ground facilities'.

*Assessor reasoning:* Mission, rationale, and single-spacecraft choice are well covered with references. However, users are only vaguely identified: 'operated and accessed from Australia ground facilities' and implied scientists; no explicit operator entity or customer groups are named.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

All major requirements are addressed with STK screenshots and an access report, which is good practice. However, the stated 87.79° inclination contradicts your own plot (~97.9°) and your 'retrograde SSO' description; Kourou's latitude is ~5.2°N, not 45.05°N, affecting your launch-window logic; and 580.8 s is ~10 min, not 'almost twenty minutes'. Also mention your STK scenario files. Resolving these errors and inconsistencies is what the Accomplished level requires.

*Assessor reasoning:* All major requirements addressed with STK evidence (screenshots, access report, element table). But significant errors: stated 87.79° inclination contradicts own plot (~97.9°) and retrograde SSO claim; Kourou latitude is ~5°N not 45.05°N; mean access 580 s is ~10 min not 20; STK files not mentioned.
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous" *(quote not found in submission)*  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Launch: "it is situated very close to the equator, with a latitude of 45.05°N" *(quote not found in submission)*  

### C3 Conclusion (6/10, Adequate)

Your conclusions summarise each segment and sensibly flag the Vega E availability risk with a fallback. To reach Accomplished, add quantitative synthesis — e.g. revisit coverage vs reef-monitoring needs, data volumes vs contact time — rather than restating body content generically.

*Assessor reasoning:* Conclusions summarise each segment and acknowledge a programmatic risk (Vega E availability) with fallback. Somewhat generic and repeats body content without quantitative synthesis, but useful and evidence-based.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your structure is logical with a clear executive summary, but figures lack numbers, tables are unlabelled, references are bare URLs without titles or dates, and Wikipedia is disallowed. Grammar slips ('a Earth observation satellite', 'which is also desirable') also appear. Consistent figure/table numbering and proper referencing are required for the Accomplished level.

*Assessor reasoning:* Clear structure with executive summary and logical sections. However, figures lack figure numbers, tables are unnumbered, references are bare URLs with no titles/dates, Wikipedia is used (explicitly disallowed), and grammar slips occur ('a Earth observation satellite', 'which is also desirable').
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction — operator/customers only implied, not explicitly identified |
| R4 | State the launch site and launch vehicle. | yes | Launch — Vega E from Kourou (latitude value erroneous) |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit — elements given but inclination (87.79°) inconsistent with retrograde SSO and own plot (~97.9°) |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit — no manoeuvres except EOL disposal |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications — Mt Pleasant Observatory, STK access summary |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL — 5-year life, drag-sail disposal |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit/Ground Control — STK 11 used with supporting plots |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Screenshots provided (Images 1–5) but no mention of attached STK scenario files |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Structure logical and sources cited, but Wikipedia used and figure/table labelling inconsistent |

## Technical issues

- Orbit: Inclination 87.79° is prograde and not sun-synchronous at 600 km; correct value is ~97.8°, matching the student's own plot. Contradicts 'retrograde' description.
- Launch: Kourou latitude stated as 45.05°N; actual is ~5.2°N. Downstream two-window logic is affected.
- Ground Control & Communications: Mean access duration 580.8 s (~9.7 min) described as 'almost twenty minutes'.
- Orbit: 'A very high altitude would yield low resolution images which is also desirable' — should be 'not desirable'.
- Mission Duration & EOL: Graveyard-orbit option discussed despite LEO context; redundant/contradictory sentences about thrusters and passive disposal.
- Bibliography: Wikipedia cited, which the task disallows; references lack titles and access dates.

## Next steps

1. Correct the inclination: verify the sun-synchronous value at 600 km (~97.8°, retrograde) against your own STK plot, and re-check any downstream calculations that used 87.79°.
2. Fix the Kourou latitude (~5.2°N, not 45.05°N) and re-examine your launch-window reasoning, which depends on it; also restate the mean access duration (580.8 s ≈ 9.7 min) accurately.
3. Name your operator entity and customer groups explicitly in the Introduction, and state whether STK scenario files are attached in an appendix.
4. Replace Wikipedia with primary/technical sources, give full reference details (titles, access dates), and number all figures and tables consistently with in-text citations.
5. Tighten the EOL section: remove the graveyard-orbit discussion (inapplicable in LEO) and resolve the contradictory thruster/passive-disposal sentences.

---
<sub>Run Input_2_d-Run_1-Eff_high-261116-112608 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15261/5579 | cost $0.0037 (incl. $0.001387 for the reused reference rubric+task structure) | 70.41s</sub>
