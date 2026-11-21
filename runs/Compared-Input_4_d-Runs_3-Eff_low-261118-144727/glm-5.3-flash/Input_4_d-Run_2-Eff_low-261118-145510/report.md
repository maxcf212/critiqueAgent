# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

Good work overall: your Q2 recommendation was excellent, with trade-offs tied directly to the scenario, and your Q3 method was correct apart from one arithmetic slip. To lift your mark, fix the inverted circuit breaker states in Q4, apply CAP correctly and name a payment technique in Q5, add a negative consequence to your ADR, and trim Q2 and Q4 to 150 words with a complete reference list.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 | 6 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose suitable attributes with good scenario-based justification, and your performance scenario was fully six-part and measurable. To reach Excellent, make the availability response measure measurable — replace 'stay up most of the time' with a figure such as 99.5% uptime per month.

*Assessor reasoning:* Performance and availability are well justified from the scenario and the performance scenario is fully six-part and measurable. However, the availability response measure ('stay up most of the time') is not measurable, so not Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. Your modular monolith recommendation was justified with two scenario-specific trade-offs (five developers, single VM, 20-minute deployment downtime) and you explicitly acknowledged the downside of not scaling modules independently. Nothing more needed here.

*Assessor reasoning:* Clear recommendation (modular monolith) with two trade-offs tied to scenario specifics (five developers, single VM, 20-minute deployment downtime), and the downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (6/8, Proficient)

Your method was correct and part (a) was right, but in (b) 0.00699 × 720 = 5.03 hours, not 3.5. In (c), give 99.9975% to two decimal places (100.00%) and 0.018 h to one decimal (0.0 h). Show working and match the requested precision to reach Excellent.

*Assessor reasoning:* Method correct throughout; (a) 99.30% is correct. But (b) 0.00699 × 720 = 5.03, not 3.5 hours — one arithmetic slip. (c) is correct but precision not to spec (99.9975% not two decimals; 0.018 h not one decimal). One slip keeps it Proficient.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  

### C4 Q4 Resilience pattern (2/5, Developing)

The circuit breaker was an appropriate choice and applied to the outage, but your state machine is inverted: Open should fail fast, Closed should pass calls normally, and successful Half-Open trials should close the breaker. Correct the mechanism and add a drawback or tuning consideration to reach Excellent.

*Assessor reasoning:* Circuit breaker is an appropriate pattern and applied to the outage, but the state machine is explained incorrectly: Open should block calls, Closed should pass them, and Half-Open success should close the breaker, not open it. The explanation is materially wrong.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold ... the breaker moves to Closed" *(quote not found in submission)*  

### C5 Q5 Consistency and availability (3/6, Proficient)

Both choices were reasonable and Redis with TTL was a good technique for menu browsing. However, partition tolerance cannot be given up — during a partition you choose between consistency and availability. Also name a concrete technique for payments (e.g. synchronous two-phase commit) to reach Excellent.

*Assessor reasoning:* Both choices are reasonable and justified; Redis with TTL is a concrete technique for menu browsing. But CAP is used incorrectly (partition tolerance cannot be given up; the real trade-off is C vs A during a partition), and no concrete technique is named for payments.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR had specific, scenario-based Context, Decision and Consequences, which is strong. To reach Excellent, add at least one negative consequence, such as eventual order notification delays or added operational overhead from the queue.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to the scenario (synchronous tablet calls, 4.2 s p95, offline tablets). However, consequences are entirely positive — no negative consequence (e.g. eventual notification, operational overhead) is given, so not Excellent.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your writing was clear and headings correct, but Q2 (~200 words) and Q4 (~180 words) exceed the 150-word limit, and citation [2] used in Q4 is missing from your reference list. Trim both answers and complete the reference list in IEEE style to reach Excellent.

*Assessor reasoning:* Q2 (~200 words) and Q4 (~180 words) exceed the 150-word limit. Citation [2] is used in Q4 but is missing from the reference list, so the reference list is incomplete. Writing is otherwise clear and headings are correct.
> Question 2: "Second, the known problems are not caused by the monolith itself."  
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

- Question 3(b): 0.00699 × 720 = 5.03 hours, not 3.5 hours; correct answer is 5.0 hours.
- Question 3(c): Precision not as required: 99.9975% should be given to two decimal places (100.00%) and 0.018 h to one decimal (0.0 h).
- Question 4: Circuit breaker states are inverted: Open should fail fast, Closed passes calls normally, and successful Half-Open trials close the breaker.
- Question 5: CAP theorem misapplied: partition tolerance cannot be sacrificed; during a partition one chooses between C and A. No concrete technique named for payments.
- References: Citation [2] (circuit breaker source) is cited in Q4 but absent from the reference list.

## Next steps

1. Rewrite the circuit breaker state machine in Q4: Open fails fast, Closed passes calls normally, and successful Half-Open trials close the breaker.
2. In Q5, explain that partition tolerance cannot be sacrificed — during a partition you choose between consistency and availability — and name a concrete technique for payments (e.g. synchronous commit or a quorum write).
3. Add at least one negative consequence to your Q6 ADR (e.g. delayed notifications or operational overhead), trim Q2 and Q4 to 150 words, and add citation [2] to your reference list.

---
<sub>Run Input_4_d-Run_2-Eff_low-261118-145510 | marking=z-ai/glm-5.3-flash, feedback=z-ai/glm-5.3-flash | tokens in/out 8122/5093 | cost $0.002699 (incl. $0.001628 for the reused reference rubric+task structure) | 68.28s</sub>
