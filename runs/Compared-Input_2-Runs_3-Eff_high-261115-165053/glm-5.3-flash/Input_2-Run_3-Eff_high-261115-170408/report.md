# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 67 / 100 (67%)**

A well-structured mission design for a fluid-lensing reef-monitoring satellite, addressing nearly all requirements with genuine STK evidence and a sensible SSO and ground-station choice. The introduction is strong, but presentation and referencing (including Wikipedia) hold the report back, and a few technical statements contain contradictions. With cleaner figures, proper references and resolved reasoning, this design could reach the top rubric level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Adequate | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (8/10, Accomplished)

Mark: 8/10 (Accomplished). You addressed all required elements: the primary mission (fluid-lensing reef monitoring), a well-cited rationale using bleaching statistics, a clear single-spacecraft justification, and identified users such as CSIRO and BOM. To reach the very top of the band, make the operator and customer roles more explicit and expand the user discussion with a little more detail on how each user would access or apply the mission data.

*Assessor reasoning:* All required elements addressed: primary mission (fluid-lensing reef monitoring), rationale with cited bleaching statistics, single-spacecraft justification, and users/funding. Detail is good with references, though user discussion is brief and operator/customer roles could be more explicit.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  
> Introduction: "The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (42/60, Accomplished)

Mark: 7/10 (Accomplished). All major requirements are covered: Vega E from Guiana Space Centre with justification, a 600 km SSO with a correct COE table (a = 6971 km, i = 97.79°), manoeuvres, STK-based access analysis for Mt Pleasant, and duration/EOL plans. To advance further, fix the contradiction that low resolution is 'desirable', quantify the contact-geometry claim about near-vertical inclination passes, show at least one hand calculation, and supply explicit STK files or an appendix.

*Assessor reasoning:* All major requirements addressed: launch site/vehicle with justification, SSO with COE table (a=6971km, i=97.79° correct for 600km SSO), manoeuvres, ground station with STK access report, duration and EOL. Weakened by the altitude/resolution contradiction, unclear provenance of the inclination plot, no hand calculations shown, and no explicit STK files/appendix.
> Mission Design - Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre Spaceport."  
> Mission Design - Orbit: "an altitude of 600km requires a mean inclination of 97.7924°"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below"  
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’"  

### C3 Conclusion (7/10, Adequate)

Mark: 7/10 (Adequate, at the top of the band). Your conclusions follow from the evidence and honestly acknowledge design risks, such as Vega E not yet being built and the fallback to Vega C. To reach Accomplished, go beyond summarising: draw deeper engineering insights, for example discussing coverage gaps between passes, data latency for time-critical reef monitoring, or how the EOL choice affects mission risk.

*Assessor reasoning:* Conclusions follow from the evidence and acknowledge design risks (Vega E availability, fallback to Vega C). Somewhat summary-like rather than drawing deeper engineering insights (e.g. coverage gaps, data latency), but specific and appropriate.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (10/20, Adequate)

Mark: 5/10 (Adequate). Your structure is clear, with headings and an executive summary, and in-text citations match the reference list. However, figures and tables lack numbers, references are bare URLs with Wikipedia used (explicitly disallowed), and there are grammar and typo errors ('a Earth observation', 'complied', 'purposed', 'current owned'). Careful proofreading, consistent reference formatting and numbered, captioned figures would lift this to Accomplished.

*Assessor reasoning:* Clear structure with headings and executive summary; in-text citations match list. However, figures/tables lack numbers, references are bare URLs with Wikipedia used (explicitly disallowed), and there are grammar/typo errors ('a Earth observation', 'complied', 'purposed', 'current owned'). Not professional-level presentation.
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Orbit: "STK 3D view of orbit: 12 hours apart"  
> Ground Control & Communications: "This station is current owned and operated by the University of Tasmania"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | Introduction |
| R4 | State the launch site and launch vehicle. | yes | Mission Design - Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design - Orbit (COE table) |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design - Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications (STK) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Screenshots provided (Images 1-5, access report) but no explicit STK files or appendix mentioned |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Structure and citations present, but Wikipedia cited and reference formatting poor |

## Technical issues

- Mission Design - Orbit: Contradictory statement: 'A very high altitude would yield low resolution images which is also desirable' – low resolution is not desirable; likely a missing negation.
- Bibliography [6]: Wikipedia used as a source, explicitly not acceptable per task requirements.
- Mission Duration & EOL: Redundant/contradictory reasoning: uncontrolled descent considered then dismissed because satellite 'is without thrust capability', which was already stated; drag sail discussion incomplete sentence.
- Mission Design - Orbit: Inclination-vs-altitude plot (Image 3) provenance unclear – appears reproduced without clear citation or shown hand calculation; RAAN=27.33° justified only loosely as launch-site location.
- Ground Control & Communications: Claim that vertical inclination 'maintains a significant contact for the vast majority of passes' is imprecise; contact geometry not quantified beyond STK output.

## Next steps

1. Replace the Wikipedia citation with a primary or peer-reviewed source, and format all references consistently (e.g. IEEE style) so each in-text citation maps cleanly to a full bibliographic entry.
2. Number and caption all figures and tables (e.g. 'Figure 1: STK 3D view of orbit'), and clearly state the provenance of the inclination-vs-altitude plot, citing its source or showing the hand calculation behind it.
3. Include your STK scenario files or an appendix listing them, and add a short hand calculation (e.g. SSO inclination or access-duration estimate) to strengthen the evidence for your design choices.

---
<sub>Run Input_2-Run_3-Eff_high-261115-170408 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15391/4871 | cost $0.002613 (incl. $0.001387 for the reused reference rubric+task structure) | 63.74s</sub>
