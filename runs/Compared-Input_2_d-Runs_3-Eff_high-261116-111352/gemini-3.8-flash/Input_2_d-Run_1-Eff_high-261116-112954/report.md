# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You have developed an engaging mission concept for monitoring Australian coral bleaching, effectively supported by STK simulations and architecture trade-offs. To reach the Accomplished level across your design, focus on resolving key technical discrepancies—such as your orbital inclination and launch coordinates—and explicitly distinguishing formal operators from customers. Additionally, elevate your report presentation by adopting standard academic referencing, adding figure captions, and thoroughly proofreading incomplete text.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You articulated a strong mission rationale and payload concept (fluid lensing) that clearly benefits Australia, well-justifying a single-satellite architecture. To reach Accomplished, explicitly differentiate the spacecraft operator from the customer organizations in your Introduction, and strengthen the background context with more thorough literature citations.

*Assessor reasoning:* The mission rationale and payload concept (fluid lensing for coral bleaching) are well explained and clearly benefit Australia. The single-satellite architecture is justified based on the timescale of bleaching events. However, users are only loosely identified as 'marine and conservation scientists' without distinguishing formal operating bodies from commercial or governmental customer entities. Referencing in the introduction is also quite sparse.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You effectively applied STK access analyses and trade-offs across your mission design sections. To achieve Accomplished, verify technical calculations and parameters for consistency: correct Kourou's latitude in Mission Design (~5.2°N), ensure the 600 km SSO inclination is retrograde (~97.8°), and convert contact times accurately (580.8 s is ~9.7 minutes, not twenty).

*Assessor reasoning:* Major design aspects are covered using STK access analyses and trade-offs. However, several substantial technical errors occur: Kourou's latitude is incorrectly stated as 45.05°N rather than ~5.2°N; the 600 km sun-synchronous orbit inclination is reported as prograde 87.79° instead of retrograde 97.79° (contradicting the student's own MATLAB plot); and an average contact duration of 580.8 seconds (~9.7 minutes) is incorrectly described as 'almost twenty minutes'.
> Mission Design: "with a latitude of 45.05°N." *(quote not found in submission)*  
> Orbit: "requires a mean inclination of 87.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  

### C3 Conclusion (6/10, Adequate)

Your conclusion neatly connects your launch vehicle, sun-synchronous orbit, and the Mt Pleasant ground station back to the coral monitoring objectives. To reach Accomplished, move beyond descriptive summaries by incorporating critical evaluation of design limitations, operational mission risks, and concrete engineering recommendations.

*Assessor reasoning:* The conclusion recaps the core mission elements, connecting the launch vehicle, sun-synchronous orbit, and Tasmanian ground station back to the coral monitoring objective. However, it remains high-level and descriptive, lacking critical reflection on design limitations, operational risks, or specific technical recommendations.
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Your report maintains an accessible structure with clear headings. To meet Accomplished standards, replace prohibited Wikipedia links with complete academic citations instead of bare URLs, number and caption all figures and tables, and proofread to eliminate unfinished sentences, such as the cut-off text in Mission Duration & EOL.

*Assessor reasoning:* Structure and readability are acceptable, but professional presentation is lacking. Wikipedia is explicitly cited despite task instructions forbidding it; raw launch tables are pasted directly with orphan superscript tags; figures lack formal numbering and captions; reference [10] is corrupted; the bibliography consists only of bare URLs; and an incomplete sentence is left in the EOL section.
> Mission Design: "a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Mission Duration & EOL: "utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Mission Design: Kourou (Guiana Space Centre) latitude is stated as 45.05°N; French Guiana is located near equatorial latitudes (~5.2°N).
- Orbit: A 600 km circular sun-synchronous orbit requires a retrograde inclination of ~97.8°. The reported value of 87.79° is prograde and physically non-sun-synchronous.
- Ground Control & Communications: The STK report lists a mean contact duration of 580.786 s (9.68 minutes), which the text erroneously claims is 'almost twenty minutes'.
- Mission Duration & EOL: The final sentence of the section cuts off abruptly mid-clause ('utilising a large surface area to ‘ and is suitable').

## Next steps

1. Revisit orbital mechanics and geographic parameters to correct technical values, ensuring your SSO inclination is retrograde (~97.8°) and Kourou's latitude is accurately defined (~5.2°N).
2. Formalize your stakeholder analysis in the Introduction by explicitly defining the spacecraft operating entity separately from specific end-user and customer organizations.
3. Upgrade report presentation by replacing Wikipedia links with peer-reviewed sources, fully formatting bibliography citations, numbering and captioning all figures, and completing truncated sentences.

---
<sub>Run Input_2_d-Run_1-Eff_high-261116-112954 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18358/11565 | cost $0.048524 (incl. $0.001387 for the reused reference rubric+task structure) | 64.55s</sub>
