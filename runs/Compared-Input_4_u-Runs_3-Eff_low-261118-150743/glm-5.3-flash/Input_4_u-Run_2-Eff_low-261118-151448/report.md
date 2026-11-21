# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

An outstanding submission. Every question is complete, scenario-specific and well justified: your Q1 scenarios are fully six-part with measurable response measures, Q3 calculations are all correct with working shown, and your Q2, Q4, Q5 and Q6 answers each name the concept, apply it to CampusEats and acknowledge downsides. Formatting, headings and IEEE citations are all in place. You are at the top rubric level throughout; focus next on sustaining this depth in more open-ended, design-heavy tasks.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 6 / 6 | 6 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

Excellent (6/6). You chose performance and availability and justified both from the scenario (900 orders/hour, 4.2 s p95, payment outage). Both scenarios contain all six parts with measurable response measures, e.g. 'p95 response time under 1.5 s and no requests dropped'. To stay at this level, keep justifying attribute choice from scenario evidence rather than naming attributes alone.

*Assessor reasoning:* Performance and availability are well justified from the scenario (900 orders/hour, 4.2 s p95, payment outage). Both scenarios have all six named parts with measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent (6/6). Your modular monolith recommendation is backed by two scenario-specific trade-offs (five developers vs eight-plus services; single-VM lunchtime slowness and weekly downtime) and you explicitly acknowledge the downside. Maintain this by always tying trade-offs to concrete scenario facts like team size and load profile.

*Assessor reasoning:* Clear modular monolith recommendation with two scenario-specific trade-offs (team size, single-VM lunchtime slowness, weekly downtime) and the downside explicitly acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  

### C3 Q3 Availability calculation (8/8, Excellent)

Excellent (8/8). All three parts correct with working shown: series product 99.30%, 5.0 h downtime, parallel payment pair 0.999975 giving 99.80% and 1.5 h, at the required precision and units. Keep showing intermediate working as you did; it protects marks against small slips.

*Assessor reasoning:* All three parts correct with working shown: series product 99.30%, 5.0 h downtime, parallel payment pair 0.999975 giving 99.80% and 1.5 h. Precision and units as required.
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent (5/5). Circuit breaker named, Closed/Open/Half-Open mechanism explained correctly, applied to the 25-minute outage, with a tuning consideration (thresholds from real latency data) and a drawback. This full combination is exactly what the top level requires; keep pairing mechanisms with tuning and drawbacks.

*Assessor reasoning:* Circuit breaker named, mechanism (Closed/Open/Half-Open) explained correctly, applied to the 25-minute outage, with both a tuning consideration and a drawback given.
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Excellent (6/6). AP for browsing and CP for payments, both justified; CAP stated correctly with P not optional; concrete techniques named (Redis TTL cache, idempotency keys). Your idempotency-key example is a strong, concrete touch; continue naming specific mechanisms rather than generic ones.

*Assessor reasoning:* AP for browsing and CP for payments, both justified; CAP theorem stated correctly (P not optional); concrete techniques named (Redis TTL cache, idempotency keys).
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Excellent (5/5). Your ADR has scenario-specific Context, a clear Decision, and both positive and negative consequences, including at-least-once delivery and the queue as extra operational burden. Balanced consequences are what distinguishes the top level; keep including at least one of each.

*Assessor reasoning:* ADR has scenario-specific Context, a clear Decision, and multiple positive and negative consequences including at-least-once delivery and alerting.
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Excellent (4/4). Required headings used in order, answers within 150 words, precise terminology, IEEE-style citations and reference list, and assumptions stated where needed. Sustain this discipline in longer assignments where word limits and citation expectations typically tighten.

*Assessor reasoning:* Required headings used in order; answers appear within 150 words; precise terminology; IEEE-style citations and reference list included; assumptions stated where needed.
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

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

1. Practise applying the same six-part scenario structure to quality attributes beyond performance and availability (e.g. security, modifiability) so the method transfers to new contexts.
2. Extend your trade-off analysis by quantifying downsides where possible (e.g. estimating the operational cost of the queue for five developers) to strengthen future ADRs and recommendations.
3. Explore tuning trade-offs in resilience patterns further, such as how circuit-breaker thresholds interact with retry budgets and cascading failure risk.

---
<sub>Run Input_4_u-Run_2-Eff_low-261118-151448 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 7920/4602 | cost $0.002522 (incl. $0.001628 for the reused reference rubric+task structure) | 34.49s</sub>
