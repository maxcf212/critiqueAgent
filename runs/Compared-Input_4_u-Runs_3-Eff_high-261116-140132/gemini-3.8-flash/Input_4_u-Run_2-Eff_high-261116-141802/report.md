# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You delivered an outstanding submission, achieving full marks across all criteria. Your architectural decisions, trade-off analyses, and availability calculations were exceptionally thorough and grounded in the CampusEats scenario. Throughout Questions 1 to 6, you demonstrated rigorous application of architectural concepts, balanced positive and negative consequences, and adhered strictly to word counts, required structures, and IEEE referencing standards.

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

In Question 1, you clearly justified performance and availability using quantitative scenario metrics. You achieved the Excellent standard by providing complete six-part scenarios with clear, measurable response measures. To sustain this standard in future work, always ensure that your stimulus and response measures remain strictly quantifiable and verifiable against system telemetry.

*Assessor reasoning:* The two most critical attributes (performance and availability) are selected and well justified with quantitative details from the scenario. Both quality attribute scenarios strictly follow the six-part specification format and specify clear, measurable response measures.
> ## Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  

### C2 Q2 Architectural style (6/6, Excellent)

In Question 2, you provided a well-reasoned recommendation for a modular monolith. You successfully reached the Excellent level by grounding trade-offs in scenario constraints—such as team size and operational overhead—while explicitly addressing realistic downsides like shared failure domains. Continue to emphasize these operational realities and organizational scaling factors in future architectural evaluations.

*Assessor reasoning:* The student provides a clear recommendation for a modular monolith, justified by two specific, context-relevant trade-offs (small team operational overhead and monolith horizontal scaling vs rewrite costs). Realistic downsides (lack of independent process scaling and shared failure domain) are explicitly acknowledged.
> ## Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  

### C3 Q3 Availability calculation (8/8, Excellent)

In Question 3, your availability calculations for parts (a), (b), and (c) met the Excellent tier. You showed all working clearly, correctly applied series and parallel system availability formulas, and adhered strictly to the requested rounding precision. Keep displaying step-by-step intermediate working to ensure transparent, verifiable calculations in complex system topologies.

*Assessor reasoning:* Calculations for parts (a), (b), and (c) are completely accurate. Series and parallel availability formulas are correctly applied with clear intermediate working shown, and results are appropriately rounded to the requested precision (two decimal places for percentages, one for hours).
> ## Question 3: "The availability of placing an order is 99.30%."  

### C4 Q4 Resilience pattern (5/5, Excellent)

In Question 4, you met the Excellent rubric level by recommending the Circuit Breaker pattern, detailing its state transitions, and mapping it directly to the payment thread starvation issue. You also thoughtfully addressed tuning thresholds and fallback requirements. In future designs, consider pairing circuit breakers with bulkheads to isolate resource pools even further.

*Assessor reasoning:* The circuit breaker pattern is correctly identified and explained via closed, open, and half-open state transitions. It is directly tied to the scenario's cascading failure and thread starvation. Both tuning parameters (latency thresholds) and drawbacks (fallback requirement) are thoroughly covered.
> ## Question 4: "The Circuit Breaker pattern [2] would have contained the failure. Calls to the payment provider are wrapped in a breaker"  

### C5 Q5 Consistency and availability (6/6, Excellent)

In Question 5, you achieved the Excellent level by correctly applying the CAP theorem under network partitions to justify AP for menu browsing and CP for payments. Naming concrete techniques—Redis caching with TTL and idempotency keys—solidified your technical depth. Continue linking theoretical distributed system limits directly to practical application-level mitigation strategies.

*Assessor reasoning:* Both menu browsing and payment scenarios are evaluated with sound architectural choices (AP vs CP). The CAP theorem is accurately interpreted regarding network partitions, and concrete implementation techniques (Redis caching with TTL and idempotency keys) are provided.
> ## Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

In Question 6, your ADR fulfilled all Excellent criteria by including scenario-specific Context, Decision, and Consequences. You identified practical benefits and acknowledged negative impacts, such as running a RabbitMQ queue and managing at-least-once delivery deduplication. Maintain this rigor by always detailing both positive architectural gains and ongoing operational trade-offs.

*Assessor reasoning:* The ADR adheres to the required template and contains scenario-specific context (tablet outages and latency), a clear architectural decision (RabbitMQ queue), and balanced consequences covering both concrete latency/resilience benefits and negative operational/at-least-once delivery overheads.
> ## Question 6: "The queue is one more component for five developers to run and monitor. Delivery is at-least-once, so the tablet must ignore duplicate order IDs."  

### C7 Communication and format (4/4, Excellent)

In your document structure and References section, you satisfied all Excellent requirements. Every response remained under the 150-word limit, the required question headings were followed, technical terminology was precise, and citations followed IEEE style. Continue applying this concise, structured communication style to professional technical documentation.

*Assessor reasoning:* All responses strictly adhere to the 150-word limit. Headings follow the requested structure and sequence, technical terminology is precise, and external sources are cited and referenced in proper IEEE style.
> ## Question 1: "The scenarios use the six-part form from [1]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | ## Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | ## Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | ## Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | ## Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | ## Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | ## Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | ## References |

## Next steps

1. Continue utilizing six-part scenarios and concrete response measures in future software design tasks to define precise service level objectives.
2. Explore advanced resilience and data patterns, such as combining circuit breakers with bulkheads or implementing saga patterns for distributed transactions.
3. Maintain your balanced ADR documentation practice by capturing architectural reversibility and migration strategies alongside positive and negative trade-offs.

---
<sub>Run Input_4_u-Run_2-Eff_high-261116-141802 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8111/12554 | cost $0.042998 (incl. $0.001628 for the reused reference rubric+task structure) | 60.98s</sub>
