# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 38 / 40 (95%)**

You produced a strong, scenario-specific submission, with correct availability calculations and clear architectural reasoning. Your recommendation, circuit-breaker explanation, and ADR meet the highest rubric level. To strengthen the work further, make your payment consistency mechanism more explicit, clarify what happens to order placement during a payment outage, and state your assumptions.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

Question 1 selects and justifies performance and availability, and both scenarios include the six required parts with measurable response criteria. Clarify the order-placement behaviour during payment outages to make the availability scenario more complete.

*Assessor reasoning:* Selects and justifies two important scenario-specific attributes. Both scenarios identify source, stimulus, artefact, environment, response, and measurable response criteria.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering."  

### C2 Q2 Architectural style (6/6, Excellent)

Question 2 gives a well-supported modular-monolith recommendation, linking trade-offs to the five-person team, current performance and downtime issues, and the 12-month horizon. You also acknowledge the downside of shared scaling and process failure.

*Assessor reasoning:* Clear recommendation with trade-offs tied to the five-person team, current VM-related performance and downtime, and the 12-month horizon. A relevant downside is acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Question 3 shows the availability working and gives correct results to the requested precision, including the series calculation, monthly downtime, and active-active payment availability.

*Assessor reasoning:* Series and active-active payment availability calculations are correct. Monthly downtimes round to 5.0 and 1.5 hours, and availabilities are given to two decimal places.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Question 4 correctly explains and applies the circuit breaker to the provider outage. Your discussion of threshold tuning and rejecting payments while the breaker is open makes the trade-offs clear.

*Assessor reasoning:* Names and accurately explains the pattern states, applies it to the payment-provider outage, and discusses threshold tuning and the consequence of blocking payments while open.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded; too lax and threads are exhausted first."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Question 5 justifies both choices and names techniques, but an idempotency key prevents duplicate retries rather than ensuring consistent order/payment state during a partition. Add a transactional or strongly consistent mechanism to reach the top rubric level.

*Assessor reasoning:* Both choices are justified using partition behavior and CAP, and each has a concrete technique: cached menu data and payment idempotency keys. Idempotency helps prevent duplicate charges but is not, by itself, a consistency-enforcement technique for order/payment state.
> Question 5: "Menu browsing: I would favour availability."  
> Question 5: "This is the AP choice, with eventual consistency."  
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Question 6 includes a scenario-specific context, decision, and positive and negative consequences. Strengthen it by explaining how payment completion and queue publication are made atomic or otherwise coordinated.

*Assessor reasoning:* Includes specific context and decision, plus positive and negative consequences relevant to the scenario.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Your answers are clear, use the required headings, stay within the word limit, and include IEEE-style citations and references. State your assumptions explicitly to address the remaining gap noted in the marking.

*Assessor reasoning:* Answers use the required headings, are clear and within the 150-word limit, and include bracketed in-text citations and a reference list in substantially IEEE-style format.
> Question 1: "## Question 1"  
> Question 6: "## Question 6"  
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

## Technical issues

- Question 5: An idempotency key prevents duplicate processing of retries but does not alone ensure consistent order/payment state during a partition; a transactional or strongly consistent mechanism would make the consistency technique clearer.
- Question 1: The availability scenario says payment calls fail fast and browsing is unaffected, but does not specify how order placement behaves when payment is unavailable; the measured criterion covers non-payment requests and recovery.
- Question 6: The response-time benefit depends on how the system reports payment success and handles queue publication. The answer identifies at-least-once delivery and duplicate handling, but does not explain atomicity between payment completion and event publication.

## Next steps

1. In Question 5, keep your availability choice for menu browsing and consistency choice for payments, but add a mechanism that enforces consistent order/payment state during a partition, such as a transactional or strongly consistent operation. Explain that an idempotency key prevents duplicate retries but does not enforce consistency by itself.
2. In Question 1, specify what happens when payment is unavailable—for example, whether order placement is rejected or deferred—and include that behaviour in the measurable response criterion. This makes the outage scenario’s response clearer.
3. In Question 6, explain how payment completion and publication of the OrderPaid event are coordinated, including how you avoid losing an event if payment succeeds. Also state relevant assumptions explicitly; your references are present, but the marking identifies assumptions as the remaining gap.

---
<sub>Run Input_4_u-Run_1-Eff_low-261118-151113 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8454/5109 | cost $0.003611 (incl. $0.001628 for the reused reference rubric+task structure) | 29.69s</sub>
