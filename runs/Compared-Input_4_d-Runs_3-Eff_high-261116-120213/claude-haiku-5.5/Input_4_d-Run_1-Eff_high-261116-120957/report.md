# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You have built a solid, well-structured assignment with a clear architecture recommendation (Question 2 is excellent) and sensible quality attributes. The main gaps are technical: the availability calculations in Question 3 need correcting, the circuit breaker states in Question 4 are misstated, and the CAP reasoning in Question 5 needs revisiting. Tightening word counts, completing the reference list and adding a negative consequence to your ADR would also raise your marks.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Developing | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose performance and availability as the right attributes, grounded clearly in the lunch-hour load and the 4.2 s p95 latency. Your performance scenario has all six parts with a measurable response. Your availability response measure, 'stay up most of the time', is not measurable. Rewrite it as a specific, quantified target over a stated period so both scenarios are complete.

*Assessor reasoning:* Performance and availability are well justified from the lunch-hour and 4.2 s p95 scenario. The performance scenario has all six parts with a measurable response. The availability scenario's response measure ('stay up most of the time') is not measurable, so the scenarios are not fully complete.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. You made a clear case for a modular monolith and tied it to your five-developer team and the single-VM deployment problems. You also acknowledged its downside, including no independent scaling and shared process failure. Linking the weekly downtime to rolling deployments was well reasoned. Keep this level of scenario-specific justification.

*Assessor reasoning:* Clear recommendation for a modular monolith. Two scenario-specific trade-offs are given: team size of five developers and the single-VM and deployment problems. The downside (no independent scaling, shared process failure) is acknowledged.
> Question 2: "The 20-minute weekly downtime is a deployment process problem and can be removed with rolling deployments."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct at 99.30%, showing good use of the series formula. Part (b) has an arithmetic error: 0.00699 x 720 is about 5.0 hours, not 3.5. Part (c) does not include all four components; combining them in series gives about 99.80% and about 1.5 hours of monthly downtime. Keep showing your working and recheck each multiplication and rounding step.

*Assessor reasoning:* Part (a) is correct at 99.30%. Part (b) is an arithmetic error: 0.00699 × 720 is about 5.0 h, not 3.5 h. Part (c) omits the other three components, so the end-to-end availability should be about 99.80% and downtime about 1.5 h, not 99.9975% and 0.018 h.
> Question 3 (b): "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3 (c): "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You chose the Circuit Breaker, which is an appropriate pattern for this outage. However, the state descriptions are wrong: Open and Closed are swapped, and Half-Open should close again after a successful trial call rather than reopen. Correct the state behaviour, then explain how it protects the ordering flow during the outage. Adding a drawback or tuning consideration, such as threshold or timeout choice, would strengthen the answer.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern. The state explanation is wrong: Open and Closed are swapped, and Half-Open is described as reopening on success. The outage application is asserted but the explanation is incorrect, and no drawback or tuning trade-off is given.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Developing)

Your menu browsing choice is well justified, and the Redis cache with a TTL is a concrete, suitable technique. The CAP reasoning needs correction: partition tolerance is not optional in a distributed system, so the real trade-off is between consistency and availability when a partition occurs. Restate your payment choice on that basis and name a concrete technique such as idempotency keys or a transactional outbox.

*Assessor reasoning:* Menu browsing favouring availability is justified, with a concrete technique (Redis cache with TTL). The CAP usage is incorrect: partition tolerance is not optional in a distributed system, and the payment choice is misstated. No concrete technique is named for the payment case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your ADR has clear Context, Decision and Consequences sections that are specific to the tablets and the lunch peak. However, all your consequences are positive. Add at least one negative consequence, such as duplicate delivery from retries or the extra operational effort of running a message broker. This would make the record more balanced and complete.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to the tablets and lunch peak. However, all consequences are positive; no negative consequence (for example duplicate delivery from retries or added broker operations) is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings are correct and your writing is clear. Several answers, including Questions 1, 2 and 4, appear to exceed the 150-word limit, so tighten them. Reference [2] is cited in Question 4 but missing from the reference list, so add it. Your references should also state the assumptions you made, and all citations should follow IEEE style.

*Assessor reasoning:* Several answers, including Questions 1, 2 and 4, appear to exceed 150 words. Reference [2] is cited but absent from the reference list, so citations are incomplete. Headings are correct and the writing is clear.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

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

- Question 3 (b): 0.00699 × 720 equals about 5.0 hours, not 3.5 hours.
- Question 3 (c): End-to-end availability omits the other three components. Correct result is about 99.80%, with about 1.5 h monthly downtime, not 99.9975% and 0.018 h.
- Question 4: Circuit breaker states are wrong: Open and Closed are swapped, and Half-Open should close on success, not reopen.
- Question 5: CAP is misapplied: partition tolerance is not optional in a distributed system, so the payment choice is misstated.
- Question 5: No concrete consistency technique is named for placing and paying for an order (for example idempotency keys or transactional outbox).
- References: Reference [2] is cited in Question 4 but missing from the reference list; no assumptions are stated.

## Next steps

1. Recheck Question 3. In part (b), 0.00699 x 720 gives about 5.0 hours, not 3.5. In part (c), combine all four components in series; the expected result is about 99.80% availability and about 1.5 hours of monthly downtime.
2. Correct the circuit breaker states in Question 4 and explain how Half-Open decides whether to close or reopen. Then apply the pattern to the outage and add one drawback or tuning consideration, such as threshold or timeout choice.
3. Revise Question 5 so that partition tolerance is treated as a given, then name a concrete technique for payments, such as idempotency keys or a transactional outbox. Trim answers to 150 words, add a negative ADR consequence, and add the missing reference [2] with your stated assumptions.

---
<sub>Run Input_4_d-Run_1-Eff_high-261116-120957 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11373/11942 | cost $0.007165 (incl. $0.001628 for the reused reference rubric+task structure) | 47.18s</sub>
