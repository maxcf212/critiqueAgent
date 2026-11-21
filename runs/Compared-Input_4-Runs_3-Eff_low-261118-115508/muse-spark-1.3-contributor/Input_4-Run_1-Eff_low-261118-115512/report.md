# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 28 / 40 (70%)**

You wrote clear scenario-grounded answers with strong Q2 and Q4. To reach Excellent, tighten measurability in Q1, correct Q3c recombination, fix CAP reasoning in Q5, add a negative consequence in Q6, and meet word limits.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

Well done in Q1: you chose relevant attributes and gave a full six-part performance scenario with measurable p95. For Excellent, rewrite your availability response 'stay up most of the time' as measurable, e.g. % uptime per month.

*Assessor reasoning:* Performance scenario is six-part with measurable p95. Availability scenario has six parts but response measure is vague and unmeasurable, matching Proficient descriptor.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent in Q2: you clearly recommended modular monolith with scenario-specific team-size and single-VM trade-offs and acknowledged downtime risk that a bug 'can still crash the whole process'. Keep this specificity.

*Assessor reasoning:* Modular monolith clearly recommended with two scenario-specific trade-offs team size and single-VM plus deployment downtime, downside acknowledged.
> Question 2: "a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Well done in Q3: your (a) 99.30% series and (b) 5.0h downtime with working were correct. For Excellent, fix (c): you reported 99.9975% for payment alone, multiply it by other components for end-to-end ~99.80%.

*Assessor reasoning:* (a) series product 99.30% and (b) 5.0h correct with working. (c) parallel payment 0.999975 correct but failed to multiply by other components, so end-to-end and downtime wrong. One part incorrect.
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent in Q4: you correctly explained Circuit Breaker Closed/Open/Half-Open, applied it to the 25-min outage, and gave tuning of '50% of calls in 10 seconds'. Keep linking mechanism to scenario.

*Assessor reasoning:* Circuit Breaker correctly explained with Closed/Open/Half-Open, applied to 25-min outage, tuning threshold and timeout given.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds)"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Good in Q5: reasonable choices with concrete Redis TTL and idempotency key. For Excellent, fix CAP: you wrote 'give up partition tolerance' but you must retain P and choose C or A during partition.

*Assessor reasoning:* Both choices reasonable with concrete techniques Redis TTL and idempotency key, but CAP misused partitions cannot be given up, must choose C or A.
> Question 5: "we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Good in Q6: specific Context and Decision on OrderPaid RabbitMQ and positive smoothing of 'lunch peak'. For Excellent, add at least one negative consequence such as ops complexity or delay.

*Assessor reasoning:* Context and Decision specific to OrderPaid RabbitMQ, but Consequences list only positives, no negative consequence like ops complexity or consistency delay.
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (3/4, Proficient)

Clear writing with headings and IEEE references. For Excellent, bring every answer within 150 words: Q2 at ~180 words starting 'I recommend against a full microservices rewrite' exceeds the limit.

*Assessor reasoning:* Headings and IEEE references present and writing clear, but Question 2 exceeds 150-word limit at ~180 words.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  

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

- Question 3: Part (c) omits series components: correct end-to-end is ~0.99798 = 99.80% and ~1.5h downtime, not 99.9975% and 0.018h.
- Question 5: CAP error: cannot choose C+A and abandon P during partition; partition tolerance is mandatory.
- Question 1: Availability response measure 'stay up most of the time' is not measurable; needs %/time bound.
- Question 6: No negative consequence stated for queue introduction.

## Next steps

1. Make your Q1 availability response measurable with a % and time bound, e.g. uptime % per month.
2. Recalculate Q3c end-to-end as series of all components including redundant payment, then derive downtime.
3. Correct CAP to choose C or A under partition, add one negative ADR consequence, and trim Q2 under 150 words.

---
<sub>Run Input_4-Run_1-Eff_low-261118-115512 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 7926/6796 | cost $0.003015 (incl. $0.001628 for the reused reference rubric+task structure) | 49.4s</sub>
