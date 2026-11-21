# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 31 / 40 (77.5%)**

You demonstrated strong architectural reasoning and produced well-structured solutions grounded in the CampusEats scenario, particularly in your Q2 recommendation and IEEE referencing. To improve, ensure all quality attribute response measures are quantitatively measurable, address architectural trade-offs such as negative consequences in your ADR and resilience pattern drawbacks, and correctly articulate the trade-offs of the CAP theorem. Additionally, double-check end-to-end availability calculations across composite components and observe word count constraints.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 | 6 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You justified performance and availability well for CampusEats and used the six-part structure effectively. However, your availability response measure ('stay up most of the time') was qualitative. To achieve Excellent, ensure both scenarios feature quantitatively measurable response measures (such as 99.9% uptime or under 5 minutes MTTR).

*Assessor reasoning:* Performance and availability are well chosen and justified for CampusEats. Both scenarios use the six-part structure, but the availability response measure ('stay up most of the time') is subjective and not quantitatively measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You provided an excellent recommendation for a modular monolith, effectively linking team size and single-VM constraints to scenario trade-offs while acknowledging scaling and coupling downsides. You met all criteria for Excellent.

*Assessor reasoning:* A modular monolith is clearly recommended and justified using two scenario-specific trade-offs (5-developer team size vs. microservice overhead, and single-VM bottlenecks vs. architectural rewrite). Downside trade-offs regarding process coupling and independent scaling are explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (6/8, Proficient)

Parts (a) and (b) showed clear, correct working. In part (c), you calculated parallel provider availability accurately, but forgot to include the remaining series components in the end-to-end availability calculation and missed requested precision. To reach Excellent, calculate total series availability and adhere to decimal specifications.

*Assessor reasoning:* Parts (a) and (b) are entirely correct with clear working. In part (c), dual-provider availability is correctly calculated, but the student mistakenly equates it to the end-to-end order placement availability, omitting the other series components.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You correctly identified the Circuit Breaker pattern, accurately explained its state transitions, and applied it to the payment outage. To reach Excellent, provide at least one drawback or operational tuning consideration, such as configuring timeout thresholds or handling fallback complexity.

*Assessor reasoning:* The Circuit Breaker pattern is appropriately identified, its state transitions are accurately explained, and it is applied directly to the payment outage. However, no specific drawback or tuning consideration is provided.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

### C5 Q5 Consistency and availability (4/6, Proficient)

You chose sensible trade-offs and provided concrete techniques like Redis TTL and idempotency keys. However, your CAP theorem rationale stated you can drop partition tolerance to achieve CA. To reach Excellent, correctly articulate that partitions are unavoidable in distributed networks, requiring a trade-off between consistency and availability.

*Assessor reasoning:* Both availability and consistency choices are sensible, and concrete techniques (Redis cache TTL and idempotency keys) are provided. However, the CAP theorem explanation is incorrect: in a distributed network, partition tolerance cannot be 'given up' during a network partition.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR included clear Context, Decision, and Consequences sections tailored specifically to CampusEats. However, the consequences were entirely positive. To attain Excellent, also document negative consequences or new trade-offs introduced by the decision, such as increased operational complexity or message broker overhead.

*Assessor reasoning:* Context, Decision, and Consequences are present and tailored to the scenario. However, the consequences section is one-sided, describing multiple benefits but omitting any negative consequences or operational costs.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing was clear, well-structured with required headings, and supported by proper IEEE citations. To reach Excellent, adhere strictly to the 150-word limit (Question 2 was ~187 words) and follow the requested numerical precision in calculation answers.

*Assessor reasoning:* The submission uses standard headings, clear technical writing, and IEEE references. However, Question 2 exceeds the 150-word limit (approximately 187 words), and Question 3(c) neglects the requested precision formatting.
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

- Question 1: The availability scenario response measure ('stay up most of the time') is qualitative and not measurable.
- Question 3: In part (c), total order-placement availability was equated to the redundant payment provider availability alone, ignoring the other three components in series.
- Question 3: Precision instructions were not followed in part (c) (percentage given to 4 decimal places instead of 2, downtime given to 3 decimal places instead of 1).
- Question 4: Failed to discuss a drawback or operational tuning consideration for the Circuit Breaker pattern.
- Question 5: Incorrect CAP formulation: during a network partition, one cannot choose CA and drop P; systems must trade off consistency against availability.
- Question 6: No negative consequences were documented in the ADR.

## Next steps

1. In Question 1 and Question 3, ensure metrics and calculations are precise: quantify qualitative response measures into measurable thresholds and incorporate all series components into availability equations.
2. In Question 4 and Question 6, balance your proposals by explicitly evaluating operational trade-offs, such as tuning thresholds for circuit breakers and negative architectural consequences in your ADR.
3. Review the CAP theorem for Question 5 to correctly reflect that network partitions cannot be chosen away, and adhere strictly to the 150-word limit across all answers.

---
<sub>Run Input_4-Run_3-Eff_high-261115-174715 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8169/12874 | cost $0.044243 (incl. $0.001628 for the reused reference rubric+task structure) | 67.93s</sub>
