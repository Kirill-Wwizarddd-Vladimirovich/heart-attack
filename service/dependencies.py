from dependency_injector import containers, providers

from service.config import Config
from service.model.types import Model


class Dependencies(containers.DeclarativeContainer):
    """Declarative list of dependencies in your application.

    Attributes:
        config (`providers.Object`): `pydantic.BaseSettings` configuration
        model (`providers.Dependency`): model object for prediction initialized
            outside container
    """

    config = providers.Object(Config())
    model = providers.Dependency(instance_of=Model)
