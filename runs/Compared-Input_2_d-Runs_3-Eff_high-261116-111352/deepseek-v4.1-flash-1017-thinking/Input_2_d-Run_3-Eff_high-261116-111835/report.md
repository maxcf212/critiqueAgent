# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 53 / 100 (53%)**

Your coral-reef imaging mission is coherent and supported by STK screenshots, with a clear mission need and single-spacecraft rationale. However, core orbital values (Kourou latitude, SSO inclination), contact-duration claims, EOL analysis and referencing need correction. You are at Adequate for C2/C3/C4 and low Accomplished for C1; the next level requires accurate, well-supported and professionally presented evidence.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction clearly explains the coral-reef imaging need and why one spacecraft suffices, with mostly appropriate references. To move beyond low Accomplished, explicitly identify the operator and customers (not just implied scientists) and add specific detail on their roles. That will meet the Accomplished requirement for detailed descriptions and appropriate literature.

*Assessor reasoning:* Mission need, rationale and single-spacecraft choice are clear and mostly referenced. Users are implied (scientists) but operator and customers are not explicitly identified, so only low Accomplished.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover all major design areas and include STK screenshots, but key values undermine accuracy: Kourou is ~5.2°N not 45.05°N; 600 km SSO inclination should be ~97.8° not 87.79°; mean contact is 580.786 s (9.7 min), not almost 20 min. Justify RAAN with launch geometry, add quantitative deorbit/25-year compliance, and include required STK/PIGI files. Accomplished requires accurate, comprehensive, persuasive evidence.

*Assessor reasoning:* All major design areas and STK screenshots are present, but core errors undermine accuracy: Kourou latitude, SSO inclination, contact-duration statistic. Therefore adequate, not accomplished.
> Launch: "with a latitude of $ 45.05^{\circ} $N."  
> Orbit: "an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (6/10, Adequate)

Your Conclusion summarises the design and notes launch-vehicle uncertainty, but it largely restates earlier sections and inherits the orbit/coverage errors. To reach Accomplished, draw specific conclusions from corrected evidence—e.g., quantified coverage, contact frequency and EOL compliance—rather than repeating the body. Keep the launch-risk point but tie it to design impact.

*Assessor reasoning:* Conclusion summarises the design and launch uncertainty, but mostly restates earlier sections and inherits orbit and coverage errors. Some specific detail is present.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

You use clear headings and an executive summary, making the report readable. To reach Accomplished, number and caption all figures/tables consistently, replace bare URLs and Wikipedia with properly formatted references that match in-text citations, and polish spelling/grammar and language style. The current presentation is Adequate but not yet professional.

*Assessor reasoning:* Clear headings and executive summary, but figures/tables are unnumbered, references are bare URLs and include Wikipedia, and writing/formatting flaws remain. Readable but not professional.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Ground Control & Communications: "DN path for orbits 1-15"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit; Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit; Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography; Contents |

## Technical issues

- Launch: Kourou latitude is given as 45.05°N; it is about 5.2°N. This contradicts the 'close to equator' claim and affects launch/orbit geometry.
- Orbit: Sun-synchronous inclination at 600 km should be about 97.8°, not 87.79°; the report's own plot implies ~97.7°. At 87.79° the orbit is prograde, not retrograde SSO.
- Orbit: RAAN initial value 27.33° is said to indicate launch location; RAAN is not simply launch-site longitude/latitude and needs launch-time/geometry justification.
- Ground Control & Communications: Mean access duration shown is 580.786 s (9.7 min), not 'almost twenty minutes'; max is 12.8 min. Contact-frequency claims are overstated.
- Mission Duration & EOL: Drag-sail explanation is incomplete and no quantitative deorbit time or 25-year/space-debris compliance analysis is provided.
- Bibliography: References are bare URLs and include Wikipedia, contrary to task instructions; citation formatting is incomplete.

## Next steps

1. Correct the orbital-mechanics values and claims: Kourou latitude (~5.2°N, not 45.05°N), 600 km SSO inclination (~97.8°, not 87.79°), RAAN justification using launch geometry, and mean contact duration (580.786 s, not almost 20 min). Update affected figures and text.
2. Add a quantitative end-of-life/deorbit analysis (including 25-year/space-debris compliance) and include the required STK/PIGI software files so your design evidence is complete.
3. Improve presentation and referencing: number and caption all figures/tables, replace bare URLs and Wikipedia with properly formatted citations matching the reference list, and explicitly identify the operator and customers in the Introduction.

---
<sub>Run Input_2_d-Run_3-Eff_high-261116-111835 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14254/11277 | cost $0.006992 (incl. $0.001387 for the reused reference rubric+task structure) | 88.0s</sub>
