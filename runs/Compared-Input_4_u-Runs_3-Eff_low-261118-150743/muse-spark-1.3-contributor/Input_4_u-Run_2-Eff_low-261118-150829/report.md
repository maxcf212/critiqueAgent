# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You delivered a strong, complete response across all six questions. Your calculations, patterns, trade-offs and ADR were scenario-specific and precise, and your writing met format requirements. Excellent work — focus now on sustaining this standard.

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

You did well in Question 1 choosing performance and availability with six-part measurable scenarios like p95 under 1.5 s. To stay Excellent, keep justifying from scenario and keeping measures measurable.

*Assessor reasoning:* Performance and availability justified from lunch peak and outage. Both scenarios list all six parts with quantitative measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You did well in Question 2 recommending modular monolith with team-size trade-off about five developers. To stay Excellent, keep giving two scenario-specific trade-offs and acknowledging downside.

*Assessor reasoning:* Modular monolith recommended. Two scenario-specific trade-offs: scaling vs 5-person overhead, rewrite cost vs VM and downtime fixes. Downside acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  

### C3 Q3 Availability calculation (8/8, Excellent)

You did well in Question 3 showing working to get A_new = 0.99798 and correct downtime. To stay Excellent, keep showing method and requested precision for all parts.

*Assessor reasoning:* All three parts correct with working. Series multiplication, parallel payment formula, 720h downtime correct to required precision.
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You did well in Question 4 explaining Closed/Open/Half-Open and tuning sensitivity. To stay Excellent, keep applying pattern to outage with drawback.

*Assessor reasoning:* Circuit Breaker named, Closed/Open/Half-Open explained correctly, applied to 25-min hang, with threshold tuning and fallback drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded"  

### C5 Q5 Consistency and availability (6/6, Excellent)

You did well in Question 5 choosing AP browsing with Redis cache and CP payment with idempotency key. To stay Excellent, keep using CAP correctly with concrete techniques.

*Assessor reasoning:* AP for browsing and CP for payment justified. CAP partition trade-off stated correctly. Concrete techniques given for each case.
> Question 5: "show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

You did well in Question 6 with specific Context, OrderPaid via RabbitMQ Decision, and positive/negative Consequences. To stay Excellent, keep all three specific.

*Assessor reasoning:* ADR has specific Context, Decision, positive and negative Consequences tied to synchronous tablet call and p95.
> Question 6: "Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

You did well using Q1-Q6 headings, concise writing and IEEE citations like [1] and Nygard. To stay Excellent, keep within limits with precise terms and citations.

*Assessor reasoning:* Headings Q1-Q6 in order, concise precise writing within limits, IEEE in-text citations and reference list present.
> Question 1: "The scenarios use the six-part form from [1]."  
> References: "M. T. Nygard, Release It! Design and Deploy Production-Ready Software, 2nd ed."  

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

1. Keep grounding each architectural choice in CampusEats specifics like lunch peak, team size, and outage.
2. Keep adding measurable response measures and concrete tuning details to show precision.
3. Keep using precise terminology, headings and IEEE citations to sustain clear communication.

---
<sub>Run Input_4_u-Run_2-Eff_low-261118-150829 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 7958/5424 | cost $0.002419 (incl. $0.001628 for the reused reference rubric+task structure) | 28.24s</sub>
