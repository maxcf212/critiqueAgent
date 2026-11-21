# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You made sensible attribute choices and gave a strong, scenario-specific modular-monolith recommendation in Q2. However, Q3 has an arithmetic slip and an incorrect end-to-end calculation, Q4's circuit breaker states are inverted, Q5 misapplies CAP, and your ADR lacks a negative consequence. Fixing these method-level errors would lift several criteria to the next level.

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

Your performance and availability attributes are well justified from the lunch-hour scenario, and the performance scenario has all six parts with measurable response measures. To reach Excellent, make the availability measure measurable too — 'stay up most of the time' should become something like 'no more than 5 minutes of downtime per month' or a specific uptime percentage.

*Assessor reasoning:* Performance and availability are well justified from the lunch-hour scenario, and the performance scenario has all six parts with measurable measures. However, the availability response measure ('stay up most of the time') is not measurable, placing this in Proficient.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work. Your modular-monolith recommendation is justified by two trade-offs tied to the scenario — the five-developer team's infrastructure overhead and the insight that the root causes are the single VM and deployment process, not the monolith — and you explicitly acknowledge the downside. This meets the Excellent standard; keep applying this scenario-specific reasoning style elsewhere.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team overhead; root causes are single VM and deployment process, not the monolith) and the downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct (99.30%). Part (b) has an arithmetic slip: 0.00699 × 720 is about 5.03 hours, not 3.5. Part (c) reports the payment-pair availability (99.9975%) as end-to-end; the correct end-to-end is 0.99800125 × 0.999975 ≈ 99.80%, or roughly 1.5 hours of downtime. Your method is sound, so careful checking of each part would move you up.

*Assessor reasoning:* Part (a) is correct (0.99301 → 99.30%). Part (b) has an arithmetic slip: 0.00699 × 720 = 5.0 h, not 3.5 h. Part (c) is incorrect: 99.9975% is only the payment subsystem availability; end-to-end should be 0.99800125 × 0.999975 ≈ 99.80%, downtime ≈ 1.5 h. Two parts wrong, so Developing despite correct method.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

The Circuit Breaker is an appropriate pattern and you applied it to the outage, but the state machine is inverted: Closed should pass calls normally, Open should fail fast, and a successful Half-Open probe should close the breaker, not open it. Correct the mechanism and add a drawback or tuning consideration (e.g., threshold or reset timeout) to reach Excellent.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and is applied to the outage, but the state machine is explained backwards: Closed should pass calls normally and Open should fail fast; also 'if they succeed it opens again' is inverted. The mechanism is incorrect, so Developing.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold... the breaker moves to Closed and calls fail immediately" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both consistency/availability choices are reasonable and you named a concrete technique for menu browsing (Redis with a 60-second TTL). However, CAP is misapplied: during a partition you cannot 'give up partition tolerance' — you must trade consistency against availability. Name a concrete technique for the payment path (e.g., synchronous replication or a quorum write) to reach Excellent.

*Assessor reasoning:* Both choices are reasonable and a concrete technique (Redis TTL cache) is named for menu browsing, but none is named for payments. The CAP use is incorrect: during a partition you cannot 'give up partition tolerance'; you must trade C against A.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has all three sections and is specific to CampusEats, with good use of the offline tablets, 4.2 s p95 and lunch-peak details. To reach Excellent, add at least one negative consequence — for example, delayed order notifications, the need for duplicate-order handling, or the operational burden of running the queue.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (offline tablets, 4.2 s p95, lunch peak). However, only positive consequences are given; no negative consequence (e.g., eventual notification delay, duplicate handling, queue operation burden) is stated.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear and headings are used correctly. Two issues hold you at Proficient: Question 2 exceeds the 150-word limit (roughly 200 words), and source [2] is cited in Question 4 but missing from your reference list, which contains only [1]. Trim Q2 and complete the IEEE reference list to reach Excellent.

*Assessor reasoning:* Writing is clear and headings are used, but Question 2 clearly exceeds 150 words (~200), and [2] is cited in Question 4 yet is missing from the reference list, which contains only [1].
> Question 2: "A rewrite would freeze feature work for months without directly fixing either problem."  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

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

- Question 3 (b): Arithmetic error: 0.00699 × 720 = 5.03 hours, not 3.5 hours.
- Question 3 (c): Reports payment-pair availability (99.9975%) as end-to-end; correct end-to-end is 0.99800125 × 0.999975 ≈ 99.80%, downtime ≈ 1.5 h/month. Also exceeds the two-decimal percentage format.
- Question 4: Circuit breaker states are inverted: Open should fail fast and Closed pass normally; Half-Open success should transition to Closed, not Open.
- Question 5: CAP theorem misapplied: 'give up partition tolerance' is not a valid option during a partition; no concrete technique named for the payment path.
- References: Source [2] cited in Question 4 but absent from the reference list.
- Question 1: Availability response measure is not measurable.

## Next steps

1. Redo Q3(b) and (c): check 0.00699 × 720, then multiply the order-path and payment-pair availabilities for the true end-to-end figure, showing all working to two decimals.
2. Rewrite the circuit breaker state machine so Closed passes calls normally, Open fails fast, and Half-Open success returns to Closed; add a tuning consideration such as threshold or timeout values.
3. Revisit CAP: during a partition you must trade consistency against availability, so pick one for payments and name a concrete technique (e.g., synchronous replication or a write quorum), and add a negative consequence to your ADR.

---
<sub>Run Input_4_d-Run_1-Eff_high-261116-121238 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8297/6826 | cost $0.003472 (incl. $0.001628 for the reused reference rubric+task structure) | 84.18s</sub>
