# Contributing to CREAM

This is a research scaffold. Read the [hypotheses](docs/RESEARCH_QUESTIONS_AND_HYPOTHESES.md), [protocols](docs/EXPERIMENT_PROTOCOLS.md) and [license decision](LICENSE_DECISION.md) before contributing. Contribution permissions and outbound licensing remain unresolved; no contributor license agreement or automatic rights assignment is implied.

## Workflow

1. Describe the research question/problem, evidence and expected deliverable in an issue or local decision proposal. Existing project instructions and permissions take precedence.
2. Work in a small focused branch when a branch is appropriate; preserve existing user changes. Do not rewrite the original v1 paper files. Record scientific design changes in the decision log and amend frozen protocols explicitly.
3. Keep data acquisition separate from implementation. Commit code, safe configuration, schemas and reviewed reports; keep real audio, private manifests, consent forms, weights and local runs outside Git according to the data policy.
4. Validate relative links and scaffold integrity with `python3 scripts/validate_repository.py`. For implemented behavior, add proportionate tests for meaningful contracts and numerical edge cases; do not claim test coverage for unimplemented interfaces.
5. Request review with the concrete change, rationale, validation, hypothesis/protocol impact, dependency/rights implications and limitations. Separate confirmatory and exploratory findings. Do not publish, push, merge or upload assets unless the task scope authorizes it.

## Code and research standards

Use the `src/cream/` boundaries, typed inputs with explicit units/masks and stable recording IDs, and small functions that separate measurement, reference estimation, representation and evaluation. No implicit test-set fitting, network download or expensive training on import. Raise an explicit error for unavailable methods instead of returning fake features or scores. Avoid adding a dependency before the relevant measurement/implementation need is established.

For experiments record dataset/model versions and rights, exact splits/calibration, config and environment hashes, seeds, budgets, all attempted runs and effect uncertainty. Any simulated data must be labeled synthetic and excluded from empirical result claims. Do not convert planned sample counts or desired effect sizes into reported findings.

Cite accessible primary sources and record what they actually support. Source verification and independent replication are different. Preserve failed retrieval and unresolved references in the literature register. Respect voice consent, contributor attribution and coauthor decisions; a code contribution does not automatically determine academic authorship.

## Original files

The [v1 index](papers/v1/README.md) records unchanged originals at their existing paths. New manuscript versions belong in a new version directory with provenance and an explicit relationship to v1. Do not replace historical originals as part of routine code/documentation changes.
