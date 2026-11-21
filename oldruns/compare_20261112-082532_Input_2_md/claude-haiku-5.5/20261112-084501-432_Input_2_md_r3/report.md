# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 50 / 100 (50%)**

You have built a clear, mostly complete space-segment design for monitoring the Great Barrier Reef, with a well-motivated purpose and a sound single-satellite rationale. The main gaps are the quantitative justification of your orbit and launch choices, an inconsistent access table, an incomplete end-of-life analysis, and reference and figure presentation. Addressing these would raise several criteria by a level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 7 / 10 | 7 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (7/10, Accomplished)

Your introduction clearly states the mission purpose (monitoring coral reefs, particularly the Great Barrier Reef), explains why it is needed, justifies using one satellite, and names likely users such as CSIRO and BOM. To reach Accomplished, clearly identify the operator, describe the customer groups in more specific detail, support the need with more referenced evidence, and remove speculative funding comments.

*Assessor reasoning:* Mission purpose, need, single-spacecraft choice with reasons, and user groups are all addressed with supporting context and some sourced statistics. The operator is not clearly identified, and the customer description is general. Funding discussion is speculative. Overall a solid, referenced introduction with minor gaps.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education."  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

You cover all required segments, including launch, the orbit table, STK access data, ground tracks and an end-of-life option. To reach Accomplished, support your key choices quantitatively. The 600 km altitude argument is contradictory (higher altitude lowers resolution yet is called desirable), so add swath or ground sample distance calculations. Correct the RAAN explanation, justify the ~42°S ground station, caveat the unflown Vega E, fix the sunlight claim for the descending pass, and quantify end-of-life.

*Assessor reasoning:* All major segments are covered, with an orbit table, STK access data, ground track images and an EOL option. However, the altitude logic is contradictory, the Vega E is unflown yet is used without caveat, and the RAAN explanation is unjustified. The ground station is at about 42°S, not near the pole. There is little quantitative support for swath, resolution or EOL, and STK files are not evidenced.
> Mission Design / Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "The initial value indicates the location of the launch facility."  
> Orbit: "A very high altitude would yield low resolution images which is also desirable."  
> Ground Control & Communications: "a ground station is selected whose latitude will be frequented by the satellite."  
> Mission Duration & EOL: "utilising a large surface area to"  

### C3 Conclusion (5/10, Adequate)

Your conclusion summarises the satellite configuration and usefully acknowledges launch-vehicle risk. To reach Accomplished, draw specific conclusions from your evidence: restate key results such as the 97.79° inclination and access statistics, and show how they support mission feasibility. Replace generic claims, such as coral bleaching being minimised or solved, with conclusions your analysis actually supports, and note the limits of your design.

*Assessor reasoning:* The conclusion summarises the configuration and notes launch-vehicle risk, which is useful. However, it does not restate key quantitative results such as the 97.79° inclination or the access statistics. Several claims are generic or overstated, such as bleaching being minimised or solved.
> Conclusion: "hopefully contribute to the prevention of coral bleaching within the Great Barrier Reef and elsewhere."  

### C4 Report presentation (8/20, Adequate)

Your report has a recognisable structure, with headings and a contents list. To reach Accomplished, number and title every figure and table consistently, fix the truncated sentence and inconsistent heading levels, and correct the bibliography: replace the Wikipedia source [6], add the missing sources cited as [49]-[74], resolve the reused [10], and check that every in-text citation matches a reference. Proofread for spelling, grammar and formatting consistency.

*Assessor reasoning:* Sections follow a recognisable structure with headings and a contents list. Figures and tables are unnumbered and untitled, heading levels are inconsistent, and one sentence is broken. Launch-table superscripts cite [49]-[74], which are absent from the 10-item bibliography. [6] is Wikipedia, and [10] is used for two different sources.
> Launch: "3 February"  
> Bibliography: "[5] f. https://www.qrg.northwestern.edu"  
> Bibliography: "To compare existing spaceflight mission plans, a wiki sorted directory"  
> Image 1  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Introduction |
| R3 | State the spacecraft's primary mission. | yes | Executive Summary |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | partial | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | partial | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | partial | Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | partial | Contents |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | no | Image 1 |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Orbit: Altitude justification is inconsistent: a higher altitude gives lower resolution, yet this is called desirable. No swath or ground sample distance calculation supports the 600 km choice.
- Orbit: The claim that the initial RAAN indicates the launch facility location is unsupported and does not match standard orbit-element meaning.
- Ground Control & Communications: Mt Pleasant (about 42°S) is described as selected for a latitude close to the poles, which is a weak and partly incorrect rationale.
- Ground Control & Communications: The access table duplicates access 14 as access 15, and the statistics say 15 accesses while the list is labelled with a '----' row, so the count is inconsistent.
- Launch: Vega E is used as the launch vehicle though not yet flown; its 2024 first-launch claim is unsourced and conflicts with the VV18 rideshare plan.
- Mission Duration & EOL: A sentence is truncated, and the drag-sail description is incomplete. The EOL strategy has no decay time or delta-V analysis despite stated STK runs to 2030.
- Mission Design / Orbit: The descending pass is described as constantly in sunlight, which overstates the sunlit conditions for a sun-synchronous orbit.
- Bibliography: Wikipedia is cited as [6], which the brief prohibits. Launch-table citations [49]-[74] are not in the bibliography, and [10] is reused for two different sources.

## Next steps

1. Strengthen your orbit and launch justification with quantitative evidence: add a swath or ground sample distance calculation for 600 km, correct the RAAN explanation, and caveat or justify the unflown Vega E.
2. Complete your access and end-of-life analysis: correct the duplicated access entry and its statistics, and quantify your end-of-life option with a decay time or delta-V estimate.
3. Repair referencing and presentation: replace the Wikipedia source, reconcile citations [49]-[74] and the reused [10] with the bibliography, and number and title all figures and tables consistently.

---
<sub>Run 20261112-084501-432_Input_2_md_r3 | rubric=anthropic/claude-haiku-5.5, task=anthropic/claude-haiku-5.5, marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 19849/12803 | cost $0.008386 | 65.4s</sub>
