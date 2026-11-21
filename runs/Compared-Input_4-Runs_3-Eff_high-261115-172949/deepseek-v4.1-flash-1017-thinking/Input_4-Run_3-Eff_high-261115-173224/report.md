# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

Total 30/40. You are strongest in Q2 and Q4: your modular-monolith trade-offs and circuit-breaker application are specific and well argued. Main losses are Q3(c) end-to-end availability, Q5 CAP misuse, Q1 non-measurable availability measure, Q6 missing negative consequence, and Q2 over the word limit. Address these to move Proficient criteria to Excellent.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose performance and availability and your performance scenario is complete and measurable. The availability response measure 'stay up most of the time' is not measurable, and its justification is thin. For Excellent, make both scenarios six-part and both response measures measurable (e.g. uptime % or downtime per month), and justify why these two attributes matter most in CampusEats.

*Assessor reasoning:* Performance scenario is complete and measurable, but availability response measure is vague ('most of the time') and availability justification is thin. Suitable attributes, so Proficient.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

You clearly recommend a modular monolith and tie it to the five-developer team, single-VM load issue and deployment downtime, while acknowledging the downside. This is Excellent. To sustain it, keep every trade-off scenario-specific and the downside explicit; avoid generic textbook advantages.

*Assessor reasoning:* Clear modular-monolith recommendation tied to five-developer team, single-VM load issue and deployment downtime; downside acknowledged. Excellent.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct. In (c) you compute payment availability but do not combine it with the other components; end-to-end should be 0.9995×0.999×0.9995×0.999975 = 99.80%, downtime 1.5 h/month, not 99.9975%/0.018 h. For Excellent, show the full series calculation for all components to the requested precision.

*Assessor reasoning:* (a) and (b) correct. (c) computes payment availability but fails to combine it with other components; end-to-end should be 99.80% and 1.5 h/month. One part incorrect, so Proficient.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "So the new availability of placing an order is 99.9975%"  
> Question 3: "0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named circuit breaker, explained its states and threshold, and applied it to last month's outage. The tuning consideration satisfies Excellent. To make it even stronger, add an explicit drawback (e.g. false positives or added latency) alongside the tuning threshold.

*Assessor reasoning:* Circuit breaker mechanism, states, outage application and tuning threshold are correct. No explicit drawback, but tuning consideration satisfies Excellent.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  
> Question 4: "In the outage last month the breaker would have opened within seconds"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices and idempotency-key technique are reasonable, but CAP is misused: you cannot 'give up partition tolerance' during a partition. Payments should be CP and menu browsing AP. For Excellent, explain CAP correctly, justify both choices, and name a concrete technique for each case.

*Assessor reasoning:* Choices and techniques are reasonable, but CAP is misused: partition tolerance cannot be given up during a partition. Proficient with incorrect CAP explanation.
> Question 5: "we choose consistency and availability and give up partition tolerance"  
> Question 5: "each order request carries an idempotency key"  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are specific to CampusEats, but all consequences are positive. For Excellent, add at least one negative consequence, such as added complexity, eventual consistency, or handling outlets that are offline, while keeping the three sections specific.

*Assessor reasoning:* Context, Decision and Consequences are specific, but consequences are entirely positive; no negative consequence. Proficient.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  
> Question 6: "Outlets that are briefly offline still receive their orders when they reconnect."  

### C7 Communication and format (3/4, Proficient)

Headings and IEEE-style references are present, but Question 2 is about 181 words, over the 150-word limit. For Excellent, keep every answer within 150 words and maintain precise terminology and citation formatting.

*Assessor reasoning:* Headings and IEEE-style references are present, but Question 2 is about 181 words, exceeding the 150-word limit. Proficient.
> Question 2: "I recommend against a full microservices rewrite for the next 12 months."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed."  

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

- Question 1: Availability response measure 'stay up most of the time' is not measurable; availability justification is weak.
- Question 2: Answer is about 181 words, exceeding the 150-word limit.
- Question 3(c): End-to-end availability after adding the second payment provider is wrong; should be 0.9995×0.999×0.9995×0.999975 = 99.80%, downtime 1.5 h/month, not 99.9975%/0.018 h.
- Question 5: CAP theorem misuse: cannot 'give up partition tolerance' during a partition; payments should be CP, menu browsing AP.
- Question 6: Consequences are all positive; no negative consequence is stated.

## Next steps

1. Recompute Q3(c): multiply all four availabilities (0.9995×0.999×0.9995×0.999975) to get 99.80% and 1.5 h/month downtime; show each step.
2. Rewrite Q5 CAP: explain partition tolerance is not optional; justify payments as CP and menu browsing as AP, naming a concrete technique for each.
3. Tighten Q2 to 150 words, make Q1 availability response measure measurable (e.g. uptime % or downtime per month), and add a negative consequence to Q6.

---
<sub>Run Input_4-Run_3-Eff_high-261115-173224 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8221/14669 | cost $0.009288 (incl. $0.001628 for the reused reference rubric+task structure) | 88.89s</sub>
