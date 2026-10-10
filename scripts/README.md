# Scripts

Run `python3 scripts/validate_repository.py` from the repository root. The checker is read-only and uses the Python standard library. It verifies required structure, local Markdown file/heading links, empty-directory placeholders, original checksums and the explicit E1 draft configuration. It performs no download, training, test-set access or Git mutation.

External URLs are not fetched by this checker. Citation/source verification is recorded separately in [LITERATURE_REVIEW](../docs/LITERATURE_REVIEW.md). The preserved manuscript is hash-checked, not rewritten or linted.

There is no data acquisition or experiment runner yet. Future runners must reject unresolved or unfrozen configs, preserve provenance and avoid private data in committed output. See [REPRODUCIBILITY](../docs/REPRODUCIBILITY.md).
