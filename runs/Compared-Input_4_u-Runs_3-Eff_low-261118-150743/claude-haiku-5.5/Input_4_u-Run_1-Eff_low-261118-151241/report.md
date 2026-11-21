# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 37 / 40 (92.5%)**

You scored strongly on the core content: well-chosen quality attributes, correct availability calculations, a well-applied Circuit Breaker answer and a clear, specific decision record. Your main deductions come from answers that exceed the 150-word limit, unstated assumptions, and a weak consistency technique for payments. Your estimated total is 37/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 5 / 6 | 5 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

You chose two attributes, performance and availability, and justified them clearly from the lunchtime load of 900 orders and the 4.2 s p95 that causes abandoned orders. Both scenarios have all six parts and numeric response measures. The availability measure bundles three measures into one line, which makes it harder to test. Separating them would strengthen this answer. Scored 6/6.

*Assessor reasoning:* Two attributes are chosen and justified from the scenario. Both scenarios have all six parts, and both response measures are numeric and testable. Word count may slightly exceed 150, which is handled under C7.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Your recommendation is clear and tied to the scenario: five developers running eight or more services, the single virtual machine behind the lunchtime slowness, and the 20-minute weekly downtime. You also acknowledge the downside that modules cannot be scaled independently. Scored 6/6.

*Assessor reasoning:* Clear recommendation with trade-offs tied to team size, the single VM and the 20-minute weekly downtime. The downside is acknowledged. The answer is likely over 150 words, which is penalised under C7 rather than here.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The lunchtime slowness comes from a single virtual machine and is fixed by running several instances"  
> Question 2: "The downside I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct, with working shown to the requested precision: 99.30% and 5.0 h for (a), 5.0 h for (b), and 99.80% and 1.5 h for (c). Scored 8/8.

*Assessor reasoning:* Recomputed: (a) 99.30%, 5.0 h; (b) 5.0 h; (c) 0.999975 and 99.80%, 1.5 h. All correct with working and the requested precision.
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  
> Question 3: "Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

Circuit Breaker is an appropriate choice. You explained its mechanism correctly, applied it to the 25-minute outage and gave a tuning consideration, noting that the threshold must come from real latency data. Scored 5/5.

*Assessor reasoning:* Circuit Breaker is appropriate and its states are explained correctly. It is applied to the 25-minute outage, and tuning and drawback considerations are given.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (5/6, Excellent)

Your browsing choice (AP with eventual consistency, supported by caching with TTL) is justified and your CAP reasoning is correct. The payment technique is the weak point: an idempotency key prevents duplicate charges but is not a consistency technique. Scored 5/6.

*Assessor reasoning:* Both choices are justified and CAP is used correctly. Caching with TTL is named for browsing. The payment technique is weaker, since an idempotency key is more about duplicate handling than consistency, so 5 rather than 6.
> Question 5: "This is the AP choice, with eventual consistency."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Context, Decision and Consequences are all present and specific to CampusEats. You give both positive and negative consequences, including the extra queue component for five developers and the lost orders from offline tablets. Scored 5/5.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific. Both positive and negative consequences are given.
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  
> Question 6: "If a tablet is offline the order is lost, and these calls add to the 4.2 s p95."  

### C7 Communication and format (2/4, Developing)

Your writing is clear and you use the required headings and IEEE-style references. However, several answers exceed the 150-word limit, with Question 2 clearly over. The references criterion is only partially met, so check that every source follows IEEE style fully. Scored 2/4.

*Assessor reasoning:* Question 2 is clearly over 150 words, and Question 1 is likely also over. Multiple answers exceed the limit. Headings and IEEE references are present, and the writing is clear.
> Question 2: "First, independent scaling versus operational overhead."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice"  

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

- Question 5: An idempotency key prevents duplicate charges but is not a consistency technique. A stronger choice would be a consensus or quorum-based write, or a single-leader transaction for payments.
- Question 1: The availability scenario bundles three response measures into one line, which makes it harder to test.

## Next steps

1. Trim Questions 1 and 2 (and check the others) to 150 words or fewer, keeping the trade-offs and scenario-specific reasoning.
2. Replace the idempotency key in Question 5 with a true consistency technique for payments, such as a single-leader transaction or a quorum-based write, and explain how it preserves consistency.
3. State your assumptions explicitly in the calculations and design answers, and make each Question 1 response measure a separate, testable statement.

---
<sub>Run Input_4_u-Run_1-Eff_low-261118-151241 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11522/7578 | cost $0.004997 (incl. $0.001628 for the reused reference rubric+task structure) | 29.18s</sub>
