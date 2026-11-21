# SWEN3204 Assignment 2 – Short-Answer Questions

## Question 1

The two most important quality attributes are performance and availability, because the business depends on the lunch hour: 900 orders arrive between 12:00 and 13:00 and the current p95 of 4.2 s for placing an order makes students abandon their orders. The scenarios below use the six-part form from [1].

Performance scenario. Source: students using the mobile app. Stimulus: 900 order requests arrive within one hour (about 150 per minute on average). Artefact: the order placement endpoint. Environment: a normal weekday lunch peak. Response: every order is accepted and confirmed. Response measure: the p95 response time is under 1.5 s and no requests are dropped.

Availability scenario. Source: the external payment provider. Stimulus: it becomes slow or stops responding. Artefact: the order service. Environment: the lunch peak. Response: the system keeps working and students can still browse menus. Response measure: the system should stay up most of the time.

## Question 2

I recommend against a full microservices rewrite for the next 12 months. Instead the existing application should be restructured into a modular monolith with clear internal modules (orders, menu, payments, outlets).

First, team size versus operational overhead. Microservices let each service scale and deploy independently, but every service needs its own pipeline, monitoring and on-call knowledge. With five developers, running eight or ten services would mean more time spent on infrastructure than on features. A modular monolith keeps one deployable unit and one database while still enforcing module boundaries.

Second, the known problems are not caused by the monolith itself. The slow lunchtime responses come from running on a single virtual machine, which can be fixed by running two or more instances of the monolith behind a load balancer. The 20-minute weekly downtime is a deployment process problem and can be removed with rolling deployments. A rewrite would freeze feature work for months without directly fixing either problem.

The trade-off I accept is that modules cannot be scaled independently, and a bug in one module can still crash the whole process.

## Question 3

(a) Placing an order needs all four components, so the availabilities multiply:

A = 0.9995 × 0.999 × 0.9995 × 0.995 = 0.99301

The availability of placing an order is 99.30%.

(b) A 30-day month has 30 × 24 = 720 hours.

Downtime = (1 − 0.99301) × 720 = 0.00699 × 720 = 3.5 hours per month.

(c) With two independent payment providers in active-active, payment only fails if both fail:

A_pay = 1 − (1 − 0.995)² = 1 − 0.000025 = 0.999975

So the new availability of placing an order is 99.9975%, which reduces the downtime to 0.000025 × 720 = 0.018 hours, or about one minute per month.

## Question 4

The Circuit Breaker pattern [2] would have contained the failure. Calls from the order service to the payment provider are wrapped in a breaker that counts failures and timeouts. In the Open state calls pass through normally. When failures exceed a threshold (for example 50% of calls in 10 seconds) the breaker moves to Closed and calls fail immediately without waiting, so request threads are not blocked and the rest of the application (menu browsing, order history) keeps responding. After a wait period the breaker goes Half-Open and lets a few trial calls through. If they succeed it opens again, otherwise it stays closed.

In the outage last month the breaker would have closed within seconds of the provider slowing down. Students would have seen "payment temporarily unavailable, please try again or pay at the counter" instead of the whole app hanging for 25 minutes.

## Question 5

(i) Menu browsing: I would favour availability. If a partition separates an application server from the database, it is better to show a slightly stale menu from a cache (for example Redis with a 60-second TTL) than an error page. The worst case is that a student sees an item that sold out a minute ago, which the outlet can handle by rejecting that order. This is eventual consistency.

(ii) Placing and paying for an order: I would favour consistency, because charging a student twice or accepting an order without a payment is unacceptable. The CAP theorem says a system can only provide two of consistency, availability and partition tolerance, so for payments we choose consistency and availability and give up partition tolerance.

## Question 6

**ADR-007: Use a message queue for outlet order notifications**

Status: Proposed

Context: After an order is paid, the application calls the outlet's tablet synchronously and waits for the reply. If a tablet is offline the order is lost, and during the lunch peak these calls add to the 4.2 s p95 response time.

Decision: Publish an "OrderPaid" event to a durable message queue (RabbitMQ). A notification worker consumes the events and pushes them to the outlet tablets, retrying until each one is acknowledged.

Consequences: Placing an order no longer waits for the outlet, so the response time improves. Outlets that are briefly offline still receive their orders when they reconnect. The queue also smooths the lunch peak because the workers process orders at a steady rate.

## References

[1] L. Bass, P. Clements, and R. Kazman, *Software Architecture in Practice*, 3rd ed. Upper Saddle River, NJ, USA: Addison-Wesley, 2012.
