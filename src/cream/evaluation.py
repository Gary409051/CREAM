"""Independent evaluation boundary; metrics and inference remain unimplemented."""

from typing import Mapping, Protocol, Sequence


class TransferEvaluator(Protocol):
    def evaluate(
        self,
        predictions: Sequence[str],
        labels: Sequence[str],
        speaker_groups: Sequence[str],
        text_groups: Sequence[str],
    ) -> Mapping[str, float]:
        """Evaluate registered endpoints with explicit class and dependence policies."""
        ...
