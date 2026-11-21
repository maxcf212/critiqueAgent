# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You demonstrated strong architectural reasoning in Question 2 by recommending a modular monolith with concrete trade-offs. However, marks were lost across other questions due to imprecise quality attribute response measures, inverted Circuit Breaker state definitions, calculation errors in end-to-end availability, misapplication of the CAP theorem, and an incomplete consequences section in your ADR. Addressing these conceptual and quantitative gaps will help you reach the Excellent rubric band.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 3 / 5 | 3 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You selected and justified suitable quality attributes. To reach Excellent, ensure both response measures are objectively measurable; your availability measure ('stay up most of the time') was too vague.

*Assessor reasoning:* Performance and availability are well chosen and justified. However, the availability scenario's response measure ('stay up most of the time') is vague and not objectively measurable.
> ## Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. You provided a clear recommendation justified by scenario-specific trade-offs regarding team size and performance, while explicitly acknowledging the architectural downsides.

*Assessor reasoning:* Clear recommendation of a modular monolith justified by two detailed, scenario-specific trade-offs (team size/overhead and root cause of performance issues), with explicit downsides acknowledged.
> ## Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

To achieve Excellent, eliminate calculation slips (5.03 hours in part b) and remember to multiply the parallel payment availability back into the overall series chain for part (c).

*Assessor reasoning:* Parts (a) and (b) are correct (99.30% and 5.03/3.5 depending on hours; 720*0.00699 ≈ 5.03h, student calculated 3.5h due to arithmetic error). In (c), the student forgot to multiply A_pay by the other series components.
> ## Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (3/5, Proficient)

You chose a relevant pattern, but inverted the states: Closed allows normal traffic, while Open blocks calls. For Excellent, correct the state mechanism and include tuning considerations or drawbacks.

*Assessor reasoning:* The student inverted the fundamental states of the Circuit Breaker (stated Open passes calls and Closed blocks them). Furthermore, no drawback or tuning consideration was provided.
> ## Question 4: "In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Proficient)

You justified reasonable choices, but misapplied the CAP theorem. Distributed systems cannot forfeit partition tolerance; you must trade Availability for Consistency (CP). Correcting this precision is required for Excellent.

*Assessor reasoning:* The student misinterprets CAP by claiming a distributed network can 'give up partition tolerance' (CA) during network partitions; one must choose CP (sacrificing availability).
> ## Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR sections are well-structured and scenario-specific. To reach Excellent, include at least one negative consequence or trade-off (such as eventual consistency or operational overhead) alongside the positive outcomes.

*Assessor reasoning:* Context, Decision, and Consequences are present and specific, but Consequences are entirely positive; no negative consequence or trade-off (e.g. operational complexity, eventual consistency) is stated.
> ## Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing was clear and met word limits. To earn full marks, ensure all in-text citations (such as [2] in Question 4) have corresponding full bibliographic entries in your References section.

*Assessor reasoning:* Clear writing within word limits, but citation [2] is cited in Question 4 without appearing in the References section.
> ## Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> ## References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed. Upper Saddle River, NJ, USA: Addison-Wesley, 2012."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | ## Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | ## Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | ## Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | ## Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | ## Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | ## Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | ## References |

## Technical issues

- ## Question 3: Arithmetic error in (b): 0.00699 * 720 = 5.03 hours, not 3.5 hours. In (c), only the payment subsystem availability was reported instead of multiplying by the other series components (0.9995 * 0.999 * 0.9995 * 0.999975 = 99.80%).
- ## Question 4: Circuit Breaker states are inverted: Closed is normal operation where calls pass through; Open trips and fails fast.
- ## Question 5: Network partitions cannot be 'given up' in distributed systems under CAP; when a partition occurs, one must trade off Availability for Consistency (CP).

## Next steps

1. Ensure quality attribute response measures use objective, quantified metrics (e.g., uptime percentages or MTTR) rather than subjective phrasing like 'most of the time'.
2. Review core resilience and distributed systems concepts, specifically the correct state machine for Circuit Breakers and how network partitions dictate trade-offs under CAP.
3. Complete end-to-end reliability calculations by multiplying all series subsystem availabilities, and always include balanced consequences (positive and negative) in ADRs.

---
<sub>Run Input_4_d-Run_1-Eff_low-261118-145708 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8098/4720 | cost $0.013611 (incl. $0.001628 for the reused reference rubric+task structure) | 21.42s</sub>
