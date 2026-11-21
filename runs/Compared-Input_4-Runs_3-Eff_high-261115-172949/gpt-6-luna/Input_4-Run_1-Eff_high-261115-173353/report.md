# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You earned 29/40. Your strongest work is the scenario-specific modular-monolith recommendation in Q2 and the circuit-breaker explanation in Q4. To progress, make Q1’s availability target measurable, correct the end-to-end calculation in Q3(c), apply CAP precisely in Q5, and add balanced consequences in Q6. Also reduce Q2 to the 150-word limit.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You appropriately justified performance using lunch-hour demand and the p95 response target in Q1. Your availability scenario is relevant and has six parts, but “stay up most of the time” is not measurable. The Excellent level requires measurable response measures for both scenarios, such as a numerical availability target and time period.

*Assessor reasoning:* Performance is justified by the lunch-hour demand and current response time, and its scenario has a measurable response measure. The availability scenario includes the six parts and is relevant, but its measure, “most of the time,” is not measurable.
> Question 1: "The p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "The system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is excellent: Q2 links the five-person team, infrastructure overhead, VM and deployment problems, and rewrite cost to clear trade-offs, while acknowledging shared-process risk. Maintain this scenario-specific reasoning; ensure the answer also remains within the 150-word communication limit.

*Assessor reasoning:* The modular-monolith recommendation is supported by scenario-specific trade-offs concerning the five-person team, operational overhead, the VM and deployment problems, and the cost of a rewrite. It also acknowledges reduced independent scaling and shared-process risk.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) in Q3 are correctly calculated and rounded. In part (c), you correctly calculated redundant payment availability but treated it as end-to-end availability. Recalculate using all required components, report approximately 99.80% and 1.5 hours monthly downtime, and show working to reach Excellent.

*Assessor reasoning:* Parts (a) and (b) are correctly calculated and rounded. In (c), the redundant payment-provider availability is calculated correctly, but it is incorrectly reported as end-to-end availability and used directly for system downtime; the other required components are omitted.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.0 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Your Q4 circuit-breaker answer is excellent. You correctly explain the states and mechanism, apply them to the slow payment-provider outage, and give a threshold and time window as tuning considerations. Continue linking the pattern’s behaviour directly to the CampusEats failure scenario.

*Assessor reasoning:* The circuit breaker mechanism and states are explained correctly, applied to the slow-provider outage, and connected to keeping other application functions responsive. The specified failure threshold and time window provide a tuning consideration.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices and techniques in Q5 are reasonable, including cached menus and payment idempotency. However, CAP is stated imprecisely. During a partition, consistency and availability cannot both be guaranteed; consistency-focused behaviour sacrifices availability for affected requests. Correct this explanation to reach Excellent.

*Assessor reasoning:* The choices are reasonable and concrete techniques are named: a cached menu and payment idempotency. However, the CAP explanation is incorrect: during a partition, a system cannot guarantee both consistency and availability; choosing consistency means sacrificing availability for affected requests, not partition tolerance.
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance"  
> Question 5: "each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (3/5, Proficient)

Q6 includes a scenario-specific Context, Decision and Consequences, and correctly identifies faster responses. To reach Excellent, add a negative consequence such as eventual delivery, queue or worker operations, or duplicate handling. Also distinguish persistence of the paid order from delivery of its notification when discussing an offline tablet.

*Assessor reasoning:* Context, decision, and consequences are present and specific to outlet notifications. Consequences are positive only; the record does not acknowledge a negative consequence such as eventual delivery, queue/worker operations, or handling duplicates.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings, generally clear writing, numbered citations and reference list are effective. Q2 is approximately 180 words, so it exceeds the limit. The Excellent level requires every answer to be within 150 words, use precise terminology, retain the required headings, and use IEEE-style citations.

*Assessor reasoning:* The required headings and order are used, writing is generally clear, and external sources have numbered citations and a reference list. Question 2 exceeds the 150-word limit (approximately 180 words), so the answer does not meet the excellent format descriptor.
> Question 2: "A rewrite would freeze feature work for months without directly fixing either problem."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Question 3; References |

## Technical issues

- Question 1: The availability response measure, “stay up most of the time,” is not measurable.
- Question 3: Part (c) reports payment availability as end-to-end order-placement availability. Including the other components gives approximately 99.80% end-to-end availability and 1.5 hours of monthly downtime.
- Question 5: CAP does not permit choosing consistency and availability during a network partition while giving up partition tolerance; consistency-focused behavior sacrifices availability for affected requests during the partition.
- Question 6: An offline tablet can prevent or delay notification, but does not necessarily mean the paid order itself is lost; distinguish order persistence from notification delivery.

## Next steps

1. Revise Q1’s availability scenario with a numerical target, correct Q3(c) by including all end-to-end components, and show the resulting availability and monthly downtime to the requested precision.
2. Correct Q5’s CAP explanation: during a partition, consistency-focused behaviour sacrifices availability for affected requests; retain concrete techniques such as menu caching and payment idempotency.
3. Add a negative consequence and distinguish order persistence from notification delivery in Q6; then edit Q2 to 150 words or fewer and check IEEE citation and formatting requirements.

---
<sub>Run Input_4-Run_1-Eff_high-261115-173353 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8205/9824 | cost $0.005871 (incl. $0.001628 for the reused reference rubric+task structure) | 74.83s</sub>
