# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

A strong submission overall. Q2 was excellent with scenario-specific trade-offs, and Q1, Q3, Q4, Q5 and Q6 all showed sound method. To lift marks: make the availability response measure measurable, include the non-payment components in Q3(c), apply CAP correctly in Q5, add a negative consequence to the ADR, and keep every answer within 150 words.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 | 6 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose suitable attributes (performance and availability) with good scenario-based justification, and your performance scenario was fully six-part and measurable. To reach Excellent, both response measures must be measurable: 'stay up most of the time' is not. Replace it with a quantified target, e.g. '99.5% availability measured monthly', and keep the six-part structure for both scenarios.

*Assessor reasoning:* Performance and availability are well justified from the scenario and performance scenario is fully six-part and measurable, but the availability response measure ('stay up most of the time') is not measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work. Your modular monolith recommendation was clearly justified with two trade-offs tied to the scenario — the five-developer team size and the root causes of the known problems — and you acknowledged the downside (no independent scaling, one bug can crash the process). This meets the Excellent standard; just watch the 150-word limit (see C7).

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (team size, root causes of known problems) and the downside of the recommendation explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (6/8, Proficient)

Parts (a) and (b) were correct with working shown (99.30%, 5.0 h). Part (c) reported only the payment-pair availability (99.9975%) and dropped the other three components. The end-to-end availability is 0.9980010×0.999975 ≈ 99.80%, about 1.5 h downtime per month. Your method is sound — show the full product in part (c) to reach Excellent.

*Assessor reasoning:* Parts (a) and (b) are correct with working (99.30%, 5.0 h). Part (c) is wrong: the student reports only the payment-pair availability (99.9975%) and omits the other three components; correct end-to-end is ~99.80% with ~1.5 h downtime. One part incorrect, method otherwise correct.
> Question 3 (c): "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You named the circuit breaker correctly, explained its states and thresholds well, and applied it convincingly to the outage with a realistic user-facing message. The missing element for full marks is an explicit drawback or tuning consideration — e.g. false trips on slow (rather than failed) calls, or how to choose the failure threshold and timeout values.

*Assessor reasoning:* Circuit breaker correctly named and explained (states, thresholds) and applied to the outage, but no explicit drawback or tuning consideration is given beyond an example threshold.
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter""  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both choices were reasonable and you named concrete techniques (Redis TTL cache; idempotency keys), which is good. However, CAP was misapplied: 'giving up partition tolerance' is not an option — partitions will happen, so the real choice during a partition is between consistency and availability. Restate each choice as C-over-A or A-over-C under partition to reach Excellent.

*Assessor reasoning:* Both choices justified with concrete techniques (Redis TTL cache; idempotency keys), but CAP is applied incorrectly: partition tolerance cannot be given up; during a partition one must trade C against A.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR had all three sections, scenario-specific context and a clear decision, and the positive consequence (faster order placement) was well stated. What held it at Proficient was the one-sided consequences: add at least one negative consequence, such as eventual outlet notification, duplicate-order handling, or extra infrastructure cost.

*Assessor reasoning:* Context, Decision and Consequences are present and scenario-specific, but consequences are one-sided; no negative consequence (e.g. eventual notification, extra infrastructure, duplicate handling) is stated.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings, ordering and IEEE citations were correct, but Q2 (~200 words) and Q4 (~160 words) exceeded the 150-word limit and no assumptions were stated. Practise writing tight, prioritised answers: state assumptions in one line, cut generic textbook material, and count words before submitting to reach the Excellent level.

*Assessor reasoning:* Headings, order and IEEE citations/references are correct, but at least two answers (Q2 ~200 words, Q4 ~160 words) exceed the 150-word limit, and no assumptions are stated.
> Question 2: "First, team size versus operational overhead."  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 (c) |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3 (c): End-to-end availability after adding the second payment provider is computed as the payment-pair availability alone (99.9975%); the other three components (0.9995×0.999×0.9995) were dropped. Correct: 0.9980010×0.999975 ≈ 99.80%, downtime ≈ 1.5 h/month.
- Question 5: CAP theorem misapplied: 'give up partition tolerance' is not a valid choice; partitions must be tolerated, forcing a C-vs-A choice during a partition.
- Question 1: Availability response measure 'stay up most of the time' is not measurable.
- Question 6: No negative consequence given in the ADR.

## Next steps

1. In Q3(c), multiply the payment-pair availability (0.999975) by the other three components (0.9995×0.999×0.9995) to get the end-to-end availability (~99.80%, ~1.5 h downtime) rather than reporting the payment pair alone.
2. In Q5, reframe the CAP argument: partition tolerance cannot be given up; during a partition you must choose between consistency and availability, so justify each choice as C or A under partition.
3. In Q6, add at least one negative consequence (e.g. delayed outlet notification, duplicate-order handling, extra infrastructure) to balance the ADR.
4. Trim Q2 and Q4 to 150 words each, stating any assumptions explicitly, and make the Q1 availability response measure measurable (e.g. '99.5% uptime measured monthly').

---
<sub>Run Input_4-Run_3-Eff_low-261118-120451 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8093/5163 | cost $0.002708 (incl. $0.001628 for the reused reference rubric+task structure) | 54.88s</sub>
