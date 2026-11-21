# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You showed strong scenario-specific reasoning in Q1 and an excellent, well-justified recommendation in Q2. However, Q3 contains an arithmetic slip in (b) and a conceptual error in (c), Q4 reverses the circuit breaker states, Q5 misapplies CAP and omits a payment technique, and your ADR lacks a negative consequence. Total: 24/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Your performance scenario is excellent: all six parts with a measurable response measure (p95 under 1.5 s). To reach Excellent, make the availability scenario's response measure measurable too — 'stay up most of the time' should be quantified, e.g. 'no more than 5 minutes downtime per month'.

*Assessor reasoning:* Performance and availability are well justified from the lunch-hour scenario. The performance scenario has all six parts with a measurable response measure, but the availability scenario's response measure ('stay up most of the time') is not measurable.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. Your recommendation of a modular monolith is justified by two scenario-specific trade-offs (five-developer team overhead; root causes being the single VM and deployment process) and you explicitly acknowledge the downside. Nothing more needed here.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team overhead; root causes are single VM and deployment process, not the monolith). The downside of the recommendation is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct with working shown. Part (b) has an arithmetic slip: 0.00699 × 720 = 5.0 hours, not 3.5. Part (c) is conceptually wrong: you quoted the payment-pair availability (99.9975%) instead of recomputing end-to-end availability (0.99800125 × 0.999975 ≈ 99.80%, ≈1.5 h downtime). Correcting both parts would lift you to Excellent.

*Assessor reasoning:* (a) is correct (0.99301 → 99.30%). (b) is an arithmetic slip: 0.00699 × 720 = 5.0 h, not 3.5 h. (c) is conceptually wrong: the student reports the payment-pair availability (99.9975%) rather than the end-to-end availability (0.99800125 × 0.999975 ≈ 99.80%, ≈1.5 h downtime). Two parts incorrect, so Developing despite correct method and shown working.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit Breaker is an appropriate pattern and you applied it to the outage with a tuning threshold, but the states are reversed: Open should fail fast, Closed is normal operation, and successful Half-Open trials transition to Closed. Correct the mechanism and keep your threshold discussion to reach Excellent.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and is applied to the outage with a tuning threshold, but the mechanism is explained incorrectly: the Open/Closed (and Half-Open transition) behaviours are reversed. Open must fail fast; Closed is normal; a successful Half-Open trial closes the breaker.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed and calls fail immediately"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both choices are reasonable and you named a concrete technique for browsing (Redis with 60-second TTL). However, CAP is misapplied: partition tolerance is mandatory in distributed systems — during a partition you sacrifice consistency or availability, not P. Also name a concrete technique for the payment case (e.g., synchronous write with quorum) to reach Excellent.

*Assessor reasoning:* Both choices (availability for browsing, consistency for payment) are reasonable and a concrete technique is named for menu browsing (Redis cache with TTL). However, CAP is misused: partition tolerance cannot be sacrificed; during a partition one gives up C or A. No concrete technique is named for the payment case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "for example Redis with a 60-second TTL"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Context, Decision and Consequences are all present and specific to CampusEats, with several positive consequences. To reach Excellent, add at least one negative consequence, such as delayed order notification, duplicate delivery risk, or the operational burden of running the queue.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (offline tablets, 4.2 s p95). Several positive consequences are given, but no negative consequence (e.g., eventual notification delay, duplicate delivery, queue operational burden) is stated, so the consequences are one-sided.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear and headings are used correctly, but Q2 exceeds the 150-word limit (~185 words) and source [2] is cited in Q4 yet missing from your reference list. Trim Q2 and complete the reference list to reach Excellent.

*Assessor reasoning:* Writing is clear and headings are used correctly, but Question 2 exceeds 150 words (~185), and [2] is cited in Question 4 yet missing from the reference list. No explicit assumptions are stated anywhere.
> Question 2: "A rewrite would freeze feature work for months without directly fixing either problem."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3 (b): Arithmetic error: 0.00699 × 720 = 5.0 hours, not 3.5 hours.
- Question 3 (c): End-to-end availability was not recomputed: should be 0.99800125 × 0.999975 ≈ 99.80% with ≈1.5 h downtime; the quoted 99.9975% is only the payment subsystem.
- Question 4: Circuit breaker states are reversed: Open should fail fast, Closed is normal operation, and successful Half-Open trials transition to Closed.
- Question 5: CAP theorem misapplied: partition tolerance is mandatory in distributed systems; one sacrifices consistency or availability during a partition, not P. No concrete technique named for payments.
- Question 6: No negative consequence included in the ADR.
- References: Source [2] is cited in Question 4 but absent from the reference list; no assumptions stated.

## Next steps

1. Redo Q3(b): 0.00699 × 720 = 5.0 hours, and recompute (c) end-to-end as 0.99800125 × 0.999975 ≈ 99.80% (≈1.5 h downtime), not the payment subsystem alone.
2. Rewrite your circuit breaker explanation: Open fails fast, Closed is normal operation, and successful Half-Open trials transition back to Closed.
3. Fix your CAP statement (P is mandatory; you trade C or A during a partition), name a concrete technique for payments, and add a negative consequence to your ADR.

---
<sub>Run Input_4_d-Run_2-Eff_high-261116-121402 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8353/6842 | cost $0.003247 (incl. $0.001628 for the reused reference rubric+task structure) | 57.98s</sub>
