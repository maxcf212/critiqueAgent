# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 25 / 40 (62.5%)**

You demonstrated strong architectural reasoning in Question 2, effectively tailoring your modular monolith recommendation to CampusEats. Questions 1, 5, and 6 also showed solid situational understanding. To reach higher bands across all areas, focus on precise calculation modeling for composite systems, ensure resilience pattern state mechanics are accurate, verify all response measures are quantifiable, and always balance design decisions with explicit negative consequences.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose well-justified attributes, and your performance scenario was well-defined. However, your availability response measure ('stay up most of the time') was unmeasurable. To reach Excellent, ensure both response measures specify concrete, quantifiable metrics, such as a target MTTR, percentage uptime (e.g., 99.9%), or maximum allowed minutes of downtime.

*Assessor reasoning:* Suitable attributes are selected and justified. The performance scenario is fully specified with measurable metrics. However, the availability scenario's response measure is vague and unmeasurable, lacking clear downtime, MTTR, or degraded-availability percentages.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You achieved an Excellent mark here. Your recommendation for a modular monolith was strongly argued using realistic CampusEats trade-offs, particularly team size and operational overhead, and you appropriately acknowledged its downsides. Keep applying this level of context-specific justification to all design questions.

*Assessor reasoning:* The recommendation for a modular monolith is clearly argued with two solid trade-offs tailored to CampusEats: small team operational overhead and resolving root issues via horizontal scaling and deployment changes. Downsides are explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  

### C3 Q3 Availability calculation (3/8, Developing)

You calculated part (a) accurately. To reach Proficient or Excellent, ensure arithmetic in part (b) is checked (0.00699 × 720 = 5.03 hours) and correctly model system topology in part (c) by chaining the parallel payment availability in series with the upstream order-placement components.

*Assessor reasoning:* Part (a) is correct. Part (b) contains an arithmetic error (0.00699 × 720 is 5.0 hours, not 3.5). Part (c) incorrectly takes the redundant payment provider availability as the entire order placement availability, neglecting the upstream components in series.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit Breaker was an appropriate pattern choice. To reach Proficient or Excellent, ensure the operational states are correctly described: Closed represents normal traffic flow, while Open trips to block calls. Additionally, discuss practical tuning considerations or drawbacks, such as timeout thresholds and fallback responses.

*Assessor reasoning:* While Circuit Breaker is an appropriate pattern, the explanation fundamentally inverts the state transitions: normal operation is Closed and tripped is Open. Additionally, no tuning considerations or drawbacks (such as fallback handling or setting sensitive thresholds) are discussed.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices and the Redis caching technique for menu browsing were sound. To reach Excellent, address CAP theorem mechanics accurately—network partitions cannot be 'given up' in distributed systems—and provide a concrete implementation technique for payment consistency, such as two-phase commit or a saga pattern.

*Assessor reasoning:* Both trade-off choices are sound, but the CAP theorem explanation relies on the misconception that partition tolerance can be sacrificed during a partition. Furthermore, a concrete technique is given for menu browsing (Redis cache) but omitted for order payment.
> Question 5: "we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your Context, Decision, and positive Consequences were clearly articulated and relevant to the scenario. To reach Excellent, avoid one-sided consequences by explicitly documenting negative trade-offs, such as message broker operational overhead, eventual consistency delays, or handling duplicate order events.

*Assessor reasoning:* Context, Decision, and Consequences are clearly articulated and specific to CampusEats. However, the consequences section only lists positive outcomes and fails to note any negative consequences or architectural trade-offs, such as broker management or duplicate deliveries.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves. Outlets that are briefly offline still receive their orders"  

### C7 Communication and format (3/4, Proficient)

Your response was well-structured with clear headings. To achieve Excellent, ensure all answers stay strictly within the 150-word limit (Question 2 reached 179 words), verify that every in-text citation (such as [2]) appears in your reference list, and maintain precise terminology throughout.

*Assessor reasoning:* Writing is generally clear and structured under the required headings. However, Question 2 significantly exceeds the 150-word limit (179 words), citation [2] is referenced in Question 4 but omitted from the reference list, and state terminology is inverted in Question 4.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months. Instead the existing application should be restructured into a modular monolith"  

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

- Question 1: Availability response measure ('most of the time') is subjective and not measurable.
- Question 3: Part (b) calculation 0.00699 * 720 equals 5.03 hours, not 3.5 hours.
- Question 3: Part (c) fails to combine redundant payment availability with other components to calculate end-to-end availability (~99.80%).
- Question 4: Circuit breaker operational states are inverted (described Open as normal and Closed as tripped).
- Question 5: Partition tolerance cannot be 'given up' in distributed systems; no concrete implementation technique was named for payments.
- Question 6: ADR consequences omit negative trade-offs (e.g., broker operational overhead, eventual consistency).
- References: Citation [2] appears in text but is missing from the reference list.

## Next steps

1. In Question 3, review availability calculations for composite systems: compute parallel redundancy first, then multiply upstream series components to determine end-to-end availability.
2. Review the state lifecycle of resilience patterns like the Circuit Breaker in Question 4, ensuring you distinguish normal operating states (Closed) from tripped states (Open).
3. Audit your ADRs and scenarios in Questions 1 and 6 to ensure quality attribute response measures are numerically measurable and consequences include negative trade-offs.

---
<sub>Run Input_4_d-Run_3-Eff_high-261116-121758 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8198/13000 | cost $0.044737 (incl. $0.001628 for the reused reference rubric+task structure) | 55.05s</sub>
