# Experiment Protocols

Version 0.1 · 2026-10-10 · **DRAFT / NOT PREREGISTERED / NOT EXECUTED**.

This is a preregistration-style design, not evidence or permission to acquire data. All numeric design values below are **candidates**, not measured results, accepted scientific standards or frozen commitments. The [E1 configuration](../configs/e1_residual_validation.draft.json) intentionally has `frozen: false` and unresolved data/sample-size fields. Freeze a dated, immutable protocol and configuration under [preregistrations](../experiments/preregistrations/README.md) after a development-only pilot and before accessing final test outcomes.

## Rules shared by all experiments

1. Record data/version/rights, permissible training and release, study owner, protocol hash, Git commit, environment, splits, random seeds, budget and exclusions. No test-based feature, baseline or hyperparameter choice.
2. Partition speakers, normalized text/semantic groups, sessions and duplicate recordings before deriving features or references. A neutral/expressive pair and all its variants inherit the query's partition. Keep a neutral support/calibration partition explicit if the operating regime permits it.
3. Fit normalization, missingness policies, feature selection, baseline prediction and annotation-lag correction using permitted training/development data only. Test labels are held by an evaluator until freeze.
4. Match data access, feature extraction, alignment, downstream models and tuning budgets across causal comparisons. Report parameter count, training budget and calibration information. External systems with different resources are contextual references.
5. Declare one primary endpoint per experiment and the family of directional/secondary comparisons. Report effects and intervals; control multiplicity and cluster dependence. Frames, utterances from the same speaker and repeated listener judgments are not independent subjects.
6. Preserve unsuccessful runs and missingness; no selective seed reporting or optional stopping. Amendments after freeze are dated deviations; analysis affected by test inspection is exploratory.

## E1 — Expressive Residual Validation

### Purpose and scope

Test whether subtracting a **predicted** conditioned neutral reference provides transferable information beyond raw or simply normalized acoustic features. No generator is needed. E1 isolates the measurement/reference part of H1; it does not establish perceptual cross-lingual expression equivalence.

Candidate corpus: licensed ESD, subject to a physical inventory, pairing and term audit. English and Mandarin recordings are language groups, not assumed bilingual speakers or translated sentence pairs. ESD's non-neutral categories (happy, angry, sad, surprise) supply a restricted acted-style diagnostic. Do not fabricate continuous valence/arousal labels from these categories. Optional continuous prediction requires a separate licensed corpus with real continuous annotations and a separate endpoint registration.

**Primary target excludes neutral.** If an expressive query is subtracted from its own observed neutral-class recording, neutral can become identically zero. Including that class would create a trivial recognition cue. Neutral material is used for reference fitting and independent-reference controls instead.

### E1.1 Corpus audit and split plan

Inventory unique speakers, languages/dialects, texts, repetitions, expression labels, sessions, microphones, sample rates and missing pairs. Validate same-speaker/same-language/same-text neutral matches by transcript and recording ID; verify at least a development subset manually. Hash recordings to identify duplicates. Check whether emotion conditions are segregated by session or loudness; such segregation limits attribution.

Candidate speaker and text group proportions are 60/20/20 for training/development/test **within each language**, subject to audited availability and power. Construct crossed partitions: training uses training speakers × training text groups; development uses development speakers × development texts; test uses test speakers × test texts. Quarantine off-diagonal combinations rather than silently reusing their speakers/texts. All styles, neutral partners and duplicate/near-duplicate text variants remain in the same assigned groups. Publish actual retained/discarded counts and split rules. These proportions are not a substitute for speaker-level precision analysis.

For English→Mandarin, fit the expression classifier on English training labels, tune on English development labels, and evaluate only Mandarin test speakers/texts. Reverse the procedure for Mandarin→English. Neither target expressive labels nor target test performance may select hyperparameters. Both directions and their primary comparison form a registered family. Within-language held-out performance is secondary.

Separate these reference regimes:

- **E1-P (primary, predicted reference with neutral-only target adaptation):** reference predictor may use source training neutral data and target-language *training-partition* neutral data; target development neutral data may tune reference prediction/QC. No target expressive labels are used. No neutral support from target test speakers/texts is allowed. The baseline must therefore support unseen speakers without fitting speaker-specific parameters on evaluation recordings; use a speaker-agnostic reference initially, or preregister a fixed independently trained speaker encoder. Every raw/normalized comparator has the same permitted neutral calibration information. This is not a strict no-target-data zero-shot experiment.
- **E1-O (secondary, paired-reference oracle):** obtain the held-out query's same-speaker/same-text observed neutral partner solely to construct that reference. No label-dependent pairing or test-trained scale is allowed. This intentionally gives stronger reference access. Report its advantage as a diagnostic bound on baseline estimation, not as deployable evidence. The gap to E1-P can reflect both reference quality and extra calibration information.
- **E1-Z (optional, strict no-target-data transfer):** only if a language-conditioned reference can be specified without target-corpus calibration. Register separately; do not relabel E1-P as E1-Z.

No baseline model, pretrained corpus or encoder is selected yet. Its training data and overlap must be audited. If actual corpus coverage cannot sustain crossed splits, revise the design before test access, choose an independent corpus or report the limitation; do not reduce separation after viewing results.

### E1.2 Measurement and reference specification

Begin with log F0 (voiced regions), log energy with consistent recording gain handling, phone/syllable duration log ratios, and a small justified voice-quality set. Define sample-rate handling, frame/hop sizes, aligner version, supported languages, valid F0 range, octave-error policy, minimum voiced coverage, silence handling and voice-quality validity on development data. Do not fill unvoiced F0 with a physical zero. Event pauses remain event variables.

Predict the neutral trajectory from text/phonology/language and any registered speaker conditioning; do not feed the query's expressive trajectory into the neutral predictor. Align query and reference on frozen phonetic/event coordinates; apply equivalent resampling/masks to raw comparators. Query-derived alignments are permitted measurements, not label supervision, and their failure rate must be reported.

Use training-neutral variability floors to standardize continuous deviations and log ratios for durations. Record per-channel prediction MAE/RMSE, bias and calibration coverage on held-out neutral development material, broken down by language, speaker and tone/focus context. With only one neutral take per text, independent same-text neutral residual variance is unidentifiable; do not manufacture it by subtracting a recording from itself. Acquire authorized repeats or disclose the missing diagnostic.

**Development QC candidates:** manually audited pair/alignment acceptance ≥95%; median valid voiced-F0 coverage ≥80% of audited voiced time; report all failed observations. Coverage denominator and audit sampling must be frozen. These values require pilot justification. Final exclusions apply identically across matched comparisons and use signal/metadata criteria rather than label/model performance; report common-subset and failure-inclusive sensitivity analyses.

### E1.3 Matched conditions and controls

| ID | Representation | Role |
| --- | --- | --- |
| R0 | Raw acoustic features after required log/unit transforms; common classifier scaler | Primary comparator |
| R1 | Global channel normalization and permitted neutral-only population/speaker calibration; no content-conditioned reference subtraction | Test whether ordinary normalization explains gains |
| R2-P | Predicted conditioned neutral residual, no multiscale/coupling component | Primary residual candidate |
| R2-O | Paired-reference residual | Reference-access diagnostic; secondary |
| N1 | Wrong-text reference, matched language and available speaker regime, permuted without expression labels | Test content conditioning; repeat registered permutations |
| N2 | Training expression labels shuffled within registered language/speaker strata | Pipeline/leakage negative control; evaluation labels unchanged |
| N3 | Independent neutral vs independent neutral residual, where repeats exist | Estimate false expression signal and neutral variability |

Use identical event/window functionals, valid masks, feature dimensionality, classifier architecture and search budget for R0/R1/R2-P. Start with a low-capacity linear classifier; explicitly register regularization search and folds. A higher-capacity follow-up is exploratory until separately frozen. Do not add wavelets to only R2-P in E1. Use the same classifier scaler policy, fitted on source training observations per condition. Make missingness-only classification a secondary confound check.

Neutral-only target calibration is available equally to comparators; R1 may use that same training neutral pool. A predicted residual gain over R0 alone is insufficient to distinguish conditioned subtraction from simple normalization. Preregister R2-P versus R1 as a secondary corroboration needed for a mechanism-specific conclusion.

### E1.4 Endpoints and inference

**Primary endpoint:** target-language macro unweighted average recall (UAR) on the four non-neutral acted categories. For each direction, `Delta = UAR(R2-P) - UAR(R0)` in absolute units, paired on the same held-out queries. Compute one prediction per query per seed; average metrics over the prespecified seeds, without treating seeds as independent participants.

Candidate seeds: 13, 37, 73. Freeze all stochastic stages and preserve every seed. Candidate useful benefit: `delta_min = 0.03` (three percentage points), pending pilot/precision justification. Candidate confidence procedure: 10,000 paired crossed-cluster bootstrap draws, independently resampling target speaker and text groups and using their product weights, identical resampling across model conditions; average the fixed seed metrics in each draw. Register handling for empty classes and too few clusters before freezing. For two directional primary effects, use 97.5% two-sided intervals (Bonferroni simultaneous family coverage of at least 95%); do not present ordinary utterance bootstrap intervals as equivalent. Low cluster counts must be flagged and sensitivity shown; no number of resampled draws creates new speakers.

**Candidate E1 scientific success gate:** both directional lower bounds exceed 0.03, R2-P beats R1 after the registered secondary-family correction, and leakage/QC controls pass. A single-direction effect supports only that direction. Upper bounds below 0.03 count against the proposed practically useful effect under this setting. Broad intervals are inconclusive and call for precision or scope revision. Oracle-only success blocks progression on an operational-residual claim.

Secondary endpoints: within-language UAR; macro-F1 and class recall; R2-P versus R1 and N1; reference error/variance; expression retrieval on independently annotated event pairs if available; language and speaker probe performance at matched expression utility. Candidate secondary family uses Holm-adjusted tests at 0.05, with all tests/family members frozen in advance. Probe identities are learned/evaluated under their own valid disjoint-recording splits; do not try to classify unseen speaker IDs absent from probe training. Corpus confounding limits probe interpretation.

**Power and sample size remain unresolved.** Simulate speaker/text-cluster variation using independent development data and the frozen analysis, aiming at 80% power for the practical primary target in both directions and an acceptable interval width. Specify the exact planning alternative, variance and retained cluster counts before registration. Existing ESD speaker counts may be insufficient; report that honestly. Do not count every frame, repetition or seed as an independent sample. A pilot used for planning never becomes the confirmatory test set.

### E1.5 Exclusions, stopping and reporting

Exclude only preregistered corrupt files, rights-ineligible recordings, unavailable pairs for a condition, irrecoverable alignment failures or insufficient valid measurement windows. Report exclusions by class, language and speaker, including whether paired-reference availability changes the comparison population. Lock a common primary query set for R0/R1/R2-P. Technical failures are logged; no early termination because interim results look favorable. If running cannot continue for resource/access reasons, report an incomplete study without a confirmatory success claim.

Deliver: frozen protocol/config; legal access record; private manifests and permitted public split recipe; reference/mask/error audits; directional primary effects with simultaneous intervals; all secondary comparisons and adjustments; controls; all run metadata; negative cases; limitations and a gate decision. Numeric tables must remain empty until populated from traceable real runs.

## E2 — Multiscale Temporal Structure and Coupling

Proceed after a justified E1 decision; if E1 is inconclusive, any E2 extension is explicitly exploratory. Hold the reference regime, query set and downstream task fixed. Compare single-scale summaries, fixed multiscale transforms, matched-budget temporal convolutions, and multiscale plus coupling. Separate the scale contrast from the coupling contrast; control their comparison family.

Register masks, scale ranges, edge/cone-of-influence exclusions, treatment of irregular event sampling, and capacity/training budgets. Circularly shift or permute channel timing within valid segments while preserving each channel's marginal statistics; use multiple registered perturbations and same-artifact controls. A perturbation can harm phonetic plausibility independently of expression; a listening effect is interpretable only after that artifact audit.

Candidate primary endpoint: directional held-out non-neutral UAR increment from coupling over uncoupled multiscale representation, using E1's dependence-aware inference. Candidate useful increment: 0.02, to be justified and frozen. Subsequent blinded perception requires its own registered study. Report whether reduced language leakage trades off against expression utility. No scale or channel is declared a physical emotion component.

## E3 — Constrained Cross-Lingual Expression Reconstruction

### Data, systems and blinding

Requires authorized source voices, a licensed renderer and bilingual semantic/event annotation. Use reviewed translations shared across systems, held-out speaker/text/semantic groups, both directions and a separately consented listener study. ESD is not a cross-language translation gold standard. If a new corpus is collected, speaker numbers and sentence counts are decided by power/budget/consent, not copied as completed counts from the manuscript.

| ID | System | Attribution role |
| --- | --- | --- |
| B0 | Neutral target rendering | No-transfer reference |
| B1 | Direct acoustic mapping | Raw-feature comparator |
| B2 | Discrete style or low-dimensional condition | Coarse-expression comparator |
| B3 | Reference-style embedding without explicit residual | Primary matched system comparator |
| B4 | External expressive translator, if accessible/licensed | Contextual reference with unmatched resources |
| M1/M2/M3 | Residual; residual + scales; residual + scales + coupling | Component ablations |
| M4 | M3 + semantic events + target phonological constraints | Full CREAM |

B1–B3/M1–M4 share the renderer, translations, speaker condition, data and practical tuning budget. Register whether speaker identity preservation is permitted and evaluable. Compare M4 to otherwise identical variants without event alignment and without language constraints; match the absolute-time/linear-stretch/DTW alternatives. Predefine strata for reordered focus, lexical tone, pauses, sarcasm and alignment ambiguity. Blind model identity, randomize B/C order and balance trials, sessions and language direction. Match recording/playback loudness transparently while preserving within-utterance dynamics; disclose that normalization can remove an expression cue.

### Primary endpoint and constraints

Primary experiment-level endpoint: blinded reference-A, candidate-B/C 2AFC expression preference, M4 versus B3, reported separately by direction. Use qualified bilingual listeners for cross-language matching; monolingual target listeners may assess target intelligibility/naturalness but cannot replace the primary bilingual task. Give one expression prompt covering delivery/strength/focus/timing, with intelligibility/naturalness evaluated in separate tasks.

Candidate useful preference: probability of choosing M4 ≥0.55; require the simultaneous directional lower bound to exceed 0.55. Freeze a mixed-effects logistic analysis with listener and source speaker/semantic-item random effects, order/language controls and a prespecified convergence fallback. Use marginal preference estimates/intervals under that model; do not equate a conditional logit intercept to a marginal probability without the registered conversion. Determine listeners/items through crossed-design power simulation. Freeze eligibility, hearing/language checks, attention-trial exclusions and stopping before enrollment.

Candidate harm margins versus B3: WER (English) or CER (Mandarin) increase ≤0.02 absolute; Mandarin tone-error increase ≤0.02 absolute; naturalness MOS difference ≥−0.20 on a frozen 1–5 scale. Human transcript/keyword intelligibility supplements a fixed ASR whose known language bias is reported. Speaker-identity margins remain **TBD** until a permitted identity target and calibrated verifier are chosen. Non-inferiority must use interval bounds, not non-significance. Register simultaneous intervals or a specified intersection-union testing plan for the full constraint set. Full H4 support requires every applicable frozen constraint to pass; inability to measure one is a limitation, not automatic success.

Secondary: focus/event localization, continuous annotation CCC if actually annotated, independent human-calibrated expression metrics, identity similarity if authorized, and error strata. Judges used in training/selection must not serve as the only final evaluator. Shared semantic accuracy failures must be reported even when expression preference improves.

## E4 — Minimal Representation and Independent Replication

Remove channels, scales, coupling, event alignment and latent factors individually, with the same budget and a prespecified performance/complexity criterion. Select simplifications on development data. Replicate the frozen selected system on a legally acquired independent corpus, new speakers and listener population. Register a new primary endpoint and precision/power plan before accessing its test outcomes. Do not reuse the E3 test set to choose a “minimal” model and claim replication.

Release a claim table linking H1–H4 to supported, contradicted or inconclusive findings, with language/genre/reference-access limits. Failed generalization and negative ablations belong in the final paper.
