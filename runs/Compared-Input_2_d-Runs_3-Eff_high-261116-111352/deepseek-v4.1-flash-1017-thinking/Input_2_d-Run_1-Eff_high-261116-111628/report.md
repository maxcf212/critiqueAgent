# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a clear, well-motivated reef-monitoring mission with a justified single-satellite concept and structured coverage of launch, orbit, ground control, duration and EOL, supported by STK screenshots. Credibility is reduced by the incorrect SSO inclination (87.79° vs ~97.8°), wrong Kourou latitude, overstated contact duration, missing link/swath calculations and STK files, and weak referencing. Addressing these will lift the report from Adequate toward Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly explain the mission need and single-satellite rationale with references. To reach Accomplished, explicitly identify the operator and customers (not just implicit Australian facilities, UTAS and scientists), add detailed user/operations discussion, and use quality literature rather than bare URLs. Keep the strong rationale.

*Assessor reasoning:* Mission and rationale are clearly presented with references, and the single-satellite choice is justified. Users are only implicit (Australian facilities, University of Tasmania, scientists); operator and customers are not explicitly defined, and references are mostly bare URLs. Adequate high.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Executive Summary: "is operated and accessed from Australia ground facilities"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover launch, orbit, ground control, duration and EOL with STK screenshots. Next level requires correcting the SSO inclination (~97.8°, not 87.79°), Kourou latitude (~5.2°N) and contact duration (~9.7 min mean); adding GSD/swath and link-budget calculations; including STK files; and supporting drag-sail EOL with deorbit-lifetime and compliance evidence.

*Assessor reasoning:* Most required design elements are covered and STK evidence is included, but the orbit definition is self-contradictory/wrong: 600 km SSO inclination should be ~97.8°, not 87.79°. Kourou latitude is wrong, mean contact claim is wrong, no link/swath calculations, no STK files. Adequate.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "requires a mean inclination of $ 87.7924^{\circ} $"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (5/10, Adequate)

Your conclusion restates launch, orbit and ground-station choices. To reach Accomplished, include key quantitative outcomes (altitude, inclination, contact statistics, mission lifetime), state the EOL approach, and avoid overclaiming a fully described configuration. Tie conclusions directly to evidence in the main body.

*Assessor reasoning:* Conclusion restates launch, orbit and ground-station choices, but is brief, omits EOL and key quantitative results, and overclaims that a fully described configuration was constructed. Some specific conclusions but generic.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Structure, headings and executive summary are clear. Next level requires numbered/captioned figures and tables, consistent formatting, and a reference list matching all in-text citations (including [49]–[74]); replace Wikipedia with credible sources and proofread grammar. This will make the report professional and easy to follow.

*Assessor reasoning:* Structure and headings are clear and an executive summary is present, but figures/tables lack numbering/titles, references are bare URLs and do not match in-text citations (e.g. [49]-[74] missing), Wikipedia is used, and grammar slips occur. Adequate low.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Executive Summary/Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Executive Summary/Introduction/Ground Control & Communications |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit/Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit/Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit/Ground Control & Communications (no files/appendix) |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Report structure/Bibliography |

## Technical issues

- Launch: Kourou latitude is given as 45.05°N; Guiana Space Centre is about 5.2°N, so launch-site geometry discussion is wrong.
- Orbit: SSO inclination for 600 km is stated as 87.79°; correct value is about 97.8° retrograde. The graph indicates ~97.8°, so text/table are inconsistent and the defined orbit is not sun-synchronous.
- Orbit: Initial RAAN 27.33° is said to indicate launch facility; RAAN at epoch depends on launch time/date, not simply site.
- Ground Control & Communications: Average contact duration stated as almost 20 min; table mean 580.786 s ≈ 9.7 min (max 12.8 min).
- Ground Control & Communications: Claim descending path is constantly sunlit is unsupported; SSO normally has eclipses unless a dawn-dusk local-time orbit is specified.
- Orbit: No GSD/swath calculation; text says low resolution 'also desirable' where likely undesirable, undermining altitude rationale.
- Ground Control & Communications: No link budget/data rate or ground-station capability analysis to show image data can be downlinked.
- Mission Duration & EOL: Drag-sail EOL chosen without deorbit lifetime/ballistic coefficient calculation or debris-mitigation compliance demonstration.
- Mission Duration & EOL: Text says only orbital manoeuvre occurs at EOL but then selects passive drag sail and says no thrusters; does not clearly state no operational manoeuvres.
- Launch/Bibliography: Uses Wikipedia '2021 in spaceflight' and tables with citations [49]-[74] absent from reference list; not acceptable source.
- Report: No STK/PIGI software files included with report/appendix; only screenshots.

## Next steps

1. Correct the orbital geometry: recompute the 600 km SSO inclination (~97.8° retrograde), fix Kourou's latitude (~5.2°N), and re-run STK so text, table and figure agree. Add a GSD/swath calculation to justify the 600 km altitude and clarify why low resolution is undesirable.
2. Strengthen quantitative evidence: reconcile the mean contact duration (~9.7 min, not almost 20 min), add a link budget/data-rate and ground-station capability analysis, and support the drag-sail EOL with deorbit-lifetime/ballistic-coefficient and debris-mitigation compliance calculations.
3. Improve evidence and referencing: include STK/PIGI files in an appendix, number and caption all figures/tables, replace the Wikipedia source, ensure citations [49]–[74] appear in the reference list, and explicitly define the operator and customers in the Introduction.

---
<sub>Run Input_2_d-Run_1-Eff_high-261116-111628 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14573/13149 | cost $0.009177 (incl. $0.001387 for the reused reference rubric+task structure) | 96.7s</sub>
