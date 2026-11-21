# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 58 / 100 (58%)**

Your reef-monitoring SSO mission concept is well structured and supported by genuine STK evidence covering nearly all requirements. However, several numerical errors (inclination, semi-major axis, Kourou latitude, contact duration), use of Wikipedia, and unnumbered figures/tables hold the report at Adequate. Fixing these accuracy and presentation issues is the clearest path to Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You clearly state the primary mission, justify why it is needed, and give a well-referenced rationale for a single spacecraft. To reach Accomplished, explicitly identify both users: name the operator (who owns/flies the satellite) and state the customer groups (e.g. marine and conservation scientists) directly rather than leaving them implied.

*Assessor reasoning:* Mission, rationale, and single-spacecraft choice are well covered with references. However, users are only implied: customers (marine/conservation scientists) are hinted at, but the operator is never explicitly identified, so not all requirements are fully addressed.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost"  
> Introduction: "A near-real-time relay to monitoring stations on the ground would allow marine and conservation scientists"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

All major requirements are addressed with good STK evidence (3D views, inclination plot, access report, ground tracks), and your launch, manoeuvre, ground station and EOL choices are justified. However, key values are inconsistent: 87.79° inclination contradicts your own plot and the 'retrograde' claim; a = 7171 km should be 6971 km; Kourou's latitude is ~5.2°N; and the 'twenty minutes' contact claim conflicts with your STK table (580.8 s). Also clarify the RAAN justification and the resolution-vs-altitude statement. Accurate, self-consistent numbers plus an appendix of STK files would support Accomplished.

*Assessor reasoning:* All major requirements addressed with STK evidence (3D views, inclination plot, access report, ground tracks). However, several technical errors: 87.79° inclination contradicts the student's own plot (~97.8°) and the 'retrograde' claim; a=7171 km should be 6971 km; Kourou latitude 45.05°N is wrong (~5.2°N); 'twenty minutes' contradicts the 580.8 s mean. Content adequate but not fully accurate.
> Mission Design - Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Mission Design - Orbit: "an altitude of 600km requires a mean inclination of $ 87.7924^{\circ} $"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "a 'drag sail' – a drag-enhancing deorbit device that deploys at the EOL"  

### C3 Conclusion (6/10, Adequate)

Your conclusions follow from the evidence and honestly flag the Vega E availability risk with a fallback, which is good practice. To reach Accomplished, deepen the synthesis: draw specific quantitative insights from your STK results (coverage, contact statistics, disposal timeline) rather than restating design choices, and reflect on limitations and how the design would be refined.

*Assessor reasoning:* Conclusions follow from the report's evidence and acknowledge a real risk (Vega E availability) with a fallback. However, the conclusion is brief and generic in places, reiterating design choices rather than synthesising deeper insight.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your report has a clear structure with headings, TOC and executive summary, and in-text citations match the reference list. To reach Accomplished: number and caption all figures and tables and refer to them in text; remove the Wikipedia reference (not an acceptable source); fix typos and broken sentences (e.g. 'purposed', the drag-sail sentence); and make formatting consistent throughout.

*Assessor reasoning:* Clear structure with headings, TOC and executive summary; references cited in text. But figures/tables lack numbers, Wikipedia is used (explicitly disallowed), and there are grammar/typo issues ('purposed', 'which is also desirable', broken drag-sail sentence). Formatting inconsistent in places.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Design - Orbit: "STK 3D view of orbit: 12 hours apart"  
> Ground Control & Communications: "for the purposed of this satellite"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction - 'Thus, only one satellite is required' |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction - customers implied (marine/conservation scientists); operator never explicitly identified |
| R4 | State the launch site and launch vehicle. | yes | Mission Design - Launch (Vega E from Kourou) |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Mission Design - Orbit - elements given but inclination (87.79°) and semi-major axis (7171 km) values are erroneous |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design - Orbit - 'the only orbital manoeuvre occurs at the EOL segment' |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications - Mt Pleasant Observatory with STK access summary |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL - five-year life, drag-sail disposal |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit/Ground Control sections - STK 11 used with plots and reports |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Screenshots included in body, but no appendix or statement that STK files are provided |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Structure is logical, but Wikipedia is cited (disallowed) and figures/tables are unnumbered |

## Technical issues

- Mission Design - Orbit: Inclination 87.79° is prograde and not sun-synchronous at 600 km (~97.8° required); contradicts the student's own inclination-vs-altitude plot and the 'retrograde' description.
- Mission Design - Orbit (COE table): Semi-major axis 7171 km is wrong: 6371 + 600 = 6971 km.
- Mission Design - Launch: Kourou's latitude stated as 45.05°N; actual is ~5.2°N.
- Ground Control & Communications: Claims 'almost twenty minutes' mean contact, but the STK table shows mean duration 580.786 s (~9.7 min).
- Mission Design - Orbit (COE table): RAAN 27.33° said to indicate launch facility location, inconsistent with Kourou (~52°W).
- Mission Design - Orbit: Text states low resolution from high altitude 'is also desirable' - contradicts the resolution requirement.
- Bibliography: Reference [6] is Wikipedia, explicitly not an acceptable source.

## Next steps

1. Recheck your sun-synchronous inclination calculation: at 600 km the required mean inclination is ~97.8° (retrograde), not 87.79°, and correct the semi-major axis to 6371 + 600 = 6971 km in your COE table.
2. Cross-check every quoted number against your own STK outputs before submission - e.g. the mean contact duration is 580.8 s (~9.7 min), not 'almost twenty minutes', and Kourou's latitude is ~5.2°N, not 45.05°N.
3. Number all figures and tables, cite them in the text, replace the Wikipedia reference with an acceptable source, and add an appendix (or a statement) confirming your STK files are provided.

---
<sub>Run Input_2_d-Run_2-Eff_high-261116-112718 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15437/5520 | cost $0.002893 (incl. $0.001387 for the reused reference rubric+task structure) | 86.58s</sub>
