# SWEN3204 Assignment 2 – Short-Answer Questions

## Question 1

Performance and availability matter most: 900 orders arrive in the lunch hour, the 4.2 s p95 makes students abandon their orders, and last month's payment slowdown took the whole application down. The scenarios use the six-part form from [1].

Performance scenario. Source: students using the mobile app. Stimulus: 900 order requests arrive within one hour (about 15 per minute on average). Artefact: the order placement endpoint. Environment: a normal weekday lunch peak. Response: every order is accepted and confirmed. Response measure: the p95 response time is under 1.5 s and no requests are dropped.

Availability scenario. Source: the external payment provider. Stimulus: it becomes slow or stops responding. Artefact: the order service. Environment: the lunch peak. Response: payment calls fail fast and browsing is unaffected. Response measure: menu p95 stays under 2 s, under 0.1% of non-payment requests fail, and ordering works again within 1 minute of the provider recovering.

## Question 2

I recommend a modular monolith (modules: orders, menu, payments, outlets) rather than a microservices rewrite for the next 12 months.

First, independent scaling versus operational overhead. Microservices let each service scale and deploy on its own, but each needs its own pipeline, monitoring and on-call knowledge. Five developers running eight or more services would spend more time on infrastructure than on features. A modular monolith keeps one deployable unit while enforcing module boundaries.

Second, rewrite cost versus fixing the known problems. The lunchtime slowness comes from a single virtual machine and is fixed by running several instances of the monolith behind a load balancer. The 20-minute weekly downtime is removed by rolling deployments. A rewrite would freeze feature work for months without directly fixing either.

The downside I accept is that modules cannot be scaled independently and a bug in one module can still crash the whole process.

## Question 3

(a) Placing an order needs all four components, so the availabilities multiply:

A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301

The availability of placing an order is 99.30%.

(b) A 30-day month has 30 × 24 = 720 hours.

Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 5.03, so 5.0 hours per month.

(c) With two independent payment providers in active-active, payment only fails if both fail:

A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975

The other three components are still in series with the payment pair:

A_new = 0.9995 × 0.999 × 0.9995 × 0.999975 = 0.99798

The new availability of placing an order is 99.80%.

Downtime = (1 − 0.99798) × 720 = 0.00202 × 720 = 1.46, so 1.5 hours per month.

## Question 4

The Circuit Breaker pattern [2] would have contained the failure. Calls to the payment provider are wrapped in a breaker that counts failures and timeouts. In the Closed state calls pass through. When failures exceed a threshold the breaker moves to Open and calls fail immediately, so request threads are not blocked and menu browsing keeps responding. After a wait it goes Half-Open and lets a few trial calls through; if they succeed it closes, otherwise it reopens.

Last month the breaker would have opened within seconds, and students would have seen "payment temporarily unavailable" instead of the app hanging for 25 minutes.

Tuning consideration: the threshold must come from real latency data. Too sensitive and it opens on a brief blip, rejecting payments that would have succeeded; too lax and threads are exhausted first. Drawback: nobody can pay while it is open, so a fallback is needed.

## Question 5

(i) Menu browsing: I would favour availability. If a partition separates an application server from the database, it is better to show a slightly stale menu from a cache (Redis with a 60-second TTL) than an error page. At worst a student sees an item that sold out a minute ago. This is the AP choice, with eventual consistency.

(ii) Placing and paying for an order: I would favour consistency, because charging a student twice or accepting an unpaid order is unacceptable. The CAP theorem says that during a partition a system must give up either consistency or availability; partitions cannot be ruled out in a distributed system, so partition tolerance is not optional. For payments I choose consistency (CP): the order is rejected with a clear error rather than risk an inconsistent charge. Each order request carries an idempotency key, so a retry does not create a second charge.

## Question 6

**ADR-007: Use a message queue for outlet order notifications**

Status: Proposed

Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply. If a tablet is offline the order is lost, and these calls add to the 4.2 s p95.

Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ). A notification worker consumes the events and pushes them to the outlet tablets, retrying until each one is acknowledged.

Consequences (positive): Placing an order no longer waits for the outlet, so the response time improves. Outlets that are briefly offline still receive their orders when they reconnect.

Consequences (negative): The queue is one more component for five developers to run and monitor. Delivery is at-least-once, so the tablet must ignore duplicate order IDs. The student is told "paid" before the outlet has seen the order, so a stuck queue needs an alert.

## References

[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed. Upper Saddle River, NJ, USA: Addison-Wesley, 2012.

[2] M. T. Nygard, *Release It! Design and Deploy Production-Ready Software*, 2nd ed. Raleigh, NC, USA: Pragmatic Bookshelf, 2018.
