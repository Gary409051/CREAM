# Data Management and Access

Version 0.1 · 2026-10-10 · no corpus acquired during initialization.

## Candidate assets and access state

| Asset | Scientific role | Rights/access evidence | Current action |
| --- | --- | --- | --- |
| ESD | Same-language neutral/acted-expression pairs; initial English/Mandarin diagnostics | [Official README](https://github.com/HLTSingapore/Emotional-Speech-Data) requests a license form and research-purpose use; repository license marker does not settle recording rights | Pending agreement/term review and pairing audit; no download or contact made |
| RECOLA | Optional continuous-affect measurement study | [Official corpus paper](https://recola.human-ist.ch/data/emoSPACE13_RECOLA_Database.pdf); French interaction scope | Access agreement and annotation/release terms not reviewed; not part of E1 by default |
| Controlled bilingual recordings | Semantic-event alignment and perceptual reconstruction | No asset exists here; consent/review/collection plan required | Do not treat planned people/sentence counts as data |
| Pretrained feature, emotion, alignment or TTS models | Candidate measurement or rendering components | Exact artifact/version, training overlap and terms unresolved | Select later; weights and derived outputs have separate release checks |
| SeamlessExpressive (optional B4) | External contextual comparison | [Official implementation](https://github.com/facebookresearch/seamless_communication), [Seamless license](https://github.com/facebookresearch/seamless_communication/blob/main/SEAMLESS_LICENSE) | Model materials have a distinct noncommercial-research agreement; confirm artifact-specific conditions before use or release |

Source checks dated 2026-10-10. These are access notes, not a comprehensive legal opinion or accepted agreement. Before acquisition, record the actual signed/accepted terms and permitted purpose, training, redistribution, derived features/weights, generated audio, attribution, retention and any commercial-use restrictions. Do not send licensing correspondence automatically.

## Storage contract

| Location | Contents and rule |
| --- | --- |
| `data/raw/` | Original licensed recordings, read-only after acquisition; hash at ingestion; never overwrite |
| `data/interim/` | Resampling/alignment/QC intermediates; reproducible from raw; track provenance |
| `data/processed/` | Derived features, labels, split indices; exact pipeline/config links; privacy remains applicable |
| `data/external/` | Authorized third-party assets; preserve license text and version provenance privately |
| `data/manifests/` | Tracked schema/guide only; actual `.private.jsonl` manifests ignored |
| `experiments/runs/` | Local run configs/logs/predictions; ignored; release selected reviewed summaries separately |

Identity/contact/consent linkage tables and signed license forms belong in access-controlled storage outside this repository. Use encryption/access permissions and an approved backup location for actual data; ignoring files in Git does not encrypt them. Backups must follow the same access, retention and withdrawal policy. Document custodian, storage location and restore-check date privately.

## Manifest fields

The [manifest guide](../data/manifests/README.md) defines one JSONL row per recording with an opaque stable recording ID, corpus/version, relative path, SHA-256, pseudonymous speaker, language/dialect, normalized text group, semantic group if verified, expression-label provenance, neutral-pair ID if audited, session, sample rate/duration, split, QC and rights-record ID. Keep sensitive transcripts, identities and consent specifics out of public Git. Missing metadata is explicit `null` with a reason; missing translation equivalence is not guessed from filenames.

Private rights records include the license/consent version, acquisition date, permitted uses, attribution, access holders, retention deadline and allowed release categories. Code, recordings, labels, embeddings, checkpoints and generated examples can have different rights. Features and pseudonymous voices can remain identifying.

## Ingestion and split procedure

1. Resolve access rights and ethics requirements; assign a data steward. Save private evidence of the actual terms and approval scope.
2. Ingest into a versioned raw subdirectory without modifying originals. Record archive/file hashes, source/version, inventory and recording conditions.
3. Audit labels, transcripts and neutral pairs; identify duplicate waveforms and near-duplicate text/semantic groups. Treat expression labels as elicitation/annotation data, not verified mental states.
4. Generate deterministic speaker/text/session partitions and separate permitted neutral calibration. Pair links never silently bridge training and test. Quarantine ambiguous pairing and off-diagonal split cells.
5. Fit preprocessing/reference models on registered training/development partitions only. Propagate recording IDs, masks, QC reasons and transform versions through every derivative.
6. Freeze private manifests/config hashes before test evaluation. Release only a reviewed split recipe or sanitized identifier list when terms permit; private transcripts/paths never become automatically public.

## Retention, withdrawal and release

Retention duration is **TBD before any new collection**, subject to corpus terms and consent; no arbitrary indefinite retention is assumed. Define the withdrawal cutoff, treatment of published aggregate findings and how affected features/models/backups are traced and removed or retrained. Record withdrawals privately and regenerate affected manifests. Preserve a non-identifying audit of the action when allowed.

Before sharing an asset, the steward reviews licensing, identifiable voices/text, consent scope, third-party notices, destination and reproducibility sufficiency. Public summaries need not include raw audio. Report access restrictions honestly and provide permitted acquisition instructions. See [ETHICS](ETHICS.md), [REPRODUCIBILITY](REPRODUCIBILITY.md) and [LICENSE_DECISION](../LICENSE_DECISION.md).
