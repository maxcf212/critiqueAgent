# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 24 / 40 (60%)**

You give a strong, scenario-specific recommendation in Question 2 and make relevant choices across the assignment. To strengthen your work, make every quality-attribute measure measurable, check the end-to-end availability calculations, explain the circuit-breaker states and CAP trade-off accurately, and complete the ADR consequences and references.

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

Question 1 identifies and justifies relevant attributes, and the performance scenario has a measurable target. For the next level, make the availability response measure measurable too—for example, specify an availability percentage or maximum downtime—and ensure both scenarios clearly include all six parts.

*Assessor reasoning:* Both attributes are relevant and justified with scenario details. The performance scenario has all six parts and measurable targets. The availability scenario also names the six parts, but its response measure, “most of the time,” is not measurable.
> Question 1: "The two most important quality attributes are performance and availability, because the business depends on the lunch hour"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Question 2 gives a clear modular-monolith recommendation tied to your five-person team and current problems, and acknowledges the downside of limited independent scaling and shared failure risk. This meets the Excellent criteria; preserve this scenario-specific trade-off reasoning.

*Assessor reasoning:* The recommendation is clear and supported by scenario-specific trade-offs involving the small team, operational overhead, current performance and deployment problems. It also acknowledges concrete downsides of the modular monolith.
> Question 2: "Instead the existing application should be restructured into a modular monolith with clear internal modules"  
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  

### C3 Q3 Availability calculation (3/8, Developing)

Your working in Question 3(a) is correct, but the downtime multiplication in (b) should give about 5.0 hours, not 3.5. In (c), include the other series components: the result is about 99.80% end-to-end availability and 1.5 hours of monthly downtime. Correct all parts to reach the next rubric level.

*Assessor reasoning:* Part (a) is correct. Part (b) has an arithmetic error: the downtime is about 5.0 hours, not 3.5. Part (c) gives payment-provider availability rather than end-to-end availability; including the other series components gives about 99.80% availability and 1.5 hours of monthly downtime.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Question 4 names a relevant pattern and connects it to the outage, but reverses its states. Closed permits calls; failures move the breaker to Open; successful Half-Open trials return it to Closed. Correctly explain this mechanism, then add a drawback or tuning consideration to meet Excellent.

*Assessor reasoning:* The circuit breaker is an appropriate pattern, and fast failure and a threshold are discussed. However, the state transitions are reversed: normal calls pass in Closed, failures open the breaker, and successful Half-Open trials close it. The outage application is relevant, but this central mechanism error limits the answer.
> Question 4: "When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed"  
> Question 4: "If they succeed it opens again, otherwise it stays closed."  

### C5 Q5 Consistency and availability (3/6, Proficient)

Question 5 makes reasonable choices and names Redis with a 60-second TTL for browsing. Correct the CAP explanation: during a partition, consistency and availability must be traded off. Name a concrete technique for the payment consistency choice as well as the browsing choice to meet Excellent.

*Assessor reasoning:* The availability choice for browsing and consistency preference for payment are reasonable, and Redis is a concrete browsing technique. CAP is misrepresented: during a partition, a system must trade consistency against availability, not give up partition tolerance. No concrete technique is named for the payment case.
> Question 5: "it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL)"  
> Question 5: "for payments we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (3/5, Proficient)

Question 6 includes scenario-specific Context, Decision, and Consequences, with benefits of the durable queue. To reach Excellent, add a relevant negative consequence—for example, that queued outlet updates may be delayed—and explain how you would address it.

*Assessor reasoning:* Context, decision and consequences are present and specific to the scenario. The consequences describe several benefits, but no negative consequence is stated, so the ADR is one-sided.
> Question 6: "Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply."  
> Question 6: "Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your required headings are used and answers appear within the word limit. To reach Excellent, keep every answer within 150 words, use precise terminology, and ensure citations and references match in IEEE style: citation [2] needs a reference-list entry. Also state your assumptions.

*Assessor reasoning:* The required headings and order are used, and the answers appear within the word limit. The reference list includes [1] but not cited source [2], and no assumptions are stated. These are citation and format problems.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*"  

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

- Question 3: The downtime multiplication in part (b) is incorrect: 0.00699 × 720 is approximately 5.0 hours, not 3.5.
- Question 3: Part (c) reports redundant payment availability as end-to-end availability. The other components remain in series, giving approximately 99.80% end-to-end availability and 1.5 hours of monthly downtime.
- Question 4: Circuit breaker state transitions are inverted: Closed permits normal calls, failures move it to Open for fast failure, and successful Half-Open trials return it to Closed.
- Question 5: CAP does not permit choosing consistency and availability while giving up partition tolerance; during a partition, consistency and availability must be traded off.
- Question 5: No concrete technique is provided for the payment consistency choice.
- References: Citation [2] has no corresponding reference-list entry, and the submission does not state assumptions.

## Next steps

1. In Question 3, show and check each calculation: 0.00699 × 720 is about 5.0 hours, and the redundant payment component does not replace the other components in the end-to-end calculation.
2. In Questions 4 and 5, explain circuit-breaker transitions in the correct order and state that during a partition CAP requires a trade-off between consistency and availability; name a concrete technique for each consistency/availability choice.
3. In Questions 1 and 6 and your References, replace vague measures with measurable targets, add a negative ADR consequence, include the missing reference for citation [2], and state your assumptions. Check each answer against the 150-word limit.

---
<sub>Run Input_4_d-Run_2-Eff_high-261116-120755 | marking=openai/gpt-6-luna, feedback=openai/gpt-6-luna | tokens in/out 8366/8748 | cost $0.005046 (incl. $0.001628 for the reused reference rubric+task structure) | 51.79s</sub>
