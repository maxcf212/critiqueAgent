# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 22 / 40 (55%)**

You showed good judgment on style and trade-offs, with clear scenarios for performance and a solid ADR. To improve, you need measurable response measures, correct availability maths, accurate pattern and CAP explanations, and balanced consequences with precise formatting.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 1 / 5 | 1 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You did well in Question 1 choosing two relevant attributes with lunch-peak justification and a measurable performance scenario. To reach Excellent, rewrite your availability measure — 'stay up most of the time' is not measurable — as a quantified target.

*Assessor reasoning:* Two relevant attributes justified from lunch-peak scenario. Performance scenario is six-part and measurable. Availability scenario has six parts but response measure is not measurable.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You excelled in Question 2 with a clear modular-monolith recommendation, two scenario-specific trade-offs on 5-person team and single VM downtime, and acknowledged that 'a bug in one module can still crash the whole process.'

*Assessor reasoning:* Clear modular-monolith recommendation. Two scenario-specific trade-offs: 5-person team vs overhead, single VM and deployment downtime fixes. Downside explicitly acknowledged.
> Question 2: "a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

You showed correct method in Question 3(a). To move up, fix Question 3(b) to ~5.0h and Question 3(c) to end-to-end series ~99.80% with ~1.5h downtime, showing working to requested precision.

*Assessor reasoning:* Part (a) correct. Part (b) arithmetic wrong: 0.00699x720 is ~5.0h not 3.5h. Part (c) wrong: uses payment-only 99.9975% not series ~99.80% and downtime ~1.5h.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours"  

### C4 Q4 Resilience pattern (1/5, Developing)

You picked an appropriate pattern for the Question 4 outage. To progress, correct your states — you wrote 'In the Open state calls pass through normally' — to Closed normal, Open fail-fast, Half-Open trials, plus a drawback.

*Assessor reasoning:* Appropriate pattern chosen and applied, but open/closed states inverted, so mechanism explained incorrectly. No clear drawback or tuning trade-off stated.
> Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices in Question 5 and named Redis TTL for menus. For Excellent, correct CAP — you cannot give up partition tolerance — and name a concrete payment technique.

*Assessor reasoning:* Both availability vs consistency choices reasonable. Menu technique named (Redis TTL). Payment technique missing and CAP misused; partition tolerance cannot be given up.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

You wrote specific Context, Decision and Consequences for outlet notification with good positives on lunch-peak smoothing. To reach Excellent, add at least one negative consequence like cost or complexity.

*Assessor reasoning:* Context, Decision, Consequences present and specific to outlet notification. Multiple positives given but no negative consequence, cost or complexity.
> Question 6: "The queue also smooths the lunch peak because the workers process orders"  

### C7 Communication and format (3/4, Proficient)

Your writing is clear with required headings. For Excellent, keep every answer within 150 words (check Q2), add missing reference [2] cited in Q4 to your list, and state assumptions.

*Assessor reasoning:* Clear writing with required headings, but [2] cited in Q4 missing from list, no assumptions stated, and Q2 likely exceeds 150-word limit.
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

- Question 3: (b) 0.00699*720 = 5.03h not 3.5h; (c) end-to-end = 0.9995*0.999*0.9995*0.999975 ~99.80% with ~1.5h downtime, not 99.9975% and 0.018h
- Question 4: Circuit breaker states reversed: Closed is normal operation, Open fails fast, Half-Open trials
- Question 5: CAP: partition tolerance is mandatory during partition; choice is between C and A, cannot sacrifice P

## Next steps

1. Rewrite vague measures and add missing negative consequence, payment technique, and breaker tuning.
2. Recalculate Q3(b)-(c) as full series with working and fix inverted Open/Closed breaker states and CAP claim.
3. Keep all answers under 150 words and complete your IEEE list, including [2] from Q4.

---
<sub>Run Input_4_d-Run_1-Eff_low-261118-144731 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 7887/6690 | cost $0.00299 (incl. $0.001628 for the reused reference rubric+task structure) | 37.16s</sub>
