# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You made a strong start with your modular-monolith choice in Question 2 and Q3(a). To move higher, make your measures measurable, fix availability maths, correct breaker and CAP ideas, and balance your ADR.

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

You chose suitable attributes with scenario justification and your Question 1 performance scenario was complete. Your availability measure “stay up most of the time” is not measurable. For Excellent you need all six parts and measurable response measures.

*Assessor reasoning:* Suitable attributes with scenario justification. Performance scenario complete and measurable. Availability measure is vague and not measurable, fitting Proficient one missing measure.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You did excellent work in Question 2 recommending modular monolith with two scenario-specific trade-offs on team size and single-VM deployment. You acknowledged downside that modules cannot scale independently and a bug can crash the process. Keep this specificity.

*Assessor reasoning:* Clear modular-monolith recommendation with two scenario-specific trade-offs team size overhead and single-VM plus deployment causes, plus explicit downside acknowledged.
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

You got Q3(a) 99.30% correct with working. Your Q3(b) states 0.00699x720 as 3.5h and Q3(c) gives 99.9975% ~0.018h. For next level check arithmetic, include payment-to-outlet chain ~99.80% ~1.5h, and use requested precision.

*Assessor reasoning:* (a) 99.30% correct. (b) arithmetic wrong: 0.00699x720 is 5.0h not 3.5h. (c) 99.9975% is payment-only, end-to-end should be ~99.80% ~1.5h. Two parts incorrect.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  

### C4 Q4 Resilience pattern (2/5, Developing)

You appropriately named Circuit Breaker for the outage in Question 4, but you reversed states: “Open state calls pass through normally”. For next level explain Closed/Open/Half-Open correctly and add one drawback or tuning consideration.

*Assessor reasoning:* Circuit Breaker appropriate and applied to outage, but open/closed states reversed, half-open transition reversed. No explicit drawback, only threshold example. Explanation incorrect.
> Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices in Question 5 and named Redis TTL for browsing. You wrote you “give up partition tolerance” for payments and missed a payment technique. For Excellent use CAP correctly during partition and name a concrete technique for each case.

*Assessor reasoning:* Both choices reasonable with Redis TTL for browsing. CAP misused: cannot give up partition tolerance. No concrete technique named for payment consistency.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

You wrote clear Context, Decision and Consequences specific to outlets reconnecting in Question 6. You listed positives only. For Excellent keep specificity and add at least one negative consequence like eventual consistency or operational complexity.

*Assessor reasoning:* Context Decision Consequences present and specific, with multiple positives but no negative consequence such as eventual consistency or operational complexity.
> Question 6: "Outlets that are briefly offline still receive their orders when they reconnect."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear with headings and IEEE entry [1]. Your Q2 exceeds 150 words and in-text [2] has no reference entry. For Excellent keep every answer within 150 words and complete IEEE citations.

*Assessor reasoning:* Clear writing with headings, but Q2 exceeds 150 words and [2] cited in text has no reference entry, plus IEEE list incomplete.
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

- Question 3: (b) 0.00699*720=5.0h not 3.5h; (c) end-to-end is 0.9995*0.999*0.9995*0.999975≈99.80% ~1.5h, not 99.9975% ~0.018h; wrong precision.
- Question 4: Breaker states reversed: Closed is normal pass-through, Open is fail-fast; Half-Open on success closes, not opens.
- Question 5: CAP: during partition must choose C or A; cannot弃 partition tolerance; payment technique missing.

## Next steps

1. Rewrite your Question 1 availability response measure with a number and time window, then recheck all six parts.
2. Recalculate Q3(b)-(c) downtime and end-to-end availability showing working to requested precision.
3. Correct breaker states, CAP choice during partition, and add payment technique plus ADR negative.

---
<sub>Run Input_4_d-Run_2-Eff_low-261118-144808 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 7909/6472 | cost $0.002637 (incl. $0.001628 for the reused reference rubric+task structure) | 38.75s</sub>
