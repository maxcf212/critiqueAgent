# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 19 / 40 (47.5%)**

You make a strong, scenario-specific case for a modular monolith in Question 2, including team-size and operational trade-offs. To reach higher rubric levels, make both Question 1 scenarios measurable and correct the availability, circuit-breaker, and CAP reasoning. Your ADR and references also need completing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 2 / 8 | 2 / 8 |
| C4 Q4 Resilience pattern | Developing | 1 / 5 | 1 / 5 |
| C5 Q5 Consistency and availability | Developing | 2 / 6 | 2 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

Question 1 links performance and availability to the lunch-hour scenario, and the p95 target is measurable. However, “most of the time” is not measurable, and the availability scenario focuses on browsing rather than order placement. Quantify the target and complete all six scenario parts.

*Assessor reasoning:* The attributes are relevant and tied to the lunch-hour scenario, and the performance measure is measurable. The availability scenario lacks a measurable response measure; “most of the time” is not quantifiable. Its response also focuses on menu browsing rather than maintaining order-placement availability.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your Question 2 recommendation of a modular monolith is clear and specific to the five-person team and existing performance and deployment problems. You discuss relevant trade-offs and acknowledge that modules cannot be scaled independently; this meets the top rubric level.

*Assessor reasoning:* The recommendation is clear and addresses team size, operational overhead, the single-VM performance problem, and deployment downtime. It gives a relevant downside of the modular monolith. The proposed scaling and rolling-deployment remedies are plausible.
> Question 2: "Instead the existing application should be restructured into a modular monolith"  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (2/8, Developing)

In Question 3, your series-availability method and product are essentially correct. Recheck part (b): the downtime is about 5.03 hours per month. In part (c), multiply the redundant payment availability by the other required component availabilities; the resulting end-to-end downtime is about 1.46 hours per month.

*Assessor reasoning:* The series availability method and product are essentially correct, but the monthly downtime arithmetic is wrong: it is about 5.03 hours, not 3.5. For (c), the redundant payment availability must still be multiplied by the other required component availabilities. End-to-end availability is about 99.80%, with about 1.46 hours of downtime monthly; the stated answer is incorrect.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (1/5, Developing)

You chose an appropriate pattern and gave a threshold and recovery trial in Question 4, but the states are reversed. Closed permits calls, Open fails fast, and Half-Open allows trial calls. Apply this sequence to the payment-provider outage and add a drawback or tuning consideration.

*Assessor reasoning:* The pattern is appropriate and a threshold and recovery trial are described, but the state transitions are reversed. A breaker normally starts Closed, transitions to Open to fail fast, then to Half-Open to test recovery. The incorrect mechanism undermines the explanation and outage application. No drawback or tuning consideration is stated.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  
> Question 4: "After a wait period the breaker goes Half-Open"  

### C5 Q5 Consistency and availability (2/6, Developing)

Your Question 5 menu choice includes a concrete cache technique and stale-data trade-off. For payments, CAP requires a consistency–availability trade-off during a partition; you cannot give up partition tolerance during that partition. Name a concrete technique for the payment choice.

*Assessor reasoning:* The menu choice is supported by a concrete cache technique and an appropriate stale-data trade-off. The payment choice is plausible, but CAP is misapplied: during a partition a system must trade consistency against availability; it cannot give up partition tolerance in that circumstance. No concrete payment technique is named.
> Question 5: "Menu browsing: I would favour availability."  
> Question 5: "Placing and paying for an order: I would favour consistency"  
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Question 6 includes scenario-specific Context, Decision, and Consequences, including benefits of publishing an OrderPaid event. Add at least one negative consequence, such as duplicate-delivery or queue/worker operational concerns, to meet the top rubric level.

*Assessor reasoning:* Context, decision, and consequences are present and specific, with several benefits. No negative consequence is acknowledged, such as duplicate delivery, ordering concerns, or queue/worker operational overhead.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet"  

### C7 Communication and format (2/4, Developing)

Your writing is generally clear and uses question headings. Question 1 appears to exceed the 150-word limit, and reference [2], cited in Question 4, is missing from the reference list. Check word limits, complete the references, and state assumptions.

*Assessor reasoning:* Writing is generally clear and the required question headings are used. However, reference [2] is cited but absent from the reference list, and the availability scenario is incomplete. Question 1 appears to exceed the 150-word limit. These citation and format issues prevent a higher mark.
> Question 1: "The scenarios below use the six-part form from [1]."  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | no | References |

## Technical issues

- Question 1: The availability scenario's response measure, “most of the time,” is not measurable.
- Question 3: Part (b) arithmetic is incorrect: (1 − 0.9930112435) × 720 is approximately 5.03 hours, not 3.5.
- Question 3: Part (c) treats the probability of both payment providers failing as the whole order-placement failure probability. Multiplying the other required component availabilities gives end-to-end availability about 99.80% and monthly downtime about 1.46 hours.
- Question 4: Circuit-breaker states are reversed: Closed permits calls, Open fails fast, and Half-Open permits trial calls.
- Question 5: CAP is misapplied: during a network partition, a distributed system cannot guarantee both consistency and availability; it cannot simply give up partition tolerance during the partition.
- Question 5: No concrete technique is named for the payment consistency choice.
- Question 6: Consequences give benefits only and omit a negative consequence.
- References: Reference [2] is cited in Question 4 but is missing from the reference list; assumptions are not stated.

## Next steps

1. In Question 1, keep the measurable p95 performance target and define availability with a quantified order-placement target over a stated period. Ensure each scenario includes all six parts and explains why the attribute matters.
2. In Questions 3–5, show the availability calculations carefully, including all required components in part (c). Correct the circuit-breaker states in Question 4 and explain the consistency–availability trade-off during a partition in Question 5; name a concrete payment technique.
3. In Question 6, add a specific negative consequence of the queue decision. Check every citation against the reference list, state assumptions where relevant, and keep each answer within 150 words.

---
<sub>Run Input_4_d-Run_3-Eff_low-261118-145226 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8503/5339 | cost $0.003358 (incl. $0.001628 for the reused reference rubric+task structure) | 25.78s</sub>
