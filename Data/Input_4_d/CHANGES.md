# Input_4_d - what was changed (NOT sent to any model)

DEGRADED / poisoned ("_d") variant of `Input_4`. `Rubric_4.md`, `Task_4.md` are byte-identical copies of the originals; only the solution differs (`Solution_4_d.md`, derived from `Input_4/Solution_4.md`).

Five defects were injected into the original answer. The six original flaws (F1-F6 in `Input_4/NOTES.md`) are all still present.

**Basis for the edits:** Defects were chosen to cover the three kinds named in the README to-do (false claims, omitted requirements, calculation errors) and to be checkable from the task and rubric alone.

**Expected effect on marking:** Lower than the original (expected 27-31 of 40): Q3 should fall to Developing (two parts wrong), Q4 to Developing (mechanism incorrect), Q5 stays at or below Proficient (technique missing as well as CAP misuse), Communication loses for the missing reference. Roughly 20-25 of 40.

| ID | Type | Where | Change | Why / what a marker should notice |
|---|---|---|---|---|
| P1 | calculation error | Question 1, performance scenario stimulus | 'about 15 per minute' changed to 'about 150 per minute' | 900 orders in 60 minutes is 15 per minute, not 150 (factor-of-ten slip in the load the scenario is built on) |
| P2 | calculation error | Question 3(b) | Downtime product changed from 5.0 to 3.5 hours | 0.00699 x 720 = 5.03, not 3.5. Together with the original error in 3(c) two of three parts are now wrong (rubric Q3 Developing, 1-4) |
| P3 | false claim | Question 4, circuit breaker states | Closed and Open states swapped | In a circuit breaker Closed = calls pass through, Open = calls fail fast. The poisoned text says the opposite (Open passes calls, failures move it to Closed), so the mechanism is explained incorrectly |
| P3b | false claim (consistency of P3) | Question 4, Half-Open sentence and outage paragraph | Follow-on wording changed to match the swapped states | Keeps the swapped-state error internally consistent so it reads as a misconception rather than a typo |
| P4 | omitted requirement | Question 5(ii) | Idempotency-key sentence deleted | Task Q5: 'Name one concrete technique you would use in each case'. Case (ii) now names no technique |
| P5 | omitted requirement | References and Question 4 | Reference [2] removed from the reference list while the in-text citation [2] remains | Task: cite sources in IEEE style and list them at the end. [2] is now cited but not listed |

## Exact text changes

### P1 - Question 1, performance scenario stimulus

Original:

> 900 order requests arrive within one hour (about 15 per minute on average)

Changed to:

> 900 order requests arrive within one hour (about 150 per minute on average)

### P2 - Question 3(b)

Original:

> 0.00699 × 720 = 5.0 hours per month.

Changed to:

> 0.00699 × 720 = 3.5 hours per month.

### P3 - Question 4, circuit breaker states

Original:

> In the Closed state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open and calls fail immediately without waiting

Changed to:

> In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed and calls fail immediately without waiting

### P3b - Question 4, Half-Open sentence and outage paragraph

Original:

> If they succeed it closes again, otherwise it reopens. In the outage last month the breaker would have opened within seconds

Changed to:

> If they succeed it opens again, otherwise it stays closed. In the outage last month the breaker would have closed within seconds

### P4 - Question 5(ii)

Original:

> To be safe on retries, each order request carries an idempotency key so that a repeated request does not create a second charge.

Changed to:

> (deleted)

### P5 - References and Question 4

Original:

> [2] M. T. Nygard, *Release It! Design and Deploy Production-Ready Software*, 2nd ed. Raleigh, NC, USA: Pragmatic Bookshelf, 2018.

Changed to:

> (deleted)
