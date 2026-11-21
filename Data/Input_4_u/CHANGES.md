# Input_4_u - what was changed (NOT sent to any model)

UPGRADED ("_u") variant of `Input_4`. `Rubric_4.md`, `Task_4.md` are byte-identical copies of the originals; only the solution differs (`Solution_4_u.md`, derived from `Input_4/Solution_4.md`).

All six flaws that were deliberately written into the original answer (F1-F6 in `Input_4/NOTES.md`) are fixed. Nothing else is changed.

**Basis for the edits:** Input_4 is synthetic, so the 'marking' used here is the list of planted flaws in `Input_4/NOTES.md` (no pipeline run of Input_4 existed when this was made). Re-check against a real marking run of Input_4 once one exists.

**Expected effect on marking:** Every criterion should reach its top level: about 37-40 of 40 (original expected 27-31).

| ID | Type | Where | Change | Why / what a marker should notice |
|---|---|---|---|---|
| U1 | fix F1 (unmeasurable response measure) | Question 1, availability scenario | Response and response measure rewritten with numbers | Rubric Q1 Excellent needs both response measures measurable; the task says each must be measurable |
| U1b | word limit (follows from U1) | Question 1, opening sentences | Justification tightened (and the payment outage added as the reason for availability) so the answer stays within 150 words | Task: each answer at most 150 words |
| U2 | fix F2 (word limit) | Question 2 | Answer tightened from 181 words to under 150; same recommendation, same two trade-offs, downside kept | Task: each answer at most 150 words; rubric Communication and format |
| U3 | fix F3 (calculation) | Question 3(b) and 3(c) | (c) now multiplies the payment pair by the other three components: 99.80% and 1.5 h (was 99.9975% and 0.018 h); (b) shows 5.03 before rounding | Answer key: 0.9995 x 0.999 x 0.9995 x 0.999975 = 0.997976; rubric Q3 Excellent needs all three parts correct |
| U4 | fix F4 (missing drawback / tuning consideration) | Question 4 | A tuning consideration and a drawback added; the rest shortened to stay within 150 words (mechanism unchanged) | Task Q4 requires at least one drawback or tuning consideration; rubric Q4 Excellent |
| U5 | fix F5 (CAP theorem misuse) | Question 5 | CAP corrected in (ii): partition tolerance cannot be given up, so payments choose consistency over availability (CP); (i) labelled AP and shortened | Rubric Q5 Excellent needs the CAP theorem used correctly |
| U6 | fix F6 (one-sided ADR) | Question 6 | Consequences split into positive and negative, three negative consequences added; context sentence shortened | Task Q6 requires at least one positive and one negative consequence; rubric Q6 Excellent |

## Exact text changes

### U1 - Question 1, availability scenario

Original:

> Response: the system keeps working and students can still browse menus. Response measure: the system should stay up most of the time.

Changed to:

> Response: payment calls fail fast and browsing is unaffected. Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering.

### U1b - Question 1, opening sentences

Original:

> The two most important quality attributes are performance and availability, because the business depends on the lunch hour: 900 orders arrive between 12:00 and 13:00 and the current p95 of 4.2 s for placing an order makes students abandon their orders. The scenarios below use the six-part form from [1].

Changed to:

> Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders, and last month's payment slowdown took the whole application down. The scenarios use the six-part form from [1].

### U2 - Question 2

Original:

> I recommend against a full microservices rewrite for the next 12 months. Instead the existing application should be restructured into a modular monolith with clear internal modules (orders, menu, payments, outlets). First, team size versus operational overhead. Microservices let each service scale and deploy independently, but every service needs its own pipeline, monitoring an [...] still crash the whole process.

Changed to:

> I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months. First, independent scaling versus operational overhead. Microservices let each service scale and deploy on its own, but each needs its own pipeline, monitoring and on-call knowledge. Five developers running eight or more services would spend more [...] still crash the whole process.

### U3 - Question 3(b) and 3(c)

Original:

> Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.0 hours per month. (c) With two independent payment providers in active-active, payment only fails if both fail: A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975 So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours, or about one minute per month.

Changed to:

> Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month. (c) With two independent payment providers in active-active, payment only fails if both fail: A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975 The other three components are still in series with the payment pair: A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798 The new availability of placing a [...]  1.46, so 1.5 hours per month.

### U4 - Question 4

Original:

> The Circuit Breaker pattern [2] would have contained the failure. Calls from the order service to the payment provider are wrapped in a breaker that counts failures and timeouts. In the Closed state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Open and calls fail immediately without waiting, so reque [...] le app hanging for 25 minutes.

Changed to:

> The Circuit Breaker pattern [2] would have contained the failure. Calls to the payment provider are wrapped in a breaker that counts failures and timeouts. In the Closed state calls pass through. When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked and menu browsing keeps responding. After a wait it goes Half- [...] open, so a fallback is needed.

### U5 - Question 5

Original:

> (i) Menu browsing: I would favour availability. If a partition separates an application server from the database, it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL) than an error page. The worst case is that a student sees an item that sold out a minute ago, which the outlet can handle by rejecting that order. This is eventual consi [...] es not create a second charge.

Changed to:

> (i) Menu browsing: I would favour availability. If a partition separates an application server from the database, it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page. At worst a student sees an item that sold out a minute ago. This is the AP choice, with eventual consistency. (ii) Placing and paying for an order: I would favou [...] es not create a second charge.

### U6 - Question 6

Original:

> **ADR-007: Use a message queue for outlet order notifications** Status: Proposed Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply. If a tablet is offline the order is lost, and during the lunch peak these calls add to the 4.2 s p95 response time. Decision: Publish an "OrderPaid" event to a durable message queue (Ra [...] ocess orders at a steady rate.

Changed to:

> **ADR-007: Use a message queue for outlet order notifications** Status: Proposed Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply. If a tablet is offline the order is lost, and these calls add to the 4.2 s p95. Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ). A notification worker consu [...]  a stuck queue needs an alert.
