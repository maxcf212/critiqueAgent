# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You produced an outstanding submission, achieving full marks across every criterion. Your technical reasoning in the short-answer questions demonstrates exceptional engineering maturity. You skillfully grounded each response in the CampusEats scenario—from your six-part quality attribute scenarios and precise availability calculations to your well-balanced modular monolith recommendation and architecture decision record. Your writing remained rigorous, concise, and professional throughout.

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

In Question 1, you excellently formulated both performance and availability scenarios using the complete six-part template. Your justification drew directly from scenario load numbers, establishing precise, measurable response metrics. To maintain this high standard in future work, ensure you continue to define realistic operational environments and explicit failure thresholds.

*Assessor reasoning:* Performance and availability are justified with concrete data from the prompt. Both scenarios adhere strictly to the six-part template and provide clear, quantifiable response measures.
> Question 1: "Performance scenario. Source: students using the mobile app. Stimulus: 900 order requests arrive within one hour (about 15 per minute on average)."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation in Question 2 showed strong architectural reasoning. You anchored the decision in CampusEats' specific constraints—such as the five-person team and deployment overhead—while explicitly addressing operational downsides. To build on this level, continue balancing long-term evolution strategies against immediate team capacity and maintenance trade-offs.

*Assessor reasoning:* The recommendation of a modular monolith is well-grounded in scenario-specific trade-offs, citing the five-person team size, operational overhead, and existing architectural bottlenecks. Trade-off downsides are clearly acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  

### C3 Q3 Availability calculation (8/8, Excellent)

In Question 3, your calculations for parts (a), (b), and (c) were fully accurate with clear intermediate working and correct rounding precision. You effectively modelled series system availability and downtime. To push further in complex architectures, consider exploring parallel redundancy modeling and degraded-mode availability calculations.

*Assessor reasoning:* Parts (a), (b), and (c) are completely accurate. Calculations and clear intermediate working are shown, and final values are rounded to the required precision (two decimal places for percentages, one for hours).
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  

### C4 Q4 Resilience pattern (5/5, Excellent)

For Question 4, you thoroughly explained the Circuit Breaker pattern across all three states (Closed, Open, Half-Open). You directly linked it to mitigating thread exhaustion during payment outages and provided realistic tuning considerations. Moving forward, keep analyzing how multiple resilience patterns (such as fallback queues with bulkhead isolation) interact under failure.

*Assessor reasoning:* The Circuit Breaker pattern is correctly named and its states (Closed, Open, Half-Open) clearly explained. Its direct benefit to preventing thread exhaustion during the payment outage is shown alongside tuning considerations and drawbacks.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure. Calls to the payment provider are wrapped in a breaker"  

### C5 Q5 Consistency and availability (6/6, Excellent)

In Question 5, you applied the CAP theorem accurately, choosing AP for menu browsing and CP for order processing with solid justifications. Recommending concrete techniques like TTL caching and idempotency keys demonstrated practical depth. In future designs, explore how distributed consistency models like saga patterns handle partial transaction failures across boundaries.

*Assessor reasoning:* Appropriate choices are made for menu browsing (AP) and order placement/payment (CP). Justifications correctly apply the CAP theorem, and concrete technical solutions (caching with TTL and idempotency keys) are specified.
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your Architecture Decision Record in Question 6 is exceptionally well structured, covering Context, Decision, and Consequences with direct scenario relevance. You balanced positive impacts against clear negative trade-offs, such as deduplication complexity. Maintain this standard by continuing to capture operational and cost implications in professional ADRs.

*Assessor reasoning:* The ADR contains Context, Decision, and Consequences tailored to the scenario. Both positive impacts (improved latency, resilience to offline tablets) and negative consequences (operational overhead, deduplication requirements) are identified.
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  

### C7 Communication and format (4/4, Excellent)

Your presentation throughout the document was exemplary. Every response adhered strictly to the 150-word limit while using precise technical terminology, standard headings, and properly formatted IEEE references. Retain this concise, rigorous communication style in future professional documentation and design proposals.

*Assessor reasoning:* Formatting and structural requirements are fully respected. Required headings are used in order, answers adhere strictly to the 150-word limit, and references follow standard IEEE citation conventions.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Next steps

1. Extend your availability modeling by exploring how parallel redundancy, active-passive failover, and degraded service modes impact overall system reliability.
2. Investigate distributed transaction patterns, such as the Saga pattern, to handle consistency and compensating actions across modular boundaries.
3. Apply your Architecture Decision Record approach to larger-scale evolution strategies, explicitly factoring in deployment pipelines and operational run costs.

---
<sub>Run Input_4_u-Run_3-Eff_high-261116-141903 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8072/9796 | cost $0.032627 (incl. $0.001628 for the reused reference rubric+task structure) | 47.29s</sub>
