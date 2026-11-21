# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 39 / 40 (97.5%)**

Excellent work across all six questions. Your Q1 scenarios were complete and measurable, Q3 calculations were fully correct with working shown, and your Q2, Q4, Q5 and Q6 answers showed scenario-specific reasoning, correct CAP usage and balanced consequences. The only gap is format: Question 2 appears marginally over the 150-word limit, which held Communication at Proficient. Tighten word counts to reach the top level there.

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

Excellent. You chose performance and availability and justified them from scenario data (900 orders/hour, 4.2 s p95, payment outage). Both scenarios had all six parts with measurable response measures, e.g. 'p95 response time under 1.5 s and no requests dropped'. This is exactly what the top rubric level requires; maintain this standard.

*Assessor reasoning:* Performance and availability are clearly justified from scenario data (900 orders/hour, 4.2 s p95, payment outage). Both scenarios have all six parts with measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent. Your modular monolith recommendation was justified by two scenario-specific trade-offs (team size, lunchtime load from a single VM) and you explicitly acknowledged the downside that modules cannot be scaled independently. To stay at this level, keep trade-offs anchored to the scenario rather than textbook points.

*Assessor reasoning:* Clear recommendation with two trade-offs tied to team size, load profile and known problems; downside explicitly acknowledged.
> Question 2: "The lunchtime slowness comes from a single virtual machine and is fixed by running several instances"  
> Question 2: "The downside I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (8/8, Excellent)

Excellent. All parts verified correct: series availability 0.99301 (99.30%), downtime 5.0 h; parallel payment 0.999975 giving 99.80% and 1.5 h downtime. Working was shown to the requested precision. Keep showing your working step by step, as this is what full marks depend on.

*Assessor reasoning:* Verified: series product 0.99301 (99.30%), downtime 5.0 h; parallel payment 0.999975, new availability 99.80%, downtime 1.5 h. All parts correct with working and required precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent. You named the Circuit Breaker pattern, explained the Closed/Open/Half-Open mechanism correctly, applied it to the payment outage, and gave both a tuning consideration (thresholds from real latency data) and a drawback. This covers every element of the top level; sustain this completeness in future answers.

*Assessor reasoning:* Circuit Breaker named, mechanism (Closed/Open/Half-Open) explained correctly, applied to the payment outage, with both a tuning consideration and a drawback.
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Excellent. Both consistency/availability choices were justified, CAP was used correctly (P not optional), and concrete techniques were named for each case (Redis with 60-second TTL; idempotency keys). Your framing of rejecting orders with a clear error rather than risking inconsistent charges was strong applied reasoning.

*Assessor reasoning:* Both choices justified, CAP theorem stated correctly (P not optional), concrete techniques named for each case (Redis TTL cache; idempotency keys).
> Question 5: "the order is rejected with a clear error rather than risk an inconsistent charge"  
> Question 5: "Redis with a 60-second TTL"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Excellent. Context, Decision and Consequences were all present and scenario-specific, with both positive and negative consequences, e.g. the queue being one more component for five developers to run. Balanced consequences are what distinguish Excellent from Proficient; you did this well.

*Assessor reasoning:* Context, Decision and Consequences all present and scenario-specific, with multiple positive and negative consequences.
> Question 6: "Consequences (negative): The queue is one more component for five developers to run"  

### C7 Communication and format (3/4, Proficient)

Proficient. Headings were used in order, IEEE citations and a reference list were present, and terminology was precise. The single issue was Question 2 appearing marginally over the 150-word limit. To reach Excellent, ensure every answer is within 150 words and double-check counts before submitting.

*Assessor reasoning:* Headings used in order, IEEE citations and reference list present, terminology precise. Question 2 appears marginally over the 150-word limit; no other format issues.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  

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

1. Trim Question 2 to 150 words or fewer by cutting general background and keeping the recommendation and trade-offs
2. Check every answer against the word limit before submission, as one overrun cost a mark here
3. Keep citing sources in IEEE style and using the required headings, which you did well

---
<sub>Run Input_4_u-Run_1-Eff_low-261118-151417 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 7927/4518 | cost $0.002742 (incl. $0.001628 for the reused reference rubric+task structure) | 31.04s</sub>
