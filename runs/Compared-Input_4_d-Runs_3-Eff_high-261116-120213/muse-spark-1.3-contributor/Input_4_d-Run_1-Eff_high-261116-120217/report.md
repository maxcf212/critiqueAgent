# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You did well to reason from the CampusEats scenario, especially your excellent Q2 modular monolith justification. To move up you need measurable response measures, correct availability maths, correct breaker states and CAP, plus negative consequences and tight referencing.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose relevant attributes and your Q1 performance scenario was complete with measurable p95 under 1.5s, which is strong. Your availability scenario used 'the system should stay up most of the time.' For Excellent, rewrite that response measure as measurable, e.g. percentage uptime and degraded-mode time.

*Assessor reasoning:* Performance scenario complete with measurable p95 under 1.5s. Availability scenario has six parts but response measure is vague and unmeasurable, so not Excellent. Exactly matches Proficient.
> Question 1: "the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You earned Excellent in Q2 with clear modular monolith recommendation, two scenario-specific trade-offs around five-developer overhead and single-VM 20-min deployments, and you acknowledged downside that modules cannot scale independently and a bug can crash the process. Keep this specificity and stay within word limit in C7.

*Assessor reasoning:* Clear modular monolith recommendation with two scenario-specific trade-offs: five-developer overhead and single-VM plus 20-min deployment fixes. Downside acknowledged. Word overrun penalised in C7.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

You showed correct method and correct (a) 99.30% with working in Q3. Your (b) 'Downtime = ... = 3.5 hours' should be 5.0h, and your (c) '99.9975%' is payment-only; end-to-end needs series of all steps ~99.80% ~1.5h. For higher level, correct both and keep requested precision.

*Assessor reasoning:* (a) 99.30% correct. (b) method correct but 0.00699x720 is 5.0h not 3.5h. (c) 0.999975 correct for payment only, but end-to-end should be ~99.80% ~1.5h, not 99.9975%. Two parts wrong.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

You picked appropriate Circuit Breaker for the slow provider in Q4 and applied it with tuning, which is good. You wrote 'In the Open state calls pass through normally.' For Excellent, reverse this: Closed is normal, Open is fail-fast, Half-Open is trial, then add a drawback/tuning consideration.

*Assessor reasoning:* Circuit Breaker appropriate and applied to slow provider with tuning example, but Open/Closed reversed. Open is fail-fast, Closed is normal. Explanation therefore incorrect.
> Question 4: "In the Open state calls pass through normally."  

### C5 Q5 Consistency and availability (3/6, Proficient)

You made reasonable choices in Q5 and named Redis 60-second TTL for browsing well. You wrote 'for payments we choose consistency and availability and give up partition tolerance.' For Excellent, correct CAP to choose C vs A during partition, and name a concrete technique for payment.

*Assessor reasoning:* Choices reasonable, Redis 60-second TTL named for browsing, but no concrete technique for payment and CAP misused: during partition choose C or A, cannot give up partition tolerance.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Your Q6 ADR had specific Context, Decision on tablets and RabbitMQ OrderPaid, and positives like 'Placing an order no longer waits...' For Excellent, add at least one negative consequence such as queue complexity, ordering, or ops cost.

*Assessor reasoning:* Context, Decision, Consequences present and specific to tablets and RabbitMQ OrderPaid. Multiple positives given but no negative consequence such as complexity or ops cost.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings were ordered and writing clear, but Q2 was ~181 words over 150, '[2]' in Q4 was missing from references, and breaker/CAP terms were imprecise. For Excellent, keep every answer within 150 words, use precise terms, and complete IEEE citations.

*Assessor reasoning:* Headings in order and writing clear, but Q2 ~181 words exceeds 150, [2] cited but absent from list, and breaker/CAP terminology imprecise.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

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

- Question 1: Availability response measure unmeasurable, should specify percentage and time, e.g. degraded mode.
- Question 3: (b) arithmetic error: 5.0h not 3.5h; (c) used payment availability as end-to-end, correct is ~99.80% ~1.5h.
- Question 4: Circuit Breaker states reversed: Closed=normal, Open=fail-fast, Half-Open=trial.
- Question 5: CAP error: cannot forgo partition tolerance; must trade C vs A. No technique named for payment.
- Question 6: No negative consequence stated for queue introduction.

## Next steps

1. Rewrite your Q1 availability response measure as measurable with percentage uptime and degraded-mode time.
2. Recheck Q3: fix (b) 0.00699x720 to 5.0h and (c) to end-to-end series ~99.80% ~1.5h with working and precision.
3. Correct Q4 to Closed=normal Open=fail-fast Half-Open=trial, fix Q5 CAP to C vs A with payment technique, add Q6 negative consequence, keep all answers under 150 words with full IEEE references.

---
<sub>Run Input_4_d-Run_1-Eff_high-261116-120217 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8029/14023 | cost $0.004471 (incl. $0.001628 for the reused reference rubric+task structure) | 56.73s</sub>
