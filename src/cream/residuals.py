"""Residual boundary; uncertainty, valid masks and matched grids must be explicit."""

from typing import Protocol

from .data import FeatureSequence


class ResidualEstimator(Protocol):
    def transform(
        self,
        observed: FeatureSequence,
        reference: FeatureSequence,
        training_neutral_scale: FeatureSequence,
    ) -> FeatureSequence:
        """Use frozen channel policies; durations/events need type-specific handling."""
        ...
