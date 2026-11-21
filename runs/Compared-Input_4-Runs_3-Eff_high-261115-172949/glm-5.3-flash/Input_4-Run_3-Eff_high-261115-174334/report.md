# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

A strong, well-structured submission with scenario-specific justifications throughout. Q1 and Q2 are well argued, and Q4 applies the Circuit Breaker convincingly. To reach the top band: make the availability response measure measurable, complete the end-to-end calculation in Q3(c), apply CAP correctly in Q5, add a negative consequence to your ADR, and trim Q2 to 150 words. Total: 29/40.

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

You chose suitable attributes and justified them well from the scenario (900 lunch orders, 4.2 s p95, payment outage). Your performance scenario is complete and measurable. To reach Excellent, both scenarios need all six parts with measurable response measures — your availability measure ('stay up most of the time') is not measurable. Replace it with something quantifiable, such as 99.9% uptime or a maximum downtime figure.

*Assessor reasoning:* Performance and availability are well justified from the scenario (900 lunch orders, 4.2 s p95, payment outage). The performance scenario is complete and measurable, but the availability response measure ('stay up most of the time') is not measurable, matching the Proficient descriptor.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work. Your recommendation of a modular monolith is justified by two scenario-specific trade-offs: the five-developer team's overhead of running many services, and the lunchtime load being caused by deployment/VM issues rather than the monolith. You also explicitly acknowledged the downside (modules cannot be scaled independently; a bug can crash the whole process). This is a solid Excellent answer.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team overhead; lunchtime load and 20-minute downtime caused by deployment/VM, not the monolith). Downside of the recommendation explicitly acknowledged. Solid Excellent, not exceptional.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct with working shown (99.30%; 5.0 h). In part (c) you correctly computed the parallel payment pair (0.999975) but reported it as the end-to-end availability. You must multiply it by the other components in series: 0.99800125 × 0.999975 ≈ 99.80%, giving ≈1.5 h monthly downtime. Show this full working to reach Excellent.

*Assessor reasoning:* Parts (a) and (b) are correct with working (0.99301 → 99.30%; 5.0 h). Part (c) correctly computes the parallel payment pair (0.999975) but reports it as the end-to-end availability, omitting multiplication by the other components (correct: ≈99.80%, ≈1.5 h downtime). One part incorrect → Proficient.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You named the Circuit Breaker correctly, explained the Closed/Open/Half-Open mechanism accurately, and applied it concretely to the 25-minute outage. To reach Excellent (5/5), state an explicit drawback or tuning consideration as its own point — for example, that a poorly tuned failure threshold can trip the breaker on transient spikes, or that Half-Open probing adds latency.

*Assessor reasoning:* Circuit Breaker correctly named and its Closed/Open/Half-Open mechanism explained accurately, and applied concretely to the 25-minute outage. A tuning consideration (failure threshold) is only implicit within the mechanism; no explicit drawback is stated, so not full marks.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both choices (availability for browsing, consistency for payments) are reasonable and well justified, and you named concrete techniques (Redis TTL cache, idempotency keys). However, CAP is misapplied: you wrote that payments 'give up partition tolerance', but partitions are inevitable and cannot be sacrificed. During a partition you must choose between consistency and availability — say payments sacrifice availability. Fixing this statement is the key step to Excellent.

*Assessor reasoning:* Both choices (availability for browsing, consistency for payment) are reasonable and justified; concrete techniques named (Redis TTL cache, idempotency keys). However, CAP is misapplied: partition tolerance cannot be 'given up'—partitions are inevitable; choosing C means sacrificing A during a partition.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has all three sections, and Context, Decision and Consequences are specific to CampusEats (synchronous tablet calls, 4.2 s p95, offline tablets). However, your consequences are entirely positive. To reach Excellent, add at least one negative consequence, such as delayed or eventually consistent order notifications, or the operational overhead of running and monitoring RabbitMQ.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (synchronous tablet calls, 4.2 s p95, offline tablets). Consequences are entirely positive—no negative consequence (e.g., eventual notification delay, operational overhead of RabbitMQ) is given, so Excellent (5) is not reached.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear, the required headings are used, and you cite sources in IEEE style with a reference list. The one issue keeping you from Excellent is that Question 2 exceeds the 150-word limit (roughly 190 words). Tighten that answer by cutting generic phrasing so every answer fits the limit, and consider explicitly stating any assumptions you make.

*Assessor reasoning:* Writing is clear, headings used, IEEE-style in-text citations [1], [2] and reference list present. However, Question 2 clearly exceeds the 150-word limit (roughly 190 words), matching the Proficient descriptor of one answer over the limit.
> Question 2: "Second, the known problems are not caused by the monolith itself."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 (c) — end-to-end availability/downtime incorrect |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 — CAP theorem misapplied for payments |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 — no negative consequence |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References present in IEEE style, but no assumptions are explicitly stated |

## Technical issues

- Question 3 (c): End-to-end availability should be 0.99800125 × 0.999975 ≈ 99.80% with ≈1.5 h monthly downtime; the student reported the payment-pair availability (99.9975%) as the whole order-placement availability.
- Question 5: CAP theorem misstated: one cannot 'give up partition tolerance'; during a partition the choice is between consistency and availability.
- Question 1: Availability response measure ('stay up most of the time') is not measurable.
- Question 6: ADR consequences are one-sided; no negative consequence such as delayed or eventually-consistent notifications is given.
- Question 2: Answer exceeds the 150-word limit.

## Next steps

1. Redo Q3(c): multiply the payment-pair availability (0.999975) by the other components to get end-to-end availability ≈99.80% and ≈1.5 h monthly downtime, showing the working.
2. Rewrite the Q5 CAP statement: partition tolerance cannot be given up; during a partition you choose between consistency and availability, so say payments sacrifice availability.
3. Add at least one negative consequence to the Q6 ADR (e.g., delayed or eventually consistent notifications) and make the Q1 availability response measure measurable (e.g., a percentage uptime).

---
<sub>Run Input_4-Run_3-Eff_high-261115-174334 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8314/7099 | cost $0.00346 (incl. $0.001628 for the reused reference rubric+task structure) | 83.4s</sub>
