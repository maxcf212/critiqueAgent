# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You demonstrated strong architectural reasoning throughout your answers, especially in your well-justified style recommendation in Question 2 and resilience mechanism in Question 4. To push your work to the highest level across all criteria, ensure your quality attribute response measures are quantitatively measurable, verify end-to-end system calculations rather than subsystem metrics, correctly apply theoretical models like CAP, and present balanced trade-offs including negative consequences in your architecture decision records.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You selected two relevant quality attributes and provided a complete, measurable performance scenario. However, your availability response measure ('stay up most of the time') was subjective. To reach Excellent, ensure both response measures use objective, quantified metrics (such as target percentage uptime or MTTR).

*Assessor reasoning:* Two attributes are justified from the scenario. However, while the performance scenario is fully specified and measurable, the availability scenario's response measure ('stay up most of the time') is vague and not measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work recommending a modular monolith. You grounded your justification in realistic scenario constraints (team size of five, single VM bottleneck) and explicitly addressed architectural trade-offs, including whole-process failure and coupled scaling.

*Assessor reasoning:* The modular monolith recommendation is strongly justified using scenario-specific constraints: developer team size (5 developers) versus microservices overhead, single VM bottleneck, and deployment downtime. The trade-off of whole-process failure and coupled scaling is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  

### C3 Q3 Availability calculation (5/8, Proficient)

You showed clear working and achieved full marks on parts (a) and (b). In part (c), you correctly calculated parallel redundancy for payments, but equated it to total system availability. To reach Excellent, multiply the parallel subsystem result by the remaining series components for end-to-end availability.

*Assessor reasoning:* Parts (a) and (b) are completely correct with working shown to requested precision. In part (c), the parallel availability of the payment provider is calculated correctly, but the student mistakenly equates it to the end-to-end availability, omitting the remaining series components.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You correctly identified the Circuit Breaker pattern, explained its three states clearly, and applied it effectively to the payment outage scenario. To achieve Excellent, discuss at least one drawback or tuning consideration, such as threshold configuration or fallback complexity.

*Assessor reasoning:* The Circuit Breaker pattern is correctly named, its three states are clearly explained, and it is well applied to the payment outage. However, no tuning considerations or drawbacks (such as threshold tuning or operational overhead) are provided.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure. Calls from the order service to the payment provider are wrapped in a breaker"  

### C5 Q5 Consistency and availability (4/6, Proficient)

You made sensible choices for browsing and ordering, supported by concrete techniques like Redis caching and idempotency keys. However, your CAP theorem explanation was inaccurate; network partitions cannot be forfeited. To reach Excellent, correctly apply CAP by choosing between consistency and availability (CP vs AP) under partition conditions.

*Assessor reasoning:* Architectural choices for browsing and ordering are sound and concrete techniques (Redis cache TTL, idempotency key) are given. However, the CAP theorem explanation is flawed: distributed systems cannot forfeit partition tolerance to choose CA when network partitions occur.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR successfully includes Context, Decision, and Consequences specific to CampusEats. However, your consequences only highlighted positive outcomes. To reach Excellent, provide a balanced view by including at least one negative consequence, such as message broker operational overhead or handling asynchronous failures.

*Assessor reasoning:* Context, Decision, and Consequences are present and tailored to the scenario. However, the consequences are entirely positive, omitting any negative consequences such as operational overhead of RabbitMQ or message-ordering challenges.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves. Outlets that are briefly offline still receive their orders"  

### C7 Communication and format (3/4, Proficient)

Your submission was clearly structured, used required headings, and properly cited sources in IEEE format. However, Question 2 exceeded the strict 150-word limit at approximately 179 words. To reach Excellent, ensure every individual response adheres to the word constraints.

*Assessor reasoning:* Clear writing and required headings are used, and external sources are cited in IEEE style. However, Question 2 exceeds the 150-word limit (approximately 179 words).
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 1: Availability response measure ('stay up most of the time') is subjective and not quantitatively measurable.
- Question 3: In part (c), 99.9975% is only the availability of the redundant payment subsystem; end-to-end availability must multiply by the remaining series components (0.9995 × 0.999 × 0.9995 × 0.999975 ≈ 99.80%), yielding ~1.5 hours/month downtime instead of 0.018 hours.
- Question 4: Failed to provide any drawback or tuning consideration for the Circuit Breaker pattern.
- Question 5: Incorrect application of CAP theorem claiming to choose consistency and availability while forfeiting partition tolerance during a network partition.
- Question 6: ADR Consequences section omits negative consequences (e.g., added operational complexity, asynchronous failure handling).
- Question 2: Question 2 exceeds the strict 150-word limit at approximately 179 words.

## Next steps

1. Ensure all quality attribute response measures are specific and quantitatively measurable rather than subjective (e.g., in Question 1, specify an exact uptime percentage or recovery time limit).
2. In end-to-end availability calculations like Question 3(c), incorporate the redundant subsystem back into the overall series equation rather than treating subsystem availability as total system availability.
3. Review the constraints of the CAP theorem for distributed systems, recognizing that network partitions are inevitable and the trade-off is strictly between consistency (CP) and availability (AP).

---
<sub>Run Input_4-Run_2-Eff_high-261115-174559 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8281/14953 | cost $0.052122 (incl. $0.001628 for the reused reference rubric+task structure) | 76.59s</sub>
