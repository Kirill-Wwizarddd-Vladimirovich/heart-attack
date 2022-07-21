"""API Endpoints for accessing model."""

from fastapi import APIRouter, status
from fastapi.responses import Response

from service.api.contracts import PredictionRequest

router = APIRouter()


@router.post("/predict")
async def predict(contract: PredictionRequest):
    """Executes actions for making prediction.

    Basically it should execute ETL scripts and then actual model on parsed data.
    """


# TODO healthcheck endpoint
@router.get("/healthcheck", status_code=200)
def helthcheck():
    """Healthcheck endpoint that returns 200 OK on any request."""
    return Response(status_code=status.HTTP_200_OK)
