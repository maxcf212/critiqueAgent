# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You demonstrated strong scenario-based reasoning in Q1 and Q2, especially justifying quality attributes and recommending a modular monolith with clear trade-offs. However, Q3 has two computational errors, Q4 inverts circuit-breaker semantics, Q5 misstates CAP, and Q6 lacks a negative consequence. Several answers exceed the word limit and a citation is missing. Addressing these will lift your marks.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose and justified two relevant attributes well, and your performance scenario is complete with a measurable p95 target. To reach Excellent, make the availability scenario's response measure measurable (e.g., specify a percentage uptime or maximum downtime) so both scenarios have all six parts and measurable measures.

*Assessor reasoning:* Both attributes are well justified from the scenario (lunch peak, 4.2 s p95). The performance scenario has all six parts with a measurable measure; the availability scenario's response measure ('stay up most of the time') is not measurable, so it falls short of Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work—your modular monolith recommendation is clearly justified with two scenario-specific trade-offs (team size, known deployment problems) and you explicitly acknowledge the downside (no independent scaling, whole-process crash risk). This meets the top rubric level; keep linking trade-offs to the scenario.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (five-developer team, single-VM and deployment causes of known problems) and an explicit acknowledged downside.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct. In (b), recheck the multiplication: 0.00699 × 720 = 5.03 h, not 3.5 h. In (c), you reported the payment service's availability (99.9975%) rather than the end-to-end product; multiply all four availabilities (0.9995×0.999×0.9995×0.999975 ≈ 99.80%) and recompute downtime (~1.5 h). To reach Proficient, show working and ensure at most one part has an arithmetic slip.

*Assessor reasoning:* Part (a) is correct (99.30%). Part (b) has an arithmetic slip: 0.00699×720 = 5.0 h, not 3.5 h. Part (c) wrongly reports 99.9975% (that is only the payment availability); the correct end-to-end figure is ~99.80% with ~1.5 h downtime. Two parts incorrect.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

You correctly identified circuit breaker and applied it to the outage. However, the state semantics are inverted: Open should reject calls immediately (fail fast), and Closed should pass calls through. Correct this explanation. Also add at least one drawback or tuning consideration (e.g., threshold tuning, half-open state) to reach Excellent.

*Assessor reasoning:* Circuit breaker is an appropriate pattern and is applied to the outage, but the state semantics are inverted (Open should fail fast, Closed should pass through), so the mechanism is explained incorrectly. No real drawback or tuning consideration beyond a threshold example.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold ... the breaker moves to Closed and calls fail immediately" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable and you justify them; the Redis TTL for menu browsing is a good concrete technique. However, CAP is misapplied: partition tolerance is not optional—during a partition you must choose consistency or availability. Rephrase to say you choose consistency over availability for payments during a partition. Also name a concrete technique for the payment case (e.g., two-phase commit, saga, or idempotency keys) to reach Excellent.

*Assessor reasoning:* Both choices are reasonable and justified, and a concrete technique is given for menu browsing. However CAP is misapplied (partition tolerance cannot be 'given up' during a partition) and no concrete technique is named for the payment case.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has all three sections and is specific to CampusEats (synchronous tablet call, 4.2 s p95, offline tablets). The consequences are one-sided: add at least one negative consequence (e.g., eventual consistency, duplicate notifications, operational overhead of the queue) to reach Excellent.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (synchronous tablet call, 4.2 s p95, offline tablets). Consequences are one-sided: no negative consequence (e.g. eventual consistency, duplicate notifications, queue operations) is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your writing is clear and headings are used. However, Q1 and Q2 exceed the 150-word limit, reference [2] (circuit breaker) is cited in Q4 but missing from the reference list, and no assumptions are stated. To reach Proficient, keep at most one answer over the limit and fix the citation; for Excellent, ensure every answer is within 150 words and all sources are cited in IEEE style.

*Assessor reasoning:* Writing is clear and headings are used, but several answers (Q1, Q2) exceed 150 words, and reference [2] (circuit breaker) is cited in text but absent from the reference list. No assumptions are stated.
> Question 2: "Second, the known problems are not caused by the monolith itself."  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3(b): Arithmetic error: 0.00699 × 720 = 5.03 h, not 3.5 h; correct downtime is 5.0 h per 30-day month.
- Question 3(c): End-to-end availability miscomputed: 0.9995×0.999×0.9995×0.999975 ≈ 99.80%, downtime ≈ 1.5 h, not 99.9975% and 0.018 h.
- Question 4: Circuit breaker states inverted: Open should reject calls immediately; Closed should pass calls through.
- Question 5: CAP misapplied: partition tolerance is not optional; during a partition one must choose C or A. No concrete technique given for the payment case.
- Question 6: No negative consequence in the ADR; message queue introduces eventual consistency, duplicate delivery and operational overhead.
- References: Reference [2] cited in Q4 but missing from the reference list; no assumptions stated as required.

## Next steps

1. Recompute Q3(b) and Q3(c) showing each step: 0.00699 × 720 = 5.03 h; for end-to-end multiply all four availabilities (≈99.80%) and convert downtime correctly (~1.5 h).
2. Correct Q4 circuit-breaker semantics (Open = fail fast, Closed = pass through) and add a tuning consideration; in Q5 rephrase CAP to choose C or A during a partition and name a concrete payment technique.
3. In Q6 add a negative consequence; trim Q1 and Q2 to 150 words; add missing reference [2] and state assumptions.

---
<sub>Run Input_4_d-Run_3-Eff_low-261118-145100 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8362/9256 | cost $0.006177 (incl. $0.001628 for the reused reference rubric+task structure) | 30.29s</sub>
