# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You delivered an outstanding submission, achieving full marks across every criterion. Your technical justifications were thoroughly contextualized to the CampusEats scenario, your architectural calculations were precise with clear working, and your communication strictly met all formatting constraints.

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

You achieved Excellent by clearly justifying performance and availability with scenario data, providing fully complete six-part scenarios with measurable response metrics.

*Assessor reasoning:* Both attributes are well-justified from the scenario. Both six-part scenarios are complete and include measurable response measures.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  

### C2 Q2 Architectural style (6/6, Excellent)

You achieved Excellent by recommending a modular monolith grounded in team size and operational profile, explicitly acknowledging architectural downsides.

*Assessor reasoning:* Clear recommendation of a modular monolith justified by two detailed trade-offs explicitly tied to team size and operational profile, with explicit downsides acknowledged.
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

You achieved Excellent by correctly calculating parts (a), (b), and (c) with clear working and proper rounding precision.

*Assessor reasoning:* Parts (a), (b), and (c) are all completely correct with explicit working shown, rounded appropriately to the requested decimal places.
> Question 3: "The availability of placing an order is 99.30%."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You achieved Excellent by detailing the Circuit Breaker pattern's mechanics, applying it directly to the payment outage, and addressing tuning considerations.

*Assessor reasoning:* Circuit Breaker is named, states/transitions clearly explained, applied directly to the slow payment outage, and tuning considerations plus drawbacks are well articulated.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

### C5 Q5 Consistency and availability (6/6, Excellent)

You achieved Excellent by applying the CAP theorem accurately to both scenarios and identifying concrete technical solutions like Redis caching and idempotency keys.

*Assessor reasoning:* Both AP/CP choices are clearly justified using CAP principles, with concrete techniques named (Redis cache with TTL; idempotency key).
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  

### C6 Q6 Architecture decision record (5/5, Excellent)

You achieved Excellent by structuring ADR-007 with scenario-specific context, a definitive decision, and balanced positive and negative consequences.

*Assessor reasoning:* Context, Decision, and Consequences are scenario-specific, including multiple clear positive and negative consequences.
> Question 6: "ADR-007: Use a message queue for outlet order notifications"  

### C7 Communication and format (4/4, Excellent)

You achieved Excellent by adhering to the 150-word limit per question, maintaining precise terminology, and utilizing proper IEEE citation style.

*Assessor reasoning:* All answers adhere strictly to the 150-word limit, required headings are followed, terminology is precise, and IEEE references are properly formatted.
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

1. Continue applying rigorous six-part quality attribute scenarios and balanced trade-off evaluations in larger system design contexts.
2. Explore how the Circuit Breaker pattern integrates with complementary patterns like Bulkhead or Fallback in complex microservice architectures.
3. Apply this high standard of ADR documentation to capture non-functional trade-offs in future collaborative projects.

---
<sub>Run Input_4_u-Run_2-Eff_low-261118-151621 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 7914/3914 | cost $0.010451 (incl. $0.001628 for the reused reference rubric+task structure) | 14.15s</sub>
