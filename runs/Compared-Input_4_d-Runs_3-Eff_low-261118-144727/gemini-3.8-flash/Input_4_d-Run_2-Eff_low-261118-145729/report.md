# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 28 / 40 (70%)**

You demonstrated solid architectural reasoning, clear structure, and strong trade-off analysis in your modular monolith evaluation. However, marks were dropped due to vague response metrics in Q1, an incomplete series calculation in Q3(c), inverted Circuit Breaker states in Q4, a CAP theorem misconception in Q5, one-sided ADR consequences in Q6, and a missing reference citation.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 3 / 5 | 3 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You selected and justified relevant quality attributes well. To reach Excellent, ensure both response measures are strictly measurable; replace vague phrases like 'stay up most of the time' with concrete metrics such as 99.9% uptime or MTTR under 5 minutes.

*Assessor reasoning:* Performance and availability are well chosen and justified. However, the availability response measure ('stay up most of the time') is completely unmeasurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. You provided a clear, scenario-specific recommendation for a modular monolith, effectively balancing team size, scaling, and rolling deployments while explicitly acknowledging process-level crash risks and independent scaling downsides.

*Assessor reasoning:* Clear recommendation (modular monolith) thoroughly justified using specific trade-offs (team size, VM scaling, rolling deployments) with downsides explicitly acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) were executed correctly. To achieve Excellent, carry through the full composite calculation in part (c) by multiplying your parallel payment availability (99.9975%) back into the remaining series components.

*Assessor reasoning:* Parts (a) and (b) are correct. In part (c), the student calculated parallel payment availability but forgot to recombine it with the other components in series (0.9995 * 0.999 * 0.9995 * 0.999975).
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (3/5, Proficient)

You correctly identified the Circuit Breaker pattern. To reach Excellent, accurately describe its mechanism (Closed allows traffic, Open fails fast), and include tuning considerations (e.g., reset timeouts) or drawbacks.

*Assessor reasoning:* Circuit Breaker is appropriate, but the states are reversed (closed passes traffic, open blocks traffic). Tuning considerations or drawbacks are also omitted.
> Question 4: "In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Menu browsing consistency was handled well. For Excellent, apply CAP correctly—distributed systems cannot forfeit partition tolerance (P)—and supply a concrete technique for the payment case (such as distributed transactions or the Saga pattern).

*Assessor reasoning:* Menu browsing is handled well. For payments, claiming to choose CA over P in a distributed system during network partition fundamentally misapplies CAP, and a concrete technique for payments is missing.
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance, so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context and Decision sections were well-tailored to the scenario. To achieve Excellent, balance the Consequences section by including at least one negative trade-off, operational downside, or added complexity alongside the benefits.

*Assessor reasoning:* Context, Decision, and Consequences are present and tailored to the scenario, but consequences are one-sided without any negative trade-offs or operational costs mentioned.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your writing was clear, concise, and followed structural constraints. To achieve Excellent, verify that every in-text citation (such as [2] in Question 4) has a corresponding entry in the reference list.

*Assessor reasoning:* Answers are concise and adhere to word limits and headings, but citation [2] is referenced in Question 4 without appearing in the reference list.
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

- Question 3: In part (c), the parallel payment availability (99.9975%) was treated as the entire system availability instead of multiplying by the remaining series components.
- Question 4: Circuit breaker states are inverted: traffic flows when Closed, and fails fast when Open.
- Question 5: Misinterprets CAP theorem by claiming a distributed network partition can choose 'CA and give up partition tolerance'.

## Next steps

1. Ensure all quality attribute response measures are quantified using precise metrics (e.g., uptime percentages or MTTR) rather than subjective phrasing.
2. Correct technical definitions: in Circuit Breaker, traffic flows during Closed states, and network partitions (P) in distributed systems cannot be opted out of under CAP.
3. When documenting architecture decisions, explicitly identify negative consequences, operational overheads, or trade-offs alongside the benefits.

---
<sub>Run Input_4_d-Run_2-Eff_low-261118-145729 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 7961/4329 | cost $0.012043 (incl. $0.001628 for the reused reference rubric+task structure) | 20.6s</sub>
