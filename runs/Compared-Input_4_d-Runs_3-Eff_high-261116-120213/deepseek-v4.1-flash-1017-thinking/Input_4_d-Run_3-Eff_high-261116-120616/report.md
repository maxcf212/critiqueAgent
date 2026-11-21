# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 25 / 40 (62.5%)**

You have a clear structure and a strong Q2 recommendation. Q1 and Q6 are close to the next level, but Q3 has two calculation errors, Q4 reverses circuit-breaker states, Q5 misuses CAP and omits a payment technique, and Q2 exceeds the word limit. Reference [2] is also missing from your list.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Q1: You justify performance and availability well, and your performance scenario is measurable. To reach Excellent, make the availability response measure measurable (e.g., 99.9% monthly uptime) and include the required explicit assumptions section; both scenarios then need all six parts with measurable measures.

*Assessor reasoning:* Performance and availability are well justified and the performance scenario is measurable. The availability scenario has all six parts but its response measure is vague, so it is not measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Q2: Excellent. Your modular-monolith recommendation is clear and grounded in the scenario: five developers, ops overhead, and known problems not caused by the monolith. You also acknowledge the downside (no independent scaling, whole-process crash risk). Keep this level by staying within 150 words in future answers.

*Assessor reasoning:* Clear modular-monolith recommendation with two scenario-specific trade-offs (team size/ops overhead, known problems not caused by monolith) and an acknowledged downside.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Q3: Part (a) is correct, but (b) should be 0.00699 × 720 = 5.03 hours, not 3.5. For (c), multiply all component availabilities before converting to downtime; that gives about 99.80% and 1.5 hours, not 99.9975% and 0.018 hours. Show each step to reach Excellent.

*Assessor reasoning:* Part (a) is correct, but (b) should be 5.0 hours and (c) should multiply all components, giving about 99.80% and 1.5 hours. Two parts are wrong.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

Q4: You name Circuit Breaker and apply it to the outage, but the Open/Closed states are reversed. Open should fail fast; Closed should pass calls. Correct that mechanism and explain how the breaker would open as the provider slows, then add a drawback or tuning consideration to reach Excellent.

*Assessor reasoning:* Circuit Breaker is named and applied, but the Open/Closed states are reversed: Open should fail fast and Closed should pass calls. The outage application is therefore also wrong.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "the breaker would have closed within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Q5: Your choices are reasonable and menu caching is concrete. However, CAP is misused: you cannot give up partition tolerance in a distributed system; during a partition you choose CP or AP. Name a concrete payment technique (e.g., idempotency keys or transactional outbox) and justify both choices to reach Excellent.

*Assessor reasoning:* Both choices are reasonable and menu caching is a concrete technique. However, CAP is misused (partition tolerance cannot be given up) and no concrete payment technique is named.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Q6: Context, Decision and Consequences are present and specific. To reach Excellent, add at least one negative consequence to balance the positive ones—for example, the added complexity or a new failure mode from decoupling order placement from the outlet.

*Assessor reasoning:* Context, Decision and Consequences are present and specific, but the consequences are one-sided: only positive outcomes are listed, with no negative consequence.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

C7: Writing is clear and headings are used. Q2 is about 182 words, over the 150-word limit, and reference [2] is cited but missing from your reference list. Trim Q2 and add the missing IEEE-style entry to reach Excellent.

*Assessor reasoning:* Writing is clear and headings are used, but Q2 is about 182 words (over 150) and reference [2] is cited without a corresponding entry in the reference list.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed. Upper Saddle River, NJ, USA: Addison-Wesley, 2012."  

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

- Question 3: Part (b): 0.00699 × 720 = 5.03 hours, not 3.5 hours.
- Question 3: Part (c): new availability must multiply all components; result is about 99.80% and 1.5 hours downtime, not 99.9975% and 0.018 hours.
- Question 4: Circuit Breaker states reversed: Open should fail fast, Closed should pass calls; 'closed within seconds' should be 'opened'.
- Question 5: CAP misuse: cannot give up partition tolerance in a distributed system; during partition choose CP or AP. No concrete payment technique named.
- Question 6: No negative consequence in ADR.
- Question 1: Availability response measure is not measurable.
- Question 2: Answer exceeds 150-word limit (about 182 words).
- References: Reference [2] is cited but missing from reference list.
- Question 1: No explicit assumptions section despite task requirement.

## Next steps

1. Re-work Q3(b) and Q3(c): show 0.00699 × 720 = 5.03 hours for (b), and for (c) multiply all component availabilities before converting to downtime (about 99.80%, 1.5 hours).
2. Correct Q4's circuit-breaker states (Open = fail fast, Closed = pass calls) and Q5's CAP use: in a partition choose CP or AP, and name a concrete payment technique such as idempotency keys or a transactional outbox.
3. Tighten Q2 to 150 words, make Q1's availability response measure measurable (e.g., 99.9% monthly uptime), add a negative consequence to Q6's ADR, and add reference [2] to the list.

---
<sub>Run Input_4_d-Run_3-Eff_high-261116-120616 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8218/16720 | cost $0.010204 (incl. $0.001628 for the reused reference rubric+task structure) | 41.74s</sub>
