# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 58 / 100 (58%)**

You have a readable preliminary design that covers all mission areas with STK evidence and a clear Australian-benefit rationale. To move from Adequate to Accomplished in the main body, you need quantitative support for launch, orbit, communications and EOL, plus complete software files and referencing. Your Introduction is strong; your Conclusion and presentation need more specific, evidence-linked detail.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (7/10, Accomplished)

Your Introduction clearly explains the reef-monitoring mission, Australian benefit, single-spacecraft rationale and likely users, with references. To secure a higher Accomplished mark, name the operator explicitly and define customer/funding roles more precisely; the rubric requires detailed descriptions and appropriate literature throughout.

*Assessor reasoning:* Mission purpose, Australian benefit, single-spacecraft rationale and likely users are described in detail with references. Operator is only implied (Australian facilities/government), and user/funding roles are somewhat vague, so low Accomplished.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You cover launch, orbit, ground control, communications, duration and EOL with STK screenshots and an access table. The next level requires quantitative evidence: launch performance/azimuth for direct SSO injection, swath/resolution derivation for 600 km, link budget/data volume, drag area/lifetime/casualty risk, and STK files. Correct the contradictory resolution statement and RAAN/J2 claim, and replace the unbuilt Vega E or justify it with performance data.

*Assessor reasoning:* All major design areas are covered with STK screenshots and an access table, but support is incomplete: no STK files, no quantitative swath/resolution, launch performance, link budget or drag-lifetime calculations. Launch selection is speculative and some orbit/EOL claims are inconsistent.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "The most suitable orbit for this task would be a low-earth sun-synchronous orbit."  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’"  

### C3 Conclusion (5/10, Adequate)

Your Conclusion restates the main design choices and links to the body, but it is brief and partly generic. To reach Accomplished, draw specific evidence-based conclusions for each design area, including EOL, and remove the inaccurate claim that Mt Pleasant gives constant contact; the access results show limited passes over three days.

*Assessor reasoning:* Conclusions restate the main design choices and are linked to the body, but they are brief and partly generic. The claim of constant ground-station contact is inaccurate, and EOL conclusions are omitted.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (10/20, Adequate)

Your headings and structure are clear, but presentation is not yet professional. Number and caption every figure/table, including Image 4 and the access summary, add missing references [49]-[55] and [66]-[74], replace bare URLs and Wikipedia with proper citations, and fix typos/contradictions. Accomplished requires consistent formatting, an executive summary and in-text/reference-list matching.

*Assessor reasoning:* Report structure and headings are clear, but presentation is not professional: figures/tables lack numbers and captions, references are URL-only and mismatched, Wikipedia is used, and several typos/contradictory statements remain.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 4: "DN path for orbits 1-15"  
> Ground Control & Communications: "Satellite-ZYZZsat-To-Facility-Mt_Pleasant_Radio_Observatory: Access Summary Report"  

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
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Image 4 |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Bibliography |

## Technical issues

- Launch: Launch choice relies on a 2021 VV18 example and the unbuilt Vega E; no performance/azimuth analysis for direct injection from 5.05°N into a 97.8° retrograde SSO, and Wikipedia is used as the launch database.
- Orbit: The statement that high altitude yields low resolution images “which is also desirable” is contradictory; the 600 km altitude is not derived from required swath, resolution or sensor field of view.
- Orbit: RAAN is stated to indicate launch-facility location; RAAN depends on launch time/azimuth and orbital dynamics, not facility latitude alone. J2 precession rate is stated but not calculated.
- Ground Control & Communications: Mount Pleasant Radio Observatory is a radio-astronomy facility, not an established EO downlink station; no link budget, data rate or data-volume assessment supports the claim that passes are sufficient. Access results cover only three days.
- Mission Duration & EOL: Five-year life is asserted without component/lifetime analysis. Drag-sail EOL is proposed without drag area, deployment reliability, orbital-lifetime, 25-year-rule or casualty-risk calculation; no propulsive manoeuvre is actually designed.
- Bibliography: References in tables [49]-[55] and [66]-[74] are absent from the bibliography; bibliography entries are bare URLs and include Wikipedia.

## Next steps

1. Add quantitative design evidence: launch performance/azimuth for direct SSO injection, swath/resolution derivation for 600 km, link budget/data volume, drag area/lifetime/casualty risk, and include your STK files.
2. Correct and support orbit and ground-station claims: calculate RAAN/J2 effects, replace or justify Mt Pleasant as an EO downlink, extend access analysis beyond three days, and remove the 'constant' contact claim.
3. Fix referencing and presentation: number and caption all figures/tables, add missing references [49]-[55] and [66]-[74], replace bare URLs and Wikipedia with proper citations, and clarify operator/users and EOL conclusions.

---
<sub>Run Input_2-Run_1-Eff_high-261115-165142 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14459/11206 | cost $0.008 (incl. $0.001387 for the reused reference rubric+task structure) | 86.74s</sub>
