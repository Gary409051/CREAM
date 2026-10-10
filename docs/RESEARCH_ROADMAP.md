# Research Roadmap

Version 0.1 · 2026-10-10 · planning document · owner: project maintainer (role; not an assigned investigator).

## Aim and scope

Test a conditional residual mechanism for vocal expression, then test multiscale temporal modeling and cross-lingual expression rendering. Begin with English and Mandarin as candidate languages, including lexical-tone failure cases. Generalization beyond these languages requires new evidence. Classification is a diagnostic, not the final perceptual objective. No claim of unique latent emotion factors or causal identification from observational data is assumed.

The preserved [manuscript](../LECR_Research_Manuscript_v1.md) provides the conceptual starting point. The [protocol](EXPERIMENT_PROTOCOLS.md) supplies current operational definitions. Differences from the manuscript are deliberate design refinements, recorded in [DECISIONS](DECISIONS.md); the original is not rewritten.

## Stages and gates

| Stage | Work and deliverables | Exit gate | Current state |
| --- | --- | --- | --- |
| S0: scientific and access audit | Evidence matrix; rights register; corpus inventory; compute budget; roles; draft preregistration | Dataset/model terms and permitted uses documented; actual speaker/text/pair coverage audited; key prior work read; license and ethics decisions assigned | Draft documents only; access unresolved |
| S1: measurement pilot | Feature/mask specification, aligner audit, repeated-neutral checks where available, leakage-free split manifest, baseline calibration report | Candidate QC thresholds justified on development-only data; independent query/reference pairs; baseline error and missingness quantified | Not started |
| S2: E1 residual validation | Matched raw/normalized/residual comparisons; oracle vs predicted-reference separation; negative controls; uncertainty and failure report | Freeze E1 before test access. Predicted residuals meet the registered transfer criterion, or revise/reject the mechanism based on a documented result | Not started |
| S3: E2 temporal structure | Matched-budget scale and coupling ablations; distribution-preserving temporal perturbations | Registered incremental benefit with robustness to capacity and perturbation artifacts; otherwise simplify representation | Not started |
| S4: E3 reconstruction | Authorized controllable renderer; bilingual event annotations; blinded listening study; intelligibility and naturalness audit | Expression superiority plus every registered non-inferiority constraint; both directions reported | Not started |
| S5: E4 replication and publication | Independent corpus/speakers, compact-feature analysis, error taxonomy, reproducible paper revision | Claim scope matches replicated evidence; release rights reviewed; negative findings included | Not started |

Gates are scientific decisions, not calendar deadlines. No training or data collection is authorized by this document. Separate budgets for corpus access, annotation, listening participants, compute and replication must be estimated before committing a schedule.

## First executable research milestone

E1 should run without a speech generator. Use a licensed corpus with verified same-language neutral/expressive text pairs. Audit whether text content, speaker and recording conditions can be separated; do not assume a filename encodes a translation pair. Establish raw and simple normalization baselines first. Freeze a predicted-neutral baseline using development data, then compare expression transfer on held-out non-neutral speech. If only a paired-reference advantage exists, the deliverable is a reference-availability limitation, not an operational success.

The minimum E1 report includes corpus/version/rights, exact split hashes, pair availability, excluded material, baseline prediction errors, masked channel coverage, primary directional effects and intervals, normalization and shuffled-reference controls, language/speaker probes, all seeds and failures. It must state that acted category transfer is only a proxy for expression preservation.

## Risk register

| Risk | Diagnostic | Response |
| --- | --- | --- |
| “Neutral” varies with recording, speaker or discourse | Repeated-neutral variance and reference-condition sensitivity | Restrict the claim; collect authorized repeats or compare alternative references |
| Subtraction amplifies baseline error | Oracle/predicted gap; error versus transfer-effect plot | Improve estimation or abandon subtraction; propagate uncertainty |
| Classifier exploits neutral self-subtraction | Exclude neutral class from E1's primary target; audit independent repeats | Use non-neutral transfer and separate neutral controls |
| Language and speaker are confounded | Speaker-disjoint evaluation; balanced diagnostic probes | Report confounding; add bilingual/independent data rather than assert invariance |
| Corpus labels encode acted stereotypes | Listener annotation and second-corpus replication | Limit conclusions to acted styles until replicated |
| Tone or semantic focus is removed | Mandarin tone/focus strata and intelligibility audit | Retain necessary linguistic information and impose target-language constraints |
| Generator cannot execute valid representations | Control-bandwidth and within-language render/reanalysis audit | Separate representation and rendering failures; change renderer |
| Low speaker count or access delay | Cluster-aware precision/power analysis | Report inconclusive evidence; reduce scope or acquire approved independent data |
| Unresolved release rights | Rights register and participant consent audit | Restrict release to permitted metadata/code or postpone release |

## Decisions needed before S1/S2

- Project license scopes: code, authored documentation/papers, weights and data.
- Initial dataset and its completed access process; ESD is a candidate, not an approved acquisition.
- Languages/dialects, expression dimensions, neutral-reference operating regime and acceptable calibration information.
- Primary practical effect, precision/power target, speaker/text sample size and compute budget.
- Responsible investigator, data steward, analysis reviewer and ethics review route, where required.

These decisions do not prevent building this scaffold. Their resolution must be documented before dependent experiments begin.
