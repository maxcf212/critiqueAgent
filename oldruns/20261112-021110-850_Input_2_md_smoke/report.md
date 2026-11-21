# AERO9500 Final Report (Part 2) - T3 2020 Assignment: Graded Feedback

**Total: 59 / 100 (59%)**

You delivered a solid, well-justified coral-reef monitoring mission with clear Australian benefit and good STK evidence. Your single-satellite rationale and user definition were strong. Technical definitions in Orbit and missing comms details (frequency, GBR coverage quantification, link budget) kept the design at Adequate rather than Accomplished.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design | Adequate | 6 / 10 | 36 / 60 |
| C3 Conclusion | Adequate | 5 / 10 | 5 / 10 |
| C4 Report presentation | Adequate | 5 / 10 | 10 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale (8/10, Accomplished)

You did well framing coral reef/ocean monitoring for fluid lensing, justifying one satellite for bleaching timescales, and naming users like CSIRO/BOM in your Introduction. To stay at Accomplished, keep that level of specific rationale and fully cited references in future work.

*Assessor reasoning:* Primary mission (coral reef monitoring benefiting Australia), single spacecraft rationale (bleaching over days/weeks), users/operators clearly stated with context, supported by references. Meets all required info to high standard.
> Introduction: "coral reef and ocean monitoring. The satellite must provide images for a fluid lensing tool"  
> Introduction: "only one satellite is required. This also just allows for simplicity"  
> Introduction: "likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design (36/60, Adequate)

You demonstrated good understanding: Vega E from Guiana Space Centre rationale in Launch, 600km SSO with 97.7924deg calculation in Orbit, and Mt Pleasant access report in Ground Control. For Accomplished: correct RAAN (not 27.33deg latitude), use proper AOP/nu not Arg of Latitude, verify Vega E performance with mass budget, add frequency band/link budget, quantify GBR swath and daily revisits, not just 580s mean contact.

*Assessor reasoning:* Demonstrates adequate understanding: launch vehicle/site with rationale, SSO orbit type, 600km altitude, inclination calculation and table of elements, maneuver note, ground station with STK access report, EOL drag sail. Some errors: RAAN described as launch facility location, Arg of lat misuse, swath not quantified, comm frequency band missing, Vega E not yet flown but used as definitive choice. Evidence present (Image 1-5, plots, tables).
> Launch: "proposed satellite will thus use the Vega E rocket as a launch vehicle – launched from the Guiana Space Centre"  
> Orbit: "altitude of 600km requires a mean inclination of 97.7924° for the satellite to remain sun-synchronous" *(quote not found in submission)*  
> Ground Control & Communications: "Satellite-ZYZZsat-To-Facility-Mt_Pleasant_Radio_Observatory: Access Summary Report"  

### C3 Conclusion (5/10, Adequate)

Your Conclusion usefully summarises segments and benefits. For Accomplished, draw specific quantitative conclusions from your evidence - e.g., from Images 1-5, your inclination table, and Access Summary - on coverage performance, contact statistics, and risks/mitigations, rather than generic reiteration.

*Assessor reasoning:* Conclusion summarizes mission segments and reiterates launch, orbit, ground station and benefit but lacks quantitative conclusions drawn from STK results (e.g., coverage performance, contact duration stats) and risk/mitigation. Generic but appropriate.
> Conclusion: "fully described satellite configuration has been constructed. The initial problem of not catching coral bleaching events"  

### C4 Report presentation (10/20, Adequate)

You used clear headings and included STK screenshots and tables, making the report readable. For Accomplished, format tables consistently, add titles/captions to Images 4-5, make executive summary concise, and replace Wikipedia with primary sources with consistent in-text citations matching your reference list.

*Assessor reasoning:* Has logical structure, headings, figures labelled partially, readable but formatting inconsistent (tables broken, STK screenshots lacking titles), uses Wikipedia despite prohibition, references not properly formatted, executive summary present but not concise. Meets adequate level.
> Image 4  
> Bibliography: "https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Define spacecraft's primary mission, must benefit Australia, keep concept simple (examples: bushfire tracking and alert, weather satellite, internet/communication, earth observation for city planning/real estate) | yes | Introduction |
| R2 | State whether mission uses one or multiple spacecraft | yes | Introduction |
| R3 | Identify users (operator and customers) | yes | Introduction |
| R4 | Specify launch location and launch vehicle | yes | Launch |
| R5 | Specify orbit type, its characteristics and orbital elements | yes | Orbit |
| R6 | Determine if any orbital maneuvers are required | yes | Orbit |
| R7 | Identify which ground control facilities will be used and how often spacecraft can communicate with ground control | partial | Ground Control & Communications |
| R8 | Define mission duration and plans for end-of-life (EOL) | yes | Mission Duration & EOL |
| R9 | Use software of choice for design (STK, PIGI requiring competition registration for license, or other with instructor approval) supplemented with hand calculations | yes | Ground Control & Communications |
| R10 | Cover in main body space segment elements: launch, orbit, ground stations, coverage, mission operation and end-of-life | yes | Mission Design |

## Technical issues

- Orbit: RAAN value 27.33° linked to launch facility latitude, incorrect definition; Argument of Latitude used to replace AOP/ν but not valid classic element set; e=0 claim circular but J2 perturbed SSO typically slightly eccentric; no communication frequency band defined despite requirement.
- Launch: Selects Vega E (first flight 2024 planned, not yet proven in 2020 assignment) without performance verification or mass budget; equatorial launch benefit argument applied to SSO retrograde which reduces benefit; references Wikipedia timeline as primary source despite ban.
- Ground Control & Communications: Access report shows mean ~580s contact but fails to compute daily communication opportunities/revisit to GBR; no link budget, frequency, or data rate.

## Next steps

1. Fix classical elements in Orbit: define RAAN correctly, replace Argument of Latitude with AOP= and nu, set slightly eccentric e for J2-perturbed SSO with hand calc, and add swath/Revisit analysis for GBR not just ground station.
2. Complete Ground Control & Communications: specify communications frequency band, add link budget with data rate, and compute daily GBR imaging opportunities from STK beyond the Mt Pleasant 580s access mean.
3. In Launch, justify Vega E vs flown alternative in 2020 with performance/mass budget and correct equatorial benefit argument for retrograde SSO; replace Wikipedia references with manufacturer/user guides and format references consistently.

---
<sub>Run 20261112-021110-850_Input_2_md_smoke | rubric=meta/muse-spark-1.3-contributor, task=meta/muse-spark-1.3-contributor, marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 14308/4076 | cost $0.002246 | 37.53s</sub>
