# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You have a clear structure and a strong, scenario-specific recommendation in Q2, and your menu-browsing reasoning in Q5 is well justified. The main gaps are technical: Q3 has an arithmetic slip and an incorrect end-to-end availability, Q4 reverses the circuit-breaker states, and Q5 misstates CAP. Q1 needs a measurable availability measure, Q6 needs negative consequences, and formatting needs tightening.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 4 / 8 | 4 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Developing | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose two relevant attributes and justified them from the scenario, and your performance scenario has all six parts with a measurable response measure. To reach Excellent, make the availability response measure measurable, for example with a specific uptime percentage or maximum downtime per month, so both scenarios fully meet the six-part, measurable requirement.

*Assessor reasoning:* Two relevant attributes are chosen with reasonable scenario-based justification. The performance scenario has all six parts and a measurable response measure. The availability response measure ('stay up most of the time') is not measurable, so the scenarios are not fully compliant.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is clear and well grounded. You linked it to the five-person team and to the single-VM lunchtime slowdown and 20-minute weekly downtime, and you acknowledged the downside of no independent scaling and shared process failure. This is Excellent-level work; keep your trade-offs this specific.

*Assessor reasoning:* A clear modular-monolith recommendation is justified by scenario-specific trade-offs: five-developer team size and the specific known problems (single VM, 20-minute weekly downtime). The downside (no independent scaling, shared process failure) is acknowledged.
> Question 2: "The slow lunchtime responses come from running on a single virtual machine, which can be fixed by running two or more instances"  

### C3 Q3 Availability calculation (4/8, Developing)

Part (a) is correct with working shown. In (b), recheck 0.00699 × 720, which gives about 5.0 hours rather than 3.5, and give the answer to one decimal place as requested. In (c), end-to-end availability must include all four components, not just payment; the result is about 99.80%, or about 1.5 hours of downtime per month. Getting all three parts right would reach the Excellent level.

*Assessor reasoning:* Part (a) is correct (99.30%) with working. Part (b) is an arithmetic error: 0.00699×720 is about 5.0 h, not 3.5 h. Part (c) correctly gives 99.9975% for payment only, but wrongly reports it as end-to-end availability, omitting the other components (about 99.80%, about 1.5 h/month). Two parts are wrong.
> Question 3: "0.00699 × 720 = 3.5 hours per month"  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You named an appropriate pattern, applied it to the outage, and included a threshold tuning example, which covers the tuning consideration. However, the states are reversed: Closed should pass calls, Open should fail fast, and Half-Open should close the breaker on success and reopen it on failure. Correct these state transitions to reach the Excellent level.

*Assessor reasoning:* The pattern is appropriate and applied to the outage, with a threshold tuning example. However, the state mechanism is wrong: Closed passes calls and Open fails fast, and the Half-Open transitions are reversed. The explanation is therefore incorrect.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "If they succeed it opens again, otherwise it stays closed."  

### C5 Q5 Consistency and availability (3/6, Developing)

Your menu-browsing choice is well justified, and naming cached data with a TTL is a concrete technique. The payment answer misstates CAP: under a partition you must choose between consistency and availability, and partition tolerance cannot be given up in a distributed system. Restate the trade-off correctly and name a concrete technique for payments, such as idempotency keys, quorum or consensus.

*Assessor reasoning:* Menu browsing is well justified with a named technique (cached data with TTL). The payment choice misstates CAP, since partition tolerance cannot be sacrificed and the trade-off is C versus A under partition. No concrete technique (e.g., idempotency keys, quorum, consensus) is named for the payment case.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your context is specific, citing offline tablets and lunch-peak latency, and the decision is clearly stated. However, the consequences list only benefits. Add at least one negative consequence, such as the operational burden of running a message broker, the possibility of duplicate or out-of-order messages, or the extra handling needed for eventual consistency in the outlet view.

*Assessor reasoning:* Context is specific (offline tablets, lunch-peak latency) and the decision is clear. Consequences are one-sided, with only positive effects listed and no negative consequence such as broker operations, duplicate delivery or ordering concerns.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your headings are correct and your writing is clear. Some answers appear to exceed the 150-word limit, so check Questions 1, 2 and 4 and trim them. Citation [2] is used in Question 4 but is missing from the references, so add it in IEEE format. Addressing these points would move your presentation to the Excellent level.

*Assessor reasoning:* Several answers (Questions 1, 2 and 4 appear to) exceed 150 words. Citation [2] is used but absent from the reference list. Headings are correct and the writing is clear.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

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

- Question 3: (b) 0.00699 × 720 is about 5.0 hours, not 3.5 hours; the result should also be given to one decimal place.
- Question 3: (c) End-to-end availability ignores the other three components; the correct value is about 99.80% (about 1.5 h/month downtime), not 99.9975%.
- Question 4: Circuit breaker states are confused: Closed should pass calls and Open should fail fast; Half-Open success should close the breaker and failure should reopen it.
- Question 5: CAP is misstated: under a partition the choice is consistency versus availability; partition tolerance cannot be dropped in a distributed system.
- Question 1: Availability response measure is not measurable.
- Question 6: Consequences list only benefits; no negative consequence is given.
- Question 4: Citation [2] is not included in the reference list.
- General: No assumptions section is provided, although the brief requires assumptions to be stated.

## Next steps

1. Correct the technical errors first: the Q3 arithmetic and end-to-end availability, the Q4 circuit-breaker states, and the Q5 CAP statement.
2. In Q1, replace the availability response measure with a measurable target, and in Q6 add at least one negative consequence to the decision record.
3. Check Questions 1, 2 and 4 against the 150-word limit, add citation [2] to the references in IEEE style, and include the assumptions section the brief requires.

---
<sub>Run Input_4_d-Run_3-Eff_high-261116-121130 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 16483/17090 | cost $0.010249 (incl. $0.001628 for the reused reference rubric+task structure) | 68.4s</sub>
