# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 37 / 40 (92.5%)**

You produced strong, scenario-specific work overall. Your Question 3 availability calculations are fully correct, and your modular monolith recommendation and Circuit Breaker answer are well grounded in CampusEats details. The main areas to improve are the word limits, the missing assumptions statement, and the depth of your payment consistency reasoning. The estimated mark is 37 out of 40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 5 / 6 | 5 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

You chose two attributes that clearly matter most for CampusEats, performance and availability, and tied them to the 900 lunch orders and the 4.2 s p95 problem. Both scenarios are in complete six-part form, and each response measure is numeric and testable, such as a p95 under 1.5 s. This is excellent work.

*Assessor reasoning:* Two attributes are chosen and justified from the scenario (900 lunch orders, 4.2 s p95, payment outage). Both scenarios have all six parts, and both response measures are numeric and testable.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation is clear and well justified by scenario-specific trade-offs, including your five-developer team and the operational cost of running many services. You also honestly acknowledge the downside: modules cannot scale independently and one bug can crash the whole process. Keep this level of specificity in future answers.

*Assessor reasoning:* A clear modular monolith recommendation is justified by scenario-specific trade-offs: five developers, the single-VM lunchtime slowness, and the 20-minute weekly downtime. The downside is explicitly acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct, with working shown: 99.30%, 5.0 h, 99.80% and 1.5 h. Your method and precision are sound. Continue showing each intermediate step clearly, as this is what secures full credit.

*Assessor reasoning:* I rechecked all parts: 99.30%, 5.0 h, 99.80% and 1.5 h are correct with working shown. The intermediate values are correct to the precision used, and the requested precision is met.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You correctly named the Circuit Breaker and explained the Closed, Open and Half-Open states. You applied it to the 25-minute outage and included a tuning consideration and a drawback. Your claim that the breaker would have opened within seconds last month needs supporting data or stated assumptions, otherwise it reads as unsupported.

*Assessor reasoning:* Circuit Breaker is appropriate and its Closed/Open/Half-Open mechanism is correct. It is applied to the 25-minute outage, with both a tuning consideration and a drawback given.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (5/6, Excellent)

Your CAP reasoning is correct, including the point that partition tolerance is not optional, and your choices for menu browsing and payments are justified. Redis TTL caching and idempotency keys are appropriate techniques. For payments, idempotency keys alone are limited, so discuss a stronger consistency mechanism such as transactional or quorum writes.

*Assessor reasoning:* Both choices are justified and CAP is stated correctly (partition tolerance is not optional). Redis TTL caching and idempotency keys are named. The payment consistency technique is thin, so I did not award the top mark.
> Question 5: "(i) Menu browsing: I would favour availability."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your decision record has clear Context, Decision and Consequences sections that are specific to CampusEats. You include both positive and negative consequences, such as the need to alert on a stuck queue and the operational burden for five developers. This is a strong decision record.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats. There are positive and negative consequences, including at-least-once delivery and the need for an alert on a stuck queue.
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (2/4, Developing)

Your headings are correct and your writing is clear. Several answers, including Questions 1, 2 and 4, appear to exceed the 150-word limit, so trim them. The references requirement was only partly met, so check that every source is complete. Add the explicit assumptions statement the brief asks for.

*Assessor reasoning:* Question 1, Question 2 and Question 4 each appear to exceed the 150-word limit, so several answers are over. Headings and IEEE-style references are correct. No assumptions section is given.
> Question 2: "First, independent scaling versus operational overhead."  
> Question 1: "The scenarios use the six-part form from [1]."  

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

## Technical issues

- Question 4: Claims the breaker 'would have opened within seconds' last month without supporting data or stated assumptions.
- Question 5: Payment consistency technique is limited to idempotency keys; no stronger consistency mechanism (e.g., transactional or quorum write) is discussed.
- Assumptions: No explicit statement of assumptions, such as independence of failures, despite the requirement.

## Next steps

1. Trim Questions 1, 2 and 4 to 150 words or fewer, keeping the key trade-offs and response measures.
2. Add a short assumptions section, for example stating whether component failures are independent, and check that your Question 3 and Question 4 reasoning is consistent with it.
3. Strengthen Question 5 by discussing a stronger payment consistency mechanism, such as transactional or quorum writes, and explain when idempotency keys alone are not enough. Also check that every reference is complete.

---
<sub>Run Input_4_u-Run_3-Eff_low-261118-151337 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11526/8673 | cost $0.005545 (incl. $0.001628 for the reused reference rubric+task structure) | 40.04s</sub>
