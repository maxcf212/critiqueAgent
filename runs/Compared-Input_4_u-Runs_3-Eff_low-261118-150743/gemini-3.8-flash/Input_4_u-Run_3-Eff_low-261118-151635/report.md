# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You delivered an exceptional submission that met all requirements at the highest level. Your architectural decisions were tightly coupled with the CampusEats scenario, calculations were exact and neatly presented, and all patterns were thoroughly analyzed with practical trade-offs. Your writing remained precise, well-structured, and strictly compliant with word counts and citation guidelines throughout.

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

You achieved Excellent by justifying performance and availability using direct metrics from the scenario in Question 1. Both quality attribute scenarios included all six parts with concrete, measurable response measures.

*Assessor reasoning:* Both quality attributes are thoroughly justified using specific scenario details. Each scenario includes all six required parts with clear, concrete, and measurable response measures.
> ## Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> ## Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You achieved Excellent by recommending a modular monolith in Question 2, supporting it with scenario-specific constraints like team size, and transparently acknowledging the downside of shared-process failures.

*Assessor reasoning:* A clear recommendation is provided and justified with two scenario-specific trade-offs (team size/overhead and VM/deployment issues vs rewrite costs), with explicit downsides acknowledged.
> ## Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> ## Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

You achieved Excellent by correctly computing parts (a), (b), and (c) in Question 3 with full working shown and accurate rounding to the requested precision.

*Assessor reasoning:* Parts (a), (b), and (c) are fully correct. All mathematical workings are shown clearly, and values are rounded accurately to the requested precision (two decimals for availability, one for downtime).
> ## Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301

The availability of placing an order is 99.30%."  
> ## Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> ## Question 3: "The new availability of placing an order is 99.80%.

Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You achieved Excellent in Question 4 by clearly detailing the Circuit Breaker mechanism, mapping it to the outage, and discussing practical threshold-tuning considerations and operational risks.

*Assessor reasoning:* Circuit Breaker is appropriately selected. The mechanism across closed, open, and half-open states is clearly explained, directly applied to the scenario outage, and includes tuning considerations and drawbacks.
> ## Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> ## Question 4: "Tuning consideration: the threshold must come from real latency data. Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded"  

### C5 Q5 Consistency and availability (6/6, Excellent)

You achieved Excellent by correctly applying the CAP theorem in Question 5, justifying AP for browsing and CP for payments, and offering concrete implementation techniques like Redis TTL caches and idempotency keys.

*Assessor reasoning:* Both choices (AP for menu browsing, CP for ordering/payments) are soundly justified with clear reference to CAP theorem implications. Concrete techniques (Redis cache with TTL, idempotency keys) are provided.
> ## Question 5: "Menu browsing: I would favour availability. If a partition separates an application server from the database, it is better to show a slightly stale menu"  
> ## Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

You achieved Excellent in Question 6 by providing a well-structured ADR containing specific context, a clear decision, and balanced positive and negative operational consequences.

*Assessor reasoning:* The ADR is structured cleanly with Context, Decision, and both positive and negative consequences that are specific and relevant to the scenario.
> ## Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> ## Question 6: "Consequences (positive): Placing an order no longer waits for the outlet, so the response time improves."  
> ## Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor. Delivery is at-least-once"  

### C7 Communication and format (4/4, Excellent)

You achieved Excellent by keeping every response under the 150-word limit, adhering to required headings, and correctly formatting external sources in IEEE citation style.

*Assessor reasoning:* All answers are well within the 150-word limit. Headings strictly follow the required structure, writing is concise and precise, and external sources are cited properly in IEEE style.
> ## Question 1: "The scenarios use the six-part form from [1]."  
> ## References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed. Upper Saddle River, NJ, USA: Addison-Wesley, 2012."  

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

1. Apply your strong scenario-grounded reasoning and quality attribute workshops to future end-to-end system design projects.
2. Explore distributed tracing and observability patterns to complement resilience tactics like Circuit Breakers in asynchronous workflows.
3. Practice evaluating complex architectural trade-offs where multiple viable consistency models (such as causal or read-your-writes consistency) apply.

---
<sub>Run Input_4_u-Run_3-Eff_low-261118-151635 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8452/4909 | cost $0.014585 (incl. $0.001628 for the reused reference rubric+task structure) | 29.58s</sub>
