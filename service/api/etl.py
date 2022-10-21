"""Pipelines for processing data before sending it to the model."""

from service.api.contracts import PredictionRequest
from service.model.types import PredictionInput


def transform(request: PredictionRequest) -> PredictionInput:
    """Extract Transform Load Data part of pipeline."""
