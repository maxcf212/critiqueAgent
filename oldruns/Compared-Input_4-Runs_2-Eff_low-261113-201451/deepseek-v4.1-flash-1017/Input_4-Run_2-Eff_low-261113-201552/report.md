# Input_4: Graded Feedback (one-shot)

**Total: 32 / 40 (80%)**

Strong answers on architectural style, resilience and ADR structure. Main losses are the non-measurable availability response measure in Q1, the part (c) calculation error in Q3, the CAP theorem misstatement in Q5, the missing negative consequence in Q6, and the Q2 word-limit breach.

## Marks

| Criterion | Level | Points |
|---|---|---|
| C1 Q1 Quality attributes | Proficient | 4 / 6 |
| C2 Q2 Architectural style | Excellent | 6 / 6 |
| C3 Q3 Availability calculation | Proficient | 6 / 8 |
| C4 Q4 Resilience pattern | Excellent | 5 / 5 |
| C5 Q5 Consistency and availability | Proficient | 4 / 6 |
| C6 Q6 Architecture decision record | Proficient | 4 / 5 |
| C7 Communication and format | Proficient | 3 / 4 |

## Feedback by criterion

### C1 Q1 Quality attributes (4/6, Proficient)

Performance and availability are suitable choices and performance is justified from the lunch-peak data. The performance scenario is complete and measurable. The availability scenario has all six parts, but its response measure ('stay up most of the time') is not measurable, and the justification for availability as a top-two attribute is weaker than for performance.

### C2 Q2 Architectural style (6/6, Excellent)

Clear recommendation of a modular monolith. Two trade-offs are specific to the scenario (five-developer team vs operational overhead; known problems are deployment/VM issues rather than monolith issues) and the downside is acknowledged. Note that this answer exceeds the 150-word limit, which is addressed under Communication.

### C3 Q3 Availability calculation (6/8, Proficient)

Parts (a) and (b) are correct with working shown. Part (c) is incorrect: after improving payment availability to 99.9975%, you must still multiply by the other three components. The correct new availability is about 99.80%, giving about 1.5 hours downtime per 30-day month, not 0.018 hours.

### C4 Q4 Resilience pattern (5/5, Excellent)

Circuit Breaker is named and explained correctly (Closed/Open/Half-Open, failure threshold, fail-fast). It is applied well to the payment-provider outage, and tuning considerations (threshold, wait period) are given.

### C5 Q5 Consistency and availability (4/6, Proficient)

Both choices are reasonable and concrete techniques are named (cache with TTL for menu; idempotency key for payments). However, the CAP theorem explanation is incorrect: in a partition you cannot 'give up partition tolerance'; you choose consistency over availability (CP) for payments.

### C6 Q6 Architecture decision record (4/5, Proficient)

Context, Decision and Consequences are all present and specific to CampusEats. The consequences are one-sided: only positive consequences are listed, with no negative consequence as required for the excellent level.

### C7 Communication and format (3/4, Proficient)

Writing is clear, headings are used, and references are in IEEE style. However, Question 2 is about 180 words, exceeding the 150-word limit. One answer over the limit fits the 3-mark level.

## Next steps

1. Make every response measure measurable, e.g. 'availability is at least 99.9% during the lunch peak'.
2. In Q3(c), multiply the improved payment availability by the other three component availabilities to get the overall order-placement availability.
3. Correct the CAP explanation: during a partition, choose consistency or availability; partition tolerance is assumed, not given up.
4. Add at least one negative consequence to the ADR, e.g. eventual consistency or extra operational overhead for the queue.
5. Trim Question 2 to 150 words or fewer; keep all answers within the word limit.

---
<sub>Run Input_4-Run_2-Eff_low-261113-201552 | oneshot=deepseek/deepseek-v4.1-flash-1017 | tokens in/out 3297/6378 | cost $0.004156 | 41.16s</sub>
