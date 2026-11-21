# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Outstanding work across all six questions. Your Q1 scenarios were complete and measurable, Q2 was justified with scenario-specific trade-offs, all Q3 calculations verified correct with working shown, and Q4–Q6 named appropriate patterns and techniques with drawbacks acknowledged. Communication was precise, within word limits, and properly cited in IEEE style. Full marks awarded on every criterion.

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

Excellent. You chose performance and availability and justified both from scenario facts (900 orders/hour, 4.2 s p95, payment outage). Both scenarios contain all six parts with measurable response measures such as p95 thresholds and recovery time. To push further, make 'no requests are dropped' as precisely quantified as your other measures.

*Assessor reasoning:* Performance and availability are well justified from scenario facts (900 orders/hour, 4.2 s p95, payment outage). Both scenarios contain all six parts with measurable response measures (p95 thresholds, failure rate, recovery time).
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Source: the external payment provider. Stimulus: it becomes slow or stops responding."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent. Your modular monolith recommendation was justified by two scenario-specific trade-offs: the five-developer team's infrastructure overhead and the single-VM lunchtime bottleneck, with the weekly downtime window. You explicitly acknowledged the downside of independent scaling and crash propagation, which is exactly what the top level requires.

*Assessor reasoning:* Clear modular monolith recommendation with two scenario-specific trade-offs (team size of five, single-VM lunchtime bottleneck, 20-minute weekly downtime) and an explicitly acknowledged downside.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Excellent. All three parts verified correct with working shown: (a) 99.30%, (b) 5.0 hours, and (c) parallel payment availability 0.999975 giving 99.80% and 1.5 hours downtime. You met the requested precision throughout. Keep showing your working this clearly in future calculations.

*Assessor reasoning:* Verified: (a) 0.99301 → 99.30%; (b) 0.00699×720 = 5.03 → 5.0 h; (c) parallel payment 0.999975, series 0.99798 → 99.80%, downtime 1.46 → 1.5 h. All parts correct with working shown, percentages to two decimals and hours to one decimal as required.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent. You named the Circuit Breaker, correctly explained the Closed/Open/Half-Open mechanism, applied it concretely to the 25-minute payment outage, and gave both a tuning consideration and the drawback that payments fail while open, requiring a fallback. This covers every element of the top band.

*Assessor reasoning:* Circuit Breaker named, mechanism (Closed/Open/Half-Open) explained correctly, applied concretely to the 25-minute payment outage, and both a tuning consideration and a drawback are given.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Excellent. Your AP choice for menu browsing (Redis cache with TTL) and CP choice for payments (idempotency keys) were both justified, and you used the CAP theorem correctly by noting partition tolerance is not optional. A concrete technique was named for each case, meeting the highest level fully.

*Assessor reasoning:* AP for menu browsing (Redis cache with TTL) and CP for payments (idempotency keys) are both justified; CAP theorem is used correctly, noting partition tolerance is not optional. Concrete technique named for each case.
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Excellent. Your ADR contains Context, Decision and Consequences, all specific to CampusEats (4.2 s p95, offline tablets, five developers), with multiple positive and negative consequences including the at-least-once delivery requirement that the tablet must handle duplicate order IDs.

*Assessor reasoning:* ADR has Context, Decision and Consequences, all specific to the CampusEats scenario (4.2 s p95, offline tablets, five developers). Multiple positive and negative consequences are given.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs."  

### C7 Communication and format (4/4, Excellent)

Excellent. Every answer stayed within 150 words, the required Question 1–6 headings were used in order, terminology was precise, and you provided IEEE-style citations with a reference list. Availability and downtime formats were followed as required. Maintain this standard of presentation.

*Assessor reasoning:* All answers appear within 150 words, required headings Question 1–6 used in order, terminology precise, IEEE-style citations and reference list included, availability/downtime formats followed.
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

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

- Question 1: Minor: 'no requests are dropped' is slightly less precisely quantified than the other response measures, though bounded by the 0.1% failure figure elsewhere.

## Next steps

1. Quantify response measures like 'no requests are dropped' with an explicit figure (e.g. drop rate < 0.1%) so every measure is independently measurable.
2. Deepen trade-off analysis by quantifying the downside you accept, e.g. estimating the load at which the single-VM monolith would need to be split.
3. Practise applying these patterns beyond the scenario, e.g. sketch how the circuit breaker and idempotency keys would interact during a payment retry storm.

---
<sub>Run Input_4_u-Run_1-Eff_high-261116-141341 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8233/5725 | cost $0.003135 (incl. $0.001628 for the reused reference rubric+task structure) | 51.77s</sub>
