# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 38 / 40 (95%)**

You produced a strong, technically accurate assignment. Your modular monolith recommendation, Q3 availability calculations and Circuit Breaker analysis were clearly grounded in the CampusEats scenario, and your ADR was complete. The main gaps are presentation: several answers sit at or just above the 150-word limit, your inputs are not stated as assumptions, and one technique choice needs tightening.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 5 / 6 | 5 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

You chose performance and availability and tied them to scenario facts such as the 900 lunch orders and the 4.2 s p95 response. Both scenarios have all six parts, and both response measures are quantified and testable. This is an Excellent answer. Keep this level of measurability in future responses.

*Assessor reasoning:* Two attributes are chosen and tied to scenario facts (900 lunch orders, 4.2 s p95, payment slowdown). Both scenarios have all six parts, and both response measures are quantified and testable.
> Question 1: "Performance and availability matter most"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You recommended a modular monolith and linked your trade-offs to the five-developer team, the single-VM lunchtime slowness and the weekly downtime. You also acknowledged the downside that modules cannot scale independently. To strengthen it, state the service count behind your claim of eight or more services as an explicit assumption.

*Assessor reasoning:* The modular monolith is clearly recommended. Trade-offs are tied to the five-developer team, the single-VM slowness and the weekly downtime. The downside is acknowledged. The unstated assumption of eight services slightly weakens it.
> Question 2: "The lunchtime slowness comes from a single virtual machine and is fixed by running several instances of the monolith behind a load balancer."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct: 99.30% for (a), 5.0 h for (b), and 99.80% with 1.5 h for (c). Working is shown to the required precision. Your component availabilities are not restated or sourced, so a reader cannot check your inputs. State them explicitly as assumptions to make your working fully verifiable.

*Assessor reasoning:* All three parts are correct on checking: (a) 99.30%, (b) 5.0 h, (c) 99.80% and 1.5 h. Working is shown at two decimal places. Component availabilities are not restated explicitly, which is a minor presentation gap.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named the Circuit Breaker and explained the Closed, Open and Half-Open states correctly, applying them to the 25-minute outage. You also gave a drawback (no payments while open, so a fallback is needed) and a tuning consideration. The claim that the breaker would have opened within seconds needs supporting data or stated assumptions, such as the failure threshold and latency figures used.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern. Closed, Open and Half-Open states are explained correctly and applied to the 25-minute outage. Tuning and fallback drawbacks are both given.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (5/6, Excellent)

Your CAP reasoning is correct. You chose consistency for payments, rejecting the order rather than risking an inconsistent charge, and availability for the menu with eventual consistency. You named a concrete technique for each, including a cache with TTL. The idempotency key prevents duplicate charges on retry but does not enforce consistency during a partition, so it is a weaker fit for the CP choice.

*Assessor reasoning:* CAP is used correctly, with both choices justified and a concrete technique for each (cache with TTL, idempotency key). The idempotency key addresses retry safety more than partition-time consistency, so it is a slightly weak fit.
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  
> Question 5: "This is the AP choice, with eventual consistency."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your ADR includes Context, Decision and Consequences, all specific to CampusEats. You described the synchronous tablet call and gave both positive and negative consequences, including at-least-once delivery and the stuck-queue risk. This is a complete record. Keep the consequences balanced as you did here.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats. Both positive and negative consequences are given, including at-least-once delivery and the stuck-queue risk.
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  

### C7 Communication and format (3/4, Proficient)

Your headings, IEEE citations and reference list are correct, and your terminology is precise. To reach the top band, every answer must be within 150 words. Q2, Q4 and Q6 sit at or slightly above the limit, so trim them. Adding an assumptions section would also make your inputs explicit.

*Assessor reasoning:* Headings, IEEE citations and reference list are correct and the terminology is precise. Several answers (Q2, Q4, Q6) sit at or slightly above 150 words by my count, and no assumptions section is provided.
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  
> References: "[2] M. T. Nygard, Release It! Design and Deploy Production-Ready Software, 2nd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 3: Component availabilities (0.9995, 0.999, 0.9995, 0.995) are used without being stated as assumptions or sourced, so the reader cannot verify the inputs.
- Question 2: The claim 'Five developers running eight or more services' assumes a service count that is not stated in the scenario or as an assumption.
- Question 5: An idempotency key prevents duplicate charges on retry; it is not a mechanism that enforces consistency during a partition, so it is a weak technique for the CP choice.
- Question 4: The claim that the breaker 'would have opened within seconds' is asserted without supporting data or stated assumptions.

## Next steps

1. Trim Questions 2, 4 and 6 so every answer is within 150 words. This is the main step needed to reach the top band for communication.
2. Add a short assumptions section that states your component availabilities for Q3 and the service count behind your claim of eight or more services in Q2, so a reader can verify your inputs.
3. In Q5, strengthen the CP payment choice with a mechanism that enforces consistency during a partition, such as a confirmed, synchronous write to the payment record, and explain how it does so.

---
<sub>Run Input_4_u-Run_3-Eff_high-261116-141240 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11695/17203 | cost $0.009827 (incl. $0.001628 for the reused reference rubric+task structure) | 61.0s</sub>
