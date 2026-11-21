# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 26 / 40 (65%)**

You demonstrated strong architectural reasoning in your modular monolith analysis (Question 2) and structured your ADR well in Question 6. To improve future submissions, focus on quantitative precision in your calculations (Question 3) and quality attribute response measures (Question 1). Additionally, refine technical accuracy regarding distributed resilience patterns (Question 4) and CAP trade-offs (Question 5), while adhering strictly to word limits and citation requirements.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 4 / 8 | 4 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You selected relevant quality attributes and developed a strong, measurable performance scenario. In Question 1, however, your availability response measure ('stay up most of the time') is qualitative. To reach Excellent, specify an exact, quantifiable response measure for both scenarios (such as achieving 99.9% uptime or defining a maximum permissible downtime per month).

*Assessor reasoning:* Performance and availability are appropriate and justified from the scenario. The performance scenario is complete with a measurable metric. However, the availability scenario's response measure ('stay up most of the time') is qualitative and non-measurable.
> ## Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work in Question 2! You provided a well-justified recommendation for a modular monolith, explicitly tailoring trade-offs to the five-developer team size and operational constraints while clearly acknowledging key downsides like shared failure domains.

*Assessor reasoning:* A modular monolith is clearly recommended and justified using scenario-specific trade-offs: team size (5 developers) versus operational overhead, and addressing single-VM and deployment downtime. Trade-offs and downsides (shared failure domain, lack of independent scaling) are acknowledged.
> ## Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  

### C3 Q3 Availability calculation (4/8, Developing)

You solved part (a) correctly. In part (b), check your arithmetic (0.00699 × 720 equals 5.03 hours). For part (c), ensure the parallel payment subsystem is multiplied back into the remaining series components. To reach Proficient, apply the complete series calculation across all required parts.

*Assessor reasoning:* Part (a) is correct (99.30%). In part (b), an arithmetic error occurs: 0.00699 × 720 equals 5.03 hours, not 3.5. In part (c), the student omitted the other series components, equating overall availability solely to the parallel payment provider availability.
> ## Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

In Question 4, you appropriately selected the Circuit Breaker pattern for external outages. However, your explanation inverted the state machine: requests pass through when Closed and fail fast when Open. To reach Excellent, describe these states accurately and include tuning considerations or drawbacks, such as timeout thresholds.

*Assessor reasoning:* Although the Circuit Breaker is an appropriate pattern and applied to the outage, the explanation inverts the state machine (stating calls pass through when Open and fail fast when Closed). Furthermore, no drawback or tuning consideration is provided.
> ## Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your trade-off choices and recommendation of Redis caching for menu browsing in Question 5 were well-reasoned. To reach Excellent, clarify that partition tolerance cannot be sacrificed during network partitions under the CAP theorem, and propose a concrete technique (such as a Saga or two-phase commit) for order placement and payment.

*Assessor reasoning:* Both trade-off choices are sound, and Redis caching is properly suggested for menu browsing. However, no concrete technique is given for order placement/payment, and CAP is misconstrued by stating partition tolerance can be traded off during a network partition.
> ## Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

In Question 6, your ADR Context and Decision sections are clear and tailored to CampusEats. However, the Consequences section only listed benefits. To reach Excellent, ensure you also document negative consequences or operational trade-offs, such as increased broker management or handling eventual consistency.

*Assessor reasoning:* Context and Decision are clear, well reasoned, and specific to the scenario. However, the Consequences section is strictly one-sided, omitting any negative consequences or architectural trade-offs (such as message broker maintenance or eventual consistency handling).
> ## Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing is clear with correct structural headings. To reach Excellent, keep all responses strictly within the 150-word limit (Question 2 exceeded this at ~188 words) and ensure every in-text citation, such as [2] in Question 4, is fully documented in your reference list.

*Assessor reasoning:* The submission uses required headings and clear language. However, Question 2 exceeds the 150-word limit (~188 words), and citation [2] referenced in Question 4 is missing from the reference list.
> ## Question 2: "I recommend against a full microservices rewrite for the next 12 months."  

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

- ## Question 1: The response measure for the availability scenario ('stay up most of the time') is qualitative and not measurable.
- ## Question 3: Arithmetic calculation error in part (b): 0.00699 × 720 hours equals 5.03 hours, not 3.5 hours.
- ## Question 3: In part (c), end-to-end order placement availability was calculated using only the payment subsystem (99.9975%), omitting the other three series components.
- ## Question 4: Circuit breaker states are inverted: normal requests pass through when Closed, and requests fail immediately when Open.
- ## Question 4: No drawback or tuning consideration is stated for the Circuit Breaker pattern.
- ## Question 5: The CAP theorem explanation incorrectly states that partition tolerance can be sacrificed to achieve consistency and availability during a network partition.
- ## Question 5: No concrete technique is proposed for placing and paying for an order.
- ## Question 6: The ADR lists only positive consequences; negative consequences or operational trade-offs are omitted.
- ## References: Citation [2] is referenced in Question 4 but omitted from the reference list.

## Next steps

1. Recalculate end-to-end availability by ensuring parallel subsystems are factored back into the broader series system formula.
2. Review distributed systems definitions, specifically the state transitions of the Circuit Breaker pattern and CAP theorem implications during network partitions.
3. Ensure architectural evaluations consistently document negative trade-offs and operational overhead alongside positive outcomes in ADRs.

---
<sub>Run Input_4_d-Run_1-Eff_high-261116-121554 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8252/15302 | cost $0.053409 (incl. $0.001628 for the reused reference rubric+task structure) | 64.14s</sub>
