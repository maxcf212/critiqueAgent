# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You argued your modular-monolith well, but your availability calculations, breaker states and CAP explanation need correction. Tighten your measurable scenarios, add your ADR negative consequence, and fix word count and references to reach higher levels.

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

You chose two relevant attributes with good lunch-peak justification and your performance scenario is measurable. In Question 1 your availability response “the system should stay up most of the time.” is vague and unmeasurable. For Excellent, rewrite it with a measurable response measure covering all six parts.

*Assessor reasoning:* Two relevant attributes chosen with lunch-peak justification. Performance scenario measurable. Availability scenario has six parts but response measure is vague and unmeasurable, preventing Excellent.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You gave a clear modular-monolith recommendation in Question 2 with two scenario-specific trade-offs: five-developer overhead “With five developers, running eight or ten services would mean more time spent on infrastructure than on features.” and deployment fixes, plus you acknowledged “a bug in one module can still crash the whole process.” Excellent work — keep this specificity.

*Assessor reasoning:* Clear modular-monolith recommendation. Two scenario-specific trade-offs: 5-person team overhead and single-VM plus deployment downtime fixes. Downside of no independent scaling and process crash acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

You showed correct series method and part (a) 99.30% in Question 3. However “Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month.” should be ~5.03h, and “So the new availability of placing an order is 99.9975%” uses payment-only, not end-to-end ~99.80% ~1.5h. For higher level, recalculate (b) and (c) with working to requested precision.

*Assessor reasoning:* (a) 99.30% correct. (b) method correct but 0.00699x720 is 5.0h not 3.5h. (c) uses payment-only 99.9975% as end-to-end; correct is ~99.80% and ~1.5h. Two parts wrong.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You chose an appropriate Circuit Breaker for the outage with a threshold example in Question 4. But “In the Open state calls pass through normally.” inverts states — Closed is normal, Open is fail-fast. For higher level, correct Open/Closed/Half-Open behaviour and add one drawback or tuning consideration like timeouts or fallback.

*Assessor reasoning:* Circuit Breaker appropriate and applied to outage with threshold example. Mechanism reversed: Open described as normal and Closed as fail-fast, opposite of correct states. No clear drawback stated.
> Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices in Question 5 — availability with Redis 60-second TTL for menus and consistency for payments. However “so for payments we choose consistency and availability and give up partition tolerance.” misuses CAP; you must choose C vs A under partition. For Excellent, fix CAP and name a concrete technique for payments.

*Assessor reasoning:* Both choices reasonable: availability with Redis 60-second TTL for menus, consistency for payments. CAP misused; partition tolerance cannot be sacrificed. No concrete technique named for payment case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Question 6 Context and Decision are specific with RabbitMQ and OrderPaid event, and positives like “Outlets that are briefly offline still receive their orders when they reconnect.” are clear. For Excellent, keep those and add at least one negative consequence such as operational complexity or eventual-consistency handling.

*Assessor reasoning:* Context and Decision specific to CampusEats with RabbitMQ and OrderPaid event. Consequences present but only positive: latency, offline delivery, smoothing. No negative consequence stated.
> Question 6: "Outlets that are briefly offline still receive their orders when they reconnect."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear with required headings in order. In Question 2 you exceed 150 words (~181) and [2] is cited but absent, with “[1] L. Bass, P. Clements, and R. Kazman,” showing incomplete IEEE list. For Excellent, keep every answer within 150 words, list all sources, and state assumptions.

*Assessor reasoning:* Headings in order and clear writing. Question 2 exceeds 150 words (~181). [2] cited in text but missing from reference list, so IEEE citations incomplete.
> References: "[1] L. Bass, P. Clements, and R. Kazman,"  

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

- Question 3: (b) 0.00699*720=5.03h not 3.5h; (c) end-to-end ~99.80% ~1.5h, not 99.9975% 0.018h
- Question 4: Circuit Breaker states inverted: Closed is normal, Open is fail-fast
- Question 5: CAP: cannot choose C+A and give up P; must choose C vs A under partition
- Question 1: Availability response measure unmeasurable
- References: [2] cited but absent from reference list; no assumptions stated

## Next steps

1. Rewrite your Q1 availability response measure to be measurable with numbers, then recalculate Q3 (b) as 0.00699x720=~5.03h and Q3 (c) end-to-end as ~99.80% ~1.5h with working shown.
2. Correct your Q4 Circuit Breaker states to Closed is normal and Open is fail-fast, add one drawback or tuning consideration, and fix your Q5 CAP to choose consistency versus availability under partition with a concrete technique for payments.
3. Add at least one negative consequence to your Q6 RabbitMQ ADR, bring your Q2 answer within 150 words, complete your IEEE list so [2] appears, and state assumptions.

---
<sub>Run Input_4_d-Run_3-Eff_high-261116-120401 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 7987/13361 | cost $0.003886 (incl. $0.001628 for the reused reference rubric+task structure) | 57.9s</sub>
