# Research Questions and Hypotheses

Version 0.1 · 2026-10-10 · **all CREAM hypotheses below are untested**.

## Operational vocabulary

- **Vocal expression:** audible intensity, emphasis, timing, voice quality and intended delivery; listener-perceived expression is not a verified internal psychological state.
- **Neutral reference:** an explicitly elicited or predicted reference delivery under specified content, language, phonology, speaker and recording conditions. It retains lexical tone and obligatory linguistic prosody.
- **Counterfactual target:** the acoustic pattern that would occur under a stipulated neutral delivery. An observed paired recording approximates this target under strong comparability assumptions; subtraction alone establishes no causal effect.
- **Transferable representation:** information useful on new speakers/texts and a specified target language, under a disclosed training/calibration regime. Probe failure alone cannot prove independence.
- **Expression preservation:** perceived similarity of delivery under semantic-event correspondence, jointly constrained by target intelligibility, naturalness and authorized speaker identity.

## Measurement model and limits

Let `p_k(u)` be acoustic channel `k` aligned to a phonetic or prosodic event coordinate `u`; `b_k(u)` is its reference prediction and `s_k(u)` a training-estimated neutral variability scale. For valid continuous observations:

```text
r_k(u) = (p_k(u) - b_k(u)) / max(s_k(u), epsilon_k)
```

Use voiced masks for log F0, valid-window masks for voice quality, log ratios for positive durations, and event representations for pauses. Invalid values remain missing with a mask; zero padding must not be interpreted as observed neutral expression. Scales, clipping and `epsilon_k` are frozen from development data. Report how changing these choices affects conclusions.

Neither `p - b` nor a learned latent vector identifies a unique emotion coordinate system. Recording effects, aligner errors, baseline prediction error, lexical tone and discourse context can enter the residual. A flexible encoder/decoder can reparameterize latent coordinates without changing reconstruction.

## Questions and falsifiable hypotheses

| ID | Question and hypothesis | Main comparison / evidence | Evidence against the claim |
| --- | --- | --- | --- |
| RQ1 / H1 | Does a conditioned neutral reference retain more transferable expression information than raw acoustic features? Residuals should improve held-out cross-language diagnostics and ultimately perceived expression preservation. | E1 predicted residual vs matched raw and simple normalized features; E3 M4 vs B3 for perceptual expression | Adequately precise effects below registered practical benefit; effects disappear with leakage controls; improvement restricted to oracle references |
| RQ2 / H2 | Do multiple time scales and cross-channel timing add information beyond marginals and capacity? | E2 multiscale vs single-scale; coupled vs uncoupled; matched-capacity and temporal perturbation controls | No useful incremental benefit, or all gains explained by parameters, distributions or audible perturbation artifacts |
| RQ3 / H3 | Does semantic-event alignment preserve focus and expressive turning points better than time stretching or acoustic DTW? | E3 alignment ablation, emphasis location and listener comparison in word-order strata | No benefit in registered reordered-event strata or increased annotation/deletion errors |
| RQ4 / H4 | Can constrained reconstruction improve expression without unacceptable intelligibility, tone or naturalness loss? | E3 M4 vs B3, primary 2AFC preference plus non-inferiority constraints | Perceptual benefit fails or any harm interval crosses the permitted margin |

E1 tests a restricted implication of H1 using non-neutral acted-category recognition. It cannot establish H1's full human-perception claim, H2–H4, or cultural universality. H2, H3 and H4 must have separate comparison families; success of the full system does not by itself attribute a gain to each component.

## Competing explanations

1. Ordinary speaker/global normalization accounts for all improvement; a conditioned reference adds nothing.
2. Pairing removes content/recording differences instead of isolating expression.
3. Target-language neutral calibration supplies domain adaptation responsible for the result.
4. Reference prediction strips tone or focus and damages the signal of interest.
5. Dataset styles are shared performance conventions; natural expression transfers differently.
6. Rendering bottlenecks conceal a useful representation, or a powerful generator compensates for an uninformative one.

## Interpretation rules

Report effect estimates, uncertainty, exclusions and operating conditions. An interval too wide to decide the registered practical threshold means **inconclusive**. A non-significant p-value alone does not refute a hypothesis. An upper bound below the practical threshold provides evidence against the stipulated useful effect; an interval wholly below zero indicates deterioration for that condition. Formal equivalence tests require independently preregistered equivalence margins.

Absolute language/speaker invariance is not an acceptance criterion. Evaluate whether expression utility remains while leakage decreases, and describe the utility/leakage tradeoff. A low language-probe score accompanied by a collapsed expression score is a failure, not evidence of a successful representation.

See [EXPERIMENT_PROTOCOLS](EXPERIMENT_PROTOCOLS.md) for draft comparisons, candidate thresholds and freeze rules, and [LITERATURE_REVIEW](LITERATURE_REVIEW.md) for existing evidence and novelty boundaries.
