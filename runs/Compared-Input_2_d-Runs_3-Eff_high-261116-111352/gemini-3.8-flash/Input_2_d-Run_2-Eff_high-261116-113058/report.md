# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 52 / 100 (52%)**

You proposed an innovative coral reef monitoring concept for Australia and effectively used STK to model the mission profile. The rationale for a single satellite was well justified. To improve, address several technical inaccuracies in your orbital calculations and ground pass data, expand on specific operational stakeholders, and polish presentation by replacing raw copied tables and Wikipedia citations with rigorous academic sources.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly justified your single-satellite coral reef monitoring concept. To reach Accomplished, identify specific operational and customer organizations (e.g., CSIRO, GBRMPA, or the Australian Space Agency) rather than broad user groups, and substantiate your rationale with peer-reviewed literature rather than general web links.

*Assessor reasoning:* The report presents a relevant mission concept addressing Great Barrier Reef monitoring using fluid lensing. The rationale for deploying a single satellite is clearly justified based on coral bleaching timescales. However, mission users are only defined broadly as marine scientists and Australian ground facilities, without identifying specific operational entities (e.g., ASA, CSIRO) or customer organisations (e.g., GBRMPA). Referencing relies heavily on general online links.
> Introduction: "marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your architecture effectively covered key phases using STK. To achieve Accomplished, resolve critical technical discrepancies: correct Kourou's latitude to ~5.23°N, calculate the semi-major axis accurately (6971 km, not 7171 km), specify the correct retrograde SSO inclination (97.79°), and reconcile the ground pass duration in your text with the STK report's 9.7-minute mean.

*Assessor reasoning:* The mission architecture covers launch, orbit, ground access, and passive de-orbiting using STK. However, multiple technical errors undermine the design: Kourou's latitude is given as 45.05°N instead of 5.23°N; semi-major axis arithmetic is incorrect (6371 + 600 = 7171 km); inclination is transcribed as 87.79° (prograde) rather than 97.79° (retrograde SSO); and STK mean pass duration (581 s / ~9.7 min) is incorrectly stated as 'almost twenty minutes'.
> Mission Design: "altitude of 600km requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Mission Design: "Earth radius of 6371km plus a proposed altitude of 600km as previously explained."  

### C3 Conclusion (6/10, Adequate)

You successfully summarized your design decisions and noted Vega E launcher risks. To achieve Accomplished, move beyond descriptive summaries by critically synthesizing the performance trade-offs, engineering compromises, and technical limitations identified across your STK analyses.

*Assessor reasoning:* The conclusion summarises the primary mission decisions across launch, orbit, ground station access, and end-of-life disposal. While it ties together the main operational segments and highlights risks with the unbuilt Vega E vehicle, it remains largely qualitative and does not critically synthesise performance compromises or technical limitations encountered during the design.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  

### C4 Report presentation (10/20, Adequate)

Your report follows a clear structure with an executive summary. To reach Accomplished, replace raw Wikipedia tables and links with properly formatted, original tables and academic citations. Ensure all figures and tables have numbers and descriptive captions, and proofread thoroughly to fix incomplete sentences, such as the truncated text in your EOL section.

*Assessor reasoning:* The report follows a standard structure with an executive summary. However, presentation quality is degraded: figures and tables lack standard numbering and captions; Wikipedia tables with raw footnote tags are copy-pasted; a broken sentence appears in the EOL section; reference list formatting is messy with broken entries; and Wikipedia is cited as a source despite being explicitly prohibited.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design: Launch site latitude for Kourou (CSG) is erroneously stated as 45.05°N; Kourou is located near the equator at approximately 5.23°N.
- Mission Design: Semi-major axis calculation error: 6371 km Earth radius + 600 km altitude is calculated as 7171 km instead of 6971 km.
- Mission Design: Sun-synchronous inclination at 600 km altitude is stated as 87.79° (prograde), which is physically invalid for an SSO; the correct retrograde inclination is 97.79° (as shown on the student's plot).
- Ground Control & Communications: Text reports an average pass duration of 'almost twenty minutes', contradicting the included STK report which indicates a mean duration of 580.8 seconds (~9.7 minutes).
- Mission Duration & EOL: The drag sail discussion terminates abruptly mid-sentence: 'utilising a large surface area to ‘ and is suitable...'.
- Mission Design: Direct copy-pasting of raw Wikipedia tables into the document body with unformatted hyperlink reference numbers (e.g. [50][51], [66]).

## Next steps

1. Recalculate key orbital parameters to resolve errors: adjust the semi-major axis to 6971 km, correct Kourou's latitude to ~5.23°N, fix the SSO inclination to 97.79°, and align pass durations with STK reports (~9.7 minutes).
2. Identify dedicated mission operators and customer agencies (such as CSIRO, GBRMPA, or the Australian Space Agency) in your Introduction, backed by academic literature.
3. Replace raw Wikipedia tables and citations with custom, numbered engineering tables and peer-reviewed sources, ensuring all sentences are complete and thoroughly proofread.

---
<sub>Run Input_2_d-Run_2-Eff_high-261116-113058 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 32391/18024 | cost $0.072249 (incl. $0.001387 for the reused reference rubric+task structure) | 105.9s</sub>
