"""Neutral-reference prediction boundary, distinct from paired-reference evaluation."""

from typing import Protocol, Tuple

from .data import Conditioning, FeatureSequence


class NeutralReferencePredictor(Protocol):
    def predict(
        self, conditioning: Conditioning, grid: Tuple[float, ...], grid_unit: str
    ) -> FeatureSequence:
        """Predict using a frozen model and only registered conditioning inputs."""
        ...
