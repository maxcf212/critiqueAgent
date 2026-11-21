# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 39 / 40 (97.5%)**

Excellent work — you scored 39/40. Every answer is technically accurate and tightly tied to the CampusEats scenario: your Q3 calculations are all correct with working shown, and Q1, Q2, Q4, Q5 and Q6 all reached the Excellent level. The only gap is communication: a few answers (Q1, Q2, Q4) sit at or slightly above the 150-word limit, which cost one mark.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 6 / 6 | 6 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

Excellent (6/6). You chose performance and availability and justified both from the scenario (lunch-hour load, 4.2 s p95, payment outage). Both quality attribute scenarios contain all six parts with measurable response measures. To stay at this level, keep both response measures explicitly quantified as you did.

*Assessor reasoning:* Both attributes are clearly justified from the scenario (lunch-hour load, 4.2 s p95, payment outage). Both scenarios have all six named parts with measurable response measures.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent (6/6). Your modular monolith recommendation is supported by two scenario-specific trade-offs (five developers vs eight-plus services; load profile) and you explicitly acknowledge the downside of independent scaling. Maintain this pattern of naming the accepted cost of your recommendation.

*Assessor reasoning:* Clear modular monolith recommendation with two trade-offs tied to team size, load profile and known problems; downside explicitly acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (8/8, Excellent)

Excellent (8/8). All three parts are correct with working shown: the series product 99.30%, 5.0 h downtime, and the parallel payment pair giving 99.80% and 1.5 h, all at the requested precision. Continue showing your intermediate products so your method stays verifiable.

*Assessor reasoning:* All three parts correct with working shown: series product 99.30%, 5.0 h downtime, parallel payment pair 0.999975 giving 99.80% and 1.5 h. Precision matches requirements.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent (5/5). You named the circuit breaker, explained the Closed/Open/Half-Open mechanism correctly, applied it to the 25-minute outage, and gave both a tuning consideration and the drawback that payments fail while Open. This full coverage is what the single-mark rubric requires.

*Assessor reasoning:* Circuit breaker named, mechanism (Closed/Open/Half-Open) explained correctly, applied to the 25-minute outage, with both a tuning consideration and a drawback.
> Question 4: "the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Excellent (6/6). You justified AP for browsing and CP for payments, used the CAP theorem correctly, and named concrete techniques (Redis TTL cache; idempotency keys). Keep pairing each consistency/availability choice with a named mechanism to stay at this level.

*Assessor reasoning:* AP for browsing (Redis TTL cache) and CP for payments, both justified; CAP theorem used correctly; concrete techniques named for each case.
> Question 5: "during a partition a system must give up either consistency or availability"  
> Question 5: "Each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Excellent (5/5). Your ADR has a scenario-specific Context, a clear Decision, and both positive and negative Consequences tied to CampusEats. This balance of consequences is exactly what distinguishes Excellent from Proficient — keep including at least one negative consequence.

*Assessor reasoning:* ADR has specific Context, Decision and Consequences with multiple positive and negative consequences tied to the scenario.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (3/4, Proficient)

Proficient (3/4). Your writing is clear, headings and IEEE citations are correct, but Q1, Q2 and Q4 sit at or slightly above the 150-word limit. To reach Excellent, trim each answer comfortably under the limit while keeping the scenario-specific justification.

*Assessor reasoning:* Clear writing, correct headings, IEEE citations and reference list. However, several answers (Q1, Q2, Q4) appear to sit at or slightly above the 150-word limit, a minor formatting issue.
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Next steps

1. Trim Q1, Q2 and Q4 to comfortably under 150 words by cutting general textbook background and keeping only scenario-specific justification.
2. Practise drafting answers to a word budget: state the recommendation or choice first, then add only the two or three strongest scenario-linked reasons.
3. Keep your current habits — showing working, naming concrete techniques, and acknowledging downsides — as they are exactly what the top rubric levels reward.

---
<sub>Run Input_4_u-Run_3-Eff_low-261118-151522 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8076/4673 | cost $0.002559 (incl. $0.001628 for the reused reference rubric+task structure) | 42.3s</sub>
