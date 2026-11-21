# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 23 / 40 (57.5%)**

You showed solid architectural reasoning: your Q2 recommendation was excellent, and Q1, Q5 and Q6 were reasonable. The main losses came from Q3 (arithmetic slip and end-to-end availability), a reversed circuit-breaker explanation in Q4, a misstatement of CAP in Q5, and a one-sided ADR. Total: 23/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Developing | 4 / 8 | 4 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

Good choice of performance and availability, justified from the lunch-hour scenario, and your performance scenario was fully six-part and measurable. To reach Excellent, make the availability response measure measurable — e.g. '≤0.2% failed requests per month' instead of 'stay up most of the time'.

*Assessor reasoning:* Suitable attributes (performance, availability) justified from the lunch-hour scenario, and the performance scenario is fully six-part and measurable. However, the availability response measure ('stay up most of the time') is not measurable, so Proficient rather than Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work: a clear modular-monolith recommendation with two trade-offs tied to the five-developer team and the single-VM/deployment problems, and you explicitly acknowledged the downside (no independent scaling, one bug can crash the process). This is the standard to carry into the other answers.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team vs operational overhead; problems traced to single VM and deployment process, not the monolith). The downside of the recommendation is explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (4/8, Developing)

Your method and working were shown and part (a) was correct, but (b) had an arithmetic slip (0.00699 × 720 = 5.0 h, not 3.5 h) and (c) reported the payment-pair availability (99.9975%) instead of end-to-end order-placement availability (≈99.80%, ≈1.5 h). Showing working kept this in Developing; fixing both parts would reach Excellent.

*Assessor reasoning:* Method and working are shown. (a) is correct (0.99301, 99.30%). But (b) is wrong: 0.00699 × 720 = 5.0 hours, not 3.5. In (c) the student reports the payment-pair availability (99.9975%) as the end-to-end availability; the correct end-to-end is ≈99.80% with ≈1.5 h downtime. Two parts incorrect → Developing.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit breaker was an appropriate pattern and you applied it to the outage, but the states were reversed: Open should fail fast and Closed passes calls normally. You also gave no drawback or tuning consideration. Correcting the mechanism and adding, say, a half-open testing note would reach the top level.

*Assessor reasoning:* Circuit breaker is an appropriate pattern and is applied to the outage, but the state machine is reversed (Open should block calls; Closed is normal operation), so the explanation is incorrect. No drawback or tuning consideration is given either.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold... the breaker moves to Closed and calls fail immediately" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both choices (availability for browsing, consistency for payments) were reasonable and you named Redis with TTL for menus. However, CAP was misapplied — you cannot 'give up partition tolerance'; partitions are not optional — and no concrete technique was named for payments (e.g. synchronous two-phase commit or a single writable ledger).

*Assessor reasoning:* Both choices (availability for browsing, consistency for payment) are reasonable and justified; a concrete technique (Redis cache with TTL) is named for menus. But CAP is explained incorrectly (claiming CP+A is possible by 'giving up partition tolerance'), and no concrete technique is named for the payment case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Context, Decision and Consequences were all present and specific to CampusEats, which is good. To reach Excellent, include at least one negative consequence, such as delayed order confirmation during eventual-consistency lag or the added message infrastructure and its operational cost.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (offline tablets, 4.2 s p95, lunch peak). However, all listed consequences are positive; no negative consequence (e.g. eventual notification delay, added infrastructure) is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing was clear and headings were used correctly, but Q2 and Q4 exceeded the 150-word limit and reference [2], cited in Q4, was missing from the reference list. Keep every answer within 150 words and check that every in-text citation appears in the list, in IEEE style.

*Assessor reasoning:* Writing is clear and headings are used in order, but Question 2 and Question 4 exceed 150 words, and citation [2] (cited in Question 4) is missing from the reference list, so the reference list is incomplete.
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*"  

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

- Question 3 (b): 0.00699 × 720 = 5.0 hours, not 3.5 hours.
- Question 3 (c): Reported 99.9975% is the payment-pair availability, not end-to-end order-placement availability (should be ≈99.80%, ≈1.5 h downtime).
- Question 4: Circuit breaker states reversed: Open should fail fast, Closed passes calls normally.
- Question 5: CAP misapplied: cannot have consistency + availability during a partition; partitions are not optional.
- References: Reference [2] cited in Question 4 but absent from the reference list.

## Next steps

1. Redo Q3(b): 0.00699 × 720 = 5.0 hours, and compute end-to-end availability by multiplying component availabilities (≈99.80%, ≈1.5 h downtime), not just the payment pair.
2. Rewrite the circuit breaker state machine: Open = fail fast, Closed = normal operation, and add a drawback or tuning consideration (e.g. threshold/half-open testing).
3. Fix your CAP explanation — you cannot keep consistency and availability during a partition — and name a concrete technique for the payment case.
4. Add at least one negative consequence to your ADR (e.g. delayed order confirmation, extra infrastructure).
5. Trim Q2 and Q4 to 150 words and add the missing reference [2] to your reference list.

---
<sub>Run Input_4_d-Run_3-Eff_low-261118-145618 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8095/5196 | cost $0.002962 (incl. $0.001628 for the reused reference rubric+task structure) | 49.84s</sub>
