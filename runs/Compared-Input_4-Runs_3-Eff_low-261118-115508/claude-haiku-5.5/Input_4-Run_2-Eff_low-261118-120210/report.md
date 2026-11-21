# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You chose strong quality attributes and made a well-argued recommendation against a full microservices rewrite, with trade-offs grounded in your team size and the lunchtime load. Your Circuit Breaker answer explains the states clearly and applies them to the outage. The main gaps are in Q3(c), where payment availability was not combined with the other components, the CAP reasoning in Q5(ii), the unquantified availability measure in Q1, and the one-sided ADR in Q6. Several answers also appear to exceed the 150-word limit.

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

Your choice of performance and availability is well justified by the lunch-hour dependency, and the performance scenario is fully measurable. The availability scenario has all six parts, but its response measure says the system should stay up 'most of the time', which is not quantified. Give a specific uptime target and measurement period to reach the next level.

*Assessor reasoning:* Attributes are well justified from the scenario and the performance scenario is fully measurable. The availability scenario has all six parts but its response measure ('stay up most of the time') is not measurable, which places it at Proficient.
> Question 1: "The two most important quality attributes are performance and availability, because the business depends on the lunch hour"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

This is a strong answer. You make a clear recommendation and tie your trade-offs to the scenario, including the five-person team, the single-VM lunchtime slowdown and the weekly downtime. You also acknowledge the downside of the recommendation, which is that modules cannot scale independently and a bug can still crash the process.

*Assessor reasoning:* Clear recommendation with scenario-specific trade-offs: five-developer team size, single-VM lunchtime slowness and 20-minute weekly downtime. The downside is explicitly acknowledged.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct and the working is shown. Part (c) is incorrect because the payment availability was not combined with the other three components. The end-to-end figure should be about 99.80%, with roughly 1.5 hours of downtime per month, not the payment-only 0.018 hours. Recheck the series calculation across all components.

*Assessor reasoning:* Parts (a) and (b) are correct with working. Part (c) is wrong: the payment availability of 99.9975% was not combined with the other three components, so the end-to-end figure should be about 99.80% and downtime about 1.5 h, not 0.018 h. Exactly one part is incorrect.
> Question 3 (a): "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3 (c): "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You name the Circuit Breaker pattern and explain its states correctly, and you apply it to the slow-provider outage. To reach the top level, add an explicit drawback or tuning consideration, such as how the threshold and wait period should be set and what happens to users while the breaker is open.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern, correctly explained with its states and applied to the slow-provider outage. Threshold and wait-period tuning is mentioned only in passing and no explicit drawback is discussed, so it falls short of Excellent.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable, and you name concrete techniques (TTL cache and idempotency keys). The CAP explanation is imprecise, however. It gives up partition tolerance, which is not optional in a distributed system, and it contradicts the stated choice of consistency over availability. Restate the trade-off accurately for each case.

*Assessor reasoning:* Choices are reasonable and concrete techniques (TTL cache, idempotency keys) are named. The CAP explanation is imprecise: it contradicts the stated choice of consistency over availability and treats partition tolerance as optional in a distributed system.
> Question 5 (ii): "we choose consistency and availability and give up partition tolerance"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Context, Decision and Consequences are all present and specific to the scenario. The Consequences section lists only positive outcomes. Add at least one negative consequence, such as added operational complexity, or message-ordering and duplicate-delivery handling, to reach the top level.

*Assessor reasoning:* Context, Decision and Consequences are all present and scenario-specific. The Consequences section lists only positive outcomes and omits any negative consequence, such as added infrastructure or queue ordering and delivery complexity.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings are used and IEEE citations [1] and [2] are present. However, several answers, including Q1 and Q2, appear to exceed the 150-word limit. Reduce the length of these answers and check the word count of each, and make sure the references list is complete and cited consistently.

*Assessor reasoning:* Question 1 and Question 2 both appear to exceed the 150-word limit. Headings and IEEE citations [1] and [2] are correct, but several answers exceed the limit.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 (c) |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3 (c): Payment availability was not combined with the other components. End-to-end availability should be about 99.80% and downtime about 1.5 h per month, not 99.9975% and 0.018 h.
- Question 3 (c): Downtime of 0.018 h is inconsistent with the end-to-end calculation; 0.000025 × 720 is the payment-only downtime.
- Question 5 (ii): CAP is misapplied: partition tolerance is not optional in a distributed system, and the text says consistency and availability are chosen while giving up partition tolerance.
- Question 1: The availability response measure 'stay up most of the time' is not quantified, so it is not measurable.
- Question 6: The ADR gives no negative consequence, such as added operational complexity or message-ordering and duplicate-delivery handling.
- Question 1: Stated word counts appear to exceed 150 words.
- Overall: No explicit assumptions section is provided, as required by R7.

## Next steps

1. Recalculate Q3(c) by combining all four components in series, so the end-to-end availability and monthly downtime reflect the whole ordering path, and show the working.
2. Rewrite Q5(ii) so that partition tolerance is treated as a given in a distributed system, and the trade-off is between consistency and availability during a partition. Quantify the Q1 availability response measure (for example, a percentage uptime target over a stated period) and add a negative consequence to the Q6 ADR. Add an explicit assumptions section.
3. Trim Q1 and Q2 to 150 words or fewer, and check every other answer against the limit before submitting.

---
<sub>Run Input_4-Run_2-Eff_low-261118-120210 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11672/7641 | cost $0.005044 (incl. $0.001628 for the reused reference rubric+task structure) | 30.65s</sub>
