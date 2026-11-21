# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You gave strong scenario-based answers, especially Q2’s modular-monolith recommendation with specific trade-offs and an acknowledged downside. Main fixes: Q3(c) end-to-end availability, Q5 CAP misuse, Q6 missing negative consequence, Q2 over the word limit, and missing measurable/tuning detail in Q1/Q4. These are targeted revisions rather than a rewrite.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You justified performance and availability well, and your performance scenario is measurable. To reach Excellent, make the availability response measure measurable too (Q1 currently says “stay up most of the time”) and ensure both scenarios have all six parts. Keep the scenario-specific justification.

*Assessor reasoning:* Attributes are well justified and the performance scenario is measurable, but the availability response measure is not measurable, so it fits Proficient rather than Excellent.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent: your modular-monolith recommendation is clear and tied to team size, load profile and deployment problems, and you acknowledge the downside that modules cannot scale independently. Keep linking trade-offs to the CampusEats scenario. Note the 150-word limit is addressed under C7.

*Assessor reasoning:* Clear modular-monolith recommendation with scenario-specific trade-offs on team size, load, and deployment problems, plus an acknowledged downside.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

You showed correct working for Q3(a) and (b). In Q3(c), you used payment availability as end-to-end availability; the correct end-to-end figure is about 99.80% with about 1.5 hours/month downtime. For Excellent, recompute the full chain, show working, and report to the requested precision.

*Assessor reasoning:* Parts (a) and (b) are correct with working. Part (c) wrongly treats payment availability as end-to-end availability; correct end-to-end is about 99.80% and downtime about 1.5 hours/month.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You correctly named and explained Circuit Breaker and applied it to the outlet-tablet outage, including a threshold example. To reach Excellent, add at least one explicit drawback or tuning consideration (for example, how you choose the failure threshold/window or what risk the breaker introduces).

*Assessor reasoning:* Circuit Breaker is correctly explained and applied to the outage, but no explicit drawback or tuning consideration is given.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds)"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable and you name idempotency keys. However, Q5 misuses CAP: partition tolerance cannot simply be given up in a distributed system, and payments should favour consistency during a partition. For Excellent, correct the CAP explanation and name a suitable concrete technique for each case.

*Assessor reasoning:* Both choices are reasonable and techniques are named, but CAP is misused: partition tolerance cannot simply be given up in a distributed system; payments should be CP during partition.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has specific Context, Decision and Consequences for the synchronous tablet call. To reach Excellent, add at least one negative consequence alongside the positive response-time consequence—state what becomes harder or what new risk you accept.

*Assessor reasoning:* Context, Decision, and Consequences are present and specific, but consequences are one-sided with no negative consequence.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear and IEEE-style references are present. Q2 exceeds the 150-word limit, so to reach Excellent keep every answer within 150 words, use precise terminology and required headings, and include the required assumptions in References.

*Assessor reasoning:* Writing is clear and IEEE-style references are present, but Question 2 exceeds the 150-word limit.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> References: "[1] L. Bass, P. Clements, and R. Kazman"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 1: Availability response measure 'stay up most of the time' is not measurable.
- Question 3: Part (c) uses payment availability as end-to-end availability; correct end-to-end is about 99.80% with about 1.5 hours/month downtime.
- Question 4: No explicit drawback or tuning consideration is stated for Circuit Breaker.
- Question 5: CAP theorem is misused; partition tolerance cannot be given up, and payments should favour consistency during a partition.
- Question 6: No negative consequence is included in the ADR.
- Question 2: Answer exceeds the 150-word limit.
- References: No assumptions are stated as required.

## Next steps

1. Recompute Q3(c) end-to-end availability as the product of all relevant components (about 99.80%, about 1.5 hours/month downtime) and show the working to the requested precision.
2. Revise Q5 so CAP is used correctly: partition tolerance cannot be given up; during a partition payments should favour consistency, and each case needs a concrete technique.
3. Make Q1’s availability response measure measurable, add an explicit Circuit Breaker drawback/tuning consideration in Q4, add a negative consequence in Q6, and trim Q2 to 150 words.

---
<sub>Run Input_4-Run_1-Eff_low-261118-115807 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8167/12151 | cost $0.007894 (incl. $0.001628 for the reused reference rubric+task structure) | 49.45s</sub>
