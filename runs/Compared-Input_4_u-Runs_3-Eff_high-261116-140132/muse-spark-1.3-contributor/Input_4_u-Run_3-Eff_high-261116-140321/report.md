# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions: Graded Feedback

**Total: 40 / 40 (100%)**

You produced a strong complete submission with correct calculations and well-justified architecture choices across all six questions and clear communication. Keep this precision and scenario grounding as you tackle larger design tasks.

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

In Question 1 you justified two central attributes from the scenario and wrote complete six-part scenarios. Your measures like p95 under 1.5 s and under 0.1% fail are measurable. You meet Excellent; keep every future scenario fully six-part and quantitative.

*Assessor reasoning:* Two central attributes chosen with scenario justification. Both scenarios contain all six parts with quantitative measurable response measures.
> Question 1: "the p95 response time is under 1.5 s and no requests are dropped"  
> Question 1: "under 0.1% of non-payment requests fail"  

### C2 Q2 Architectural style (6/6, Excellent)

In Question 2 you recommended a modular monolith with modules orders, menu and linked trade-offs to 5-dev overhead and VM/downtime. You acknowledged downside about modules not scaling independently. You meet Excellent; keep grounding both trade-offs and downside in scenario.

*Assessor reasoning:* Clear modular-monolith recommendation. Two scenario-specific trade-offs: 5-dev ops overhead and single-VM/weekly-downtime fixes. Downside acknowledged.
> Question 2: "I recommend a modular monolith (modules: orders, menu, payments, outlets)"  
> Question 2: "modules cannot be scaled independently and a bug in one module can still crash"  

### C3 Q3 Availability calculation (8/8, Excellent)

In Question 3 you showed working for series A = 0.9995 x 0.999 x 0.9995 x 0.995 = 0.99301, downtime and A_pay = 1-(1-0.995) squared to required precision. All parts correct. You meet Excellent; keep showing method steps and rounding exactly as requested.

*Assessor reasoning:* Series multiplication, 720h downtime, and active-active parallel payment all correct. Working shown, 99.30%/5.0h and 99.80%/1.5h to required precision.
> Question 3: "A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301"  
> Question 3: "A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975"  

### C4 Q4 Resilience pattern (5/5, Excellent)

In Question 4 you explained Circuit Breaker Closed/Open/Half-Open and applied it to the 25-min hang with calls fail immediately and tuning note Too sensitive. You meet Excellent; keep adding an applied mechanism plus drawback/tuning.

*Assessor reasoning:* Circuit Breaker correctly described with Closed/Open/Half-Open, applied to 25-min hang, with tuning and fallback drawback.
> Question 4: "When failures exceed a threshold the breaker moves to Open and calls fail immediately"  
> Question 4: "Too sensitive and it opens on a brief blip"  

### C5 Q5 Consistency and availability (6/6, Excellent)

In Question 5 you justified AP browsing with stale menu via Redis with 60-second TTL and CP payment with idempotency key. You used CAP correctly. You meet Excellent; keep pairing each choice with correct CAP reasoning and concrete technique.

*Assessor reasoning:* AP for browsing and CP for payment justified. CAP used correctly with partition tolerance mandatory. Concrete techniques named for both.
> Question 5: "show a slightly stale menu from a cache (Redis with a 60-second TTL)"  
> Question 5: "Each order request carries an idempotency key, so a retry does not create a second charge"  

### C6 Q6 Architecture decision record (5/5, Excellent)

In Question 6 you gave specific Context, Decision Publish an OrderPaid event with RabbitMQ and both consequences including must ignore duplicate order IDs. You meet Excellent; keep context specific with positive and negative consequences.

*Assessor reasoning:* Specific Context, Decision, and both positive and negative consequences present and tied to tablet loss and p95 scenario.
> Question 6: "Publish an "OrderPaid" event to a durable message queue (RabbitMQ)"  
> Question 6: "Delivery is at-least-once, so the tablet must ignore duplicate order IDs"  

### C7 Communication and format (4/4, Excellent)

Across Questions 1-6 you stayed within 150 words, used headings in order and precise terminology with six-part form from [1] and IEEE list. You meet Excellent; keep word-count discipline and IEEE citations.

*Assessor reasoning:* Headings Question 1-6 in order, all answers <=150 words, precise terminology, in-text citations and IEEE reference list.
> Question 1: "The scenarios use the six-part form from [1]"  
> References: "[1] L. Bass, P. Clements, and R. Kazman,"  

## Task requirements

| ID | Requirement | Met | Where |
|---|---|---|---|
| R1 | Question 1: Identify the two most important quality attributes for CampusEats and justify each choice using the scenario. For each attribute, provide a quality attribute scenario with all six parts: source, stimulus, artefact, environment, response, and a measurable response measure. | yes | Question 1 |
| R2 | Question 2: Recommend an architectural style for the next 12 months (for example, monolith, modular monolith, or microservices). Justify the recommendation with at least two trade-offs specific to CampusEats. | yes | Question 2 |
| R3 | Question 3: Show your working. Calculate (a) order-placement availability using the component availabilities and independent failures, (b) expected order-placement downtime in hours per 30-day month, and (c) end-to-end availability and monthly downtime when a second independent payment provider of 99.5% availability is added active-active, with payment unavailable only when both providers are down. | yes | Question 3 |
| R4 | Question 4: Name one architectural resilience pattern that could contain the slow-payment-provider failure. Explain how it works and would limit the outage, and state at least one drawback or tuning consideration. | yes | Question 4 |
| R5 | Question 5: For menu browsing and for placing and paying for an order, choose whether to favour availability or consistency during a network partition. Justify each choice with reference to CAP theorem and name one concrete technique for each. | yes | Question 5 |
| R6 | Question 6: Write a short ADR for introducing a message queue between order payment and outlet notification. Include Context, Decision, and Consequences, with at least one positive and one negative consequence. | yes | Question 6 |
| R7 | State any assumptions made. Cite external sources in IEEE style and include the corresponding reference list; references do not count toward answer word limits. | partial | - |

## Next steps

1. Keep writing measurable response measures for every quality-attribute scenario you create.
2. Keep tying each architectural trade-off and downside explicitly to team, load and failure context.
3. Keep showing full calculation working and citing sources in IEEE style to retain precision.

---
<sub>Run Input_4_u-Run_3-Eff_high-261116-140321 | marking=meta/muse-spark-1.3-contributor, feedback=meta/muse-spark-1.3-contributor | tokens in/out 8046/12196 | cost $0.003646 (incl. $0.001628 for the reused reference rubric+task structure) | 54.51s</sub>
