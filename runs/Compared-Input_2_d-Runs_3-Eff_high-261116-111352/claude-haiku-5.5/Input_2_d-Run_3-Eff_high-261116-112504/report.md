# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 36 / 100 (36%)**

Your report covers all the required mission segments, and the STK screenshots and access table give useful supporting evidence. Several technical errors weaken it, including the sun-synchronous inclination, the semi-major axis, the Kourou latitude and the contact-time claim. The end-of-life plan, lifetime analysis, references and presentation also need work.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | - | 0 / 10 | 0 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (0/10, -)

Your assessor recorded that the introduction meets its requirements, but no criterion level or written reasoning was provided for this criterion, so specific feedback cannot be given here. Please check with your assessor for detail on the mission rationale, the number of spacecraft and the operator and customers.

*Assessor reasoning:* 

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

Your STK screenshots and access table give real evidence for the design, and each required topic is touched on. Several values need correcting: the sun-synchronous inclination of 87.79 degrees conflicts with your plot and your retrograde claim, the semi-major axis should be 6971 km, and the Kourou latitude is about 5.2 N. Your average contact claim also conflicts with your table mean of about 581 s.

*Assessor reasoning:* STK screenshots and an access table give some evidence, and the required topics are touched on. However, the 87.79 degree inclination contradicts the plot (about 97.8 degrees) and the 'retrograde' claim. Semi-major axis is wrong (6971 km, not 7171 km). The Kourou latitude is wrong. The 'twenty minute' contact claim contradicts the table mean of about 581 s. Manoeuvres, operations, and EOL are inconsistent and thinly supported, and perturbation and hand calculations are absent.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of"  
> Orbit: "Required to achieve an altitude of 600km while remaining sun-synchronous."  
> Orbit: "Earth radius of 6371km plus a proposed altitude of 600km as previously explained."  
> Launch: "it is situated very close to the equator, with a latitude of"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "Thus, abandoning the satellite at its EOL is not environmentally or socially responsible."  

### C3 Conclusion (4/10, Adequate)

You summarise each mission segment and acknowledge the Vega E launch risk, which is useful. However, the conclusion is generic and draws no quantitative findings from your STK results. The claim that the mission will prevent coral bleaching overstates what the evidence shows, so state what your analysis demonstrates and its limits.

*Assessor reasoning:* The conclusion summarises each segment and acknowledges the Vega E launch risk. However, it is generic, draws no quantitative conclusions from the STK results, and overclaims that the mission will prevent bleaching. It restates the report rather than reaching specific, evidence-based conclusions.
> Conclusion: "The initial problem of not catching coral bleaching events in time can be minimised, if not solved"  

### C4 Report presentation (8/20, Adequate)

Your report has clear headings, an executive summary and a contents page. To reach a professional standard, proofread for complete sentences, spelling and formal language, and check the title-page date, which appears to be wrong. Number all tables and figures consistently. Make citations match: remove Wikipedia and ensure every referenced source (including 49 to 74) appears in the bibliography with complete entries.

*Assessor reasoning:* Clear headings, an executive summary and a contents page give a reasonable structure. However, there are truncated sentences, typos, informal wording, and an incorrect date on the title page. Tables and images are not numbered. Citations are inconsistent: tables cite refs 49 to 74, which are absent, Wikipedia is used, and reference entries are garbled.
> Mission Design / Orbit: "utilising a large surface area to"  
> Title page: "AERO9500 - T3 2020"  
> Bibliography: "a wiki sorted directory"  
> Launch tables: "Small Satellites Mission Service (SSMS) piggyback mission."  
> Bibliography: "[10 d."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 1 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: Sun-synchronous inclination at 600 km stated as 87.79 degrees, which is prograde and contradicts the plotted value (about 97.8 degrees) and the 'retrograde' claim.
- Orbit (COE table): Semi-major axis of 7171 km is wrong; 6371 + 600 gives 6971 km.
- Orbit (COE table): RAAN is said to indicate the launch facility location, which is conceptually incorrect.
- Launch: Kourou latitude given as 45.05 N; it is about 5.2 N. The launch-window reasoning based on this value is also confused.
- Ground Control & Communications: Claimed average contact of almost twenty minutes conflicts with the table mean of 580.786 s (about 9.7 min).
- Ground Control & Communications (access table): Access 13 is duplicated, and the text says fifteen periods but only fourteen are listed; total duration does not match the rows.
- Ground Control & Communications: Claims the descending pass is constantly sunlit; a 600 km SSO has eclipse seasons, and this is not analysed.
- Orbit / Mission Duration & EOL: States only manoeuvre is at EOL while also stating the satellite has no thrusters, so no EOL manoeuvre is possible as described.
- Mission Duration & EOL: No decay or lifetime analysis supports the 5-year duration or the claim that uncontrolled re-entry is passive and sufficient at 600 km.
- Executive Summary: Claims perturbation calculations are included, but none are presented.
- Bibliography: Wikipedia is cited despite being explicitly unacceptable; tables cite references 49 to 74 that do not appear in the bibliography.

## Next steps

1. Correct the orbit and launch values: a 600 km sun-synchronous orbit is retrograde (about 97.8 degrees), the semi-major axis is 6371 + 600 = 6971 km, and Kourou is at about 5.2 N. Rewrite the RAAN explanation as an angle from the vernal equinox, not a launch-site location, then update all tables and plots to match.
2. Strengthen the mission-life and end-of-life analysis. State clearly that the satellite has no thrusters, explain how passive deorbit works, and add a decay or lifetime calculation that supports the 5-year duration. Analyse eclipse seasons and reconcile the contact statements with the access table, fixing the duplicated access 13 and the fourteen-versus-fifteen count.
3. Support your claims with evidence. Include the perturbation calculations mentioned in your executive summary, replace Wikipedia with authoritative sources, and rewrite the conclusion as specific, quantified findings with realistic limits, not claims such as preventing coral bleaching.

---
<sub>Run Input_2_d-Run_3-Eff_high-261116-112504 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21279/14265 | cost $0.009314 (incl. $0.001387 for the reused reference rubric+task structure) | 63.78s</sub>
