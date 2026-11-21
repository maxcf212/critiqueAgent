# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You have a solid grasp of architectural reasoning, especially in Question 2, where your recommendation is well argued and tied to CampusEats' team size and known deployment problems. Your main losses come from Question 3 arithmetic and the payment availability figure, inverted circuit-breaker states in Question 4, and CAP being misapplied in Question 5. Tightening these areas and the formal requirements will lift your mark considerably.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose two attributes that matter most for CampusEats and justified them from the scenario, including the 4.2 s p95 ordering latency, which is a strong, specific link. Both scenarios are in six-part form. The availability response measure, however, says the system should stay up most of the time, which is not measurable. Give a specific target such as 99.5% over a month to reach the top level.

*Assessor reasoning:* Attributes are well chosen and justified from the scenario, and both scenarios have all six parts. However, the availability response measure is vague and not measurable, which caps it at Proficient.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "the current p95 of 4.2 s for placing an order makes students abandon their orders"  

### C2 Q2 Architectural style (6/6, Excellent)

This is an excellent answer. You recommend a clear style and justify it with two trade-offs specific to CampusEats: the operational overhead for a five-person team and the known problems from the single VM and deployment process. You also state the downside you accept, namely that modules cannot scale independently. Keep this standard in future answers.

*Assessor reasoning:* Clear recommendation with two scenario-specific trade-offs (team size/operational overhead, known problems caused by single VM and deployment process) and an explicit acknowledged downside.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct at 0.99301 (99.30%), and your working is shown. In part (b), 0.00699 × 720 gives about 5.0 hours, not 3.5 hours, so recheck that multiplication. In part (c), the end-to-end availability should multiply all four component availabilities, giving about 99.80% and roughly 1.5 hours of downtime a month. Your 99.9975% reflects only the payment service.

*Assessor reasoning:* (a) is correct (0.99301, 99.30%). (b) has an arithmetic slip: 0.00699 x 720 = 5.0 h, not 3.5 h. (c) wrongly gives payment availability as the end-to-end figure; correct answer 99.80% (~1.5 h/month). Working is shown, so Developing.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Choosing the circuit breaker is appropriate and you apply it sensibly to the outage. However, the states are inverted: Closed should pass calls through, and Open should fail fast. Your Half-Open description is correct. Add a clear drawback or tuning consideration, such as choosing failure thresholds and reset timeouts, to reach the top level.

*Assessor reasoning:* Circuit breaker is the right pattern and is applied well to the outage, but the Open/Closed states are inverted, a significant explanatory error. No explicit drawback or tuning consideration is stated beyond an example threshold.
> Question 4: "the breaker moves to Closed and calls fail immediately without waiting"  
> Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your menu-browsing choice with a Redis TTL cache is correct and well reasoned. For payments, your instinct to favour consistency is directionally right, but CAP is misapplied: in a partitioned system you must trade availability against consistency, not give up partition tolerance. Also name a concrete technique for payment consistency, such as idempotency keys, two-phase commit or a saga.

*Assessor reasoning:* Menu browsing choice plus Redis TTL technique is correct. The payment choice favours consistency, which is directionally right, but CAP is misapplied (you cannot give up partition tolerance) and no concrete technique is named for the payment case.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your record has clear Context, Decision and Consequences sections, all specific to CampusEats, and the consequences describe the queue's benefits well. It lacks any negative consequence. Add one, for example the added operational cost of the queue, the need to handle duplicate messages, or eventual consistency of order status.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats. Consequences are entirely positive; no negative consequence (e.g. eventual consistency, duplicate handling, queue operational cost) is given.
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  
> Question 6: "If a tablet is offline the order is lost, and during the lunch peak these calls add to the 4.2 s p95 response time."  

### C7 Communication and format (2/4, Developing)

Your writing is generally clear and your terminology is mostly precise. Questions 2 and 4 exceed the 150-word limit, and Question 1 is borderline. Reference [2] is cited but missing from the reference list, and the availability figures should be given consistently to two decimal places. Trim your answers and complete the reference list in IEEE style.

*Assessor reasoning:* Questions 2 and 4 clearly exceed 150 words; Q1 is borderline. Reference [2] is cited in Q4 but absent from the reference list. Availability figures are not consistently given to two decimal places as required.
> Question 2: "Microservices let each service scale and deploy independently, but every service needs its own pipeline, monitoring and on-call knowledge."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | no | References |

## Technical issues

- Question 3: Downtime arithmetic: 0.00699 x 720 = 5.03 h, not 3.5 h (should be 5.0 h to one decimal place).
- Question 3: Part (c) reports 99.9975% — the payment-only figure. End-to-end availability is 0.9995 x 0.999 x 0.9995 x 0.999975 = 99.80%, downtime ~1.5 h/month.
- Question 4: Circuit breaker states inverted: Closed should pass calls; Open should fail fast. Half-open description is correct.
- Question 5: CAP misapplied — a partitioned distributed system must sacrifice availability or consistency, not partition tolerance; unavailable payment provider is not a partition anyway.
- Question 5: No concrete consistency technique named for payments (e.g. idempotency keys, two-phase commit, saga).
- Question 1: Availability response measure not measurable; peak load of 150 orders/min is stated but not tied to a capacity measure beyond latency.
- References: Reference [2] cited but missing from the reference list; no assumptions section as required.

## Next steps

1. Recheck Question 3: multiply the downtime fraction by 720 hours carefully, and calculate end-to-end availability by multiplying all component availabilities, not reporting the payment figure alone.
2. Revisit circuit breaker states: Closed passes calls through, Open fails fast, and Half-Open probes recovery. Also apply CAP correctly, remembering partition tolerance is not optional in distributed systems, and name a concrete consistency technique such as idempotency keys or a saga for payments.
3. Add a negative consequence to your Question 6 decision record, cite every reference used (including [2]) in the reference list, and keep each answer within 150 words with an assumptions section.

---
<sub>Run Input_4_d-Run_2-Eff_low-261118-145322 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11658/5996 | cost $0.00422 (incl. $0.001628 for the reused reference rubric+task structure) | 30.53s</sub>
