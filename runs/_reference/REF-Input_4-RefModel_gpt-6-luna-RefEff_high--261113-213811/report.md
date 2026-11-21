# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You show strong, scenario-specific architectural reasoning, especially in Q2’s modular-monolith trade-offs and Q4’s circuit-breaker explanation. To strengthen the remaining answers, make both Q1 response measures measurable, complete the end-to-end calculation in Q3, explain the CAP trade-off accurately in Q5, and include a negative consequence in Q6. Your concise format and IEEE-like references are good foundations.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

In Q1, your performance scenario is measurable and both scenarios include the six parts. “Stay up most of the time” is not measurable; give availability a numeric target. To reach Excellent, both scenarios need complete parts and measurable response measures.

*Assessor reasoning:* Performance and availability are appropriate choices and are linked to the lunch peak and order abandonment. Both scenarios include the six parts, and the performance measure is measurable. The availability response measure is not measurable, so the scenarios are not fully complete to the Excellent standard.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your Q2 modular-monolith recommendation is clearly linked to the five-person team and single-VM bottleneck. You explain trade-offs and acknowledge shared failure risk and reduced independent scaling. This meets Excellent; keep grounding both benefits and downsides in CampusEats.

*Assessor reasoning:* The modular-monolith recommendation is clear and grounded in team size, the single-VM bottleneck, and deployment downtime. It gives specific trade-offs and acknowledges the reduced independent scaling and shared process-failure risk.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Your Q3(a) and (b) are correct. In (c), you calculate redundant payment availability but report it as end-to-end order availability. Include the other components; the result is about 99.80% availability and 1.5 hours of monthly downtime. Excellent requires all parts correct, with working and requested precision.

*Assessor reasoning:* Parts (a) and (b) are calculated correctly. In (c), the redundant payment availability is correct, but the other required components are omitted from the end-to-end calculation, making both the stated order-placement availability and downtime incorrect.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Your Q4 circuit-breaker mechanism and states are explained correctly and applied to the slow-provider outage. The threshold and time window show a useful tuning consideration. This meets Excellent; retain the clear explanation of how the breaker protects other functions.

*Assessor reasoning:* The circuit breaker mechanism and states are explained correctly and applied to the slow-provider outage. The threshold and time window provide a tuning consideration, and the answer explains how the pattern protects other application functions.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open and calls fail immediately without waiting"  
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your Q5 choices and techniques are reasonable, including menu caching and payment idempotency keys. Correct the CAP explanation: during a network partition, partition tolerance is the condition experienced, and the system trades consistency against availability. Excellent requires accurate CAP reasoning and a suitable technique for each case.

*Assessor reasoning:* Both choices are reasonable and concrete techniques are named: a cached menu and payment idempotency keys. However, the CAP explanation is incorrect for a network partition: a system cannot choose to give up partition tolerance when the partition occurs; it must trade off consistency versus availability.
> Question 5: "The worst case is that a student sees an item that sold out a minute ago"  
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Q6 includes scenario-specific Context, Decision and Consequences. The consequences are positive only. Add a negative consequence—such as delayed or duplicate outlet notifications—and a response to duplicates. Excellent requires all three specific sections and at least one positive and one negative consequence.

*Assessor reasoning:* Context, Decision, and Consequences are present and specific to CampusEats. The consequences are positive only; a negative consequence such as delayed outlet notification, queue operations, or duplicate deliveries is not stated.
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings, concise answers and IEEE-like citations are effective. Q3’s reported availability and downtime do not use the requested precision. For Excellent, keep every answer within 150 words, use precise terminology and calculations, and retain the required headings and IEEE-style citations.

*Assessor reasoning:* The required headings and order are used, the answers are concise, and citations and a reference list are provided in an IEEE-like style. The reported part (c) availability and downtime do not follow the required two-decimal and one-decimal precision, respectively.
> Question 3: "0.018 hours, or about one minute per month."  
> References: "[1] L. Bass, P. Clements, and R. Kazman"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | Question 3; References |

## Technical issues

- Question 1: The availability response measure, “stay up most of the time,” is not measurable.
- Question 3: Part (c) reports payment-subsystem availability as end-to-end order-placement availability. Multiplying the redundant payment availability by the other component availabilities gives approximately 99.80% end-to-end availability and 1.5 hours of monthly downtime.
- Question 5: Under a network partition, partition tolerance is the condition being experienced; the system must trade off consistency against availability rather than choose to give up partition tolerance.
- Question 6: Retrying queued notifications until acknowledged can produce duplicate deliveries; the ADR does not mention deduplication or this as a negative consequence.

## Next steps

1. In Q1, replace “stay up most of the time” with a measurable availability target. In Q3(c), multiply the redundant payment availability by the other component availabilities; report approximately 99.80% end-to-end availability and 1.5 hours of monthly downtime, using the requested precision.
2. In Q5, explain that a network partition is the condition the system must tolerate, so the choice is between consistency and availability during the partition. Keep your concrete techniques, such as a cached menu and payment idempotency keys, tied to the two cases.
3. In Q6, add a specific negative consequence of queued notifications, such as delayed outlet notification or duplicate delivery, and state how you would address duplicates. For the next communication level, also ensure every answer meets the word limit and calculations use the requested precision.

---
<sub>Run REF-Input_4-RefModel_gpt-6-luna-RefEff_high--261113-213811 | rubric=openai/gpt-6-luna, task=openai/gpt-6-luna, marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8263/10191 | cost $0.006127 | 111.13s</sub>
