# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 31 / 40 (77.5%)**

A strong submission. Your modular monolith recommendation (Q2) is excellent, and Q3(a),(b) are correct with clear working. To reach the top levels: fix the Q3(c) end-to-end calculation, apply CAP correctly in Q5, add a negative consequence to your ADR, make your availability response measure measurable, and keep every answer within 150 words.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 | 6 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose suitable attributes with good justification, and your performance scenario is fully six-part and measurable. To reach Excellent, both scenarios must be complete and measurable: your availability response measure ('stay up most of the time') is not measurable. Replace it with a quantified target, such as uptime percentage or maximum downtime per month.

*Assessor reasoning:* Performance and availability are well justified from the scenario and the performance scenario is fully six-part and measurable. However, the availability response measure ('stay up most of the time') is not measurable, so not Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. Your modular monolith recommendation is justified with two trade-offs tied to scenario specifics (five developers, single VM, 20-minute deployment downtime), and you explicitly acknowledge the downside that a bug in one module can crash the whole process. This is exactly what the top level requires.

*Assessor reasoning:* Clear recommendation (modular monolith) with two trade-offs tied to scenario specifics (five developers, single VM, 20-minute deployment downtime), and the downside of the recommendation is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (6/8, Proficient)

Parts (a) and (b) are correct with working shown. In (c) you reported the payment subsystem's availability (99.9975%) as the end-to-end figure; end-to-end availability is the product of all three: 0.9985005 × 0.9995 × 0.999975 ≈ 99.75%, or about 1.8 h downtime per month. Also keep percentages to two decimals and downtime to one decimal as requested.

*Assessor reasoning:* Parts (a) and (b) are correct with working (99.30%, 5.0 h). In (c) the student reports the payment-subsystem availability (99.9975%) as the end-to-end availability; correct end-to-end is 0.9985005×0.9995×0.999975 ≈ 99.75%, downtime ≈ 1.8 h. Exactly one part incorrect, so Proficient.
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (4/5, Proficient)

Your Circuit Breaker answer is appropriate and correctly explained (Closed/Open/Half-Open) and applied to the 25-minute outage. For the full 5 marks, add an explicit drawback or tuning consideration — for example, the risk of a breaker opening too eagerly under transient spikes, or how the failure threshold and half-open probe rate should be tuned.

*Assessor reasoning:* Circuit Breaker is appropriate, correctly explained (Closed/Open/Half-Open) and applied to the 25-minute outage. However, no explicit drawback or tuning consideration is given beyond an example threshold, so not Excellent.
> Question 4: "the breaker moves to Open and calls fail immediately without waiting"  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both consistency/availability choices are reasonable and you named concrete techniques (Redis TTL cache, idempotency keys). However, CAP was misapplied: you cannot 'give up partition tolerance' — partitions will happen, and under a partition you must choose between consistency and availability. Restate each choice in those terms to reach Excellent.

*Assessor reasoning:* Both choices are reasonable and justified, with concrete techniques (Redis TTL cache; idempotency keys). But CAP is used incorrectly: partition tolerance cannot be given up; under partition one must trade C against A.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has specific Context, Decision and Consequences sections, but all consequences are positive. The top level requires at least one negative consequence too — for example, delayed outlet notifications, added queue infrastructure to operate, or the need to handle duplicate submissions.

*Assessor reasoning:* Context, Decision and Consequences are present and specific to the scenario, but all stated consequences are positive; no negative consequence (e.g., eventual notification delay, added infrastructure, duplicate handling) is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear, headings are used correctly, and IEEE citations and a reference list are present. To reach Excellent, every answer must be within 150 words — Question 2 (and likely Question 4) exceed the limit, so tighten these by cutting to the most scenario-specific points.

*Assessor reasoning:* Writing is clear, headings used, IEEE citations and reference list present. However, Question 2 (and likely Question 4) exceed the 150-word limit, so not Excellent.
> Question 2: "First, team size versus operational overhead."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 3 (c): End-to-end availability reported as 99.9975% (payment only); correct value is 0.9985005×0.9995×0.999975 ≈ 99.75%, downtime ≈ 1.8 h/month, not 0.018 h.
- Question 5: CAP theorem misapplied: partition tolerance cannot be sacrificed; during a partition one chooses between consistency and availability.
- Question 1: Availability response measure 'stay up most of the time' is not measurable.
- Question 3: Percentages not consistently given to two decimal places (99.9975%); downtime 0.018 h not rounded to one decimal place as required.

## Next steps

1. Recompute Q3(c) as the product of all three subsystem availabilities (0.9985005 × 0.9995 × 0.999975 ≈ 99.75%), giving ~1.8 h downtime/month, and round percentages to two decimals and downtime to one decimal as required.
2. In Q5, revise your CAP statement: partition tolerance cannot be sacrificed; during a partition you must choose between consistency and availability, then justify each choice on that basis.
3. Add at least one negative consequence to your Q6 ADR (e.g., delayed notifications or added infrastructure), add a drawback/tuning consideration to Q4, and make the Q1 availability response measure measurable (e.g., '99.5% uptime per month').

---
<sub>Run Input_4-Run_1-Eff_low-261118-120318 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8083/5023 | cost $0.002909 (incl. $0.001628 for the reused reference rubric+task structure) | 40.49s</sub>
