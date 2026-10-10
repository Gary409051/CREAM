# Module Boundaries

The modules provide typed contracts only. They are not feature extractors, models, metrics or trained results. Protocols describe future implementations; importing them has no file/network/training side effects. Tuples provide dependency-free type examples, not a recommended storage format for large arrays.

| Module | Responsibility | Key constraint |
| --- | --- | --- |
| `data.py` | Recording identity, feature sequence and representation contracts | Units, masks, grids and provenance explicit; no embedded private identity |
| `acoustics.py` | Feature extraction | F0/voice-quality validity and event channels are explicit |
| `baselines.py` | Conditioned neutral-reference prediction | Input conditioning excludes the expressive query trajectory |
| `residuals.py` | Reference-relative deviations | Aligned grids and training-only variability scales |
| `representations.py` | Multiscale/coupling encoding | Keep single-scale/capacity controls and leakage evaluation |
| `alignment.py` | Reviewed semantic-event mapping | Language constraints and ambiguity disclosed; not assumed monotonic |
| `synthesis.py` | Authorized target rendering | Voice permission and control bandwidth checked |
| `evaluation.py` | Transfer/perception/intelligibility evaluation | Fixed independent endpoints; clustered uncertainty |

Interfaces deliberately do not supply plausible-looking default outputs. Data records do not yet validate dimensions, units, permissions or split leakage; those validations belong to implemented modules and meaningful tests. The [test plan](../../tests/README.md) lists these contracts.

Implement E1 measurement/reference modules first after access/pilot decisions. Any eventual package dependency and experiment runner must be justified and documented. The [protocol](../../docs/EXPERIMENT_PROTOCOLS.md) is the scientific authority for permitted calibration and primary comparisons.
