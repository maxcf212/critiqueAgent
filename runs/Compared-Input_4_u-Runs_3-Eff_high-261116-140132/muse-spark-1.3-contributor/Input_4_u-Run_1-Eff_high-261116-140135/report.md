# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

Outstanding work — you achieved full marks across all questions. Your scenarios were measurable, trade-offs scenario-specific, calculations precise, and patterns well applied. Keep this precision and justification as you tackle larger design tasks.

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

You excellently justified performance and availability from the lunch peak in Question 1 with measurable p95 response time is under 1.5 s and no requests are dropped. You included all six parts for both scenarios. You are at Excellent – maintain this by keeping every response measure quantifiable.

*Assessor reasoning:* Performance and availability justified from lunch peak, p95 and outage. Both scenarios list all six parts with measurable response measures including p95 thresholds, failure rates and recovery time.
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped."  
> Question 1: "menu p95 stays under 2 s, under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

You gave a clear modular monolith recommendation in Question 2 I recommend a modular monolith with two scenario-specific trade-offs around 5 developers and single-VM. You acknowledged scaling downside. You are at Excellent – keep linking trade-offs to team and load.

*Assessor reasoning:* Clear modular monolith recommendation. Two scenario-specific trade-offs: 5-developer operational overhead and single-VM plus rolling-deployment fixes. Downside of shared fate and scaling explicitly accepted.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets)"  
> Question 2: "The downside I accept is that modules cannot be scaled independently"  

### C3 Q3 Availability calculation (8/8, Excellent)

You showed correct working in Question 3 A = 0.9995 x 0.999 x 0.9995 x 0.995 = 0.99301 achieving 99.30% 5.0h and 99.80% 1.5h to requested precision. You handled series, parallel payment and 720-hour downtime perfectly. You are at Excellent – continue showing all steps and rounding.

*Assessor reasoning:* Series multiplication, parallel payment calculation and downtime using 720 hours all correct. Results 99.30% 5.0h and 99.80% 1.5h to requested precision with working shown.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

You correctly explained Circuit Breaker Closed/Open/Half-Open in Question 4 When failures exceed a threshold the breaker moves to Open applied to payment hang. You noted tuning Too sensitive and it opens on a brief blip. You are at Excellent – keep adding drawback/tuning.

*Assessor reasoning:* Circuit Breaker correctly described with Closed Open Half-Open, applied to payment hang preserving browsing, plus tuning threshold and open-state drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open"  
> Question 4: "Too sensitive and it opens on a brief blip"  

### C5 Q5 Consistency and availability (6/6, Excellent)

You justified menu AP vs order CP in Question 5 using CAP correctly with show a slightly stale menu from a cache Redis with a 60-second TTL and idempotency key. Both techniques were concrete. You are at Excellent – sustain this by pairing each CAP choice with a specific mechanism.

*Assessor reasoning:* Menu AP vs order CP both justified, CAP partition trade-off stated correctly, concrete techniques Redis TTL and idempotency key with fail-fast CP behaviour named.
> Question 5: "show a slightly stale menu from a cache (Redis with a 60-second TTL)"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create"  

### C6 Q6 Architecture decision record (5/5, Excellent)

You built a specific ADR in Question 6 Publish an OrderPaid event to a durable message queue RabbitMQ with Context on tablet loss and both positive latency and negative queue is one more component for five developers. You are at Excellent – keep balancing positives with negatives.

*Assessor reasoning:* ADR has specific Context on synchronous tablet loss and p95, Decision RabbitMQ worker retry, positive latency and offline benefits and negative ops at-least-once and paid-before-seen consequences.
> Question 6: "Publish an "OrderPaid" event to a durable message queue (RabbitMQ)."  
> Question 6: "The queue is one more component for five developers to run and monitor."  

### C7 Communication and format (4/4, Excellent)

You kept all answers within 150 words with Question 1-6 headings, precise terminology and IEEE citations like L. Bass, P. Clements, and R. Kazman. Your writing was clear throughout. You are at Excellent – maintain headings, limits and citation accuracy.

*Assessor reasoning:* Headings Question 1 through Question 6 in order, all answers within 150 words, precise terminology, in-text [1][2] citations and IEEE reference list.
> References: "[1] L. Bass, P. Clements, and R. Kazman,"  
> Question 1: "Source: students using the mobile app."  

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

1. Keep practising six-part scenarios with p95 measures to retain precision under time pressure.
2. Continue weighing operational cost for a 5-developer team when evaluating styles in future designs.
3. Maintain IEEE citation habit and 150-word conciseness in upcoming reports.

---
<sub>Run Input_4_u-Run_1-Eff_high-261116-140135 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8101/14254 | cost $0.004525 (incl. $0.001628 for the reused reference rubric+task structure) | 62.16s</sub>
