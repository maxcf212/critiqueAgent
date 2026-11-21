# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You have a clear, well-supported introduction and a good evidence base from your STK access analysis, and you openly flag the Vega E launch risk. The main barriers to a higher level are internal consistency: the launch plan, RAAN explanation, manoeuvre statements and ground-station rationale contradict each other or the evidence. Presentation errors, a truncated EOL paragraph and citation problems also need attention.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your introduction is a clear strength. It states the primary mission, explains why monitoring the Great Barrier Reef matters, justifies the single-spacecraft choice and identifies likely users such as CSIRO and BOM, supported by literature. To move further up the band, name the operator explicitly and strengthen your sources, favouring peer-reviewed or agency literature over general web pages.

*Assessor reasoning:* Primary mission, rationale, single-spacecraft choice with justification and likely customers are all addressed in detail with supporting literature. The operator is never clearly named, and the cited sources are mostly web pages rather than strong literature, so this sits at the lower end of Accomplished.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Other Earth observation satellites use networks or constellations of satellites"  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your STK access statistics, whose totals check out, and several screenshots give the design a good evidence base. The design is held back by inconsistencies: the piggyback and direct launch accounts conflict, the RAAN is wrongly linked to the launch site, and Tasmania contradicts your pole-proximity argument. To reach Accomplished, reconcile these, quantify altitude with swath width and GSD, align manoeuvre statements with a passive EOL, and include the STK files.

*Assessor reasoning:* Most required elements are present, with STK access statistics that check out arithmetically and several screenshots. However the launch plan is inconsistent (piggyback versus direct launch, unbuilt Vega E, a 2021 manifest used for a 2025 launch). The RAAN explanation is wrong, the ground-station rationale contradicts Tasmania's latitude, and altitude choice lacks quantitative swath or GSD calculations. No STK files are provided.
> Executive Summary: "a direct launch into a retrograde sun-synchronous polar orbit"  
> Launch: "it should instead partake in the common practice of 'piggybacking'"  
> Orbit: "The initial value indicates the location of the launch facility."  
> Orbit: "the only orbital manoeuvre occurs at the EOL segment of the satellite's mission"  
> Ground Control & Communications: "selecting a ground facility close to the poles"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (5/10, Adequate)

Your conclusion sensibly flags the Vega E launch risk and offers a fallback, which is a useful reflective point. However, it mostly restates the design rather than drawing specific conclusions from your evidence, such as the access statistics, the EOL trade-off or the launch uncertainty. It also overstates the mission's effect on bleaching prevention. Tie conclusions to specific results and temper claims to what the analysis supports.

*Assessor reasoning:* The conclusion restates the design and flags the Vega E risk with a fallback, which is reasonable. It is largely a summary, however, and does not draw specific conclusions from the access statistics, EOL trade-off or sensitivity to the launch uncertainty. It also overstates the mission's effect on bleaching prevention.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (8/20, Adequate)

Your report has a clear heading and contents structure, which helps navigation. Presentation is held back by spelling and grammar errors, a truncated sentence in the EOL section, and tables and figures without consistent numbering and captions. Citations also need work: references [49]-[74] are not in the bibliography and Wikipedia is cited. Proofread thoroughly and check every in-text citation against the reference list.

*Assessor reasoning:* Headings and a contents list give a clear structure, but there are many spelling and grammar errors and at least one truncated sentence in EOL. Tables and figures are not numbered or captioned properly. In-text citations [49]–[74] have no matching bibliography entries, a Wikipedia source is used, and reference entries are malformed. Presentation falls short of Accomplished.
> Mission Duration & EOL: "It would therefore make sense to choose an uncontrolled descent as an end-of-life strategy"  
> Bibliography: "[5] f. https://www.qrg.northwestern.edu"  
> Bibliography: "[10 d."  
> Launch: "according to the in-text citation [50][51] in the launch table" *(quote not found in submission)*  
> Ground Control & Communications: "Mount Pleasant Radio Observatory)"  

## Technical issues

- Executive Summary vs Launch: Executive summary claims a direct launch, but the body describes a piggyback rideshare on an unselected mission.
- Launch: The two-launch-windows-per-day argument based on Kourou latitude versus inclination is muddled and not quantified.
- Launch: Relies on a February 2021 spaceflight manifest and an unbuilt Vega E for a 2025 launch, with no verified schedule.
- Orbit: RAAN of 27.33° is described as indicating the launch facility location, which is incorrect; no epoch or LTAN (local time of ascending node) is given.
- Orbit: Altitude reasoning is inconsistent: a very high altitude is called desirable for low resolution, and no swath width or GSD calculation supports the 600 km choice.
- Orbit: States the only manoeuvre is at EOL, yet the EOL strategy is passive, so manoeuvre requirements are contradictory.
- Ground Control & Communications: Claims that proximity to the poles maximises pass frequency, then selects Tasmania (about 42°S) without reconciling this.
- Ground Control & Communications: Claims the descending pass is 'constantly in sunlight', which overstates illumination and ignores seasonal eclipse or dawn-dusk considerations.
- Ground Control & Communications: Access table lists access number 13 twice; otherwise the duration total and mean (8711.797 s, 580.786 s) are arithmetically correct.
- Mission Duration & EOL: Drag-sail paragraph is truncated mid-sentence, and the EOL recommendation is inconsistent with the earlier uncontrolled-descent reasoning.
- Bibliography: Uses Wikipedia (2021_in_spaceflight), which the brief explicitly forbids, and in-text citations [49]–[74] are missing from the list.

## Next steps

1. Make the launch plan consistent across the executive summary, launch section and conclusion. Either justify a direct launch with a specific vehicle and a verified 2025 schedule, or commit to a rideshare and name the host mission and its status.
2. Correct the orbit section: explain that RAAN does not indicate the launch site, give an epoch and LTAN, and quantify the 600 km altitude with swath width and GSD calculations. Make your manoeuvre statements consistent with a passive EOL strategy.
3. Fix presentation and sourcing: complete the truncated drag-sail paragraph, proofread for spelling and grammar, number and caption all figures and tables, replace the Wikipedia source, and make sure every in-text citation [49]-[74] appears in the bibliography. Add the STK files to the appendix.

---
<sub>Run Input_2-Run_2-Eff_high-261115-165929 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21451/15611 | cost $0.010004 (incl. $0.001387 for the reused reference rubric+task structure) | 88.25s</sub>
