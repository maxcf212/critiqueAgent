# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You produced an outstanding submission with full marks. You wrote measurable six-part scenarios, scenario-specific trade-offs, correct availability calculations, and well-applied patterns with balanced ADRs and precise communication. Keep using this specific, evidence-based style.

## Marks

| Criterion | Level | Score | Points |
|---|---|---|---|
| C1 Q1 Quality attributes | Excellent | 6 / 6 | 6 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 | 6 / 6 |
| C3 Q3 Availability calculation | Excellent | 8 / 8 | 8 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 | 5 / 5 |
| C5 Q5 Consistency and availability | Excellent | 6 / 6 | 6 / 6 |
| C6 Q6 Architecture decision record | Excellent | 5 / 5 | 5 / 5 |
| C7 Communication and format | Excellent | 4 / 4 | 4 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (6/6, Excellent)

In Question 1 you chose well-justified attributes and wrote complete six-part scenarios with measurable measures like 'p95 response time is under 1.5 s'. You are at Excellent. To stay there, keep selecting the two most critical attributes and keeping every response measure measurable.

*Assessor reasoning:* Two relevant attributes chosen with scenario justification. Both scenarios contain all six parts with clear measurable response measures.
> Question 1: "Response measure: the p95 response time is under 1.5 s"  
> Question 1: "menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

In Question 2 your modular monolith recommendation with scenario-specific trade-offs on team overhead and single-VM issues was excellent, and you acknowledged the downside about modules not scaling independently. You are at Excellent. To stay there, continue linking both trade-offs to the scenario and naming a downside.

*Assessor reasoning:* Clear recommendation. Two scenario-specific trade-offs: team overhead and fixing single VM/rolling deploy issues. Downside acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets)"  
> Question 2: "modules cannot be scaled independently and a bug in one module can still crash"  

### C3 Q3 Availability calculation (8/8, Excellent)

In Question 3 your series calculation A=0.99301, 720h downtime and parallel result A_new=0.99798 were all correct with working to required precision. You are at Excellent. To stay there, keep showing series/parallel working and checking rounding and precision.

*Assessor reasoning:* All three parts correct with working. Series multiplication, 720h downtime, parallel payment formula correct to required precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798"  

### C4 Q4 Resilience pattern (5/5, Excellent)

In Question 4 you correctly explained Closed/Open/Half-Open Circuit Breaker and applied it to the 25-min outage with tuning like sensitivity causing rejected payments. You are at Excellent. To stay there, keep applying the mechanism to the outage and including a drawback.

*Assessor reasoning:* Appropriate pattern named, Closed/Open/Half-Open mechanism correct, applied to 25-min outage, tuning and drawback given.
> Question 4: "The Circuit Breaker pattern [2] would have contained the failure."  
> Question 4: "Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded"  

### C5 Q5 Consistency and availability (6/6, Excellent)

In Question 5 your AP browsing with Redis 60-second TTL cache and CP payment with idempotency key were well justified with correct CAP use. You are at Excellent. To stay there, keep justifying both choices via partition trade-off and naming a concrete technique for each.

*Assessor reasoning:* AP for browsing, CP for payment justified. CAP correctly states partition requires C/A trade-off. Concrete techniques named for each.
> Question 5: "show a slightly stale menu from a cache (Redis with a 60-second TTL)"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create"  

### C6 Q6 Architecture decision record (5/5, Excellent)

In Question 6 your OrderPaid event via RabbitMQ ADR had specific Context, Decision and positive/negative Consequences like extra work for five developers. You are at Excellent. To stay there, keep all three sections scenario-specific with balanced consequences.

*Assessor reasoning:* Context, Decision, Consequences present and scenario-specific. Positive and negative consequences included.
> Question 6: "Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

Across all answers you stayed within 150 words with precise terminology, ordered headings and IEEE citations like Bass et al. You are at Excellent. To stay there, keep checking word limits, headings and IEEE references.

*Assessor reasoning:* All answers within 150 words, headings in order, precise terminology, IEEE citations and reference list present.
> Question 1: "Performance and availability matter most: 900 orders arrive in the lunch hour"  
> References: "[1] L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 3rd ed."  

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

## Next steps

1. Keep writing response measures with numbers and time bounds like p95 under 1.5 s.
2. Keep tying trade-offs and decisions to CampusEats load, team size and outage details.
3. Keep showing working to required precision and citing IEEE sources with ordered headings.

---
<sub>Run Input_4_u-Run_2-Eff_high-261116-140238 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8035/11578 | cost $0.003658 (incl. $0.001628 for the reused reference rubric+task structure) | 43.7s</sub>
