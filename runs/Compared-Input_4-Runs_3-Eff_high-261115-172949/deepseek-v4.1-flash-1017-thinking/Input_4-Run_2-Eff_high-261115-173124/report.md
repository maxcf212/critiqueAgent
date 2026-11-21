# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 30 / 40 (75%)**

You have strong Q2 and Q4, with correct Q3(a)(b). The main gaps are Q3(c) end-to-end availability, CAP misuse in Q5, a non-measurable availability response measure in Q1, one-sided consequences in Q6, and Q2 over the word limit. Fix these specific issues to move from Proficient to Excellent in those criteria.

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

You justified performance and availability well from the lunch-peak scenario. Your performance scenario has all six parts and a measurable response measure. Your availability scenario has all parts, but “stay up most of the time” is not measurable. To reach Excellent, make both response measures measurable—for example, a specific uptime percentage or maximum downtime.

*Assessor reasoning:* Performance and availability are well justified from the lunch-peak scenario. The performance scenario has all six parts and a measurable measure. The availability scenario has all parts, but its response measure is vague and not measurable.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent: your modular-monolith recommendation is clear, and your trade-offs are specific to the five-developer team and known problems, with the downside acknowledged. To stay at Excellent, keep trade-offs scenario-specific and continue acknowledging the downside. (Watch the separate 150-word limit for Q2.)

*Assessor reasoning:* Clear modular-monolith recommendation. Trade-offs are specific to team size and known problems, and the downside is acknowledged.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (5/8, Proficient)

You got Q3(a) and (b) correct with working shown. In Q3(c) you used the payment-provider availability as the overall order-placement availability and ignored the other three components; the correct end-to-end availability is 99.80% with 1.5 h/month downtime. To reach Excellent, show the full end-to-end calculation for (c) combining all four components.

*Assessor reasoning:* Parts (a) and (b) are correct with working. Part (c) is wrong: it uses payment-provider availability as overall availability and ignores the other three components. Correct overall availability is 99.80%, downtime 1.5 h/month.
> Question 3: "So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours"  

### C4 Q4 Resilience pattern (5/5, Excellent)

Excellent: you named Circuit Breaker, explained its mechanism correctly, applied it to the slow-provider outage, and included tuning via failure threshold and wait period. To stay at Excellent, keep the mechanism, outage application, and at least one tuning or drawback consideration explicit.

*Assessor reasoning:* Circuit Breaker is named, correctly explained, applied to the slow-provider outage, and includes tuning via failure threshold and wait period.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your choices are reasonable and you named concrete techniques. However, CAP is misapplied: partition tolerance is not optional; during a partition you choose consistency or availability. For payments, favouring consistency sacrifices availability, not partition tolerance. To reach Excellent, correct the CAP explanation and tie each choice to the C-versus-A trade-off during a partition.

*Assessor reasoning:* Both choices are reasonable and concrete techniques are named. However, CAP is misapplied: partition tolerance is not optional, and favouring consistency during a partition sacrifices availability, not partition tolerance.
> Question 5: "so for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are present and specific to the scenario. The consequences are one-sided: you list only positive outcomes. To reach Excellent, add at least one negative consequence (for example, a cost, risk, or trade-off) while keeping the positive consequence.

*Assessor reasoning:* Context, Decision and Consequences are present and specific. Consequences are one-sided: only positive outcomes are listed, with no negative consequence.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Headings and IEEE-style references are present. Question 2 is about 181 words, exceeding the 150-word limit. To reach Excellent, keep every answer within 150 words and maintain precise terminology and citations.

*Assessor reasoning:* Headings and IEEE-style references are present. However, Question 2 is about 181 words, exceeding the 150-word limit.
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
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | References |

## Technical issues

- Question 3(c): Uses payment-provider availability 99.9975% as overall order-placement availability; ignores the other three components. Correct end-to-end availability is 99.80% and downtime is 1.5 h/month.
- Question 3(c): Does not show the full end-to-end calculation for part (c), only the payment-provider calculation.
- Question 5: CAP theorem is misapplied: partition tolerance is not optional; during a partition one chooses consistency or availability. For payments, favouring consistency sacrifices availability, not partition tolerance.
- Question 1: Availability scenario response measure 'stay up most of the time' is not measurable.
- Question 6: Consequences list only positive outcomes; no negative consequence is given.
- Question 2: Answer is about 181 words, exceeding the 150-word limit.

## Next steps

1. Re-work Q3(c): compute end-to-end availability from all four components (not just the payment provider), show the full calculation, and report overall availability and downtime to the requested precision.
2. Revise Q5: state that partition tolerance is not optional; explain that during a partition you choose consistency or availability, and for payments consistency sacrifices availability—not partition tolerance.
3. Tighten Q1, Q6 and Q2: make the availability response measure measurable, add at least one negative consequence to Q6, and cut Q2 to 150 words or fewer while keeping the scenario-specific trade-offs.

---
<sub>Run Input_4-Run_2-Eff_high-261115-173124 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8119/11376 | cost $0.007424 (incl. $0.001628 for the reused reference rubric+task structure) | 60.19s</sub>
