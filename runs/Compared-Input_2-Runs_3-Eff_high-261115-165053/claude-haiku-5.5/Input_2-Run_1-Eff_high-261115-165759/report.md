# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You have set out a clear, well-motivated single-satellite concept in the Introduction, with a sensible sun-synchronous inclination at 600 km and useful STK access analysis. The main gaps are in the technical reasoning: the launch-site argument needs revisiting for a retrograde orbit, the RAAN and manoeuvre statements need correcting, and the end-of-life and referencing need completing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction clearly states the primary mission, the bleaching and fluid-lensing rationale, why one spacecraft suffices, and the likely users. To reach Accomplished, name the operator precisely rather than 'Australia ground facilities', justify or remove the speculative funding comment, and replace the URL-only bibliography with full literature references.

*Assessor reasoning:* Primary mission, rationale (bleaching, fluid lensing), single-spacecraft choice and customers are all addressed with reasoned detail. The operator is vague ('operated and accessed from Australia ground facilities') and funding is speculative. Introduction references are present, but the bibliography is URL-only and incomplete, so referencing is only partly adequate.
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your strongest evidence is the sun-synchronous inclination (about 97.8° at 600 km), the STK access analysis and the orbit screenshots. The launch reasoning and RAAN explanation are currently inverted or incorrect, and the manoeuvre claims contradict the no-thrust design. To reach Accomplished, support major requirements with calculations (period, swath, GSD, decay), correct these errors, and justify the Mount Pleasant downlink with frequency and data rate.

*Assessor reasoning:* Strengths: SSO inclination for 600 km (about 97.8°) checks out, and STK access data and orbit screenshots are provided. Weaknesses: equatorial-launch logic is inverted for a retrograde orbit; the Vega E is unbuilt; the RAAN explanation is wrong; no local time of descending node, period or swath/GSD sizing; manoeuvre statements contradict; no decay analysis; EOL drag-sail text is truncated; the access table is mis-numbered.
> Mission Design – Launch: "The most efficient rocket launches are from locations close to the equator as this is where maximum rotational velocity can be experienced [5]."  
> Mission Design – Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit – orbital elements table: "The initial value indicates the location of the launch facility."  
> Orbit: "the only orbital manoeuvre occurs at the EOL segment of the satellite's mission."  
> Mission Duration & EOL: "However, the ZYZZsat is without thrust capability and so must use a ‘passive’ strategy."  
> Ground Control & Communications: "The first fifteen access periods are listed above."  

### C3 Conclusion (5/10, Adequate)

Your conclusion makes sensible points about constant illumination and launch-vehicle risk, but it is largely generic. It does not cite quantitative results such as contact durations, pass counts or EOL lifetime. To reach Accomplished, summarise the key numbers from your analysis, state what they show, and acknowledge the remaining limitations.

*Assessor reasoning:* The conclusion draws some reasonable points, including the launch-vehicle risk and the ground-station choice. However, it largely restates the design without quantitative evidence such as contact durations, pass counts or EOL lifetime. It does not acknowledge the unresolved issues in the body, so it is somewhat generic.
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (8/20, Adequate)

The report has a clear heading structure and an executive summary, and most figures are captioned. Citation consistency is the main weakness: in-text references run beyond the bibliography, one number is used for two sources, entries are garbled, and Wikipedia is cited. To reach Accomplished, fix every citation, label all tables and Image 3 consistently, and proofread for grammar and typos.

*Assessor reasoning:* Headings and a clear section structure with an executive summary are present, and most figures carry captions. Citations are seriously inconsistent: in-text numbers run to [74] but the bibliography lists only [1]–[10], [10] is used twice, entries are garbled, and Wikipedia is cited. Frequent grammar and typo errors, unnumbered tables and an uncaptioned Image 3 further reduce quality.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Design – Launch: "It’s first launch will occur in 2024"  
> Introduction: "construction of a Earth observation satellite"  
> Mission Design – Launch table: "February (TBD)"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design – Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit; Mission Duration & EOL |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit and Ground Control (Images 1–5); STK files not evident |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Whole document |

## Technical issues

- Mission Design – Launch: Equatorial launch is argued to be most efficient, but Earth-rotation benefit largely disappears for a retrograde ~98° orbit. Plane-change penalty from 5°N is not analysed.
- Orbit – orbital elements table: RAAN is said to indicate the launch facility location. RAAN depends on launch time/epoch and site longitude; no epoch is given. Table also uses Earth radius 6371 km, inconsistent with STK's 6378 km.
- Orbit: Sun-synchronous daytime imaging is claimed but local time of descending node is never specified. Orbit period, swath width and ground sample distance are not calculated, so 600 km and 'daily' coverage are unsupported.
- Orbit / Mission Duration & EOL: The only orbital manoeuvre is said to occur at EOL, yet the satellite is stated to have no thrusters, so manoeuvre claims are contradictory.
- Mission Duration & EOL: A five-year life at 600 km with passive disposal is asserted without decay or lifetime analysis. STK run 2025–2030 is mentioned but no results are shown; executive summary cites perturbation calculations that are absent.
- Mission Duration & EOL: Drag-sail sentence is truncated ('to ‘ and is suitable...'), leaving the EOL description incomplete and the drag sail unsized.
- Ground Control & Communications: Access table lists two entries numbered 13 and 14 rows in total despite text claiming fifteen periods; pass frequency per day is not stated explicitly.
- Ground Control & Communications: Mount Pleasant radio telescopes are used as an Earth-observation downlink without frequency, link budget, data rate or antenna suitability justification.
- Orbit – Image 3: Inclination-altitude plot has no source citation and appears to be borrowed material.
- Mission Design – Launch: Wikipedia is used as a source ('Timeline of spaceflight'), which the task explicitly prohibits.
- Bibliography: In-text citations run to [74] but only [1]–[10] are listed; [10] is used for both the Falcon 9 manifest and the drag-sail reference; entries [5] and [10] are garbled.

## Next steps

1. Revisit the launch-site justification in Mission Design – Launch. For a retrograde ~98° orbit the Earth-rotation benefit of an equatorial site is much smaller, so explain why Vega E is still preferable, including the plane-change cost from 5°N.
2. Correct and complete the Orbit section: state the local time of descending node, orbital period, swath width and ground sample distance, and explain your RAAN and epoch. Make the manoeuvre statements consistent with a satellite that has no thrusters.
3. Finish Mission Duration & EOL with a decay or lifetime estimate supporting the five-year life, show the STK results, and complete the drag-sail description with its size. Replace the Wikipedia source with authoritative references and check every in-text citation against the bibliography.

---
<sub>Run Input_2-Run_1-Eff_high-261115-165759 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21901/20266 | cost $0.012377 (incl. $0.001387 for the reused reference rubric+task structure) | 90.24s</sub>
