# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You demonstrated a strong grasp of architectural trade-offs, particularly in your modular monolith recommendation. However, marks were lost due to an incomplete end-to-end availability calculation in Question 3, a misconception regarding CAP theorem trade-offs in Question 5, an unmeasurable scenario metric in Question 1, one-sided ADR consequences in Question 6, and exceeding the word limit in Question 2.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 4 / 8 | 4 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You selected and justified relevant quality attributes well. However, the availability scenario's response measure ('stay up most of the time') was vague. To reach Excellent, ensure both scenarios include fully quantifiable, measurable response metrics (e.g., uptime percentages or maximum allowable downtime).

*Assessor reasoning:* Performance and availability are well chosen and justified. However, the availability scenario's response measure ('stay up most of the time') is vague and not quantitatively measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. You provided a clear, scenario-tailored recommendation for a modular monolith, supported by concrete trade-offs around team size and operational overhead, while clearly acknowledging its architectural downsides.

*Assessor reasoning:* Recommends a modular monolith with clear trade-offs specific to CampusEats (team size/overhead, single VM vs scaling, deployment issues) and explicitly acknowledges downside.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (4/8, Developing)

Parts (a) and (b) were completed correctly. In part (c), you calculated the parallel payment block correctly but omitted multiplying it by the remaining series components to find total system availability. Showing full end-to-end working for all parts is required for Excellent.

*Assessor reasoning:* Parts (a) and (b) are correct. In part (c), the student forgot to multiply the remaining three series components with the new payment subsystem availability, falsely equating payment subsystem availability to end-to-end availability.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You correctly identified the Circuit Breaker pattern, explained its states, and linked it well to the outage scenario. To reach Excellent, include specific tuning considerations (such as failure rate thresholds or timeout durations) or trade-offs/drawbacks.

*Assessor reasoning:* Identifies Circuit Breaker, explains states accurately and applies it to the outage. However, it fails to state a distinct drawback or tuning consideration (e.g. threshold tuning, fallback handling).
> Question 4: "In the outage last month the breaker would have opened within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your chosen techniques were concrete and suitable. However, stating that a distributed system can choose CA and abandon partition tolerance misapplies CAP. To reach Excellent, correctly frame the theorem around choosing between consistency (CP) or availability (AP) during inevitable network partitions.

*Assessor reasoning:* Choices and concrete techniques are sound, but the explanation of CAP theorem claims one can choose CA and give up partition tolerance in a distributed network scenario, which is a classic misunderstanding of CAP.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Context and Decision were well-articulated and relevant to the scenario. However, your Consequences section only listed positive impacts. To reach Excellent, include at least one negative consequence or trade-off (such as eventual consistency lag or broker operational overhead).

*Assessor reasoning:* Context, Decision, and Consequences are scenario-specific. However, the consequences section only lists positive consequences; no negative consequence or operational cost is identified.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves. Outlets that are briefly offline still receive their orders"  

### C7 Communication and format (3/4, Proficient)

Your response was well-structured with precise terminology and IEEE referencing. To achieve Excellent, strictly adhere to the 150-word constraint across all sections, as Question 2 exceeded this limit.

*Assessor reasoning:* Structure and IEEE citations are followed well. However, Question 2 is approximately 188 words, exceeding the 150-word limit.
> Question 2: "First, team size versus operational overhead."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Question 2 |

## Technical issues

- Question 3: In part (c), total availability was calculated using only the parallel payment block (0.999975) rather than multiplying by the other three series components (0.9995 * 0.999 * 0.9995 * 0.999975 = 0.99798 / 99.80%).
- Question 5: Stating that a distributed system can 'choose consistency and availability and give up partition tolerance' under network partitions misapplies the CAP theorem.

## Next steps

1. Revisit availability mathematics to ensure subsystem calculations (parallel blocks) are integrated back into the overall end-to-end series formula.
2. Clarify your understanding of the CAP theorem: in distributed systems where network partitions are inevitable, trade-offs must be made between consistency and availability (CP vs AP).
3. Ensure all Architecture Decision Records (ADRs) present a balanced view by explicitly documenting negative trade-offs and operational overheads alongside benefits.

---
<sub>Run Input_4-Run_1-Eff_low-261118-120546 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8068/4400 | cost $0.012389 (incl. $0.001628 for the reused reference rubric+task structure) | 21.13s</sub>
