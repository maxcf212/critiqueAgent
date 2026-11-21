# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 25 / 40 (62.5%)**

You provide a clear, scenario-aware response, especially in Q2, where your modular-monolith recommendation reflects the five-person team and current deployment problems. Your main opportunities are to make Q1’s availability target measurable, correct Q3(c)’s end-to-end calculation, and use CAP accurately in Q5. Adding an explicit assumption and a downside to Q6’s queue decision would also strengthen completeness.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Developing | 2 / 6 | 2 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (2/6, Developing)

In Q1, you justify performance and availability using lunch-hour demand and latency, and your performance scenario is measurable. “Stay up most of the time” is not measurable, and the availability response does not address order placement or payment during provider failure. Add an explicit assumption and measurable target for the next level.

*Assessor reasoning:* The choices are justified using the lunch-hour load and current latency. The performance scenario has six parts and a measurable response measure. The availability measure is not measurable, and its response does not explain how orders are handled when payment is unavailable.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

In Q2, your modular-monolith recommendation is well grounded in the five-person team, deployment problems and lunch-hour load. You explain scenario-specific trade-offs and acknowledge that modules cannot be scaled independently. This is a strong response; keep linking trade-offs to the CampusEats context.

*Assessor reasoning:* The recommendation is clear and grounded in the five-person team, current deployment problems, and the lunch-hour load. It gives multiple scenario-specific trade-offs and acknowledges a downside.
> Question 2: "Instead the existing application should be restructured into a modular monolith"  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

In Q3(a)–(b), you show correct working. In Q3(c), your payment-provider redundancy calculation is correct, but you report it as end-to-end availability. Include the other three components in series to reach approximately 99.80% availability and 1.4 hours of monthly downtime for the next level.

*Assessor reasoning:* Parts (a) and (b) are correct to the requested precision. In (c), the payment availability is correctly calculated, but the end-to-end availability and downtime omit the other three required components. This is one incorrect part.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (4/5, Proficient)

In Q4, you correctly explain how the circuit breaker responds to a slow provider and how it can contain the failure. To reach the next level, add a drawback or tuning consideration, such as the risk of opening too readily or how to choose thresholds and recovery timing.

*Assessor reasoning:* The pattern mechanism and application to the slow-provider outage are explained correctly. It describes the user-visible benefit, but does not give a drawback or tuning consideration beyond an example threshold.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  

### C5 Q5 Consistency and availability (3/6, Proficient)

In Q5, you choose reasonable priorities and name concrete techniques: cached menu data and idempotency keys. Your CAP explanation needs correction: during a partition, a system must trade consistency against availability. Explain that favouring payment consistency can mean delaying or rejecting operations.

*Assessor reasoning:* The choices are reasonable and concrete techniques are named for both cases: cached menu data and idempotency keys. However, the CAP explanation is incorrect: during a partition, consistency and availability cannot both be guaranteed; choosing consistency means rejecting or delaying some requests.
> Question 5: "I would favour availability."  
> Question 5: "I would favour consistency"  
> Question 5: "each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (3/5, Proficient)

In Q6, your Context, Decision and Consequences are specific to the synchronous outlet-tablet call, and you identify the benefit of a durable queue. To reach the next level, add a negative consequence, such as increased operational complexity or delayed outlet notification while messages await processing.

*Assessor reasoning:* Context, decision, and consequences are present and scenario-specific. The consequences are only positive; no negative consequence, such as added operational complexity or eventual notification delivery, is acknowledged.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet"  

### C7 Communication and format (3/4, Proficient)

Your answers are clearly written, use the required headings and include an IEEE-like reference list; they appear to stay within the word limit. State the assumptions required by the task. For the top rubric level, ensure every answer meets the word limit and terminology and citations remain precise.

*Assessor reasoning:* The required headings are used in order, writing is clear, and sources are cited with a reference list in IEEE-like style. The response appears to keep each answer within 150 words. However, the submission does not state any assumptions, as required.
> Question 1: "The scenarios below use the six-part form from [1]."  
> References: "[2] M. T. Nygard, *Release It! Design and Deploy Production-Ready Software*"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 1: The availability response measure, “stay up most of the time,” is not measurable. The response describes menu browsing but does not specify handling order placement or payment during provider failure.
- Question 3: Part (c) reports payment-provider availability as end-to-end availability. The other three components remain in series: end-to-end availability is approximately 0.9980 (99.80%), giving about 1.4 hours of monthly downtime.
- Question 5: CAP is misstated: under a network partition, a distributed system must trade off consistency against availability. For payments, favouring consistency means refusing or delaying some operations during the partition, not retaining both consistency and availability.
- Question 6: The consequences list no downside of the queue decision, such as added infrastructure/operational complexity or delayed outlet notification while messages await processing.
- Question 1: No explicit assumptions are stated, despite the task requiring them.

## Next steps

1. In Q1, state an explicit assumption and make availability measurable (for example, a target percentage over a stated period). Explain what happens to order placement and payment if a provider fails; the next rubric level requires complete, measurable scenarios.
2. In Q3(c), combine the redundant payment-provider availability with the other three components, which remain in series, then calculate end-to-end availability and monthly downtime. Show the working to the requested precision; this is needed for the next rubric level.
3. In Q5, explain that during a network partition consistency and availability cannot both be guaranteed, then clarify that favouring payment consistency can delay or reject operations. In Q4 and Q6, add a circuit-breaker tuning consideration and a negative consequence of the queue decision, such as operational complexity or delayed outlet notification.

---
<sub>Run Input_4-Run_3-Eff_low-261118-120057 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8360/5284 | cost $0.003305 (incl. $0.001628 for the reused reference rubric+task structure) | 33.41s</sub>
