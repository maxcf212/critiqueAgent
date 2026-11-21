# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 81 / 100 (81%)**

You present a strong, well-organised preliminary mission design with a clear Australian benefit, substantial orbital and operations analysis, and useful STK evidence. Your conclusions identify important limitations. To make the proposed capabilities more convincing, verify imaging and communications performance and replace simplified revisit estimates with coverage analysis that includes mission constraints.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 8 / 10 | 8 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

In Section 1, you clearly explain the mission, its need, the single-spacecraft choice, and the operator and customers, with cited rationale. To strengthen this, substantiate the mission-performance case and ensure the cited evidence directly supports it.

*Assessor reasoning:* Clearly states the mission, explains the need and rationale, justifies a single spacecraft, and identifies the operator and customer groups. The rationale is specific and supported with citations, although the cited evidence and mission-performance case could be more rigorously substantiated.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)"  
> 1 Introduction: "The customers are the Great Barrier Reef Marine Park Authority"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

You address launch, orbit, maneuvers, ground communications, mission duration and EOL, and provide STK evidence. To make the design more persuasive, verify imaging feasibility and the link budget, and assess actual constrained reef coverage rather than treating the approximate five-day revisit as demonstrated access.

*Assessor reasoning:* Comprehensive preliminary design with launch alternatives, orbital elements and J2 sun-synchronous calculation, STK figures/access results, communications/data budget, and a reasoned EOL concept. Strong evidence overall. The link budget is explicitly absent, performance feasibility is not fully demonstrated, and the revisit estimates rely on simplified geometry rather than reported mission coverage analysis.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "The orbit is circular, so it has no perigee and two of the six classical orbital elements, the argument of perigee and the true anomaly, are undefined."  
> 2.3 Orbit: "No orbital manoeuvres are required."  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC)"  
> 2.5 Mission Duration & EOL: "The mission lasts five years."  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

### C3 Conclusion (8/10, Accomplished)

Your Section 3 draws specific conclusions and identifies four limitations and next steps. Keep linking conclusions to demonstrated results, and distinguish preliminary estimates—especially imaging performance, downlink capacity and revisit—from verified mission capability.

*Assessor reasoning:* Draws specific conclusions from the proposed orbit, coverage, communications, and EOL analysis, and identifies important limitations and next steps. Conclusions are relevant rather than generic, though some claimed performance remains preliminary.
> 3 Conclusion: "The design has four limitations."  
> 3 Conclusion: "With these points addressed in the next design phase, the mission can provide the direct, regular bleaching maps that current temperature-based monitoring cannot."  

### C4 Report presentation (16/20, Accomplished)

Your executive summary, section structure, labelled figures and tables, and bibliography support a clear report. For a more professional and evidence-led presentation, complete or strengthen source details and support key engineering assumptions with traceable calculations and analysis.

*Assessor reasoning:* Clear report structure, executive summary, labelled figures and tables, generally professional writing, and a bibliography corresponding to in-text citations. Some source entries are incomplete or less authoritative than ideal, and key engineering assumptions (notably imaging feasibility and link performance) are not supported by detailed evidence.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite"  
> 2 Mission Design: "The mission is described in five parts: the spacecraft, launch, orbit, ground control and communications, and mission duration and end of life (EOL)."  
> 2.3 Orbit: "Figure 1: STK 3D view of the ZYZZsat orbit at two times 12 hours apart (generated in STK 11)."  
> Bibliography: "[11] D. A. Vallado, Fundamentals of Astrodynamics and Applications, 4th ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3 Orbit |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Throughout report |

## Technical issues

- 2.3 Orbit: The approximately five-day revisit estimate divides equatorial ground-track spacing by maximum roll-reach width. It does not demonstrate actual access to every reef location under the selected imaging, lighting, cloud, and pointing constraints; treat it as an approximate geometric estimate.
- 2.1 Spacecraft overview: The 5 m GSD and 60 km swath are derived from pixel count and focal-plane geometry, but no radiometric/SNR, detector, or optical system performance analysis establishes that the proposed 0.10 m aperture can deliver usable multispectral reef imagery.
- 2.4 Ground Control & Communications: The report acknowledges that no X-band link budget has been calculated. Thus the assumed 50 Mbit/s rate and resulting daily downlink margin are not verified for the stated spacecraft, antenna, and station.

## Next steps

1. In Section 2.1, substantiate the proposed 5 m GSD and 60 km swath with detector, optical-system and radiometric/SNR analysis, including whether the 0.10 m aperture can provide usable multispectral reef imagery.
2. In Section 2.4, calculate an X-band link budget for the stated spacecraft, antenna and ground station to verify the assumed 50 Mbit/s rate and daily downlink margin. In Section 2.3, test reef access against imaging, lighting, cloud and pointing constraints rather than relying on geometric revisit estimates.
3. Retain the specific limitations and next-phase direction in Section 3, and strengthen the supporting evidence with complete, authoritative references and traceable calculations or software outputs. These steps will make your design conclusions and report presentation more robust.

---
<sub>Run Input_2_u-Run_1-Eff_low-261118-133317 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 15050/4813 | cost $0.004287 (incl. $0.001387 for the reused reference rubric+task structure) | 36.85s</sub>
