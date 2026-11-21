# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Outstanding work across all six questions. Your Q1 scenarios were complete and measurable, your Q2 recommendation was scenario-specific with an acknowledged downside, and every Q3 calculation was verified correct with working shown. Your Circuit Breaker, CAP analysis and ADR were all precise and grounded in CampusEats. Formatting, headings and IEEE citations were exemplary. You achieved full marks: 40/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 6 / 6 | 6 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

Excellent. You chose performance and availability and justified both from scenario figures (900 orders/hour, 4.2 s p95, payment outage). Both scenarios included all six parts with measurable response measures, such as p95 under 1.5 s and under 0.1% of non-payment requests failing. To sustain this level, keep tying every response measure to a concrete scenario number.

*Assessor reasoning:* Performance and availability are well justified from the scenario (900 orders/hour, 4.2 s p95, payment outage). Both scenarios contain all six named parts with measurable response measures tied to scenario figures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent. Your modular monolith recommendation was justified by two scenario-specific trade-offs: the five-developer team's infrastructure burden and the lunchtime load with 20-minute downtime tolerance. You explicitly acknowledged the downside that modules cannot be scaled independently. Maintain this habit of naming what you give up with every recommendation.

*Assessor reasoning:* Clear modular monolith recommendation with two scenario-specific trade-offs (team size, lunchtime load, 20-minute downtime) and an explicit downside acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (8/8, Excellent)

Excellent. All three parts were verified correct: the series product 0.99301 (99.30%), 5.0 hours downtime, and the parallel payment pair at 0.999975 giving 99.80% and 1.5 hours. Working was shown and precision matched requirements. One refinement: explicitly state the independence assumption behind the product formula rather than leaving it implicit.

*Assessor reasoning:* All three parts verified correct: series product 0.99301 (99.30%), downtime 5.0 h, parallel payment pair 0.999975 giving 99.80% and 1.5 h. Working shown, precision matches requirements.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent. You named the Circuit Breaker, correctly explained the Closed/Open/Half-Open mechanism, applied it to the 25-minute payment outage, and gave both a tuning consideration and the drawback that payments fail while open, requiring a fallback. This full treatment is exactly what the top level requires; keep pairing mechanisms with their costs.

*Assessor reasoning:* Circuit Breaker correctly named and its Closed/Open/Half-Open mechanism explained, applied to the 25-minute payment outage, with both a tuning consideration and a drawback given.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Excellent. You justified AP for menu browsing (Redis cache with TTL) and CP for payments (idempotency keys preventing duplicate charges), and applied CAP correctly by noting partition tolerance is not optional. Naming a concrete technique for each case lifted this to the top level; continue grounding theory in specific mechanisms.

*Assessor reasoning:* AP for menu browsing (Redis cache with TTL) and CP for payments (idempotency keys) both justified; CAP theorem applied correctly, noting partition tolerance is not optional.
> Question 5: "during a partition a system must give up either consistency or availability"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Excellent. Your ADR contained scenario-specific Context, Decision and Consequences, with positives and negatives including at-least-once delivery requiring duplicate ID handling, offline tablet order loss, and added load on the 4.2 s p95. Balanced consequences on both sides is what distinguishes the top level; keep this two-sided style in future records.

*Assessor reasoning:* ADR has Context, Decision and Consequences, all specific to CampusEats, with multiple positive and negative consequences including duplicate delivery and operational burden.
> Question 6: "If a tablet is offline the order is lost, and these calls add to the 4.2 s p95."  
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs."  

### C7 Communication and format (4/4, Excellent)

Excellent. You used the required headings in order, kept every answer within 150 words (correctly excluding calculations), used precise terminology, and provided IEEE-style in-text citations and a reference list. This is a model of the communication standard; maintain it in longer assignments where discipline is harder.

*Assessor reasoning:* Required headings used in order, answers appear within 150 words, terminology precise, IEEE-style in-text citations and reference list present. Calculations correctly excluded from limit.
> References: "L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | Question 3 / References |

## Technical issues

- Question 3: Independence of component failures is assumed rather than explicitly stated as an assumption, though the task supplies it; minor.

## Next steps

1. State your assumptions explicitly in calculations (e.g., note in Q3 that component failures are treated as independent), even when the task supplies them.
2. Deepen your pattern knowledge by exploring combinations, such as Circuit Breaker paired with a fallback or bulkhead, and their interaction trade-offs.
3. Practise applying these skills to larger design tasks, such as architecture documentation or evaluation exercises, where the same rigour will transfer well.

---
<sub>Run Input_4_u-Run_3-Eff_high-261116-141547 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8130/5673 | cost $0.00286 (incl. $0.001628 for the reused reference rubric+task structure) | 70.93s</sub>
