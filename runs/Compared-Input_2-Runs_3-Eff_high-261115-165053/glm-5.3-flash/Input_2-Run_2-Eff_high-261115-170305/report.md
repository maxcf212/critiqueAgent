# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 73 / 100 (73%)**

Your EO mission for Great Barrier Reef monitoring is well motivated and addresses nearly all task requirements, with justified launch, SSO orbit, ground stations, and EOL plans supported by STK evidence. To reach the top band, resolve internal contradictions in orbit/EOL reasoning, add numbered figure/table captions, replace Wikipedia with credible sources, and format references consistently.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

Accomplished (8/10). Your introduction clearly covers the primary mission, rationale with bleaching statistics and references, the single-spacecraft justification, and users/operator/funding. To strengthen further, sharply distinguish customers from operators and add a little more detail on the funding/user arrangements.

*Assessor reasoning:* All required elements addressed: primary mission (fluid-lensing reef imaging), rationale (bleaching statistics, references), single-spacecraft justification, and users/operator/funding. Detailed with literature citations; only minor gaps (customers vs operators not sharply distinguished).
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Accomplished (8/10). You justified the Vega E launch, presented the SSO with a COE table and J2 reasoning, addressed manoeuvres, ground stations, contact durations, and a 5-year mission with drag-sail EOL, supported by STK screenshots. Next level requires removing the contradictory altitude/resolution and EOL statements, correcting the RAAN rationale (set by local time of descending node, not launch-site location), acknowledging LEO eclipse periods, and including hand calculations and explicit STK file references.

*Assessor reasoning:* Launch site/vehicle justified, SSO orbit with COE table and J2 reasoning, manoeuvres addressed (EOL only), ground station selection justified, STK access report and ground-track screenshots provided, 5-year duration and drag-sail EOL. Weakened by internal contradictions (altitude/resolution statement, EOL logic), no hand calculations shown, and STK files not explicitly included.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924"  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  

### C3 Conclusion (7/10, Accomplished)

Accomplished (7/10). Your conclusions summarise each segment and acknowledge risks such as Vega E availability with a Vega C fallback. To improve, add a quantitative recap of key results (orbit elements, contact statistics, mission duration) so conclusions follow directly from the evidence presented.

*Assessor reasoning:* Conclusions summarise each segment's outcome and acknowledge risks (Vega E availability, fallback to Vega C). Appropriate but brief; lacks quantitative recap of key results.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Adequate (5/10). Your structure with headings and executive summary is clear, but figures and tables lack numbered captions, references are bare URLs including the disallowed Wikipedia citation, and there are grammar/typo issues (e.g. 'a Earth observation', 'complied') plus contradictory sentences. The next level requires consistent formatting, numbered and labelled figures/tables, properly cited references matching the list, and careful proofreading.

*Assessor reasoning:* Clear structure with headings and executive summary, but figures/tables lack numbers, references are bare URLs including Wikipedia (explicitly disallowed), broken citation '[10 d.]', and grammar/typo issues ('a Earth observation', 'complied', 'current owned', contradictory sentences).
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "A very high altitude would yield low resolution images which is also desirable."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit / Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: 'A very high altitude would yield low resolution images which is also desirable' contradicts the design logic (should read 'not desirable').
- Mission Duration & EOL: Contradictory/redundant EOL reasoning: uncontrolled descent is endorsed then dismissed because the satellite 'is without thrust capability'; drag sail strategy conflated with passive deorbit discussion.
- Orbit: Claim of 'constant supply of sunlight' ignores eclipse periods inherent to LEO SSO.
- Orbit: RAAN initial value justified as 'location of the launch facility' is dubious; RAAN should be set by desired local time of descending node over the reef.
- Bibliography: Wikipedia cited as [6], which the task explicitly disallows; references are unformatted bare URLs with stray characters ('f.', '[10 d.]').
- Report body: Figures and tables lack numbered captions; STK files are not explicitly referenced as included in an appendix.

## Next steps

1. Proofread for internal contradictions: fix the altitude/resolution sentence, the eclipse/sunlight claim, the RAAN justification, and the EOL drag-sail vs uncontrolled-descent logic.
2. Add numbered captions to all figures and tables and explicitly state where STK files are included (e.g. Appendix A).
3. Replace the Wikipedia citation with primary sources and format all references consistently (e.g. IEEE style), removing stray characters like 'f.' and '[10 d.]'.

---
<sub>Run Input_2-Run_2-Eff_high-261115-170305 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15225/4831 | cost $0.002661 (incl. $0.001387 for the reused reference rubric+task structure) | 62.66s</sub>
