# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

A competent, well-structured report covering all mission elements with STK evidence. Your introduction is strong and persuasive. The main body is weakened by a speculative launch choice, unverified orbital geometry, missing hand calculations and incomplete EOL analysis. Referencing and figure formatting need work. Overall adequate.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Your Introduction clearly states the mission purpose, need, single-spacecraft justification and users, with literature support. To reach the top of Accomplished, tighten the operator/customer distinction and ensure every claim is referenced.

*Assessor reasoning:* Mission purpose, rationale, single-spacecraft justification and users are all addressed with literature support. Rationale is persuasive; operator/customer distinction is somewhat loose but adequate for high standard.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

All major elements are covered with STK screenshots and access data, but the Vega E choice is speculative, the RAAN/launch-site geometry is not demonstrated, and J2 and delta-v hand calculations are missing. The EOL drag-sail discussion is truncated and conflicts with the earlier manoeuvre mention. Add quantitative support and resolve the inconsistency.

*Assessor reasoning:* All major elements covered with STK screenshots and access data. However, launch choice is speculative (Vega E not yet built), RAAN/launch-site consistency is questionable, no hand calculations for J2 or delta-v, and EOL drag-sail discussion is incomplete. Evidence present but not fully rigorous.
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (6/10, Adequate)

Your Conclusion summarises the design and acknowledges launch risk, but is largely generic. Reach the next level by stating quantitative outcomes (coverage, contact statistics, deorbit time) and explicit EOL conclusions drawn from your evidence.

*Assessor reasoning:* Conclusion summarises design and acknowledges launch risk, but is largely generic and lacks quantitative outcomes or explicit EOL/coverage conclusions.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Structure and headings are clear, but references are bare URLs (including Wikipedia), citation formatting is inconsistent, figures lack numbered captions, and there are typos. Move to the next level with a consistent citation style, numbered captions and a proofread.

*Assessor reasoning:* Structure and headings are clear, but references are bare URLs, one is Wikipedia, citation formatting is inconsistent, figures lack numbered captions, and there are typos/awkward phrasing. Readable but not professional.
> Bibliography: "[5] f. https://www.qrg.northwestern.edu"  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight"  
> Orbit: "[Image 1]"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Executive Summary |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | partial | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | partial | Orbit |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Orbit |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Contents |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Orbit: RAAN 27.33° claimed to indicate launch facility location, but Kourou at 5°N cannot directly inject into 97.79° SSO with that RAAN without plane change; launch geometry not demonstrated.
- Orbit: Inclination 97.79° for 600 km SSO is plausible, but no hand calculation of J2 nodal precession shown; only a plot.
- Launch: Selecting Vega E (first launch 2024, unproven) for a 2025 mission is high risk; no delta-v or payload mass analysis.
- Ground Control & Communications: Access table has duplicate row 15 and inconsistent date formatting; mean duration stated as ~10 min but table mean is 580.8 s (~9.7 min), acceptable but rounding unclear.
- Mission Duration & EOL: Drag sail discussion truncated; no deorbit time estimate or casualty risk assessment; statement that satellite is 'without thrusters' conflicts with earlier mention of orbital manoeuvre at EOL.
- Orbit: Swath/altitude trade not quantified; 600 km choice not supported by resolution calculation.

## Next steps

1. Add hand calculations for J2 nodal precession and launch delta-v/payload mass, and demonstrate the launch-site-to-RAAN geometry or justify the plane change.
2. Complete the EOL analysis with a deorbit time estimate and casualty risk, and resolve the thruster inconsistency between the manoeuvre and EOL sections.
3. Replace bare-URL and Wikipedia references with properly formatted citations, add numbered figure captions, and proofread for typos and awkward phrasing.

---
<sub>Run 20261112-055905-865_Input_2_md_r1 | rubric=deepseek/deepseek-v4.1-flash-1017, task=deepseek/deepseek-v4.1-flash-1017, marking=deepseek/deepseek-v4.1-flash-1017, feedback=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 12524/1434 | cost $0.001144 | 29.55s</sub>
