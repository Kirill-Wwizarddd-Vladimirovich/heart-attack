"""Model execution scripts."""

from dependency_injector.wiring import Provide, inject

from service.dependencies import Dependencies
from service.model.types import Model, PredictionInput, PredictionOutput


@inject
def predict(
    data: PredictionInput,
    model: Model = Provide[Dependencies.model],
) -> PredictionOutput:
    """Make prediction with injected model."""
