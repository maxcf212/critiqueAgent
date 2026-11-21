# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 60 / 100 (60%)**

A competent, well-structured mission design that covers most requirements with STK evidence and a clear mission rationale. To reach the next level, tighten the orbital analysis (RAAN consistency, hand calculations), justify the launch vehicle with data, complete the EOL discussion, and professionalise referencing and figures.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

Your Introduction clearly states the mission purpose, the single-spacecraft rationale and the users, with literature support. To reach the top of Accomplished, firm up the user discussion (avoid 'likely') and cite specific operator/customer commitments rather than speculative wording.

*Assessor reasoning:* Mission purpose, rationale, single-spacecraft justification and users (operator/customers) all addressed with literature references. Some user detail is speculative ('likely'), but overall strong.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

You cover all major design elements with STK screenshots and an access table, but several errors weaken persuasiveness. The RAAN of 27.33° is inconsistent with a Kourou launch into a 97.79° SSO; the Vega E choice is speculative with no mass/cost analysis; no hand calculation supports the 97.7924° inclination; and the EOL paragraph is truncated. Fix these and add quantitative evidence to move from Adequate to Accomplished.

*Assessor reasoning:* All major elements covered with STK screenshots and access table. But launch choice is speculative (Vega E not yet built), RAAN 27.33° is inconsistent with Kourou launch site, no hand calcs for inclination, and EOL text is truncated. Errors reduce persuasiveness.
> Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "The proposed ZYZZsat is small and without thrusters in a low-earth orbit."  

### C3 Conclusion (6/10, Adequate)

Your Conclusion recaps the design and flags launch risk, but remains a generic summary. To reach Accomplished, state quantitative outcomes (orbit, contact frequency, lifetime) and critically assess trade-offs and residual risks against the evidence in the main body.

*Assessor reasoning:* Conclusion summarises design and notes launch risk, but is largely generic recap without quantitative outcomes or critical assessment.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

Headings and structure are logical, but referencing is not professional: bare URLs, Wikipedia as a source, and inconsistent citation formatting. Figures are partly unlabelled and some writing errors remain. To reach Accomplished, use a consistent citation style, replace Wikipedia with primary sources, label all figures/tables, and proofread.

*Assessor reasoning:* Structure and headings are logical, but references are bare URLs with OCR/typo artefacts, Wikipedia used as a source, figures partly unlabelled, and some writing errors. Not professional level.
> Bibliography: "[5] f. https://www.qrg.northwestern.edu"  
> Bibliography: "[10 d. ] https://www.thespacereview.com"  
> Launch: "a wiki sorted directory – ‘Timeline of spaceflight’ – will be referred to throughout the report [6]."  

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
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Orbit |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Contents |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Orbit |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Orbit: RAAN of 27.33° is inconsistent with a Kourou (5°N) launch into a 97.79° SSO; RAAN depends on launch time, not launch site latitude.
- Orbit: Inclination 97.7924° for 600 km SSO is plausible but no hand calculation shown; only a plotted curve.
- Launch: Selecting Vega E (first flight 2024, unbuilt) is speculative; no mass/payload compatibility or cost analysis.
- Ground Control & Communications: Access table has duplicate row 15 and a mislabelled row 6 date; mean duration stated as ~10 min but table mean is 580.8 s (~9.7 min) — minor.
- Mission Duration & EOL: EOL paragraph truncated ('utilising a large surface area to ‘'); no quantitative deorbit time or drag-sail sizing.
- Orbit: Claim that a high altitude yields 'low resolution images which is also desirable' is a wording/logic error.

## Next steps

1. Recompute and justify the RAAN for your Kourou launch time, and add a hand calculation for the 97.7924° SSO inclination to support the STK plot.
2. Replace the Vega E with a flown vehicle or provide payload mass, cost and schedule evidence; complete the EOL section with a quantitative deorbit time and drag-sail sizing.
3. Rebuild the bibliography in a consistent style using primary sources (no Wikipedia or bare URLs), label every figure and table, and proofread for wording errors such as the 'low resolution images' claim.

---
<sub>Run 20261112-055935-424_Input_2_md_r2 | rubric=deepseek/deepseek-v4.1-flash-1017, task=deepseek/deepseek-v4.1-flash-1017, marking=deepseek/deepseek-v4.1-flash-1017, feedback=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 12509/1501 | cost $0.001183 | 31.11s</sub>
