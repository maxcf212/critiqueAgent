# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 67 / 100 (67%)**

Your Part 2 report presents a well-structured, technically sound mission design for reef monitoring, addressing all major space-segment requirements with STK evidence and sensible SSO and ground-station choices. It is held back by missing STK software files, use of Wikipedia as a source, unnumbered figures/tables, and several small technical and writing errors. Fixing these presentation and evidence gaps is your clearest path to higher marks.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Accomplished (8/10). Your introduction clearly states the primary mission (fluid-lensing reef monitoring), justifies why it is needed (bleaching data for the GBR), explains the single-spacecraft choice, and identifies users such as CSIRO and BOM with literature citations. To reach the very top of the band, sharpen the distinction between operator and customers and detail their specific roles and data products.

*Assessor reasoning:* Primary mission (fluid-lensing reef monitoring), rationale (bleaching data), single-spacecraft justification, and users/funding all addressed with literature citations. Discussion is detailed though user/customer roles could be more specific.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

Accomplished (7/10). All major requirements are addressed: Vega E from Guiana with rationale, a full COE table for your 600 km SSO, no manoeuvres until EOL, ground-station access (~10 min average) with STK evidence, and a 5-year duration with drag-sail EOL. To advance, include the STK software files, tighten the swath/resolution analysis, correct the claim that low resolution is 'desirable', and clarify the RAAN discussion.

*Assessor reasoning:* All major requirements addressed: launch site/vehicle with rationale, SSO with full COE table, manoeuvres (none until EOL), ground station, STK access report, 5-year duration and drag-sail EOL. Good STK evidence and hand calculation. Weaknesses: no software files shown, swath/resolution analysis hand-wavy, Wikipedia source, and an error claiming low resolution is 'desirable'.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’"  

### C3 Conclusion (7/10, Accomplished)

Accomplished (7/10). Your conclusions are drawn from the report's evidence and acknowledge real risk, such as the Vega E not yet being built, with fallback options. They are specific rather than generic. To strengthen them, quantify key outcomes (e.g. revisit time, contact statistics, data volume) so each conclusion traces directly to a number in the body.

*Assessor reasoning:* Conclusions are drawn from the evidence for each segment and acknowledge risk (Vega E availability) with fallback options. Somewhat brief and could quantify outcomes, but specific rather than generic.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Adequate (5/10). Your structure is clear with a concise executive summary, but figures and tables lack numbers (e.g. 'STK 3D view of orbit: 12 hours apart'), references are bare URLs including Wikipedia, and there are grammar slips ('a Earth observation', 'complied daily'). The Accomplished level requires consistent numbering, proper citations matching the reference list, and polished, professional writing throughout.

*Assessor reasoning:* Clear structure with headings and a concise executive summary, but figures/tables lack numbering (captions only), references are bare URLs including Wikipedia, and there are several typos/grammar slips ('a Earth observation', 'for the purposed of', 'complied daily'). Not professional-level presentation.
> Orbit: "STK 3D view of orbit: 12 hours apart"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Executive Summary: "the construction of a Earth observation satellite"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design (Launch, Orbit, Ground Control, EOL) |
| R3 | State the spacecraft's primary mission. | yes | Introduction / Executive Summary |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit (COE table) |
| R8 | Identify any orbital manoeuvres required. | yes | Orbit / EOL |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Orbit, Ground Control (STK + inclination plot) |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Screenshots included (Images 1-5, access report); no software files evidenced in body or appendix |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Report structure (Executive Summary through Bibliography) |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Captions present but no figure/table numbers (e.g. 'STK 3D view of orbit: 12 hours apart') |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography cites sources in text, but Wikipedia [6] is used, which is not accepted |

## Technical issues

- Orbit: States 'A very high altitude would yield low resolution images which is also desirable' – should be undesirable; contradicts design logic.
- Bibliography: Wikipedia cited as reference [6], explicitly not accepted as a proper source.
- Orbit: RAAN initial value claimed to 'indicate the location of the launch facility' – RAAN is set by launch timing/geometry, not directly by site latitude.
- Mission Duration & EOL: Redundant/contradictory passage: satellite 'without thrusters' stated twice; uncontrolled descent vs passive drag sail discussion is muddled.
- Ground Control & Communications: Access rows 13 and 14 are identical duplicates in the STK table; no explanation.
- Deliverables: No STK software files included or referenced in an appendix.

## Next steps

1. Attach your STK scenario files (or a clearly referenced appendix listing them) so the software evidence behind your orbit and access analysis can be verified.
2. Replace Wikipedia [6] with a primary or peer-reviewed source, and convert bare-URL bibliography entries into a consistent referencing style (e.g. IEEE).
3. Number all figures and tables (Figure 1, Table 1, etc.), cite them in the text, and proofread for typos such as 'a Earth observation' and 'for the purposed of'.

---
<sub>Run 20261112-084606-844_Input_2_md_r1 | rubric=z-ai/glm-5.3-flash, task=z-ai/glm-5.3-flash, marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 13600/2721 | cost $0.002176 | 53.02s</sub>
