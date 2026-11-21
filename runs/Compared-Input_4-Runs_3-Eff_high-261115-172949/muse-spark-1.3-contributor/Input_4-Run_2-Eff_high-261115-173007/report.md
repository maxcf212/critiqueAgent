# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 28 / 40 (70%)**

You show strong practical judgment on style, resilience and availability calculations. To reach Excellent, tighten measurable response measures in Q1, correct end-to-end availability aggregation in Q3c, fix CAP reasoning in Q5, and add a negative consequence in your ADR while staying within word limits.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You chose relevant attributes and justified them from the lunch peak. Your first scenario with p95 under 1.5s is complete and measurable. For Excellent, change your second measure 'stay up most of the time' to a quantified value like 99.9% uptime or <30s recovery.

*Assessor reasoning:* Two relevant attributes chosen with justification from lunch peak scenario. First scenario has all six parts and measurable measure. Second scenario has six parts labelled but measure 'stay up most of the time' is not measurable, so one scenario fails measurability -> Proficient.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work in Q2. You recommended modular monolith with two CampusEats-specific trade-offs – 5-person team vs microservice overhead, and single-VM issues – and you acknowledged the downside that modules cannot scale independently.

*Assessor reasoning:* Clear modular monolith recommendation. Two trade-offs specific to CampusEats: team size 5 vs microservice overhead, and known problems (single VM latency, deployment downtime) not architectural. Downside explicitly acknowledged.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months"  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure"  
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Well shown working: Q3(a) 99.30% and Q3(b) 5.0h are correct. For Excellent, in Q3(c) you used payment availability only for 99.9975% and 0.018h. You need to multiply by the other three components to get ~99.80% and ~1.5h.

*Assessor reasoning:* Working shown. (a) series multiplication correct to 99.30%. (b) downtime ~5.0h correct to one decimal. (c) payment active-active calc 0.999975 correct but end-to-end incorrectly uses only payment failure, giving 99.9975% and 0.018h instead of ~99.80% and ~1.5h. Exactly one part incorrect.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.0 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Strong Q4 – you correctly named Circuit Breaker, explained Closed/Open/Half-Open with 50% in 10s, applied it to the payment outage to avoid thread blocking, and gave tuning considerations.

*Assessor reasoning:* Appropriate pattern named, closed/open/half-open mechanism explained correctly, applied to slow provider outage limiting thread blocking. Tuning consideration provided (50% threshold, 10s window, wait period).
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  
> Question 4: "students would have seen "payment temporarily unavailable" instead of the whole app hanging" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices – cached menu for availability and idempotency key for payment consistency. For Excellent, correct CAP: you must handle partitions, so justify CP for payments vs AP for menu, not choosing C and A and giving up P.

*Assessor reasoning:* Both choices reasonable (menu AV availability, payment consistency) with concrete techniques. CAP theorem used incorrectly stating to give up partition tolerance, which is not an option; should be CP vs AP. One technique each named.
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance, so for payments we choose consistency and availability"  
> Question 5: "show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  
> Question 5: "each order request carries an idempotency key so that a repeated request does not create a second charge."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your ADR in Q6 has specific Context, Decision with RabbitMQ OrderPaid event, and positive consequences. For Excellent, add at least one negative consequence like duplicate handling, ordering, or operational complexity.

*Assessor reasoning:* ADR has specific Context, Decision, Consequences. Positive consequences explained (latency, offline resilience, smoothing) but no negative consequence (operational complexity, ordering, duplicate handling, schema evolution) => one-sided.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Clear writing with headings and IEEE citations [1]. For Excellent, keep every answer ≤150 words – Q2 is ~165 words – and add an explicit assumptions statement if required.

*Assessor reasoning:* Headings used, IEEE citations correct, mostly clear. Q2 exceeds 150-word limit (approx 165 words) and no explicit assumptions statement, so one formatting requirement breach -> Proficient.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months. Instead the existing application should be restructured"  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3(c): End-to-end availability calculated as payment availability only: 99.9975% and 0.018h. Correct is A_other * A_pay = (0.9995*0.999*0.9995)*0.999975 ≈ 0.99798 = 99.80%, downtime ≈ (1-0.99798)*720 ≈ 1.5h.

## Next steps

1. Rewrite Q1 second response measure to be measurable, e.g. 'system remains available 99.9% of peak hour' instead of 'stay up most of the time'.
2. For Q3c recalculate end-to-end as A_menu*A_notify*A_orders*A_pay_new = 0.9995*0.999*0.9995*0.999975 ≈ 99.80%, then downtime ≈1.5h for 720h.
3. Fix Q5 CAP explanation: you cannot give up partition tolerance; explain CP vs AP choice, and in Q6 add one negative consequence like ordering or duplicate handling, and trim Q2 to <150 words.

---
<sub>Run Input_4-Run_2-Eff_high-261115-173007 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8309/6230 | cost $0.002617 (incl. $0.001628 for the reused reference rubric+task structure) | 15.46s</sub>
