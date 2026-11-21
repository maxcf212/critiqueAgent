# AERO9500 Final Report (Part 2): Space Mission Design: Graded Feedback

**Total: 47 / 100 (47%)**

You have produced a clear, well-structured report that covers all the major mission segments, supported by STK screenshots and a sensible single-spacecraft rationale. The main barriers to a higher grade are technical accuracy: the Kourou latitude, the unresolved launch vehicle choice, the retrograde and sun-synchronous contradiction, and unsupported lifetime and contact claims. Tightening these, identifying your users and improving your references would move the report up a level.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? | Adequate | 5 / 10 | 5 / 10 |
| C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? | Adequate | 5 / 10 | 30 / 60 |
| C3 Conclusion | Adequate | 4 / 10 | 4 / 10 |
| C4 Report presentation | Adequate | 4 / 10 | 8 / 20 |

## Feedback by criterion

### C1 Introduction: mission concept and rationale. Include the following required information: What is the spacecraft's primary mission? Why is the mission needed? How many spacecraft are used and why? Who are the users (operator and customers)? (5/10, Adequate)

Your introduction clearly states the primary mission, the reef-related rationale and why one spacecraft suffices, with good reasoning on cost and simplicity. To reach Accomplished, explicitly identify your operator and customers, develop your descriptions in more depth, and replace the Wikipedia source with high-quality literature references.

*Assessor reasoning:* Mission purpose, rationale and single-spacecraft choice are addressed with reasonable justification and references. However, users (operator and customers) are not clearly identified, and the operator/customer discussion is missing. Some claims lack citation quality (Wikipedia used as source [6]), limiting the referencing standard.
> Introduction: "Thus, only one satellite is required. This also just allows for simplicity in communications, reduces cost, and requires less time to build and launch."  
> Introduction: "Hundreds of millions of humans rely on reefs for food, natural protection, jobs, and tourism."  

### C2 Main body: mission design. Present a summary of the mission design using software and/or hand calculations as appropriate. Include relevant screenshots and software files in the main body of the report and/or appendix. Include the following information: Where will it launch from, and using which launch vehicle? Why did you choose this option? What type of orbit will you use? What are its characteristics and orbital elements? Will you need to perform any orbital maneuvers? Which ground control facilities will you use? How often will your spacecraft be able to communicate with ground control? How long will the mission last, and what are your plans for EOL? (30/60, Adequate)

Your design covers launch, the orbit with Keplerian elements, ground station access and end-of-life, and your STK screenshots give useful visual evidence. Accuracy let it down: the Kourou latitude is wrong, the launch vehicle choice is unresolved, and the retrograde near-polar description conflicts with the 87.8° sun-synchronous inclination. To reach Accomplished, make the design internally consistent, justify key values such as RAAN, and reference your STK files and calculations.

*Assessor reasoning:* Covers launch, orbit with Keplerian elements, ground station and access data, and EOL with screenshots. But launch site latitude is wrong (45.05°N for Kourou, which is ~5°N), the Vega E is not yet built and the launch is contradictory, RAAN 27.33° is not justified, the 'retrograde' claim conflicts with 87.8° SSO, the access table has duplicated numbering, no STK files are referenced, and EOL/manoeuvre analysis is thin and partly incoherent.
> Mission Design / Launch: "The proposed satellite will thus use the Vega E rocket as a launch vehicle"  
> Orbit: "the satellite will be positioned at an altitude of 600km above Earth’s surface"  
> Ground Control & Communications: "Systems Tool Kit 11 (STK) was used to calculate access periods as seen below:"  

### C3 Conclusion (4/10, Adequate)

You reach some sensible conclusions, including the launch-date risk, and summarise the mission segments. They remain generic, and your claim of constant contact is not supported by your access data, which shows gaps between passes. For Accomplished, draw specific conclusions from your evidence, covering coverage gaps and lifetime limits and what they mean for the mission.

*Assessor reasoning:* Conclusion summarises segments and notes launch-date risk, but conclusions are generic and do not critically evaluate the evidence; claim of constant long-duration contact conflicts with the reported access data (gaps between passes).
> Conclusion: "The Mt Pleasant Radio Observatory is well-located to receive data from this orbit type constantly and for long durations."  

### C4 Report presentation (8/20, Adequate)

The report has clear headings and numbered figures, giving a logical structure. Problems include an unfinished drag sail sentence, an EOL paragraph that needs revision, inconsistent table numbering, a contents entry that does not match the structure, and generic web references including Wikipedia. For Accomplished, proofread the text, label and number all tables consistently, and make every in-text citation match a proper reference list entry.

*Assessor reasoning:* Clear headings and numbered figures, but there are truncated sentences, a broken EOL paragraph, unlabeled/inconsistent tables, duplicated table numbering, Wikipedia cited despite prohibition, and a contents page referencing the wrong structure. Reference style is inconsistent and several sources are generic web URLs.
> Mission Duration & EOL: "Thus, abandoning the satellite at its EOL is not environmentally or socially responsible."  
> Bibliography: "[6] https://en.wikipedia.org/wiki/2021_in_spaceflight. [Online]."  
> Mission Duration & EOL: "The most promising alternative is a ‘drag sail’ – a drag-enhancing deorbit device that deploys at the EOL. It acts like a regular sail, utilising a large surface area to ‘ and is suitable"  
> Contents: "Executive Summary ..... 2"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Propose a simple mission that benefits Australia and explain its primary mission, overview and rationale. | yes | Introduction |
| R2 | Specify whether the mission uses one or multiple spacecraft. | yes | Introduction |
| R3 | Identify the mission's users, including operator and customers. | partial | Introduction |
| R4 | State the launch site and launch vehicle. | partial | Mission Design / Launch |
| R5 | Describe the orbit, including its type, characteristics and orbital elements. | partial | Orbit |
| R6 | State whether orbital manoeuvres are required and describe them as relevant. | partial | Orbit |
| R7 | Identify ground-control facilities and explain how often the spacecraft can communicate with ground control. | partial | Ground Control & Communications |
| R8 | Specify mission duration and end-of-life plans. | partial | Mission Duration & EOL |
| R9 | Use mission-design software; hand calculations may be added where useful. PIGI users must register for its competition to obtain a software licence. | yes | Ground Control & Communications |
| R10 | Support the mission design with relevant screenshots and provide all relevant STK or PIGI files. | partial | Orbit |
| R11 | Ensure the report has a clear, logical structure and is concise; properly identify and cite all borrowed text, diagrams, ideas and other information. | no | Bibliography |

## Technical issues

- Mission Design / Launch: Kourou latitude stated as 45.05°N; actual is about 5.2°N, and the equatorial argument is therefore inconsistent.
- Mission Design / Launch: Vega E is not yet built and is selected as the baseline, while the text alternates between Vega C, Vega E and rideshare options without a clear decision.
- Orbit: Describes the orbit as retrograde and near-polar yet states it passes over almost the entire Earth; the 'constant sun angle' and J2 explanation conflate the RAAN drift sign and rate.
- Orbit: The 'Argument of Latitude' is stated as 0° while RAAN is said to change daily; the 'initial' epoch and RAAN source are not derived.
- Ground Control & Communications: Access table repeats satellite number 13 and claims mean duration near 20 minutes; the summary table is inconsistent with the listed durations and the claim of constant contact is not supported.
- Mission Duration & EOL: A 600 km circular orbit decays within years without propulsion; 5-year life is asserted without drag or lifetime analysis, and the drag sail discussion is incomplete.

## Next steps

1. Correct and verify your launch and orbital data: use Kourou's actual latitude (about 5.2°N), commit to one launch vehicle with a clear reason, and derive or source your RAAN, argument of latitude and epoch.
2. Make your orbit description consistent by reconciling the retrograde and sun-synchronous claims and explaining the J2 drift sign. Support your 5-year life with a drag or lifetime analysis and complete the drag sail discussion.
3. Replace Wikipedia with scholarly or authoritative sources, name your operator and customers, fix the access table numbering and mean-duration figures, and proofread so every sentence is complete.

---
<sub>Run Input_2_d-Run_1-Eff_low-261118-125350 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 21193/6726 | cost $0.005536 (incl. $0.001387 for the reused reference rubric+task structure) | 45.55s</sub>
