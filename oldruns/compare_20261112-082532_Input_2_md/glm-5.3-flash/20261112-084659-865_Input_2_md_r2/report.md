# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 73 / 100 (73%)**

You produced a well-structured, technically sound preliminary mission design for ZYZZsat, addressing all space-segment requirements with genuine STK evidence and hand calculations. Your introduction, launch/orbit/ground-control rationale and conclusions are strong. To reach the top rubric levels, attach your STK software files, add numbered figure/table captions, replace Wikipedia and bare-URL references with proper citations, and fix the technical and editorial slips noted below.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Accomplished (8/10). Your introduction clearly covers the primary mission (fluid-lensing reef imaging), the rationale with cited bleaching statistics, the single-spacecraft justification, and users such as CSIRO and BOM. Referencing is appropriate. To reach 9-10, deepen the discussion distinguishing the operator from customers/users and their respective needs and responsibilities.

*Assessor reasoning:* All four requirements addressed: primary mission (fluid-lensing reef imaging), rationale (bleaching threat with cited statistics), single-spacecraft justification, and users/funders. Well referenced. Slightly limited depth on user/customer distinction prevents a top mark.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Accomplished (8/10). All major requirements are covered: Vega E from Guiana with rationale, a full COE table for your SSO, no manoeuvres until EOL, ground-station selection logic, STK access analysis quantifying contact frequency, and a 5-year duration with drag-sail EOL. Minor technical slips (J2 explanation, 'undesirable' typo) and the missing STK software files keep you from 9-10.

*Assessor reasoning:* All major requirements covered: launch site/vehicle with rationale, SSO with full COE table, manoeuvres (none until EOL), ground station selection logic, STK access report quantifying contact frequency/duration, 5-year duration and drag-sail EOL. STK screenshots and inclination-vs-altitude hand calculation included. Minor technical slips and no software files attached keep it from 9-10.
> Mission Design - Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Mission Design - Orbit: "an altitude of 600km requires a mean inclination of $ 97.7924^{\circ} $"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’"  

### C3 Conclusion (7/10, Accomplished)

Accomplished (7/10). Your conclusions are specific and traceable to evidence, including honest caveats about Vega E availability and alternatives. To strengthen, expand slightly to summarise the EOL plan and communications findings, so the conclusion fully reflects all evidence in the report.

*Assessor reasoning:* Conclusions are specific and trace back to evidence, including honest caveats (Vega E availability, alternatives). Somewhat brief and omits EOL/communications summary detail, so at the lower end of Accomplished.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Adequate (5/10). Your structure is clear with headings and an executive summary, but figures and tables lack numbered captions, the bibliography uses bare URLs and cites Wikipedia (explicitly disallowed), and typos/incomplete sentences persist (e.g. 'a Earth observation', the broken drag-sail sentence). Consistent formatting and polished referencing are required for the Accomplished level.

*Assessor reasoning:* Clear structure with headings and executive summary, but figures/tables lack numbered captions (e.g. 'Figure 1'), bibliography is bare URLs without titles/authors, Wikipedia is cited (explicitly disallowed), and several typos/incomplete sentences ('a Earth observation', 'current owned', broken drag-sail sentence) persist.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  
> Mission Duration & EOL: "utilising a large surface area to ‘ and is suitable for low-earth orbit altitudes"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design (Launch, Orbit, Ground Control, EOL) |
| R3 | State the spacecraft's primary mission. | yes | Introduction / Executive Summary |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Mission Design - Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Mission Design - Orbit (COE table) |
| R8 | Identify any orbital manoeuvres required. | yes | Mission Design - Orbit / EOL |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications (STK access report) |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Orbit (STK + J2 inclination plot) |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Screenshots included; no evidence of attached STK software files |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Report structure (Exec Summary, Introduction, Mission Design, Conclusion, Bibliography) |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Figures/tables have captions but no figure/table numbers |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography: Wikipedia cited as [6]; references are bare URLs |

## Technical issues

- Mission Design - Orbit: "A very high altitude would yield low resolution images which is also desirable" – should read 'undesirable'; contradicts design logic.
- Mission Design - Orbit: "significant J2 perturbations as a result of its highly polar inclination" is imprecise: RAAN precession ∝ cos(i) is zero at i=90°; SSO relies on retrograde inclination (~98°), not polar proximity per se.
- Mission Duration & EOL: Graveyard-orbit discussion is largely irrelevant for a LEO satellite; EOL paragraph is redundant/contradictory ("without thrusters... uncontrolled descent... However, the ZYZZsat is without thrust capability").
- Mission Duration & EOL: Drag-sail sentence is incomplete: "utilising a large surface area to ‘ and is suitable".
- Bibliography: Wikipedia used as a source, explicitly disallowed; references lack titles, authors and access dates.
- Ground Control & Communications: Access table numbering is inconsistent (first row unnumbered, duplicate access 14/15) – possibly an OCR artefact but should be checked.

## Next steps

1. Attach your STK scenario files (or export packages) in an appendix so your access and orbit results can be verified, and number all figures and tables (e.g. Figure 1, Table 1) with captions referenced in the text.
2. Replace the Wikipedia citation and bare URLs with full references (authors, titles, year, access dates) in a consistent style, and ensure every in-text citation matches the reference list.
3. Proofread carefully: correct 'undesirable' in the orbit altitude discussion, complete the broken drag-sail sentence, rewrite the contradictory EOL/graveyard-orbit paragraph for your LEO satellite, and fix the J2/RAAN explanation (precession ∝ cos i, zero at i = 90°; SSO uses ~98° retrograde inclination).

---
<sub>Run 20261112-084659-865_Input_2_md_r2 | rubric=z-ai/glm-5.3-flash, task=z-ai/glm-5.3-flash, marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 13723/2998 | cost $0.001436 | 57.42s</sub>
