# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You produced a solid submission with a clear modular-monolith recommendation and an accurate circuit-breaker explanation. Your strongest work is in Questions 2 and 4. The main areas to fix are the end-to-end availability in Question 3(c), the CAP reasoning in Question 5(ii), the non-measurable availability target in Question 1, and the missing negative consequences in the Question 6 record.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Your performance attribute is well justified from the lunch-peak scenario, and its six-part scenario is complete with a measurable response (p95 under 1.5 s, no dropped requests). The availability response measure, 'stay up most of the time', cannot be tested. To reach the next level, state a numeric target, such as a percentage uptime over a defined period, so both scenarios are fully measurable.

*Assessor reasoning:* Performance and availability are well justified from the lunch-peak scenario. The performance scenario is complete and measurable. The availability response measure ('stay up most of the time') is not measurable, which places this in Proficient.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Your modular-monolith recommendation is clear and tied to the scenario, particularly the five-person team and the cost of running eight or ten services. You also acknowledge the downside that modules cannot scale independently. To strengthen it further, link one trade-off more explicitly to the load profile during lunch peaks.

*Assessor reasoning:* Clear modular-monolith recommendation with scenario-specific trade-offs (five-person team, single-VM and deployment-downtime problems) and an acknowledged downside. Strong, though the trade-offs could be sharper on load profile.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct and your working is shown. In part (c), you used the payment-only availability of 99.9975% as the system figure. The end-to-end figure must combine all components in series, giving about 99.80% and about 1.5 h/month. Also give the downtime to one decimal place rather than 0.018 hours.

*Assessor reasoning:* (a) 99.30% and (b) 5.0 h are correct. Part (c) is wrong: it gives payment-only availability 99.9975% as end-to-end, ignoring the other components. Correct end-to-end is about 99.80% and about 1.5 h/month. Downtime is also not given to one decimal place.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You name the circuit breaker pattern and explain its Closed, Open and Half-Open states correctly, with threshold and wait-period tuning. You apply it clearly to the slow-provider outage and mention tuning considerations. The claim that the breaker would have opened within seconds during last month's outage needs supporting data or stated assumptions.

*Assessor reasoning:* Circuit breaker is correctly explained with states and threshold tuning, and applied to the slow-provider outage. Tuning considerations are present. The claim about 'the outage last month' is asserted without supporting detail.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Your choices are reasonable, and you name suitable techniques: caching with a TTL for the menu and idempotency keys for payments. The CAP explanation is imprecise, however. Partition tolerance cannot be given up in a distributed system, so reframe the choice as consistency versus availability during a partition.

*Assessor reasoning:* Both choices are reasonable and techniques are named (cache with TTL, idempotency keys). However, the CAP application is imprecise: partition tolerance cannot be given up in a distributed network, so the CAP explanation is incorrect.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Context, Decision and Consequences sections are all present and reasonably specific to CampusEats. The consequences, however, list only benefits. Add a negative consequence such as added broker operations, delivery ordering issues, or duplicate notifications, and explain how you would manage it.

*Assessor reasoning:* Context, Decision and Consequences are present and fairly specific. Consequences are entirely positive, with no negative consequence (e.g., added infrastructure, duplicate or ordering issues, queue failure risk), so it falls to the upper-middle of Proficient.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (4/4, Proficient)

Your answers stay within the word limits, the required headings are used in order, and your IEEE-style references are cited in the text. Tighten the precision of your CAP wording and the downtime figures in Question 3 to match the terminology the course expects.

*Assessor reasoning:* Headings are used in order, answers are within limits, and IEEE-style references are provided and cited in text. Minor precision issues exist, such as the CAP wording and downtime precision in Q3.
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 3 (c): End-to-end availability should combine the other components with the 99.9975% payment availability, giving about 99.80% and about 1.5 h/month. The answer reports payment-only availability as the system figure.
- Question 3 (c): Monthly downtime given as 0.018 hours rather than to one decimal place as required.
- Question 5 (ii): CAP is misapplied: partition tolerance is not optional in a distributed system, so the choice is between consistency and availability during a partition.
- Question 1: Availability response measure 'stay up most of the time' is not measurable.
- Question 6: Consequences list only benefits; no negative consequence such as added broker operations, delivery ordering, or duplicate notifications.
- Question 4: Claims the breaker would have opened within seconds during last month's outage without supporting data or stated assumptions.

## Next steps

1. In Question 3(c), combine the payment availability with the other components in series, then restate the monthly downtime to one decimal place.
2. In Question 5(ii), correct the CAP reasoning: partition tolerance must be assumed in a distributed system, so the real choice during a partition is between consistency and availability.
3. Add at least one negative consequence to your Question 6 ADR (for example, extra broker operations, message ordering, or duplicate notifications), and replace the unmeasurable availability target in Question 1 with a numeric measure.

---
<sub>Run Input_4-Run_3-Eff_low-261118-120241 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11556/7808 | cost $0.005115 (incl. $0.001628 for the reused reference rubric+task structure) | 37.04s</sub>
