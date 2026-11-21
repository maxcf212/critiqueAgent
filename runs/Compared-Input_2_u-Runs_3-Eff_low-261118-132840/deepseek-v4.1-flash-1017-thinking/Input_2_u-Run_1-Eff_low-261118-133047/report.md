# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 88 / 100 (88%)**

Your preliminary ZYZZsat design is strong and technically sound: the launch trade, J2 sun-synchronous orbit, STK access work, data budget and drag-sail EOL are well evidenced and numerically consistent. The main gaps are the missing link, power and mass budgets and the unexamined optics volume. These are largely acknowledged. Marks are unchanged; the feedback below shows how to move each criterion toward the top of its band.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 9 / 10 | 54 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You address all four required elements in Section 1 with specific detail: mission, need, single-spacecraft rationale and AIMS/GBRMPA users. The bleaching-monitoring and resolution arguments are well made. To reach the top of Accomplished, replace the National Geographic source with peer-reviewed literature and add a little more customer-requirement detail.

*Assessor reasoning:* All four required elements (primary mission, rationale/need, number of spacecraft with justification, operator and customers) are addressed in detail with literature support on bleaching monitoring and resolution limitations. Well argued and specific; minor reliance on non-scholarly sources (National Geographic) keeps it just below top.
> 1 Introduction: "The primary mission of ZYZZsat is to image the whole Great Barrier Reef in visible bands at 5 m resolution"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost"  
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS) ... The customers are the Great Barrier Reef Marine Park Authority" *(quote not found in submission)*  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (54/60, Accomplished)

Section 2 is comprehensive: launch trade and fallback, full orbital elements with a verified J2 SSO calculation, manoeuvre rationale, STK access, data budget, duration and drag-sail EOL. To reach the top band, close the link, power and mass budgets and examine the optics focal-length/volume issue; these are the remaining unsupported requirements.

*Assessor reasoning:* Launch site/vehicle with trade and fallback, orbit type and full elements, manoeuvre rationale, ground station, contact frequency from STK access and data budget, duration and EOL disposal are all covered. Hand calculations (period, J2 SSO inclination, swath, track spacing, drag decay, data budget) check out numerically and are validated against STK. Gaps: no link budget, no power/mass budget, optics focal-length/volume feasibility unexamined.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.3 Orbit: "cos i = −(1.991 × 10⁻⁷) / (1.5 × 1.0826 × 10⁻³ × 0.8354 × 1.0831 × 10⁻³) = −0.1355, so i = 97.79°"  
> 2.4 Ground Control & Communications: "There are six passes each day, three in the evening and three in the morning (UTC), and the mean pass lasts 580.8 s"  
> 2.5 Mission Duration & EOL: "With a 4 m² sail the satellite re-enters about two years after the end of the mission"  

### C3 Conclusion (9/10, Accomplished)

Your conclusion is specific and quantitative, drawing on revisit, pass frequency, margin and decay lifetime, and it honestly lists limitations and next steps. To secure the highest level, map each conclusion explicitly back to the mission-design requirements and state the quantified margin or evidence for each.

*Assessor reasoning:* Conclusion is specific, quantitative and derived directly from the body (revisit, passes, margin, decay lifetime), and honestly enumerates limitations and next steps. Not generic.
> 3 Conclusion: "The design has four limitations. First, Vega C has not yet flown, so the Falcon 9 rideshare service is kept as a fallback"  

### C4 Report presentation (16/20, Accomplished)

The report has a clear engineering structure, a concise abstract, numbered sections, captioned figures/tables with sources, consistent IEEE-style citations and an STK appendix. To reach the top of Accomplished, add page numbers to the contents, replace weak web references, support the reef-area claim, and check formatting consistency throughout.

*Assessor reasoning:* Clear engineering structure, concise abstract, numbered sections, captioned figures/tables with sources, consistent IEEE-style citations matching the bibliography, and an appendix listing delivered STK files. Minor weaknesses: contents list without page numbers, a couple of weak web references and some unsupported factual claims (reef area), and no explicit page-limit note.
> Executive Summary: "The design is supported by STK simulations and by hand calculations of the orbit, coverage, data budget and orbital decay."  
> Figure 1: "Figure 1: STK 3D view of the ZYZZsat orbit at two times 12 hours apart (generated in STK 11)."  
> Appendix A: STK files and settings: "The following STK 11 files are submitted with this report in ZYZZsat_STK.zip."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | 1 Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | 1 Introduction (Number of spacecraft) |
| R3 | Identify the mission's users, including operator and customers. | yes | 1 Introduction (Users) |
| R4 | State the launch site and launch vehicle. | yes | 2.2 Launch / Table 2 |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | yes | 2.3 Orbit / Table 4 |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | yes | 2.3 Orbit (Manoeuvres) |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | yes | 2.4 Ground Control & Communications / Table 5 |
| R8 | Specify mission duration and end-of-life plans. | yes | 2.5 Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.3–2.5, Appendix A |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Figures 1–4, Table 5, Appendix A |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | yes | Contents, Bibliography |

## Technical issues

- Table 1 / 2.3 Orbit: 5 m GSD at 600 km implies a focal length of roughly 0.6–1.2 m (5–10 µm pixels); fitting this in a 0.6 m box requires folded optics and is not discussed, though the diffraction aperture check is correct.
- 2.4 Ground Control & Communications: No X-band link budget (antenna gain, EIRP, C/N0, modulation) to substantiate 50 Mbit/s to a 12 m dish; acknowledged by the author as further work.
- 2.4 / Table 5: STK access computed at 0° elevation with no constraint, then corrected approximately by hand to 10° (60% usable); an elevation constraint in STK would be more rigorous.
- Table 3: Revisit estimate uses equatorial ground-track spacing and a nadir strip model; latitude-dependent spacing and roll-access geometry would change the ~5 day figure somewhat.
- 2.1 / 2.5: No mass or power budget (solar array size, battery capacity for the 34 min eclipse) to demonstrate the 50 kg bus closes.
- Table 7: Air density at 600 km (1e-13 kg/m³) is highly variable with solar activity; the lifetime figures rest on a single value, though the uncertainty is acknowledged.

## Next steps

1. Close the missing engineering budgets in Sections 2.4 and 2.5: add an X-band link budget (antenna gain, EIRP, C/N0, modulation) to substantiate 50 Mbit/s to the 12 m dish, and add mass and power budgets (solar array, battery for the 34 min eclipse) to show the 50 kg bus closes.
2. Address the optics feasibility flagged in Table 1 and Section 2.3: calculate the focal length implied by 5 m GSD at 600 km and explain how the folded optics fit within the 0.6 m box, or revise the GSD/aperture assumption.
3. Strengthen the orbit and coverage evidence: apply a 10° elevation constraint directly in STK rather than correcting 0° access by hand, and refine the revisit estimate in Table 3 for latitude-dependent ground-track spacing and roll-access geometry.

---
<sub>Run Input_2_u-Run_1-Eff_low-261118-133047 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 14533/10014 | cost $0.007194 (incl. $0.001387 for the reused reference rubric+task structure) | 38.21s</sub>
