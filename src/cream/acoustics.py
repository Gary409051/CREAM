"""Acoustic measurement boundary; extractor and masks must be audited before E1."""

from pathlib import Path
from typing import Protocol

from .data import FeatureSequence


class AcousticExtractor(Protocol):
    def extract(self, recording_path: Path, recording_id: str) -> FeatureSequence:
        """Extract valid acoustic/event channels with explicit units and provenance."""
        ...
