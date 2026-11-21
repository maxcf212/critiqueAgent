# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 61 / 100 (61%)**

You delivered a well-conceived Australian reef-monitoring mission concept with strong STK access analysis in your ground segment and a thorough introduction. To advance your mission design to a professional standard, focus on refining orbital mechanics fundamentals (such as retrograde launch dynamics), providing supporting hand calculations, eliminating design contradictions regarding maneuvers, and adhering to formal academic reporting standards with proper figure numbering and peer-reviewed citations.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You clearly established ZYZZsat's primary reef-monitoring mission, justified a single satellite, and identified key stakeholders like CSIRO and BOM in the Introduction. To reach the top of Accomplished, integrate deeper literature citations connecting your mission requirements directly to existing Australian Earth-observation and reef-monitoring frameworks.

*Assessor reasoning:* The introduction clearly identifies the primary mission (Great Barrier Reef monitoring via fluid lensing), its national benefit, justification for a single satellite, and users/operators (CSIRO, BOM, Australian government).
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You effectively applied STK to assess Mt Pleasant access and selected an appropriate 600 km SSO. To achieve Accomplished, correct technical misconceptions—such as the velocity penalty when launching retrograde orbits from equatorial sites—resolve contradictions between active maneuvers and passive drag deorbit, and support software models with hand calculations.

*Assessor reasoning:* Core mission elements are addressed (Vega E rideshare, 600 km circular SSO, Mt Pleasant station with STK access analysis, passive drag-sail EOL). However, it exhibits technical misconceptions (equatorial launch velocity benefit for a retrograde SSO), contains contradictions about maneuvers vs passive design, and lacks hand calculations.
> Orbit: "As the satellite can be launched directly into low-earth orbit, the only orbital manoeuvre occurs at the EOL segment"  

### C3 Conclusion (7/10, Accomplished)

Your conclusion provides a solid synthesis of the mission architecture and astutely highlights programmatic risks, such as Vega E development status. To achieve the top mark in Accomplished, include more detailed, quantitative conclusions evaluating whether the final orbital elements and revisit intervals fully satisfy the initial science goals.

*Assessor reasoning:* The conclusion synthesizes the findings across launch, orbit, ground segment, and reef monitoring objectives, acknowledging launcher availability risks.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

The report features a logical structure and concise executive summary. To achieve Accomplished, number and caption all figures formally, proofread to fix incomplete sentences (such as in Mission Duration & EOL), and ensure your bibliography uses professional reference styles rather than bare URLs or Wikipedia citations.

*Assessor reasoning:* The report follows a standard structure with an executive summary. However, presentation is compromised by unnumbered figure captions, incomplete sentences in the EOL section, bare URLs, and the prohibited use of Wikipedia as a reference.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | partial | Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Equatorial launch sites do not assist retrograde sun-synchronous orbits ($i \approx 97.8^\circ$); Earth's eastward rotational velocity imposes a $\Delta v$ penalty rather than a fuel saving.
- Orbit: The text states an orbital maneuver occurs at EOL, but later confirms the satellite has no propulsion system and uses passive drag deorbit.
- Mission Duration & EOL: Incomplete sentence: 'utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10].'

## Next steps

1. Recalculate your launch delta-v budget to correctly account for the Earth rotational velocity penalty when launching into retrograde sun-synchronous inclinations from equatorial sites.
2. Supplement your STK simulation outputs with independent hand calculations for parameters like orbital period, coverage revisit rates, or aerodynamic drag decay timelines.
3. Standardise your report presentation by numbering all figure captions, completing truncated text in the EOL section, and replacing non-academic references like Wikipedia with peer-reviewed literature.

---
<sub>Run Input_2-Run_1-Eff_high-261115-170512 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 32067/15287 | cost $0.064814 (incl. $0.001387 for the reused reference rubric+task structure) | 103.05s</sub>
