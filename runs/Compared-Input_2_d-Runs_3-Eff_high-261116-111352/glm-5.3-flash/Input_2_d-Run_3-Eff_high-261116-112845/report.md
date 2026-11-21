# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 59 / 100 (59%)**

Your report presents a well-structured, comprehensive mission design for Great Barrier Reef monitoring, supported by genuine STK evidence including access reports and orbital element tables. However, several technical inconsistencies (inclination, Kourou latitude, contact duration), unnumbered figures, and use of Wikipedia hold the work back. Careful technical review and stronger referencing would lift this to the accomplished level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 6 / 10 | 6 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (6/10, Adequate)

Your Introduction clearly explains the mission purpose, its rationale for the Great Barrier Reef, and justifies the single-spacecraft choice with references. To reach the accomplished level, explicitly identify the operator and the customers/users (e.g. which agency operates it, who purchases or accesses the data) rather than leaving them implied.

*Assessor reasoning:* Mission, rationale and single-spacecraft choice are well explained with references. However, users (operator and customers) are only vaguely implied ('operated and accessed from Australia ground facilities', scientists as beneficiaries) rather than explicitly identified, so not all requirements are met to a high standard.
> Introduction: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated satellite monitoring."  
> Introduction: "Thus, only one satellite is required."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (36/60, Adequate)

All major requirements are addressed with STK screenshots, access summaries and element tables, which is a real strength. However, key errors undermine accuracy: the stated 87.79° inclination contradicts your own plot (~97.9°) and cannot be sun-synchronous; Kourou's latitude is ~5°N, not 45.05°N; the 'twenty minutes' contact claim conflicts with your 580.8 s mean; the RAAN justification is dubious; and STK files are not referenced. Resolving these inconsistencies and providing the software files would support the accomplished level.

*Assessor reasoning:* All major requirements addressed with STK screenshots, access reports and element tables. However, key errors: stated inclination 87.79° contradicts the student's own plot (~97.9°) and is not sun-synchronous/retrograde; Kourou latitude given as 45.05°N (actually ~5°N); 'twenty minutes' contradicts the 580.8 s mean; STK files not mentioned. Comprehensive but not fully accurate.
> Mission Design - Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Mission Design - Orbit: "an altitude of 600km requires a mean inclination of 87.7924°"  
> Ground Control & Communications: "An average contact duration of almost twenty minutes was achieved"  
> Mission Duration & EOL: "A span of five years is a sound estimate of the useful lifespan"  

### C3 Conclusion (7/10, Accomplished)

Your conclusions are specific and evidence-based, including a candid acknowledgement of Vega E availability risk with a Vega C mitigation - excellent practice. To strengthen further, quantify key outcomes (e.g. coverage statistics, data volumes) so conclusions flow more directly from the analysis presented.

*Assessor reasoning:* Conclusions are specific and trace back to the analysis, including a candid risk (Vega E availability) and mitigation (Vega C). Slightly brief and does not quantify outcomes, but clearly evidence-based rather than generic.
> Conclusion: "A specific launch vehicle – the Vega E – has been selected although it has not been built yet."  

### C4 Report presentation (10/20, Adequate)

The report has a clear structure with an executive summary and logical sections. To reach the accomplished level: number all figures and tables and cite them in text, replace bare URLs (and the disallowed Wikipedia source) with properly formatted references, and proofread for slips such as 'which is also desirable' and 'for the purposed of'.

*Assessor reasoning:* Clear structure with executive summary and logical sections, but figures/tables lack numbers (e.g. 'STK 3D view of orbit'), bibliography is bare URLs including Wikipedia (unacceptable per task), and there are grammar slips ('which is also desirable', 'for the purposed of'). Not professional level; adequate.
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Design - Orbit: "STK 3D view of orbit: 12 hours apart"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction - 'Thus, only one satellite is required.' |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction - operator/customers only implied, never explicitly identified |
| R4 | State the launch site and launch vehicle. | yes | Mission Design - Launch (Vega E from Kourou) |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | Mission Design - Orbit (SSO, COE table) |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | Mission Design - Orbit ('the only orbital maneuver occurs at the EOL segment') |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | Ground Control & Communications (Mt Pleasant, STK access summary) |
| R8 | Specify mission duration and end-of-life plans. | yes | Mission Duration & EOL (5 years, drag sail) |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Orbit/Ground Control sections (STK 11 used, inclination plot) |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Screenshots provided (Images 1-5) but no mention of STK files in report or appendix |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | Structure logical, but Wikipedia cited and figures/tables unnumbered |

## Technical issues

- Mission Design - Launch: Kourou latitude stated as 45.05°N; actual is ~5.05°N. The subsequent launch-window reasoning is built on this error.
- Mission Design - Orbit: Stated sun-synchronous inclination 87.79° at 600 km contradicts the student's own plot (~97.9°); 87.79° is prograde, not retrograde, and cannot be sun-synchronous.
- Ground Control & Communications: 'Average contact duration of almost twenty minutes' contradicts the STK mean duration of 580.786 s (~9.7 min).
- Mission Design - Orbit: 'A very high altitude would yield low resolution images which is also desirable' - contradiction; low resolution is undesirable here.
- Mission Design - Orbit: RAAN of 27.33° justified as 'location of the launch facility' is technically dubious; RAAN relates to the orbital plane, not the launch site latitude.
- Bibliography: Wikipedia ([6]) used, which the task explicitly disallows; references are bare URLs without proper formatting.

## Next steps

1. Cross-check every stated number against your own STK outputs and plots before submission - especially inclination, site coordinates and contact durations.
2. Number all figures and tables, cite them in the text, and replace Wikipedia with primary sources formatted in a consistent citation style.
3. Explicitly name the operator and customer segments in the Introduction, and reference your STK scenario files in the main body or an appendix.

---
<sub>Run Input_2_d-Run_3-Eff_high-261116-112845 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 15343/4943 | cost $0.002711 (incl. $0.001387 for the reused reference rubric+task structure) | 69.02s</sub>
