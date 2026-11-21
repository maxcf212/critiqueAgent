# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 100 / 100 (100%)**

You produced an exemplary, technically sophisticated space mission design report for ZYZZsat. Your justification for coral bleaching monitoring, thorough analytical hand calculations, and seamless STK modeling demonstrated outstanding engineering rigor across all sections. Your self-critical appraisal in Section 3 was particularly mature. To push this work toward flight-ready standard, address the minor technical omissions in communication link budgets and ground station tracking capabilities.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 10 / 10 | 10 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 10 / 10 | 60 / 60 |
| C3 Conclusion | Accomplished | 10 / 10 | 10 / 10 |
| C4 Report presentation | Accomplished | 10 / 10 | 20 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (10/10, Accomplished)

You achieved Accomplished by establishing a compelling rationale for Great Barrier Reef monitoring in Section 1. Your single-spacecraft architecture, operational user definitions, and literature support thoroughly addressed all requirements. To maintain this high standard in future work, continue directly mapping user data latency requirements to orbital revisit trade-offs.

*Assessor reasoning:* All introductory requirements are addressed to a very high standard. The coral bleaching rationale is compelling and backed by relevant literature. The single-spacecraft architecture is justified convincingly against revisit requirements. Users, operators, and funding arrangements are explicitly specified.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (60/60, Accomplished)

You achieved Accomplished through rigorous orbital mechanics, launch vehicle selection, and atmospheric decay analysis matching STK outputs in Section 2. To build on this level of technical depth, provide a formal RF link budget for the 50 Mbit/s X-band downlink and verify slew-rate constraints for the Mount Pleasant antenna during fast LEO passes.

*Assessor reasoning:* The mission design is technically rigorous and thorough. Orbital mechanics, launch vehicle selection, azimuth calculations, diffraction optics sizing, access duration, data volume budgets, and analytical atmospheric drag decay calculations are accurate, clearly explained, and closely tied to STK outputs.
> 2.3 Orbit: "The orbit is near-polar and retrograde, so over time the satellite passes over all latitudes up to 82°."  

### C3 Conclusion (10/10, Accomplished)

You achieved Accomplished by delivering a concise, evidence-based synthesis in Section 3. Your candid critical appraisal of engineering limitations—including launcher flight heritage, fluid lensing efficacy, and ground station modifications—showed mature engineering judgment. To further elevate future project conclusions, consider proposing targeted risk-reduction test plans for the key uncertainties identified.

*Assessor reasoning:* The conclusion concisely synthesises core findings and provides an insightful critical appraisal of four genuine engineering limitations (launcher flight heritage, fluid lensing efficacy, ground station modifications, and nadir repeat cycle).
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  

### C4 Report presentation (20/20, Accomplished)

You achieved Accomplished with a polished, logically structured report. Your Executive Summary was comprehensive, graphical and tabular data were clearly formatted, and IEEE references matched the bibliography accurately. Maintain this professional presentation by continuing to ensure all appendix data and configuration files are explicitly referenced within the main text.

*Assessor reasoning:* The document is structured logically as a professional engineering report. Formatting, tables, equation layout, and figure captions are consistent. The executive summary is comprehensive and IEEE references are properly cited.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite for monitoring coral bleaching on the Great Barrier Reef."  

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
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Bibliography |

## Technical issues

- 2.4 Ground Control & Communications: A formal RF link budget (transmit power, G/T, path loss, margin) for the 50 Mbit/s X-band downlink was omitted, as acknowledged.
- 2.4 Ground Control & Communications: Mount Pleasant 12 m antenna is primarily a geodetic VLBI dish; slew-rate limits and tracking performance for low-elevation LEO passes should be verified.

## Next steps

1. Formulate a formal RF link budget for the 50 Mbit/s X-band downlink in Section 2.4, calculating transmit power, path loss, G/T, and link margin.
2. Verify the tracking performance and slew-rate limits of the Mount Pleasant 12 m antenna for fast, low-elevation LEO passes.
3. Develop targeted risk-reduction and testing roadmaps for the engineering limitations identified in Section 3, specifically launcher flight heritage and fluid lensing.

---
<sub>Run Input_2_u-Run_1-Eff_high-261116-131133 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18787/8935 | cost $0.038983 (incl. $0.001387 for the reused reference rubric+task structure) | 47.78s</sub>
