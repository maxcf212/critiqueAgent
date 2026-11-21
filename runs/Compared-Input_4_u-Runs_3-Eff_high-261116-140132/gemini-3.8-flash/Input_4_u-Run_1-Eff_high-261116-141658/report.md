# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You have submitted an exemplary assignment that meets the Excellent standard across every criterion. Your calculations in Question 3 are exact and thoroughly documented, while your architectural justifications in Questions 1, 2, 4, 5, and 6 are tightly linked to CampusEats' specific constraints such as team size and peak traffic. Your concise technical writing and rigorous IEEE citations demonstrate outstanding professional communication.

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

You achieved Excellent by grounding performance and availability in scenario metrics (such as the 900 lunch-hour orders) and structuring both scenarios with all six parts. Both response measures were concrete and measurable (e.g., p95 under 1.5 s). To sustain this level, always ensure all six parts remain clearly labeled and tied to business impact.

*Assessor reasoning:* Both performance and availability are clearly justified using scenario metrics. Both quality attribute scenarios include all six parts (source, stimulus, artefact, environment, response, response measure) and feature concrete, measurable response metrics.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You achieved Excellent by recommending a modular monolith grounded in specific team-size and operational constraints, while explicitly accepting its drawbacks (shared process failure, coupled scaling). You fully met the top standard by pairing scenario-specific trade-offs with honest downsides.

*Assessor reasoning:* A modular monolith is recommended with two clear, scenario-specific trade-offs addressing team size, operational overhead, and existing architectural bottlenecks. Trade-off downsides are clearly acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The lunchtime slowness comes from a single virtual machine and is fixed by running several instances of the monolith"  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

You met the Excellent level by providing flawless calculations for parts (a), (b), and (c). Showing full step-by-step working and reporting availability to two decimal places and monthly downtime to one decimal place perfectly aligned with the prompt's precision requirements.

*Assessor reasoning:* All calculations for parts (a), (b), and (c) are technically correct, full working is shown, and results are reported to the required precision (availability to two decimal places, downtime to one decimal place).
> Question 3: "The availability of placing an order is 99.30%."  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "The new availability of placing an order is 99.80%."  
> Question 3: "Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You earned Excellent by correctly explaining the Circuit Breaker pattern's three states (Closed, Open, Half-Open), mapping it directly to the gateway failure, and highlighting latency-based tuning considerations. You have mastered this standard; maintain this by always considering fallback behavior alongside breaker state transitions.

*Assessor reasoning:* The circuit breaker pattern is correctly identified and its state transitions (Closed, Open, Half-Open) clearly explained. It is directly applied to the scenario failure, and practical tuning considerations and drawbacks are provided.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "In the Closed state calls pass through. When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (6/6, Excellent)

You reached Excellent by accurately applying the CAP theorem to justify separate consistency models for browsing (AP) and ordering (CP). Naming concrete techniques—Redis caching with TTL and idempotency keys with fast rejection—satisfied all requirements for the highest tier.

*Assessor reasoning:* Both architectural choices are sound and well justified using accurate CAP theorem reasoning. Concrete technical solutions (Redis caching with TTL for AP; idempotency keys and fast rejection for CP) are specified.
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability; partitions cannot be ruled out"  
> Question 5: "better to show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

You achieved Excellent by delivering a complete Architecture Decision Record (Context, Decision, Consequences) tailored to tablet disconnection. Including balanced trade-offs—such as acknowledging operational overhead and at-least-once delivery for RabbitMQ—solidified your top mark.

*Assessor reasoning:* The ADR is structured into Context, Decision, and Consequences. It specifically addresses tablet disconnection and latency issues, providing well-balanced positive and negative consequences.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor. Delivery is at-least-once"  

### C7 Communication and format (4/4, Excellent)

You met the Excellent standard across communication by adhering strictly to the 150-word limit per question, employing precise architectural terminology, using required headings, and providing clean IEEE citations and references. Continue using this clean, structured formatting in future submissions.

*Assessor reasoning:* All answers strictly observe the 150-word limit. Headings follow the prescribed format, technical terminology is used precisely throughout, and external sources are cited using IEEE format with a complete reference list.
> Question 1: "The scenarios use the six-part form from [1]."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

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

1. When designing future event-driven architectures (as in Question 6), consider detailing consumer-side idempotency strategies and dead-letter queue policies to handle poisoned messages.
2. In future architectural evaluations (like Question 2), explore potential phased migration paths, such as transitioning a modular monolith to selectively extract high-load components.
3. Continue using the six-part quality attribute scenario framework and explicit mathematical working across complex architectural design problems.

---
<sub>Run Input_4_u-Run_1-Eff_high-261116-141658 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8460/12135 | cost $0.04169 (incl. $0.001628 for the reused reference rubric+task structure) | 63.67s</sub>
