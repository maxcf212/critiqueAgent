# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 31 / 40 (77.5%)**

You submitted strong, scenario-grounded answers (31/40). Q2 and Q4 are excellent; Q1, Q3, Q5, Q6 and communication are proficient. Main losses: Q3(c) never recomputes end-to-end availability, Q5 misstates CAP, Q6 lacks a negative consequence, Q2 exceeds the word limit, and Q1's availability measure is unmeasurable. Address these to move up.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose performance and availability well, grounded in 900 orders and 4.2 s p95. The performance scenario is complete and measurable. The availability scenario has all six parts, but 'stay up most of the time' is not measurable and the response drifts from the order-placement artefact. For Excellent, make both response measures measurable and align the availability response with the order service.

*Assessor reasoning:* Both attributes are well chosen and justified from the scenario data (900 orders, 4.2 s p95). The performance scenario has all six parts and a measurable measure. The availability scenario has all six parts but its response measure ('stay up most of the time') is not measurable, and the response drifts from the order-placement artefact.
> Question 1: "The two most important quality attributes are performance and availability, because the business depends on the lunch hour"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Strong modular monolith recommendation with scenario-specific trade-offs: five developers versus infrastructure overhead, and known problems stemming from the single VM and deployment process rather than the monolith shape. You explicitly acknowledge the downside (no independent scaling, one module can crash the process). This meets Excellent; keep tying trade-offs to scenario evidence.

*Assessor reasoning:* A clear, argued recommendation (modular monolith) with two scenario-specific trade-offs: team size versus operational overhead, and the observation that the known problems stem from a single VM and the deployment process rather than the monolith shape. A specific downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) 99.30% and (b) 5.0 hours are correct with working shown. In (c) you correctly combine payment to 0.999975 but never recombine it with the other three components. End-to-end availability should be 99.80% with about 1.5 hours monthly downtime, not 99.9975% and 0.018 hours. For Excellent, recompute the full series and carry rounding to two decimals.

*Assessor reasoning:* (a) 0.99301 = 99.30% and (b) 5.0 hours are correct with working shown. In (c) the payment combination 0.999975 is right, but it is never recombined with the other three components: the end-to-end availability should be 99.80% and downtime about 1.5 hours, not 99.9975% and 0.018 hours.
> Question 3(c): "the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Circuit breaker is named and its Closed/Open/Half-Open mechanism, including failure counting and timeouts, is explained correctly. You apply it concretely to the 25-minute outage with a user-visible fallback and give a tuning consideration (failure threshold and window). This meets Excellent; keep the concrete outage application.

*Assessor reasoning:* Circuit breaker is named and its Closed/Open/Half-Open mechanism, including failure counting and timeouts, is explained correctly. It is applied concretely to the 25-minute outage with a user-visible fallback, and a tuning consideration (failure threshold and window) is provided.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging for 25 minutes."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both choices are sensible and justified, with concrete techniques (Redis cache with 60-second TTL; idempotency keys). However, your CAP explanation is wrong: a partition-tolerant system cannot give up partition tolerance and keep both C and A; during a partition it must sacrifice one. For Excellent, correct the CAP framing and tie each choice to partition behaviour.

*Assessor reasoning:* Both choices are sensible and justified, with concrete techniques (Redis cache with TTL; idempotency keys). However, the CAP explanation is wrong: a partition-tolerant distributed system cannot 'give up' partition tolerance and keep both C and A; it must sacrifice one during a partition.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are all present and specific (offline tablet, synchronous call, 4.2 s p95, RabbitMQ, retrying worker). The consequences are entirely positive, so the record is one-sided. For Excellent, add at least one negative consequence, such as duplicate notifications, eventual consistency for outlets, or queue operations burden.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific (offline tablet, synchronous call, 4.2 s p95, RabbitMQ, retrying worker). Consequences are entirely positive; no negative consequence such as duplicate notifications, eventual consistency for outlets, or queue operations burden is stated.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Writing is clear and precise, with headings and IEEE-style references and a reference list. Q1, Q4, Q5 and Q6 appear within 150 words. Q2 is roughly 195 words and exceeds the limit. For Excellent, bring every answer within 150 words and keep citations precise.

*Assessor reasoning:* Writing is clear and precise, headings and IEEE-style references with a reference list are present; Q1 (~145), Q4, Q5 and Q6 appear within 150 words. Q2 is roughly 195 words, exceeding the limit.
> Question 2: "The 20-minute weekly downtime is a deployment process problem and can be removed with rolling deployments."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3(c) |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 3(c): End-to-end availability after adding the second provider is not recomputed: 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798 (99.80%), so monthly downtime is ~1.5 hours, not 0.018 hours. The 99.9975% figure is only the payment component.
- Question 3: (a) reports 99.30% (99.301%) and (b) 5.0 hours, both acceptable, but the 0.02% rounding is not carried through to the two-decimal requirement in (c).
- Question 1: Availability response measure 'stay up most of the time' is not measurable, and the response (browse menus) does not match the order-service artefact.
- Question 5: CAP misuse: partition tolerance cannot be traded away in a network partition; the choice is between consistency and availability during the partition.
- Question 6: No negative consequence recorded in the ADR, so the record is one-sided.
- Question 2: Answer is approximately 195 words, over the 150-word limit.

## Next steps

1. Recompute Q3(c) end-to-end: multiply 0.9995 × 0.999 × 0.9995 × 0.999975, show the working, and report 99.80% with about 1.5 hours monthly downtime to two decimals.
2. Correct Q5's CAP framing: partition tolerance cannot be given up; during a partition choose consistency or availability, then tie your Redis TTL and idempotency-key techniques to that choice.
3. Tighten Q1 and Q6: make the availability response measure measurable and tied to order placement, add a negative ADR consequence, and cut Q2 to 150 words.

---
<sub>Run Input_4-Run_1-Eff_high-261115-173037 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8512/10200 | cost $0.006758 (incl. $0.001628 for the reused reference rubric+task structure) | 47.56s</sub>
