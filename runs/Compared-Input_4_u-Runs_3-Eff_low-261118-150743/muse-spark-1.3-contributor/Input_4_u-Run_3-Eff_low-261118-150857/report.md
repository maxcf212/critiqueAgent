# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Excellent work — you achieved full marks across all six questions. You justified scenario-specific choices, kept response measures measurable, showed accurate working, and wrote clearly within format limits. Keep this precision and grounding in scenario detail in future architecture tasks.

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

You did well choosing two central attributes with scenario justification in Question 1, including your measurable "p95 response time is under 1.5 s and no requests are dropped". To stay Excellent, keep all six parts with measurable responses.

*Assessor reasoning:* Two central attributes chosen with scenario justification; both scenarios list all six parts with measurable response measures.
> Question 1: "p95 response time is under 1.5 s and no requests are dropped"  

### C2 Q2 Architectural style (6/6, Excellent)

You did well recommending a modular monolith in Question 2 with "Five developers running eight or more services would spend more time" plus downside. To stay Excellent, keep two scenario-specific trade-offs and acknowledge downside.

*Assessor reasoning:* Modular monolith recommended; two scenario-specific trade-offs plus accepted downside all clearly stated.
> Question 2: "Five developers running eight or more services would spend more time"  

### C3 Q3 Availability calculation (8/8, Excellent)

You did well showing working for all three parts in Question 3, e.g., "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798". To stay Excellent, keep correct method and requested precision.

*Assessor reasoning:* All three calculations correct with working; percentages to two decimals and downtime to one decimal as required.
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You explained Circuit Breaker well in Question 4, including "After a wait it goes Half-Open and lets a few trial calls through" applied to the outage. To stay Excellent, keep application plus drawback/tuning.

*Assessor reasoning:* Circuit Breaker correctly explained, applied to 25-min outage, with tuning consideration and drawback given.
> Question 4: "After a wait it goes Half-Open and lets a few trial calls through"  

### C5 Q5 Consistency and availability (6/6, Excellent)

You justified AP for browsing and CP for payments in Question 5, noting "partitions cannot be ruled out in a distributed system, so partition tolerance is not optional". To stay Excellent, keep correct CAP use and concrete techniques.

*Assessor reasoning:* AP for browsing with Redis cache and CP for payments with idempotency key; CAP used correctly with justification.
> Question 5: "partitions cannot be ruled out in a distributed system, so partition tolerance is not optional"  

### C6 Q6 Architecture decision record (5/5, Excellent)

You wrote a specific ADR in Question 6 with Context, Decision and both consequences, e.g., "Delivery is at-least-once, so the tablet must ignore duplicate order IDs". To stay Excellent, keep positive and negative consequences.

*Assessor reasoning:* ADR has specific Context, Decision, positive and negative consequences relevant to queue introduction.
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs"  

### C7 Communication and format (4/4, Excellent)

You kept every answer within 150 words with headings, precise terms and IEEE references. To stay Excellent, keep this clear formatting and citation discipline.

*Assessor reasoning:* All answers within 150 words, headings in order, precise terminology, IEEE citations and reference list present.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than"  

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

1. Keep linking every architectural choice and trade-off explicitly to scenario constraints like team size and load.
2. Keep showing full working with correct precision and tuning consequences for calculations and patterns.
3. Keep using precise headings, concise wording under limits, and IEEE citations for sources.

---
<sub>Run Input_4_u-Run_3-Eff_low-261118-150857 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 11243/8209 | cost $0.003304 (incl. $0.001628 for the reused reference rubric+task structure) | 44.24s</sub>
