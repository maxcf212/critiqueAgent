# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You achieved 40/40, with Excellent performance across all six questions and communication. Your answers apply architecture concepts to CampusEats, show correct availability calculations, and support decisions with scenario-specific reasoning. You are already at the highest rubric level; the suggestions below are ways to sustain and extend that work.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 6 / 6 | 6 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

Question 1 earns Excellent: you justify performance and availability using the lunch-hour order load, and both scenarios include all six parts with measurable response measures. You have met the top rubric level; keep making each measure precise and testable in future work.

*Assessor reasoning:* Selects and justifies two scenario-relevant attributes. Both scenarios include source, stimulus, artefact, environment, response, and measurable response measures.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

Question 2 earns Excellent: your modular-monolith recommendation reflects the five-developer team and existing VM and downtime concerns, and you acknowledge limited independent scaling and shared-process risk. You have met the top rubric level; continue making trade-offs this specific to the scenario.

*Assessor reasoning:* The recommendation is supported by trade-offs tied to team size, the single-VM load problem, and downtime, and it acknowledges a relevant downside.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Question 3 earns Excellent: you show the series-availability and redundant-payment calculations, with correct results and requested rounding for availability and downtime. You have met the top rubric level; retain this clear working in future quantitative answers.

*Assessor reasoning:* Series and redundant-payment calculations are correct, with working shown. Availability percentages and monthly downtime are rounded to the requested precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  
> Question 3: "Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

Question 4 earns Excellent: you explain circuit-breaker states, apply them to the payment slowdown, and discuss the risk of opening too readily. You have met the top rubric level; continue relating pattern tuning to both service protection and user impact.

*Assessor reasoning:* Correctly explains the breaker states and how fast failures protect request threads and browsing during the payment slowdown. It applies the pattern to the outage and discusses tuning and payment unavailability.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded"  

### C5 Q5 Consistency and availability (6/6, Excellent)

Question 5 earns Excellent: you justify availability for cached browsing and consistency for payments, use CAP appropriately, and name eventual consistency and idempotency keys. You have met the top rubric level; keep matching concrete techniques to each scenario's risk.

*Assessor reasoning:* Both choices are justified in partition scenarios, CAP is used appropriately, and concrete techniques are given for cached browsing and idempotent payment retries.
> Question 5: "I would favour availability."  
> Question 5: "This is the AP choice, with eventual consistency."  
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  
> Question 5: "Each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (5/5, Excellent)

Question 6 earns Excellent: your ADR gives specific context, a clear durable-queue decision, and positive and negative consequences, including operational overhead. You have met the top rubric level; continue making consequences explicit and scenario-specific.

*Assessor reasoning:* The ADR includes specific context, a clear queue-based decision, and both positive and negative consequences, including delivery semantics and operational overhead.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Communication earns Excellent: your answers use the required headings, stay within the word limit, use precise terminology, and cite sources in IEEE style. You have met the top rubric level; maintain these practices in future submissions.

*Assessor reasoning:* All answers use the required headings and are within the word limit. Writing is clear, terminology is appropriate, and cited sources have corresponding IEEE-style reference entries.
> Question 1: "## Question 1"  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  
> References: "[2] M. T. Nygard, *Release It! Design and Deploy Production-Ready Software*, 2nd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | Question 3; References |

## Next steps

1. In future quality-attribute answers, continue labeling each of the six scenario elements explicitly and make every response measure quantifiable, as you did in Question 1.
2. Keep showing calculation steps and requested rounding, as in Question 3, so a reader can verify each result independently.
3. When proposing patterns or architecture decisions, continue pairing the scenario-specific benefit with a practical limitation or operational consideration, as you did in Questions 2, 4, and 6.

---
<sub>Run Input_4_u-Run_3-Eff_high-261116-140928 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8338/7678 | cost $0.00449 (incl. $0.001628 for the reused reference rubric+task structure) | 51.64s</sub>
