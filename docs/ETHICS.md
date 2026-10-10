# Ethics and Responsible Research

Version 0.1 · 2026-10-10 · review status: **not determined; no new collection or human study conducted**.

## Scope and interpretation

CREAM models audible and perceived expression. Do not claim to diagnose internal emotions, personality, mental health or deception from residuals. Acted style labels and listeners' impressions are not psychological ground truth. Report dialect, culture, recording setting, demographic coverage where consent and sample size allow, and uncertainty without turning groups into stereotypes.

“Neutral” is an elicitation/reference convention. It may contain pragmatic focus, social stance or cultural expectations. Audit the harm from stripping those cues, especially Mandarin lexical tone and emphasis. A strong expression score does not justify lost semantic content or an unintelligible translation.

## Before licensed-data reuse

Verify the intended use, permitted processing/training, publication and redistribution. Record the relevant review or exemption determination through the applicable institution/process, rather than assuming public availability exempts a study. Restricted corpora, private voice identities and generated examples require artifact-specific decisions. There is no automated outreach or consent acquisition in this scaffold.

## Before new recordings or listener studies

Assign an accountable investigator and obtain the required review determination before recruitment. Prepare a participant information/consent process in a language the participant understands, stating:

- Research purpose, recording/listening tasks, duration, compensation and voluntary participation.
- Potential discomfort from expressive/negative prompts, stopping or skipping options, and withdrawal process/cutoff.
- Recording, transcription, annotation, feature extraction and training permissions, with clear retention and access rules.
- Separate choices for identifiable audio release, voice-conditioned synthesis, cross-language reuse and demonstration examples. General recording consent is not voice-cloning permission.
- Storage/backup security, identity-linkage separation, publication scope and contact route for questions/withdrawal.

Consent text, compensation, retention periods and review identifiers are **TBD**; they are not approved forms. Start with consenting adults if new collection is pursued. Any inclusion of minors or vulnerable populations needs a separately justified design and review. Listener hearing/language eligibility and attention exclusions must be preregistered and applied consistently; compensation must not depend on giving favorable model ratings.

## Voice rendering and examples

Use only speakers whose permissions cover the intended synthesis. Do not demonstrate impersonation of an unconsenting person. Mark synthetic examples and their limitations; preserve generation provenance and consider supported watermarking/disclosure mechanisms without claiming perfect detection. Keep authorized voice identity separate from expressive similarity in evaluation. Public demonstration release is a separate rights/consent check.

## Data stewardship and equitable evaluation

Treat voices, transcripts and embeddings as potentially identifiable. Pseudonymization does not guarantee anonymity. Restrict access, keep linkage tables outside Git, and follow [DATA_MANAGEMENT](DATA_MANAGEMENT.md) for retention/withdrawal and backups. Report subgroup performance only when consent, meaningful coverage and privacy allow; do not infer group traits from small differences. Include native/bilingual language competence and dialect context in interpreting listener agreement.

Record bias/error cases, unintelligible or tone-damaged outputs and negative findings. If consent/access changes, pause the affected data use, trace derivatives and document corrective actions privately. Log non-identifying study decisions in [DECISIONS](DECISIONS.md).
