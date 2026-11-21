# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You submitted a strong, well-written set of answers with scenario-specific justifications throughout, especially in Q2 and Q6. The main issues are a conceptual error in Q3(c) end-to-end availability, an imprecise CAP explanation in Q5, a one-sided ADR, a non-measurable availability response measure in Q1, and a word-limit breach in Q2. Fixing these would lift several criteria to the top rubric levels.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose suitable attributes and justified them well from the scenario, with a complete, measurable performance scenario (p95 under 1.5 s, no dropped requests). To reach Excellent, make the availability response measure measurable too — 'stay up most of the time' is not; try a concrete target such as 99.9% monthly uptime.

*Assessor reasoning:* Performance and availability are well justified from the scenario (900 lunch orders, 4.2 s p95, payment outage). Performance scenario is complete and measurable, but the availability response measure ('stay up most of the time') is not measurable, so Proficient.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped"  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work: a clear modular-monolith recommendation with scenario-specific trade-offs (five developers, single-VM lunchtime load, 20-minute deployment downtime) and the downside acknowledged. Your second argument reads more as justification than a trade-off; framing it as a genuine trade-off would secure the top of the range.

*Assessor reasoning:* Clear recommendation (modular monolith) with scenario-specific trade-offs (five-developer team, single-VM lunchtime load, 20-minute deployment downtime) and the downside explicitly acknowledged. The second argument is more justification than trade-off, so not the top of the range.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct with working shown. In (c) you reported only the paired payment availability (99.9975%) and omitted recombination with the other components; the correct end-to-end figure is ≈99.80%, giving ≈1.5 h downtime, not 0.018 h. Also report downtime to one decimal place as required. Fixing (c) alone would reach Excellent.

*Assessor reasoning:* Parts (a) and (b) are correct with working (0.99301, 5.0 h). Part (c) is conceptually wrong: the student reports only the paired payment availability (99.9975%) and omits recombination with the other three components; correct end-to-end is ≈99.80% and ≈1.5 h downtime. Exactly one part incorrect, so Proficient.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You named the Circuit Breaker correctly, explained its states well, and applied it concretely to the 25-minute outage. For the full 5 marks, state an explicit drawback or tuning consideration as such — for example, discussing how to choose the failure threshold or the risk of tripping on transient faults — rather than embedding it in the mechanism.

*Assessor reasoning:* Circuit Breaker is correctly named and its states/mechanism explained well, and it is concretely applied to the 25-minute outage. However, no explicit drawback or tuning consideration is stated as such; the threshold example is embedded in the mechanism, not offered as a consideration.
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging for 25 minutes."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both choices (availability for browsing, consistency for payments) are reasonable and well justified, with concrete techniques (Redis TTL cache, idempotency keys). However, CAP is used imprecisely: you wrote that you 'give up partition tolerance', but partition tolerance cannot be sacrificed — during a partition the choice is between consistency and availability. Correcting this would reach Excellent.

*Assessor reasoning:* Both choices (availability for browsing, consistency for payment) are reasonable and justified, with concrete techniques (Redis TTL cache, idempotency keys). But CAP is used imprecisely: partition tolerance cannot be 'given up'; during a partition one must choose between C and A.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are all present and specific to CampusEats (synchronous tablet calls, 4.2 s p95, offline tablets). To reach Excellent, add at least one negative consequence — for example, delayed order notifications to the outlet or added operational complexity from the asynchronous flow — since your consequences are currently one-sided.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (synchronous tablet calls, 4.2 s p95, offline tablets). However, the consequences are one-sided: only benefits are listed, with no negative consequence such as eventual notification delay or added operational complexity.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear, headings are used in order, and IEEE-style citations [1], [2] with a reference list are present. However, Q2 exceeds the 150-word limit (roughly 190 words) and Q4 is borderline. Tightening every answer to within 150 words would secure the full 4 marks for communication.

*Assessor reasoning:* Writing is clear, headings are used in order, and IEEE-style citations [1], [2] with a reference list are present. However, Question 2 clearly exceeds the 150-word limit (roughly 190 words), and Question 4 is borderline, so Proficient.
> Question 2: "A rewrite would freeze feature work for months without directly fixing either problem."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3 (c): End-to-end availability incorrectly reported as 99.9975%; the paired payment availability (0.999975) must be multiplied by the other components: 0.99800125 × 0.999975 ≈ 99.80%, giving ≈1.5 h downtime, not 0.018 h.
- Question 3 (c): Downtime of 0.018 hours is not given to one decimal place as required.
- Question 5: CAP theorem misapplied: partition tolerance cannot be sacrificed; during a partition the choice is between consistency and availability.
- Question 1: Availability response measure ('stay up most of the time') is not measurable.
- Question 6: No negative consequence stated in the ADR.
- Whole document: No assumptions explicitly stated, contrary to the task instruction.

## Next steps

1. In Q3(c), multiply the paired payment availability (0.999975) by the other components (0.99800125 × 0.999975 ≈ 99.80%) and report downtime to one decimal place (≈1.5 h).
2. In Q5, correct your CAP explanation: partition tolerance cannot be sacrificed; during a partition you must choose between consistency and availability.
3. Add a negative consequence to your Q6 ADR, make the Q1 availability response measure measurable, and trim Q2 to under 150 words.

---
<sub>Run Input_4-Run_2-Eff_high-261115-174220 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8278/7002 | cost $0.003523 (incl. $0.001628 for the reused reference rubric+task structure) | 73.31s</sub>
