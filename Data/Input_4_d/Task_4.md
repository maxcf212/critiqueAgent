# SWEN3204 Software Architecture – Assignment 2: Short-Answer Questions

Term 2 Assignment (15% of course grade)

## Purpose

This assignment checks that you can apply the architecture concepts from Weeks 4–8 (quality attributes, architectural styles, availability, resilience patterns, data consistency and architecture decision records) to a concrete system. It is a short-answer assignment: we are looking for precise, well-justified answers, not essays.

## Scenario: CampusEats

CampusEats is a food pre-ordering platform used on one university campus. Students order and pay in a mobile app, and each food outlet receives its orders on a tablet in the kitchen.

- 12,000 registered students and 14 food outlets.
- On weekdays about 900 orders are placed between 12:00 and 13:00 (the lunch peak). Outside the peak the load is low.
- The system is a single monolithic web application with one PostgreSQL database, both running on one virtual machine. The development team has 5 developers.
- Placing an order is a synchronous request that passes through four components, all of which must be working: the API gateway, the order service code in the monolith, the database, and an external payment provider.
- Measured availability of each component: API gateway 99.95%, order service 99.9%, database 99.95%, payment provider 99.5%. Assume failures are independent.

Known problems:

1. During the lunch peak the 95th-percentile (p95) response time for placing an order is 4.2 seconds, and students abandon their orders.
2. Last month the payment provider became very slow for 25 minutes. Requests waiting on it used up all the request threads and the whole application, including menu browsing, stopped responding.
3. Every weekly deployment takes the system offline for about 20 minutes.
4. After an order is paid, the application calls the outlet's tablet directly and waits for the reply. If a tablet is offline the order is lost.

## Questions

Answer all six questions. The marks for each question are shown in brackets (40 marks in total, including 4 marks for communication).

**Question 1 – Quality attributes (6 marks).** Identify the two quality attributes that matter most for CampusEats and justify your choice from the scenario. For each one, write a quality attribute scenario in six-part form (source, stimulus, artefact, environment, response, response measure). Each response measure must be measurable.

**Question 2 – Architectural style (6 marks).** The CTO proposes rewriting CampusEats as microservices. Recommend an architectural style for the next 12 months (for example: keep the monolith, modular monolith, or microservices). Justify your recommendation with at least two trade-offs that are specific to this scenario.

**Question 3 – Availability calculation (8 marks).** Show your working.

- (a) Calculate the availability of placing an order.
- (b) Calculate the expected downtime of order placement in hours per 30-day month.
- (c) A second, independent payment provider with the same availability (99.5%) is added in an active-active configuration, so payment fails only if both providers are down. Calculate the new availability of placing an order and the new expected downtime per 30-day month.

**Question 4 – Resilience pattern (5 marks).** Name one architectural pattern that would have contained the failure described in known problem 2. Explain how it works and how it would have limited the outage. State at least one drawback or tuning consideration of the pattern.

**Question 5 – Consistency and availability (6 marks).** For each of (i) menu browsing and (ii) placing and paying for an order, state whether you would favour availability or consistency when a network partition occurs, and justify your choice with reference to the CAP theorem. Name one concrete technique you would use in each case.

**Question 6 – Architecture decision record (5 marks).** Write a short architecture decision record (ADR) for introducing a message queue between order payment and outlet notification (known problem 4). It must contain Context, Decision and Consequences, with at least one positive and at least one negative consequence.

## Format and submission requirements

- Answer under the headings "Question 1" to "Question 6", in order.
- Each answer must be at most 150 words. Calculations and working in Question 3 do not count towards the word limit.
- State any assumptions you make.
- Cite any external sources in IEEE style and list them at the end. References do not count towards the word limit.
- Give availabilities as percentages to two decimal places and downtimes in hours to one decimal place.
- Submit a single document through the course website. This is an individual assignment.
