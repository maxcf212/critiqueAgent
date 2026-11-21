# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 25 / 40 (62.5%)**

You scored 25/40. Q2 is excellent: a clear modular-monolith recommendation with scenario-specific trade-offs and an acknowledged downside. Q1, Q4, Q5 and Q6 are proficient; Q3 and communication need work. Focus next on correcting the availability arithmetic, circuit-breaker state semantics, CAP application, and adding a negative ADR consequence.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Proficient | 3 / 5 | 3 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You justified performance and availability from the lunch-hour scenario, and your performance scenario has all six parts with a measurable measure. To reach Excellent, make the availability response measure measurable (e.g. 99.9% monthly uptime) and justify availability explicitly from the scenario, not implicitly.

*Assessor reasoning:* Two suitable attributes justified from the scenario; the performance scenario has all six parts with a measurable measure. The availability scenario's response measure ('stay up most of the time') is not measurable, and availability is justified only implicitly.
> Question 1: "The two most important quality attributes are performance and availability, because the business depends on the lunch hour"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work: you recommended a modular monolith and tied trade-offs to the five-developer team, single-VM latency and deployment downtime, and you acknowledged the downside (no independent scaling, whole-process crashes). This is exactly the scenario-specific trade-off reasoning the top level requires; keep this pattern.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team, single-VM latency, deployment downtime) and an explicit acknowledged downside.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

You showed working and got part (a) right (99.30%). In (b), 0.00699×720 is 5.03 h, not 3.5 h. In (c), 99.9975% is only the payment provider; end-to-end availability is 0.9995×0.999×0.9995×0.999975 ≈ 99.80%, about 1.5 h/month. To reach Proficient/Excellent, correct these two parts and keep showing each step.

*Assessor reasoning:* (a) correct (99.30%). (b) arithmetic wrong: 0.00699×720 = 5.03 h, not 3.5 h. (c) 99.9975% is only the payment availability; the end-to-end figure should be ~99.80% with ~1.5 h downtime. Two parts incorrect, though method and working are shown.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (3/5, Proficient)

You chose an appropriate pattern and applied it well to the outage, including the student-facing fallback message. However, your Open/Closed semantics are inverted: Closed should pass calls and Open should fail fast, with the threshold tripping Closed→Open. To reach Excellent, correct the states and add a drawback or tuning consideration (e.g. threshold choice, half-open probing).

*Assessor reasoning:* Appropriate pattern, well applied to the outage, but the Open/Closed state semantics are inverted (a real error), and no drawback or tuning consideration is discussed beyond quoting a threshold.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold ... the breaker moves to Closed" *(quote not found in submission)*  
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable and your Redis TTL cache for menus is concrete. But CAP is misapplied: partition tolerance is not optional; during a partition you sacrifice C or A. You also name no concrete technique for payments. To reach Excellent, correct the CAP explanation and name a payment technique (e.g. idempotency keys, saga/2PC).

*Assessor reasoning:* Both choices are reasonable and the menu technique (Redis TTL cache) is concrete. However CAP is misused (partition tolerance cannot be given up; you trade C against A during a partition) and no concrete technique is named for the payment case.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has Context, Decision and Consequences and is specific to CampusEats. The consequences are entirely positive, though. To reach Excellent, add at least one negative consequence (e.g. eventual consistency, duplicate notifications, queue operations) alongside the positive response-time gain.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats, but the consequences are entirely positive — no negative consequence (e.g. eventual consistency, duplicate notifications, queue operations) is given.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your writing is clear and headings are used, but Q1 (~160) and Q2 (~185) exceed 150 words, reference [2] is cited in Q4 but missing from the list, and assumptions are not stated. To reach Proficient/Excellent, trim each answer to ≤150 words, complete the reference list in IEEE style, and state assumptions.

*Assessor reasoning:* Q1 (~160) and Q2 (~185) exceed the 150-word limit, and reference [2] is cited but absent from the reference list; assumptions are never stated. Writing itself is clear and headings are used.
> Question 2: "Second, the known problems are not caused by the monolith itself."  
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

- Question 3(b): 0.00699 × 720 = 5.03 hours, not 3.5 hours; downtime should be ~5.0 h/month.
- Question 3(c): 99.9975% is the payment-provider availability only; end-to-end availability is 0.9995×0.999×0.9995×0.999975 ≈ 99.80%, giving ~1.5 h/month downtime, not 0.018 h.
- Question 4: Circuit breaker states inverted: Open should fail fast and Closed should pass calls; the threshold should trip Closed→Open.
- Question 5: CAP misapplied: partition tolerance is not optional; during a partition one must sacrifice C or A. No concrete consistency technique (e.g. idempotency keys, 2PC/saga) named for payments.
- Question 6: No negative consequence recorded in the ADR.
- References: Reference [2] cited in Q4 but missing from the reference list; no assumptions stated.
- Question 1: Availability response measure is not measurable ('stay up most of the time').

## Next steps

1. Re-work Q3(b) and Q3(c): recompute downtime as (1−availability)×720 and multiply all component availabilities for end-to-end availability; show each step.
2. Correct Q4's circuit-breaker states: Closed passes calls, Open fails fast; describe the threshold trip Closed→Open and add a tuning or drawback sentence. In Q5, state that partition tolerance is not optional and name a concrete payment consistency technique (e.g. idempotency keys or saga).
3. In Q6 add at least one negative consequence; trim Q1 and Q2 to ≤150 words, add missing reference [2] to the list in IEEE style, and state assumptions.

---
<sub>Run Input_4_d-Run_2-Eff_low-261118-145025 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8398/8392 | cost $0.005368 (incl. $0.001628 for the reused reference rubric+task structure) | 34.13s</sub>
