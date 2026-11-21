# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 38 / 40 (95%)**

You produced a strong, well-reasoned submission. Your attribute choices, modular-monolith recommendation and decision record are closely tied to CampusEats facts, and your availability calculations are correct with working shown. The main gaps are an explicit assumptions statement, a stronger consistency mechanism in Question 5, and a few unsupported figures in Questions 2 and 4.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 5 / 6 | 5 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Proficient | 3 / 4 | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

You chose two attributes that matter most, performance and availability, and tied them to scenario facts such as the 900 lunch-hour orders and the 4.2 s p95 payment slowdown. Both scenarios have all six parts, and your response measures are quantified and testable, such as p95 under 1.5 s with no dropped requests. Your answer sits at the word limit, so keep future answers concise.

*Assessor reasoning:* Two attributes are chosen and tied to scenario facts (900 orders, 4.2 s p95, payment slowdown). Both scenarios have all six parts, and both response measures are quantified and testable. Word count is at the limit but compliant.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> Question 1: "Response measure: the p95 response time is under 1.5 s and no requests are dropped."  

### C2 Q2 Architectural style (6/6, Excellent)

Your modular-monolith recommendation is clear, and both trade-offs are linked to the scenario: a five-person team and the lunchtime slowness from the single virtual machine. You also acknowledge the downside of the recommendation. The 'eight or more services' figure is not derived from the scenario, so either justify it from the brief or state it explicitly as an assumption.

*Assessor reasoning:* Clear modular-monolith recommendation with two trade-offs tied to team size and known problems (single VM, weekly downtime). The downside is explicitly acknowledged. The 'eight or more services' figure is an unstated assumption, which slightly weakens it but does not lower the level.
> Question 2: "Five developers running eight or more services would spend more time on infrastructure than on features."  
> Question 2: "The lunchtime slowness comes from a single virtual machine and is fixed by running several instances"  

### C3 Q3 Availability calculation (8/8, Excellent)

All three parts are correct: 99.30% availability for placing an order, 5.0 hours of monthly downtime, and 99.80% availability after the change, with 1.5 hours of downtime. Your working is shown and the precision matches the request. The method is sound, but you did not state that the components are independent and in series, or give the component mapping. Adding these would make the answer fully transparent.

*Assessor reasoning:* Recomputed: (a) 0.99301 gives 99.30%; (b) 0.00699×720 = 5.03, so 5.0 h; (c) A_pay = 0.999975, A_new = 0.997976 gives 99.80%, and downtime 1.46 gives 1.5 h. All correct, working shown, precision as requested.
> Question 3: "The availability of placing an order is 99.30%."  
> Question 3: "The new availability of placing an order is 99.80%."  

### C4 Q4 Resilience pattern (5/5, Excellent)

You named the Circuit Breaker pattern and explained its Closed, Open and Half-Open states correctly. You applied it directly to the 25-minute payment hang and discussed tuning and drawbacks, noting that the threshold must come from real latency data. Your claim that the breaker would have opened within seconds needs a supporting threshold or timing calculation, because at present it is asserted rather than shown.

*Assessor reasoning:* Circuit Breaker is an appropriate pattern with correct Closed/Open/Half-Open mechanics. It is applied directly to the 25-minute payment hang, and tuning and drawback are discussed. The claim 'opened within seconds' is asserted without support.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Tuning consideration: the threshold must come from real latency data."  

### C5 Q5 Consistency and availability (5/6, Excellent)

Your choices are justified, you state the CAP theorem correctly, and Redis TTL caching is a concrete AP technique. For the CP case, the idempotency key prevents duplicate charges but does not by itself enforce consistency during a partition. Name a specific CP mechanism, such as quorum or consensus, and explain how it works when the network partitions.

*Assessor reasoning:* Both choices are justified and CAP is stated correctly. Redis TTL caching is a concrete AP technique. The idempotency key is concrete but mainly prevents duplicate charges rather than providing partition-time consistency, so the CP mechanism is weakly named.
> Question 5: "The CAP theorem says that during a partition a system must give up either consistency or availability"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge."  

### C6 Q6 Architecture decision record (5/5, Excellent)

Your decision record includes Context, Decision and Consequences, all specific to CampusEats, including the 4.2 s p95 and offline tablets. You give positive consequences, such as improved response time, and negative ones, including at-least-once delivery requiring duplicate handling and orders being paid before the outlet sees them. This clearly documents the trade-offs.

*Assessor reasoning:* Context, Decision and Consequences are all present and specific to CampusEats (4.2 s p95, offline tablets, five developers). Positive and negative consequences are both given, including the at-least-once and 'paid before outlet sees it' risks.
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs."  
> Question 6: "Placing an order no longer waits for the outlet, so the response time improves."  

### C7 Communication and format (3/4, Proficient)

Your headings are correct, your writing is clear, and you cite sources in-text in IEEE style. Several answers are at or near the 150-word limit, so tighten Questions 1 and 5 to leave a margin. The assumptions statement required by the brief is missing, and the references requirement was only partly met. The marking does not specify the reference issue, so check your list against the IEEE requirements.

*Assessor reasoning:* Headings are correct, citations are IEEE-style and in-text, and the writing is clear. Answers are at or near the 150-word limit (Q1 and Q5 are borderline). No assumptions statement is provided despite the explicit requirement, so this falls to Proficient.
> References: "[1] L. Bass, P. Clements, and R. Kazman"  
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  

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

- Question 3: Assumes the four component availabilities are independent and in series without stating this assumption, and does not state the component mapping.
- Question 2: 'Eight or more services' is an unstated assumption not derived from the scenario.
- Question 5: Idempotency keys prevent duplicate charges but do not themselves enforce consistency during a partition; the CP mechanism (e.g., quorum or consensus) is not named.
- Question 4: Claim that the breaker 'would have opened within seconds' is asserted without a supporting threshold or timing calculation.

## Next steps

1. Add an explicit assumptions statement before your Question 3 calculations. State the component mapping and that the four components are independent and in series, so the reader can check your working.
2. In Question 5, name a concrete CP mechanism such as quorum or consensus and explain how it keeps data consistent during a partition. Idempotency keys prevent duplicate charges but do not by themselves enforce consistency.
3. Support the 'within seconds' claim in Question 4 with a threshold or timing calculation. Derive the 'eight or more services' figure from the scenario or state it as an assumption. Check your reference list against the IEEE requirements in the brief.

---
<sub>Run Input_4_u-Run_2-Eff_high-261116-141129 | marking=anthropic/claude-haiku-5.5, feedback=anthropic/claude-haiku-5.5 | tokens in/out 11726/18987 | cost $0.010722 (incl. $0.001628 for the reused reference rubric+task structure) | 71.25s</sub>
