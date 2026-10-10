# Test Plan

This directory is a test scaffold; there are no implemented algorithm tests or claimed scientific coverage. The repository integrity checker lives in [scripts](../scripts/README.md).

Use `unit/` for local behavior, `integration/` for pipeline contracts and `fixtures/` for small clearly synthetic non-identifying inputs only. No licensed audio or real participant data in fixtures.

When implementing the relevant module, prioritize:

- Invalid/unvoiced F0 masks, zero-duration/log-domain errors and mismatched grids; missing is distinct from observed zero.
- Train/development/test speaker/text/session/pair separation, duplicate exclusion and prohibited target-label fitting.
- Training-only scale fitting and reproducible reference alignment; predictor inputs must not contain query expression.
- Incorrect pair IDs, path traversal, duplicate manifests and checksum mismatches.
- Metric class coverage, paired crossed-cluster sampling, all-seed reporting and refusal of draft experiment configs.
- Synthetic known-effect/null checks of statistical code, distinguished from empirical results.

Choose a test toolchain with the first implementation, then document executable commands and results. Do not test an empty stub simply to claim coverage.
