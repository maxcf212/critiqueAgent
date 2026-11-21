# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 38 / 40 (95%)**

You produced a strong, complete submission with scenario-specific architecture choices, correct availability calculations and a well-formed ADR. Your answers are clearly organised and supported by references. To strengthen the work further, state assumptions explicitly and refine the overload and payment-consistency details in Questions 1 and 5.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 5 / 6 | 5 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 5 / 6 | 5 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (5/6, Excellent)

In Question 1, you chose and justified relevant attributes, and both scenarios include the six parts with measurable responses. To make the performance scenario stronger, define overload handling instead of promising every order is accepted without qualification.

*Assessor reasoning:* Both choices are justified by the scenario, and both scenarios include all six parts with measurable response measures. The performance response's requirement that every order be accepted may not be realistic under overload, but the measurable latency and dropped-request targets are clear.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering."  

### C2 Q2 Architectural style (6/6, Excellent)

Your Question 2 recommendation is specific to the five-person team, current deployment problems and 12-month horizon. You compare trade-offs and acknowledge the downside of a modular monolith.

*Assessor reasoning:* Clear recommendation, with trade-offs grounded in team size, known single-VM and deployment problems, and the 12-month horizon. The downside is explicitly acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Your Question 3 calculations are correct, with working and requested precision. State the independence assumption explicitly, rather than leaving it implicit in the availability multiplication.

*Assessor reasoning:* Series and redundant-payment calculations are correct under the stated independence assumptions. Availability is reported to two decimal places and final downtime to one decimal place; working is shown for all parts.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

In Question 4, you accurately explain and apply the circuit breaker to the provider outage. Your discussion of threshold tuning and the risk of rejecting recoverable payments adds a useful practical consideration.

*Assessor reasoning:* Circuit breaker mechanism is accurately explained and applied to the slow-provider outage, with a concrete threshold-tuning consideration and fallback drawback. It appropriately prevents blocked calls from exhausting request threads, though payment remains unavailable while open.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Last month the breaker would have opened within seconds, and students would have seen "payment temporarily unavailable" instead of the app hanging for 25 minutes."  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded; too lax and threads are exhausted first."  

### C5 Q5 Consistency and availability (5/6, Excellent)

Your Question 5 choices are justified using CAP trade-offs, and you name concrete techniques. Clarify that an idempotency key prevents duplicate retry effects but does not by itself ensure consistency between payment and order records.

*Assessor reasoning:* Both choices are justified, CAP is applied to partition-time trade-offs, and each case has a concrete technique. Idempotency addresses duplicate retries; by itself it does not ensure transactional consistency across order and payment systems, but the stated fail-closed choice is reasonable.
> Question 5: "it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page."  
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your Question 6 ADR includes scenario-specific Context, Decision and Consequences, with positive and negative outcomes. The durable queue decision and its operational cost are clearly identified.

*Assessor reasoning:* Context, decision, and consequences are specific to the scenario. Positive and negative consequences are both identified, including duplicate delivery handling and the delay before an outlet sees a paid order.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Your answers use the required headings, stay within the word limit, and include IEEE-style citations and references. The concise, organised presentation makes your reasoning easy to follow.

*Assessor reasoning:* All six required headings are used in order, answers are within the 150-word limit, and citations and a reference list are provided in an IEEE-style numbered format. Calculation working is included.
> Question 1: "## Question 1"  
> Question 3: "## Question 3"  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Question 1 |

## Technical issues

- Question 1: The performance scenario says every order is accepted while also setting peak-load response targets. Under overload, accepting every request may be infeasible; the response measure could specify an explicit rejection or queueing policy.
- Question 5: An idempotency key prevents duplicate effects for retries when implemented correctly, but does not alone guarantee consistency between payment and order records.
- Question 1: No assumptions are explicitly stated, despite the requirement to state any assumptions made. Independence is implicit in the availability multiplication in Question 3.

## Next steps

1. In Question 1, state any assumptions explicitly, including the independence assumption used in Question 3. Clarify what happens at peak load if the system cannot accept every order, such as queueing or returning a defined rejection response.
2. In Question 5, keep the idempotency key for preventing duplicate effects on retries, but explain how you would maintain or reconcile consistency between payment and order records; the key alone does not guarantee consistency across both.
3. Continue using the scenario-specific reasoning and concise structure shown in Questions 2, 4 and 6. For Question 4, retain the useful circuit-breaker tuning trade-off; for Question 6, keep showing both positive and negative consequences.

---
<sub>Run Input_4_u-Run_2-Eff_low-261118-151143 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8535/5126 | cost $0.003238 (incl. $0.001628 for the reused reference rubric+task structure) | 27.29s</sub>
