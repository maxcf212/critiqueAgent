# Input_4: Graded Feedback (one-shot)

**Total: 28 / 40 (70%)**

Solid application of concepts: good attribute choice and modular monolith justification with scenario trade-offs, correct series availability and circuit breaker. Main gaps are unmeasurable availability measure, incorrect overall availability in Q3c, CAP misstatement in Q5ii and idempotency-key not a consistency technique, ADR lacking negative consequence, and Q2 over word limit.

## Marks

| Criterion | Level | Points |
|---|---|---|
| C1 Q1 Quality attributes | Proficient | 3 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 5 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 3 / 6 |
| C6 Q6 Architecture decision record | Proficient | 3 / 5 |
| C7 Communication and format | Proficient | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (3/6, Proficient)

Two relevant attributes (performance, availability) chosen with scenario-based justification. Performance scenario has six parts and measurable measure (p95 <1.5s). Availability scenario has six parts but response measure 'stay up most of the time' is not measurable. Source/stimulus/artefact/environment/response are present but second measure fails rubric requirement.

### C2 Q2 Architectural style (6/6, Excellent)

Clear recommendation to keep modular monolith, not full microservices. Two specific trade-offs: (1) team size 5 vs operational overhead of 8-10 services pipelines/monitoring, (2) known problems are single VM and deployment process fixable by horizontal scaling and rolling deployments. Downside acknowledged (no independent scale, process-wide crash). Specific to CampusEats.

### C3 Q3 Availability calculation (5/8, Proficient)

(a) correct method 0.9995*0.999*0.9995*0.995 = 0.99301 -> 99.30%. (b) correct 720h*(1-A) ~5.0h to one decimal. (c) payment availability 1-(0.005)^2=0.999975 correct, but new overall availability incorrectly reported as 99.9975% using payment only. Correct overall = 0.9995*0.999*0.9995*0.999975 ≈ 99.80% and downtime ≈ 1.5h. Arithmetic slip in final step.

### C4 Q4 Resilience pattern (5/5, Excellent)

Circuit Breaker correctly named. Mechanism explained (Closed/Open/Half-Open, failure threshold, fast-fail to avoid thread pool exhaustion). Applied well to Problem 2 – would isolate payment provider slowness and keep menu browsing working. Tuning consideration given (50% in 10s threshold, wait period). Could explicitly list drawback (need to choose timeout/threshold, stale fallback UX) but meets requirement for tuning.

### C5 Q5 Consistency and availability (3/6, Proficient)

(i) menu browsing – favour availability with concrete technique Redis cache 60s TTL and rationale about stale read tolerable – correct and good CAP use (eventual consistency). (ii) placing/paying – favour consistency correct, but CAP explanation is incorrect: 'choose consistency and availability and give up partition tolerance' – in distributed systems partition tolerance must be assumed. Technique given (idempotency key) does not provide consistency across replica/partition; should name strong consistency, single-writer, transactional outbox, or synchronous payment ledger. One technique misaligned.

### C6 Q6 Architecture decision record (3/5, Proficient)

ADR has Context (sync tablet call, lost orders, p95 impact), Decision (RabbitMQ durable OrderPaid event + retrying worker), Positive consequences (decoupling, offline tablet recovery, peak smoothing). Specific to Problem 4. Negative consequence missing – e.g., operational complexity of broker, need for idempotent consumers, eventual notification latency, ordering/deduplication – required for Excellent.

### C7 Communication and format (3/4, Proficient)

Headings used, precise terminology, IEEE citations present. Q2 exceeds 150-word limit (~180 words in submission). All other answers within limit. Minor citation formatting okay.

## Next steps

1. Rewrite availability scenario measure to be measurable, e.g., '99.9% of browse requests succeed during payment-provider degraded mode' or 'system in degraded mode within 5s'.
2. Recalculate Q3c as A_total = A_gateway*A_order*A_db*A_pay-new ≈ 99.80% and downtime ≈ (1-A_total)*720 ≈ 1.5h to 1 decimal place.
3. Fix CAP explanation: during partition you must choose between C and A (P is mandatory); for payments choose C, for menu choose A. Replace idempotency key with strong consistency technique such as single DB transaction for order+payment state or synchronous confirmation before acknowledging.
4. Add at least one explicit negative consequence to ADR-007 such as broker operating cost, monitoring, retry poison messages, need for idempotent/replay handling.
5. Trim Q2 to <=150 words by removing generic sentences.

---
<sub>Run Input_4-Run_1-Eff_low-261113-201455 | oneshot=meta/muse-spark-1.3-contributor | tokens in/out 3256/2348 | cost $0.000795 | 19.54s</sub>
