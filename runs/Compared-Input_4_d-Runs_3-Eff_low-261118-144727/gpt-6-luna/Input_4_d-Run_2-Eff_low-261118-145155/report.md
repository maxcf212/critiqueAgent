# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 20 / 40 (50%)**

You made a strong, scenario-specific case for a modular monolith in Question 2, linking your recommendation to the five-person team and the single-VM load issue. To strengthen the other answers, focus on measurable quality-attribute responses, accurate availability calculations, and precise explanations of resilience and CAP. Your ADR has a specific context and decision; add a negative consequence to make the trade-offs clear.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Developing | 2 / 6 | 2 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

In Question 1, you chose relevant attributes and linked them to the lunch peak and slow payment provider. To reach the next level, make the availability response measurable and address order placement; check that the performance scenario does not promise accepting every order during a provider outage.

*Assessor reasoning:* Performance and availability are relevant and are justified using the lunch peak and slow payment-provider scenario. Both scenarios include the six parts, but availability's response measure is not measurable, and its response is limited to browsing rather than order placement. The performance scenario also promises every order is accepted, which is not clearly compatible with a payment-provider outage.
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Your Question 2 recommendation is clear and grounded in the five-person team, single-VM load issue, and deployment downtime. You also acknowledge shared scaling and process-failure downsides. Keep this scenario-specific trade-off reasoning, and clarify how your deployment approach addresses downtime.

*Assessor reasoning:* The modular-monolith recommendation is clear and supported by scenario-specific trade-offs involving the five-person team, single-VM load issue, and deployment downtime. It acknowledges the downside of shared scaling and process failure. The proposed rolling deployments do not by themselves establish zero-downtime deployment, but the overall reasoning is strong.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The slow lunchtime responses come from running on a single virtual machine"  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (3/8, Developing)

You used the series-product method and an appropriate redundancy formula. In Question 3(b), the downtime is about 5.0 hours, not 3.5. In (c), include the other components in end-to-end availability: it is about 99.80%, or 1.5 hours of monthly downtime. Show and check each calculation.

*Assessor reasoning:* The series-product method and payment-provider redundancy formula are appropriate, but the downtime calculation in (b) is arithmetically wrong: it is about 5.0 hours. In (c), the redundant payment availability is not the end-to-end availability; the other three components must still be included. Correct end-to-end availability is about 99.80%, with about 1.5 hours of monthly downtime.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You selected an appropriate circuit-breaker pattern, applied it to the slow-provider outage, and gave a tuning example. In Question 4, correct the states: Closed permits normal calls, Open fails fast, and Half-Open admits trial calls. Explain how the corrected sequence limits impact and recovery.

*Assessor reasoning:* Circuit breaker is an appropriate pattern and the answer applies it to the slow-provider outage and gives a tuning example. However, its states are reversed: Closed normally permits calls, Open rejects or fails fast, and Half-Open allows trial calls. The incorrect mechanism undermines the explanation.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (2/6, Developing)

Your menu choice in Question 5 is reasonable and includes a cache with a TTL. CAP does not allow choosing consistency and availability while giving up partition tolerance during a partition; explain the consistency/availability trade-off under partition, and name a concrete technique for payment consistency.

*Assessor reasoning:* The menu choice is reasonable and names a cache with a TTL, but the payment choice has no concrete technique. CAP is misstated: under a network partition, a distributed system must trade off consistency and availability while tolerating the partition; it cannot simply give up partition tolerance. The answer does not explain how payment behavior handles a partition.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "I would favour consistency"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Question 6 context and decision are specific, and you identify benefits such as smoothing the lunch peak. To reach the next level, add a negative consequence, such as delayed notifications, duplicate-delivery handling, or queue operations, and explain its relevance.

*Assessor reasoning:* Context and decision are specific, and the consequences describe several benefits. No negative consequence is stated, so the ADR is one-sided and fits the proficient level. It would also be useful to address delivery guarantees, duplicate events, or eventual notification delay.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (2/4, Developing)

Your headings and clear, concise writing support the response. Citation [2] in Question 4 has no matching reference. Complete the reference list and state assumptions so your citations and format meet the requirements.

*Assessor reasoning:* The required headings are used, writing is generally clear, and answers appear within the word limit. However, citation [2] has no corresponding reference, and no assumptions are stated. The reference list is incomplete, so the citation and format requirements are not met.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | no | - |

## Technical issues

- Question 3: Part (b): (1 - 0.99301) × 720 is approximately 5.0 hours, not 3.5 hours.
- Question 3: Part (c) reports payment availability as end-to-end availability. Multiplying 0.999975 by the other component availabilities gives approximately 99.80% end-to-end availability and 1.5 hours of monthly downtime.
- Question 4: Circuit-breaker states are reversed: Closed permits normal calls, Open fails fast, and Half-Open admits trial calls.
- Question 5: CAP does not permit choosing consistency and availability while giving up partition tolerance during a partition; the consistency/availability trade-off applies when a partition occurs.
- Question 5: No concrete technique is given for the order-and-payment consistency choice.
- Question 6: The ADR omits negative consequences, such as eventual notification, duplicate delivery handling, or queue operations.
- References: Citation [2] is used in Question 4 but no corresponding reference is listed.

## Next steps

1. In Question 1, make both response measures measurable. For availability, specify a target and ensure the scenario covers placing orders, not only browsing; check that the performance response remains realistic during a payment-provider outage.
2. In Question 3, show each calculation and verify the arithmetic: part (b) is about 5.0 hours; in part (c), multiply redundant payment availability by the other component availabilities to find end-to-end availability, then calculate downtime.
3. In Questions 4–6, correct the circuit-breaker state sequence, explain CAP’s consistency/availability trade-off during a partition and name a payment-consistency technique. Add a negative consequence to the ADR and complete the references and assumptions.

---
<sub>Run Input_4_d-Run_2-Eff_low-261118-145155 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8434/5834 | cost $0.003597 (incl. $0.001628 for the reused reference rubric+task structure) | 30.51s</sub>
