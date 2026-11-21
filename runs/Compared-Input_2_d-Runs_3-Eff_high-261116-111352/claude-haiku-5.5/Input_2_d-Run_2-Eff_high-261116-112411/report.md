# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 43 / 100 (43%)**

You have built a solid STK-based design for a single sun-synchronous satellite, with well-referenced rationale and useful access data. Core orbital calculations need correcting, including the inclination, semi-major axis and launch-site latitude. The end-of-life plan needs completing, and tidying the reference list will also strengthen your presentation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your primary mission, rationale for using one spacecraft and literature support are clearly argued, which earns an Adequate mark. To reach Accomplished, explicitly identify your operator and customers, which are currently only implied as marine and conservation scientists. Also resolve the conflict between the 'direct launch' wording in the executive summary and your piggyback launch plan.

*Assessor reasoning:* Primary mission, rationale and single-spacecraft choice are well argued with references. Users are only implied (marine and conservation scientists); operator and customers are not explicitly identified. The executive summary's 'direct launch' conflicts with the later piggyback approach. Overall detailed but not fully complete.
> Executive Summary: "a direct launch into a retrograde sun-synchronous polar orbit"  
> Introduction: "Thus, only one satellite is required."  
> Executive Summary: "is operated and accessed from Australia ground facilities"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

Your STK screenshots, access tables and orbit analysis give real evidence of design work. Errors undermine it: the 87.79° inclination is prograde, so it cannot be the retrograde sun-synchronous orbit you describe, and 6371 km plus 600 km is 6971 km, not 7171 km. Kourou's latitude is also misstated. To reach Accomplished, correct these, reconcile the contact duration with your table, and complete a decay and delta-V assessment for end of life.

*Assessor reasoning:* Substantial STK evidence and access tables support the design. However, the 87.79° inclination is prograde, contradicting the claimed retrograde sun-synchronous orbit and the plotted ~97.8°. The semi-major axis is arithmetically wrong (6371+600 is 6971 km). Kourou latitude is misstated, the contact-duration claim conflicts with the table, and the EOL analysis is incomplete with no decay or delta-V assessment.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of"  
> Orbit (COE table): "Earth radius of 6371km plus a proposed altitude of 600km as previously explained."  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "utilising a large surface area to"  

### C3 Conclusion (5/10, Adequate)

You reach conclusions on the main segments and sensibly flag the Vega E launch risk with a fallback. However, the conclusion mostly restates the report rather than drawing evidence-based conclusions on performance and end of life. Avoid overstating outcomes, such as claiming the mission prevents bleaching. To reach Accomplished, tie each conclusion to specific results from your analysis.

*Assessor reasoning:* The conclusion summarises the main segments and identifies the Vega E launch risk with a fallback. It is largely a restatement and does not draw evidence-based conclusions on performance or EOL. It also overstates the mission outcome as preventing bleaching.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

Clear headings and a contents page give the report a sensible structure. Marks are held back by a broken reference entry, a duplicated [10] citation, citations up to [74] without list entries, Wikipedia use, a duplicated access number, a truncated sentence in the drag-sail discussion, and some tables lacking clear labels. Fix these and check that every in-text citation matches the reference list.

*Assessor reasoning:* Clear headings and a contents page give reasonable structure. Presentation is undermined by a truncated sentence, a duplicated access number, a broken reference entry, and a duplicated [10] citation. Citations up to [74] have no list entries, and Wikipedia is cited. Typos and some unlabelled or uncaptioned tables reduce clarity.
> Mission Duration & EOL: "utilising a large surface area to"  
> Bibliography: "[10 d."  
> Launch: "The Block 5 variation is currently the only active Falcon 9 variant"  

## Technical issues

- Orbit: Inclination of 87.79° is prograde and cannot be sun-synchronous; it also contradicts the plotted ~97.8° at 600 km and the claimed retrograde orbit.
- Orbit (COE table): Semi-major axis 7171 km is wrong; 6371 km + 600 km = 6971 km.
- Orbit (COE table): RAAN 'initial value indicates the location of the launch facility' is incorrect; RAAN is set by the epoch and sun-synchronous condition, not the launch site.
- Orbit: Claims the true anomaly is undefined for a circular orbit. It is defined from the ascending node, with argument of latitude as the usual replacement for ω+ν.
- Launch: States Kourou is at 45.05°N and 'very close to the equator'. Kourou is ~5.2°N; the latitude is wrong and the justification is inconsistent.
- Launch: Proposes Vega E as the launch vehicle while acknowledging it is unbuilt, and the executive summary says 'direct launch' despite a piggyback plan.
- Ground Control & Communications: Mean contact duration of 580.8 s is ~9.7 min, not 'almost twenty minutes'. The access table also repeats access number 13 and lists only 14 unique passes.
- Ground Control & Communications: Claims a near-polar ground station maximises passes, but Mt Pleasant (~43°S) is not polar; pass frequency and number of stations are not quantified.
- Mission Duration & EOL: Uncontrolled re-entry from 600 km is not checked against decay time or the 25-year guideline. The 'graveyard' manoeuvre requires propulsion, which contradicts the 'without thrusters' statement.
- Mission Duration & EOL: Drag-sail sentence is truncated and unfinished.
- Bibliography: Wikipedia is cited despite being explicitly unacceptable. Reference [10] is used for two unrelated claims, the entry is malformed, and citations [11]–[74] have no bibliography entries.

## Next steps

1. Recheck your orbital elements. A 600 km circular orbit has a semi-major axis of 6971 km, and a sun-synchronous orbit at this altitude is retrograde (about 97.8°). Make the COE table, text and plots consistent with each other.
2. Correct the Kourou latitude (about 5.2°N), the RAAN explanation (set by epoch and the sun-synchronous condition, not the launch site) and the mean contact duration (about 9.7 min). Quantify ground-station pass frequency and justify the number of stations.
3. Complete the end-of-life analysis: check decay time against the 25-year guideline, state whether the graveyard manoeuvre needs propulsion, and finish the drag-sail discussion. Replace Wikipedia with an acceptable source, fix the duplicated [10] entry and add bibliography entries for citations [11]–[74].

---
<sub>Run Input_2_d-Run_2-Eff_high-261116-112411 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21189/12352 | cost $0.008349 (incl. $0.001387 for the reused reference rubric+task structure) | 53.32s</sub>
