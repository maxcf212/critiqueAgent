# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You demonstrated solid architectural intuition and strong contextual application, particularly in your Q2 recommendation of a modular monolith. To reach higher rubric levels, ensure your quality attribute response measures are quantitatively measurable, maintain accuracy across multi-step availability calculations, account for network partitions correctly under the CAP theorem, and include trade-offs such as drawbacks or negative consequences in patterns and ADRs.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You selected appropriate attributes with good justification. However, in Question 1, your response measure ('the system should stay up most of the time') is unmeasurable. To reach Excellent, ensure both scenarios include all six parts with concrete, measurable metrics (e.g., 99.9% uptime or recovery within 5 minutes).

*Assessor reasoning:* Performance and availability are well chosen, but the availability response measure ('up most of the time') is completely unmeasurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. In Question 2, you provided a clear recommendation for a modular monolith strongly grounded in scenario constraints (team size and load issues) while explicitly acknowledging real architectural downsides.

*Assessor reasoning:* Clear recommendation (modular monolith) backed by specific trade-offs (small team, load VM issue, deployment process) with explicit downsides acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Your method was clear, but in Question 3(c) you equated total availability directly to A_pay alone. To reach Excellent, complete the series calculation by multiplying A_pay by the remaining three series components (0.9995 * 0.999 * 0.9995 * 0.999975).

*Assessor reasoning:* In part (c), the student forgot to multiply the remaining three series components (0.9995 * 0.999 * 0.9995 = 0.998), substituting only A_pay into end-to-end availability.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

In Question 4, you accurately selected the Circuit Breaker pattern and applied its mechanism well to the recent outage. To achieve Excellent, also provide at least one drawback or operational tuning consideration (e.g., setting threshold sensitivities or managing fallback states).

*Assessor reasoning:* Circuit Breaker is well-chosen and thoroughly explained/applied, but the student fails to explicitly provide a drawback or tuning consideration.
> Question 4: "In the outage last month the breaker would have opened within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (4/6, Proficient)

You identified sensible choices and concrete techniques in Question 5. However, stating that payments choose CA and 'give up partition tolerance' misinterprets CAP; partitions cannot be chosen away. Excellent requires framing trade-offs strictly between CP and AP during a network partition.

*Assessor reasoning:* Partitions are inevitable in distributed networks, so claiming to 'give up partition tolerance' (CA) during a network partition is a standard CAP misconception.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

In Question 6, your Context, Decision, and positive consequences were clearly articulated and relevant. To achieve Excellent, you must also include at least one negative consequence or trade-off, such as added operational complexity or eventual consistency lag.

*Assessor reasoning:* Context, Decision, and positive consequences are clear, but there are no negative consequences (e.g. increased architectural complexity, eventual consistency lag).
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing and terminology were generally clear and well-structured. However, Question 2 ran to approximately 198 words, exceeding the 150-word limit. To attain Excellent, ensure all responses adhere strictly to the word count constraints.

*Assessor reasoning:* Word limits in Question 2 (~198 words) exceed the 150-word ceiling.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 3: In part (c), total availability was set equal to A_pay alone rather than multiplying A_pay by the other three series components (0.9995 * 0.999 * 0.9995 * 0.999975 = 99.80%).
- Question 5: Under CAP, networks cannot choose 'CA' during a partition; one must choose between CP and AP when a partition occurs.

## Next steps

1. Refine quality attribute scenarios by defining quantified, testable response measures (e.g., uptime percentages or MTTR rather than vague qualitative descriptors).
2. Review CAP theorem fundamentals: remember that network partitions are unavoidable, meaning distributed systems must choose between Consistency (CP) and Availability (AP).
3. Ensure balanced architectural evaluations by explicitly detailing negative consequences or tuning complexities in both pattern descriptions and ADRs.

---
<sub>Run Input_4-Run_2-Eff_low-261118-120607 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8007/4366 | cost $0.012215 (incl. $0.001628 for the reused reference rubric+task structure) | 19.21s</sub>
