# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 44 / 100 (44%)**

You proposed a plausible single-satellite GBR reef-monitoring mission with STK modelling across launch, orbit and ground segments. To reach Accomplished you need to correct critical technical errors, fully define users and EOL, and tighten presentation and referencing with quantitative synthesis.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You described your coral reef and ocean monitoring mission and GBR bleaching need well, with clear single-satellite rationale to allow marine and conservation scientists to predict bleaching. For Accomplished, explicitly name the operator versus customers and add detailed discussion with complete literature references.

*Assessor reasoning:* Primary mission, need for GBR bleaching and single-satellite rationale well described with references. Operator vs customers vague: operated from Australia facilities, users implied scientists, no explicit operator/customer definition.
> Introduction: "specifically for coral reef and ocean monitoring"  
> Introduction: "Thus, only one satellite is required"  
> Introduction: "allow marine and conservation scientists to more accurately predict"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

You covered launch with Vega E, orbit and Mount Pleasant Radio Observatory with STK views, ground-tracks and access table. For Accomplished, correct your 87.79 deg inclination to ~97.8 deg retrograde to match Image 3, fix Kourou latitude and RAAN logic, correct mean contact to ~9.7 min, and resolve EOL contradiction with supported calculations.

*Assessor reasoning:* All segments addressed with STK views, ground-tracks and access table. Critical errors: SSO inclination given as 87.79 deg prograde vs required ~97.8 deg retrograde, Kourou latitude wrong, RAAN logic wrong, EOL manoeuvre contradictory.
> Launch: "will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "an altitude of 600km requires a mean inclination of"  
> Ground Control & Communications: "the Mount Pleasant Radio Observatory"  
> Image 4  

### C3 Conclusion (5/10, Adequate)

You summarised polar sun-synchronous orbit for consistent illumination and Mt Pleasant for data receipt with Vega E caveat in your Conclusion. For Accomplished, move beyond restatement to detailed conclusions synthesising quantitative evidence on coverage, access and lifetime to prove mission benefit.

*Assessor reasoning:* Summarises launch, orbit, ground station and benefit for bleaching monitoring. Largely restates design with caveat on Vega E availability, but generic and lacks quantitative synthesis from evidence.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans"  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data"  

### C4 Report presentation (10/20, Adequate)

Your Executive Summary and logical headings made your report readable. For Accomplished, add numbered figure/table titles, ensure in-text citations match your Bibliography, replace Wikipedia with approved sources, and use consistent academic formatting throughout.

*Assessor reasoning:* Logical headings and readable prose with executive summary. Figures/tables lack numbers/titles, reference formatting broken, Wikipedia used despite prohibition, in-text citations loosely matched.
> Executive Summary: "This report outlines the intended designs and procedures involved"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight"  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: 600 km SSO inclination stated as 87.79 deg; correct ~97.8 deg. 87.79 deg is prograde, contradicts claimed retrograde near-polar SSO and Image 3 plot.
- Launch: Kourou latitude stated as 45.05 deg N; actual ~5.2 deg N. Invalidates launch-window reasoning.
- Orbit: RAAN 27.33 deg claimed to indicate launch facility location; RAAN does not encode launch site and value unjustified.
- Ground Control & Communications: Mean contact claimed almost twenty minutes; table mean 580.8 s (~9.7 min), max 770 s. Overstatement ~2x.

## Next steps

1. Correct your Orbit SSO inclination from 87.79 deg to ~97.8 deg retrograde at 600 km to match Image 3, and fix your RAAN 27.33 deg launch-site logic.
2. Correct Kourou latitude from 45.05 deg N to ~5.2 deg N with revised launch reasoning, and correct your mean contact from almost twenty minutes to 580.8 s (~9.7 min) from your access table.
3. Explicitly define your operator versus customers in the Introduction, resolve your EOL manoeuvre contradiction, and add figure numbers/titles with matched Bibliography references without Wikipedia.

---
<sub>Run Input_2_d-Run_1-Eff_high-261116-111355 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14869/8044 | cost $0.003819 (incl. $0.001387 for the reused reference rubric+task structure) | 45.75s</sub>
