# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

You present a coherent, well-organised preliminary design that covers most requirements and is supported by STK evidence. The main gaps are in the mission design: no comms frequency or link budget, no coverage/swath analysis, a questionable RAAN rationale, and an under-supported EOL plan. Presentation and referencing also need work.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale (8/10, Accomplished)

Strong introduction: the coral-reef/ocean-monitoring concept, rationale, single-spacecraft justification and users are all covered with references. To reach the top of this level, replace the Wikipedia launch citation with a primary source and tighten referencing throughout.

*Assessor reasoning:* Primary mission (coral reef/ocean monitoring via fluid lensing), rationale, single-spacecraft justification and users (operator/customers) are all covered with literature references. Some referencing is weak (Wikipedia used for launch data), but overall detailed and persuasive.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design (36/60, Adequate)

Launch, orbit, ground station, duration and EOL are addressed with STK evidence, but the design is inconsistent. Add a comms frequency and link budget, a coverage/swath calculation justifying 600 km, a correct RAAN explanation, and a quantified deorbit analysis that resolves the thrusters contradiction.

*Assessor reasoning:* Launch site/vehicle, orbit elements, ground station, comms frequency, duration and EOL are addressed with STK evidence. But design has inconsistencies: no comms frequency/link budget, no coverage/swath analysis, EOL drag sail contradicts 'no thrusters' and no manoeuvre quantified, and launch rationale relies on Wikipedia. Adequate but not comprehensive.
> Orbit: "Specifically, an altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous." *(quote not found in submission)*  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (6/10, Adequate)

Your conclusion restates the design and flags the unbuilt Vega E risk, but stays generic. Move to the next level by drawing quantified conclusions from your results and critically assessing limitations such as the missing link budget and coverage analysis.

*Assessor reasoning:* Conclusions summarise the design and acknowledge the unbuilt Vega E risk, but are largely generic restatements without quantified outcomes or critical assessment of limitations.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (10/20, Adequate)

Headings and an executive summary give structure, but figures are unnumbered, tables lack titles, references are bare URLs and Wikipedia is cited, with typos ('purposed', 'complied'). Number and caption all figures/tables and use full, consistent references to reach the next level.

*Assessor reasoning:* Structure with headings and executive summary is present, but figures are unnumbered/unlabelled (only captions), tables lack titles, references are bare URLs with no author/title/date, Wikipedia is cited, and there are typos ('purposed', 'complied'). Readable but not professional.
> Orbit: "[Image 1]"  
> Ground Control & Communications: "DN path for orbits 1-15"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Define the spacecraft's primary mission. | yes | Introduction |
| R2 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R3 | Identify the users, including operator and customers. | yes | Introduction |
| R4 | Specify the launch site and launch vehicle. | yes | Launch |
| R5 | Define the orbit type, its characteristics and orbital elements. | yes | Orbit |
| R6 | Identify any required orbital maneuvers. | partial | Orbit |
| R7 | Identify ground control facilities and state how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | State the mission duration and end-of-life (EOL) plans. | yes | Mission Duration & EOL |
| R9 | Ensure the mission benefits Australia in some way and keep the mission concept simple. | yes | Introduction |
| R10 | Complete the design using software of choice (STK, PIGI, or other approved software such as flightclub after contacting Naomi), supplementing with hand calculations as needed. | yes | Orbit |
| R11 | If using PIGI, register for the Saber Astronautics competition to obtain a software license; the design may be entered in the competition. | no | - |
| R12 | Contact Naomi before starting work with software other than STK or PIGI. | no | - |
| R13 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R14 | Cover all main-body space segment topics: launch, orbit, ground stations, coverage, mission operation and end-of-life. | partial | Mission Design |
| R15 | Fully and correctly label figures and tables with number, title and reference if necessary. | no | Orbit |
| R16 | Clearly identify and properly cite/reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Orbit: RAAN 27.33° is stated to indicate launch facility location, which is incorrect; RAAN is set by launch time/azimuth, not site longitude.
- Orbit: No coverage/swath or resolution calculation to justify 600 km altitude; claim that high altitude gives low resolution is stated but not quantified.
- Ground Control & Communications: No communication frequency band, data rate or link budget given, despite requirement to state comms frequency.
- Mission Duration & EOL: EOL drag sail described but no deorbit time/altitude analysis; text says satellite has no thrusters yet earlier mentions retro-burn options inconsistently.
- Launch: Launch vehicle selection relies on Wikipedia '2021 in spaceflight' and an unbuilt Vega E; no delta-V or launch azimuth analysis.
- Ground Control & Communications: Access table shows duplicate access 14/15 and a 151 s minimum pass; no assessment of data volume vs contact time.

## Next steps

1. Add a communications section with frequency band, data rate and a link budget, and check data volume against the 151 s minimum pass.
2. Quantify the orbit choice: compute swath/coverage and resolution for 600 km, and correct the RAAN explanation to launch time/azimuth.
3. Resolve the EOL inconsistency and add a deorbit time/altitude analysis for the drag sail; then fix figure/table numbering and replace Wikipedia with primary references.

---
<sub>Run 20261112-053119-856_Input_2_md_ref | rubric=deepseek/deepseek-v4.1-flash-1017, task=deepseek/deepseek-v4.1-flash-1017, marking=deepseek/deepseek-v4.1-flash-1017, feedback=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 14173/3007 | cost $0.003221 | 65.22s</sub>
