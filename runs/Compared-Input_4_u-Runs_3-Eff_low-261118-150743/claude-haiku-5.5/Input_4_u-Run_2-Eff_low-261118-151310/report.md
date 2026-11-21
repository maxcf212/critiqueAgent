# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You produced a strong, accurate submission. Your Question 3 availability calculations are correct, and your answers are closely tied to the CampusEats scenario. Your trade-offs in Question 2 and your Architecture Decision Record in Question 6 are clear and specific. The main gap is the absence of an explicit assumptions statement, which R7 requires and which would have made two of your claims easier to verify.

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

You chose performance and availability and justified them with scenario facts: 900 lunchtime orders and the 4.2 s p95 response time. Both scenarios have all six parts, and each response measure is measurable (p95 under 1.5 s, under 0.1% failures, one-minute recovery). This is an excellent answer.

*Assessor reasoning:* Two attributes are chosen and tied to scenario facts (900 orders, 4.2 s p95, payment slowdown). Both scenarios have all six parts and measurable response measures (p95 under 1.5 s, under 0.1% failures, 1 minute recovery).
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

You recommended a modular monolith and linked it to the scenario through team size and the lunchtime slowness and weekly downtime of the single VM. You also acknowledged the downside: modules cannot be scaled independently and a bug can crash the whole process. The one weakness is the unstated assumption behind 'eight or more services', which should be an explicit assumption.

*Assessor reasoning:* Clear modular monolith recommendation with two trade-offs tied to the scenario: team size and the single-VM lunchtime slowness and weekly downtime. The downside is explicitly acknowledged.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts (a), (b) and (c) are correct, and your working is shown to the requested precision. Your use of series multiplication and conversion to monthly downtime is clear. The independence assumption behind the multiplication is not stated explicitly, and stating it would make the answer complete.

*Assessor reasoning:* All three parts recomputed and correct: 99.30%, 5.0 h, 99.80%, 1.5 h. Working is shown to the requested precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You correctly explained the Circuit Breaker's states and applied it to the slow payment outage. You also gave a tuning consideration (the threshold should come from real latency data) and a drawback (nobody can pay while it is open, so a fallback is needed). This is an excellent answer.

*Assessor reasoning:* Circuit Breaker is correctly explained with states, applied to the slow payment outage, and includes both a tuning consideration and a drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked"  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  
> Question 4: "Drawback: nobody can pay while it is open, so a fallback is needed."  

### C5 Q5 Consistency and availability (6/6, Excellent)

You justified both your consistency and availability choices. You applied CAP correctly, treating partition tolerance as mandatory, and named concrete techniques: a Redis TTL cache and idempotency keys. This is an excellent answer.

*Assessor reasoning:* Both choices are justified, CAP is applied correctly with partition tolerance treated as mandatory, and concrete techniques are named (Redis TTL cache, idempotency keys).
> Question 5: "This is the AP choice, with eventual consistency."  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your Architecture Decision Record has Context, Decision and Consequences, all specific to CampusEats. It includes both positive and negative consequences, such as the extra queue component for five developers to run and monitor. This is an excellent answer.

*Assessor reasoning:* Context, Decision and Consequences are all present and scenario-specific, with both positive and negative consequences.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Consequences (negative): The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Your headings are in order, your answers are within the word limits, your terminology is precise, and your references follow IEEE style. The missing explicit assumptions statement is a content gap against R7, not a format deduction, but adding it would fully meet the requirement.

*Assessor reasoning:* Headings are used in order, answers are within limits, terminology is precise and IEEE-style citations and reference list are present. No explicit assumptions section is included, which is a gap against R7 but not a format-level deduction here.
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

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

- Question 2: The claim of 'eight or more services' is an unstated assumption about the planned microservice split, not stated as an assumption.
- Question 3: Independence of the component failures and of the two payment providers is assumed but not explicitly stated as an assumption.

## Next steps

1. Add a short, explicit assumptions section. State that the planned split is eight or more services, and that the component failures and the two payment providers fail independently in your Question 3 calculation.
2. In Question 3, state the independence assumption before you multiply the availabilities, so the reader can see why the series calculation is valid.
3. Check that every in-text citation matches an entry in your References list, and that all entries follow IEEE style, so R7 is fully met.

---
<sub>Run Input_4_u-Run_2-Eff_low-261118-151310 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11494/7293 | cost $0.004852 (incl. $0.001628 for the reused reference rubric+task structure) | 26.45s</sub>
