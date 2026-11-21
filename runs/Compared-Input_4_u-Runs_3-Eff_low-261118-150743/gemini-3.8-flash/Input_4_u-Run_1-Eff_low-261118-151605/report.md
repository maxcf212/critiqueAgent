# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You have submitted an exemplary assignment that earned full marks across all criteria. Your answers demonstrated rigorous architectural reasoning, highly accurate mathematical working, precise terminology, and strict adherence to formatting constraints. You effectively integrated scenario-specific context throughout each question, from quality attribute scenarios to architecture decision records.

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

You achieved the Excellent level. In Question 1, you clearly justified performance and availability using exact scenario metrics. Both scenarios comprehensively detailed all six parts with precise, measurable response measures.

*Assessor reasoning:* Both performance and availability are thoroughly justified from the scenario details. Each scenario correctly specifies all six parts with precise, measurable response measures.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  

### C2 Q2 Architectural style (6/6, Excellent)

You achieved the Excellent level. In Question 2, your modular monolith recommendation was strongly justified by scenario constraints—such as the five-developer team and infrastructure overhead—while candidly acknowledging the structural downsides.

*Assessor reasoning:* Recommends a modular monolith with concrete, scenario-specific trade-offs addressing the 5-person team, single VM bottlenecks, and downtime. Accurately acknowledges inherent downsides.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  

### C3 Q3 Availability calculation (8/8, Excellent)

You achieved the Excellent level. In Question 3, parts (a), (b), and (c) presented fully correct formulas, clear intermediate working, and precise rounding as required.

*Assessor reasoning:* All calculations for parts (a), (b), and (c) are fully detailed with correct mathematical formulas, clear working, and accurate rounding to requested precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You achieved the Excellent level. In Question 4, you accurately detailed the Circuit Breaker pattern's mechanisms and states, applied it directly to thread pool starvation, and addressed threshold tuning.

*Assessor reasoning:* Correctly names the Circuit Breaker pattern, explains its three states, directly ties it to preventing thread pool starvation during payment outages, and discusses threshold tuning.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

### C5 Q5 Consistency and availability (6/6, Excellent)

You achieved the Excellent level. In Question 5, you applied the CAP theorem accurately to differentiate browsing and ordering, pairing each choice with concrete techniques like Redis caching and idempotency keys.

*Assessor reasoning:* Makes appropriate AP vs CP choices for browsing and ordering, explains the CAP trade-off accurately, and specifies concrete mechanisms (Redis cache with TTL, idempotency keys).
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  

### C6 Q6 Architecture decision record (5/5, Excellent)

You achieved the Excellent level. In Question 6, your ADR clearly articulated Context, Decision, and Consequences, balancing asynchronous decoupled event publishing against operational overhead and duplicate message delivery.

*Assessor reasoning:* Contains Context, Decision, and Consequences structured specifically around the scenario. Clearly balances operational benefits against duplicate delivery and operational overhead.
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  

### C7 Communication and format (4/4, Excellent)

You achieved the Excellent level. Across all questions and References, you strictly adhered to the 150-word limit per answer, maintained required headings, used precise terminology, and cited in proper IEEE format.

*Assessor reasoning:* All sections strictly conform to the 150-word limit, employ accurate terminology, maintain required structure, and cite valid sources in IEEE format.
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Next steps

1. Extend your architectural analysis by exploring quantitative modeling for circuit breaker failure rate thresholds and reset timeouts under varying traffic spikes.
2. Practice designing distributed transaction strategies, such as the Saga pattern, to handle complex multi-step failures across CP and AP boundaries.
3. Maintain this high standard of clear, balanced trade-off analysis and professional IEEE referencing in your future software architecture deliverables.

---
<sub>Run Input_4_u-Run_1-Eff_low-261118-151605 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 7953/4059 | cost $0.011024 (incl. $0.001628 for the reused reference rubric+task structure) | 16.73s</sub>
