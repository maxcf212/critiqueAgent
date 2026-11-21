# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 52 / 100 (52%)**

You have a strong mission concept and clear report structure, with STK screenshots and coverage of all major design areas. The main gaps are technical substantiation: launch vehicle availability and mass check, RAAN/LTAN and orbital calculations, link budget, EOL sizing, and reference quality. Addressing these will make your design more accurate and persuasive.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction clearly frames GBR coral-reef monitoring via fluid lensing, explains the need, justifies a single satellite, and identifies users such as CSIRO/BOM. To strengthen within Accomplished, explicitly name the operator and support broad claims with targeted literature. You are at the lower end of this band; sharper ownership and referencing will make the rationale more persuasive.

*Assessor reasoning:* Mission concept is clearly framed: GBR coral-reef monitoring via fluid lensing. It explains need, single-satellite choice, and users/customers with references. Operator is only implied, and some claims are broad, but most required elements are addressed well.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground control, communications, duration and EOL with STK screenshots, but support is thin. Resolve the Vega E availability contradiction and add a mass/capability check; correct the RAAN rationale and give period/velocity/LTAN with a hand calculation; remove the resolution contradiction; add a link budget, extend access beyond ~3 days, and size the drag sail with deorbit time. Accomplished requires comprehensive, accurate, persuasive evidence including software files.

*Assessor reasoning:* All major design areas are covered with STK screenshots and an access report, but support is thin: no launch mass/capability check, Vega E availability inconsistency, incorrect RAAN rationale, no link budget, no deorbit sizing, and a resolution-error statement. Major requirements are addressed but not comprehensive or persuasive.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved, in addition to the already frequent amount of passes."  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  
> Orbit: "A very high altitude would yield low resolution images which is also desirable."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion restates the design and acknowledges Vega E uncertainty, but it is brief and generic. To reach Accomplished, draw specific evidence-based conclusions on launch choice, communications access, mission duration and EOL, and state how the design meets the mission need. Link each conclusion back to results in the main body rather than summarising only.

*Assessor reasoning:* Conclusion restates design choices and acknowledges Vega E uncertainty, but is brief and does not draw specific evidence-based conclusions on communications, mission duration or EOL. Some conclusions are reached but they are fairly generic.
> Conclusion: "After analysis of each mission segment, a fully described satellite configuration has been constructed."  
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your report has clear headings and an executive summary, but figures/tables are unnumbered, spelling/grammar slips remain, and references are URL-only and include Wikipedia. To reach Accomplished, use a consistent engineering-report format, number and caption all figures/tables, proofread, and provide a properly formatted reference list with matching in-text citations from credible sources.

*Assessor reasoning:* Structure and headings are clear and an executive summary is present. However, figures/tables lack numbering, there are spelling/grammar slips, references are URL-only and include Wikipedia, and formatting is not fully consistent. Not professional but readable.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Ground Control & Communications: "This station is current owned and operated by the University of Tasmania"  
> Mission Duration & EOL: "This may be lengthened though, by the addition of solar panels for electrical power."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Selects Vega E, but conclusion says it 'has not been built yet'; no firm launch mission/date, mass/capability check, or contingency.
- Orbit: RAAN stated to indicate launch facility location; RAAN is set by launch time/azimuth and target LTAN, which is not specified.
- Orbit: No orbital period/velocity/LTAN given; SSO inclination only shown graphically, with no hand calculation or equation.
- Orbit: Statement 'very high altitude would yield low resolution images which is also desirable' is technically wrong or contradictory.
- Mission Duration & EOL: No thrusters but earlier says EOL orbital manoeuvre; drag sail not sized and no deorbit time/25-year compliance shown.
- Ground Control & Communications: No link budget/data rate; access summary covers only ~3 days; 'constantly in sunlight' on descending side is not justified without LTAN.
- Bibliography: Cites Wikipedia [6], which is not acceptable; references are incomplete and inconsistently formatted.

## Next steps

1. Resolve the launch and orbit inconsistencies: confirm Vega E availability/date or choose an operational vehicle, include a mass/capability check and contingency, correct the RAAN explanation, and add orbital period, velocity and LTAN with a hand calculation for the 97.79° SSO.
2. Strengthen the design evidence: add a link budget/data rate, justify the 'constant sunlight' claim via LTAN, extend the access summary beyond ~3 days, and size the drag sail with deorbit time and 25-year compliance; include your STK/software files.
3. Tighten presentation and referencing: number and caption all figures/tables, proofread for spelling/grammar, replace Wikipedia with credible sources, and make in-text citations match a consistently formatted reference list.

---
<sub>Run Input_2-Run_2-Eff_high-261115-165309 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14489/12574 | cost $0.007892 (incl. $0.001387 for the reused reference rubric+task structure) | 79.24s</sub>
