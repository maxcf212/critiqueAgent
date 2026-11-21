# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 25 / 40 (62.5%)**

You scored 25/40. Your Q2 modular-monolith recommendation is excellent and Q1 justification is strong. The main losses are in Q3 calculations, Q4 circuit-breaker states, Q5 CAP use, Q6 consequences, and formatting/citations. Use the next steps to target the specific rubric gaps.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Developing | 3 / 8 | 3 / 8 |
| C4 Q4 Resilience pattern | Developing | 2 / 5 | 2 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

You chose performance and availability and justified both from the scenario. Your performance scenario is complete and measurable. To reach Excellent, make the availability response measure measurable—replace 'stay up most of the time' with a numeric target such as 99.9% monthly uptime—so both scenarios have all six parts and measurable measures.

*Assessor reasoning:* Attributes are well chosen and justified; performance scenario is complete and measurable. Availability scenario has six parts but its response measure is not measurable, so not Excellent.
> Question 1: "The two most important quality attributes are performance and availability"  
> Question 1: "Response measure: the system should stay up most of the time."  

### C2 Q2 Architectural style (6/6, Excellent)

Excellent: your modular-monolith recommendation is clearly tied to the five-person team, single VM, deployment downtime and rewrite risk, and you acknowledge the scaling downside. Keep this structure. No rubric action needed here; just watch the word limit noted under C7.

*Assessor reasoning:* Clear modular-monolith recommendation tied to five-person team, single VM, deployment downtime, and rewrite risk; downside acknowledged. Excellent.
> Question 2: "With five developers, running eight or ten services would mean more time spent on infrastructure than on features."  
> Question 2: "The trade-off I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (3/8, Developing)

Part (a) is correct. In (b), 0.00699 × 720 = 5.03 hours, not 3.5. In (c), payment availability alone is not end-to-end; multiply all component availabilities to get about 99.80% and 1.46 hours downtime. Show each step to reach Excellent.

*Assessor reasoning:* Part (a) correct. Part (b) arithmetic wrong: 0.00699×720=5.03h, not 3.5h. Part (c) treats payment availability as end-to-end and omits other components; correct end-to-end is about 99.80% and 1.46h downtime. Two parts incorrect.
> Question 3: "Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month."  
> Question 3: "So the new availability of placing an order is 99.9975%"  

### C4 Q4 Resilience pattern (2/5, Developing)

Circuit breaker is the right pattern and you apply it to the outage, but the states are reversed: Closed is normal, Open fails fast, Half-Open allows trial calls. Correct the state semantics and add a clear drawback or tuning consideration (e.g., threshold calibration) to move from Developing to Proficient/Excellent.

*Assessor reasoning:* Circuit breaker is appropriate and applied, but state semantics are reversed: Closed is normal, Open fails fast, Half-Open trials. No clear drawback/tuning consideration beyond threshold example. Explanation incorrect.
> Question 4: "In the Open state calls pass through normally."  
> Question 4: "the breaker moves to Closed and calls fail immediately"  

### C5 Q5 Consistency and availability (3/6, Proficient)

Your menu choice and cache technique are good. For payment, name a concrete consistency technique (e.g., transactional outbox or two-phase commit). CAP is misused: during a partition you cannot give up partition tolerance; you choose consistency or availability. Correct that framing and justify both choices to reach Excellent.

*Assessor reasoning:* Menu choice and cache technique are good. Payment choice is reasonable but no concrete technique is named, and CAP is misused: partition tolerance cannot be given up during a partition; choose C or A.
> Question 5: "we choose consistency and availability and give up partition tolerance."  

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are present and specific. To reach Excellent, add at least one negative consequence—for example, the outlet no longer gets synchronous order confirmation, or added complexity in handling asynchronous failures—so the consequences are balanced.

*Assessor reasoning:* Context, Decision, Consequences present and specific. Consequences are all positive; no negative consequence, so Proficient not Excellent.
> Question 6: "Consequences: Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Writing is clear and headings are used. Q2 is about 181 words, over the 150-word limit, and [2] is cited in Q4 but missing from the reference list. Trim Q2 and add the missing IEEE-style reference to reach Excellent.

*Assessor reasoning:* Writing is clear and headings used, but Q2 is about 181 words (over 150), and [2] is cited without a reference-list entry. Minor citation/format issues.
> Question 2: "The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process."  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice"  

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

- Question 1: Availability response measure 'stay up most of the time' is not measurable.
- Question 3: Part (b) arithmetic error: 0.00699 × 720 = 5.03 hours, not 3.5 hours.
- Question 3: Part (c) uses payment availability as end-to-end availability; other components must also be multiplied, giving about 99.80% and 1.46 hours downtime, not 99.9975% and 0.018 hours.
- Question 4: Circuit breaker states are reversed: Closed is normal, Open fails fast, Half-Open allows trial calls.
- Question 5: CAP theorem is misused: partition tolerance cannot be given up during a partition; the choice is C or A. No concrete payment consistency technique is named.
- Question 6: No negative consequence is given in the ADR.
- Question 2: Answer exceeds the 150-word limit (about 181 words).
- References: Reference [2] is cited in Question 4 but missing from the reference list.

## Next steps

1. Recompute Q3(b) and Q3(c) showing each step: 0.00699 × 720 = 5.03 h, and multiply all component availabilities for end-to-end availability (~99.80%, ~1.46 h).
2. Correct Q4's circuit-breaker states (Closed normal, Open fails fast, Half-Open trial) and add a tuning or drawback sentence.
3. In Q5, state CAP as choosing C or A during a partition and name a concrete payment consistency technique; in Q6 add a negative consequence; trim Q2 to 150 words and add reference [2].

---
<sub>Run Input_4_d-Run_2-Eff_high-261116-120542 | marking=deepseek/deepseek-v4.1-flash-1017:thinking, feedback=deepseek/deepseek-v4.1-flash-1017:thinking | tokens in/out 8212/12842 | cost $0.007876 (incl. $0.001628 for the reused reference rubric+task structure) | 34.41s</sub>
