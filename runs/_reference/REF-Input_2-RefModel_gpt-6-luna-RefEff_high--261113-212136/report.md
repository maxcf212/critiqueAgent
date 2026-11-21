# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent preliminary reef-monitoring concept, explain why one spacecraft is proposed, and include STK evidence for orbit and access planning. To reach the next rubric level, substantiate key claims about imaging and revisit, launch compatibility, ground-station capability, sunlight conditions, and end-of-life disposal. Your conclusion and presentation also need stronger evidence-based synthesis and more consistent referencing and figure formatting.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the reef-monitoring purpose and environmental rationale, justifies using one spacecraft, and identifies likely science and government customers. To reach Accomplished, name the spacecraft operator explicitly, clarify the roles of operators and customers, and support the rationale with appropriate literature.

*Assessor reasoning:* The report explains the reef-monitoring purpose, environmental rationale, and reasons for using one spacecraft. It identifies likely science and government customers and Australian ground facilities, but does not clearly name the spacecraft operator or establish customer roles in detail.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

In Launch, Orbit, Ground Control & Communications, and Mission Duration & EOL, you address the major design elements and include STK access evidence (Images 1–5). To reach Accomplished, substantiate launch compatibility, imaging and revisit, station TT&C capability, link performance, and drag-sail decay time. Correct the RAAN and sunlight explanations and support access conclusions quantitatively.

*Assessor reasoning:* The report addresses launch, orbit and elements, manoeuvres, ground access, duration, EOL, and includes STK outputs and screenshots. However, key design claims are inadequately substantiated: imaging performance and revisit are not established, ground-station capability is assumed, and sunlight and EOL manoeuvre reasoning contain inconsistencies.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  
> Image 1  
> Image 4  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the main design choices and notes uncertainty about the launch vehicle. To reach Accomplished, draw detailed conclusions from demonstrated evidence and acknowledge limitations: in particular, qualify the claims about consistent illumination and Mount Pleasant access using verified orbit, coverage, and ground-station results.

*Assessor reasoning:* The conclusion recaps the principal design choices and their intended benefit, and notes a launch-vehicle uncertainty. It is appropriate but mostly summarizes earlier claims rather than drawing detailed conclusions from the evidence or acknowledging important limitations.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognizable engineering structure, an executive summary, and useful figures and data. To reach Accomplished, make figure and table numbering and titles consistent, improve writing and formatting consistency, and ensure every in-text citation matches a complete reference-list entry. Replace the cited Wikipedia source with an appropriate reference.

*Assessor reasoning:* The report has a recognizable engineering structure, executive summary, and useful figures and data. Writing and formatting are uneven, figures and tables are not consistently numbered and titled, and the reference list is incomplete and inconsistent; it also cites Wikipedia, which the task disallows.
> Contents: "Executive Summary ..... 2"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Ground Control & Communications: "The first fifteen access periods are listed above."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications; Images 1–5 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: The report treats RAAN as indicating the launch facility location. RAAN specifies the inertial orientation of the orbital plane; the launch site constrains achievable planes but does not determine RAAN by itself.
- Orbit; Ground Control & Communications: Sun-synchronous motion maintains approximately consistent local solar time, not continuous sunlight. A 600 km orbit will generally experience eclipses; the claim that the descending track is constantly sunlit is unsupported without specifying a dawn-dusk orbit.
- Orbit: The report selects 600 km and asserts daily reef-section imaging, but provides no payload field of view, ground sample distance, swath, pointing limits, or revisit/coverage analysis to demonstrate that capability.
- Ground Control & Communications: Mount Pleasant Radio Observatory is selected as a control station based on its radio telescopes, but the report does not establish that it has spacecraft TT&C equipment, compatible frequencies, or operational support for this satellite.
- Mission Duration & EOL: The report calls EOL disposal an orbital manoeuvre, then states the spacecraft has no thrusters and proposes a passive drag sail. It gives no drag-sail sizing or decay-time analysis to show disposal within an acceptable period.
- Launch: The launch discussion relies on a general equatorial-launch advantage without evaluating the implications of launching into a retrograde, approximately 98-degree orbit or substantiating Vega E payload and schedule compatibility.
- Ground Control & Communications: The access results cover only a short simulation interval and do not state the access elevation constraint or demonstrate data-rate/link-budget adequacy; the conclusion that contact is sufficient is therefore unsupported.

## Next steps

1. In Orbit, define the payload’s field of view, ground sample distance, swath, and pointing limits, then use coverage or revisit analysis to support the daily reef-imaging claim. Explain that RAAN describes orbital-plane orientation, not launch-site location, and that a sun-synchronous orbit does not guarantee continuous sunlight; support any illumination claim with the orbit design.
2. In Launch and Ground Control & Communications, assess Vega E’s payload and schedule compatibility for the proposed retrograde orbit. Establish that Mount Pleasant has suitable spacecraft TT&C equipment, frequencies, and operational support. State the access elevation constraint, extend the access analysis beyond a short simulation, and provide a link budget and data-rate basis for concluding that contact is sufficient.
3. In Mission Duration & EOL, reconcile the stated lack of thrusters with the proposed passive drag sail by sizing the sail and estimating decay time against an acceptable disposal period. Then strengthen the Conclusion by drawing only evidence-supported findings and limitations. For presentation, number and title figures and tables consistently, complete and cross-check citations, and replace Wikipedia with an appropriate source.

---
<sub>Run REF-Input_2-RefModel_gpt-6-luna-RefEff_high--261113-212136 | rubric=openai/gpt-6-luna, task=openai/gpt-6-luna, marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15255/7943 | cost $0.005878 | 76.02s</sub>
