# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You showed strong scenario reasoning, especially in Question 2 modular monolith. Your performance scenario, ADR context and browsing cache are good. To improve, make availability measurable, fix calculations, correct breaker states and CAP, add ADR negative and fix length/citations.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You chose relevant attributes and your performance scenario in Question 1 is complete with measurable 'p95 under 1.5 s'. Well done. For Excellent, rewrite your availability response 'stay up most of the time' as a measurable measure with all six parts complete.

*Assessor reasoning:* Suitable attributes with scenario justification. Performance scenario complete and measurable. Availability scenario has six parts but response measure is vague and unmeasurable, matching Proficient.
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work in Question 2: you recommended modular monolith with two scenario-specific trade-offs about five developers and single-VM downtime, and you acknowledged scaling/crash downside. To stay Excellent, keep linking both trade-offs and downside to scenario.

*Assessor reasoning:* Clear modular-monolith recommendation. Two scenario-specific trade-offs: 5-person team overhead and single-VM plus deployment downtime fixes. Downside explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Your Question 3(a) 99.30% was correct with working. To move up, fix (b) to 0.00699x720 ~5.0h not 3.5h, recalculate (c) end-to-end ~99.80% ~1.5h not payment-only 99.9975%, and show working to requested precision.

*Assessor reasoning:* (a) 99.30% correct. (b) method correct but 0.00699x720 is 5.0h not 3.5h. (c) uses payment-only 99.9975% not end-to-end ~99.80% and wrong downtime. Two parts wrong.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%,"  

### C4 Q4 Resilience pattern (2/5, Developing)

You correctly chose Circuit Breaker for the outage in Question 4 with threshold example. For higher level, correct states: Closed passes normally, Open fails fast, Half-Open probes recovery; and add a drawback/tuning trade-off.

*Assessor reasoning:* Circuit Breaker appropriate and applied to outage, but Open/Closed reversed throughout, so mechanism incorrect. Threshold example given but no explicit drawback or tuning trade-off.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds)"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your Question 5 choices AP browsing with Redis 60-second TTL and CP payments are sensible. For Excellent, correct CAP: you cannot give up partition tolerance, and name a concrete technique for orders/payments as you did for browsing.

*Assessor reasoning:* Both AP for browsing and CP for payments are reasonable. Browsing technique named, payment technique missing. CAP misused: cannot choose C+A over P during partition.
> Question 5: "show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Question 6 ADR gives specific context on synchronous tablet call at lunch peak and decision to publish OrderPaid via RabbitMQ. For Excellent, add at least one negative consequence like complexity or lag alongside positives.

*Assessor reasoning:* Context and Decision specific to synchronous tablet call and lunch peak. Multiple positives given but no negative consequence such as complexity or consistency lag, so one-sided.
> Question 6: "Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Outlets that are briefly offline still receive their orders when they reconnect."  

### C7 Communication and format (3/4, Proficient)

Your headings and IEEE [1] are clear. For Excellent, keep every answer within 150 words — shorten Question 2 from ~180 — list cited [2] in References and use precise breaker terms.

*Assessor reasoning:* Headings in order and IEEE-style [1]. Q2 ~180 words exceeds 150. [2] cited but missing from references, imprecise breaker terminology.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice,"  

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

- Question 1: Availability response measure 'most of the time' is not measurable.
- Question 3: (b) 5.03h not 3.5h; (c) end-to-end ~99.80% ~1.5h not 99.9975% 0.018h; wrong precision.
- Question 4: Open/Closed states reversed; Half-Open recovery reversed.
- Question 5: CAP error: cannot forgo partition tolerance; no concrete technique for orders.
- Question 6: No negative consequence stated.
- References: [2] cited but not listed; no assumptions stated.

## Next steps

1. Rewrite Q1 availability response to a measurable target and check all six parts for both scenarios.
2. Recalculate Q3(b)-(c) end-to-end availability/downtime to requested precision and correct Q4 breaker Open/Closed/Half-Open with a drawback.
3. Fix Q5 CAP wording plus concrete orders technique, add Q6 negative consequence, trim Q2 to 150 words and complete References.

---
<sub>Run Input_4_d-Run_2-Eff_high-261116-120314 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8126/11261 | cost $0.003616 (incl. $0.001628 for the reused reference rubric+task structure) | 47.18s</sub>
