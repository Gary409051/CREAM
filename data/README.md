# Data Layout

Only documentation, schemas and `.gitkeep` placeholders belong in the initial Git tree. No real recordings, labels, features or model weights are supplied.

- [raw](raw/): acquired originals, immutable and ignored.
- [interim](interim/): reversible preprocessing/alignment products, ignored.
- [processed](processed/): derived features/splits, ignored.
- [external](external/): third-party assets with separately audited terms, ignored.
- [manifests](manifests/README.md): tracked schema and policy; real manifests remain private.

Complete the [data access and management process](../docs/DATA_MANAGEMENT.md) before ingestion. `.gitignore` is a publication guard, not an access-control or encryption system.
