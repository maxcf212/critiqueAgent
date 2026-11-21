# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

This is an excellent submission. Your availability calculations in Question 3 are fully correct with working shown, your quality-attribute scenarios are complete and measurable, and your trade-offs, circuit breaker explanation, CAP reasoning and ADR are all scenario-specific and well justified. The only gap is that you never stated your assumptions explicitly, particularly the independence of component failures in Question 3, which the task instructions required.

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

Excellent (6/6). Your performance and availability attributes are well justified from scenario facts such as the 900 orders/hour load, the 4.2 s p95 and the payment outage. Both scenarios have all six labelled parts with measurable response measures. To sustain this level, keep each scenario focused on one response measure rather than bundling several, as you did in the availability scenario.

*Assessor reasoning:* Performance and availability are well justified from scenario facts (900 orders/hour, 4.2 s p95, payment outage). Both scenarios have all six labelled parts with measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent (6/6). Your modular monolith recommendation is clearly justified by two trade-offs tied to the scenario: the five-developer team and the single-VM lunchtime slowness with 20-minute downtime. You also explicitly acknowledged the downside that modules cannot be scaled independently. This is exactly the scenario-specific reasoning the top level requires; maintain it in future design justifications.

*Assessor reasoning:* Clear modular monolith recommendation with two scenario-specific trade-offs (team size, single-VM lunchtime slowness, 20-minute downtime) and an explicit downside acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (8/8, Excellent)

Excellent (8/8). All three parts are correct with working shown at the requested precision: the series product 0.99301 (99.30%), 5.0 hours downtime, and the parallel payment pair 0.999975 giving 99.80% and 1.5 hours. One improvement for next time: state the independence assumption behind the series and parallel formulas explicitly, as the task required and the marker noted it was only implied.

*Assessor reasoning:* All three parts verified correct: series product 0.99301 (99.30%), downtime 5.0 h, parallel payment pair 0.999975 giving 99.80% and 1.5 h. Working shown, precision as requested.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent (5/5). You named the Circuit Breaker pattern, correctly explained the Closed/Open/Half-Open mechanism, applied it to the 25-minute payment outage, and gave both a tuning consideration and the drawback that nobody can pay while it is open. This covers every element of the top rubric level; nothing further was needed here.

*Assessor reasoning:* Circuit Breaker correctly named and its Closed/Open/Half-Open mechanism explained, applied to the 25-minute payment outage, with both a tuning consideration and a drawback given.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Excellent (6/6). Both choices are justified: AP for menu browsing with a Redis cache and TTL, and CP for payments with idempotency keys. Your CAP reasoning is correct, noting that partition tolerance is not optional and a system must give up either consistency or availability during a partition. Concrete techniques are named for each case, meeting the top level fully.

*Assessor reasoning:* AP for menu browsing (Redis cache with TTL) and CP for payments (idempotency keys), both justified; CAP theorem used correctly, noting partition tolerance is not optional.
> Question 5: "during a partition a system must give up either consistency or availability"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Excellent (5/5). Your ADR has scenario-specific Context, a clear Decision (durable queue with a retrying worker), and both positive and negative consequences, including at-least-once delivery requiring the tablet to ignore duplicate order IDs and the added operational burden. This satisfies every requirement of the top level; a model structure to reuse in later ADRs.

*Assessor reasoning:* ADR has scenario-specific Context, a clear Decision (durable queue with retrying worker), and both positive and negative consequences including duplicate delivery and operational burden.
> Question 6: "If a tablet is offline the order is lost, and these calls add to the 4.2 s p95."  
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs."  

### C7 Communication and format (4/4, Excellent)

Excellent (4/4). All answers appear within the 150-word limit, the Question 1-6 headings are used in order, terminology is precise, and you provided IEEE-style citations including the Bass, Clements and Kazman reference. Keep this discipline with headings and citation style in future submissions.

*Assessor reasoning:* All answers appear within 150 words, headings Question 1–6 used in order, terminology precise, IEEE-style citations and reference list present.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Question 3 / References |

## Technical issues

- Whole document: No explicit assumptions statement; independence of component failures in Q3 is implied by the calculation but never stated as an assumption, contrary to the task instruction.
- Question 1: Availability scenario response measure bundles three measures; still measurable but slightly over-specified for a single six-part scenario.

## Next steps

1. Add an explicit assumptions section at the start of future submissions, e.g. stating that component failures are independent in availability calculations.
2. Keep each quality-attribute scenario to a single response measure; your availability scenario bundled three measures, which is over-specified for one six-part scenario.
3. Carry this standard of scenario-specific justification into the project work, where assumptions and trade-offs must be documented in your ADRs.

---
<sub>Run Input_4_u-Run_2-Eff_high-261116-141433 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8166/6378 | cost $0.003075 (incl. $0.001628 for the reused reference rubric+task structure) | 74.32s</sub>
