# Configurations

[e1_residual_validation.draft.json](e1_residual_validation.draft.json) mirrors the current [E1 protocol](../docs/EXPERIMENT_PROTOCOLS.md). It is readable using Python's standard library and deliberately cannot be treated as a finalized experiment: `frozen` is false; data, model, environment, sample size/power and QC freeze are unresolved.

Seeds, split proportions, effect thresholds and confidence settings are candidate design values. They are not observations or owner-approved final thresholds. Keep the written protocol and configuration synchronized; record changes in [DECISIONS](../docs/DECISIONS.md). Future runners must refuse drafts or missing required fields and save a resolved configuration/hash with each run. No runner is supplied yet.

Before freezing, replace unresolved values with actual approved data/version/rights and split hashes, predictor/extractor/aligner/classifier identities, dependency lock, justified thresholds/cluster counts and a reviewed analysis specification. Copy the resolved version to the preregistration directory; do not overwrite frozen configurations. Credentials and machine-specific private paths belong outside Git.
