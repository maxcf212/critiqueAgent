# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You present a relevant Australian reef-monitoring mission and use STK evidence to explore access and mission design. Your report has a clear structure, but errors in the launch-site latitude and orbit inclination undermine key conclusions. Strengthening the technical evidence, operational details, sourcing and final editing would make the design more persuasive and move the main-body, conclusion and presentation criteria toward the next rubric level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

You explain the Australian reef-monitoring purpose, rationale and single-spacecraft choice in the Introduction. To strengthen this further, name the spacecraft operator and customer organisations, clarify their roles, and support the operational rationale with specific details and stronger sources.

*Assessor reasoning:* The mission purpose, Australian benefit, rationale, and single-spacecraft choice are explained. The report identifies conservation scientists as users but does not clearly name the spacecraft operator or define customer organisations. The mission rationale is relevant, though some claims and the mission concept would benefit from stronger sourcing and more specific operational detail.
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react to coral bleaching events."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You use STK and provide orbit views and access results, addressing launch, orbit, communications, duration and disposal. The launch-site latitude and stated 87.79° inclination are incorrect, and coverage, link capacity, launch feasibility and disposal lifetime lack evidence. Correct these and add quantitative analyses and supporting files to reach Accomplished.

*Assessor reasoning:* The report uses STK, includes orbit views and access results, and addresses launch, orbit, communications, duration, and disposal. However, the stated 87.79° inclination is not sun-synchronous at 600 km; a retrograde inclination near 97.8° is needed. The stated launch-site latitude is also wrong. Launch feasibility, sensor performance, communications capacity, and EOL lifetime are not adequately demonstrated, and no software files are provided.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved, in addition to the already frequent amount of passes."  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  
> Image 1  

### C3 Conclusion (5/10, Adequate)

Your Conclusion summarises the proposed mission and notes launch-vehicle uncertainty. To reach Accomplished, draw specific conclusions from verified design results, correct the orbit premise, and acknowledge analysis limitations rather than mainly restating the proposal.

*Assessor reasoning:* The conclusion summarises the chosen mission elements and recognises launch-vehicle uncertainty. It is relevant but largely restates the proposal, and its conclusions rely on the incorrect sun-synchronous orbit inclination and do not discuss the limitations of the analysis.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "Thus, launch may need to be adjusted if the rocket is still not constructed by the proposed date."  

### C4 Report presentation (8/20, Adequate)

You provide an executive summary, recognisable engineering structure, figures, tables and a bibliography. To reach Accomplished, improve grammar and consistency, complete the EOL sentence, use clear numbered captions, and ensure in-text citations and references are complete, reliable and matched.

*Assessor reasoning:* The report has a recognisable engineering structure, executive summary, figures, tables, and bibliography. Presentation is weakened by an unacceptable Wikipedia source, incomplete and inconsistent references, unnumbered or weakly captioned figures, awkward grammar, and a visibly incomplete EOL sentence. The overall structure remains readable.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Launch: "To compare existing spaceflight mission plans, a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes [10]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: The report gives the Guiana Space Centre latitude as 45.05° N. Kourou is approximately 5.2° N. This invalidates the associated launch-window explanation.
- Orbit: A 600 km circular sun-synchronous orbit requires a retrograde inclination of approximately 97.8°, not 87.79°. The stated inclination is prograde and cannot provide the claimed sun-synchronous nodal precession.
- Orbit: The stated RAAN explanation is incorrect: RAAN is not determined by the launch facility's location, and a sun-synchronous orbit's node precesses about 360° per year, not necessarily eastward as described without sign or reference-frame clarification.
- Ground Control & Communications: The access table supports contact durations for the simulated orbit and facility, but the report does not specify communication link parameters or demonstrate that the available contact time and data rate can downlink the imagery.
- Mission Duration & EOL: The report proposes a drag sail but does not size it, estimate decay time, or show compliance with a disposal timeline. It also describes the spacecraft as having no thrusters without establishing how the sail is deployed or powered.
- Launch: Vega E was a planned future launcher in the report's proposed timeframe, not an established launch option. The contingency is mentioned, but there is no supported rideshare availability, payload interface, or launch-injection analysis.
- Orbit: The claimed coverage and imaging suitability are not supported by sensor parameters, ground resolution, swath, revisit analysis, or a quantitative assessment of underwater fluid-lensing performance.

## Next steps

1. In Launch, correct Kourou’s latitude and reassess the launch-window discussion. Verify the launch vehicle’s availability for your proposed timeframe and support feasibility with payload-interface, rideshare or injection information.
2. In Orbit, use a retrograde inclination near 97.8° for a 600 km sun-synchronous orbit, then verify the RAAN and nodal-precession explanation. Add sensor parameters and quantitative coverage, revisit and imaging-performance analysis.
3. In Ground Control & Communications and Mission Duration & EOL, show that link capacity supports the imagery and estimate drag-sail deployment and decay time. Clarify operator and customer organisations, strengthen and cross-check sources, and edit the incomplete EOL sentence and figure captions.

---
<sub>Run Input_2_d-Run_2-Eff_low-261118-125248 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15213/4787 | cost $0.003085 (incl. $0.001387 for the reused reference rubric+task structure) | 30.63s</sub>
