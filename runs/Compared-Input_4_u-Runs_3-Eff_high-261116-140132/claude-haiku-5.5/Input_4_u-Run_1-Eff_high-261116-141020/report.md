# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 37 / 40 (92.5%)**

You produced a strong submission. Your Question 3 availability calculations are fully correct, and Questions 1, 2, 4 and 6 are well argued and tied to the CampusEats scenario. Your main gaps are the missing assumptions section that the brief requires, a weakly matched consistency technique in Question 5, and Question 1 running slightly over 150 words. Addressing these would strengthen an already solid answer.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

You chose performance and availability and tied both to scenario facts, such as the 900 lunch orders, the 4.2 s p95 and last month's payment slowdown. Both scenarios have all six parts, and their response measures are measurable, such as a p95 under 1.5 s with no dropped requests. This is top-band work. Keep this level of scenario grounding in future answers.

*Assessor reasoning:* Performance and availability are chosen and tied to scenario facts (900 lunch orders, 4.2 s p95, last month's payment slowdown). Both scenarios have all six parts and measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Availability scenario. Source: the external payment provider."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation is clear and well justified. You linked it to the five-developer team's operational overhead and to the slowness and weekly downtime of the single VM. You also acknowledged the downside: modules cannot scale independently, and a bug can still crash the whole process. No change is needed for this criterion.

*Assessor reasoning:* Clear modular monolith recommendation. Two scenario-specific trade-offs are given: operational overhead for five developers, and the single-VM slowness and weekly downtime. The downside is acknowledged.
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct, with working shown and percentages given to two decimal places. To strengthen the method, state the component availabilities and the independence assumption explicitly. The marker noted that they were used without being stated as assumptions.

*Assessor reasoning:* I checked all three parts. (a) 99.30% is correct. (b) 5.0 h is correct. (c) 99.80% and 1.5 h are correct, with working shown and two-decimal percentages.
> Question 3: "Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named the Circuit Breaker, explained its states correctly and applied it to the payment outage. You also gave a drawback, that no payments can be taken while the circuit is open, and a tuning consideration, that the threshold must come from real latency data. This is an excellent answer.

*Assessor reasoning:* Circuit Breaker is named and its states are explained correctly. It is applied to the payment outage, and both a drawback (no payments while open) and a tuning consideration are given.
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Both of your choices are justified, and your CAP statement is essentially correct. However, idempotency keys prevent duplicate charges but do not provide consistency during a partition, so the technique you named for the CP case is weakly matched. Name a technique that maintains consistency under partition, such as synchronous quorum writes or a serialised transaction, and explain why it fits.

*Assessor reasoning:* Both choices are justified and the CAP statement is essentially correct. However, idempotency keys address duplicate charges rather than consistency under partition, so the CP technique is weakly matched.
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your decision record includes Context, Decision and Consequences, all specific to CampusEats. The consequences include positive points, such as faster response and offline outlets recovering, and negative points, such as the extra component, at-least-once duplicates and the risk of stuck queues. Your Context states that synchronous outlet calls add to the 4.2 s p95 without evidence, so present this as a stated assumption or support it with evidence.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific. Consequences include both positive (faster response, offline outlets recover) and negative (extra component, at-least-once duplicates, stuck-queue risk) points.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear, your headings are correct and your IEEE citations are accurate. Question 1 is about 151 words, one over the 150-word limit, so trimming it would secure the top band. The marker recorded the references requirement as only partly met without saying why, so check your reference list against the brief's requirements.

*Assessor reasoning:* Writing is clear and headings are correct. IEEE citations and the reference list are correct. Question 1 is about 151 words by my count, one word over the limit, so it is not fully Excellent.
> Question 1: "Availability scenario. Source: the external payment provider."  

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

- Question 5 (ii): Idempotency keys prevent duplicate charges but do not provide consistency during a partition. A CP technique such as synchronous quorum writes or a serialised transaction would fit better.
- Question 6 Context: Asserts that synchronous outlet calls add to the 4.2 s p95 without evidence or a stated assumption.
- Question 3: Component availabilities and the independence assumption are used without being stated as assumptions.
- Whole document: No assumptions section is provided, although the brief requires assumptions to be stated.

## Next steps

1. Add an explicit assumptions section, and state the component availabilities and the independence assumption used in Question 3 as assumptions.
2. In Question 5(ii), replace idempotency keys with a CP technique such as synchronous quorum writes or a serialised transaction, and explain why it keeps data consistent during a partition.
3. Trim Question 1 to 150 words or fewer, and check your reference list against the brief's requirements, since the marker recorded the references requirement as only partly met.

---
<sub>Run Input_4_u-Run_1-Eff_high-261116-141020 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11348/19128 | cost $0.010755 (incl. $0.001628 for the reused reference rubric+task structure) | 69.18s</sub>
