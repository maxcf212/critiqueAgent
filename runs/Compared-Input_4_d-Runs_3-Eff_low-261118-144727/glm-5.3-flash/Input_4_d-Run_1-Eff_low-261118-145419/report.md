# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 26 / 40 (65%)**

You showed strong scenario-specific reasoning in Q2 (excellent trade-offs) and good structure in Q1, Q3 and Q6. To lift your mark, fix the arithmetic slip in Q3(b), correct the reversed circuit breaker states in Q4, apply CAP correctly and name a payment-path technique in Q5, add a negative consequence to your ADR, and tighten word limits and referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 | 6 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Good choice of performance and availability with scenario-based justification, and a fully six-part, measurable performance scenario. To reach Excellent, make the availability response measure measurable — 'stay up most of the time' is not; try a percentage uptime or downtime figure per month.

*Assessor reasoning:* Performance and availability are well justified from the scenario and the performance scenario is fully six-part and measurable. However, the availability response measure ('stay up most of the time') is not measurable, so not Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work: a clear modular monolith recommendation with two trade-offs tied to the scenario (five developers, single VM, 20-minute deployment downtime) and the downside explicitly acknowledged. Keep this standard.

*Assessor reasoning:* Clear recommendation (modular monolith) with two trade-offs tied to scenario specifics (five developers, single VM, 20-minute deployment downtime), and the downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (6/8, Proficient)

Your method was correct throughout and parts (a) and (c) were right, but one arithmetic slip in (b) — 0.00699 × 720 is 5.0 hours, not 3.5 — kept you at Proficient. Show working and recheck calculations to reach Excellent.

*Assessor reasoning:* Method correct throughout; series product 0.99301 and part (c) (0.999975, 0.018 h) are right. But 0.00699 × 720 = 5.0 hours, not 3.5 — one arithmetic slip, so Proficient.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  

### C4 Q4 Resilience pattern (2/5, Developing)

The circuit breaker was an appropriate choice and well applied to the outage, but the state machine was reversed: Closed passes calls normally and Open fails fast. Correcting this core explanation, while keeping your tuning discussion, would reach Excellent.

*Assessor reasoning:* Circuit breaker is an appropriate pattern and application to the outage is good, but the state machine is reversed: Closed = normal flow, Open = fail fast. The core explanation is incorrect, so Developing despite tuning discussion.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold... the breaker moves to Closed and calls fail immediately" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both consistency/availability choices were reasonable and you named Redis with TTL for menu browsing, but CAP was misapplied — partition tolerance cannot be given up; partitions are a fact you must respond to. Also name a concrete technique for the payment path.

*Assessor reasoning:* Both choices are reasonable and a concrete technique (Redis cache with TTL) is named for menu browsing, but CAP is misused (P cannot be sacrificed; partitions are a fact) and no concrete technique is named for the payment case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Context, Decision and Consequences were all present and scenario-specific, but your consequences were entirely positive. Adding a genuine negative consequence (e.g. delayed order confirmation or added message infrastructure) would reach Excellent.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to the scenario, but consequences are entirely positive — no negative consequence (e.g. eventual notification delay, added infrastructure) is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your writing is clear and headings are correct, but Q2 and Q4 exceed the 150-word limit and reference [2], cited in Q4, is missing from your reference list. Trimming answers and completing citations in IEEE style would lift this criterion.

*Assessor reasoning:* Questions 2 and 4 clearly exceed 150 words. Reference [2] is cited in Question 4 but missing from the reference list, which contains only one entry. Writing itself is clear and headings are correct.
> Question 2: "A rewrite would freeze feature work for months without directly fixing either problem."  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3(b): 0.00699 × 720 = 5.0 hours, not 3.5 hours; arithmetic error.
- Question 4: Circuit breaker states reversed: Open should fail fast, Closed passes calls normally.
- Question 5: CAP theorem misapplied — partition tolerance cannot be given up; also no concrete technique named for the payment path.
- References: Citation [2] (cited in Q4) is missing from the reference list.

## Next steps

1. Redo Q3(b): 0.00699 × 720 = 5.0 hours, not 3.5; double-check all arithmetic before submitting.
2. Rewrite your Q4 circuit breaker explanation: Closed passes calls normally; Open fails fast; Half-Open probes recovery.
3. In Q5, explain that partition tolerance cannot be sacrificed, and name a concrete technique (e.g. synchronous replication or a transactional ledger) for the payment path.
4. Add at least one negative consequence to your Q6 ADR and make the Q1 availability response measure measurable (e.g. '99.5% uptime per month').
5. Trim Q2 and Q4 to 150 words each and add the missing reference [2] to your reference list.

---
<sub>Run Input_4_d-Run_1-Eff_low-261118-145419 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 7983/4770 | cost $0.002823 (incl. $0.001628 for the reused reference rubric+task structure) | 50.45s</sub>
