# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You made a strong, scenario-specific recommendation in Question 2 and showed a sound series-availability method in Question 3(a). To strengthen the rest of the submission, correct the availability arithmetic, explain the circuit-breaker states and CAP trade-off accurately, and make your quality-attribute measures and ADR consequences more complete.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

In Question 1, you chose relevant attributes and linked them to the lunch peak and response time. To reach Excellent, correct the load figure (900 orders/hour is 15/minute, not about 150), complete both six-part scenarios, and replace “stay up most of the time” with a measurable order-placement availability target.

*Assessor reasoning:* Both attributes are relevant and justified using the lunch peak and current response time. The performance scenario has a measurable response measure, but the availability measure is not measurable and its response does not clearly address order placement.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation in Question 2 is well matched to the five-person team and single-VM issue, and you acknowledge shared-process risk and limited independent scaling. You reached Excellent for this criterion; keep these scenario-specific trade-offs while tightening the answer to meet the word limit.

*Assessor reasoning:* Clearly recommends a modular monolith and supports it with scenario-specific trade-offs involving the five-person team, single-VM load issue, and deployment downtime. It also acknowledges the reduced independent scalability and shared-process failure risk.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

In Question 3(a), you used the series method correctly. To reach Proficient, correct the arithmetic in (b) to about 5.0 hours of monthly downtime and in (c) include all components: approximately 99.80% end-to-end availability and 1.5 hours of monthly downtime. Show the working to the requested precision.

*Assessor reasoning:* Part (a) uses the correct series method and gives 99.30%. Part (b) has an arithmetic error: downtime is about 5.0 hours. Part (c) reports provider-pair availability rather than end-to-end availability; including the other components gives about 99.80% and 1.5 hours of monthly downtime.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You identified a relevant circuit breaker and explained fail-fast containment in Question 4. To reach Proficient, correct the sequence: Closed normally allows calls; failures open the breaker; after a wait, Half-open permits probes, with successful probes closing it and failures reopening it. For Excellent, also explain a drawback or tuning consideration.

*Assessor reasoning:* The circuit breaker is appropriate and the fail-fast containment idea is relevant, but the Closed/Open transitions are reversed, as are the stated recovery transitions. No drawback or tuning consideration is given. The threshold example does show some tuning awareness, so this earns partial credit.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your availability choice for menus and use of a cache with a TTL are appropriate. To reach Excellent in Question 5, explain that during a partition CAP requires a consistency-versus-availability trade-off, and name a concrete consistency technique for payments, such as an authoritative transactional ledger with idempotency keys.

*Assessor reasoning:* The menu choice is justified and names a cache with a TTL. Consistency is a reasonable priority for payment, but the CAP explanation is incorrect and no concrete consistency technique is given for payment processing.
> Question 5: "I would favour availability."  
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Question 6 ADR includes scenario-specific Context, Decision and positive consequences, including faster order responses. To reach Excellent, add a negative consequence, such as duplicate notifications from retrying queue delivery, and explain how idempotent consumption can address it.

*Assessor reasoning:* Context, Decision, and Consequences are present and scenario-specific. The consequences describe benefits only; no negative consequence, such as duplicate delivery or added operational complexity, is acknowledged.
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings and writing are clear. To reach Excellent, keep every answer within 150 words, use precise terminology, and ensure all sources are cited in IEEE style. Question 2 exceeds the limit, and citation [2] in Question 4 needs a corresponding entry in the References section.

*Assessor reasoning:* The headings and writing are clear, but Question 2 exceeds the 150-word limit. Numeric citations are used, but citation [2] has no corresponding reference-list entry.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Question 3; References |

## Technical issues

- Question 1: 900 orders per hour is 15 orders per minute on average, not about 150 per minute.
- Question 1: The availability response measure, “stay up most of the time,” is not measurable.
- Question 3: The downtime arithmetic in part (b) is incorrect: the displayed availability yields about 5.0 hours per 30-day month.
- Question 3: Part (c) uses payment-pair availability as end-to-end availability. Multiplying by the other components gives approximately 99.80% availability and 1.5 hours of monthly downtime.
- Question 4: Circuit-breaker states are reversed: Closed normally permits calls; failures open the breaker; successful half-open probes close it.
- Question 5: CAP does not permit choosing consistency and availability while giving up partition tolerance; during a partition a system must trade off consistency and availability.
- Question 6: Retrying queue delivery can produce duplicate notifications; idempotent consumption is a relevant consideration.

## Next steps

1. Revise Question 3(b) and (c): show the monthly downtime calculation clearly, and calculate end-to-end availability using all components rather than only the payment-provider pair.
2. In Questions 4 and 5, correct the circuit-breaker state transitions and explain that during a network partition a system must trade off consistency against availability; give a concrete technique for each case.
3. In Questions 1 and 6, make the availability response measure measurable and add a negative consequence to the ADR. Also bring Question 2 within 150 words and ensure every IEEE citation has a matching reference.

---
<sub>Run Input_4_d-Run_1-Eff_high-261116-120658 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8295/9171 | cost $0.005621 (incl. $0.001628 for the reused reference rubric+task structure) | 57.29s</sub>
