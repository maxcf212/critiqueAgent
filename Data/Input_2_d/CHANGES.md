# Input_2_d - what was changed (NOT sent to any model)

DEGRADED / poisoned ("_d") variant of `Input_2`. `Rubric_2.md`, `Task_2.md` are byte-identical copies of the originals; only the solution differs (`Solution_2_d.md`, derived from `Input_2/Solution_2.md`).

Five defects were injected into the original report (P3 is applied in two places). All of its original weaknesses are still present.

**Basis for the edits:** Defects cover an omitted requirement, false technical claims and calculation errors; each is checkable from the task sheet, the report's own tables or standard orbital mechanics.

**Expected effect on marking:** Lower than the original (mean 61/100): C1 loses for the missing users, C2 for the inclination, semi-major axis, latitude and contact-time errors.

| ID | Type | Where | Change | Why / what a marker should notice |
|---|---|---|---|---|
| P1 | omitted requirement | Introduction, last paragraph | The paragraph naming the users and funding (CSIRO, BOM, universities, government) deleted | Task Part 2 item 3: 'Who are the users (operator and customers)?'; rubric C1 lists it as required information. The report now names no users at all |
| P2 | false claim (contradiction) | Launch, Guiana Space Centre paragraph | Kourou latitude changed from 5.05 deg N to 45.05 deg N | Kourou is at about 5 deg N; the same sentence still says the site is 'situated very close to the equator', which 45 deg N is not |
| P3 | false claim (technical) | Orbit, inclination sentence | Sun-synchronous inclination changed from 97.7924 deg to 87.7924 deg | A sun-synchronous orbit must be retrograde (inclination above 90 deg; about 97.8 deg at 600 km). The report still calls the orbit retrograde |
| P3b | false claim (consistency of P3) | Orbit, orbital elements table | Inclination in the table changed from 97.79 deg to 87.79 deg | Keeps the wrong inclination consistent between text and table so it reads as a real error, not a typo |
| P4 | calculation error | Orbit, orbital elements table | Semi-major axis changed from 6971 km to 7171 km | The description in the same row still says 'Earth radius of 6371km plus a proposed altitude of 600km', which is 6971 km |
| P5 | calculation error | Ground Control & Communications, after the access table | 'average contact duration of almost ten minutes' changed to 'almost twenty minutes' | The table directly above gives a mean duration of 580.786 s, which is 9.7 minutes; no single access exceeds 13 minutes |

## Exact text changes

### P1 - Introduction, last paragraph

Original:

> The proposed satellite would likely be used by governmental and science agencies (e.g. CSIRO, BOM) for research and/or education. Funding would likely be subsidised by either an Australian University or the Australian Government, since monitoring and protecting the state of the Great Barrier Reef and surrounding marine environments can be deemed a public service.

Changed to:

> (deleted)

### P2 - Launch, Guiana Space Centre paragraph

Original:

> with a latitude of $ 5.05^{\circ} $N

Changed to:

> with a latitude of $ 45.05^{\circ} $N

### P3 - Orbit, inclination sentence

Original:

> requires a mean inclination of $ 97.7924^{\circ} $

Changed to:

> requires a mean inclination of $ 87.7924^{\circ} $

### P3b - Orbit, orbital elements table

Original:

> >97.79°</td>

Changed to:

> >87.79°</td>

### P4 - Orbit, orbital elements table

Original:

> >6971km</td>

Changed to:

> >7171km</td>

### P5 - Ground Control & Communications, after the access table

Original:

> An average contact duration of almost ten minutes was achieved

Changed to:

> An average contact duration of almost twenty minutes was achieved
