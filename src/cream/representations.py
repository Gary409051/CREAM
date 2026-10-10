"""Multiscale/coupling boundary; learned transforms must fit permitted training data."""

from typing import Protocol

from .data import ExpressionRepresentation, FeatureSequence


class ExpressionEncoder(Protocol):
    def encode(self, residual: FeatureSequence) -> ExpressionRepresentation:
        """Encode with valid-support/edge policies and frozen transformation state."""
        ...
