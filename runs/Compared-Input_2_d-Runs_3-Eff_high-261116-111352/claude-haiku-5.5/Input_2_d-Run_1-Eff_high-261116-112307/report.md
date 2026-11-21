# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 43 / 100 (43%)**

You have a clear primary mission for monitoring the Great Barrier Reef, and a sound single-satellite argument supported by STK access results and ground tracks. The main concerns are technical: the 87.79° inclination does not match a 600 km sun-synchronous orbit, the Kourou latitude and RAAN rationale are incorrect, and access statistics do not match your table. Correcting these, along with the EOL and referencing gaps, would strengthen the report considerably.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 4 / 10 | 24 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your primary mission, the reason it is needed and the single-spacecraft choice are clearly argued, with some sources. To reach the next level, explicitly name the operator and the customers, such as the reef scientists and conservation managers who will use the data, rather than leaving them implied. Also replace URL-only citations with full referencing.

*Assessor reasoning:* Primary mission, rationale and single-spacecraft choice are clearly argued with some sources. Users are only implied: the operator and customers are not explicitly identified in the introduction, and the referencing is URL-only. Detail is good, but the users requirement is weakly covered.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "would allow marine and conservation scientists to more accurately predict"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (24/60, Adequate)

Your STK access data and ground tracks provide good evidence. However, 87.79° is not the inclination for a 600 km sun-synchronous orbit (about 97.8° retrograde), which contradicts your retrograde claim and Figure 3. Kourou is about 5.2° N, not 45.05° N, and RAAN does not indicate a launch site. Promised perturbation calculations are absent and the launch vehicle choice is inconsistent. Resolving these to a high standard would reach Accomplished.

*Assessor reasoning:* Most required items are addressed and STK access data and ground tracks are shown. However, the inclination of 87.79 deg is wrong for a 600 km sun-synchronous orbit (about 97.8 deg, as the student's own plot shows), contradicting the retrograde claim. Kourou's latitude is wrong, the RAAN rationale is incorrect, and promised perturbation calculations are absent. Launch vehicle choice is inconsistent.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of"  
> Orbit: "The orbit is near-polar and retrograde, meaning the satellite will pass over almost the entire Earth"  
> Launch: "it is situated very close to the equator, with a latitude of"  
> Orbit: "The initial value indicates the location of the launch facility."  
> Executive Summary: "including Systems Tool Kit (STK) simulations, perturbation calculations, launch mission alternatives evaluation"  

### C3 Conclusion (5/10, Adequate)

You identify the Vega E launch-schedule risk and summarise the segments. However, the conclusion largely restates the design rather than drawing specific conclusions from your evidence, and it does not reflect the orbit and access errors. To reach Accomplished, state what your STK results show, such as contact frequency and eclipse seasons, and what they mean for the mission's viability.

*Assessor reasoning:* The conclusion summarises the segments and identifies the Vega E launch risk. It largely restates the design rather than drawing specific conclusions from the evidence, and it does not reflect the errors in orbit and access results.
> Conclusion: "Thus, launch may need to be adjusted if the rocket is still not constructed by the proposed date."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans"  

### C4 Report presentation (8/20, Adequate)

Your report has clear headings, a contents list and a numbered executive summary, giving it a logical structure. Several sentences are garbled, and tables and figures are largely unnumbered or uncaptioned, making context hard to follow. Bibliography entries for [49]-[74] are missing, Wikipedia is cited despite the brief, and some references are incomplete. Proofread for typos and apply consistent figure and table labelling.

*Assessor reasoning:* Headings, a contents list and a numbered executive summary give structure. Sentences are garbled, and tables and figures are largely unnumbered or uncaptioned. Citations [49]-[74] are not in the bibliography, Wikipedia is cited despite the brief, and some references are truncated. Several typos appear.
> End-of-life section: "It acts like a regular sail, utilising a large surface area to"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Bibliography: "[10 d."  
> Access table: "Feb 2025 11:23:57.461"  

## Technical issues

- Orbit: Inclination of 87.79 deg is incorrect for a 600 km sun-synchronous orbit (about 97.8 deg retrograde). This contradicts the retrograde claim and the student's own Figure 3.
- Launch: Kourou latitude is stated as 45.05 deg N; it is about 5.2 deg N, and the equatorial-launch argument depends on it.
- Orbit: RAAN of 27.33 deg is said to indicate the launch facility location. RAAN is set by launch time and is not a site indicator; the value is unjustified.
- Ground Control: Text states that polar latitudes maximise pass frequency, then selects Tasmania (about 43 deg S) without quantitative access comparison.
- Ground Control: Text says average contact is almost twenty minutes, but the table mean of 580.786 s is about 9.7 minutes. The text also refers to fifteen accesses while listing fourteen with a duplicated label 13.
- Ground Control: Text says the satellite is constantly in sunlight on the descending track; a 600 km SSO has eclipse seasons.
- Mission Duration & EOL: Five-year lifetime and EOL choice are asserted without decay or drag analysis. The drag sail sentence is truncated and the final EOL strategy is not stated.
- Launch: Piggyback on a rideshare is proposed, but the satellite is then assigned to Vega E, with an unresolved schedule against the 2024 first-launch claim and the 2025 STK epoch.
- Bibliography: Wikipedia is cited as a source despite the brief, and table citations [49]-[74] are missing from the list.

## Next steps

1. Recheck the orbit and launch-site parameters: recompute the inclination for a 600 km sun-synchronous orbit (about 97.8°), correct the Kourou latitude, remove the RAAN site rationale, and add the perturbation calculations you promised to support the design.
2. Reconcile your access statistics with the STK output (mean contact time, pass count, eclipse seasons), justify the ground station choice quantitatively, resolve the rideshare versus Vega E schedule, and state a complete EOL strategy with decay or drag analysis.
3. Complete the bibliography for all in-text citations, replace Wikipedia with authoritative sources, number and caption every figure and table, rewrite garbled sentences, and proofread for typos.

---
<sub>Run Input_2_d-Run_1-Eff_high-261116-112307 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21074/13996 | cost $0.009159 (incl. $0.001387 for the reused reference rubric+task structure) | 63.04s</sub>
