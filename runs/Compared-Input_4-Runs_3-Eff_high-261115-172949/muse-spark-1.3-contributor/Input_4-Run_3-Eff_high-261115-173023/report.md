# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You justified attributes from the lunch peak and linked styles to team size and ops cost. Your calculations and circuit breaker explanation are strong. To reach Excellent, fix the measurable availability measure, correct end-to-end availability in Q3(c), correct CAP reasoning, and add negative consequences in your ADR while staying within word limits.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You did well choosing performance and availability linked to lunch peak and abandonment, and your performance scenario in Q1 is complete with p95 <1.5s. For Excellent, make your availability Response Measure measurable – your phrase 'stay up most of the time' needs a % or time-bound threshold like the other scenario.

*Assessor reasoning:* Attributes performance/availability justified from lunch peak and abandonment. Performance scenario has all six parts with measurable p95 <1.5s. Availability scenario lacks measurable response measure ('most of the time') not quantifiable, so one scenario incomplete.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work in Q2 – clear modular monolith recommendation with specific trade-offs about five-developer team overhead and VM issues, and you acknowledged downside of no independent scaling. Keep that specificity and conciseness for other answers.

*Assessor reasoning:* Clear recommendation for modular monolith not full microservices. Two specific trade-offs: team size vs ops overhead and VM/deployment issues fixable without rewrite. Downside acknowledged: no independent scaling and shared failure domain.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure"  

### C3 Q3 Availability calculation (5/8, Proficient)

Your Q3(a) 99.30% and Q3(b) 5.0h are correct with working shown. For Excellent, fix Q3(c): you used payment availability alone 99.9975% / 0.018h. You need A_db*A_app*A_api*A_pay_new ≈99.80% and downtime ≈0.002*720 ≈1.5h.

*Assessor reasoning:* (a) 0.99301=99.30% correct. (b) 5.0h correct. (c) payment redundancy calc correct but then omitted other components; used 0.999975 as end-to-end and downtime 0.000025*720. Should be ~99.80% and ~1.5h. One part incorrect, method otherwise correct.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent in Q4 – circuit breaker with Closed/Open/Half-Open is appropriate, correctly explained and applied to the 25-min payment outage, plus tuning detail like '50% of calls in 10 seconds'. That mechanism, application, and drawback meets the top level.

*Assessor reasoning:* Circuit Breaker is appropriate. States Closed/Open/Half-Open explained correctly and applied to 25-min outage with fast-fail UX. Tuning consideration provided via threshold and wait period example.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  

### C5 Q5 Consistency and availability (3/6, Proficient)

You reasonably favoured availability for menu and consistency for orders in Q5 with Redis TTL technique. For Excellent, correct CAP – you cannot give up partition tolerance – and replace idempotency key with a consistency technique like strongly consistent DB write or saga with transactional guarantees.

*Assessor reasoning:* Menu favours availability (stale cache) and orders favour consistency both reasonable. CAP explanation wrong - partition tolerance cannot be given up. Concrete technique for menu (Redis TTL) ok, but idempotency key is not a consistency technique for payments, so technique weak/imprecise.
> Question 5: "CAP theorem says a system can only provide two of consistency, availability and partition tolerance, so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Q6 ADR in context of synchronous outlet calls and 4.2s p95 has clear Context, Decision and specific positives. For Excellent, add at least one negative consequence such as increased ops complexity, eventual consistency for outlets, or risk of duplicate deliveries from outbox.

*Assessor reasoning:* ADR has Context, Decision, Consequences specific to synchronous outlet calls and 4.2s p95. Positives given (response time, offline handling, smoothing peak) but no negative consequence (ops complexity, eventual consistency, duplicate delivery) listed, so one-sided.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

You used required headings, precise terminology and IEEE citations. For Excellent, keep every answer within 150 words – Q2 currently exceeds the limit, which moved you to Proficient despite otherwise strong communication.

*Assessor reasoning:* Headings used, IEEE citations and reference list present, precise terminology. Q2 exceeds 150-word limit, others near limit, so one answer over limit triggers Proficient with minor formatting issue.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 3: (a)(b) correct but (c) calculates end-to-end availability as payment availability alone 99.9975% instead of A_db*A_app*A_api*A_pay_new = ~99.80% (approx 99.79-99.80 depending rounding) and downtime ~1.4-1.5h not 0.018h.
- Question 5: CAP statement chooses C+A and gives up P, incorrect. Partition tolerance is required in distributed system; choice is between C and A during partition. Idempotency key is resilience not consistency guarantee.
- Question 1: Availability scenario response measure 'stay up most of the time' not measurable; needs percentage or threshold.

## Next steps

1. Rewrite your Q1 availability Response Measure as measurable, e.g., '99.9% of requests succeed during peak' with clear threshold, to make both scenarios six-part and measurable.
2. Recompute Q3(c) end-to-end as A_db*A_app*A_api*A_pay_new (~99.79-99.80%) and downtime ~1.4-1.5h for 720h, not payment alone 99.9975% / 0.018h.
3. Fix Q5 CAP logic: P is required in distributed systems; choose C vs A during partition. Replace idempotency key for orders with a consistency technique like strong consistency / distributed transaction / linearizable write, and add a negative ADR consequence like ops complexity or duplicate delivery risk.

---
<sub>Run Input_4-Run_3-Eff_high-261115-173023 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8061/5666 | cost $0.00248 (incl. $0.001628 for the reused reference rubric+task structure) | 13.75s</sub>
