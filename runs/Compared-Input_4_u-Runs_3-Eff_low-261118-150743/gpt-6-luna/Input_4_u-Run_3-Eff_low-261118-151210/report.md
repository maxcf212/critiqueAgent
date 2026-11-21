# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 38 / 40 (95%)**

You produced a strong, scenario-specific submission, with complete quality-attribute scenarios, accurate availability calculations, and a clear resilience explanation and ADR. To strengthen your technical reasoning further, distinguish retry protection from payment consistency, and avoid treating an order as lost unless the scenario establishes that. Your references are present; make any requested assumptions explicit.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

Question 1: You clearly justified why performance and availability matter, and both six-part scenarios have measurable response measures. To sustain this level, keep measures precise and ensure demanding guarantees—such as accepting every request—are feasible.

*Assessor reasoning:* Both attributes are well motivated by the scenario. Both scenarios specify source, stimulus, artefact, environment, response and measurable response measures. The measures are concrete, even if the performance scenario’s guarantee that every request is accepted may be demanding.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering."  

### C2 Q2 Architectural style (6/6, Excellent)

Question 2: Your modular-monolith recommendation is tied to the five-person team, service count, and known bottleneck, and you acknowledge its downside. This meets the Excellent-level trade-off requirements; continue grounding recommendations in the scenario.

*Assessor reasoning:* The recommendation and trade-offs are specific to the team size, service count, known lunchtime bottleneck, and downtime. It acknowledges the recommendation’s downside.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months."  
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

Question 3: Your series and parallel availability calculations are correct, with working and requested precision shown. Keep stating assumptions such as independence when presenting reliability calculations.

*Assessor reasoning:* The series and parallel calculations are correct under the stated independence assumptions. Availability and monthly downtime are rounded to the requested precision; working is shown for all parts.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month."  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Question 4: You accurately explain the circuit breaker, apply it to the payment outage, and discuss tuning risks and fallback drawbacks. This meets the Excellent-level requirements; retain this link between mechanism and scenario.

*Assessor reasoning:* Circuit breaker mechanism is accurately explained and applied to the slow-payment outage. The response also gives meaningful threshold-tuning considerations and a fallback drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Last month the breaker would have opened within seconds, and students would have seen "payment temporarily unavailable" instead of the app hanging for 25 minutes."  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded; too lax and threads are exhausted first."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Question 5: Your availability and consistency choices are reasonable and you name techniques, but idempotency prevents duplicate effects on retries rather than enforcing consistency during a partition. Add a coordination, quorum, or transaction mechanism to reach the Excellent level.

*Assessor reasoning:* The availability/consistency choices are reasonable and justified, and concrete techniques are named. CAP is broadly explained correctly. However, an idempotency key prevents duplicate effects on retries but does not itself provide consistency during a partition; a consistency-enforcing coordination or transaction mechanism would strengthen the payment technique.
> Question 5: "I would favour availability."  
> Question 5: "This is the AP choice, with eventual consistency."  
> Question 5: "For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Question 6: Your ADR has scenario-specific Context, Decision, and positive and negative Consequences. Avoid asserting that an outlet tablet outage loses an order unless persistence and error handling establish that; qualify the consequence or state an assumption.

*Assessor reasoning:* Context, decision and consequences are all specific to CampusEats. Positive and negative consequences are included, with relevant delivery and duplicate-handling implications.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Your answers use the required headings, clear terminology, numbered citations, and appear within the word limit. Keep these strengths and explicitly state assumptions as requested; the marking rated communication at the Excellent level.

*Assessor reasoning:* All six required headings are used, answers appear within the 150-word limit, and terminology and citations are clear. IEEE-style numbered citations and a reference list are present. The missing assumptions statement is captured separately under R7.
> Question 1: "## Question 1"  
> Question 6: "## Question 6"  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 5: The idempotency key helps prevent duplicate charges on retries, but does not itself enforce consistency during a network partition; the payment case would benefit from naming a coordination, quorum, or transactional mechanism.
- Question 6: The claim that an offline outlet tablet means the order is lost is not established by the scenario. A synchronous call may fail or time out, but whether the paid order is actually lost depends on persistence and error-handling behavior.
- References: A reference list and numbered citations are included, but no assumptions are explicitly stated, as requested.

## Next steps

1. In Question 5, keep the idempotency key for preventing duplicate charges on retries, but add a consistency mechanism—such as coordination, quorum, or a transaction—and explain how it supports your CAP choice during a partition. This would address the main requirement for the Excellent level.
2. In Question 6, qualify the consequence of a synchronous outlet call: it may fail or time out, but whether a paid order is lost depends on persistence and error handling. State the relevant assumption or describe the outcome conditionally.
3. Add an explicit assumptions statement alongside your references, as requested. Continue using numbered IEEE-style citations and the required headings; these already support clear communication.

---
<sub>Run Input_4_u-Run_3-Eff_low-261118-151210 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8525/5214 | cost $0.003281 (incl. $0.001628 for the reused reference rubric+task structure) | 30.75s</sub>
