# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 57 / 100 (57%)**

Your report is well structured with a clear mission concept, good STK evidence and specific conclusions. However, key technical errors (Kourou latitude, sun-synchronous inclination), vague identification of users, missing STK files, and use of Wikipedia hold you at the Adequate level for C1 and C2. Fixing these would move you toward Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Accomplished | 7 / 10 | 14 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly state the primary mission, its rationale, and justify a single spacecraft with references. To reach Accomplished, explicitly identify the operator (e.g. which Australian facility) and the customers (which scientists/organisations) rather than implying them, and add more detailed discussion of the mission need.

*Assessor reasoning:* Mission, rationale and single-spacecraft choice are well covered with references. However, users are only vaguely identified: operator implied (Australian facilities) and customers (scientists) mentioned but not explicitly defined as operator/customers, so not all requirements addressed to a high standard.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "would allow marine and conservation scientists to more accurately predict and react to coral bleaching events"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

All major requirements are addressed with STK screenshots and contact analysis (e.g. ~20 min average contacts). However, the Kourou latitude (45.05°N vs actual ~5.2°N) and the 87.79° prograde inclination contradicting your retrograde SSO claim are significant errors, and no STK files/appendix were provided. Correct these and supply software files to reach Accomplished.

*Assessor reasoning:* Launch, orbit, elements, manoeuvres, ground station, comms frequency and EOL all addressed with STK evidence. But significant technical errors: Kourou is at ~5.2°N not 45.05°N; SSO inclination at 600 km should be ~97.8° (retrograde), not 87.79° (prograde), contradicting the 'retrograde' claim; no STK files/appendix evident.
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924°"  
> Launch: "situated very close to the equator, with a latitude of 45.05°N" *(quote not found in submission)*  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  

### C3 Conclusion (7/10, Accomplished)

Your conclusions are specific and traceable to the evidence, including honest treatment of risks like Vega E availability. To push higher, extend the conclusions with quantitative takeaways (e.g. contact coverage, orbit lifetime) drawn directly from your STK results.

*Assessor reasoning:* Conclusions are specific and trace back to report evidence, including risks (Vega E availability) and design rationale; not generic.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (14/20, Accomplished)

The report has a clear structure, executive summary, labelled figures/tables and consistent citations. Minor grammar slips ('It's first launch', 'complied daily'), minimal figure captions, and the use of Wikipedia (not acceptable per the task) plus incomplete references (e.g. '[10 d.]') prevent a higher mark. Proofread and upgrade sources.

*Assessor reasoning:* Clear structure, executive summary, contents, labelled figures and tables, consistent citations. Minor flaws: Wikipedia used (unacceptable per task), some figure captions minimal, occasional grammar slips ('It's first launch', 'complied daily'), preventing a higher mark.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design – Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design – Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications (STK) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit / Ground Control (screenshots present; no STK files/appendix evident) |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography (Wikipedia cited, not acceptable) |

## Technical issues

- Launch: Kourou's latitude stated as 45.05°N; actual is ~5.2°N. The claim that this is 'smaller than the target inclination' enabling two windows/day is based on the wrong value.
- Orbit: Sun-synchronous inclination at 600 km should be ~97.8° (retrograde); 87.79° is prograde and cannot be sun-synchronous, contradicting the stated retrograde orbit and Image 3 (~97.8° at 600 km).
- Orbit: Text states high altitude yields 'low resolution images which is also desirable' – likely an error; low resolution is undesirable.
- Mission Duration & EOL: Contradictory phrasing: 'without thrusters... uncontrolled descent... However, the ZYZZsat is without thrust capability' repeats and muddles the drag-sail rationale.
- Bibliography: Wikipedia used as a source, which the task disallows; some references incomplete (e.g. '[10 d.]').

## Next steps

1. Correct the Kourou latitude (~5.2°N, not 45.05°N) and re-justify your launch-window claim based on the correct value.
2. Fix the sun-synchronous inclination: at 600 km it should be ~97.8° retrograde, not 87.79° prograde; reconcile with your stated retrograde orbit and Image 3.
3. Explicitly name the operator and customers in the Introduction, and attach your STK scenario files in an appendix; replace Wikipedia with primary sources and complete incomplete references.

---
<sub>Run Input_2_d-Run_1-Eff_low-261118-125543 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15192/4062 | cost $0.003238 (incl. $0.001387 for the reused reference rubric+task structure) | 43.66s</sub>
