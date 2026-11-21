# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 48 / 100 (48%)**

You have covered the required mission segments, and your STK access results and COE table give useful evidence. Your mission purpose and rationale are clear. The main gaps are technical consistency in the launch and orbit logic, an incomplete end-of-life analysis, a conclusion that mostly restates the design, and references that do not meet the brief. Addressing these would move your report up a band.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Deficient | 2 / 10 | 2 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

You state the spacecraft's purpose clearly and explain why one spacecraft is sufficient, with useful background on the reefs. To reach the top band, name operators and customers separately and justify your funding assumptions rather than presenting them as speculative. Your Wikipedia source breaches the stated rules, so replace it with an authoritative reference such as a peer-reviewed paper or agency document.

*Assessor reasoning:* Mission purpose, rationale and single-spacecraft choice are given with background on reefs. Users are named only loosely (agencies, possibly university), with no clear operator/customer distinction and funding is speculative. Referencing is partly from weak sources and Wikipedia is used despite the explicit prohibition.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your orbit and STK access results are presented with a COE table and screenshots, which is good evidence. The launch section needs resolving: you name Vega VV18 as the rideshare option but select Vega E, which is not yet built, and this conflicts with your 2025 date. Justify your RAAN value, correct the launch window argument, and reconsider Mount Pleasant as an operational ground station. Include your software files.

*Assessor reasoning:* Orbit and STK access results are presented with a COE table and screenshots. However, the launch section is inconsistent (Vega VV18 vs Vega E from Kourou, while also claiming a 2025 launch), the RAAN value is unjustified and not tied to the launch site, the orbit is described as retrograde yet the RAAN/launch logic is confused, and the Mount Pleasant ground station is a radio observatory, not a practical operator facility. EOL is unfinished (truncated drag-sail text), and 5.05°N latitude for Kourou is roughly correct but the 'larger than inclination' window argument is wrong. Software files not evidenced.
> Orbit: "the satellite will be positioned at an altitude of 600km above Earth’s surface"  
> Orbit: "Ω 27.33° The initial value indicates the location of the launch facility."  
> Ground Control & Communications: "Mount Pleasant Radio Observatory"  

### C3 Conclusion (2/10, Deficient)

Your conclusion mainly restates the design rather than drawing conclusions from your evidence. Summarise what your access and orbit results show about performance, note limitations such as the unbuilt launch vehicle, and state what your end-of-life analysis implies. Remove unsupported claims about preventing bleaching, and tie each conclusion to a specific result.

*Assessor reasoning:* Conclusion mainly restates the design with generic claims; it does not draw evidence-based conclusions about performance, limitations, or EOL outcomes, and it introduces unsupported statements about preventing bleaching.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your report follows the requested headings and captions its figures, which supports readability. Improve consistency in figure references and access table numbering, and tighten grammar where sentences are unclear. Replace the Wikipedia reference, and ensure every in-text citation matches a reference list entry in a consistent format.

*Assessor reasoning:* Structure follows requested headings with figures captioned, but there are truncated sentences, a broken table, mislabelled figure references, inconsistent numbering of access tables, and unformatted citations. Wikipedia reference breaches the stated rules and in-text citations are not consistently tied to references.
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’ – a drag-enhancing deorbit device that deploys at the EOL. It acts like a regular sail, utilising a large surface area to ‘ and is suitable"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | partial | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | partial | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Launch: Vega VV18 is said to be the rideshare option but the design then selects Vega E from Kourou, which is not yet built, creating inconsistency with the claimed 2025 launch.
- Launch: Claims the launch window count depends on latitude being smaller than inclination; the reasoning is confused and does not justify the choice.
- Orbit: RAAN of 27.33° is stated as the launch facility location, but RAAN is not set by the site alone; no justification from launch time or sun-synchronous node drift is given.
- Orbit: Says a sun-synchronous orbit requires RAAN to change 360° per year, yet also that the orbit is retrograde while describing 'near-polar' without giving the sun-synchronous rate calculation.
- Ground Control & Communications: Stated that polar ground stations maximise pass frequency; the Tasmanian site is not polar and the choice is justified against the stated logic.
- Mission Duration & EOL: Claims uncontrolled descent requires least energy but then the drag sail is proposed without any deorbit time or altitude analysis.

## Next steps

1. Resolve the launch inconsistency: choose one launch vehicle and site that is available for your 2025 date, and justify that choice clearly.
2. Justify your RAAN and orbit choice with a sun-synchronous rate calculation, and complete the end-of-life section with a deorbit time or altitude analysis for the drag sail.
3. Replace the Wikipedia source with credible references, and rewrite the conclusion to draw evidence-based conclusions from specific results.

---
<sub>Run Input_2-Run_3-Eff_low-261118-113518 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21144/6177 | cost $0.005256 (incl. $0.001387 for the reused reference rubric+task structure) | 32.18s</sub>
