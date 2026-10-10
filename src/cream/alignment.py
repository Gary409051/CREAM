"""Semantic-event transfer boundary; reviewed correspondences may be nonmonotonic."""

from typing import Mapping, Protocol, Tuple

from .data import ExpressionRepresentation


class EventMapper(Protocol):
    def map_events(
        self,
        source: ExpressionRepresentation,
        correspondence: Mapping[str, Tuple[str, ...]],
    ) -> ExpressionRepresentation:
        """Map explicit source/target event IDs; preserve ambiguity and provenance."""
        ...
