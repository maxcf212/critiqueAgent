# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 25 / 40 (62.5%)**

You scored 25/40. Q2 is excellent and Q1/Q6 are strong. Q3 has two wrong parts, Q4 reverses circuit-breaker states, Q5 misuses CAP and omits a payment technique, Q6 lacks a negative consequence, and Q2 exceeds the word limit with a missing reference. Address these specific fixes to move up the rubric.

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

You chose performance and availability well, justified from the lunch peak and abandonment. Your performance scenario has all six parts and a measurable p95 target. Your availability scenario has six parts, but 'stay up most of the time' is not measurable. To reach Excellent, make both response measures measurable, for example 99.9% monthly uptime.

*Assessor reasoning:* Performance and availability are well justified from the lunch peak and abandonment. The performance scenario has all six parts and a measurable p95 target. The availability scenario has six parts but its response measure is not measurable, so it is not Excellent.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. Your modular-monolith recommendation is clear, with scenario-specific trade-offs: five developers versus operational overhead, and single-VM/deployment causes of known problems. You acknowledge the downside: no independent scaling and whole-process crash risk. Keep this level of specificity.

*Assessor reasoning:* Clear modular-monolith recommendation. Trade-offs are scenario-specific: five developers versus operational overhead, and single-VM/deployment causes of known problems. The downside is acknowledged: no independent scaling and whole-process crash risk.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct. Part (b) has an arithmetic slip: 0.00699×720 is about 5.03 h, not 3.5 h. Part (c) computes payment availability correctly but treats it as end-to-end; multiply all components to get about 99.80% and about 1.46 h downtime. To reach Proficient, correct both parts and show working.

*Assessor reasoning:* Part (a) is correct. Part (b) has an arithmetic error: 0.00699×720≈5.03 h, not 3.5 h. Part (c) computes payment availability correctly but then treats it as end-to-end availability; the other components must still multiply, giving about 99.80% and about 1.46 h downtime.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit breaker is appropriate and applied to the outage, but the state semantics are reversed: Open should fail fast and Closed should pass calls. 'Opens again' should be 'closes again'. No clear drawback or tuning consideration is given beyond a threshold example. To reach Proficient, correct the mechanism explanation; for Excellent, add a drawback or tuning consideration.

*Assessor reasoning:* Circuit breaker is appropriate and applied to the outage, but the state semantics are reversed: Closed is normal and Open fails fast. 'Opens again' should be 'closes again'. No clear drawback or tuning consideration is given beyond a threshold example.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "the breaker moves to Closed and calls fail immediately"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your menu choice and Redis cache technique are good. The payment choice is reasonable, but CAP is misused: partition tolerance is not optional; during a partition you choose consistency or availability. No concrete payment technique is named. To reach Excellent, explain CAP correctly and name a concrete payment technique, such as idempotency keys or a transactional outbox.

*Assessor reasoning:* The menu choice and Redis cache technique are good. The payment choice is reasonable, but CAP is misused: partition tolerance is not optional; favouring consistency during a partition sacrifices availability. No concrete payment technique is named.
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance"  
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are specific and present. Your consequences are all positive; no negative consequence is given. To reach Excellent, add at least one negative consequence, such as added complexity, operational overhead, or eventual consistency.

*Assessor reasoning:* Context, Decision and Consequences are specific and present. The consequences are all positive; no negative consequence is given, so it is Proficient rather than Excellent.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Headings and IEEE-style [1] are present, and writing is clear. Q2 is about 181 words, over the 150-word limit; [2] is cited in Q4 but missing from the reference list; assumptions are not stated. To reach Excellent, keep every answer within 150 words, add the missing reference entry, and state assumptions.

*Assessor reasoning:* Headings and IEEE-style [1] are present, but Question 2 is about 181 words (over 150), [2] is cited without a reference entry, and no assumptions are stated. Writing is otherwise clear.
> Question 4: "The Circuit Breaker pattern [2]"  
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

- Question 1: Availability response measure 'stay up most of the time' is not measurable.
- Question 2: Answer is about 181 words, exceeding the 150-word limit.
- Question 3(b): 0.00699 × 720 = 5.03 hours, not 3.5 hours.
- Question 3(c): New end-to-end availability must multiply all components; 99.9975% is only payment availability. Correct end-to-end is about 99.80%, downtime about 1.46 h.
- Question 4: Circuit breaker Open/Closed states are reversed; Open should fail fast, Closed should pass calls.
- Question 5: CAP misuse: partition tolerance cannot be given up; in a partition choose C or A. Payment technique missing.
- Question 6: No negative consequence in the ADR.
- References: [2] is cited in Question 4 but absent from the reference list; assumptions are not stated.

## Next steps

1. Re-work Q3: correct 0.00699×720 to about 5.03 h and multiply all component availabilities for end-to-end availability (about 99.80%, about 1.46 h downtime).
2. Fix Q4 circuit-breaker semantics (Open = fail fast, Closed = pass calls) and add a drawback or tuning consideration; in Q5 explain CAP correctly (partition tolerance is not optional) and name a concrete payment technique.
3. In Q6 add a negative consequence; in Q2 trim to 150 words or fewer; add reference [2] and state your assumptions.

---
<sub>Run Input_4_d-Run_1-Eff_high-261116-120459 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8306/15044 | cost $0.00962 (incl. $0.001628 for the reused reference rubric+task structure) | 43.06s</sub>
