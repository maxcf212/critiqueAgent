# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

You have developed a well-rationalised Earth-observation mission concept targeting coral bleaching on the Great Barrier Reef, supported by solid STK ground-pass access modelling. To elevate your work to a professional engineering standard, address the orbital mechanics misconception regarding equatorial launches for retrograde orbits, include target coverage and revisit-time simulations, and upgrade your presentation by replacing Wikipedia citations and bare URLs with standard referencing and formal table and figure formatting.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

You effectively rationalised the mission's focus on Great Barrier Reef coral bleaching and justified using a single spacecraft operated by agencies like CSIRO and BOM. Your thorough referencing and clear operational context successfully met the Accomplished level. To build further, continue linking specific user requirements directly to payload performance criteria.

*Assessor reasoning:* The introduction establishes a strong, well-rationalised mission concept addressing coral bleaching on the Great Barrier Reef. It clearly justifies using a single satellite rather than a constellation and identifies specific operators and users (CSIRO, BOM, Australian Government). Descriptions are detailed and supported by relevant references.
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Your STK ground-access modelling for Mt Pleasant is well executed. To achieve Accomplished, correct the technical misconception regarding equatorial launches—retrograde SSOs require extra delta-V to negate Earth's rotation. Additionally, model target coverage and revisit intervals over the Great Barrier Reef, fully cite external figures like Image 3, and complete truncated sentences in your end-of-life drag sail analysis.

*Assessor reasoning:* Core mission elements are addressed with STK analysis for orbit and ground-station passes. However, technical flaws exist: claiming an equatorial launch assists retrograde SSO insertion is incorrect. Target coverage analysis for the Great Barrier Reef is missing, Image 3 is an uncredited web plot, and the EOL discussion contains an incomplete sentence.
> Mission Design: "The most efficient rocket launches are from locations close to the equator as this is where maximum rotational velocity can be experienced"  

### C3 Conclusion (6/10, Adequate)

In your Conclusion, you clearly summarised key design selections such as the Vega E launcher, SSO parameters, and ground station. To progress to Accomplished, move beyond a qualitative summary by synthesising quantitative mission findings, specifically evaluating data throughput, revisit frequency, and projected deorbit timelines against your initial mission requirements.

*Assessor reasoning:* The conclusion accurately recaps the primary design choices (Vega E launch, SSO orbit, Mt Pleasant ground station). However, it remains largely descriptive and qualitative, lacking quantitative synthesis of key performance metrics such as contact throughput, coverage revisit, or deorbit timelines.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Your report follows a logical structure with a helpful executive summary. To reach Accomplished, adhere to professional publishing standards: add formal numbering and captions to figures and tables, remove residual Wikipedia footnote markers, resolve text cut-offs, and replace bare URLs or Wikipedia entries with formal citations to reputable technical sources.

*Assessor reasoning:* The report follows a readable structure with an executive summary. However, presentation falls short of professional standards: figures and tables lack standard numbering and formal captions, tables are copy-pasted from Wikipedia with residual footnote markers, an incomplete sentence appears in EOL, and references consist solely of bare URLs, including prohibited Wikipedia sources.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Mission Design |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Design |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Mission Design |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Mission Design |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Mission Design: Equatorial launch from Kourou does not benefit a retrograde Sun-Synchronous Orbit (i = 97.79°); Earth's eastward rotational velocity must be cancelled out, demanding extra delta-V rather than saving fuel.
- Mission Design: No coverage, swath, or revisit-time analysis was conducted over the actual target area (Great Barrier Reef) to validate whether the 600 km orbit meets imaging requirements.
- Mission Design: The sentence explaining drag sail operation at end-of-life is truncated mid-clause: 'utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes'.

## Next steps

1. Perform a dedicated STK target coverage, swath, and revisit-time analysis over the Great Barrier Reef to validate your 600 km orbit selection.
2. Re-evaluate launch mechanics for retrograde orbits, accounting for the delta-V penalty of cancelling Earth's eastward rotational velocity when launching into an SSO.
3. Upgrade your report presentation to a standard academic style, replacing all bare URLs and Wikipedia citations with peer-reviewed literature, and apply formal captions to all figures and tables.

---
<sub>Run Input_2-Run_2-Eff_high-261115-170655 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18205/10515 | cost $0.044471 (incl. $0.001387 for the reused reference rubric+task structure) | 63.4s</sub>
