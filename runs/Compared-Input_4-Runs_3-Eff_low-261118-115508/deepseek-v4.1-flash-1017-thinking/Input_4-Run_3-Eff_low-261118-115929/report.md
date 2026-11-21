# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You submitted a strong, well-argued response: Q2 and Q4 are excellent, and Q3(a)(b) are correct. The main losses are the Q3(c) chain calculation, CAP misuse in Q5, a non-measurable availability measure in Q1, a one-sided ADR in Q6, and over-length answers affecting Q7. Total 30/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You justified performance and availability from the CampusEats scenario, and your performance scenario has all six parts with a measurable p95 target. The availability scenario is complete but its response measure, “stay up most of the time,” is not measurable. For Excellent, give both scenarios measurable response measures, such as a monthly uptime percentage or maximum downtime.

*Assessor reasoning:* Both attributes are justified from the scenario (lunch peak, 4.2 s p95). The performance scenario has all six parts with a measurable measure; the availability scenario has all six parts but its response measure ('stay up most of the time') is not measurable, so it falls short of Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped"  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular monolith recommendation is clear and well linked to the scenario. You used two specific trade-offs: five developers versus operational overhead, and the known single-VM/deployment problems not being caused by the monolith. You also acknowledged the downside that modules cannot scale independently and one bug can crash the process. This meets the Excellent level.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs: team size/operational overhead and the known problems (single VM, deployment downtime) not being caused by the monolith. The downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct with working shown: 99.30% and 5.0 hours. In part (c) you correctly combined payment availability but then applied only the payment-provider downtime, 0.018 hours, ignoring the other three components. The correct result is about 99.80% and 1.5 hours per month. For Excellent, all three parts must be correct.

*Assessor reasoning:* Parts (a) and (b) are correct with working (99.30%, 5.0 h). Part (c) computes the combined payment availability correctly but then applies only the payment downtime, ignoring the other three components; correct answer is ~99.80% and ~1.5 h. Exactly one part incorrect.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Circuit Breaker is named and its Closed/Open/Half-Open mechanism is explained correctly. You applied it concretely to the 25-minute outage with a student-facing fallback message, and you gave a tuning consideration using a failure threshold and window. This meets the Excellent level.

*Assessor reasoning:* Circuit Breaker is named, its Closed/Open/Half-Open mechanism is explained correctly, applied concretely to the 25-minute outage, and a tuning consideration (failure threshold/window) is given.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging"  

### C5 Q5 Consistency and availability (4/6, Proficient)

Your choices are reasonable and you named concrete techniques: a Redis TTL cache and an idempotency key. However, your CAP statement says payments “give up partition tolerance,” which is incorrect: partition tolerance is not optional, and during a partition you must sacrifice consistency or availability. For Excellent, correct the CAP explanation while keeping both justified choices and techniques.

*Assessor reasoning:* Both choices are reasonable and concrete techniques are named (Redis TTL cache, idempotency key). However the CAP statement is wrong: partition tolerance is not optional, and in a partition one must sacrifice C or A, not P.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "a cache (for example Redis with a 60-second TTL)"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are all present and specific to the CampusEats scenario. However, your consequences are entirely positive, citing improved response time and lunch-peak smoothing. For Excellent, add at least one negative consequence, such as eventual consistency, duplicate notifications, or added operational complexity.

*Assessor reasoning:* Context, Decision and Consequences are all present and scenario-specific, but the consequences are entirely positive; no negative consequence (e.g. eventual consistency, duplicate notifications, added operational complexity) is given.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  
> Question 6: "The queue also smooths the lunch peak because the workers process orders at a steady rate."  

### C7 Communication and format (2/4, Developing)

Your writing is clear and IEEE-style references are provided. However, at least Q1 and Q2, and arguably Q4, exceed the 150-word limit, which is more than a single over-length answer. For Proficient, keep at most one answer over the limit and resolve minor citation or formatting problems.

*Assessor reasoning:* Writing is clear and IEEE-style references are provided, but at least Q1 and Q2 (and arguably Q4) exceed the 150-word limit, which is more than a single over-length answer.
> Question 2: "Second, the known problems are not caused by the monolith itself."  
> Question 1: "The scenarios below use the six-part form from [1]."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | yes | References |

## Technical issues

- Question 3: Part (c) applies only the payment-provider downtime (0.018 h) instead of the full chain availability; correct result is ~99.80% and ~1.5 h/month.
- Question 5: CAP misstated: partition tolerance cannot be 'given up'; during a partition one must sacrifice consistency or availability.
- Question 1: Availability response measure ('stay up most of the time') is not measurable.
- Question 6: No negative consequence recorded in the ADR.

## Next steps

1. Recalculate Q3(c) using the full four-component chain availability, then convert the resulting downtime to hours per month and show the working.
2. Rewrite the Q5 CAP statement so partition tolerance is not treated as optional, make the Q1 availability response measure measurable, and add at least one negative consequence to Q6.
3. Trim Q1, Q2 and Q4 to 150 words or fewer, and check that required headings and IEEE citations remain correct.

---
<sub>Run Input_4-Run_3-Eff_low-261118-115929 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8316/7228 | cost $0.004511 (incl. $0.001628 for the reused reference rubric+task structure) | 28.74s</sub>
