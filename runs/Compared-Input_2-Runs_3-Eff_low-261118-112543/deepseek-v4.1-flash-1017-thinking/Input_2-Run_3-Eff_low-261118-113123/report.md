# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 59 / 100 (59%)**

You present a clear coral-reef fluid-lensing concept and cover launch, orbit, ground station, duration and EOL with STK screenshots. The report is Adequate overall: C1 is strong, but C2-C4 need tighter technical evidence and presentation. Focus on quantified orbit/imaging and link-budget calculations, providing software files, sizing the drag sail, and professional referencing/numbering.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

Your Introduction clearly covers the coral-reef monitoring need, fluid-lensing mission, single-spacecraft rationale and users/operator, with supporting references. You already meet Accomplished; to secure the top of the band, tighten broad claims and ensure every rationale sentence is backed by a specific source.

*Assessor reasoning:* Introduction clearly explains coral-reef monitoring need, fluid-lensing mission, single-satellite rationale, and users/operator. References support rationale. Some claims are broad but all required elements are present to a high standard.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You cover launch, orbit, ground station, duration and EOL with STK screenshots, but C2 is Adequate. To reach Accomplished: address Vega E schedule/interface risk; correct the orbit/imaging contradiction and RAAN statement; quantify swath/resolution and link budget/data rate/antenna/contact capacity; size the drag sail and justify five-year life; include STK/PIGI files or model parameters (Images 1-5).

*Assessor reasoning:* Covers launch, orbit, ground station, duration and EOL with STK screenshots and some calculations. However, launch relies on unbuilt Vega E, orbit/imaging rationale has contradictions, link and drag-sail sizing are absent, and STK files are not provided. Thus adequate, not accomplished.
> Mission Design > Orbit: "an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’"  

### C3 Conclusion (5/10, Adequate)

Your Conclusion summarises launch, orbit and ground station but omits duration, EOL, users and single-satellite rationale, and remains generic. To reach Accomplished, draw specific, quantitative conclusions from your evidence and explicitly revisit each major design choice, including EOL and operations.

*Assessor reasoning:* Conclusion summarises launch, orbit and ground station, but omits duration, EOL, users and single-satellite rationale; it is largely generic and does not draw detailed quantitative conclusions.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (10/20, Adequate)

Headings give clear structure, but figures/tables are not consistently numbered, references are bare URLs including Wikipedia, [10] is malformed, and grammar/typos remain. To reach Accomplished, number and caption all figures/tables consistently, use full author/title/access-date references, and proofread for professional formatting and language.

*Assessor reasoning:* Structure and headings are clear, but figures/tables are not numbered consistently, references are bare URLs including Wikipedia, and grammar/typographical errors remain. Presentation is adequate but not professional.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Design > Launch: "a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Image 1  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design > Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design > Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Mission Design > Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Mission Design > Orbit; Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Images 1-5; Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Whole report; Bibliography |

## Technical issues

- Mission Design > Launch: Vega E is not yet operational; relying on a future launcher and unspecified rideshare creates schedule and interface risk.
- Mission Design > Orbit: Text says a very high altitude would yield low resolution images 'which is also desirable'; this is contradictory and should be undesirable.
- Mission Design > Orbit: RAAN initial value is said to indicate launch facility; RAAN at epoch depends on launch time/azimuth, not facility alone.
- Mission Design > Orbit: No swath/resolution calculation justifies 600 km for fluid lensing; 250 km reef width and daily coverage are not quantitatively linked.
- Ground Control & Communications: No link budget, data rate, ground antenna band, or contact capacity calculation; average contact duration alone is insufficient evidence for data transfer.
- Ground Control & Communications: Claim that descending path is constantly sunlit and used for imaging is not demonstrated; SSO eclipse and LTAN are not specified.
- Mission Duration & EOL: Drag-sail EOL is not sized or calculated; no demonstration of 25-year deorbit or re-entry casualty risk.
- Mission Duration & EOL: Five-year life is assumed without propulsion/station-keeping or drag/SSO drift assessment.
- Images 1-5: Only screenshots are provided; no STK/PIGI files or model parameters are included.
- Bibliography: References are bare URLs, include Wikipedia, and [10] is malformed; no author/title/access dates.

## Next steps

1. Revise Mission Design > Orbit: remove the claim that high altitude gives low resolution 'which is also desirable', correct the RAAN explanation, and add a swath/resolution calculation linking 600 km to fluid-lensing reef coverage and daily revisit.
2. Strengthen Ground Control & Communications and Mission Duration & EOL: add a link budget with data rate, ground antenna band and contact capacity; specify SSO LTAN/eclipse; size the drag sail and show 25-year deorbit or casualty-risk compliance; justify five-year life with station-keeping/drag drift.
3. Improve evidence and presentation: include STK/PIGI files or model parameters for Images 1-5, number all figures/tables, replace bare URLs/Wikipedia with full references, fix [10], and expand the Conclusion to cover duration, EOL, users and single-satellite rationale.

---
<sub>Run Input_2-Run_3-Eff_low-261118-113123 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14500/10849 | cost $0.00779 (incl. $0.001387 for the reused reference rubric+task structure) | 90.27s</sub>
