# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Excellent submission: all six answers are complete, specific and within limits, and your Q3 calculations are correct to the requested precision. You justify choices from the CampusEats scenario and acknowledge downsides. The only minor gap is that no explicit assumptions statement is included, and the references requirement was marked partial. Keep the same precision and scenario-specific reasoning.

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

You chose performance and availability and justified them from the 900 lunchtime orders and the 4.2 s p95. Both six-part scenarios have measurable response measures: p95 under 1.5 s and under 0.1% non-payment failures. This is Excellent; keep every response measure measurable and tied to the scenario.

*Assessor reasoning:* Performance and availability are clearly justified from the scenario. Both quality attribute scenarios contain all six parts and use measurable response measures.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation is clear and tied to team size, lunchtime load, single-VM slowness and weekly downtime. You explicitly acknowledge the downside: modules cannot scale independently and one bug can crash the process. Excellent. Keep trade-offs scenario-specific and continue naming the accepted downside.

*Assessor reasoning:* Clear modular monolith recommendation. Trade-offs are specific to team size, lunchtime load, single-VM slowness and weekly downtime. The downside is explicitly acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite"  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct with working shown: 99.30%, 5.0 hours, 99.80% and 1.5 hours. You rounded to the requested precision. Excellent. To maintain this, keep showing the series calculation and the downtime conversion explicitly.

*Assessor reasoning:* All three parts are correct with working shown. Results are rounded to the requested precision: 99.30%, 5.0 hours, 99.80%, and 1.5 hours.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named Circuit Breaker, explained its mechanism, applied it to the slow payment provider outage, and gave tuning considerations plus a drawback: nobody can pay while it is open, so a fallback is needed. Excellent. Keep linking the pattern to the specific failure and stating the drawback.

*Assessor reasoning:* Circuit Breaker is appropriate and correctly explained. It is applied to the slow payment provider outage, and both tuning considerations and a drawback are given.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

You justified menu browsing as availability with a Redis cache and TTL, and payments as consistency with idempotency keys, using CAP correctly. Excellent. Continue naming a concrete technique for each choice and explaining the CAP trade-off precisely.

*Assessor reasoning:* Both choices are justified using CAP correctly. Concrete techniques are named: Redis cache with TTL for menu browsing and idempotency keys for payment consistency.
> Question 5: "Menu browsing: I would favour availability."  
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error"  
> Question 5: "Each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your ADR has Context, Decision and Consequences specific to CampusEats, including positive and negative consequences: faster response, but an extra component for five developers to run and monitor. Excellent. Keep both consequence types and scenario-specific context.

*Assessor reasoning:* ADR has Context, Decision and Consequences, all specific to CampusEats. It includes both positive and negative consequences.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences (positive): Placing an order no longer waits for the outlet, so the response time improves."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

You used the required headings in order, stayed within 150 words, used precise terminology, and included IEEE-style citations. Excellent. The references requirement was marked partial, so check every entry is complete and consistently formatted.

*Assessor reasoning:* Required headings are used in order. Answers are within the 150-word limit, terminology is precise, and IEEE-style citations and reference list are present.
> Question 1: "## Question 1"  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Next steps

1. Add a short explicit assumptions statement, for example independence of components in Q3 and traffic distribution in Q1, so your calculations and scenarios are unambiguous.
2. Tighten the references list: ensure every cited source has a complete IEEE-style entry, since R7 was marked partial.
3. Maintain the Excellent standard by keeping every quality-attribute scenario in six-part form with measurable response measures and every recommendation tied to at least two scenario-specific trade-offs plus an acknowledged downside.

---
<sub>Run Input_4_u-Run_1-Eff_high-261116-140416 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8272/14281 | cost $0.009183 (incl. $0.001628 for the reused reference rubric+task structure) | 42.49s</sub>
