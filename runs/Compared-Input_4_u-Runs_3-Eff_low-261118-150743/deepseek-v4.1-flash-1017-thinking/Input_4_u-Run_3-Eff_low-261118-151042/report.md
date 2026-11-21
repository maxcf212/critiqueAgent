# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You submitted a technically strong, well-structured response: all six questions are answered, calculations are correct, and your ADR and CAP reasoning are sound. The main improvement is to state your assumptions explicitly, as the brief requires, and to keep Q1 within the word limit while doing so.

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

Q1 is excellent: you justify performance and availability from scenario facts and give measurable response measures. To stay at this level, keep both six-part scenarios complete and measurable; if you add assumptions, place them outside Q1 to avoid breaching the 150-word limit.

*Assessor reasoning:* Both attributes are justified from scenario facts (lunch load, 4.2 s p95, payment outage). Both scenarios contain all six parts and give measurable response measures (p95, failure %, recovery time).
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Q2 is excellent: your modular monolith recommendation is scenario-specific, with two concrete trade-offs and an acknowledged downside. Continue linking trade-offs to team size, load and known problems; avoid generic textbook pros and cons.

*Assessor reasoning:* Clear recommendation with two scenario-specific trade-offs (five developers vs many services; single VM and 20-minute weekly downtime fixed without a rewrite) and an explicit acknowledged downside.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite"  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Q3 is excellent: all parts are correct with working shown and correct precision. Maintain this by showing each step and rounding only at the end; your series and parallel calculations are accurate.

*Assessor reasoning:* Series product 0.99301 (99.30%), downtime 5.03→5.0 h, parallel payment 0.999975, new availability 0.99798 (99.80%), downtime 1.46→1.5 h. All correct, working shown, correct precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Q4 is excellent: circuit breaker mechanism, application to the payment hang, tuning consideration and drawback are all present. Keep naming a concrete tuning trigger and a fallback when the breaker is open.

*Assessor reasoning:* Circuit breaker named, states and transitions explained correctly, applied to the 25-minute payment hang, with both a tuning consideration (threshold from latency data) and a drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Q5 is excellent: AP for browsing and CP for payment are justified, CAP is stated correctly, and concrete techniques (Redis TTL, idempotency key) are named. Continue pairing each choice with a specific technique.

*Assessor reasoning:* AP for browsing and CP for payment, both justified; CAP stated correctly (partition tolerance not optional); concrete techniques given (Redis TTL cache, idempotency key).
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error"  
> Question 5: "it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Q6 is excellent: Context, Decision and Consequences are scenario-specific, with positive and negative consequences. Keep consequences balanced and include operational impacts such as monitoring burden.

*Assessor reasoning:* Context, Decision and Consequences all present and scenario-specific (synchronous tablet calls, lost orders, 4.2 s p95), with both positive and negative consequences including at-least-once duplicates.
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  

### C7 Communication and format (4/4, Excellent)

C7 is excellent: headings, terminology and IEEE-style citations are in place, and answers are within 150 words. Q1 is exactly at the limit, so trim if adding text; also ensure every cited source appears in the reference list.

*Assessor reasoning:* Required headings used in order, all answers at or under 150 words (Q1 is exactly at the limit), precise terminology, IEEE-style citations and reference list present.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 1: Word count is right at the 150-word limit; any additional sentence would breach the format rule.
- Whole document: No explicit assumptions section is included, although the brief asks for assumptions to be stated (e.g. independence of component failures, 30-day month).

## Next steps

1. Add a short 'Assumptions' section before Q1 stating independence of component failures and a 30-day month for downtime calculations; this addresses the brief's requirement without changing your answers.
2. For Q1, if you add any wording, trim elsewhere to stay under 150 words; it is currently exactly at the limit.
3. Check the reference list: ensure every source cited in the text appears in IEEE style and that R7 is fully satisfied.

---
<sub>Run Input_4_u-Run_3-Eff_low-261118-151042 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8270/9166 | cost $0.00599 (incl. $0.001628 for the reused reference rubric+task structure) | 31.14s</sub>
