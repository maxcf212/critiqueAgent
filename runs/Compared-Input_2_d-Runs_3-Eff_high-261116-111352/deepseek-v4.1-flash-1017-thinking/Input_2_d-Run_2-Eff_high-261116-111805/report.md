# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

Your report is readable and logically structured, and you cover all major design elements with STK evidence. The main weaknesses are numerical: the 87.79° inclination is prograde and inconsistent with a 600 km sun-synchronous orbit (~97.8°), Kourou's latitude is ~5.2°N not 45.05°N, and your 20-minute contact claim contradicts the 580.8 s table. Presentation and referencing also need work.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

You argue the fluid-lensing reef/ocean mission need well and justify a single satellite with references. To reach Accomplished, explicitly define the operator and customers (who tasks, owns, and receives data) rather than implying them, and ensure all introduction claims are referenced.

*Assessor reasoning:* Mission purpose (fluid-lensing reef/ocean monitoring) and rationale are well argued with references, and single-satellite choice is justified. However, users are only implied (scientists, Australian facilities); operator and customer relationships are never explicitly defined.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists to more accurately predict and react"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground control, communications, duration and EOL with STK screenshots. To reach Accomplished, correct the 87.79° prograde inclination to ~97.8° for a 600 km SSO, fix Kourou's latitude to ~5.2°N, and reconcile the 20-minute contact claim with your 580.8 s table. Add GSD/swath/FOV and downlink calculations, STK files, target-coverage analysis, and drag-sail sizing/re-entry timeline.

*Assessor reasoning:* All major design elements are covered with STK evidence, but key numbers are wrong: SSO inclination at 600 km must be ~97.8° (prograde 87.79° contradicts the 96.5–99.5° plot and retrograde claim); Kourou latitude is 5.2°N; stated 20-min mean contact contradicts the 581 s table value. No sensor/swath or GSD calculation, no STK files, no target-coverage analysis.
> Orbit: "an altitude of 600km requires a mean inclination of 87.7924°"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Launch: "situated very close to the equator, with a latitude of 45.05°N" *(quote not found in submission)*  

### C3 Conclusion (5/10, Adequate)

Your conclusion restates launch, orbit, ground station and EOL, and notes the Vega E fallback. To reach Accomplished, draw quantified conclusions from your analysis—revisit frequency, contact time, data volume—and acknowledge the inclination error and launch-vehicle immaturity as caveats rather than only restating choices.

*Assessor reasoning:* Conclusion summarises launch, orbit, ground station and EOL with a sensible launch fallback, but is largely restatement; no quantified outcomes (coverage frequency, data volume, revisit) or caveats about the inclination error are drawn from the analysis.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your structure, executive summary and prose are clear. To reach Accomplished, number and caption all figures and tables consistently, replace bare/broken URLs and the Wikipedia entry with properly formatted references, and cite every claim (e.g., solar panels extending life). Ensure in-text citations match the reference list.

*Assessor reasoning:* Clear structure, executive summary and readable prose; figures are captioned informally but unnumbered, tables unlabelled, and two are pasted raw wiki tables. Bibliography is bare URLs, several broken, includes Wikipedia (explicitly disallowed) and an uncited claim that solar panels extend life.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 4  
> Bibliography: "[10 d. ] https://www.thespacereview.com/article/3887/1"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design – Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Orbit / Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | partial | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 1–5 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: Inclination 87.79° is prograde; sun-synchronous at 600 km requires ~97.8°, consistent with the supplied figure but contradicting the quoted value and the retrograde claim.
- Launch: Kourou latitude given as 45.05°N; actual is ~5.2°N, which undermines the two-launch-windows-per-day argument.
- Ground Control & Communications: Mean contact duration stated as ~20 min, but table gives 580.8 s (9.7 min); min 151 s also suggests an access constraint worth explaining.
- Orbit: Claim that a very high altitude yields low resolution 'which is also desirable' is incorrect reasoning; no swath/GSD/FOV calculation supports the 600 km choice.
- Orbit: RAAN of 27.33° is asserted as indicating the launch site without derivation or launch epoch justification.
- Mission Duration & EOL: No mass/area estimate, drag-sail sizing, or re-entry timeline; 'uncontrolled descent' is incompatible with a thrusterless satellite before the passive drag-sail option is introduced.
- Launch: Reliance on a not-yet-flown Vega E and 2021 rideshare manifests as a 2025 baseline is weakly justified.
- Executive Summary: Fluid-lensing sensor requirements (GSD, spectral bands, data rate) are never quantified, so the downlink budget is not validated.

## Next steps

1. Recompute and verify the sun-synchronous inclination for 600 km and correct Kourou's latitude; reconcile the stated mean contact duration with your 580.8 s table and explain the 151 s minimum access constraint.
2. Add sensor GSD/swath/FOV and downlink-budget calculations, include STK files and target-coverage analysis, and size the EOL drag sail with a mass/area estimate and re-entry timeline.
3. Number and caption all figures and tables, replace bare/broken URLs and the Wikipedia entry with proper references, explicitly define operator and customers, and make the conclusion draw quantified outcomes and caveats.

---
<sub>Run Input_2_d-Run_2-Eff_high-261116-111805 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14456/5884 | cost $0.004709 (incl. $0.001387 for the reused reference rubric+task structure) | 30.7s</sub>
