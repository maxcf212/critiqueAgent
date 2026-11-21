# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You have built a clear, well-referenced case for a single sun-synchronous Earth-observation spacecraft, and your STK access results and ground-track evidence are a real strength. The main gaps are technical accuracy and closure: the RAAN rationale and Vega E timeline need correcting, the end-of-life strategy is unresolved, and the reference list has missing and inappropriate sources. Fixing these would lift the report substantially.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your primary mission, the rationale for it and your choice of a single spacecraft are clearly explained and supported by references, which is a solid base. To reach the next level, name the operator and specific customers rather than listing possible agencies, and support your comparison with constellation-based Earth-observation systems using credible, appropriate sources.

*Assessor reasoning:* Primary mission, rationale and single-spacecraft choice are well argued with references. Users are vague: the operator is not clearly named, and customers are listed as possible agencies rather than specified. Some citations are weak or unsuitable, which limits the mark.
> Introduction: "Other Earth observation satellites use networks or constellations of satellites"  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your STK access results, ground track and inclination-altitude plot provide good visual evidence. Key corrections are needed: RAAN is wrongly tied to the launch site, the Vega E date conflicts with your 2025 launch, and altitude reasoning is contradictory without a swath or ground sample distance calculation. Your end-of-life strategy is unresolved, and decay is not checked against the 25-year guideline.

*Assessor reasoning:* STK access results, ground track and inclination-altitude plot give reasonable evidence. However, RAAN is wrongly tied to launch site, the Vega E timeline conflicts with the 2025 launch, and the EOL strategy is unresolved and unquantified. A drag-sail sentence is broken, and no decay or 25-year compliance analysis is given.
> Orbit: "The orbit is near-polar and retrograde, meaning the satellite will pass over almost the entire Earth"  
> Orbit: "The initial value indicates the location of the launch facility."  
> Mission Duration & EOL: "In this orbit, atmospheric drag should cause the satellite to completely burn up upon re-entry."  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to"  

### C3 Conclusion (5/10, Adequate)

You reach some sensible conclusions, notably the risk of relying on a launch vehicle not yet built and the need for a fallback. However, the conclusion mainly restates the design. To reach the next level, draw specific conclusions from your evidence, such as whether the mission duration and end-of-life approach are adequate, and what your contact-time results mean for operations.

*Assessor reasoning:* The conclusion restates the design and notes launch-vehicle risk with a fallback. It is largely a summary, however, and does not draw specific conclusions from the evidence, such as EOL outcome, duration adequacy or the contact-time results.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans"  

### C4 Report presentation (8/20, Adequate)

Your report follows a clear, logical structure with headings that guide the reader. To improve presentation, replace the Wikipedia source, add the missing entries for citations [49] to [74], and resolve the duplicate use of [10]. Number your tables and figures consistently, complete the truncated drag-sail sentence, and correct the duplicated access period numbering in the Ground Control section.

*Assessor reasoning:* Headings and sections follow the required structure and the document is mostly readable. Presentation is weakened by a Wikipedia source, citations [49]–[74] absent from the bibliography, [10] used for two different sources, stray characters in references, a truncated sentence, unnumbered tables and figures, and a duplicated access number.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "It acts like a regular sail, utilising a large surface area to"  
> Ground Control & Communications: "The first fifteen access periods are listed above."  
> Launch: "February (TBD)"  

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
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: RAAN of 27.33° is described as indicating the launch facility location; RAAN is not set by launch site, and Kourou is near 53°W so the value is unjustified.
- Launch: Kourou (about 5°N) to a 97.8° retrograde orbit is an unusual, costly launch case; the report does not address azimuth or performance penalties.
- Launch: Claim that two launch windows per day occur because site latitude is smaller than inclination is loosely reasoned and not supported by calculation.
- Launch: Vega E stated to first launch in 2024, yet the mission is planned for 2025 and the alternatives section is based on a 2021 calendar; timeline is inconsistent.
- Orbit: Altitude selection reasoning is contradictory: high altitude is said to give low resolution yet this is called desirable, and no swath or GSD calculation is shown.
- Orbit: Daily imaging of the whole reef is claimed at 600 km without a revisit or swath calculation; orbital period is not stated.
- Orbit: Only argument of latitude and five elements are given; the claim that Keplerian elements fully describe the orbit lacks epoch and state details.
- Mission Duration & EOL: At 600 km, uncontrolled decay is not quantified against the 25-year guideline; claim of burn-up on uncontrolled descent is unsupported. Passive EOL is not resolved.
- Orbit: States the only manoeuvre is at EOL, yet the EOL strategy is passive and undecided, so manoeuvre requirements are inconsistent.
- Ground Control & Communications: Access table lists two entries numbered 13 and the text says fifteen periods, though numbering is inconsistent.

## Next steps

1. Resolve your end-of-life strategy in the Mission Duration and EOL section: quantify uncontrolled decay at 600 km against the 25-year guideline, remove the unsupported burn-up claim, choose passive or active disposal, and make the manoeuvre statements in the Orbit section consistent with it.
2. Correct the orbit design: remove the link between RAAN and the launch site and justify the RAAN from mission requirements. State the orbital period and epoch, and add swath, ground sample distance and revisit calculations to support your daily reef imaging claim and altitude choice. Also address the azimuth and performance penalties of launching from Kourou into a 97.8 degree retrograde orbit.
3. Tidy the launch timeline and references: align the Vega E first-launch date and the 2021 alternatives with your 2025 plan, replace the Wikipedia source, add entries for [49] to [74], and resolve the duplicate use of [10]. Then number all tables and figures and check every in-text citation against the reference list.

---
<sub>Run Input_2-Run_3-Eff_high-261115-170057 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21406/15247 | cost $0.009818 (incl. $0.001387 for the reused reference rubric+task structure) | 71.15s</sub>
