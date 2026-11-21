# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 28 / 40 (70%)**

You demonstrated solid architectural reasoning, particularly in Question 2 where your modular monolith recommendation and trade-offs were excellent. Across several technical sections, marks were lost due to minor calculation omissions, inverted definitions, or incomplete trade-off analyses. Focusing on precision in formal models like CAP, exact state definitions in resilience patterns, and balanced evaluations in your ADRs will help you reach top-tier marks.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 3 / 5 | 3 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

You selected appropriate attributes and justified them well. However, your availability response measure ('stay up most of the time') was not measurable. To reach Excellent, specify a concrete, quantified threshold (such as 99.9% uptime or under 5 minutes downtime during peak hours).

*Assessor reasoning:* Suitable attributes are chosen with justification. However, the availability scenario's response measure ('stay up most of the time') is vague and not measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. You provided a clear, context-appropriate recommendation for a modular monolith, effectively linking it to team size and deployment constraints, while explicitly addressing its architectural downsides.

*Assessor reasoning:* A clear modular monolith recommendation is strongly justified using scenario specifics (team size, load profile, VM deployment), and downsides are explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) were executed correctly with clear working. For part (c), you calculated the redundant payment subsystem (0.999975) but forgot to multiply it across the remaining series components (0.9995 * 0.999 * 0.9995 * 0.999975 = 0.99798) to determine overall end-to-end availability.

*Assessor reasoning:* Parts (a) and (b) are correct. In part (c), the student mistakenly treated the payment subsystem's availability (99.9975%) as the entire system's availability, omitting the remaining series components.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (3/5, Proficient)

You correctly identified the Circuit Breaker pattern, but inverted the states: normal operation is 'Closed', whereas the tripped failure state is 'Open'. To achieve Excellent, ensure the operational states are correctly defined and discuss operational drawbacks or tuning considerations (e.g., threshold sensitivity or fallback complexity).

*Assessor reasoning:* The student inverted the standard Circuit Breaker states (confusing Closed and Open), and did not discuss any drawback or tuning consideration.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (4/6, Proficient)

You selected reasonable consistency choices and suitable techniques (Redis caching, ACID transactions). However, claiming to choose CA over P misinterprets CAP in distributed networks; partitions cannot be chosen away, making this a CP trade-off. Correctly applying CAP trade-offs is required for Excellent.

*Assessor reasoning:* Both choices are reasonable and concrete techniques are named (Redis caching, ACID transactions). However, claiming to 'give up partition tolerance' during network partitions misapplies the CAP theorem (networks cannot forfeit partitions; it is a CP choice).
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR sections were clearly structured and tied to the scenario. However, your consequences were entirely positive. To reach Excellent, present a balanced view by explicitly documenting negative trade-offs or operational overheads introduced by the decision (such as managing a RabbitMQ broker).

*Assessor reasoning:* Context, Decision, and Consequences are present and specific, but the consequences are one-sided (no negative consequence or trade-off of introducing RabbitMQ is stated).
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your response maintained precise terminology, adhered to required headings, and stayed within the word limits. To secure full marks in Excellent, ensure every cited source—such as reference [2] in Question 4—is fully listed in your IEEE reference section.

*Assessor reasoning:* Headings are followed and word limits are respected. However, citation [2] is referenced in Question 4 but omitted from the reference list.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3: In part (c), total availability was equated to the redundant payment component availability (0.999975) instead of multiplying across all series components (0.9995 * 0.999 * 0.9995 * 0.999975 = 0.99798).
- Question 4: Inverted Circuit Breaker states: normal operation is 'Closed' and failure-tripped state is 'Open'.
- Question 5: Misinterpreted CAP theorem by claiming to choose CA over P in a distributed system during a network partition.

## Next steps

1. Ensure all quality attribute response measures are quantified with objective metrics (e.g., specific uptime percentages or allowable downtime hours) rather than qualitative descriptions.
2. Review core distributed systems concepts to ensure accurate application of standard models, specifically CAP theorem trade-offs and Circuit Breaker states.
3. Audit your citations and reference lists before submission to verify that every in-text citation key (e.g., [2]) matches an entry in your bibliography.

---
<sub>Run Input_4_d-Run_3-Eff_low-261118-145750 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8012/4488 | cost $0.012677 (incl. $0.001628 for the reused reference rubric+task structure) | 31.95s</sub>
