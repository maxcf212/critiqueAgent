# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 26 / 40 (65%)**

You produced solid, mostly well-argued answers. Question 2 has a clear, well-grounded recommendation, and Question 3(a) and (b) are correct. The main areas to strengthen are the end-to-end availability calculation in Question 3(c), the CAP explanation in Question 5, a measurable availability target in Question 1, a balanced decision record in Question 6, and the assumptions the assignment requires. Several answers also appear to exceed the word limit.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Your choice of performance and availability is well justified from the lunch-hour dependency, and your performance scenario has all six parts with a measurable response measure. Your availability scenario's response measure, 'stay up most of the time', cannot be tested. Replace it with a specific target, such as a percentage availability or a maximum monthly downtime.

*Assessor reasoning:* Performance and availability are well justified from the scenario, and the performance scenario has all six parts with a measurable response measure. The availability scenario's response measure ('stay up most of the time') is not measurable, which places this in Proficient rather than Excellent.
> Question 1 – Availability scenario: "Response measure: the system should stay up most of the time."  
> Question 1 – opening paragraph: "The two most important quality attributes are performance and availability, because the business depends on the lunch hour"  

### C2 Q2 Architectural style (5/6, Excellent)

Your modular monolith recommendation is clear and grounded in the scenario. The trade-offs of a five-person team against service overhead, and the single-VM and deployment-downtime problems, are specific to CampusEats. You also acknowledge the downside: modules cannot scale independently, and a bug in one module can crash the whole process. This is an excellent answer.

*Assessor reasoning:* Clear modular-monolith recommendation justified by scenario-specific trade-offs: five-developer team size versus service overhead, and the single-VM and deployment-downtime problems. The downside is explicitly acknowledged. Strong answer, though the known-problems argument is more rationale than trade-off.
> Question 2: "First, team size versus operational overhead."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct, with working shown: 99.30% availability and 5.0 h/month downtime. Part (c) is incorrect. You reported only the payment pair's 99.9975%, which drops the other three components from the series chain. Include all four components; the end-to-end result should be about 99.80% and 1.5 h/month downtime.

*Assessor reasoning:* Parts (a) and (b) are correct (99.30%, 5.0 h/month) with working shown. Part (c) is wrong: it reports only the payment-pair availability (99.9975%) and drops the other components from the end-to-end chain. Correct result is about 99.80% and 1.5 h/month. Exactly one part is incorrect, so Proficient.
> Question 3(c): "So the new availability of placing an order is 99.9975%"  
> Question 3(a): "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You name an appropriate pattern, Circuit Breaker, and explain its Closed, Open and Half-Open mechanism correctly. You apply it to the slow-provider outage. To reach Excellent, add at least one drawback or tuning consideration, such as the risk of false opens at your 50% threshold, or how the length of the half-open wait affects recovery.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and its Closed/Open/Half-Open mechanism is explained correctly. It is applied to the slow-provider outage. However, no drawback is given, and the threshold example is not discussed as a tuning consideration, so it falls short of Excellent.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable, and you name concrete techniques such as a TTL cache and idempotency keys. However, your CAP explanation is incorrect. Partition tolerance is not optional in a distributed system; during a partition you choose between consistency and availability. Your answer also says you favour consistency, then selects consistency and availability. Apply CAP explicitly to menu browsing as well.

*Assessor reasoning:* Choices are reasonable and concrete techniques are named (TTL cache, idempotency keys). The CAP explanation is incorrect: partition tolerance cannot be given up in a distributed system, and the answer says it favours consistency but then claims both consistency and availability. CAP is also not explicitly applied to menu browsing.
> Question 5(ii): "so for payments we choose consistency and availability and give up partition tolerance"  
> Question 5(i): "(for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your context is specific, citing offline tablets and the 4.2 s p95 latency, and your decision is clear. However, the consequences list only benefits. Add at least one negative consequence, such as added queue infrastructure and operational complexity, delayed or duplicate delivery, or the need for idempotent consumers.

*Assessor reasoning:* Context is specific (offline tablets, 4.2 s p95) and Decision is clear. Consequences list only positive outcomes; there is no negative consequence such as added queue complexity, delivery latency or the need for idempotent consumers. This is one-sided, so Proficient.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your references follow IEEE style, and in-text citations are used. However, Questions 2 and 4 appear to exceed the 150-word limit, and Questions 1 and 5 may do so too. No assumptions section is included, although the assignment requires one. Trim each answer to 150 words or fewer, and add the assumptions.

*Assessor reasoning:* References are in IEEE style and in-text citations are used. However, several answers (Questions 2, 4 and likely 1 and 5) appear to exceed the 150-word limit, and no assumptions section is provided. Estimated word counts are approximate.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 1 – Availability scenario: Response measure 'the system should stay up most of the time' is not measurable; a figure such as a percentage availability target or downtime limit is needed.
- Question 3(c): End-to-end availability ignores the other three components in series. Only the payment pair (99.9975%) is reported. Correct result is about 99.80% availability and about 1.5 h/month downtime.
- Question 5(ii): CAP misstated: partition tolerance is not optional in a distributed system; the choice is between consistency and availability during a partition. The answer also contradicts itself by saying it favours consistency and then selects consistency and availability.
- Question 6: No negative consequence is recorded (e.g., added infrastructure and operational complexity, delayed or duplicate delivery, need for idempotent consumers).
- Question 4: No drawback or tuning trade-off is discussed beyond quoting an example threshold, such as false opens or the impact of the half-open wait period.
- Overall: No assumptions are stated, although the assignment requires them.

## Next steps

1. Recalculate Question 3(c) by including all four components in the series chain, then check that your result is about 99.80% availability and 1.5 h/month downtime.
2. Correct your CAP explanation in Question 5(ii): partition tolerance is required in a distributed system, so during a partition you choose between consistency and availability. Make your choice consistent with that reasoning.
3. Give the Question 1 availability scenario a numeric target, add a negative consequence and an assumptions section, and trim each answer to 150 words or fewer.

---
<sub>Run Input_4-Run_3-Eff_high-261115-173954 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11853/12914 | cost $0.007698 (incl. $0.001628 for the reused reference rubric+task structure) | 48.73s</sub>
