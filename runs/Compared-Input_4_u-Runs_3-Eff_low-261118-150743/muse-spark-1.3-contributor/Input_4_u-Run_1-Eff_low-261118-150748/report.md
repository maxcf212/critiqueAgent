# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Outstanding work — you achieved full marks across all questions with correct calculations, well-justified choices, and clear formatting. Your scenarios, trade-offs, and ADR were specific to CampusEats and measurable. Keep this precision and scenario-linking in future architecture tasks.

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

You excelled in Question 1 choosing two key attributes with scenario justification. Your p95 under 1.5 s measure was fully measurable with all six parts. You are at Excellent; to stay there keep justifying choices from the scenario.

*Assessor reasoning:* Two most relevant attributes chosen with scenario justification. Both scenarios contain all six parts with clear measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You recommended modular monolith in Question 2 noting five developers cannot run eight+ services. You gave two scenario trade-offs and acknowledged modules cannot scale independently. You are at Excellent; keep acknowledging downsides.

*Assessor reasoning:* Modular monolith recommended. Two scenario-specific trade-offs given and downside acknowledged that modules cannot scale independently.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  

### C3 Q3 Availability calculation (8/8, Excellent)

You showed correct working in Question 3 including A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798. All percentages and downtime were to requested precision. You are at Excellent; keep showing steps and rounding.

*Assessor reasoning:* All three parts correct with working shown. Series and parallel calculations, percentages to two decimals and downtime to one decimal all correct.
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You correctly explained Circuit Breaker Closed/Open/Half-Open in Question 4 and applied it to the outage. Your tuning note on too-sensitive opening was strong. You are at Excellent; keep adding drawback/tuning.

*Assessor reasoning:* Circuit Breaker named, Closed/Open/Half-Open mechanism correct, applied to outage, with tuning consideration and drawback stated.
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded"  

### C5 Q5 Consistency and availability (6/6, Excellent)

You justified AP browsing with Redis cache and CP orders with idempotency key in Question 5. Your CAP use was correct and retry does not double-charge. You are at Excellent; keep naming concrete techniques.

*Assessor reasoning:* AP for browsing with Redis cache and CP for orders with idempotency key. CAP used correctly, both choices justified.
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your Question 6 ADR had specific Context, Decision and positive plus negative consequences, e.g. tablet must ignore duplicate IDs. You are at Excellent; keep making consequences scenario-specific.

*Assessor reasoning:* ADR has specific Context, Decision, positive and negative consequences relevant to queue and CampusEats.
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs."  

### C7 Communication and format (4/4, Excellent)

You kept every answer within 150 words with precise headings and IEEE references in Question 2 modular monolith recommendation. You are at Excellent; maintain concise terminology and citation discipline.

*Assessor reasoning:* All answers concise within 150 words, precise terminology, required headings in order, IEEE citations and reference list present.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite"  

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

1. Keep linking every architecture choice to CampusEats constraints like team size and load profile.
2. Continue showing full working and units to two-decimal precision in availability analyses.
3. Maintain your habit of stating drawbacks, tuning notes, and IEEE citations in all answers.

---
<sub>Run Input_4_u-Run_1-Eff_low-261118-150748 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 11289/7264 | cost $0.003121 (incl. $0.001628 for the reused reference rubric+task structure) | 41.49s</sub>
