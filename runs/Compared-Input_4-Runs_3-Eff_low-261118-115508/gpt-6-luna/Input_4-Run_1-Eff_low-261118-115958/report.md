# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 28 / 40 (70%)**

You demonstrate strong, scenario-specific architectural reasoning, especially in Question 2, and your clear, well-formatted answers meet the communication standard. To reach the next rubric level in several criteria, make the availability scenario measurable, calculate end-to-end availability across all components, explain CAP precisely, and include a downside in your ADR.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

In Question 1, you selected and justified relevant attributes and used six-part scenarios. Your performance measure is measurable, but “stay up most of the time” is not, and the availability response focuses on browsing rather than orders. Quantify order availability to reach Excellent.

*Assessor reasoning:* Both attributes are scenario-relevant and justified, and the scenarios include the six parts. The performance measure is measurable, but the availability response measure (“stay up most of the time”) is not quantified. The availability response also addresses browsing rather than order availability.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

In Question 2, your modular-monolith recommendation is supported by scenario-specific trade-offs involving the five-person team, VM, deployment downtime and rewrite cost. You also acknowledge that modules cannot be scaled independently. This meets the Excellent standard.

*Assessor reasoning:* The recommendation is clear and supported by scenario-specific trade-offs involving the five-person team, the VM, deployment downtime, and the cost of a rewrite. It also acknowledges the modular monolith’s downside.
> Question 2: "Instead the existing application should be restructured into a modular monolith"  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure"  
> Question 2: "The slow lunchtime responses come from running on a single virtual machine"  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

In Question 3, parts (a) and (b) are correct, and you calculate redundant payment availability correctly. In part (c), include the other series components in end-to-end availability before calculating downtime; the current payment-only calculation prevents an Excellent result.

*Assessor reasoning:* Parts (a) and (b) are correct to the requested precision. In (c), the redundant payment availability is correctly calculated, but the student uses payment-only availability for end-to-end availability and downtime instead of multiplying by the other required component availabilities.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (4/5, Proficient)

In Question 4, you correctly explain and apply the Circuit Breaker to the slow-provider outage. To reach Excellent, add a drawback or tuning consideration, such as how thresholds or trial-call timing affect false trips and recovery.

*Assessor reasoning:* The pattern and its states are explained correctly and applied to the slow-provider outage. No drawback or tuning consideration is given; a threshold example alone does not discuss a drawback or tuning trade-off.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "After a wait period the breaker goes Half-Open and lets a few trial calls through."  
> Question 4: "the breaker would have opened within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (3/6, Proficient)

In Question 5, your choices are reasonable, and you name concrete techniques for caching menus and preventing duplicate charges. Clarify that partition tolerance is assumed and a partition requires a consistency-versus-availability trade-off; state that payment operations are deferred or rejected to preserve consistency.

*Assessor reasoning:* The choices are reasonable and the menu cache and payment idempotency key are concrete techniques. However, CAP is described imprecisely: during a partition, a distributed system must choose between consistency and availability, while partition tolerance is assumed. The payment choice should explicitly sacrifice availability during the partition.
> Question 5: "I would favour availability."  
> Question 5: "I would favour consistency, because charging a student twice or accepting an order without a payment is unacceptable."  
> Question 5: "The CAP theorem says a system can only provide two of consistency, availability and partition tolerance"  

### C6 Q6 Architecture decision record (3/5, Proficient)

In Question 6, your scenario-specific ADR includes Context, Decision and positive consequences. To reach Excellent, add a negative consequence of asynchronous queue-based notification, such as delayed outlet notification or the need to handle duplicate delivery.

*Assessor reasoning:* Context, decision, and consequences are present and scenario-specific, with multiple positive consequences. The consequences omit a negative consequence, such as delayed outlet notification, duplicate delivery handling, or queue operations.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously"  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet"  

### C7 Communication and format (4/4, Excellent)

Your answers use the required headings, stay within the word limit, and cite sources in IEEE style with a reference list. Your writing and terminology are clear, meeting the Excellent standard.

*Assessor reasoning:* The required question headings are used in order, answers appear within the 150-word limit, and external sources are cited with a corresponding IEEE-style reference list. Terminology is generally clear and precise.
> Question 1: "## Question 1"  
> Question 6: "## Question 6"  
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3: Part (c) reports payment-only availability and downtime. End-to-end availability must include the other series components: 0.9995 × 0.999 × 0.9995 × 0.999975 ≈ 0.99795, or 99.80%, giving about 1.5 hours of monthly downtime.
- Question 5: CAP is not a choice to give up partition tolerance. When a partition occurs, the system must trade off consistency against availability. The payment discussion should say it rejects or defers operations during the partition to preserve consistency.
- Question 6: The ADR gives only positive consequences and does not acknowledge a downside of asynchronous queue-based notification.

## Next steps

1. In Question 1, quantify the availability response measure and focus it on order availability—for example, set a target percentage of successful order requests over a stated period.
2. In Question 3(c), multiply the availability of all series components, including the redundant payment providers, before calculating monthly downtime; show the corrected working.
3. In Questions 4–6, add a circuit-breaker tuning trade-off, explain that a partition forces a consistency-versus-availability choice, and include a negative consequence of asynchronous queue-based notification in your ADR.

---
<sub>Run Input_4-Run_1-Eff_low-261118-115958 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8407/5046 | cost $0.003573 (incl. $0.001628 for the reused reference rubric+task structure) | 28.9s</sub>
