# Input_3_u - what was changed (NOT sent to any model)

UPGRADED ("_u") variant of `Input_3`. `Rubric_3.md`, `Task.md` are byte-identical copies of the originals; only the solution differs (`Solution_3_u.md`, derived from `Input_3/Solution_3.md`).

The report was rewritten to address every reason for lost marks. The student's position (do not ship on the current basis) and section structure are kept; the evidence, the analysis of how to decide, the recommendations and the references are new. All external facts and references in the new text are real and were written from the author's knowledge of these well-documented cases, but they were not re-checked against the sources online: verify them before quoting this dataset as an example of correct referencing.

**Basis for the edits:** consolidated marking of Input_3 from 21 CritiqueAgentv3 gradings (17 runs in `runs/compare_20261113-071712_Input_3`, 2 in `runs/Compared-Input_3-Runs_2-Eff_low-261113-152625`, 2 reference runs). Original marks: mean 76/100, range 68-88; per criterion C1 18.3, C2 16.2, C3 16.6, C4 14.3, C5 10.9 of 20. The 'Why' column gives how many of the 21 runs raised each point.

**Expected effect on marking:** All five criteria should reach Excellent or Very good (roughly 90-100%).

| ID | Type | Where | Change | Why / what a marker should notice |
|---|---|---|---|---|
| U1 | C1 Introduction | Introduction | Three distinct ethical issues named and tied to the QA/design process; stakeholder table (Table 1) gives each stakeholder's interest and the decision they control; chip supplier and international customers given a role | ~7 runs: stakeholders only named, interests not developed; ~3: intro thin / generic link to engineering design |
| U2 | C2 Balanced Discussion | Arguments for shipping | For-side given its strongest form with a source [2], then answered point by point; consumer-electronics (Apple/CNBC) analogy removed | ~11 runs: CNBC source does not support the Apple claim; ~6: for-side thin, speculative, not rebutted |
| U3 | C4 Research and Evidence | Arguments against shipping | Quantitative evidence added from primary and peer-reviewed sources (NAO on WannaCry: 81 of 236 trusts, 19,000 appointments; Therac-25: six overdoses; Intel: US$475 million; Volkswagen: 11 million vehicles, US$4.3 billion). Limits of each analogy stated. BBC news item replaced by the NAO report | ~13 runs: no quantitative evidence; ~8: only four secondary news sources; 6: NHS analogy overstated ('almost identical', 'led to deaths'); 1: Volkswagen is deliberate fraud |
| U4 | task requirement (how to decide; trade-offs) | New section 'How should Rachel decide when to ship?' | Explicit decision rule (Figure 1) based on severity, likelihood, context of use and informed acceptance; Rachel's physical-harm versus data-loss threshold analysed; options A-D compared in Table 2 | ~15 runs: no explicit ship/no-ship rule and Rachel's own threshold not analysed; 3: alternatives to refusal not compared; requirement R8 partial/no in 13 of 20 runs |
| U5 | C2/C3 stakeholders | Conclusion and Recommendations | One recommendation per stakeholder (Rachel, management, health department, chip supplier, product engineers). Rachel withholds sign-off and escalates instead of 'refusing the contract'; contradictory recommendation 3 rewritten; overstatement ('life and death', 'colossal') removed | ~20 runs: recommendations only for Rachel and her company; 4: refusing the contract is beyond a QA engineer's authority; 4: recommendation 3 internally inconsistent |
| U6 | C5 visual elements | Whole report | Two tables and one figure added, each numbered, titled and referred to in the text | 21 of 21 runs: no figures or tables at all |
| U7 | C5 language | Whole report | Typos and broken sentences fixed ('DICUSSION', 'ofprofessional', 'The economic benefits of could', 'have her company might go under'); 'EACE' and garbled clause numbers removed, Code principles quoted by name | ~18 runs: language errors; 4: wrong abbreviation and garbled clause numbering; 3: clause 2.3b misapplied |
| U8 | C5 references | References | Eight complete IEEE-style references (was four incomplete ones); every reference is cited and every citation is listed | ~18 runs: reference entries incomplete or inconsistent (missing URL/author, corrupted URL, garbled authors) |
| U9 | format | Abstract and length | Abstract about 150 words; introduction + body + conclusion + recommendations under 1,500 words (tables, captions and references excluded) | Task format requirements; 1 run queried the word count |

## Exact text changes

The solution was rewritten throughout, so there is no short list of replaced passages. Compare `Input_3/Solution_3.md` with `Solution_3_u.md` in a diff tool to see every change.
