# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 26 / 40 (65%)**

You show strong understanding in several areas. Your modular-monolith recommendation in Question 2, your circuit-breaker reasoning in Question 4 and your decision record in Question 6 are all well developed. The main losses are in Question 3(c), where end-to-end availability must include all four components, the CAP argument in Question 5, the non-measurable availability measure, and the missing assumptions section and word-limit control.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose performance and availability and tied them clearly to the scenario, citing the lunch peak of 900 orders between 12:00 and 13:00 and the 4.2 s p95 latency. Both scenarios have all six parts. To reach Excellent, make the availability response measure measurable, for example with a stated percentage target over a defined period. Also trim the scenario text to fit the word limit.

*Assessor reasoning:* Performance and availability are chosen and tied to the scenario (lunch peak, 4.2 s p95). Both scenarios have all six parts, but the availability response measure ('stay up most of the time') is not measurable. Limited scenario words also push the section over the limit.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "because the business depends on the lunch hour: 900 orders arrive between 12:00 and 13:00"  

### C2 Q2 Architectural style (5/6, Excellent)

Your recommendation of a modular monolith is clear and well reasoned. You linked it to the five-person team, noting that eight or ten services would take more time on infrastructure than on features, and to the single-VM cause of slow lunchtime responses. You also acknowledged the downside of no independent scaling and a shared crash domain. Shorten the answer to 150 words to meet the format requirement.

*Assessor reasoning:* Clear modular-monolith recommendation with trade-offs tied to the five-person team and the single-VM and deployment problems. The downside (no independent scaling, shared crash domain) is acknowledged. The answer exceeds 150 words, which is a format matter under C7 rather than here.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The slow lunchtime responses come from running on a single virtual machine"  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) at 99.30% and (b) at 5.0 hours per month are correct, and your working is clear. In part (c), your end-to-end figure reflects payment alone and ignores the other three components in series. Recalculate using all four components; the end-to-end result should be about 99.80% and 1.5 hours per month. Also apply the precision rules: two decimal places for percentages and one for hours.

*Assessor reasoning:* Parts (a) 99.30% and (b) 5.0 h are correct with working. Part (c) reports payment availability (99.9975%) as end-to-end, ignoring the other three components. Correct end-to-end is about 99.80% and 1.5 h/month. Precision breaks the two-decimal and one-decimal rules.
> Question 3: "So the new availability of placing an order is 99.9975%"  
> Question 3: "which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

Circuit breaker is a suitable pattern, and you explained its states correctly. You applied it to the provider slowdown, showing how it would stop calls to the slow dependency. To reach Excellent, add a drawback or tuning consideration, such as how the failure threshold and time window (for example 50% of calls in 10 seconds) could cause false trips or slow recovery. Also support your claim that the breaker opens 'within seconds'.

*Assessor reasoning:* Circuit breaker is an appropriate pattern and its states are explained correctly. It is applied to the outage with a plausible outcome. No drawback is stated, and the threshold example is not discussed as a tuning trade-off. The 'within seconds' claim is unsupported.
> Question 4: "the breaker would have opened within seconds of the provider slowing down."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds)"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable. Caching with a TTL and idempotency keys for payments are appropriate, concrete techniques. However, the CAP argument needs correcting. Partition tolerance cannot be given up in a distributed system, so during a partition you must choose between consistency and availability. Restate your payment choice in those terms and justify it clearly.

*Assessor reasoning:* Choices are reasonable and techniques are named (TTL caching, idempotency keys). The CAP theorem is misstated: partition tolerance is not optional in a distributed system, and 'consistency and availability' contradicts choosing consistency during a partition.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "Redis with a 60-second TTL"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your decision record has clear Context, Decision and Consequences sections that are specific to the tablet dependency and the p95 latency problem. However, the consequences list only benefits. Add at least one negative consequence, such as delayed or duplicate notifications, ordering issues, or the added operational complexity of a queue, and state the trade-off you accept.

*Assessor reasoning:* Context, Decision and Consequences are present and specific to the tablet and p95 problems. Consequences are one-sided, with no negative consequence (e.g., added operational complexity, duplicate notifications, ordering). Status 'Proposed' is a minor addition.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  

### C7 Communication and format (2/4, Developing)

Your headings are clear and your IEEE-style references are present, which is good. Question 2 and probably Question 1 exceed the 150-word limit, so tighten both. Question 3(c) does not follow the precision rules. The brief requires an assumptions section, which is missing; add a short list of assumptions, such as the component availability figures you used, so that your calculations can be evaluated.

*Assessor reasoning:* Headings and IEEE-style citations are present. Question 2 is clearly over 150 words and Question 1 appears to exceed the limit. Precision formatting is wrong in Question 3(c). No assumptions section is provided.
> Question 2: "Instead the existing application should be restructured into a modular monolith with clear internal modules"  
> References: "[2] M. T. Nygard, Release It! Design and Deploy Production-Ready Software, 2nd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 1: Availability response measure ('stay up most of the time') is not measurable.
- Question 3(c): End-to-end availability ignores the other three components; correct value is about 99.80% and 1.5 h/month, not 99.9975%.
- Question 3(c): Precision violates the rules: 99.9975% has four decimals and 0.018 h is not given to one decimal place.
- Question 5: CAP misstated: partition tolerance is not optional; the 'choose consistency and availability' statement contradicts choosing consistency during a partition.
- Question 4: No drawback or tuning trade-off is discussed; the 'within seconds' outcome is asserted without support.
- Question 6: Consequences list only positives; no negative consequence such as duplicate delivery or added operational complexity.
- Overall: No assumptions section is provided, despite the requirement to state assumptions.

## Next steps

1. Recalculate Question 3(c) using all four components in series, not payment alone. Present percentages to two decimal places and hours to one decimal place, as the question requires.
2. Make the availability response measure in Question 1 numeric, for example a target percentage over a stated period. Add a short assumptions section, and trim Questions 1 and 2 to within 150 words each.
3. Correct your CAP reasoning: partition tolerance must be assumed in a distributed system, so the real choice during a partition is consistency or availability. Add a negative consequence to your ADR and a drawback or tuning consideration to your circuit-breaker answer.

---
<sub>Run Input_4-Run_1-Eff_high-261115-173734 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 16865/18827 | cost $0.011156 (incl. $0.001628 for the reused reference rubric+task structure) | 75.74s</sub>
