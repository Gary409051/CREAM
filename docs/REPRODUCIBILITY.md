# Reproducibility

Version 0.1 · 2026-10-10 · scaffold checks are not scientific validation.

## Environment and dependencies

The scaffold imports using Python 3.9+ and the standard library. `pyproject.toml` describes a local package; it is not a frozen experimental environment. No audio/ML dependency, external model, hardware target or training toolchain has been selected. For a real study, choose a supported Python/runtime, exact packages and hashes, model checkpoint revisions and extractor/aligner versions, then commit a resolved environment/lock file after validating that environment. A dependency version must never be invented from memory as “latest”.

Capture operating system, CPU/GPU, driver/runtime versions, numerical libraries, thread counts, deterministic settings and known nondeterministic operations. Explain tolerance for rerun differences. Record compute, memory, time and failed jobs. Save local environment details privately if they contain usernames, hostnames or private paths; sanitize a public summary.

## Two levels of validation

Run from the repository root:

```sh
python3 scripts/validate_repository.py
PYTHONPATH=src python3 -c "import cream; print(cream.__version__)"
```

The first command checks required files/directories, non-ignored placeholders, relative Markdown links/heading anchors in newly authored Markdown, original-file SHA-256 checksums, and the explicit E1 draft state. Remote URLs and citation correctness require separate source review. The original manuscript is hash-checked but excluded from local link linting because it is a preserved historical artifact.

The second command is an import check. Neither fits a model, verifies a scientific mechanism, nor certifies the security of a release. Future [tests](../tests/README.md) should target leakage, masks, invalid measurements and real numerical/statistical behavior.

## Freeze checklist for an experiment

- Dated protocol/version, hypothesis IDs, primary comparison/endpoint, practical effect and harm margins, multiplicity/dependence analysis, sample size/power plan, exclusions and stopping.
- Source/target languages, actual corpus version/rights, recording hashes and private split/calibration manifests; allowed information for every comparator.
- Git commit and worktree-diff hash, resolved config/hash, package/runtime/hardware provenance, checkpoint hashes/training overlap.
- Feature/window/mask/alignment definitions; training-only normalization; reference model inputs, training and error/uncertainty policy.
- Complete seed list, training/tuning budget, output schema, blinded evaluation keys and planned analysis code.
- Reviewer approval that final test outcomes were not used for design. Choose an institutional/external registration service if required; a local Git record alone is not an independent timestamped public preregistration.

Store a sanitized frozen protocol/config in [preregistrations](../experiments/preregistrations/README.md). Sensitive data/keys remain in private storage. Changing a frozen study requires a new version, reason, timestamp, original hash and disclosure of test access. Link the amendment from [DECISIONS](DECISIONS.md).

## Run records and reporting

Use `experiments/runs/<experiment-id>/<run-id>/` locally; avoid participant names in IDs. At minimum record run ID/status, UTC start/end plus timezone where relevant, protocol/config hashes, commit/dirty-diff hash, environment/hardware, input/split hashes, checkpoint IDs, seed, predictions, metric definitions, exclusion/failure logs and resource usage. Mark runs `planned`, `running`, `completed`, `failed` or `incomplete`; never make a partial run appear successful.

A reviewed report under [reports](../experiments/reports/README.md) cites the exact runs, actual retained cluster counts, all registered primary/secondary outcomes and uncertainty, multiplicity handling, comparator fairness, deviations and failures. Put exploratory analyses in a separately labeled section. Preserve negative outcomes and confidence limits. Do not create numeric result tables from expected effects or simulated planning outputs.

## Reproduction and release gate

An independent reproduction must reconstruct permitted inputs, splits and preprocessing from versioned provenance, run matched conditions within registered tolerance and reproduce the reported inference. Evaluate whether a clean machine can obtain data lawfully; provide hashes and access instructions rather than redistribute restricted assets. Record which parts cannot be reproduced because of access, hardware or proprietary models.

Before release, check manifests, paths, logs, notebooks, figures, generated audio, checkpoints and Git history for private/rights-restricted material. `.gitignore` protects future untracked files only; it does not remove an already tracked asset or authorize publication. A reproducible aggregate result can be released while voice recordings remain private, if the terms permit.
