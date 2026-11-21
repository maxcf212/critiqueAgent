# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You showed good architecture judgement across CampusEats, especially in Q2. To lift your marks, fix measurability, calculations, pattern mechanics, CAP reasoning, ADR balance and referencing precision detailed below.

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

Well done in Q1: you justified choices from the lunch peak and abandonment and your performance scenario was complete and measurable. For Excellent, rewrite your availability response measure: you wrote "stay up most of the time" which is vague. Give a measurable target like % uptime or max downtime.

*Assessor reasoning:* Attributes justified from lunch peak and abandonment. Performance scenario complete and measurable. Availability scenario has six parts but response measure is vague and not measurable, preventing Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work in Q2: you clearly recommended a modular monolith with two scenario-specific trade-offs about the 5-person team and single-VM plus deployment downtime. You acknowledged the downside that "a bug in one module can still crash the whole process." Keep this level of scenario linkage.

*Assessor reasoning:* Modular monolith clearly recommended. Two scenario-specific trade-offs: 5-person team overhead and single-VM plus deployment downtime fixes. Downside of no independent scaling and process crash acknowledged.
> Question 2: "a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

You got Q3(a) 99.30% correct in Q3, but Q3(b) should be ~5.0h not 3.5h and Q3(c) should be series ~99.80% and ~1.5h, not payment-only "0.000025 × 720 = 0.018 hours". For next level, correct both parts, show working and use requested precision.

*Assessor reasoning:* (a) 99.30% correct. (b) method correct but 0.00699x720=5.0h not 3.5h. (c) incorrect: reports payment-only availability 99.9975% instead of series ~99.80% and wrong downtime. Two parts wrong.
> Question 3: "which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

Good choice of Circuit Breaker in Q4 with fallback message and tuning idea. However you wrote "In the Open state calls pass through normally" - states are reversed. Open should fail-fast, Closed allows through. For next level, fix this and explain mechanism correctly plus drawback/tuning.

*Assessor reasoning:* Circuit Breaker appropriate and applied with fallback message. Mechanism reversed: Open described as closed-through and Closed as open-fail-fast. Tuning example given but core state explanation incorrect.
> Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable AP for menus and CP for payments choices in Q5 with Redis TTL for menus. For Excellent you must fix CAP: you wrote "for payments we choose consistency and availability and give up partition tolerance" which is incorrect, and name a concrete consistency technique for orders.

*Assessor reasoning:* Both AP for menus and CP for payments reasonable. Menu technique Redis TTL given, payment technique missing. CAP misused: partition tolerance cannot be given up in distributed case. Fits Proficient.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Q6 ADR has specific Context, Decision and Consequences around the synchronous tablet call and p95, e.g. "The queue also smooths the lunch peak". For Excellent, add at least one negative consequence like ops complexity, latency or eventual consistency, not positives only.

*Assessor reasoning:* Context, Decision, Consequences present and specific to synchronous tablet call and p95. Multiple positives given but no negative consequence such as ops complexity or eventual consistency, so one-sided.
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (3/4, Proficient)

Your headings were ordered and writing clear with IEEE [1] cited. For Excellent, keep every answer within 150 words - Q2 likely exceeds - and add the missing reference-list entry for [2] cited in Q4 with full IEEE style.

*Assessor reasoning:* Headings in order and IEEE style for [1], but [2] cited in Q4 has no reference-list entry. Q2 likely exceeds 150 words. Clear writing overall, so Proficient not Excellent.
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*,"  

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

- Question 3: (b) downtime should be ~5.0h not 3.5h; (c) end-to-end should be ~99.80% and ~1.5h downtime, not payment-only 99.9975% and 0.018h; wrong precision.
- Question 4: Circuit-breaker Open/Closed states swapped; Open should fail-fast, Closed should allow-through.
- Question 5: CAP statement incorrect: cannot sacrifice partition tolerance; must choose C or A during partition. No concrete consistency technique for orders.

## Next steps

1. Recalculate Q3(b) downtime and Q3(c) series availability to requested precision with full working shown.
2. Correct Q4 breaker states and Q5 CAP choice, adding a concrete consistency technique for payments.
3. Make Q1 availability measure measurable, add a negative consequence to Q6, and fix Q2 length and missing [2] reference.

---
<sub>Run Input_4_d-Run_3-Eff_low-261118-144847 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 11213/9237 | cost $0.003071 (incl. $0.001628 for the reused reference rubric+task structure) | 57.85s</sub>
