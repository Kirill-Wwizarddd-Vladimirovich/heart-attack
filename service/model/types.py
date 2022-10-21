"""Data structures used by model."""

from dataclasses import dataclass

from typing_extensions import TypeAlias

# TODO place here actual type for used model
Model: TypeAlias = object


@dataclass
class PredictionInput:
    """DTO for actually making prediction."""


@dataclass
class PredictionOutput:
    """DTO with actual prediction result."""
