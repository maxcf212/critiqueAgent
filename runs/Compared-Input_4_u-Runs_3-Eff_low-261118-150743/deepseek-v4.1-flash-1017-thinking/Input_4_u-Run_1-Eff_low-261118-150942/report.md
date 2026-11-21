# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Your submission is near-exemplary: all six answers are complete, calculations are correct, trade-offs are scenario-specific, and writing is within limits with IEEE references. You justify choices clearly and acknowledge downsides. The only improvement is to add an explicit assumptions section (e.g., failure independence, 30-day month) so readers can see the basis for your calculations and scenarios.

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

You chose performance and availability and grounded them in scenario evidence (900 orders/lunch hour, 4.2 s p95, payment outage). Both six-part scenarios are complete and your response measures are measurable (p95 <2 s, <0.1% non-payment failures, recovery <1 minute). This is Excellent; to maintain it, keep each part explicit and quantified.

*Assessor reasoning:* Two attributes justified from scenario evidence (lunch peak, 4.2 s p95, payment outage). Both scenarios contain all six parts and both response measures are quantified and measurable.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute"  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is clear and tied to the five-developer team and single-VM/20-minute downtime constraints. You give two scenario-specific trade-offs and explicitly acknowledge the downside (no independent scaling; one module can crash the process). Excellent level met; to sustain it, keep linking each trade-off to a named scenario fact.

*Assessor reasoning:* Clear modular-monolith recommendation with two scenario-specific trade-offs (team size/ops overhead; single VM and 20-minute downtime vs rewrite cost) and an explicit acknowledged downside.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features"  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process"  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct with working shown: series product 0.99301 (99.30%), downtime 5.03→5.0 h; parallel payment 0.999975, combined 0.99798 (99.80%), downtime 1.46→1.5 h. Precision matches the request. Excellent; to keep it, continue showing intermediate values and state assumptions such as failure independence and 30-day month.

*Assessor reasoning:* Series product 0.99301 (99.30%) correct; downtime 5.03→5.0 h correct; parallel payment 0.999975, combined 0.99798 (99.80%), downtime 1.46→1.5 h correct. Working shown, precision as requested.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You name Circuit Breaker, explain Open/Half-Open/Closed transitions correctly, and apply it to the 25-minute payment hang. You include a tuning consideration (threshold from real latency data) and a drawback (no payments while open; fallback needed). Excellent; to maintain, keep tying the pattern to the specific outage and naming the fallback behaviour.

*Assessor reasoning:* Circuit Breaker named, states and transitions explained correctly, applied to the 25-minute payment hang, with both a tuning consideration and a drawback (no payments while open, fallback needed).
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Tuning consideration: the threshold must come from real latency data"  

### C5 Q5 Consistency and availability (6/6, Excellent)

You choose AP for browsing and CP for payments, justify both, and use CAP correctly (partition tolerance is not optional). Techniques are concrete: Redis TTL cache for menus and idempotency key with rejection on partition for payments. Excellent; to tighten, frame idempotency explicitly as retry safety and pair the CP choice with a partition-consistency technique.

*Assessor reasoning:* AP for browsing and CP for payments, both justified; CAP used correctly (partition tolerance not optional); concrete techniques given (Redis TTL cache, idempotency key with rejection on partition).
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  
> Question 5: "it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your ADR has Context, Decision and Consequences, all scenario-specific: synchronous tablet call, queue-based decision, and two positive plus three negative consequences (ops burden, duplicates, premature 'paid'). Excellent; to sustain, keep consequences balanced and explicitly label positive/negative as you did.

*Assessor reasoning:* Context, Decision and Consequences all present and scenario-specific, with two positive and three negative consequences (ops burden, at-least-once duplicates, premature 'paid' state).
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply"  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor"  

### C7 Communication and format (4/4, Excellent)

All answers are within 150 words, headings are in order, terminology is precise, and IEEE citations/reference list are present. Excellent. To keep this level, add the brief assumptions statement the brief requires and re-check word counts after any revision; citations are already well formed.

*Assessor reasoning:* All answers at or under 150 words, required headings in order, precise terminology, IEEE-style citations and reference list present.
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge"  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3: Rounding of 0.993011 to 99.30% and 5.03 to 5.0 h is correct; no error, but intermediate value 0.99301 slightly truncates (0.993011) — immaterial.
- Question 5: Idempotency key is a retry-safety mechanism rather than a partition-consistency technique per se; acceptable alongside the CP rejection choice but slightly loose.
- Whole submission: No explicit assumptions section despite the brief requiring assumptions to be stated (e.g. independence of failures, 30-day month).

## Next steps

1. Add a short 'Assumptions' subsection before Q3 (and where relevant in Q1/Q5) stating independence of component failures, a 30-day month, and that response measures are under lunch-peak load; this closes the only gap noted in the overall marking.
2. In Q5, tighten the idempotency-key discussion: frame it explicitly as retry safety supporting your CP choice, and name a partition-consistency technique (e.g., quorum writes or rejecting writes during partition) so the technique maps directly to CAP.
3. Keep every answer at or under 150 words and preserve IEEE citations; when revising, re-check Q3 rounding to the requested precision (99.30%, 5.0 h, 99.80%, 1.5 h) and keep working shown.

---
<sub>Run Input_4_u-Run_1-Eff_low-261118-150942 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8392/10173 | cost $0.006607 (incl. $0.001628 for the reused reference rubric+task structure) | 29.85s</sub>
