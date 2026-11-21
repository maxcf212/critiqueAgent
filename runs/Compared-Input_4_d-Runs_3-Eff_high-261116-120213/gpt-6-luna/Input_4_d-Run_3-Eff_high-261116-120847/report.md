# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 22 / 40 (55%)**

You made a strong, scenario-specific case for a modular monolith in Q2, and your answers are generally clear and within the word limit. To strengthen the rest, focus on checking calculations, explaining patterns accurately, applying CAP correctly, and making your measures and ADR consequences complete.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 1 / 5 | 1 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

In Q1, you chose relevant attributes and gave a measurable performance target. To reach Excellent, make the availability response measure measurable too, and correct the workload rate: 900 orders per hour is 15 per minute, not 150.

*Assessor reasoning:* Both attributes are relevant and justified, and the performance scenario has a measurable target. The availability measure is not measurable, so the scenarios do not fully meet the Excellent descriptor. The stated average of 150 requests per minute is also incorrect: 900 per hour is 15 per minute.
> Question 1: "The two most important quality attributes are performance and availability, because the business depends on the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your Q2 modular-monolith recommendation is well tailored to the five-person team, the single-VM performance issue, and deployment downtime. You explain scenario-specific trade-offs and acknowledge shared scaling and process-failure risks; maintain this level of specificity.

*Assessor reasoning:* The modular-monolith recommendation is clear and grounded in team size, the single-VM performance problem, and deployment downtime. It gives relevant trade-offs and acknowledges the downside of shared scaling and process failure.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The 20-minute weekly downtime is a deployment process problem and can be removed with rolling deployments."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

In Q3(a), you showed the correct series calculation. For Excellent, correct Q3(b) to about 5.0 hours of monthly downtime and, in Q3(c), multiply payment-provider availability by the other required components; the resulting end-to-end availability is about 99.80%, with about 1.5 hours of monthly downtime.

*Assessor reasoning:* Part (a) is correctly calculated and the working is shown. Part (b) has an arithmetic error: downtime is about 5.0 hours, not 3.5. Part (c) calculates payment-only availability but does not combine it with the other required components; end-to-end availability is about 99.80% and monthly downtime about 1.5 hours.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (1/5, Developing)

In Q4, you chose an appropriate pattern and identified its containment benefit, but reversed the states. Closed allows calls, Open short-circuits them, and Half-Open permits trial calls. Explain how this handles the outage and add a drawback or tuning consideration to reach Excellent.

*Assessor reasoning:* A circuit breaker is appropriate and its intended containment benefit is identified, but the state behavior is reversed: Closed normally permits calls, while Open short-circuits them. The explanation therefore does not correctly describe the pattern. No drawback or explicit tuning consideration is discussed.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "the breaker moves to Closed and calls fail immediately without waiting"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your Q5 choices are reasonable, and the Redis cache with a 60-second TTL is a concrete browsing technique. To reach Excellent, explain that during a partition the system must tolerate the partition and choose between consistency and availability, then name a concrete payment technique.

*Assessor reasoning:* The availability choice for browsing and consistency preference for payment are reasonable, and a concrete cache technique is given for browsing. CAP is misapplied: during a partition, a system must tolerate the partition and choose between consistency and availability. No concrete technique is named for payment.
> Question 5: "it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance, so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Q6 Context, Decision, and Consequences are specific to CampusEats, and you describe benefits of a durable queue. To reach Excellent, add a negative consequence, such as queue operations, delayed delivery, or duplicate notifications requiring idempotent handling.

*Assessor reasoning:* Context, decision, and consequences are present and specific to CampusEats. The consequences describe several benefits, but no negative consequence is included, so the ADR is one-sided.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your answers are clear, use the required headings, and appear within the word limit. To reach Excellent, ensure all sources are listed in IEEE style: Q4 cites reference [2], but there is no corresponding entry in your reference list.

*Assessor reasoning:* The required headings and order are used, the answers are clear, and the responses appear within the word limit. Numeric citations are used, but reference [2] is missing from the reference list. No explicit assumptions are stated.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

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

- Question 1: 900 orders per hour is 15 orders per minute, not 150. The availability response measure, “most of the time,” is not measurable.
- Question 3: The part (b) downtime arithmetic is wrong: (1 − 0.99301) × 720 is about 5.0 hours, not 3.5.
- Question 3: Part (c) reports payment-provider availability as end-to-end availability. Multiplying by the other required components gives about 99.80% end-to-end availability and 1.5 hours of monthly downtime.
- Question 4: Circuit-breaker states are inverted: Closed normally allows calls, Open short-circuits them, and Half-Open permits trial calls.
- Question 5: CAP does not allow a system to give up partition tolerance while a network partition is occurring; the consistency-versus-availability choice applies during that partition.
- Question 6: The ADR lists only positive consequences; it omits a negative consequence such as queue operations, delayed delivery, or duplicate notifications requiring idempotent handling.
- References: Reference [2] is cited in Question 4 but has no corresponding reference-list entry.

## Next steps

1. In Q1 and Q3, check units and show each calculation: 900 orders per hour is 15 per minute, and calculate end-to-end availability by multiplying all required components.
2. In Q4 and Q5, verify the technical mechanisms before applying them: state what each circuit-breaker state does, and explain the consistency–availability choice during a network partition.
3. In Q1, Q6, and References, make the availability target measurable, add a negative ADR consequence, and include a reference-list entry for every cited source.

---
<sub>Run Input_4_d-Run_3-Eff_high-261116-120847 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8490/10714 | cost $0.006044 (incl. $0.001628 for the reused reference rubric+task structure) | 69.48s</sub>
