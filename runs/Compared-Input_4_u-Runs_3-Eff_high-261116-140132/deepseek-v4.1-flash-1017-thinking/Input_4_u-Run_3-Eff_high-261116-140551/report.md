# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You submitted an excellent response earning full marks across all criteria. Q1 scenarios are complete and measurable, Q2 trade-offs are scenario-specific, Q3 calculations are correct with working, Q4–Q6 apply patterns, CAP and ADR structure well, and references follow IEEE style. Minor polish only: align Q1 artefact and response measure, and soften Q2 'removed' wording.

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

You chose performance and availability with strong scenario justification and complete six-part scenarios. The measurable response measures are a strength. To stay at Excellent, align the availability artefact (order service) with its response measure (menu p95 and non-payment failures), so the measure clearly tests the stated artefact.

*Assessor reasoning:* Chooses performance and availability with scenario-specific justification. Both scenarios contain source, stimulus, artefact, environment, response and measurable response measures. Minor artefact/measure alignment issue but still complete.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation is clear and justified by scenario-specific trade-offs: five developers, lunchtime load, weekly downtime and rewrite cost. You also acknowledge the downside. To remain at Excellent, soften 'removed' to 'reduced' for rolling deployments, since planned downtime is not fully eliminated.

*Assessor reasoning:* Clear recommendation. Trade-offs are scenario-specific: five-developer team and operational overhead; lunchtime load and weekly downtime; rewrite cost. Downside acknowledged. Minor 'removed' wording is not material.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct with working shown: (a) 99.30%, (b) 5.0 h, (c) 99.80% and 1.5 h. Precision matches the request. To stay at Excellent, keep showing the series calculation and rounding steps exactly as you did; no changes needed.

*Assessor reasoning:* All three parts correct with working. (a) 99.30%; (b) 5.0 h; (c) 99.80% and 1.5 h. Rounding to requested precision is correct.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named circuit breaker, explained closed/open/half-open correctly, applied it to the 25-minute payment hang, and gave tuning and fallback drawbacks. This fully meets Excellent. To maintain it, keep linking the threshold to real latency data and stating the fallback behaviour explicitly.

*Assessor reasoning:* Names circuit breaker, explains closed/open/half-open mechanism, applies it to the 25-minute payment hang, and gives tuning and fallback drawbacks. Fully meets excellent.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (6/6, Excellent)

Both choices are justified and CAP is used correctly: AP for menu with Redis cache, CP for payments with rejection and idempotency key. Concrete techniques are named for each. To stay at Excellent, continue making the CAP trade-off explicit and naming the technique for each case.

*Assessor reasoning:* Both choices justified. CAP theorem used correctly: AP for menu with Redis cache; CP for payments with rejection and idempotency key. Concrete techniques named for each.
> Question 5: "Menu browsing: I would favour availability."  
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your ADR includes Context, Decision and Consequences, all scenario-specific, with both positive and negative consequences including operational cost and at-least-once duplicates. This meets Excellent. To maintain it, keep the negative consequences as concrete as the positive ones and avoid generic context.

*Assessor reasoning:* ADR has Context, Decision, and Consequences. Context and decision are scenario-specific. Positive and negative consequences are both present, including operational cost and at-least-once duplicates.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Required headings are used in order, answers are at or under 150 words, terminology is precise, and IEEE-style citations and a reference list are present. This meets Excellent. To stay there, keep Q1/Q5/Q6 at exactly 150 words or less and preserve the citation format.

*Assessor reasoning:* Required headings used in order. Answers are at or under 150 words (Q1/Q5/Q6 exactly 150). IEEE-style citations and reference list present. Terminology is precise.
> Question 1: "## Question 1"  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | Question 3; References |

## Technical issues

- Question 1: Availability scenario artefact is the order service, but the response measure includes menu p95 and non-payment failures; minor artefact/measure alignment issue.
- Question 2: Rolling deployments reduce planned deployment downtime but do not eliminate all downtime; 'removed' is slightly strong.

## Next steps

1. In Q1, tighten the availability scenario so the artefact (order service) and response measure (menu p95, non-payment failures) align; keep all six parts and measurable measures.
2. In Q2, revise 'removed' to 'reduced' or 'largely eliminated' for rolling deployments, since planned downtime is reduced not fully removed.
3. Maintain the Excellent standard by keeping every answer at or under 150 words, using required headings, and citing sources in IEEE style as you did in References.

---
<sub>Run Input_4_u-Run_3-Eff_high-261116-140551 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8319/25882 | cost $0.015695 (incl. $0.001628 for the reused reference rubric+task structure) | 79.94s</sub>
