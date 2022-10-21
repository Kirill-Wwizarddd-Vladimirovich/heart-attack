"""Data Transfer Object for API Layer."""

from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """DTO for making prediction consumed by API."""


class PredictionResponse(BaseModel):
    """DTO used as a format for predict response body."""
