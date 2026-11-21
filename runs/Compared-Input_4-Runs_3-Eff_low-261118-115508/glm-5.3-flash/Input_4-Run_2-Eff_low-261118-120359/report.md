# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

A strong submission overall. Your modular monolith recommendation in Q2 is excellent, and Q3(a)(b) show correct working. To reach higher marks: make Q1's availability response measure measurable, fix the Q3(c) series calculation, apply CAP correctly in Q5, add a negative consequence in Q6, and trim Q2 to 150 words.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 | 6 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose suitable attributes (performance, availability) with good scenario justification and six-part scenarios. To reach Excellent, both response measures must be measurable — 'stay up most of the time' is not. Replace it with a quantified target such as a percentage uptime over a stated period, and double-check the other scenario's measures too.

*Assessor reasoning:* Performance and availability are well justified from the scenario and scenarios use six-part form, but the availability response measure ('stay up most of the time') is not measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. Your modular monolith recommendation is justified with two scenario-specific trade-offs (five-developer team overhead; problems traced to the single VM and deployment process) and you explicitly acknowledge the downside of independent scaling. This fully meets the Excellent level — keep this standard for future justifications.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team overhead; problems traced to single VM and deployment process) and the downside explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (6/8, Proficient)

Parts (a) and (b) are correct with working shown. In part (c) you report 99.9975% (the payment-pair availability) as the end-to-end availability. The method requires multiplying the series: 0.998001 × 0.999975 ≈ 99.80%, giving ≈1.5 h downtime per month, not 0.018 h. Fixing this single slip moves you toward Excellent.

*Assessor reasoning:* Parts (a) and (b) are correct with working. Part (c) is wrong: the student reports the combined payment availability (99.9975%) as the end-to-end availability instead of recomputing the series (≈99.80%, ≈1.5 h downtime). One part incorrect, method otherwise correct.
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You correctly named and explained the circuit breaker (Closed/Open/Half-Open) and applied it to the outage with a sensible user-facing message. For the full 5 marks, add an explicit drawback or tuning consideration — e.g. payments fail while the breaker is Open, or how the threshold should be tuned to avoid tripping on transient faults.

*Assessor reasoning:* Circuit breaker correctly named and explained (Closed/Open/Half-Open) and applied to the outage, but no explicit drawback or tuning consideration beyond an example threshold; no downside such as failed payments during Open state is discussed.
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter""  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices (Redis TTL cache, idempotency keys) are concrete and reasonable, but CAP is misapplied: you claim choosing both consistency and availability and giving up partition tolerance. During a partition only C or A can be kept — frame payments as CP, sacrificing availability during the partition. Correcting this and ensuring a technique for each case reaches Excellent.

*Assessor reasoning:* Both choices are reasonable with concrete techniques (Redis TTL cache, idempotency keys), but CAP is misapplied: under a partition one cannot choose both C and A; the correct framing is CP, sacrificing availability during the partition.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your ADR has scenario-specific Context, Decision and Consequences, but the consequences are one-sided — only benefits are listed. Add at least one negative consequence, such as eventual notification delay or added message-queue infrastructure complexity. With that, all three sections plus balanced consequences meet the Excellent level.

*Assessor reasoning:* Context, Decision and Consequences are present and scenario-specific, but consequences are one-sided: only benefits are listed, with no negative consequence (e.g. eventual notification delay, added infrastructure complexity).
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear, headings are used correctly, and IEEE citations and a reference list are present. However, Question 2 clearly exceeds the 150-word limit, which prevents the Excellent level. Keep answers within limits while preserving the quality of your trade-off discussion.

*Assessor reasoning:* Writing is clear, headings used, IEEE citations and reference list present. However Question 2 clearly exceeds the 150-word limit, so not Excellent.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 3 (c): Reports 99.9975% (payment-pair availability) as end-to-end availability; correct series result is 0.998001×0.999975≈99.80%, downtime ≈1.5 h/month, not 0.018 h.
- Question 5: CAP theorem misstated: claims choosing both consistency and availability and giving up partition tolerance; during a partition only C or A can be kept.
- Question 1: Availability response measure 'stay up most of the time' is not measurable.

## Next steps

1. Rewrite the availability response measure in Q1 as a measurable target, e.g. '99.9% uptime measured monthly', and check both scenarios' response measures are quantified.
2. In Q3(c), multiply the order-path availability (0.998001) by the new payment-pair availability (0.999975) to get ≈99.80% end-to-end, giving ≈1.5 h downtime per month; show the working.
3. In Q5, restate CAP correctly: during a partition you must choose C or A, so frame the payment choice as CP (sacrificing availability during the partition), and add a technique for the other case.
4. Add at least one negative consequence to your Q6 ADR, e.g. delayed order confirmation or added queue infrastructure complexity.
5. Trim Q2 to within 150 words while keeping both scenario-specific trade-offs and the acknowledged downside.

---
<sub>Run Input_4-Run_2-Eff_low-261118-120359 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 7989/4937 | cost $0.002874 (incl. $0.001628 for the reused reference rubric+task structure) | 52.8s</sub>
