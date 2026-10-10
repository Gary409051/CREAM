# Research Decision Log

Version 0.1 · initialized 2026-10-10. `Adopted scaffold` means a reversible organizational choice; `Proposed` means a scientific design awaiting audit/freeze; `Pending` requires an explicit owner decision. No entry below represents an empirical finding.

| ID | Date | Status | Decision and reason | Consequence / revisit trigger |
| --- | --- | --- | --- | --- |
| D001 | 2026-10-10 | Adopted scaffold | Use CREAM / Counterfactual Residual Expression Analysis and Mapping as the project identity | Match the existing manuscript; preserve its historical LECR filename |
| D002 | 2026-10-10 | Adopted scaffold | Keep three tracked original files at the root; create `papers/v1/` archive index and SHA-256 manifest | No original content, path, tracking or index changes; physical relocation can be a separate reviewed change |
| D003 | 2026-10-10 | Adopted scaffold | English research documents; preserve Chinese original; dependency-light `src/cream` interfaces | Collaborators can work on English protocols without rewriting provenance |
| D004 | 2026-10-10 | Adopted scaffold | Treat all protocols as drafts; separate evidence, hypotheses and results | Freeze/hash before final test access; no fabricated score tables |
| D005 | 2026-10-10 | Proposed | E1 precedes generator work; predicted references are primary and observed paired references secondary | Avoid attributing oracle calibration gains to an operational model |
| D006 | 2026-10-10 | Proposed | E1 primary recognition target excludes neutral; use independent neutral controls | Prevent neutral self-subtraction shortcut; modifies operational detail of the v1 sketch |
| D007 | 2026-10-10 | Proposed | Disclose E1-P neutral-only target adaptation; speaker/text crossed splits, normalization and wrong-reference controls | Do not call this strict no-target-data transfer; freeze actual coverage after audit |
| D008 | 2026-10-10 | Proposed | Practical directional effect gates and dependence-aware intervals; no significance-only acceptance | Numeric candidates require pilot/precision justification; ambiguous results remain inconclusive |
| D009 | 2026-10-10 | Pending | Code/paper/data/weights licensing not selected | `LICENSE_DECISION.md` replaces an invented LICENSE; no grant is made |
| D010 | 2026-10-10 | Pending | ESD is a candidate; official data access and research-use agreement need review | Corpus MIT repository marker is not accepted as audio rights; no download yet |
| D011 | 2026-10-10 | Pending | New recordings and voice rendering require appropriate consent and ethics review determination | No collection, recruitment or voice cloning in initialization |
| D012 | 2026-10-10 | Adopted scaffold | No automated experiment runner, dependency lock or ML model selected | Add those after the measurement pilot fixes requirements |
| D013 | 2026-10-10 | Adopted scaffold | Read-only remote confirmation; no staging, commit, branch change or push | Origin HEAD `main` and local HEAD matched `c917141b40ec893fdd05888a501d6445a0e3ee47` at initialization |

## Append a decision

Use a new stable ID, ISO date, status, question, considered alternatives, chosen action, rationale/evidence, owner role, affected files/protocols and revisit condition. Supersede an entry with a new entry rather than erasing history. Include before/after protocol hashes for frozen-study amendments and state whether outcomes were already observed. Do not record participant identities, credentials or confidential license correspondence here.

## Next decisions

Assign the investigator/data steward/reviewer; choose license scopes and initial corpus; resolve neutral-reference calibration policy; choose feature/aligner implementation and neutral predictor; justify effect thresholds, actual splits and sample sizes; decide independent replication and human-study review route. Link those records to [data management](DATA_MANAGEMENT.md), [ethics](ETHICS.md) and the [protocol](EXPERIMENT_PROTOCOLS.md).
