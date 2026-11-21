# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You have a solid structure and a sensible modular monolith recommendation in Question 2, which is your strongest answer. The main gaps are the accuracy of Question 3(c), the CAP explanation in Question 5, and the measurability of the availability measure in Question 1. Tightening these and bringing several answers within 150 words would raise your mark considerably.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Performance and availability are sensibly chosen and justified from the lunch-hour load in the scenario. The performance scenario has all six parts and a measurable p95 target. The availability response measure, 'stay up most of the time', is not measurable, so state a numeric target and its time window to reach the top band.

*Assessor reasoning:* Performance and availability are chosen and justified from the scenario. The performance scenario has all six parts with a measurable p95 target. The availability scenario's response measure ('stay up most of the time') is not measurable, so this level applies.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "the business depends on the lunch hour: 900 orders arrive between 12:00 and 13:00"  

### C2 Q2 Architectural style (5/6, Excellent)

Your modular monolith recommendation is clear and well grounded. Team size against operational overhead and the single-VM and deployment-downtime problems are scenario-specific trade-offs, and you acknowledge the downside of losing independent scaling. Keep this level of specificity while trimming the answer to 150 words.

*Assessor reasoning:* The modular monolith recommendation is clear. Two scenario-specific trade-offs are given: team size versus operational overhead, and the single-VM and deployment-downtime problems. The downside (no independent scaling, shared process failure) is acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) at 99.30% and (b) at 5.0 hours are correct and well worked. Part (c) reports payment-only availability as end-to-end; the correct end-to-end figure is about 99.80% with about 1.5 hours monthly downtime. Also round results to the required precision (two decimals for percentages, one for hours).

*Assessor reasoning:* Parts (a) 99.30% and (b) 5.0 h are correct with working. Part (c) is wrong: it reports payment-only availability as end-to-end. The correct end-to-end value is about 99.80% and about 1.5 h/month. Results also break the two-decimal and one-decimal precision rules.
> Question 3: "So the new availability of placing an order is 99.9975%"  
> Question 3: "which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

Circuit Breaker is an appropriate pattern and its states are explained correctly, with a clear link to the provider outage. Add at least one drawback or tuning consideration, such as threshold choice or false trips. Remove the unsupported claim that it would have opened within seconds, or justify it with the timing data.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and its states are explained correctly. It is applied to the outage. No drawback is given. The threshold mention is an example, not a tuning trade-off. The claim that it would have opened within seconds is unsupported.
> Question 4: "the breaker would have opened within seconds of the provider slowing down"  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds)"  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both choices are reasonable, and you name concrete techniques: a Redis TTL cache for the menu and idempotency keys for payments. The CAP explanation needs correcting, since partitions cannot be avoided, so the trade-off is consistency versus availability during a partition. Make this precise.

*Assessor reasoning:* Both choices are reasonable and each has a concrete technique (Redis TTL cache, idempotency keys). The CAP explanation is wrong: partition tolerance cannot be given up in a distributed system, and the choice is between consistency and availability during a partition.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "for example Redis with a 60-second TTL"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Context, Decision and Consequences are all present and specific to the outlet tablet problem. The consequences currently list only benefits. Add at least one negative consequence, such as duplicate deliveries, message ordering issues, or the operational load of running RabbitMQ.

*Assessor reasoning:* Context, Decision and Consequences are present and specific to the scenario. The consequences list only positive effects, with no negative consequence such as duplicate delivery, ordering issues or added queue operations.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings and IEEE citations [1] and [2] with a reference list are correct. Several answers, including Questions 2, 4 and 5, exceed 150 words, so tighten them. Also add the required assumptions section, which is currently missing.

*Assessor reasoning:* Several answers exceed 150 words, including Questions 2, 4 and 5. Headings are correct and IEEE references [1] and [2] are cited with a reference list. No assumptions section is given, although the task requires one.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 3: Part (c) reports payment-only availability (99.9975%) as end-to-end availability. End-to-end is about 99.80% (0.99797630), with about 1.5 h monthly downtime, not 0.018 h.
- Question 3: Results 99.9975% and 0.018 hours break the required precision of two decimals for percentages and one decimal for hours.
- Question 5: States that payments give up partition tolerance. Partitions cannot be avoided in a distributed system, so the choice is consistency or availability during a partition.
- Question 1: Availability response measure ('stay up most of the time') is not measurable.
- Question 6: Consequences omit negative effects such as duplicate deliveries, message ordering and extra operational load of RabbitMQ.
- Question 4: Claims the breaker would have opened within seconds during the outage without supporting data.

## Next steps

1. Recalculate Question 3(c) using end-to-end availability (about 99.80% and about 1.5 hours monthly downtime), and report percentages to two decimals and hours to one decimal.
2. Rewrite the Question 1 availability response measure as a numeric target (for example, a percentage of uptime over a stated period), and revise the Question 5 CAP explanation so that partition tolerance is treated as unavoidable, with the real choice being consistency or availability during a partition.
3. Trim Questions 2, 4 and 5 to 150 words or fewer, add a negative consequence to the Question 6 ADR (such as duplicate deliveries, ordering or RabbitMQ operational load), and add a stated assumptions section.

---
<sub>Run Input_4-Run_1-Eff_low-261118-120131 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11647/8271 | cost $0.005356 (incl. $0.001628 for the reused reference rubric+task structure) | 39.52s</sub>
