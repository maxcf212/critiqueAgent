# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You demonstrated strong architectural reasoning, especially in Question 2 where you effectively justified a modular monolith with scenario-specific trade-offs. To improve, focus on technical precision: ensure all quality attribute response measures are quantifiable, carry calculations through to end-to-end results, frame the CAP theorem accurately around partition tolerance, include negative trade-offs in ADRs and pattern analyses, and strictly adhere to word limits across all responses.

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

You justified performance and availability well, providing a complete performance scenario. To reach Excellent, ensure your Question 1 availability response measure is objectively measurable rather than qualitative ('stay up most of the time'), fully completing all six scenario elements.

*Assessor reasoning:* Performance and availability are justified well. The performance scenario is complete with a measurable response measure. However, the availability scenario's response measure ('the system should stay up most of the time') is vague and unmeasurable, placing this in Proficient.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work recommending a modular monolith. You effectively grounded your two trade-offs in CampusEats' specific constraints (team size and operational overhead) while explicitly acknowledging the downsides of shared-process failures.

*Assessor reasoning:* The student provides a clear recommendation (modular monolith) backed by two scenario-specific trade-offs: team size vs. operational overhead and addressing existing bottleneck causes without a rewrite. Architectural downsides are explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) were calculated accurately with clear working. For Excellent, complete part (c) by multiplying the redundant payment provider's availability back into the series chain to find total end-to-end availability and downtime.

*Assessor reasoning:* Parts (a) and (b) are calculated correctly with working. In part (c), the parallel payment provider availability (99.9975%) is mistaken for the overall end-to-end order-placement availability, omitting the series calculation with the other components (should be ~99.80%, ~1.5 h downtime).
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You clearly explained the Circuit Breaker mechanism and effectively mapped it to the lunch outage. To achieve Excellent, discuss at least one operational drawback or tuning consideration, such as threshold limits or recovery timeouts.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern and its operation (Closed, Open, Half-Open) is accurately explained and applied to the lunch outage. However, no drawbacks or tuning considerations (such as setting thresholds or timeout windows) are provided.
> Question 4: "In the outage last month the breaker would have opened within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (4/6, Proficient)

You selected sensible techniques like Redis and idempotency keys. To reach Excellent, apply the CAP theorem correctly: distributed systems cannot forfeit partition tolerance (P), meaning you must choose between consistency (CP) or availability (AP) during a partition.

*Assessor reasoning:* Both choices are sensible and appropriate concrete techniques are identified (Redis cache and idempotency keys). However, the explanation of the CAP theorem invokes the flawed idea of choosing CA and 'giving up partition tolerance' during network partitions.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR successfully includes Context, Decision, and positive Consequences tailored to CampusEats. To attain Excellent, document negative consequences as well, such as added architectural complexity, queue maintenance overhead, or eventual consistency delays.

*Assessor reasoning:* The ADR contains Context, Decision, and Consequences structured specifically around the scenario. However, only positive consequences are detailed; no negative consequences or trade-offs (such as eventual consistency or operational queue management) are listed.
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (3/4, Proficient)

Your formatting, terminology, and IEEE citations were handled well. To reach Excellent, ensure every response remains strictly within the 150-word limit; Question 2 currently exceeds this constraint at approximately 181 words.

*Assessor reasoning:* Formatting is clear, headings are followed, and IEEE citations are correctly used. However, Question 2 exceeds the 150-word limit at approximately 181 words.
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

- Question 1: The availability scenario response measure ('the system should stay up most of the time') is qualitative and cannot be objectively measured.
- Question 3: In part (c), 99.9975% is only the availability of the redundant payment provider subsystem. The end-to-end availability requires multiplying by the remaining series components (0.9995 * 0.999 * 0.9995 = 0.9980), yielding 99.80% and ~1.5 hours of downtime.
- Question 4: No drawback or tuning consideration for the Circuit Breaker pattern was included.
- Question 5: Under the CAP theorem, network partitions cannot simply be chosen away in a distributed system; one cannot choose CA over P when a partition occurs.
- Question 6: The ADR lacks negative consequences (e.g., added architectural complexity, eventual consistency delays, broker maintenance overhead).

## Next steps

1. In Question 1, replace subjective response measures with precise, quantifiable metrics such as explicit uptime percentages or recovery time objectives.
2. In Question 3(c), remember to multiply redundant subsystem availability back into the full series chain to calculate overall end-to-end system availability and downtime.
3. In Questions 4 and 6, consistently balance architectural recommendations by analyzing operational trade-offs, such as tuning parameters (e.g., trip thresholds) and negative consequences.

---
<sub>Run Input_4-Run_1-Eff_high-261115-174457 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8250/12991 | cost $0.044742 (incl. $0.001628 for the reused reference rubric+task structure) | 61.4s</sub>
