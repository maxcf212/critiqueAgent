# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You show solid architectural reasoning, especially on style and resilience. Q2 and your writing meet Excellent. Marks were lost on measurable response measures in Q1, the end-to-end calc in Q3(c), CAP phrasing in Q5, and missing negatives/drawbacks in Q4 and Q6. Tightening those will lift you to Excellent across the board.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You chose two relevant attributes and your performance scenario in Question 1 with 'p95 <1.5s and no requests dropped' is complete and measurable. To reach Excellent, make your availability measure measurable too, replacing 'stay up most of the time' with e.g., 99.9% uptime.

*Assessor reasoning:* Two relevant attributes chosen with scenario justification. Performance scenario has all six parts with measurable measure. Availability scenario has six parts named but response measure is vague/not measurable, so not excellent.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (5/6, Excellent)

Excellent work in Question 2. You clearly recommend modular monolith with two CampusEats-specific trade-offs for your 5-dev team and acknowledge the downside that modules share a process and cannot scale independently. This meets Excellent.

*Assessor reasoning:* Clear modular monolith recommendation with two trade-offs specific to CampusEats (5-dev team operational overhead, known VM/deployment problems) and explicitly acknowledges downside of shared process scaling/failure.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Your working for Q3(a) 99.30% and Q3(b) 5.0h is correct and to precision. For Excellent, fix Q3(c): end-to-end is not payment-only 99.9975%/0.018h. You need App*DB*App*combined-pay ~99.80% and ~1.5h/month, as flagged.

*Assessor reasoning:* Parts (a) 99.30% and (b) 5.0h correct with working to requested precision. Part (c) incorrectly reports end-to-end availability as payment-only 99.9975% and downtime 0.018h, ignoring app and DB components. Exactly one part incorrect.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "So the new availability of placing an order is 99.9975%"  
> Question 3: "0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

Good call in Question 4 naming Circuit Breaker and explaining Closed/Open/Half-Open and applying it so students see 'payment temporarily unavailable'. For Excellent, add one drawback or tuning consideration like failure threshold, timeout, or fallback handling.

*Assessor reasoning:* Appropriate pattern named, mechanism (Closed/Open/Half-Open) correctly explained and applied to slow-provider outage. No explicit drawback or tuning consideration (e.g., threshold tuning, fallback, thundering herd) is stated.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "breaker moves to Open and calls fail immediately without waiting"  
> Question 4: "students would have seen "payment temporarily unavailable" instead of the whole app hanging" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices in Question 5 - stale menu via Redis cache and idempotency key for payments. For Excellent, correct your CAP explanation: you cannot give up partition tolerance as you wrote for payments. When partitioned you must choose between C and A.

*Assessor reasoning:* Both choices reasonable with concrete techniques (Redis cache, idempotency key). CAP theorem stated but misapplied to payments by claiming to give up partition tolerance, which is impermissible in distributed systems.
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance"  
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your ADR in Question 6 has specific Context, Decision to publish OrderPaid to RabbitMQ, and positive Consequences for latency. For Excellent, add at least one negative consequence, e.g., operational complexity or eventual consistency and duplicate handling.

*Assessor reasoning:* Context, Decision, Consequences present and specific to scenario. Consequences list only positives (latency, offline delivery, smoothing); no negative consequence such as operational complexity, eventual consistency, or ordering/duplication handling.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (4/4, Excellent)

Excellent communication: all answers within 150 words, clear headings, precise terminology, and IEEE citations like [1] and [2] with reference list. Keep this structure; no changes needed.

*Assessor reasoning:* Answers appear within 150-word limit, headings used in order, precise terminology, IEEE citations and reference list present. Q3 working excluded per instructions.
> Question 1: "The scenarios below use the six-part form from [1]."  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 1: Availability scenario response measure 'stay up most of the time' is not measurable; needs numeric target e.g., % uptime or failure rate.
- Question 3: Part (c) end-to-end availability calculated as payment-only 99.9975% and downtime 0.018h. Correct is App*DB*App*combined-pay ~99.80% and ~1.5h/month.
- Question 5: CAP explanation incorrect: claims for payments choose C+A and give up P. In presence of partition, P cannot be sacrificed; choice is between C and A.

## Next steps

1. Rewrite Q1 availability response measure with a numeric target e.g., 99.9% uptime over rolling 30 days or <0.1% failed orders.
2. Recalculate Q3(c) as App * DB * App * combined-payment and show 0-month downtime ~1.5h to fix the single-part error.
3. For Q5 state partition tolerance is unavoidable and choose C over A for payments; for Q4/Q6 add one drawback or tuning trade-off e.g., threshold tuning and operational complexity.

---
<sub>Run Input_4-Run_1-Eff_high-261115-172953 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8204/6043 | cost $0.002858 (incl. $0.001628 for the reused reference rubric+task structure) | 14.36s</sub>
