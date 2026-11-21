# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You give a clear, well-argued modular-monolith recommendation in Question 2, and your Question 3(a) and (b) calculations are correct. Your main gaps are Question 3(c), the CAP reasoning in Question 5, a non-measurable availability target in Question 1, a one-sided decision record, and some answers over the word limit.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose performance and availability with clear justification from the lunch-hour rush, and your performance scenario is complete and measurable. To reach Excellent, replace 'stay up most of the time' with a numeric target, such as a percentage of uptime or a maximum monthly downtime, so both scenarios have measurable response measures.

*Assessor reasoning:* Performance and availability are well justified from the lunch-hour scenario. The performance scenario is complete and measurable. The availability response measure is not measurable, which caps this at Proficient.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is clear and tied to the scenario. The team-size versus operational-overhead trade-off, with five developers facing eight or ten services, is specific and well argued. You also acknowledge the downside, including the single-VM and deployment-downtime problems. Keep this level of scenario-specific reasoning.

*Assessor reasoning:* Clear modular-monolith recommendation. Two scenario-specific trade-offs: team size against operational overhead, and the single-VM and deployment-downtime problems. The downside is acknowledged explicitly.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  

### C3 Q3 Availability calculation (5/8, Proficient)

Your series-availability method is sound, and parts (a) and (b) are correct with working shown: 99.30% and 5.0 hours. Part (c) considers only the payment component and omits the other three. Multiply those by 0.999975 to get about 99.80% and about 1.5 hours per month. Also round availability to two decimal places and downtime to one.

*Assessor reasoning:* (a) 99.30% and (b) 5.0 h are correct with working. (c) omits the other three components, so end-to-end availability (about 99.80%) and downtime (about 1.5 h) are wrong. The 99.9975% figure also breaks the two-decimal requirement. Exactly one part is incorrect.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

Choosing the Circuit Breaker is appropriate, and you explain the Closed, Open and Half-Open states correctly and apply them to the outage. To reach Excellent, add at least one drawback or tuning consideration, such as choosing the failure threshold and timeout, or the risk of the half-open probe. Also support or remove the claim that the breaker would have opened within seconds.

*Assessor reasoning:* Circuit Breaker is appropriate and its Closed, Open and Half-Open mechanism is explained correctly. It is applied to the outage. No explicit drawback is given; the example threshold is only a weak tuning remark.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You make reasonable choices for each case and name concrete techniques, such as a Redis TTL cache and idempotency keys. Your CAP explanation needs correcting: partition tolerance cannot be given up in a distributed system, so during a partition the trade-off is consistency versus availability. For payments, idempotency keys prevent duplicate charges on retry but do not ensure consistency across a partition, so add a stronger technique such as a transactional ledger or consensus-backed store.

*Assessor reasoning:* Choices are reasonable and concrete techniques are named (Redis TTL cache, idempotency key). The CAP explanation is wrong: partition tolerance cannot be given up in a distributed system, and the choice is C versus A during a partition.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your decision record has Context, Decision and Consequences, and the context is specific to CampusEats. The consequences are one-sided, though, listing only the response-time benefit. Add at least one negative consequence, such as ordering or duplicate-delivery concerns or the operational cost of RabbitMQ. Also justify the claim that the queue smooths the lunch-hour peak rather than asserting it.

*Assessor reasoning:* Context, Decision and Consequences are present and scenario-specific. Consequences are one-sided: no negative consequence such as delivery ordering, duplicate delivery, or RabbitMQ operational cost is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings and IEEE referencing are in place, and the writing is generally clear. Question 1 appears to exceed the 150-word limit, so check Questions 2 and 5 as well. Use CAP terminology precisely, particularly in Question 5, where partition tolerance is described incorrectly.

*Assessor reasoning:* Headings and IEEE references are correct. Several answers (Q1, Q2, Q5 by estimate) appear to exceed the 150-word limit. Writing is clear but the CAP wording is imprecise.
> Question 2: "First, team size versus operational overhead."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 1: Availability response measure ('stay up most of the time') is not measurable; it needs a numeric target such as a percentage or downtime bound.
- Question 3: Part (c) computes payment availability only. End-to-end availability should multiply the other components by 0.999975, giving about 99.80% and about 1.5 h/month downtime.
- Question 3: Precision not followed: 99.9975% and 0.018 h do not match the required two decimal places for availability and one decimal place for downtime.
- Question 5: Stating that the system gives up partition tolerance misapplies CAP, since partitions cannot be avoided in a distributed system; the trade-off is consistency versus availability during a partition.
- Question 5: Idempotency keys prevent duplicate charges on retry but do not provide consistency across a partition; a stronger technique (e.g., transactional/ledger consistency, or a consensus-backed store) is needed.
- Question 6: No negative consequence is given. The claim that the queue smooths the peak is asserted, not justified.
- Question 4: Claim that the breaker 'would have opened within seconds' is unsupported; no drawback or tuning trade-off (threshold, timeout, half-open probe risk) is discussed.
- -: No explicit assumptions section; facts such as single VM, five developers and 20-minute weekly downtime are used without being stated as assumptions.
- Question 1: Answer appears to exceed the 150-word limit.

## Next steps

1. Redo Question 3(c) using the full end-to-end chain: multiply the other components by 0.999975 to get about 99.80% availability and about 1.5 hours of downtime per month, reported to the required precision.
2. Correct your CAP explanation in Question 5: partitions cannot be avoided in a distributed system, so the real choice is consistency versus availability during a partition. Pair idempotency keys with a stronger consistency mechanism for payments.
3. State your assumptions explicitly (single VM, five developers, 20-minute weekly downtime), give a numeric availability target, add a negative consequence to your decision record, and trim answers to 150 words.

---
<sub>Run Input_4-Run_2-Eff_high-261115-173850 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11564/13618 | cost $0.008022 (incl. $0.001628 for the reused reference rubric+task structure) | 63.53s</sub>
