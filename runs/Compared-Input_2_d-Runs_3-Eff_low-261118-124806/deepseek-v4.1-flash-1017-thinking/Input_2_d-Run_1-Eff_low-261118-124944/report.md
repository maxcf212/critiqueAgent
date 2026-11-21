# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 52 / 100 (52%)**

Your report covers most mission elements and is readable, with a clear executive summary and useful STK screenshots. The main weaknesses are orbit/launch inconsistencies, contact-time misreporting, contradictory EOL logic, incomplete user/operator detail, missing software-file evidence, and weak referencing. You are in the Adequate band; to reach Accomplished, correct these technical errors and strengthen evidence and referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly describe the mission, rationale and single-spacecraft choice with references. To move from Adequate to Accomplished, explicitly name the operator and customers, not just implied Australian facilities/scientists, and support user roles with literature. Your Executive Summary and Introduction already provide a good base; add specific user requirements and operational responsibilities.

*Assessor reasoning:* Mission, rationale and single-spacecraft choice are detailed with references. Users are only partly identified: Australian facilities and scientists are implied, but operator and customers are not explicitly named. Therefore Adequate-high rather than Accomplished.
> Executive Summary: "The satellite, nicknamed ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), is operated and accessed from Australia ground facilities"  
> Introduction: "only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground station, duration and EOL with STK screenshots and an access table. Next level requires correcting the Kourou latitude (45.05°N vs ~5.2°N), making the 600 km SSO inclination consistent (~97.8° retrograde, not 87.79°), assessing the plane-change/dogleg, correcting mean contact time (580.786 s ≈9.7 min, not almost 20), resolving the EOL manoeuvre/thruster/drag-sail contradiction, and evidencing software files.

*Assessor reasoning:* Launch, orbit, ground station, duration and EOL are covered with STK screenshots and an access table. However, the SSO inclination is wrong/inconsistent with the plotted value, Kourou latitude is badly misstated, mean contact time is misreported, EOL/manoeuvre logic contradicts itself, and software files are not evidenced. Adequate but error-prone.
> Orbit: "an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "average contact duration of almost twenty minutes was achieved"  
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  

### C3 Conclusion (6/10, Adequate)

Your Conclusion summarises launch, orbit and ground-station choices, but it is generic and omits meaningful conclusions on mission duration and EOL. To reach Accomplished, draw specific conclusions from your evidence: state how the chosen orbit/launch/ground segment meet mission needs, justify the unbuilt Vega E with a clearer fallback, and include duration/EOL outcomes rather than only restating choices.

*Assessor reasoning:* The conclusion summarises launch, orbit and ground-station choices from the report, but it is somewhat generic and omits meaningful conclusions on duration and EOL. It also depends on an unbuilt launch vehicle with only a brief fallback comment.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your structure, headings and executive summary are clear and readable. To reach Accomplished, make figure/table numbering and captions consistent (e.g. Image 1/Image 4), provide full bibliography metadata (titles, authors, access dates) instead of bare URLs, remove Wikipedia, and ensure every in-text citation matches the reference list. These changes will lift presentation from readable to professional.

*Assessor reasoning:* Structure, headings and executive summary are clear, but figures/tables are inconsistently numbered or captioned, bibliography entries are mostly bare URLs without proper metadata, Wikipedia is used despite being unacceptable, and citation formatting is weak. Presentation is readable but not professional.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 1: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Executive Summary; Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary; Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit; Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 1; Image 4; Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Kourou latitude is stated as 45.05°N; actual latitude is about 5.2°N, affecting launch/inclination reasoning.
- Orbit: Inclination 87.79° is prograde and not sun-synchronous at 600 km; the plotted SSO value is near 97.8°, so the orbital element table is internally inconsistent.
- Launch; Orbit: A direct launch from Kourou at ~5°N into a ~97.8° retrograde SSO requires significant plane change/dogleg; this feasibility and cost are not assessed.
- Ground Control & Communications: Mean access duration in the STK table is 580.786 s (about 9.7 min), not 'almost twenty minutes'; maximum is about 12.8 min.
- Orbit: RAAN initial value 27.33° is said to indicate the launch facility, but no launch time/geometry calculation supports this.
- Mission Duration & EOL: Text says the only manoeuvre occurs at EOL, then says the satellite has no thrusters and uses a passive drag sail; this is contradictory and the drag-sail description is incomplete.
- Bibliography: References are largely bare URLs without titles/authors/access dates, and Wikipedia is cited despite being explicitly unacceptable.

## Next steps

1. Correct the launch and orbit calculations: Kourou latitude, SSO inclination consistency, RAAN/launch geometry, and the feasibility/cost of the plane change or dogleg for a retrograde SSO from ~5°N.
2. Reconcile the ground-contact duration with the STK table and resolve the EOL contradiction between a manoeuvre, no thrusters, and a passive drag sail; include software files as evidence.
3. Explicitly name the operator and customers in the Introduction, and rebuild the Bibliography with full metadata, no Wikipedia, and matching in-text citations.

---
<sub>Run Input_2_d-Run_1-Eff_low-261118-124944 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14361/8989 | cost $0.006415 (incl. $0.001387 for the reused reference rubric+task structure) | 54.09s</sub>
