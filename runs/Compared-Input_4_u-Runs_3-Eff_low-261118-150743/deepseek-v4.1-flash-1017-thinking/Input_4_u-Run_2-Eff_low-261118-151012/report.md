# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You delivered a strong, well-targeted submission: Q1 attributes and six-part scenarios are measurable, Q2 trade-offs are scenario-specific with an acknowledged downside, Q3 arithmetic is correct, Q4–Q6 reasoning is precise, and C7 formatting/citations are clean. To strengthen future work, make assumptions explicit—especially independence in Q3 and the hypothetical service count in Q2.

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

Q1 is excellent: you chose performance and availability from concrete scenario facts (900 lunch orders, 4.2 s p95, payment outage) and both scenarios have all six parts with measurable response measures (p95 <1.5 s; menu p95 <2 s, <0.1% non-payment failures). To stay at this level, keep tying each part to a scenario fact.

*Assessor reasoning:* Two attributes tied directly to scenario facts (lunch peak, 4.2 s p95, payment outage). Both scenarios have all six parts and measurable response measures.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

Q2 is excellent: your modular-monolith recommendation is justified by team size, single-VM lunchtime load, and weekly downtime, and you explicitly accept the downside that modules cannot scale independently and one bug can crash the process. Next time, flag the 'eight or more services' figure as an assumption about a hypothetical microservices design.

*Assessor reasoning:* Clear modular-monolith recommendation with two scenario-specific trade-offs (team size, single VM, weekly downtime) and an explicit acknowledged downside.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The lunchtime slowness comes from a single virtual machine and is fixed by running several instances of the monolith behind a load balancer."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Q3 is excellent: the series product 0.99301 (99.30%), 5.0 h downtime, and parallel payment 0.999975 giving 0.99798 (99.80%) and 1.5 h are all correct with working. To strengthen, state the independence assumption explicitly before multiplying; the arithmetic and precision already meet the Excellent descriptor.

*Assessor reasoning:* All three parts correct with working: series product 0.99301 (99.30%), 5.0 h downtime, parallel payment 0.999975 giving 0.99798 (99.80%) and 1.5 h. Precision as requested.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Q4 is excellent: you name circuit breaker, explain Open-state fail-fast behaviour, apply it to the 25-minute hang, and give both a tuning consideration (threshold from real latency data) and a drawback (no payments while open, so fallback needed). Keep this pattern of mechanism + application + trade-off.

*Assessor reasoning:* Circuit breaker named, states and transitions explained correctly, applied to the 25-minute hang, with both a tuning consideration and a drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Q5 is excellent: AP for browsing with Redis 60-second TTL and CP for payments with idempotency keys are both justified from scenario risk; CAP is stated correctly and a concrete technique is named for each case. Continue linking each choice to the specific failure risk.

*Assessor reasoning:* AP for browsing and CP for payments, both justified from scenario risk; CAP stated correctly and a concrete technique named for each case.
> Question 5: "it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page"  
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Q6 is excellent: Context, Decision and Consequences are all present and scenario-specific, with two positive and three negative consequences. The ADR clearly describes the synchronous tablet call and the RabbitMQ OrderPaid decision. Keep balancing positive and negative consequences in future ADRs.

*Assessor reasoning:* All three ADR sections present and scenario-specific, with two positive and three negative consequences.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

C7 is excellent: every answer is within 150 words, terminology is precise, headings are in order, and IEEE-style citations/reference list are present. The only improvement is to add an explicit assumptions statement where relevant (Q3 independence, Q2 service count); this will make your reasoning fully transparent.

*Assessor reasoning:* All answers at or under 150 words, precise terminology, required headings in order, IEEE-style citations and reference list. No explicit assumptions statement, but that is not part of this descriptor.
> Question 3: "(a) Placing an order needs all four components, so the availabilities multiply:"  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3: No explicit statement of the independence assumption (component failures independent, providers independent); it is implied by the multiplication but the task asks for assumptions to be stated.
- Question 2: 'eight or more services' is an unstated assumption about a hypothetical microservices design; harmless but should be flagged as an assumption.

## Next steps

1. In Q3, add one sentence before the multiplication: 'I assume component failures are independent and the two payment providers fail independently,' then show the same working.
2. In Q2, label 'eight or more services' as an assumption about a hypothetical microservices design, e.g. 'assuming a microservices split into eight or more services...'.
3. Keep the current discipline: every answer within 150 words, headings in order, and IEEE citations; for future ADRs, continue pairing positive and negative consequences as you did in Q6.

---
<sub>Run Input_4_u-Run_2-Eff_low-261118-151012 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8475/10672 | cost $0.006915 (incl. $0.001628 for the reused reference rubric+task structure) | 30.59s</sub>
