# AERO9500 Final Report (Part 2) — Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent preliminary concept for a single satellite to monitor reefs and explain its Australian benefit. Your report uses STK and covers the main mission-design topics, but important claims about imaging performance, ground communications and end-of-life disposal need evidence. Strengthening the technical analysis, conclusions and referencing would help you reach the next rubric level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale (primary mission, need, number of spacecraft and rationale, operator and customers) | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design (design method and evidence; launch site, vehicle and rationale; orbit and elements; maneuvers; ground control and communication frequency; mission duration and EOL) | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale (primary mission, need, number of spacecraft and rationale, operator and customers) (6/10, Adequate)

In the Introduction, you explain the reef-monitoring purpose, Australian benefit and choice of one spacecraft, and identify likely users such as CSIRO and BOM. To reach Accomplished, clearly specify who operates the satellite and support the rationale with stronger references and evidence that the mission can meet its users’ needs.

*Assessor reasoning:* The reef-monitoring mission and its Australian benefit are explained, and the report justifies using one spacecraft. Likely users and funding sources are identified, but the operator is not clearly specified. The rationale is useful but does not establish detailed mission performance or cite all claims with strong sources.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design (design method and evidence; launch site, vehicle and rationale; orbit and elements; maneuvers; ground control and communication frequency; mission duration and EOL) (30/60, Adequate)

Your Launch, Orbit, Ground Control & Communications, and Mission Duration & EOL sections address the major design topics and include STK output and visualisations. To reach Accomplished, quantify payload performance and reef coverage, verify Mount Pleasant’s TT&C and downlink capability, analyse disposal timing, and correct the RAAN, sunlight and access-output interpretations.

*Assessor reasoning:* The report addresses launch, orbit, communications, mission duration and EOL, and includes STK output and visualisations. However, key design evidence is incomplete: imaging performance and reef coverage are not quantified, the proposed ground facility's spacecraft-communications capability is not established, and EOL disposal is not timed or analysed. Some orbit and access interpretations are incorrect.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  
> Image 4  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the selected launch, orbit and ground station and links them to the mission purpose. To reach Accomplished, evaluate what the design evidence demonstrates, acknowledge limitations such as eclipse periods and unverified imaging or communications performance, and explain how these affect mission feasibility.

*Assessor reasoning:* The conclusion recaps the selected launch, orbit and ground station and connects the design to the mission purpose. It is mostly a summary rather than a detailed evaluation of evidence, limitations or unresolved risks.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (8/20, Adequate)

Your report has a logical structure, an executive summary and labelled sections and figures, including the STK material in Ground Control & Communications. To reach Accomplished, improve wording and grammar, use consistent professional formatting, provide complete in-text citations and reference entries, and replace the prohibited Wikipedia source.

*Assessor reasoning:* The report has a logical structure, an executive summary, labelled sections and useful figures. Writing and formatting are generally understandable but have grammatical and wording flaws. References are mostly bare URLs, the bibliography includes Wikipedia despite the task's prohibition, and some table citations are absent from the bibliography.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Ground Control & Communications: "The first fifteen access periods are listed above."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Define the primary mission and explain how it benefits Australia; keep the mission concept simple. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the users, including the operator and customers. | partial | Introduction |
| R4 | Specify the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify the ground-control facilities and state how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify the mission duration and end-of-life plan. | yes | Mission Duration & EOL |
| R9 | Use mission-design software of your choice (STK or PIGI are suggested); contact the course representative before using other software. Supplement the design with hand calculations where useful. | yes | Ground Control & Communications |

## Technical issues

- Orbit: The report says the near-polar orbit provides a constant supply of sunlight. A 600 km sun-synchronous orbit can have eclipse periods; sunlight availability depends on beta angle and season.
- Orbit: The table says the initial RAAN indicates the launch-facility location. RAAN specifies the orbital plane's orientation relative to the reference direction; it is not determined by the launch site's location alone.
- Ground Control & Communications: Mount Pleasant is identified as a radio observatory, but the report does not establish that it has suitable satellite TT&C or data-downlink equipment, frequencies, or a control capability.
- Ground Control & Communications: The access output contains a repeated access entry and an apparent date/time wrap or discontinuity. The report does not reconcile these features before using the listed periods to support its contact statistics.
- Orbit: No sensor swath, ground-sample distance, pointing limits, or image-quality analysis is provided to show that a 600 km orbit and proposed payload can image the reef adequately.
- Mission Duration & EOL: The drag-sail proposal has no area, decay-time estimate, or demonstration that the spacecraft will meet an applicable post-mission disposal timeframe.
- Bibliography: The bibliography cites Wikipedia, which the task explicitly disallows, and several numbered citations appearing in the launch tables are not matched by bibliography entries.

## Next steps

1. Specify the spacecraft operator and develop the mission rationale with credible sources and measurable user requirements.
2. Validate mission feasibility with payload and coverage calculations, confirmed ground-station communications capability, corrected orbit/access analysis, and an estimated drag-sail decay time.
3. Revise the conclusion to assess evidence and limitations, then check grammar, citation matching and reference quality throughout the report.

---
<sub>Run 20261112-024529-727_Input_2_md_gpt-6-luna | rubric=openai/gpt-6-luna, task=openai/gpt-6-luna, marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 14615/5366 | cost $0.004509 | 145.86s</sub>
