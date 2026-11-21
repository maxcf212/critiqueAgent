# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 82 / 100 (82%)**

You have produced a well-organised report that addresses every requirement, with checkable orbit, drag and access calculations supported by STK files in Appendix A. Your conclusions are specific and quantified. Marks were reduced mainly for a few numerical inconsistencies, unjustified assumptions in the data budget and eclipse analysis, an unsourced figure, and some uncited statements. Addressing these would strengthen an already strong report.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Accomplished | 9 / 10 | 9 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Accomplished | 8 / 10 | 48 / 60 |
| C3 Conclusion | Accomplished | 9 / 10 | 9 / 10 |
| C4 Report presentation | Accomplished | 8 / 10 | 16 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (9/10, Accomplished)

You clearly address all four required items: the primary mission, why it is needed, the single-spacecraft choice and its justification, and the operator and customers. Your rationale is supported by several cited sources, including NOAA, AIMS context and fluid lensing papers. To strengthen it further, add citations to the claim about hundreds of millions relying on reefs and to your funding statement, which are currently unreferenced.

*Assessor reasoning:* All four required items are addressed: primary mission, need, spacecraft count with justification, and operator and customers. Rationale is developed with multiple cited sources (NOAA, AIMS context, fluid lensing papers). Minor gaps: some claims are uncited (for example, hundreds of millions relying on reefs, and funding statement).
> 1 Introduction: "The operator is the Australian Institute of Marine Science (AIMS), which already runs the long-term monitoring program for the reef"  
> 1 Introduction: "One satellite is therefore used. This also simplifies communications, reduces cost, and requires less time to build and launch."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (48/60, Accomplished)

Your design is comprehensive and well evidenced, covering launch on Vega C, orbit elements, manoeuvres, ground station, contact statistics, data budget and end-of-life. Your key calculations check out and are backed by STK figures and appendix files. Marks were reduced for the contact-time percentage that does not match your figures, an unjustified daily-imaging assumption, an unsourced Figure 2, and an eclipse duration that is asserted rather than derived.

*Assessor reasoning:* Comprehensive design covering launch, orbit elements, inclination derivation, manoeuvres, ground station, contact statistics, data budget and EOL. Checked calculations (inclination, period, RAAN rate, drag decay, access totals) are correct and supported by STK figures and appendix files. Deductions for a 60% versus 510/771 (66%) inconsistency, an unjustified one-strip-per-day assumption, an unsourced Figure 2, and an unverified eclipse figure.
> 2.2 Launch: "The baseline is an SSMS rideshare flight on Vega C from Kourou in early 2025"  
> 2.4 Ground Control & Communications: "the mean pass lasts 580.8 s, or 9.7 minutes"  
> 2.5 Mission Duration & EOL: "Without the sail the satellite would stay in orbit for about 32 years, longer than the guideline allows, so the sail is necessary."  

### C3 Conclusion (9/10, Accomplished)

Your conclusions are detailed and follow from your evidence, quantifying the result that a 4 m² drag sail removes the satellite in about two years compared with about 32 years without it. You also identify four specific limitations, namely the Vega C launch risk, fluid lensing at 5 m, the missing X-band link budget and the 45-day revisit, and propose mitigations for each.

*Assessor reasoning:* Conclusions summarise quantified results and state four specific limitations (Vega C risk, fluid lensing at 5 m, missing X-band link budget, 45-day revisit) with proposed mitigations. Conclusions follow from the evidence in the report.
> 3 Conclusion: "a 4 m² drag sail removes the satellite in about two years, compared with about 32 years without it."  

### C4 Report presentation (16/20, Accomplished)

Your report follows a clear engineering structure, with an executive summary, numbered sections, labelled tables and figures, and an appendix of STK files, and uses consistent IEEE-style citations. Marks were reduced for awkward phrasing (for example, 'but this is not even the full extent of their nurture' in Section 1), a contents list without page numbers, an unsourced Figure 2, and several uncited statements.

*Assessor reasoning:* Clear engineering structure with executive summary, numbered sections, labelled tables and figures, and an appendix of STK files. Consistent IEEE-style citations. Deductions for awkward phrasing, a contents list without page numbers, an unsourced figure, and several uncited statements.
> 1 Introduction: "but this is not even the full extent of their nurture"  
> 2.4 Ground Control & Communications: "Table 6: Daily data budget."  

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
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | 2.4 Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | yes | Appendix A: STK files and settings |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | partial | 1 Introduction |

## Technical issues

- 2.4 Ground Control & Communications: 510 s of 771 s is about 66%, not 60%. The stated 34 min/day corresponds to 60% of 57 min, so the contact-time figure is inconsistent with the cited fraction (66% gives about 38 min).
- Table 6: Daily data budget: Downlink time labelled as 34 minutes, but 2,000 s is 33.3 minutes. Small rounding inconsistency feeding the 3.5× margin.
- Table 6: Daily data budget: Daily imaging of one 60 km × 1,000 km strip is asserted without justification against 14.9 orbits per day and the 5-day revisit claim. The 4:1 compression ratio is also unreferenced.
- 2.3 Orbit: Eclipse duration of 34 min is asserted, not derived from the 08:45 node time or beta angle. It is close to the worst-case value, so the battery sizing claim is unsupported.
- Figure 2: Figure 2 caption gives no source or credit, though the plot appears to come from an external or MATLAB model, breaching the citation requirement (R11).
- 2.5 Mission Duration & EOL: Lifetime estimate H/rate assumes a constant decay rate, but drag accelerates as altitude falls, so 2.2 and 32-year figures are only rough order-of-magnitude values, not stated as such.

## Next steps

1. Reconcile the contact-time figures in Section 2.4: 510 s of 771 s is about 66%, not the 60% stated, so check the 34 minutes per day against this.
2. Justify the one-strip-per-day imaging assumption in Table 6 against your 14.9 orbits per day and 5-day revisit claim, cite a source for the 4:1 compression ratio, and correct the downlink time (2,000 s is 33.3 minutes, not 34).
3. Derive your 34-minute eclipse duration from the node time or beta angle, credit the source of Figure 2, cite the uncited claims (such as the reef-dependent value and the funding statement), and describe the lifetime estimates as order-of-magnitude because drag increases as altitude falls.

---
<sub>Run Input_2_u-Run_3-Eff_high-261116-130528 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 20987/26377 | cost $0.013999 (incl. $0.001387 for the reused reference rubric+task structure) | 110.9s</sub>
