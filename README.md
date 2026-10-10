# CREAM

**Counterfactual Residual Expression Analysis and Mapping**

Language-independent vocal expression representation and cross-lingual reconstruction via counterfactual acoustic residuals and multiscale temporal modeling.

**Status: research framework and repository scaffold, 2026-10-10.** No dataset has been acquired in this initialization; no feature extraction, model training, human study, or empirical result is reported. The interfaces are design boundaries, not implemented algorithms. Protocols are preregistration drafts, not registered studies.

CREAM asks whether deviations from a language- and phonology-conditioned neutral acoustic reference can retain transferable vocal expression, and whether multiscale temporal structure and semantic-event alignment help reproduce that expression in another language. “Language-independent” means measured transfer in specified languages and tasks; it does not imply universal emotion coordinates or access to a speaker's internal emotional state.

## Start here

1. Read the [roadmap](docs/RESEARCH_ROADMAP.md) and [questions and hypotheses](docs/RESEARCH_QUESTIONS_AND_HYPOTHESES.md).
2. Review [E1 and the later experiment protocols](docs/EXPERIMENT_PROTOCOLS.md) before implementing a model.
3. Resolve [data access](docs/DATA_MANAGEMENT.md), [ethics](docs/ETHICS.md), and the [project license decision](LICENSE_DECISION.md).
4. Follow [reproducibility requirements](docs/REPRODUCIBILITY.md); record changes in the [decision log](docs/DECISIONS.md).
5. Consult the [literature evidence register](docs/LITERATURE_REVIEW.md) and [contribution guide](CONTRIBUTING.md).

## Research sequence

`approved data → neutral-reference audit → E1 residual validation → E2 temporal structure → E3 constrained cross-lingual reconstruction → E4 replication and minimal representation`

E1 is the first scientific gate. A paired neutral recording is a useful reference but is not evidence that an operational baseline predictor works. Predictions and paired-reference analyses must be reported separately. A negative or inconclusive result is a valid research outcome and can change the roadmap.

## Layout

```text
CREAM/
├── CREAM_Research_Paper_v1.pdf        # existing, unchanged, tracked
├── CREAM_Research_Paper_v1.docx       # existing, unchanged, tracked
├── LECR_Research_Manuscript_v1.md     # existing, unchanged, tracked
├── papers/v1/                       # archive index and original-file checksums
├── docs/                            # research design, governance and evidence
├── src/cream/                       # dependency-light module interfaces
├── tests/                           # future synthetic contract tests
├── configs/                         # explicit draft experimental configuration
├── scripts/                         # repository validation; no experiment runner yet
├── experiments/                     # preregistrations and reviewed reports
│   ├── preregistrations/
│   ├── reports/
│   └── runs/                        # ignored local outputs
├── data/
│   ├── raw/                         # immutable acquired recordings, ignored
│   ├── interim/                     # reversible intermediates, ignored
│   ├── processed/                   # features/splits, ignored
│   ├── external/                    # third-party models/data, ignored
│   └── manifests/                   # schema only; real manifests ignored
├── CONTRIBUTING.md
├── LICENSE_DECISION.md              # no open-source license selected
├── pyproject.toml
└── .gitignore
```

The [v1 archive index](papers/v1/README.md) catalogs the three originals without moving or duplicating them. Existing filenames, content, Git tracking and historical links are preserved. Future revisions can live in `papers/v2/`.

## Local scaffold checks

From the repository root, using Python 3.9 or newer:

```sh
python3 scripts/validate_repository.py
PYTHONPATH=src python3 -c "import cream; print(cream.__version__)"
```

These commands check structure, local Markdown links, original-file hashes and the draft configuration. They do not run experiments or validate scientific claims. Python 3.9 is the scaffold's minimum syntax level, not a chosen training environment; select and lock the actual research environment before E1. No ML or audio dependency is installed or selected. See the [module guide](src/cream/README.md) and [configuration guide](configs/README.md).

## Evidence and licensing

The [v1 manuscript](LECR_Research_Manuscript_v1.md) is a hypothesis and methods draft. Published prior work supports individual components; CREAM's residual-transfer mechanism and reconstruction advantage remain untested. The literature register distinguishes source verification from independent replication and keeps unresolved citations visible.

Repository publication does not resolve permissions for code, papers, models, recordings or generated voices. The owner must decide licenses separately. Real audio, participant records, model checkpoints and experiment outputs are excluded from Git by default. Do not interpret `.gitignore` as a complete privacy control.
