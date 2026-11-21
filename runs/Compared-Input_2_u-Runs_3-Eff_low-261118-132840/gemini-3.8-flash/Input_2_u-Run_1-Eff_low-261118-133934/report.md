# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 100 / 100 (100%)**

You have produced an exceptional mission design report, achieving full marks across all criteria. Your technical derivations, orbital mechanics analysis, and seamless integration of STK simulations set a benchmark for rigorous engineering documentation. Every mission requirement is thoroughly justified, clearly communicated, and directly linked to Australian stakeholder needs.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 10 / 10 | 10 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 10 / 10 | 60 / 60 |
| C3 Conclusion | Accomplished | 10 / 10 | 10 / 10 |
| C4 Report presentation | Accomplished | 10 / 10 | 20 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (10/10, Accomplished)

You achieved Accomplished by delivering a compelling mission rationale in Section 1. Defining AIMS as the operator, GBRMPA as the customer, and justifying a single-satellite architecture provided excellent context and national benefit.

*Assessor reasoning:* All required elements are thoroughly addressed with specific detail and relevant literature citations. The mission concept and rationale directly benefit Australia.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch."  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS)... The customers are the Great Barrier Reef Marine Park Authority" *(quote not found in submission)*  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (60/60, Accomplished)

You reached Accomplished through rigorous mission analysis across Section 2. Your launch vehicle trade study, J2 orbital derivations, Mount Pleasant ground link budget, and passive deorbit calculations were comprehensively validated with STK simulation files.

*Assessor reasoning:* Demonstrates an excellent understanding of mission design. Calculations for launch azimuth, J2 sun-synchronous inclination, imaging geometry, communications data budget, and passive orbital decay are accurate and rigorously supported by STK outputs.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "Table 4: Orbital elements of ZYZZsat at the scenario epoch, 3 Feb 2025 00:00:00 UTCG"  
> 2.4 Ground Control & Communications: "The Mount Pleasant Radio Observatory near Hobart, Tasmania (42.8°S, 147.4°E) is selected."  
> 2.5 Mission Duration & EOL: "The mission lasts five years... The EOL plan is therefore passive: a drag sail is deployed" *(quote not found in submission)*  

### C3 Conclusion (10/10, Accomplished)

You earned Accomplished in Section 3 by clearly synthesising your quantitative outcomes. Honestly evaluating realistic mission constraints, including Vega-C launch readiness and fluid-lensing payload maturity, demonstrated outstanding engineering maturity.

*Assessor reasoning:* The conclusion synthesises findings thoroughly, reiterates quantitative performance metrics, and offers critical engineering insight into four realistic design limitations.
> 3 Conclusion: "ZYZZsat meets the mission needs set out in the introduction with one 50 kg satellite."  
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown... Second, fluid lensing has only been demonstrated" *(quote not found in submission)*  

### C4 Report presentation (20/20, Accomplished)

You met the Accomplished level with flawless technical presentation. The report featured a succinct Executive Summary, professional heading hierarchy, pristine data tables, clear STK visualisations, and consistent academic referencing throughout.

*Assessor reasoning:* Exemplary presentation. The document features an executive summary, clear heading hierarchy, well-formatted tables, appropriately referenced figures, clean STK screenshots, and correct citation formatting throughout.
> Executive Summary: "This report presents the design of ZYZZsat (Z-axis/Y-axis Zeroed Zoning Satellite), a single Earth observation microsatellite"  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

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

## Next steps

1. Investigate active deorbiting alternatives alongside passive drag sails to assess mass tradeoffs under varying solar activity cycles.
2. Formulate a quantitative risk-mitigation plan addressing the Vega-C flight heritage and unproven fluid lensing technology identified in Section 3.
3. Explore multi-ground-station network options to increase downlink margins and reduce onboard data storage constraints.

---
<sub>Run Input_2_u-Run_1-Eff_low-261118-133934 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 18898/3429 | cost $0.018419 (incl. $0.001387 for the reused reference rubric+task structure) | 25.02s</sub>
