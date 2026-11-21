# Input_4: Graded Feedback (one-shot)

**Total: 29 / 40 (72.5%)**

Strong applied reasoning for style and resilience patterns. Main gaps: measurable availability scenario, correct recombination for second payment provider in Q3c, correct CAP reasoning, and explicit negative consequences in ADR plus word-count compliance.

## Marks

| Criterion | Level | Points |
|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Good choice of performance and availability linked to 900-orders lunch peak and 4.2s p95 abandonment. Performance scenario has full six parts and measurable measure (p95 <1.5s). Availability scenario has six parts but Response Measure 'should stay up most of the time' is not measurable - needs e.g., % uptime or max detection/recovery time.

### C2 Q2 Architectural style (6/6, Excellent)

Clear recommendation: keep modular monolith, not microservices rewrite. Two specific trade-offs: 5-dev team vs operational overhead of 8-10 services, and known problems (single VM p95, 20-min deploys) fixable with horizontal monolith instances + rolling deploys. Downside acknowledged (no independent scaling, single-process crash).

### C3 Q3 Availability calculation (5/8, Proficient)

(a) Correct: 0.9995*0.999*0.9995*0.995 = 0.99301 = 99.30%. (b) Correct: 720h *0.00699 = 5.0h (5.03h). (c) Incorrect final combination: Apay=1-(0.005)^2=0.999975 correct, but new system availability must multiply all four: 0.9995*0.999*0.9995*0.999975 = 99.80% not 99.9975%, and downtime ~1.5h not 0.0h. Method understood but arithmetic for combined availability wrong.

### C4 Q4 Resilience pattern (5/5, Excellent)

Circuit Breaker correctly chosen for problem 2 (thread-pool exhaustion). Explains Closed/Open/Half-Open, fast-fail to protect browsing, and applies to 25-min slow payment case with user message. Includes tuning consideration: 50% failure in 10s threshold and wait period.

### C5 Q5 Consistency and availability (3/6, Proficient)

(i) Menu browsing favouring availability with stale cache (Redis 60s TTL) and eventual consistency is appropriate. (ii) Payment favouring consistency is appropriate and idempotency key is useful, but CAP explanation is incorrect: you cannot give up partition tolerance in a distributed system; during partition you choose CP and sacrifice availability. Should state strong consistency via ACID transaction/payment provider.

### C6 Q6 Architecture decision record (3/5, Proficient)

ADR has Status, Context (sync call loses order when tablet offline + adds to p95), Decision (publish OrderPaid to RabbitMQ with retrying worker). Positive consequences given (lower latency, durability, smoothing peak). Missing required negative consequence, e.g., operational complexity, need for DLQ, at-least-once duplicates, eventual consistency for kitchen.

### C7 Communication and format (3/4, Proficient)

Headings used, terminology precise, IEEE citations for Bass and Nygard. Q2 exceeds 150-word limit (~190 words) so per rubric max 3 for communication.

## Next steps

1. Make all response measures quantifiable: e.g., 'API Gateway health stays 99.9% and browse requests succeed within 2s during payment slowness'
2. Recompute availability as product of all components including redundant payment: A_new = 0.9995*0.999*0.9995*0.999975 = 99.80% => downtime ~1.5h
3. Correct CAP statement: partition tolerance is mandatory; for menu choose AP (cached eventual), for orders choose CP (refuse new payments during partition)
4. Add at least one negative consequence to ADR: e.g., infrastructure to operate, duplicate delivery requires idempotency at tablet, added latency for delivery semantics

---
<sub>Run Input_4-Run_2-Eff_low-261113-201515 | oneshot=meta/muse-spark-1.3-contributor | tokens in/out 3256/1914 | cost $0.000708 | 14.96s</sub>
