"""Authorized target-language rendering boundary; no voice/model supplied."""

from pathlib import Path
from typing import Protocol

from .data import Conditioning, ExpressionRepresentation


class ExpressionRenderer(Protocol):
    def render(
        self,
        expression: ExpressionRepresentation,
        target: Conditioning,
        voice_permission_record_id: str,
        output_path: Path,
    ) -> Path:
        """Render only under audited voice/model rights and target-language constraints."""
        ...
