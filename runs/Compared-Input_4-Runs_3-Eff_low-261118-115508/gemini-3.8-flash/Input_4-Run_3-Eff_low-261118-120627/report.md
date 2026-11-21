# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You demonstrated a strong grasp of architectural trade-offs, styles, and patterns across the CampusEats scenario. Your recommendation in Question 2 and referencing were particular highlights. To reach the highest grade band, focus on using precise quantitative response measures, avoiding common misconceptions regarding the CAP theorem, ensuring end-to-end calculations account for all series components, and strictly adhering to specified word limits.

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

You justified two relevant quality attributes well. However, in Question 1, stating that the system should 'stay up most of the time' is subjective. To achieve Excellent, ensure both response measures are quantitatively measurable (e.g., specifying percentage uptime or maximum allowed downtime).

*Assessor reasoning:* Performance and availability are well chosen, but the availability response measure ('stay up most of the time') is completely unmeasurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work. You provided a well-justified recommendation for a modular monolith using scenario-specific trade-offs such as team size and deployment limits, while explicitly acknowledging downsides like shared process crashes.

*Assessor reasoning:* Clear recommendation (modular monolith) justified by two detailed scenario-specific trade-offs (team size, VM scaling/deployment issues), with explicit downsides acknowledged.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) were calculated correctly. In part (c), you equated total system availability directly to the redundant payment subsystem (99.9975%). To reach Excellent, complete the series calculation by multiplying this result by the remaining three system components.

*Assessor reasoning:* Parts (a) and (b) are correct. In (c), the student forgot to multiply the remaining three components by the new payment availability (0.9995 * 0.999 * 0.9995 * 0.999975 = 99.80%), treating A_pay as the entire system availability.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You named and clearly explained the circuit breaker pattern and applied it well to the outage. To reach Excellent, include at least one tuning consideration or drawback, such as threshold configuration challenges or fallback user experience.

*Assessor reasoning:* The circuit breaker pattern is well explained and applied to the scenario, but no drawback or tuning consideration (e.g. threshold tuning, fallback UX) is explicitly discussed.
> Question 4: "In the outage last month the breaker would have opened within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (4/6, Proficient)

You selected sound techniques for both cases, but stated that payments 'give up partition tolerance'. In distributed systems, network partitions are inevitable; you trade off consistency or availability during a partition. Frame the CAP theorem around this trade-off for Excellent.

*Assessor reasoning:* Choices and concrete techniques are sound, but the CAP explanation is flawed: network partitions cannot be chosen away in distributed networks ('give up partition tolerance' is a misconception).
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR had clear, scenario-specific Context, Decision, and Consequences sections. To achieve Excellent, avoid a one-sided evaluation by including at least one negative consequence or trade-off, such as eventual consistency delays or operational complexity.

*Assessor reasoning:* Context, Decision, and Consequences are present and specific, but Consequences only lists positive effects; no negative consequence (e.g., added architectural complexity, eventual consistency/delayed confirmation) is included.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your document was well structured with precise terminology and appropriate IEEE citations. However, Question 2 exceeded the 150-word limit. To attain Excellent, ensure all individual answers strictly adhere to the word constraints.

*Assessor reasoning:* Question 2 exceeds the 150-word limit (approx. 200 words). Headings, precision, and IEEE citations are otherwise well handled.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 1: Availability response measure ('stay up most of the time') is vague and unquantified.
- Question 3: In part (c), total system availability was equated directly to the redundant payment subsystem availability (0.999975) instead of multiplying by the other three components.
- Question 5: Misinterprets CAP theorem by claiming one can choose 'CA' over 'P' in a distributed network scenario where partitions are inevitable.

## Next steps

1. Quantify all quality attribute response measures with explicit, testable metrics rather than subjective phrasing.
2. Recalculate composite system availability by multiplying redundant subsystems back into the overall series formula.
3. Ensure architectural evaluations and ADRs explicitly document negative trade-offs, failure modes, or tuning complexities alongside benefits.

---
<sub>Run Input_4-Run_3-Eff_low-261118-120627 | marking=google/gemini-3.8-flash, feedback=google/gemini-3.8-flash | tokens in/out 8067/4361 | cost $0.012243 (incl. $0.001628 for the reused reference rubric+task structure) | 21.03s</sub>
