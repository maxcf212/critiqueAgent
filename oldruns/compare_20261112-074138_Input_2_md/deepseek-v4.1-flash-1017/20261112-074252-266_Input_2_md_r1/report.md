# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 62 / 100 (62%)**

Your coral-reef mission is comprehensive and well structured, with all major design elements and a clear STK access analysis. To reach the next level, tighten technical accuracy, include software files and hand calculations, and improve figure/table numbering and referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

You clearly define the primary mission, need, single-spacecraft rationale and users (CSIRO, BOM) in the Introduction, meeting all requirements. To reach Accomplished fully, strengthen referencing beyond general web pages and add more specific literature support for the mission need and user requirements.

*Assessor reasoning:* Covers primary mission, need, single-spacecraft rationale and users with references; detailed and relevant. Minor weakness: some sources are general web pages, but introduction meets all required elements.
> Introduction: "The spacecraft is intended to image and send data to ground stations for collation and analysis."  
> Introduction: "only one satellite is required"  
> Introduction: "used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

Your Mission Design covers launch, orbit, manoeuvres, ground control, communications, duration and EOL with STK screenshots and an access table. To move from Adequate to Accomplished, correct the RAAN explanation, fix the inconsistent access table, include software files and hand calculations (SSO/J2, link budget, drag-sail deorbit), and justify 600 km with swath/resolution.

*Assessor reasoning:* All major design elements are addressed with STK screenshots/access table, but technical errors (RAAN explanation, access table inconsistency), missing software files and no hand calculations/link budget mean evidence is not fully quality/accurate; adequate rather than accomplished.
> Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Orbit: "an altitude of 600km requires a mean inclination of"  
> Ground Control & Communications: "An average contact duration of almost ten minutes was achieved"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan"  
> Image 4  

### C3 Conclusion (8/10, Accomplished)

Your Conclusion draws specific, evidence-based conclusions on launch vehicle, orbit and mission benefit, which is strong. To fully secure Accomplished, make every conclusion traceable to report evidence and avoid generic caveats; explicitly link each conclusion to the design results and limitations you presented.

*Assessor reasoning:* Conclusion draws specific conclusions on launch, orbit, ground station and mission benefit from report evidence; mostly detailed, though some caveats are generic.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "A polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle."  

### C4 Report presentation (10/20, Adequate)

You use clear headings and a readable structure, but figures lack numbers, tables lack captions, and there are typos/grammar issues. The bibliography is URL-only and includes Wikipedia. To reach Accomplished, number and caption all figures/tables consistently, proofread carefully, and use properly cited, credible references matching in-text citations.

*Assessor reasoning:* Clear headings and readable structure, but figures lack numbers, tables lack captions, typos/grammar issues, bibliography URL-only and Wikipedia source; presentation is adequate not professional.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Image 4  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Design a space mission that benefits Australia in some way, keeping the mission concept simple (e.g. bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | Introduction |
| R2 | Identify and describe the main elements of the mission's space segment. | yes | Mission Design |
| R3 | State the spacecraft's primary mission. | yes | Introduction |
| R4 | State whether one or multiple spacecraft will be used. | yes | Introduction |
| R5 | Identify the users, including the operator and customers. | yes | Introduction |
| R6 | Specify the launch site and the launch vehicle. | yes | Launch |
| R7 | Specify the orbit type and its characteristics and orbital elements. | yes | Orbit |
| R8 | Identify any orbital manoeuvres required. | yes | Orbit |
| R9 | Identify the ground control facilities to be used and state how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R10 | State the mission duration and the plans for end-of-life (EOL). | yes | Mission Duration & EOL |
| R11 | Complete the design using software of choice (STK, PIGI, or other software such as flightclub only after contacting Naomi to discuss), supplementing with hand calculations as needed; if using PIGI, register for the competition to obtain a licence. | yes | Ground Control & Communications |
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | partial | Image 4 / Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary; Contents; Conclusion; Bibliography |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Image 4 |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Launch: RAAN 27.33° is said to indicate launch facility location; RAAN is inertial and set by launch time/azimuth, not directly by site.
- Orbit: Statement that very high altitude yields low resolution 'which is also desirable' is contradictory; should be undesirable.
- Ground Control & Communications: STK access table contains duplicate access 15 and inconsistent access 6 (3 Feb start, 4 Feb stop, 365 s), so statistics are unreliable.
- Ground Control & Communications: Mt Pleasant Radio Observatory is a radio astronomy facility; no evidence/link budget that it can support TT&C/data downlink.
- Mission Design: No STK/PIGI software files included in submission; only screenshots/table.
- Orbit: No hand calculation/derivation for SSO inclination or J2 precession; plot only.
- Mission Duration & EOL: Drag-sail deorbit not quantified (sail area, deorbit time, 25-year rule compliance).
- Bibliography: Wikipedia used as source [6]; bibliography is URL-only and [10] malformed.
- Orbit: 'constant supply of sunlight' inaccurate for SSO; eclipse periods exist.
- Ground Control & Communications: No data rate/link budget or ground station contact capacity calculation.
- Launch: Vega E not operational; reliance on unbuilt vehicle with only brief backup.
- Orbit: 600 km altitude not justified by swath/resolution calculation; 250 km reef width vs sensor swath missing.

## Next steps

1. Add STK/PIGI software files and hand calculations (e.g., SSO inclination/J2 precession, link budget, drag-sail deorbit) to support your design evidence.
2. Correct technical statements: RAAN is not set directly by launch site; remove 'constant sunlight' for SSO; fix duplicate/inconsistent STK access entries and justify 600 km with swath/resolution.
3. Replace Wikipedia/URL-only bibliography with proper cited sources, number all figures/tables, and proofread for typos and grammar.

---
<sub>Run 20261112-074252-266_Input_2_md_r1 | rubric=deepseek/deepseek-v4.1-flash-1017, task=deepseek/deepseek-v4.1-flash-1017, marking=deepseek/deepseek-v4.1-flash-1017, feedback=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 12721/8924 | cost $0.006627 | 48.21s</sub>
