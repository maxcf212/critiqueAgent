# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You produced well-structured, scenario-specific answers, with strong work in Q1, Q2 and Q6. The main losses came from Q3 (an arithmetic slip and an end-to-end availability calculation that omitted the other components), Q4 (circuit-breaker states reversed), Q5 (CAP misapplied, no payment technique), and an incomplete reference list. Overall: 24/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Good choice of performance and availability, with the performance scenario fully six-part and a measurable p95 response measure. To reach Excellent, make the availability response measure measurable too — replace 'stay up most of the time' with a figure such as 'no more than X minutes of downtime per month'.

*Assessor reasoning:* Performance and availability are well justified from the lunch-hour scenario. The performance scenario has all six parts with a measurable response measure, but the availability scenario's response measure ('stay up most of the time') is not measurable.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work: a clear modular-monolith recommendation with scenario-specific trade-offs (five-developer team, root causes in the single VM and deployment process) and the downside acknowledged. For a full 6, frame both arguments as genuine trade-offs rather than root-cause analysis.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team, root causes being single VM and deployment process) and the downside explicitly acknowledged. Not a full 6 because the second argument is root-cause analysis rather than a true trade-off.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct (99.30%). Part (b) has an arithmetic slip: 0.00699 × 720 = 5.0 hours, not 3.5. Part (c) reports payment-only availability (99.9975%); end-to-end must include the other three components: 0.99800125 × 0.999975 ≈ 99.80%, about 1.5 hours of downtime. Show all working and use two decimal places.

*Assessor reasoning:* Part (a) is correct (0.99301 → 99.30%). Part (b) has an arithmetic slip: 0.00699 × 720 = 5.0 h, not 3.5 h. Part (c) is incorrect: 99.9975% is only the payment subsystem; end-to-end should be 0.99800125 × 0.999975 ≈ 99.80%, downtime ≈ 1.5 h. Two parts wrong, so Developing despite correct method.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit Breaker is an appropriate pattern and you applied it to the outage with a tuning threshold, but the states are reversed: Closed passes calls normally, Open fails fast, and a successful Half-Open probe transitions to Closed. Correct the mechanism and keep your drawback/tuning discussion to reach Excellent.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and is applied to the outage with a tuning threshold, but the mechanism is explained incorrectly: the states are reversed (Closed should pass calls normally, Open should fail fast, and Half-Open success should move to Closed, not Open).
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold... the breaker moves to Closed and calls fail immediately" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both choices (availability for browsing, consistency for payments) are reasonable, and the Redis TTL cache is a good concrete technique. However, CAP is misapplied: partition tolerance cannot be given up in a distributed system — during a partition you choose between consistency and availability. Also name a concrete technique for payments.

*Assessor reasoning:* Both choices (availability for browsing, consistency for payment) are reasonable and justified; a concrete technique (Redis TTL cache) is named for menu browsing but none for payments. The CAP use is incorrect: partition tolerance cannot be surrendered in a distributed system; during a partition one chooses C or A.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "for example Redis with a 60-second TTL"  

### C6 Q6 Architecture decision record (4/5, Proficient)

All three ADR sections are present and specific to CampusEats (4.2 s p95, offline tablets, RabbitMQ), which is good. To reach Excellent, add at least one negative consequence, such as delayed outlet notification, added infrastructure to operate, or the need to handle duplicate orders.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (4.2 s p95, offline tablets, RabbitMQ). However, the consequences are entirely positive; no negative consequence (e.g., eventual notification delay, added infrastructure, duplicate handling) is given, so not Excellent.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear and headings are used correctly, but Q2 exceeds the 150-word limit (~185 words) and Q4 is borderline. Reference [2] is cited in Q4 but missing from your reference list, which contains only [1]. Complete the list and state assumptions explicitly.

*Assessor reasoning:* Writing is clear and headings are used in order, but Question 2 exceeds 150 words (~185) and Question 4 is borderline. Citation [2] is used in Question 4 but is missing from the reference list, which contains only [1].
> Question 2: "A rewrite would freeze feature work for months without directly fixing either problem."  
> References: "[1] L. Bass, P. Clements, and R. Kazman"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 – (a) correct; (b) arithmetic error; (c) end-to-end availability not combined with other components |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 – pattern named and applied but state machine explained incorrectly |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 – CAP misapplied; no concrete technique for payments |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 – all sections present but no negative consequence |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References – [2] cited in text but absent from reference list; assumptions only implicitly stated |

## Technical issues

- Question 3 (b): 0.00699 × 720 = 5.0 hours, not 3.5 hours.
- Question 3 (c): End-to-end availability must include the other three components: 0.99800125 × 0.999975 ≈ 99.80%, downtime ≈ 1.5 h/month; 99.9975% is payment-only. Also exceeds the two-decimal-place format.
- Question 4: Circuit breaker states are reversed: Closed passes calls normally, Open fails fast, and Half-Open success transitions to Closed.
- Question 5: CAP theorem misstated: partition tolerance cannot be given up in a distributed system; the choice under partition is between consistency and availability.
- Question 6: No negative consequence provided as required.
- References: Reference [2] is cited in Question 4 but missing from the reference list.

## Next steps

1. Redo Q3(b) and (c): check 0.00699 × 720, then multiply the payment subsystem availability by the other three components to get end-to-end availability, and round to two decimal places.
2. Rewrite your Q4 state machine so Closed passes calls, Open fails fast, and a successful Half-Open probe returns the breaker to Closed.
3. Fix your CAP statement in Q5 (partition tolerance is unavoidable; you choose between consistency and availability during a partition) and name a concrete technique for payments.
4. Add reference [2] to your reference list and trim Q2 to within 150 words.

---
<sub>Run Input_4_d-Run_3-Eff_high-261116-121500 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8415/6801 | cost $0.003241 (incl. $0.001628 for the reused reference rubric+task structure) | 53.5s</sub>
