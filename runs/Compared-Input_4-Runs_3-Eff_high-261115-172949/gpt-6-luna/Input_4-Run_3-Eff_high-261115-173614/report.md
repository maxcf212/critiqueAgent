# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 29 / 40 (72.5%)**

You achieved 29/40. Your strongest work is the scenario-specific modular-monolith recommendation in Question 2 and the circuit-breaker explanation in Question 4. To improve, make Question 1 measurable, correct Question 3(c) and the CAP explanation in Question 5, add a negative ADR consequence, state assumptions, and bring Question 2 within 150 words.

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

Question 1 appropriately selects performance and availability and gives a measurable p95 target. However, “stay up most of the time” is not measurable. The next level requires both six-part scenarios to have measurable response measures, such as a stated availability percentage or maximum downtime.

*Assessor reasoning:* Performance and availability are relevant and justified by the lunch-hour scenario. Both scenarios include the six parts, and the performance measure is measurable. The availability measure, “most of the time,” is not quantifiable, so the scenarios do not both meet the Excellent descriptor.
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is excellent: it uses the five-person team, single-VM load problem, deployment downtime, and shared-scaling/process-failure trade-offs. You have met the top rubric level; preserve this scenario-specific reasoning while shortening the answer to meet the communication limit.

*Assessor reasoning:* The modular-monolith recommendation is clear and supported by scenario-specific trade-offs involving the five-person team, single-VM load issue, and deployment downtime. The student also acknowledges the downside of shared scaling and process failure.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Parts (a) and (b) are correct with working shown. In Question 3(c), the redundant payment-provider result is not the end-to-end order-placement availability. Multiply it by the other components to report approximately 99.80% and 1.5 hours of monthly downtime for full marks.

*Assessor reasoning:* Parts (a) and (b) correctly calculate series availability and monthly downtime to the requested precision. In (c), the redundant payment availability is calculated correctly, but it is reported as end-to-end availability without multiplying by the other components. Thus exactly one part is incorrect.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours, or about one minute per month."  

### C4 Q4 Resilience pattern (5/5, Excellent)

Your Question 4 circuit-breaker explanation is excellent: the states, failure threshold, and slow-provider outage are connected correctly. You have met the top level; continue including a relevant tuning consideration such as the failure threshold.

*Assessor reasoning:* The circuit breaker mechanism and states are explained correctly and applied to the slow-provider outage. The example failure threshold is a relevant tuning consideration.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open and calls fail immediately without waiting"  
> Question 4: "In the outage last month the breaker would have opened within seconds of the provider slowing down."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your browsing and payment choices and idempotency technique are reasonable. The CAP explanation is inaccurate: during a partition, consistency and availability cannot both be retained. The next level requires precise CAP reasoning plus a suitable concrete technique for each case.

*Assessor reasoning:* The availability choice for browsing and consistency choice for payment are reasonable, and concrete techniques are named. However, the CAP explanation is incorrect: during a partition, a system cannot retain both consistency and availability; it must trade one off. This is a significant imprecision.
> Question 5: "To be safe on retries, each order request carries an idempotency key so that a repeated request does not create a second charge."  
> Question 5: "To be safe on retries, each order request carries an idempotency key so that a repeated request does not create a second charge."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Question 6 includes specific Context, Decision, and Consequences, but consequences are only positive. To reach Excellent, add a negative consequence, such as retry-until-acknowledgement causing duplicate outlet notifications unless consumers are idempotent or deduplicate messages.

*Assessor reasoning:* Context, decision, and consequences are present and specific to the scenario. Consequences list only benefits, with no negative consequence such as added queue operations or possible duplicate notifications on retry.
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings, numbered citations, reference list, and terminology are generally clear. Question 2 is approximately 181 words, so the next level requires every answer to be within 150 words, alongside precise terminology and IEEE-style citations. Also include the required explicit assumptions.

*Assessor reasoning:* The required headings and numbered citations with a reference list are used, and terminology is generally clear. Question 2 is approximately 181 words, exceeding the 150-word limit; this fits the Proficient descriptor.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Technical issues

- Question 1: The availability response measure, “stay up most of the time,” is not measurable; provide a quantified availability or downtime target.
- Question 3: Part (c) gives redundant payment-provider availability rather than end-to-end order-placement availability. Multiplying the redundant payment availability by the other components gives approximately 99.80% availability and 1.5 hours of monthly downtime.
- Question 5: CAP does not permit choosing consistency and availability while giving up partition tolerance in a partition. Under partition, consistency and availability are the trade-off.
- Question 6: The ADR gives no negative consequence. Retrying queue delivery until acknowledgement can also cause duplicate outlet notifications unless consumers handle duplicates.
- Question 2: The answer exceeds the 150-word limit.
- -: No assumptions are explicitly stated, as required by the assignment.

## Next steps

1. Revise Question 1’s availability response measure to include a quantified target, and recalculate Question 3(c) as end-to-end availability: approximately 99.80%, or 1.5 hours of monthly downtime.
2. Correct Question 5 by explaining that during a partition, consistency and availability must be traded off; then retain a concrete technique for each scenario. In Question 6, add the negative consequence that retries may create duplicate outlet notifications unless consumers handle duplicates.
3. Add an explicit assumptions section, reduce Question 2 from approximately 181 words to 150 or fewer, and proofread every answer for precise terminology, headings, and IEEE citations.

---
<sub>Run Input_4-Run_3-Eff_high-261115-173614 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8269/11005 | cost $0.006087 (incl. $0.001628 for the reused reference rubric+task structure) | 80.73s</sub>
