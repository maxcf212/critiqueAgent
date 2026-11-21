# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 22 / 40 (55%)**

You have a sound structure and a well-justified modular monolith recommendation, and you draw on scenario details throughout. The main gaps are in the calculations, where Question 3(b) and (c) contain errors. Your circuit breaker and CAP explanations also need correcting, and your decision record lacks a negative consequence. Stating assumptions, completing citations and respecting word limits will strengthen the submission.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Developing | 4 / 8 | 4 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You chose performance and availability and tied them to the lunchtime peak and the 4.2 s p95 figure, giving clear scenario-based justification. The performance scenario has all six parts and a measurable response measure. To reach Excellent, make the availability response measure measurable, for example as a percentage uptime over a stated period.

*Assessor reasoning:* Performance and availability are chosen with scenario-based justification (lunch peak, 4.2 s p95). The performance scenario has all six parts and a measurable response measure. The availability scenario's response measure ('stay up most of the time') is not measurable, and its response is vague, so the scenarios are not fully compliant.
> Question 1: "the system should stay up most of the time"  
> Question 1: "The two most important quality attributes are performance and availability"  

### C2 Q2 Architectural style (5/6, Excellent)

Your modular monolith recommendation is clear and grounded in CampusEats specifics: a five-developer team, the single-VM lunchtime slowdown and deployment downtime. You also acknowledge the downside that modules cannot scale independently. To reach the top band, develop the second trade-off into a fuller analysis that weighs its cost against a specific alternative.

*Assessor reasoning:* Clear recommendation for a modular monolith. Trade-offs are tied to CampusEats specifics: five-developer team size and the single-VM lunchtime slowdown and deployment downtime. The downside is acknowledged. The second trade-off is somewhat argumentative rather than a full trade-off analysis, so the mark is not the top of the band.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (4/8, Developing)

Part (a) is correct at 99.30% with working shown, which is a good foundation. Part (b) contains an arithmetic slip: 0.00699 × 720 is about 5.0 hours, not 3.5 hours. Part (c) does not account for the other three serial components; end-to-end availability should be about 99.80%, or about 1.5 hours per month.

*Assessor reasoning:* Part (a) is correct (99.30%) with working shown. Part (b) is an arithmetic error: 0.00699 × 720 is about 5.0 h, not 3.5 h. Part (c) ignores the other three components, so the end-to-end availability (about 99.80%, about 1.5 h/month) is wrong. Two parts are incorrect, placing it in Developing.
> Question 3: "0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You named Circuit Breaker, an appropriate pattern, and applied it to the outage. However, the state mechanism is inverted: Closed should pass calls through, Open should fail fast, and a successful Half-Open trial should close the breaker, not reopen it. Correct these and build on the tuning parameters you mention by explaining the trade-off they involve.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and is applied to the outage. However, the state mechanism is wrong: Closed should pass calls through and Open should fail fast, and Half-Open success should close the breaker, not reopen it. Tuning parameters are mentioned, but the explanation is incorrect and no clear drawback is given.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "If they succeed it opens again, otherwise it stays closed."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable and justified, and menu browsing uses a concrete technique, a Redis cache with a 60-second TTL. The CAP explanation needs correcting: partition tolerance is not optional in a distributed system, and during a partition you trade consistency against availability. For payments, name a concrete technique such as idempotency keys or strongly consistent transactions.

*Assessor reasoning:* Choices are reasonable and justified. Menu browsing uses a named concrete technique (Redis cache with TTL). The CAP explanation is wrong: partition tolerance cannot be dropped in a distributed system, and the trade-off is between C and A during a partition. No concrete consistency technique is named for payments, so one technique is missing.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your record includes Context, Decision and Consequences, and the context is specific, citing the 4.2 s p95 and offline tablets. The decision is clear. However, the consequences list only benefits. Add at least one negative consequence, such as added complexity, eventual delivery of orders, or message broker operations, to reach the top band.

*Assessor reasoning:* Context, Decision and Consequences are all present, and the context is specific (4.2 s p95, offline tablets). The Decision is clear. The Consequences section lists only positive outcomes; no negative consequence (added complexity, eventual delivery, broker operations) is stated, so it is one-sided.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings are correct and a reference list is present. Reference [2] is cited in Question 4 but missing from the list, so add it. Several answers appear to exceed the 150-word limit, and no assumptions are stated. Trim answers, add a short assumptions statement, and apply IEEE citation style consistently.

*Assessor reasoning:* Headings are correct and the reference list is present. However, [2] is cited but absent from the reference list. Several answers, including Questions 1 and 2, appear to exceed 150 words. Assumptions are not stated anywhere, and this affects the writing standard.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 1: "The scenarios below use the six-part form from [1]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | no | - |

## Technical issues

- Question 3(b): Arithmetic error: 0.00699 × 720 ≈ 5.0 hours, not 3.5 hours.
- Question 3(c): Ignores the other three serial components; end-to-end availability should be about 99.80% (≈1.5 h/month), not 99.9975%.
- Question 4: Circuit breaker states are described incorrectly: Closed passes calls through and Open fails fast; Half-Open success should close the breaker.
- Question 5: CAP theorem misstated: partition tolerance is not optional in distributed systems; the trade-off is C versus A during a partition.
- Question 5: No concrete consistency technique named for payments (e.g., idempotency keys, strongly consistent DB transactions).
- Question 6: Consequences are one-sided; no negative consequence is stated.
- Question 1: Availability response measure is not measurable.
- References: [2] is cited in Question 4 but missing from the reference list.
- Overall: No assumptions stated, and several answers appear to exceed the 150-word limit.

## Next steps

1. Recheck Question 3: multiply the component availabilities across the serial chain for part (c), and redo part (b) using 720 hours per month, showing each step.
2. Correct the circuit breaker state descriptions and the CAP explanation, and name a concrete payments technique such as idempotency keys or strongly consistent database transactions.
3. Make the availability response measure measurable, add a negative consequence to your decision record, state your assumptions, add the missing reference [2], and keep each answer within 150 words.

---
<sub>Run Input_4_d-Run_2-Eff_high-261116-121044 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11714/12101 | cost $0.007277 (incl. $0.001628 for the reused reference rubric+task structure) | 45.91s</sub>
