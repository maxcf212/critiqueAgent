# Input_4 – dataset notes (NOT sent to any model; the pipeline only reads Rubric*.md, Task*.md, Solution\*.md)

Synthetic dataset written for this project: software architecture focus, short-answer format.
Course, scenario ("CampusEats") and student are fictional. The rubric deliberately differs in shape from Inputs 1-3:
a markdown pipe table, marks per criterion (6/6/8/5/6/5/4 = 40) instead of percentage weights, and a different mark
range per level for each criterion.

## Answers for Q3 calculations are

- (a) 0.9995 x 0.999 x 0.9995 x 0.995 = 0.993011 -> 99.30%
- (b) (1 - 0.993011) x 720 h = 5.03 h -> 5.0 hours per 30-day month
- (c) payment pair = 1 - 0.005^2 = 0.999975; order placement = 0.9995 x 0.999 x 0.9995 x 0.999975 = 0.997976 -> 99.80%;
  downtime = 0.002024 x 720 h = 1.46 h -> 1.5 hours per 30-day month

## Flaws deliberately written into Solution_4.md (a good marker should find these)

| #   | Where          | Flaw                                                                                                                                                                                                                         | Rubric effect                                        |
| --- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| F1  | Question 1     | Availability scenario's response measure is not measurable ("should stay up most of the time")                                                                                                                               | Q1 Proficient (3-4 of 6)                             |
| F2  | Question 2     | Answer is 181 words, over the 150-word limit                                                                                                                                                                                 | Communication and format: Proficient (3 of 4)        |
| F3  | Question 3(c)  | Parallel payment availability is computed correctly (0.999975) but is then reported as the availability of order placement, without multiplying by the other three components (99.9975% / 0.018 h instead of 99.80% / 1.5 h) | Q3 Proficient (5-6 of 8): exactly one part incorrect |
| F4  | Question 4     | No drawback or tuning consideration of the circuit breaker is given (explicitly required by the task)                                                                                                                        | Q4 Proficient (3-4 of 5)                             |
| F5  | Question 5(ii) | CAP theorem misused: claims payments "choose consistency and availability and give up partition tolerance" (a distributed system cannot give up P; favouring consistency means giving up availability during a partition)    | Q5 Proficient (3-4 of 6)                             |
| F6  | Question 6     | ADR lists only positive consequences (at least one negative is explicitly required)                                                                                                                                          | Q6 Proficient (3-4 of 5)                             |

Everything else is intended to be correct: Q1 performance scenario, Q2 recommendation and trade-offs (Excellent, 5-6),
Q3 (a) and (b), circuit breaker mechanism, Q5(i), idempotency key, ADR context/decision, IEEE references.

## Expected mark

Roughly 27-31 of 40 (68-78%): Q1 4, Q2 5-6, Q3 5-6, Q4 3-4, Q5 3-4, Q6 3-4, Communication 3.
