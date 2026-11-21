# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You earned 29/40. Your strongest work is scenario-specific reasoning in Questions 2 and 4, including a well-applied circuit breaker pattern. To progress, make the availability target measurable, correct the end-to-end calculation in Question 3(c), revise the CAP explanation in Question 5, and include a negative consequence in Question 6.

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

In Question 1, you selected and justified suitable performance and availability attributes and used the six-part scenario form. Your performance measure is measurable, but “stay up most of the time” is not. State a target such as a percentage availability or maximum monthly downtime to reach Excellent.

*Assessor reasoning:* Both attributes are justified using the scenario, and both scenarios include the six parts. The performance measure is measurable, but the availability measure is vague and has no target.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation in Question 2 is excellent: you link trade-offs to the five-person team, the single-VM problem, and deployment downtime, and acknowledge limited independent scaling and shared-process failure. Maintain this scenario-specific justification.

*Assessor reasoning:* The modular-monolith recommendation is clear and supported by trade-offs specific to team size, the single-VM performance problem, and deployment downtime. It also acknowledges the downside of the recommendation.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) in Question 3 are correctly calculated and rounded. In part (c), do not report the redundant payment-provider figure as end-to-end availability. Include all components and report approximately 99.80% availability and 1.5 hours of monthly downtime, with working, to reach Excellent.

*Assessor reasoning:* Parts (a) and (b) are correctly calculated and rounded. Part (c) correctly calculates redundant payment-provider availability but reports it as end-to-end availability, omitting the other required components.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Question 4 is excellent. You accurately explain circuit-breaker states, apply the pattern to the slow payment provider, and give a relevant threshold and time window for tuning. Continue connecting the mechanism, outage, user impact, and operational consideration this specifically.

*Assessor reasoning:* The circuit breaker mechanism and states are explained accurately, and the response applies it to the slow-provider outage. The failure threshold and time window provide a relevant tuning consideration.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open and calls fail immediately without waiting"  
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging for 25 minutes."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices in Question 5 are reasonable and you name concrete techniques. Correct the CAP statement: during a partition, a system must choose consistency or availability; it cannot give up partition tolerance. Also explain that an idempotency key prevents duplicate retries but does not ensure consistency across a partition.

*Assessor reasoning:* The availability choice for browsing and consistency-oriented payment choice are reasonable, and concrete techniques are named. However, the CAP explanation is incorrect: during a partition, the system must choose between consistency and availability; it cannot give up partition tolerance in that situation.
> Question 5: "The worst case is that a student sees an item that sold out a minute ago, which the outlet can handle by rejecting that order."  
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance, so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Question 6 includes specific Context, Decision, and Consequences sections, and the durable queue decision is clear. Add at least one negative consequence—such as duplicate delivery, delayed notification, or extra queue operations—alongside the benefits to reach Excellent.

*Assessor reasoning:* Context, Decision, and Consequences are present and specific. The consequences describe several benefits, but omit the required negative consequence, such as duplicate delivery, delayed notification, or added queue operations.
> Question 6: "Publish an "OrderPaid" event to a durable message queue (RabbitMQ). A notification worker consumes the events and pushes them to the outlet tablets, retrying until each one is acknowledged."  
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings, clear writing, citations, and broadly IEEE-style reference list are strengths. To reach Excellent, verify every answer is within 150 words and use precise terminology throughout, particularly the CAP explanation in Question 5.

*Assessor reasoning:* The required question headings are used, the writing is clear, and citations and a reference list are present in a broadly IEEE-style format. The CAP explanation is imprecise, so terminology is not consistently precise.
> Question 1: "The scenarios below use the six-part form from [1]."  
> References: "[2] M. T. Nygard, Release It! Design and Deploy Production-Ready Software, 2nd ed. Raleigh, NC, USA: Pragmatic Bookshelf, 2018."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | Questions 1–6; References |

## Technical issues

- Question 1: The availability scenario's response measure, “stay up most of the time,” is not measurable.
- Question 3: Part (c) reports redundant payment-provider availability as end-to-end availability. Including the other components gives approximately 99.80% availability and 1.5 hours of monthly downtime.
- Question 5: CAP does not permit choosing consistency and availability while giving up partition tolerance during an actual network partition. An idempotency key prevents duplicate retries but does not itself provide consistency across a partition.

## Next steps

1. Revise Questions 1, 3(c), and 5 using explicit measurable targets, the complete end-to-end availability calculation, and the correct CAP interpretation.
2. Revise Question 6 by adding a specific negative consequence of the durable-queue decision, such as duplicate delivery, delayed notification, or additional queue operations.
3. Before submitting, check that every answer is within 150 words and that architecture terminology—especially CAP terminology—is precise and consistently supported by IEEE-style citations.

---
<sub>Run Input_4-Run_2-Eff_high-261115-173508 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8284/9016 | cost $0.005093 (incl. $0.001628 for the reused reference rubric+task structure) | 65.54s</sub>
