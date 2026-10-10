# Recording Manifest Contract

Real manifests use JSONL, one JSON object per recording, named for example `esd-vendor-version.private.jsonl`. They are excluded by `.gitignore`; the [schema](manifest.schema.json) is tracked. No actual row or participant is created here. Schema validation support will be selected with the ingestion implementation; the repository check only confirms valid JSON for this schema.

Required fields:

| Field | Meaning |
| --- | --- |
| `recording_id` | Opaque stable ID; never a participant's real name |
| `corpus`, `corpus_version` | Provider and immutable version/acquisition snapshot |
| `relative_path`, `sha256` | Relative raw-data path and file digest; no private absolute paths |
| `speaker_id`, `language`, `dialect` | Pseudonymous identity and recorded language/dialect; dialect may be unknown |
| `text_group_id`, `semantic_group_id` | Normalized same-language text group; semantic group only when equivalence is reviewed |
| `expression_label`, `label_provenance` | Observed elicitation/annotation category and its origin |
| `neutral_pair_id`, `pair_audit_status` | Verified recording link or null; unknown is not an implied pair |
| `session_id` | Recording-condition/session group if available |
| `sample_rate_hz`, `duration_seconds` | Measured recording properties, positive |
| `split` | Train/development/test/support/quarantine/unassigned |
| `qc_status`, `qc_reasons` | Audit result and explicit exclusion/unknown reasons |
| `rights_record_id` | Link to a private rights record; no agreement or identity embedded |

The schema checks row shape, not truth or leakage. Ingestion code must verify paths stay within the raw-data root, hashes match, IDs are unique, pair IDs exist, links match audited speaker/language/text, group splits are disjoint, and support is permitted by the protocol. Unknown nullable fields require a reason in QC/provenance. Do not invent missing language, expression, translation or consent data.

Store real transcripts, time annotations and identity/consent linkage separately with access controls. Public split metadata requires a rights/privacy review even when IDs are pseudonymous. See [DATA_MANAGEMENT](../../docs/DATA_MANAGEMENT.md).
