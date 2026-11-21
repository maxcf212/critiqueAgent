# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You show strong scenario-specific reasoning in Q2 and Q6, with clear trade-offs and structure. Key technical fixes: Q3 arithmetic and combined-availability method, Q4 circuit-breaker state semantics, Q5 CAP application and payment technique, Q6 negative consequence, and Q1 measurable availability target. Also tighten word limits and complete references. These targeted corrections will lift several criteria to the next level.

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

You chose two relevant quality attributes and justified them well from the scenario. Your performance scenario is complete and measurable (p95 < 1.5 s, no dropped requests). To reach Excellent, make the availability response measure measurable—replace 'stay up most of the time' with a concrete target (e.g., 99.9% uptime or max downtime per month). Ensure both scenarios have all six parts and measurable response measures.

*Assessor reasoning:* Two attributes well justified from the scenario and the performance scenario is complete and measurable, but the availability response measure ('stay up most of the time') is not measurable, so it falls short of Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You gave a clear recommendation (modular monolith) and justified it with two scenario-specific trade-offs: team size and known single-VM/deployment problems. You also explicitly acknowledged the downside (modules cannot scale independently; a bug can crash the whole process). This meets the Excellent level. Keep linking trade-offs to the scenario and acknowledging downsides.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs (team size, known single-VM and deployment problems) and an explicit acknowledged downside.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct (99.30%). In (b), your method is right but arithmetic slip: 0.00699 × 720 = 5.03 h, not 3.5 h. In (c), multiply the new payment availability by the other three components; that gives ~99.80% and ~1.5 h downtime, not 99.9975%. To reach Proficient, correct the arithmetic and use the correct combined-availability method; show working to the requested precision.

*Assessor reasoning:* Part (a) correct (99.30%). Part (b) arithmetic error: 0.00699×720 = 5.0 h, not 3.5 h. Part (c) method wrong: the combined payment availability must still be multiplied by the other three components, giving ~99.80% and ~1.5 h, not 99.9975%.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

You named an appropriate pattern (circuit breaker) and applied it to the outage with tuning detail. However, the state semantics are inverted: Open should reject calls immediately (fail fast), and Closed should pass calls normally. To reach Proficient, correct the state explanations and ensure the pattern is correctly applied; for Excellent, also include a drawback or tuning consideration (you have tuning detail, but fix the inversion).

*Assessor reasoning:* Circuit breaker is an appropriate pattern and is applied to the outage with tuning detail, but the state semantics are inverted (Open should fail fast, Closed should pass calls), a significant technical error.
> Question 4: "In the Open state calls pass through normally... the breaker moves to Closed and calls fail immediately" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable and your menu technique is concrete (Redis cache with 60-second TTL). However, CAP is misapplied: partition tolerance is not optional; during a partition you trade consistency against availability. Also, no concrete technique is named for the payment case. To reach Excellent, explain CAP correctly (C vs A during partition) and name a concrete payment technique (e.g., idempotency keys, 2PC, saga).

*Assessor reasoning:* Both choices are reasonable and the menu technique is concrete, but CAP is misused (partition tolerance is not optional; you trade C against A) and no concrete technique is named for the payment case.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has Context, Decision and Consequences, all specific to CampusEats. However, the consequences are entirely positive. To reach Excellent, add at least one negative consequence (e.g., eventual consistency, duplicate notifications, queue operations overhead) alongside the positive one.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats, but the consequences are entirely positive with no negative consequence stated.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your writing is clear, but several answers (Q1, Q2, Q4) exceed the 150-word limit, and reference [2] is cited in Q4 but missing from the reference list. To reach Proficient, keep every answer within 150 words and ensure all cited sources appear in the reference list in IEEE style. For Excellent, also ensure precise terminology and required headings throughout.

*Assessor reasoning:* Several answers (Q2, Q4, Q1) exceed the 150-word limit, and reference [2] is cited in Q4 but absent from the reference list.
> Question 2: "First, team size versus operational overhead."  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3(b): 0.00699 × 720 = 5.03 h, not 3.5 h; downtime should be ~5.0 hours per month.
- Question 3(c): Combined availability must multiply the new payment availability by the other three components: ~99.80% and ~1.5 h downtime, not 99.9975% and 0.018 h.
- Question 4: Circuit breaker states inverted: Open should reject calls immediately; Closed should pass calls normally.
- Question 5: CAP misapplied: partition tolerance cannot be 'given up'; the choice is C versus A during a partition. No concrete payment technique (e.g. idempotency keys, 2PC, saga) named.
- Question 6: No negative consequence given (e.g. eventual consistency, duplicate notifications, queue operations overhead).
- References: Reference [2] cited but missing from the reference list.

## Next steps

1. Revisit Q3: correct the arithmetic in (b) to 5.03 h and use the correct combined-availability method in (c) (multiply new payment availability by the other three components, giving ~99.80% and ~1.5 h).
2. Fix Q4 circuit-breaker state semantics: Open should reject calls immediately; Closed should pass calls normally. Then add a drawback or tuning consideration to reach Excellent.
3. In Q5, explain CAP correctly (partition tolerance is not optional; trade C vs A during a partition) and name a concrete payment technique (e.g., idempotency keys, 2PC, saga). Also add a negative consequence to Q6 and make Q1's availability response measurable.

---
<sub>Run Input_4_d-Run_1-Eff_low-261118-144945 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8237/11244 | cost $0.007357 (incl. $0.001628 for the reused reference rubric+task structure) | 40.85s</sub>
