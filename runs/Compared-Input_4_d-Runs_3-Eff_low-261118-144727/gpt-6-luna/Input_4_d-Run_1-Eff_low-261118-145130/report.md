# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 21 / 40 (52.5%)**

You give a strong, scenario-specific modular-monolith recommendation in Question 2 and show sound methods for most of Question 3. To reach the next rubric levels, make the availability measure measurable, correct the circuit-breaker and CAP explanations, and complete the end-to-end calculation. Also add a negative consequence to the ADR and complete your references and assumptions.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Developing | 2 / 6 | 2 / 6 |
| C2 Q2 Architectural style | Excellent | 5 / 6 | 5 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 | 5 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Developing | 2 / 6 | 2 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 | 3 / 5 |
| C7 Communication and format | Developing | 2 / 4 | 2 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (2/6, Developing)

Question 1 connects performance and availability to the scenario, and the performance scenario has six parts with measurable measures. The availability measure is vague (“stay up most of the time”) and does not clearly address payment failure. Use a measurable target and complete the scenario.

*Assessor reasoning:* Performance and availability are justified using the scenario, and the performance scenario has six parts with measurable response measures. The availability scenario's measure is not measurable, and its response does not clearly address payment failure.
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (5/6, Excellent)

Question 2 earns 5/6. Your modular-monolith recommendation is tied to the five-person team, current problems and 12-month horizon; you explain relevant trade-offs and acknowledge a downside. To reach Excellent, make the trade-off justification fully satisfy the rubric.

*Assessor reasoning:* The modular-monolith recommendation is clear and tied to team size, existing performance and deployment problems, and the 12-month horizon. It gives multiple scenario-specific trade-offs and acknowledges a downside.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (5/8, Proficient)

Question 3(a) and (b) are essentially correct. In (c), you calculate redundant payment availability but do not combine it with the other required components. Recalculate end-to-end availability and downtime; the expected results are approximately 99.80% and 1.5 hours monthly.

*Assessor reasoning:* Parts (a) and (b) are essentially correct to the requested precision. In (c), the redundant payment availability is calculated correctly, but it is not combined with the other required components; therefore end-to-end availability and downtime are wrong.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Question 4 identifies an appropriate pattern and applies it to the outage, but reverses the Circuit Breaker states. Correctly explain Closed (calls pass), Open (calls blocked after failures) and Half-Open (trial calls). Include a drawback or tuning consideration for the next level.

*Assessor reasoning:* The Circuit Breaker is appropriate and its intended application is clear, but its states are explained incorrectly: normal traffic passes in Closed, failures open the breaker, and trial calls occur in Half-Open. The outage discussion does not correct this mechanism error.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  

### C5 Q5 Consistency and availability (2/6, Developing)

Question 5 gives a justified menu choice and a concrete cache technique. Correct the CAP explanation: during a partition, consistency and availability must be traded off. Name a concrete consistency technique for placing and paying for an order.

*Assessor reasoning:* The menu choice is justified with a concrete cache technique. The payment choice invokes CAP incorrectly: during a partition, a system cannot guarantee both consistency and availability. No concrete payment technique is named.
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Question 6 includes scenario-specific Context, Decision and Consequences. Your consequences are positive only; add a specific downside of the queue, such as eventual delivery, duplicate handling or operational overhead, to reach Excellent.

*Assessor reasoning:* Context, Decision, and Consequences are present and specific. The consequences are only positive; no negative consequence such as eventual delivery, duplicate handling, or queue-operation overhead is acknowledged.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (2/4, Developing)

Your required headings are used and the answers appear within the word limit. Citation and format requirements are incomplete: add the reference-list entry for [2] and state your assumptions. These changes are needed to improve this criterion.

*Assessor reasoning:* The required question headings and order are used, and answers appear within the word limit. Citation and format requirements are incomplete: reference [2] is missing, and assumptions are not stated.
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed. Upper Saddle River, NJ, USA: Addison-Wesley, 2012."  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | partial | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | partial | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | partial | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | partial | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | partial | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | no | References |

## Technical issues

- Question 3: Part (c) gives payment-system availability (99.9975%) as end-to-end order-placement availability. Multiplying by the other required component availabilities gives approximately 99.80% end-to-end availability and 1.5 hours monthly downtime.
- Question 4: Circuit Breaker state transitions are reversed: Closed permits calls, failures transition to Open, and Half-Open permits trial calls.
- Question 5: CAP is misstated. During a partition, a system must trade off consistency and availability; it cannot choose consistency and availability while giving up partition tolerance.
- Question 5: No concrete consistency technique is named for placing and paying for an order.
- Question 6: Consequences omit a negative consequence of introducing the queue.
- References: Citation [2] is used but has no corresponding reference-list entry, and no assumptions are stated.

## Next steps

1. In Question 1, replace “stay up most of the time” with a measurable availability target and explain how the system should respond when payment fails; include all six scenario parts.
2. In Question 3(c), combine the redundant payment availability with every other required component before calculating end-to-end availability and monthly downtime. In Question 4, state that Closed permits calls, failures open the breaker, and Half-Open allows trial calls.
3. In Question 5, explain that a partition forces a trade-off between consistency and availability, and name a concrete payment consistency technique. In Question 6, add a negative queue consequence; complete the [2] reference and state your assumptions.

---
<sub>Run Input_4_d-Run_1-Eff_low-261118-145130 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8160/4922 | cost $0.00348 (incl. $0.001628 for the reused reference rubric+task structure) | 25.51s</sub>
