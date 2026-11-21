# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You chose sensible architectural directions, particularly the modular monolith and the performance attribute, and your trade-offs were grounded in the CampusEats scenario. Your Question 3 calculations need checking, the circuit breaker states need correcting, and your payment reasoning under CAP needs revisiting. Strengthening your availability scenario, citations and ADR consequences will also lift your marks.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Proficient | 3 / 5 | 3 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

Your performance and availability choices are well justified from the lunch-hour scenario, and your performance scenario is complete and measurable (p95 under 1.5 s). The availability response measure, 'stay up most of the time', is not quantified. Express it as a percentage or similar measurable target and make sure all six parts are present in both scenarios.

*Assessor reasoning:* Performance and availability are sensibly chosen and justified from the lunch-hour scenario. The performance scenario is complete and measurable (p95 under 1.5 s). The availability response measure ('stay up most of the time') is not measurable, so the scenarios fall short of Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Your modular monolith recommendation is clear and tied to the scenario: a five-developer team, the single-VM bottleneck and deployment downtime. You also acknowledged the downside of shared-process failure and limited independent scaling. This is an excellent answer.

*Assessor reasoning:* Clear modular-monolith recommendation. Trade-offs are tied to the scenario: a five-developer team against eight to ten services, and the single-VM and deployment-downtime problems. The downside of independent scaling and shared-process failure is acknowledged.
> Question 2: "The slow lunchtime responses come from running on a single virtual machine"  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) of your availability calculation is correct at 99.30%. Part (b) has an arithmetic slip: 0.00699 × 720 is about 5.0 hours, not 3.5. Part (c) ignores the other components in the series, so the end-to-end figure should be about 99.30%, not 99.9975%. Show the multiplication of all components clearly.

*Assessor reasoning:* Part (a) is correct at 99.30%. Part (b) is an arithmetic error: 0.00699 × 720 is about 5.0 hours, not 3.5. Part (c) is wrong because it ignores the other components and reports 99.9975% as the end-to-end figure rather than about 99.30%. Two parts are incorrect.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (3/5, Proficient)

You chose an appropriate pattern and applied it to the outage, and you mention threshold and wait-period tuning. The state names are swapped, though: failures should open the breaker, and Open is the fail-fast state. Correct these and state one explicit drawback to reach the top band.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and is applied to the outage. However, the state names are swapped (Open and Closed), so the mechanism is partly incorrect. Tuning is mentioned (threshold, wait period) but no explicit drawback is given.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both your consistency and availability choices are reasonable, and naming a cache with TTL for browsing is a good concrete technique. The CAP reasoning for payments is incorrect because partition tolerance cannot be sacrificed in a distributed system. Choose consistency during partitions and name a payment technique such as idempotency keys or sagas.

*Assessor reasoning:* Both choices are reasonable and a cache with TTL is named for browsing. The CAP reasoning is imprecise: partition tolerance cannot be given up in a distributed system, so the payment argument is wrong. No concrete technique is named for payment (for example idempotency keys or sagas).
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your ADR has Context, Decision and Consequences, and the context is reasonably specific. The consequences list only benefits. Add at least one negative consequence, such as the operational cost of running a queue, possible duplicate delivery or ordering issues, or delayed notifications, to meet the top band.

*Assessor reasoning:* Context, Decision and Consequences are all present and reasonably specific. The Consequences section lists only positive outcomes and no negative consequence (for example queue operations cost, ordering or duplicate-delivery issues, eventual notification delay).
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your answers stay within the word limit and follow the headings in order, and the writing is clear. Reference [2] is cited in Question 4 but absent from your reference list, which contains only one entry. Add it in IEEE style and ensure every citation has a matching entry, and state your assumptions such as independent failures.

*Assessor reasoning:* Answers are within the word limit and headings are used in order. Citation has a problem: [2] is cited but absent from the reference list, which contains only one entry.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3(b): 0.00699 × 720 is about 5.03 hours, not 3.5 hours.
- Question 3(c): End-to-end availability ignores the other components. The correct value is about 0.99301 × 0.999975 ≈ 99.30%, not 99.9975%.
- Question 4: Circuit breaker states are misnamed. Failures should move the breaker to Open, not Closed, and Open should be the state that fails fast.
- Question 5: Stating that partition tolerance is given up is wrong for a distributed payment system. The payment answer should choose consistency over availability during a partition and name a technique such as idempotency keys or sagas.
- Question 1: The availability response measure ('stay up most of the time') is not quantified, for example as a percentage or a p95 error rate.
- References: Reference [2] is cited in Question 4 but missing from the reference list. No assumptions are stated, for example that failures are independent.

## Next steps

1. Recheck Question 3: calculate downtime as (1 − availability) × hours in the month, and for end-to-end availability multiply all component availabilities, including the ones you left out.
2. Revise Question 4 so failures move the circuit breaker to Open, which fails fast, and correct the Closed/Open labels; then add one drawback or tuning trade-off, such as false trips from a low threshold.
3. In Question 5, drop the claim that payments give up partition tolerance; choose consistency over availability during a partition and name a technique such as idempotency keys or sagas. Also add the reference [2] to your reference list in IEEE style.

---
<sub>Run Input_4_d-Run_3-Eff_low-261118-145353 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11401/7458 | cost $0.004925 (incl. $0.001628 for the reused reference rubric+task structure) | 26.37s</sub>
