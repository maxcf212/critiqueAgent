# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You produced a strong, clearly structured submission, with scenario-specific reasoning in Questions 1, 2, 4, 5 and 6, and correct availability calculations in Question 3. Your work meets the highest rubric level across the criteria. To strengthen it further, make the circuit-breaker timing assumptions explicit and address the risk of losing an outlet notification between payment and event publication.

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

Question 1 selects performance and availability for relevant CampusEats reasons. Both six-part scenarios have measurable response measures, and the lunch-hour load is quantified. To maintain this standard, keep linking each attribute to a specific user or operational need.

*Assessor reasoning:* Performance and availability are justified with scenario details. Both scenarios include all six parts, with measurable response measures. The performance stimulus also quantifies the stated lunch-hour load.
> Question 1: "900 order requests arrive within one hour (about 15 per minute on average)."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering."  

### C2 Q2 Architectural style (6/6, Excellent)

Question 2 gives a clear modular-monolith recommendation, tied to the five-developer team, VM and deployment issues, and 12-month horizon. You also acknowledge scaling and failure-isolation costs. This meets the highest rubric level; preserve that balance of scenario-specific benefits and downside.

*Assessor reasoning:* The recommendation is clear and supported by trade-offs tied to the five-developer team, existing VM and deployment problems, and the 12-month horizon. It acknowledges the monolith’s scaling and failure-isolation downside.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Question 3 shows the series and active-active calculations, with correct results and monthly downtime to the requested precision. Keep showing each calculation step and checking that reported rounding follows the question’s instructions.

*Assessor reasoning:* The series and active-active calculations are correct, with working shown. The resulting availabilities and monthly downtimes are reported to the requested precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Question 4 correctly explains and applies the circuit breaker, including Half-Open trials and tuning trade-offs. Qualify the claim that it opens within seconds: this depends on thresholds and timeouts. Also address resource sharing, since a breaker alone may not keep browsing responsive before it opens.

*Assessor reasoning:* The circuit breaker mechanism is accurately explained and applied to the slow-payment outage, including the effect on browsing. Threshold tuning and loss of payment availability while open are suitable drawbacks. The claim it would open within seconds depends on configuration.
> Question 4: "After a wait it goes Half-Open and lets a few trial calls through; if they succeed it closes, otherwise it reopens."  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded; too lax and threads are exhausted first."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Question 5 justifies availability for cached menu browsing and consistency for payments, uses CAP appropriately, and names concrete techniques including a 60-second cache TTL and idempotency keys. Keep distinguishing the two use cases and explaining how each technique supports its choice.

*Assessor reasoning:* The AP browsing and consistency-favouring payment choices are justified, CAP is applied appropriately to partition behaviour, and concrete techniques are named. Idempotency keys help prevent duplicate charges on retries.
> Question 5: "I would favour availability. If a partition separates an application server from the database, it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page."  
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability; partitions cannot be ruled out in a distributed system, so partition tolerance is not optional."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Question 6 has specific Context, Decision and Consequences, including positive and negative effects and duplicate handling. Strengthen the design by addressing the payment-to-queue dual-write risk: use a transactional outbox or equivalent recovery so a crash cannot lose the outlet notification.

*Assessor reasoning:* The ADR includes specific context, a clear queue decision, and both positive and negative consequences. It also recognizes at-least-once delivery and duplicate handling.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Your answers use the required headings, stay within the word limits, and use clear terminology with IEEE-style citations and a reference list. Continue this concise, well-supported presentation.

*Assessor reasoning:* Answers use the required headings and are concise and clear within the word limits. Numbered in-text citations and a corresponding reference list are provided in IEEE-style format.
> Question 1: "The scenarios use the six-part form from [1]."  
> References: "[2] M. T. Nygard, *Release It! Design and Deploy Production-Ready Software*, 2nd ed. Raleigh, NC, USA: Pragmatic Bookshelf, 2018."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | Question 3; References |

## Technical issues

- Question 4: The claim that the breaker would open within seconds is configuration-dependent; no threshold or timeout values are given. A breaker alone also cannot guarantee browsing remains responsive if payment calls share saturated resources before it opens.
- Question 6: Publishing after payment creates a possible dual-write failure: a crash after payment succeeds but before the event is durably queued can leave the outlet unnotified. A transactional outbox or equivalent recovery mechanism would address this risk.

## Next steps

1. In Question 4, state the breaker’s assumed failure threshold and timeout before predicting when it opens. Also explain how you would prevent slow payment calls from exhausting resources shared with browsing.
2. In Question 6, add a transactional outbox or equivalent recovery mechanism so a crash after payment succeeds cannot leave the outlet without a durable notification.
3. Keep the strengths shown across Questions 1–3 and 5: use measurable scenarios, scenario-specific trade-offs, visible calculation working, and concrete techniques such as the Redis TTL and idempotency keys.

---
<sub>Run Input_4_u-Run_1-Eff_high-261116-140711 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8486/9178 | cost $0.005649 (incl. $0.001628 for the reused reference rubric+task structure) | 65.52s</sub>
