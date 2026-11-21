# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You have a strong, well-structured submission with clear scenario grounding and correct Q3(a)/(b). Your main losses are Q3(c) recombination, CAP misapplication in Q5, an unmeasurable Q1 availability measure, one-sided Q6 consequences, Q2 over the word limit, and no explicit assumptions section. Current total 30/40.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Proficient | 4 / 5 | 4 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Your performance scenario is complete and measurable, and you justify performance/availability from lunch-peak data. To reach Excellent, make the availability response measure measurable and tie it to the payment-dependent order flow rather than degraded browsing; 'stay up most of the time' in Q1 is not measurable.

*Assessor reasoning:* Performance and availability are well justified from the lunch-peak data and the performance scenario is complete and measurable. The availability scenario has all six parts but its response measure ('stay up most of the time') is not measurable, so it falls short of Excellent.
> Question 1: "Response measure: the system should stay up most of the time."  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is clear and well grounded: you use the five-developer team, per-service overhead, and known single-VM/deployment problems, and you acknowledge the downside. This is Excellent. For format, trim Q2 to the 150-word limit so the communication criterion is not affected.

*Assessor reasoning:* Clear recommendation (modular monolith) with two scenario-specific trade-offs: five-developer team versus per-service operational overhead, and the known problems traced to a single VM and the deployment process rather than the monolith. The downside is explicitly acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Q3(a) and (b) are correct with working (99.30%, 5.0 h). In Q3(c) you correctly compute payment availability 0.999975 but report it as whole-system availability; re-multiply by the other three components to get 99.80% and ~1.5 h downtime. That one incorrect part keeps this at Proficient; correcting it would meet Excellent.

*Assessor reasoning:* Parts (a) and (b) are correct with working (99.30%, 5.0 h). In (c) the combined payment availability 0.999975 is computed correctly, but the student then reports it as the whole-system availability instead of re-multiplying by the other three components; correct answer is 99.80% and 1.5 h. One part incorrect.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  

### C4 Q4 Resilience pattern (4/5, Proficient)

You name Circuit Breaker, explain closed/open/half-open correctly, and apply it convincingly to the 25-minute hang with a threshold example. To reach Excellent, add a drawback or genuine tuning consideration, such as threshold calibration, false trips, or fallback behaviour, in Q4.

*Assessor reasoning:* Circuit Breaker is named and its closed/open/half-open mechanism is explained correctly and applied convincingly to the 25-minute hang. A threshold value is mentioned, but no drawback or genuine tuning consideration (e.g. threshold calibration, false trips) is discussed, so it is not Excellent.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open and calls fail immediately without waiting"  
> Question 4: "Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging for 25 minutes."  

### C5 Q5 Consistency and availability (4/6, Proficient)

Your choices and techniques (Redis TTL cache, idempotency key) are sensible. However, Q5(ii) misapplies CAP: partition tolerance cannot be given up; during a partition you choose consistency or availability. Correct that framing and state the sacrifice for payments versus browsing to reach Excellent.

*Assessor reasoning:* Both choices are sensible and concrete techniques are named (Redis TTL cache, idempotency key). However the CAP application is wrong: partition tolerance cannot be 'given up' in a partition; the correct framing is choosing consistency over availability during a partition.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance"  
> Question 5: "each order request carries an idempotency key so that a repeated request does not create a second charge"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Your ADR has Context, Decision and Consequences specific to CampusEats. The consequences are one-sided: you list latency, offline outlets and peak smoothing but no negative consequence. Add one, such as duplicate delivery, ordering guarantees, or added operational complexity, to meet Excellent.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats. The consequences are entirely positive (latency, offline outlets, peak smoothing); no negative consequence such as duplicate delivery, ordering guarantees or added operational complexity is given.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  
> Question 6: "If a tablet is offline the order is lost, and during the lunch peak these calls add to the 4.2 s p95 response time."  

### C7 Communication and format (3/4, Proficient)

Writing is clear, headings are in order, and IEEE-style citations/reference list are present. Q2 is ~180 words, over the 150-word limit; trim it. Also add an explicit assumptions section, as the brief requires assumptions to be stated, to strengthen format compliance.

*Assessor reasoning:* Writing is clear, headings are used in order and IEEE-style citations with a reference list are present. Question 2 is roughly 180 words, exceeding the 150-word limit; the other answers are within it.
> Question 2: "Second, the known problems are not caused by the monolith itself."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

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

- Question 3(c): Final availability wrongly reported as 99.9975% (the payment-only figure); should re-multiply by the other three components giving 99.80% and ~1.5 h downtime.
- Question 5(ii): CAP misapplied: partition tolerance cannot be traded away; in a partition one must sacrifice consistency or availability.
- Question 1: Availability response measure 'stay up most of the time' is not measurable; also the response describes degraded browsing rather than the payment-dependent order flow.
- Question 6: No negative consequence given, so the ADR consequences are one-sided.
- Question 2: Answer exceeds the 150-word limit (~180 words).
- Whole submission: No explicit assumptions section despite the brief requiring assumptions to be stated.

## Next steps

1. In Q3(c), after computing payment availability 0.999975, recombine it with the other three components (0.9995 × 0.999 × 0.9995 × 0.999975) and report 99.80% with ~1.5 h downtime; show the multiplication explicitly.
2. In Q5(ii), reframe CAP: partition tolerance is not optional; during a partition choose consistency or availability. State which you sacrifice for payments and browsing, and keep your Redis TTL and idempotency-key techniques.
3. Revise Q1's availability response measure to a measurable target tied to payment-dependent ordering, add a negative consequence to Q6, trim Q2 to ≤150 words, and add a short assumptions section.

---
<sub>Run Input_4-Run_2-Eff_low-261118-115856 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8491/9616 | cost $0.005962 (incl. $0.001628 for the reused reference rubric+task structure) | 33.04s</sub>
