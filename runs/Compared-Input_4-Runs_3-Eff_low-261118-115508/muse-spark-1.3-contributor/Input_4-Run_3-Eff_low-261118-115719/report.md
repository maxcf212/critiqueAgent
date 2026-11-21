# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 27 / 40 (67.5%)**

You produced mostly strong, scenario-grounded analysis with clear strengths in Q2 style and Q3 working. To reach Excellent, make your measures measurable, fix your Q3c chain calculation, correct CAP, and add drawback and negative consequence discussion.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

Well done choosing two relevant attributes with lunch-peak justification, your performance scenario was complete and measurable. For Excellent, make your availability response measure measurable by adding a specific target percentage or time instead of 'stay up most of the time'.

*Assessor reasoning:* Two relevant attributes justified from lunch-peak. Performance scenario complete and measurable. Availability scenario has six parts but response measure is vague and not measurable.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent work in Question 2 recommending a modular monolith with two scenario-specific trade-offs on your 5-person team and single-VM downtime. You acknowledged the downside that modules cannot scale independently and a bug can crash, keep this specificity.

*Assessor reasoning:* Clear modular-monolith recommendation. Two scenario-specific trade-offs: 5-person team overhead and single-VM plus deployment downtime. Downside acknowledged.
> Question 2: "modules cannot be scaled independently, and a bug in one module can still crash"  

### C3 Q3 Availability calculation (5/8, Proficient)

Well done showing working for Q3a 99.30% and Q3b 5.0 hours correctly in Question 3. For Excellent, fix Q3c by multiplying all components, not payment-only 99.9975%, to get about 99.80% and about 1.5h downtime.

*Assessor reasoning:* Parts (a) 99.30% and (b) 5.0 hours correct with working. Part (c) uses payment-only availability, omits other components; correct is ~99.80% and ~1.5h downtime.
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (4/5, Proficient)

Well done naming Circuit Breaker in Question 4 and correctly explaining Half-Open trial calls applied to the 25-min outage. For Excellent, add one explicit drawback or tuning consideration such as threshold, timeout or fallback trade-off.

*Assessor reasoning:* Circuit Breaker appropriate, mechanism correctly explained and applied to 25-min outage. No explicit drawback or tuning trade-off discussed.
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Well done choosing AP for menus and CP for payments with concrete techniques in Question 5. For Excellent, correct CAP to state a partitioned system must tolerate partitions and trades C vs A, so you cannot give up partition tolerance for payments.

*Assessor reasoning:* Both AP for menus and CP for payments choices reasonable with techniques. CAP misused: partition tolerance cannot be given up.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Well done with specific Context and Decision on outlet notification and queue smoothing the lunch peak in Question 6. For Excellent, add at least one negative consequence such as ops complexity, ordering or debugging cost alongside positives.

*Assessor reasoning:* Context and Decision specific to outlet notification. Consequences list only positives; no negative consequence like ops complexity or ordering.
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (3/4, Proficient)

Well done using required headings, clear writing and IEEE references. For Excellent, keep every answer within 150 words, especially Q2 which exceeded at about 182 words, and ensure precise terminology and citation format.

*Assessor reasoning:* Headings and IEEE references present, writing clear, but Q2 ~182 words exceeds 150-word limit.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 3: Part (c) incorrect: end-to-end availability must multiply 0.9995x0.999x0.9995x0.999975=~99.80%, downtime ~1.5h, not 99.9975% / 0.018h.
- Question 5: CAP statement incorrect; partitioned system must tolerate partitions and trades C vs A. Idempotency key does not provide consistency.
- Question 1: Availability response measure not measurable, no target percentage/time.

## Next steps

1. Add a measurable target to your Q1 availability response measure and recalculate Q3c by multiplying all four components.
2. Correct your Q5 CAP explanation to show partition tolerance is mandatory and check your consistency techniques.
3. Add an explicit Q4 tuning drawback and a Q6 negative consequence, and trim Q2 to under 150 words.

---
<sub>Run Input_4-Run_3-Eff_low-261118-115719 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 7906/6773 | cost $0.002547 (incl. $0.001628 for the reused reference rubric+task structure) | 48.34s</sub>
