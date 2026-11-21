# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 28 / 40 (70%)**

You present clear, scenario-specific architecture reasoning, especially in Questions 2 and 4, and your communication meets the rubric’s highest level. To strengthen the work further, make the availability response measurable, correct the end-to-end calculation in Question 3(c), explain CAP accurately, and include a negative consequence in your ADR.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

In Question 1, you chose relevant attributes and gave a measurable performance response measure. Make “stay up most of the time” measurable to meet the next level’s response-measure requirement.

*Assessor reasoning:* Both attributes are relevant and tied to the lunch-hour scenario. The performance scenario has a measurable response measure, but the availability measure (“most of the time”) is not measurable. The six parts are otherwise identifiable in both scenarios.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

In Question 2, your modular-monolith recommendation is grounded in the five-person team and existing bottleneck, and you acknowledge a downside. Keep these scenario-specific trade-offs clear.

*Assessor reasoning:* The recommendation is clear and grounded in team size, the single-VM bottleneck, and deployment downtime. It gives specific trade-offs and acknowledges the downside of a modular monolith.
> Question 2: "Instead the existing application should be restructured into a modular monolith"  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

In Question 3, parts (a) and (b) are correct. In part (c), you report payment-provider availability as end-to-end availability; include all required components and recalculate the result and downtime.

*Assessor reasoning:* Parts (a) and (b) are correct to the requested precision. In (c), the student correctly calculates redundant payment availability but treats it as end-to-end availability, omitting the other required components. The resulting availability and downtime are therefore incorrect.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.0 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (5/5, Excellent)

In Question 4, you explain and apply the Circuit Breaker to the provider outage, and give a threshold and time window as tuning considerations. This is a strong, complete response.

*Assessor reasoning:* The pattern’s states and failure-containment mechanism are accurately explained and applied to the slow-provider outage. The threshold and time window provide a tuning consideration.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  
> Question 4: "for example 50% of calls in 10 seconds"  

### C5 Q5 Consistency and availability (3/6, Proficient)

In Question 5, your menu-cache choice and payment idempotency key are concrete. Correct the CAP explanation: under a partition, consistency and availability trade off; partition tolerance is not the option to give up.

*Assessor reasoning:* The menu choice and cache technique are reasonable, and an idempotency key is a concrete payment retry technique. However, the CAP explanation is incorrect: during a partition, a distributed system cannot guarantee both consistency and availability; partition tolerance is not an option that can simply be given up in that situation.
> Question 5: "I would favour availability."  
> Question 5: "a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance"  

### C6 Q6 Architecture decision record (3/5, Proficient)

In Question 6, your Context, Decision and positive consequences are specific to the scenario. Add at least one negative consequence of the queue decision to complete the ADR.

*Assessor reasoning:* Context, decision, and positive consequences are specific and present. No negative consequence of introducing the queue is stated, such as additional operational complexity or eventual notification delay.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (4/4, Excellent)

Your headings, concise answers and IEEE-style numbered citations meet the communication requirements. Also state any assumptions explicitly, as the task requires.

*Assessor reasoning:* All six required headings appear in order, answers are within the 150-word limit, and external sources are cited in IEEE-style numbered form with a reference list. Writing is clear and terminology is generally precise.
> Question 1: "## Question 1"  
> References: "[1] L. Bass, P. Clements, and R. Kazman"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 1: The availability response measure, “stay up most of the time,” is not measurable.
- Question 3: Part (c) reports redundant payment-provider availability as end-to-end order-placement availability. Including the other required components, availability is approximately 99.80%, with about 1.5 hours of downtime per 30-day month.
- Question 5: CAP is misstated: under a network partition, a distributed system must trade off consistency and availability; it cannot choose consistency and availability while giving up partition tolerance.
- Question 6: The ADR omits a negative consequence of the queue decision.
- References: No assumptions are explicitly stated, despite the task requirement to state any assumptions.

## Next steps

1. In Question 1, replace “stay up most of the time” with a measurable availability target, such as a specified percentage over a stated period, and check that each scenario includes all six parts.
2. In Question 3(c), distinguish the redundant payment-provider availability from end-to-end order-placement availability; include all required components and show the resulting monthly downtime. In Question 5, explain that during a network partition, consistency and availability must be traded off, then connect each choice to its technique.
3. In Question 6, add a specific negative consequence of the queue decision, such as added operational complexity or delayed notifications. State any assumptions explicitly, as required by the task. Retain the scenario-specific trade-offs in Question 2 and the outage application and tuning consideration in Question 4.

---
<sub>Run Input_4-Run_2-Eff_low-261118-120027 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8358/5188 | cost $0.003256 (incl. $0.001628 for the reused reference rubric+task structure) | 30.36s</sub>
