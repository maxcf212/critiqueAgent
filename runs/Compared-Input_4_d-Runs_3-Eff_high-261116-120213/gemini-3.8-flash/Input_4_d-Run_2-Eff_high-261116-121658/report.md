# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 26 / 40 (65%)**

You demonstrated strong architectural judgment in your architectural style recommendation in Question 2 and ADR structure in Question 6. To elevate your work, focus on technical precision: quantify quality attribute response measures, verify multi-component availability calculations, accurately define core distributed mechanisms (such as circuit breaker states and CAP trade-offs), and record both positive and negative consequences in your architecture decisions.

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

You chose and justified suitable attributes. To reach Excellent, ensure all six scenario parts are complete and measurable. In Question 1, replace subjective phrases like 'stay up most of the time' with a specific, quantifiable metric, such as a percentage uptime or a maximum allowed recovery duration.

*Assessor reasoning:* Performance and availability are well-chosen and justified. However, the availability scenario's response measure is vague and unmeasurable rather than quantified.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You achieved Excellent here by providing a well-justified recommendation for a modular monolith. You effectively grounded your trade-offs in scenario constraints (team size and VM setup) and explicitly acknowledged key architectural downsides.

*Assessor reasoning:* Recommends a modular monolith with two clear trade-offs tailored to team size, VM setup, and deployment issues. Downsides are explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (4/8, Developing)

Your series formula in (a) was correct. To reach Proficient or Excellent, avoid arithmetic slips in (b) (0.00699 × 720 = 5.03 hours) and calculate true end-to-end availability in (c) by combining the redundant payment subsystem with the remaining series components.

*Assessor reasoning:* Part (a) is correct. Part (b) contains an arithmetic error (0.00699 × 720 = 5.03 h, not 3.5 h). Part (c) equates payment availability to end-to-end availability.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

You appropriately chose the circuit breaker pattern for external outages. To advance to Excellent, reverse the inverted state definitions—calls pass through in Closed and fail fast in Open—and discuss tuning parameters (e.g., failure thresholds) or operational drawbacks.

*Assessor reasoning:* Identifies circuit breaker and applies it, but inverts the fundamental Open and Closed states. Additionally, no drawback or tuning consideration is provided.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Proficient)

You selected sensible attributes and appropriately identified caching for browsing. For Excellent, apply CAP theorem correctly by recognizing that network partitions cannot be chosen away in distributed systems, and provide a concrete technique (such as the Saga pattern or 2PC) for orders and payments.

*Assessor reasoning:* Choices are sensible and caching is named for browsing. However, CAP theorem is misstated by claiming CA can be chosen over P, and no technique is named for orders/payments.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your Context, Decision, and positive consequences were clearly articulated and grounded in CampusEats. To reach Excellent, document the negative consequences or trade-offs introduced by your decision, such as eventual consistency delays or message broker maintenance overhead.

*Assessor reasoning:* Context, decision, and positive consequences are well specified and grounded in the scenario. However, consequences are entirely one-sided, omitting negative impacts.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your response used clear headings and structure. To achieve Excellent, ensure all responses remain strictly under 150 words (Question 2 was 178 words) and verify that all cited sources, such as reference [2], appear in the reference list.

*Assessor reasoning:* Headings are followed and writing is structured, but Question 2 exceeds the 150-word limit (178 words) and reference [2] is missing from the reference list.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 1: Availability scenario response measure ('most of the time') is subjective and non-measurable.
- Question 3: Calculation error in (b): 0.00699 * 720 = 5.03 hours, not 3.5. In (c), end-to-end availability omitted the remaining components, mistakenly treating 99.9975% payment availability as overall availability.
- Question 4: Circuit breaker states are inverted: Open was described as normal flow and Closed as failing fast. Drawbacks/tuning considerations were also omitted.
- Question 5: Misapplication of CAP theorem asserting that a partitioned distributed system can choose consistency and availability over partition tolerance; no concrete technique was provided for orders/payments.
- Question 6: No negative consequences or trade-offs (e.g., message queue maintenance overhead, eventual consistency) are documented in the ADR.
- References: Source [2] cited in Question 4 is omitted from the reference list.

## Next steps

1. Review resilience patterns and distributed theory to correctly map circuit breaker states and CAP partition trade-offs.
2. Revisit availability calculations to ensure redundant subsystems are properly integrated into end-to-end series calculations.
3. Audit responses against submission constraints to keep every answer under 150 words and include all cited sources in the bibliography.

---
<sub>Run Input_4_d-Run_2-Eff_high-261116-121658 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8095/15283 | cost $0.053221 (incl. $0.001628 for the reused reference rubric+task structure) | 60.39s</sub>
