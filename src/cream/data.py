"""Dependency-free contracts. Shape, rights and leakage validation is not yet implemented."""

from dataclasses import dataclass
from typing import Mapping, Optional, Tuple


@dataclass(frozen=True)
class Conditioning:
    """Permitted reference inputs, excluding observed expressive trajectories."""

    text_group_id: str
    language: str
    phonological_context: Tuple[str, ...]
    speaker_condition_id: Optional[str] = None


@dataclass(frozen=True)
class FeatureSequence:
    """Event/grid-aligned channels; values and valid masks are channel-major.

    Invalid entries require valid=False; their numeric filler has no meaning.
    Units and scale provenance must accompany implemented transformations.
    """

    recording_id: str
    grid: Tuple[float, ...]
    grid_unit: str
    channels: Tuple[str, ...]
    units: Tuple[str, ...]
    values: Tuple[Tuple[float, ...], ...]
    valid: Tuple[Tuple[bool, ...], ...]
    provenance: Mapping[str, str]


@dataclass(frozen=True)
class ExpressionRepresentation:
    """Candidate expression coordinates, not unique or universal emotion factors."""

    recording_id: str
    coordinates: Tuple[Tuple[float, ...], ...]
    valid: Tuple[Tuple[bool, ...], ...]
    provenance: Mapping[str, str]
