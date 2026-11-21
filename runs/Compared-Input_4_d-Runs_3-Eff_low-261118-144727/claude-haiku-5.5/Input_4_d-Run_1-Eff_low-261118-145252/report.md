# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

Strong, well-structured answers overall, and your Question 2 modular-monolith recommendation is the standout piece — clearly argued with scenario-specific trade-offs. The work needed now is precision: two parts of Question 3 are arithmetically wrong, the circuit breaker states are reversed in Question 4, the CAP explanation in Question 5 misstates what can be sacrificed, and your ADR needs a negative consequence. Fixing these is mostly mechanical rather than conceptual.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Your performance and availability choices are well justified from the lunch-hour peak, and both scenarios are complete in structure. The gap to Excellent is measurability: 'stay up most of the time' cannot be tested. Restate it as a numeric uptime target over a defined period and this becomes Excellent.

*Assessor reasoning:* Performance and availability are well justified from the lunch-hour scenario. Both scenarios have six parts, but the availability response measure ('stay up most of the time') is not measurable, so this is Proficient rather than Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. The modular-monolith recommendation is specific to the five-developer team and the single-VM, deployment-downtime problems, and you explicitly accept that modules cannot be scaled independently. This is exactly the trade-off reasoning the rubric asks for.

*Assessor reasoning:* Clear modular-monolith recommendation with scenario-specific trade-offs (five-developer team, single-VM and deployment-downtime problems). The downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct at 99.30%, but (b) misstates 0.00699 × 720 as 3.5 h when it is about 5.0 h, and (c) reports payment availability as end-to-end order availability. For (c), the full order chain including the 99.30% outlet gives about 99.30% and roughly 5.1 h/month. Show your working line by line.

*Assessor reasoning:* Part (a) is correct (99.30%). Part (b) is wrong: 0.00699 × 720 ≈ 5.0 h, not 3.5 h. Part (c) is wrong: it reports payment availability as end-to-end order availability, ignoring the 99.30% chain, giving about 99.30% and roughly 5.1 h/month. Two parts are incorrect.
> Question 3(b): "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3(c): "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit breaker is the right pattern and your tuning consideration is sound, but the state machine is described backwards: Closed passes calls, Open fails fast, and Half-Open success closes the breaker. Correct the mechanism and this answer reaches the top level.

*Assessor reasoning:* Circuit breaker is an appropriate pattern with a tuning consideration. However the state mechanism is wrong: Closed passes calls through, Open fails fast, and the text reverses them. Half-Open success is also described as reopening the breaker. The explanation is incorrect.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "the breaker moves to Closed and calls fail immediately"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasoned and the Redis 60-second TTL is a concrete, appropriate technique for menu browsing. Two fixable gaps: partition tolerance cannot be given up in a distributed system, so frame the choice as C versus A during a partition; and name a concrete technique for the payment/order case too.

*Assessor reasoning:* Choices are reasoned, and a concrete technique is named for menu browsing. The CAP explanation is imprecise: partition tolerance cannot be given up in a distributed system. No concrete technique is named for the payment/order case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  
> Question 5: "(for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Context, Decision and Consequences are all present and tied to the CampusEats scenario. The consequences read entirely positively, though. Add at least one negative consequence — added queue complexity, or what happens if the broker fails — and it becomes Excellent.

*Assessor reasoning:* Context, Decision and Consequences are all present and scenario-specific. Consequences are entirely positive; no negative consequence (e.g., added complexity, eventual delivery, queue failure handling) is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Word limits and headings are respected and the writing is clear throughout. The one problem is citation [2] in Question 4 being absent from your reference list. Add the full IEEE-style entry and this criterion is fully met.

*Assessor reasoning:* Word limits and headings are met and the writing is clear. Citation [2] is used but absent from the reference list, which is a citation problem.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
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

- Question 3(b): Downtime 0.00699 × 720 is about 5.0 h, not 3.5 h.
- Question 3(c): End-to-end availability ignores the 99.30% order chain and is reported as 99.9975%; correct value is about 99.30% with roughly 5.1 h/month downtime.
- Question 4: Circuit breaker states are wrong: Closed passes calls, Open fails fast, Half-Open success should close the breaker.
- Question 5: Claiming to give up partition tolerance is incorrect; in distributed systems partitions must be tolerated, so the choice is between C and A during a partition.
- Question 1: Availability response measure is not measurable.
- Assumptions: No explicit assumptions stated, as required by R7.

## Next steps

1. Redo Question 3(b) and (c) with the arithmetic written out: 0.00699 × 720 ≈ 5.0 h, and for (c) multiply the whole order chain (including the 99.30% outlet availability) rather than reporting payment availability alone, giving ≈99.30% and about 5.1 h/month downtime.
2. Rewrite the Question 4 mechanism so the states are correct: Closed lets calls through, Open fails fast, and a successful Half-Open trial closes the breaker. Keep your tuning consideration as-is.
3. Revisit Question 5 so partition tolerance is treated as unavoidable in a distributed system — the choice is between C and A during a partition — and name a concrete technique for the payment/order case as well as for menu browsing.
4. For Question 6, add at least one negative consequence (for example added queue complexity or handling broker failure), and replace the Question 1 availability response measure with something measurable such as a percentage uptime target.
5. Replace the missing reference [2] with a full IEEE-style entry, state your assumptions explicitly, and re-check every response measure is stated in numbers.
6. Keep your Question 2 reasoning as the model for the rest — that paragraph is exactly the level of specificity the rubric rewards.

---
<sub>Run Input_4_d-Run_1-Eff_low-261118-145252 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11393/7160 | cost $0.004776 (incl. $0.001628 for the reused reference rubric+task structure) | 30.73s</sub>
