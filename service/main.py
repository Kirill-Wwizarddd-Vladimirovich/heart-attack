"""Service entrypoint."""

from dependency_injector import providers
from fastapi import FastAPI

from service.api import endpoints
from service.config import Config
from service.dependencies import Dependencies

from . import api, model


def create_app() -> FastAPI:
    """Create fastapi ASGI app for execution.

    Firstly `Dependencies` initialized. Then model read from binary file and placed into
    `Dependencies`. Next step is wiring `Dependencies` in order to inject them via
    `inject` decorator and `Provide` default value. Finally `FastAPI` object created and
    configured.

    Returns:
        `FastAPI` app
    """
    di = Dependencies()

    # TODO: read model here from binary file (pickle)
    ml_model = object()

    di.model.override(providers.Object(ml_model))

    di.wire(packages=[api, model])

    config: Config = di.config()

    app = FastAPI(
        title=config.API_TITLE,
        description=config.API_DESCRIPTION,
    )

    app.include_router(endpoints.router)

    app.di = di  # type: ignore

    return app
