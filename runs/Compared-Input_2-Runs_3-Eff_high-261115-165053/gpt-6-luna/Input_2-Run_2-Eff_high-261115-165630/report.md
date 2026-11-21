# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 49 / 100 (49%)**

You present a coherent preliminary reef-monitoring concept, explain why one spacecraft may be suitable, and use STK access results to support the design. To progress, turn the preliminary choices into a verifiable mission design: substantiate payload, orbit, communications, launch, and disposal feasibility, then make the conclusion and references consistent with that evidence.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction explains the reef-monitoring need and why one spacecraft may suffice, and identifies potential users such as CSIRO and BOM. For the next level, define who operates the spacecraft and who the operational or paying customers are, and support the stakeholder discussion with appropriate references.

*Assessor reasoning:* The report explains the reef-monitoring mission, its environmental rationale, and why one spacecraft is proposed. Potential users are identified, but the operator and paying or operational customers are not clearly assigned; the user discussion is tentative rather than a defined stakeholder model.
> Introduction: "The ZYZZsat however, does not require such constant coverage as the reef bleaching events occur over days and weeks. Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your Launch, Orbit, Ground Control & Communications, and Mission Duration & EOL sections cover the main design topics, and the STK access results provide useful evidence. To reach the next level, substantiate the launch opportunity, complete the orbit specification and eclipse analysis, demonstrate payload and link performance, provide STK files, and quantify disposal feasibility.

*Assessor reasoning:* The report addresses launch, orbit elements, manoeuvres, a named ground facility, STK access results, duration, and disposal, with useful simulation imagery and output. However, it does not provide the STK project files, a complete orbit specification including epoch/local solar time, payload or imaging-performance design, or a substantiated link and disposal analysis. Several design claims are technically unsupported or inconsistent.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $ for the satellite to remain sun-synchronous."  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan of the proposed satellite."  

### C3 Conclusion (5/10, Adequate)

Your Conclusion recaps the selected launch, orbit, and ground facility in relation to the mission. To reach the next level, draw detailed conclusions from the analysis and qualify claims about illumination and ground contact where the report has not established them.

*Assessor reasoning:* The conclusion recaps the selected launch, orbit, and ground facility and relates them to the mission purpose. It is largely a summary, however, and makes confident claims about illumination and ground contact that are not fully established by the analysis.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Your report has an executive summary, contents, headings, and relevant figures. For the next level, improve writing consistency, formally and consistently caption figures and tables, and ensure all in-text citations match the bibliography; replace the Wikipedia source and resolve unmatched citation numbers.

*Assessor reasoning:* The report has a recognisable structure, executive summary, contents, headings, and relevant figures. Grammar and phrasing are uneven, figures and tables are not consistently numbered or formally captioned, and citation practice is weak: several in-text numeric citations have no matching bibliography entry, and Wikipedia is used despite the task disallowing it.
> Executive Summary: "This report outlines the intended designs and procedures involved in the construction of a Earth observation satellite"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Ground Control & Communications |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Orbit: The report does not specify the local time of the ascending node or an epoch for its orbital elements. The stated RAAN does not by itself indicate the launch facility, and the claim that it does is incorrect.
- Orbit: Sun-synchronous orbit maintains a near-constant local solar time for a given ground track; it does not establish continuous sunlight or prove that the descending passes are always illuminated. The report gives no local-time selection or eclipse analysis.
- Orbit: No payload specifications, ground-sample distance, spectral bands, swath, or imaging-performance analysis supports the proposed satellite fluid-lensing application or the claimed ability to detect bleaching.
- Ground Control & Communications: The report gives STK access intervals but no satellite-to-ground link budget, communications frequency, data volume, or evidence that the Mount Pleasant Radio Observatory has the equipment and operational capability to serve as the proposed spacecraft ground-control station.
- Mission Duration & EOL: The drag-sail disposal proposal has no sail sizing or orbit-decay estimate for a 600 km orbit, so the time to re-entry and debris-mitigation outcome are not demonstrated. The text also initially describes an orbital manoeuvre at EOL, then states the spacecraft has no thrust capability.
- Launch: The Vega E is selected without verifying a specific rideshare opportunity, injection orbit, capacity, or schedule. The proposed direct injection into the specified orbit is therefore not demonstrated.
- Bibliography: In-text references in the launch tables include citation numbers such as [49] and [74], but the bibliography contains only entries [1]–[10]; [6] also cites Wikipedia, which the assignment explicitly excludes.

## Next steps

1. In Orbit and Ground Control & Communications, specify the orbit epoch and local solar time, assess eclipses, and support imaging and bleaching-detection claims with payload performance. Add a link budget, frequency and data-volume estimates, and evidence that Mount Pleasant can provide the proposed ground-control service; include the STK project files.
2. In Launch and Mission Duration & EOL, verify the launch vehicle’s rideshare opportunity, injection orbit, capacity and schedule. Resolve the EOL manoeuvre inconsistency and quantify drag-sail sizing and orbit decay at 600 km.
3. Strengthen the Introduction by assigning operator and customer roles, and revise the Conclusion to draw only evidence-supported findings. In the Bibliography, ensure every in-text citation has a matching entry, remove the prohibited Wikipedia source, and improve figure/table captions and writing consistency. 

---
<sub>Run Input_2-Run_2-Eff_high-261115-165630 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15246/6803 | cost $0.004091 (incl. $0.001387 for the reused reference rubric+task structure) | 42.03s</sub>
