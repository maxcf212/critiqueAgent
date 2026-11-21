# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You showed strong scenario-specific reasoning, especially in Q2. To reach Excellent, tighten measurability, correct your availability chain in Q3c, fix CAP logic, and add trade-offs and concision.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You chose suitable attributes and your performance scenario was complete and measurable. Your availability scenario used "stay up most of the time" which is vague. For Excellent you need a measurable response with threshold, percentage or time.

*Assessor reasoning:* Suitable attributes with justification. Performance scenario complete and measurable. Availability scenario has six parts but response measure is vague and not measurable.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You gave an excellent recommendation in Question 2 with two scenario-specific trade-offs on 5-person overhead and single-VM downtime. You acknowledged the downside that a bug can crash the process. Keep this specificity.

*Assessor reasoning:* Clear modular monolith recommendation. Two scenario-specific trade-offs on 5-person overhead and single-VM plus deployment downtime. Downside acknowledged.
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

You did well to show working for Q3a 99.30% and Q3b 5.0h correctly. Your Q3c reported payment-only 99.9975% and 0.018h. For Excellent you must include all series components for ~99.80% and ~1.5h.

*Assessor reasoning:* Parts (a) 99.30% and (b) 5.0h correct with working. Part (c) reports payment-only availability, omits other three components; correct is ~99.80% and ~1.5h.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You correctly named Circuit Breaker in Question 4 and explained Half-Open trial calls applied to the slow-provider outage. For Excellent you need an explicit drawback or tuning consideration beyond example thresholds.

*Assessor reasoning:* Appropriate Circuit Breaker correctly explained and applied to slow-provider outage. No explicit drawback or tuning trade-off discussed, only example thresholds.
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices in Question 5 with Redis TTL and idempotency key. You stated you give up partition tolerance for payments. For Excellent you must correct CAP: you tolerate partitions and choose between C vs A.

*Assessor reasoning:* Both choices reasonable with techniques (Redis TTL, idempotency key). CAP used incorrectly: partition tolerance cannot be given up during partition.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

You included specific Context, Decision and Consequences in Question 6 and noted the queue smooths the lunch peak. For Excellent you need at least one negative consequence like complexity, ordering or failure handling.

*Assessor reasoning:* Context, Decision, Consequences present and specific. Multiple positives given but no negative consequence such as complexity or eventual consistency.
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (3/4, Proficient)

Your writing was clear with headings and IEEE citations. Your Question 2 at ~182 words exceeds the 150-word limit. For Excellent keep every answer within 150 words with precise terminology and formatting.

*Assessor reasoning:* Clear writing with headings and IEEE citations. Question 2 exceeds 150-word limit at ~182 words.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 3: Part (c) omits series components: correct end-to-end is 0.99800124975*0.999975=99.80% and ~1.5h downtime, not 99.9975% and 0.018h.
- Question 5: CAP statement incorrect: cannot choose C+A and abandon partition tolerance; partition must be tolerated, choice is C vs A.
- Question 1: Availability response measure not measurable; no time, percentage or threshold.
- Question 6: No negative consequence of queue (e.g., operational complexity, ordering, failure handling) stated.

## Next steps

1. Make your Q1 availability response measurable with a % / time bound and re-check all six parts.
2. Recalculate Q3c end-to-end as 0.99800124975*0.999975 for ~99.80% and ~1.5h, and correct your CAP statement that you cannot abandon partition tolerance.
3. Add a drawback/tuning note to Q4, a negative consequence to Q6, and cut Q2 to under 150 words.

---
<sub>Run Input_4-Run_2-Eff_low-261118-115601 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 11313/9309 | cost $0.003207 (incl. $0.001628 for the reused reference rubric+task structure) | 77.21s</sub>
