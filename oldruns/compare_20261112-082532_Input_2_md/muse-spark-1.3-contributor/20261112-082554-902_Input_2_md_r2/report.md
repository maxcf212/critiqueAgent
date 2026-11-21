# AERO9500 Final Report (Part 2) – Space Mission Design: Graded Feedback

**Total: 72 / 100 (72%)**

You delivered a solid coral reef monitoring SSO mission with clear rationale, single-sat justification, STK analysis and Australian-focused ground segment and EOL plan. Introduction and mission design are strong. Orbital mechanics descriptions and report presentation need attention to reach full Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Adequate | 6 / 10 | 6 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale - Include the following required information: • What is the spacecraft's primary mission? • Why is the mission needed? • How many spacecraft are used and why? • Who are the users (operator and customers)? (8/10, Accomplished)

You covered all four prompts well in Introduction - coral fluid-lensing mission for bleaching, single-sat cost and revisit rationale, and users CSIRO/BOM. To strengthen within Accomplished, add more specific detail on operator control and deepen literature references for bleaching drivers.

*Assessor reasoning:* All four introduction prompts covered: coral reef fluid-lensing mission, rationale bleaching, single spacecraft justification due to slow events and cost, users CSIRO/BOM and operator Australian facilities/university. Good references.
> Introduction: "dedicated satellite monitoring. A near-real-time relay to monitoring stations"  
> Introduction: "Only one satellite is required. This also just allows for simplicity"  
> Introduction: "likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design - Present a summary of the mission design using software and/or hand calculations as appropriate - Include relevant screenshots and software files (in the main body of the report and/or appendix) - Include the following information: • Where it will launch from, and using which launch vehicle? Why did you choose this option? • What type of orbit will you use? What are its characteristics and orbital elements? • Will you need to perform any orbital maneuvers? • Which ground control facilities will you use? • How often will your spacecraft be able to communicate with ground control? • How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

You showed high understanding with STK orbit views, ground tracks, access table contact durations, SSO inclination vs altitude plot and COE table, plus Vega E from Guiana rationale. To reach top of Accomplished, fix the Argument of Latitude and RAAN explanation and correct the equatorial SSO benefit argument.

*Assessor reasoning:* Shows STK orbit views, ground tracks, access table, SSO inclination vs altitude plot, COE table. Launch site/provider rationale with equatorial benefit and rideshare examples. Maneuvers identified as direct injection plus drag sail EOL. Ground station frequency/duration quantified.
> Launch: "proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana"  
> Orbit: "altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous" *(quote not found in submission)*  
> Ground Control & Communications: "Average contact duration of almost ten minutes was achieved, in addition to the already frequent"  

### C3 Conclusion (6/10, Adequate)

Your Conclusion recaps launch, polar SSO illumination, ground station and mission benefit. To move to Accomplished, avoid generic recap and provide a quantitative synthesis of your evidence, e.g., revisit, contact time, mission duration, and explicitly link limitations like Vega E readiness to design margins.

*Assessor reasoning:* Conclusion recaps launch, orbit, ground station and mission benefit, links evidence to problem. Somewhat generic, notes future risk if Vega E not ready, but lacks quantitative synthesis.
> Conclusion: "fully described satellite configuration has been constructed. The initial problem of not catching coral bleaching"  
> Conclusion: "polar sun-synchronous orbit allows for consistent illumination of the oceans while maintaining a constant sun angle"  

### C4 Report presentation (10/20, Adequate)

You used a clear engineering structure with Executive Summary and sections and generally correct grammar. To reach Accomplished, label every figure/table with number, title and source and reference it in text, remove unlabelled Image 1, and replace prohibited Wikipedia sources with credible engineering sources.

*Assessor reasoning:* Clear engineering structure with executive summary, contents, sections. Grammar generally ok. Figures present but not fully/correctly labelled with number/title/reference; tables lack numbers. Uses prohibited Wikipedia source and inconsistent citation style.
> Executive Summary: "outlines the intended designs and procedures involved in the construction of a Earth observation"  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]"  
> Image 1  

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
| R12 | Include relevant screenshots and all relevant STK or PIGI files with the report or in the appendix. | yes | Ground Control & Communications |
| R13 | Produce the report as a single PDF document with the required sections: executive summary, introduction, main body, conclusion, bibliography. | yes | Executive Summary |
| R14 | Fully and correctly label all figures and tables (figure number, title, and reference if necessary). | partial | Image 1 |
| R15 | Clearly identify and properly cite and reference all text, diagrams, ideas or other information not originating with the student; do not use Wikipedia as a proper source. | partial | Bibliography |

## Technical issues

- Orbit: Uses Argument of Latitude as replacement for undefined true anomaly/argument of perigee; should use mean anomaly or state both undefined but still acceptable. RAAN described as launch site location 27.33° without proper LTAN derivation.
- Launch: Claims max equatorial rotational benefit for SSO retrograde launch from Kourou; SSO launches actually benefit from near-polar site and require dogleg, equatorial advantage not applicable.
- Bibliography: Relies on Wikipedia Timeline of spaceflight for launch manifests and NOAA blogs; prohibited low credibility source for engineering design justification.

## Next steps

1. In Orbit section, correct COE definitions: for circular SSO state e=0 so argument of perigee and true anomaly undefined - use mean anomaly, not Argument of Latitude; derive RAAN from LTAN rather than launch site latitude 27.33°.
2. In Launch, revise equatorial benefit claim: Vega-C/E from Kourou for retrograde SSO does not gain max rotational benefit and needs a dogleg; justify via polar performance and rideshare availability.
3. In Report presentation, add numbered titles and in-text references for all figures/tables, and replace Wikipedia Timeline and NOAA blogs with manufacturer user manuals, launch provider data and peer-reviewed sources using consistent citation style.

---
<sub>Run 20261112-082554-902_Input_2_md_r2 | rubric=meta/muse-spark-1.3-contributor, task=meta/muse-spark-1.3-contributor, marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 13126/2340 | cost $0.000716 | 22.07s</sub>
