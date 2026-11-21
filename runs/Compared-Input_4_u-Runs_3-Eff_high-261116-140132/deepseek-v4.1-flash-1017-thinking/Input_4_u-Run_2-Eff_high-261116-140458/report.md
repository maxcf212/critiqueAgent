# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You submitted a strong, complete response: all six questions are answered, Q3 calculations are correct, and your Q1 scenarios are fully six-part with measurable measures. Q2's modular monolith recommendation is well justified, and Q4–Q6 apply patterns and CAP precisely. The only gap is an explicit assumptions section beyond the 30-day month statement. Keep this standard.

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

You chose performance and availability and justified them with the lunch peak, 4.2 s p95 and payment outage. Both Q1 scenarios have all six parts and measurable response measures (p95 < 1.5 s; menu p95 < 2 s; <0.1% non-payment failures; recovery within 1 minute). You are at Excellent; to stay there, keep every scenario measurable and add a brief note on why lower-ranked attributes were excluded.

*Assessor reasoning:* Chooses performance and availability, justified with lunch peak, 4.2 s p95 and payment outage. Both scenarios contain source, stimulus, artefact, environment, response and measurable response measures. Full six-part form.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation in Q2 is clear and scenario-specific: five developers versus service overhead, and the known single-VM/20-minute downtime versus rewrite cost. You also acknowledge the downside (no independent scaling; one module can crash the process). Excellent level. To maintain it, keep linking each trade-off to the team size, load profile or known outage.

*Assessor reasoning:* Clear modular monolith recommendation. Trade-offs are scenario-specific: five-developer team vs service overhead, and known single-VM/20-minute downtime vs rewrite cost. Downside acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts of Q3 are correct with working: series product 99.30%, 5.0 h downtime, active-active payment pair 99.9975%, end-to-end 99.80%, 1.5 h downtime. Rounding matches the requested precision. You are at Excellent. To strengthen auditability, add an explicit assumptions subsection (independence, 30-day month, constant failure rates) alongside your calculations.

*Assessor reasoning:* All three parts correct with working: series product 99.30%, 5.0 h downtime, active-active payment pair 99.9975%, end-to-end 99.80%, 1.5 h downtime. Rounding matches requested precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  
> Question 3: "Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named circuit breaker, explained closed/open/half-open correctly, applied it to the 25-minute payment hang, and gave a tuning/fallback drawback ('nobody can pay while it is open'). This is Excellent. To keep it, continue pairing each pattern with a concrete outage and at least one operational drawback or tuning consideration.

*Assessor reasoning:* Names circuit breaker, explains closed/open/half-open mechanism, applies it to the 25-minute payment hang, and gives tuning and fallback drawback.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

You chose AP for menu with Redis 60-second TTL and CP for payments with rejection/idempotency keys. CAP is stated correctly, and both choices are justified by user impact. Excellent. To stay there, keep naming a concrete technique for each case and explicitly tie the consistency choice to the payment risk.

*Assessor reasoning:* Chooses AP for menu with Redis cache and CP for payments with rejection/idempotency. CAP is stated correctly and both choices are justified by user impact.
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  
> Question 5: "Redis with a 60-second TTL"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your ADR has specific Context, Decision and Consequences, with both positive and negative consequences (operational load; at-least-once duplicate handling). Excellent. To maintain it, keep consequences two-sided and scenario-specific, and avoid generic context statements.

*Assessor reasoning:* ADR has specific Context, Decision and Consequences. Positive and negative consequences are both present, including operational load and at-least-once duplicate handling.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Required headings appear in order, answers are at or under 150 words, terminology is precise, and IEEE-style references are present. Excellent. To stay there, keep every answer within the limit and add the missing explicit assumptions note to Q3; this also addresses the partial R7.

*Assessor reasoning:* Required headings appear in order; answers are at or under 150 words; terminology is precise; IEEE-style references are present.
> Question 1: "## Question 1"  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Question 3; References |

## Next steps

1. Add a brief 'Assumptions' subsection to Q3 (e.g., component independence, 30-day month, constant failure rates) so your availability model is fully auditable; this addresses the partial R7 without altering your correct results.
2. In Q1, keep the measurable response measures; for future work, add a one-line note on why other attributes (e.g., security, modifiability) were ranked lower to make the prioritisation even more defensible.
3. For Q2 and Q6, continue naming scenario-specific trade-offs and both positive and negative consequences; to secure top marks every time, explicitly link each consequence back to the five-developer team or the 20-minute outage.

---
<sub>Run Input_4_u-Run_2-Eff_high-261116-140458 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8310/17078 | cost $0.010412 (incl. $0.001628 for the reused reference rubric+task structure) | 52.38s</sub>
