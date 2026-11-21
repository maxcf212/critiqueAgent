# AERO9500 Final Report (Part 2): Graded Feedback

**Total: 69 / 100 (69%)**

You produced a solid, well-motivated Great Barrier Reef monitoring mission with good SSO design, STK evidence, and clear launch and ground segment justification. You met most requirements strongly. To reach full marks, fix the RAAN definition, complete the link budget frequency, replace Wikipedia, and tighten report presentation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale | Accomplished | 8 / 10 | 8 / 10 |
| C2 Main body: mission design | Accomplished | 7 / 10 | 42 / 60 |
| C3 Conclusion | Accomplished | 7 / 10 | 7 / 10 |
| C4 Report presentation | Adequate | 6 / 10 | 12 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale (8/10, Accomplished)

You did well defining your coral-reef monitoring concept on p.4-5, with bleaching rationale, fluid lensing, and clear users like CSIRO/BOM and single-satellite justification. This is Accomplished work. For top of band, add more quantitative literature on revisit needs.

*Assessor reasoning:* Defines coral reef monitoring to benefit Australia, rationale with bleaching stats and fluid lensing, single satellite justification, users CSIRO/BOM/University/Gov. Referenced literature.
> p.4: "Coral reefs, specifically the Great Barrier Reef, would immensely benefit from dedicated"  
> p.5: "Thus, only one satellite is required. This also just allows for simplicity"  
> p.5: "would likely be used by governmental and science agencies (e.g. CSIRO, BOM)"  

### C2 Main body: mission design (42/60, Accomplished)

Strong main body: Vega E justification p.8, 600km SSO calculation p.11 with 97.79 deg inclination, and STK ground access p.13. To improve: p.12 RAAN 27.33 deg is not launch longitude - RAAN is inertial. p.11 missing communication frequency/link budget. Add maneuver details.

*Assessor reasoning:* Covers launch, sun-synchronous LEO 600km with COEs, STK screenshots, ground access report, EOL drag sail. Some logic gaps and missing frequency.
> p.8: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> p.11: "Specifically, an altitude of 600km requires a mean inclination of 97.7924°"  
> p.13: "ground facility within Australia will suffice. As explained, a more polar latitude"  

### C3 Conclusion (7/10, Accomplished)

Good summary on p.16 linking launch, SSO, ground station and EOL drag sail back to evidence. This is Accomplished. For higher, make conclusions more specific - e.g., quantitative coverage, revisit, and deorbit time - rather than generic configuration statement.

*Assessor reasoning:* Summarizes launch vehicle, orbit type, ground station, mission purpose and EOL, linked to evidence.
> p.16: "After analysis of each mission segment, a fully described satellite configuration has been constructed." *(quote not found in PDF)*  

### C4 Report presentation (12/20, Adequate)

Clear structure and labelled STK figures with executive summary p.2-3. To reach Accomplished: p.17 replace Wikipedia source [6] which brief forbids and fix bibliography formatting, and p.15 complete truncated EOL sentence 'to ‘ and is suitable' for professionalism.

*Assessor reasoning:* Clear headings, executive summary, figures labelled. Bibliography poorly formatted, Wikipedia used as source contrary to requirements, some incomplete sentences.
> p.2: "This report outlines the intended designs and procedures involved in the construction"  
> p.3: "Executive Summary ...........................................................................................2"  

## Task requirements

| ID | Requirement | Met | Page |
|---|---|---|---|
| R1 | Define spacecraft's primary mission - must benefit Australia, keep concept simple (examples: bushfire tracking/alert, weather satellite, internet/communication, Earth observation for city planning/real estate). | yes | 4 |
| R2 | State whether one or multiple spacecraft will be used. | yes | 5 |
| R3 | Identify users (operator and customers). | yes | 5 |
| R4 | Specify launch location and launch vehicle. | yes | 8 |
| R5 | Specify orbit type, its characteristics and orbital elements. | yes | 11 |
| R6 | Determine if any orbital maneuvers are required and detail them. | partial | 12 |
| R7 | Identify which ground control facilities will be used and how often spacecraft can communicate with ground control, including coverage analysis. | yes | 13 |
| R8 | Define mission duration and plans for End-of-Life (EOL). | yes | 15 |
| R9 | Use mission design software of choice (STK industry-standard, PIGI from Saber Astronautics requires competition registration for license, or other e.g. flightclub only after contacting Naomi) to complete design, supplemented with hand calculations as needed. | yes | 10 |
| R10 | Include in main body all space segment aspects: launch, orbit, ground stations, coverage, mission operation and end-of-life. | yes | 6 |

## Technical issues

- p.12: COE table lists RAAN 27.33 deg as launch facility location; RAAN is Earth-inertial and not equal to launch longitude, misunderstanding.
- p.11: Missing communication frequency / link budget; requirement to define frequency not addressed.
- p.17: Uses Wikipedia https://en.wikipedia.org/wiki/2021_in_spaceflight [6] as reference which brief states not acceptable.
- p.15: EOL drag sail description truncated: 'utilising a large surface area to ‘ and is suitable' - incomplete.

## Next steps

1. Correct p.12 COE table: explain RAAN in inertial frame, set RAAN from SSO LTAN requirement and list launch site latitude/longitude separately.
2. Complete p.11 comms: state UHF/S/X-band frequency, show simple link budget table for your Australian ground station to meet requirements.
3. Replace Wikipedia [6] with primary source, fix reference formatting, and proofread p.15 drag sail paragraph for final submission polish.

---
<sub>Run 20261111-144243-895_Input_2_all_spark13_fixed | rubric=meta/muse-spark-1.3-contributor, task=meta/muse-spark-1.3-contributor, marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 61146/4142 | cost $0.006943 | 63.38s</sub>
