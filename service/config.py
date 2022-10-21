"""Global configuration for service."""

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    """Configuration for project.

    Example usage of `pydantic.BaseSettings` can be found on
    https://pydantic-docs.helpmanual.io/usage/settings/

    List of all supported by `pydantic` data types
    https://pydantic-docs.helpmanual.io/usage/types/

    Specifically `pydantic` supports `pathlib.Path` and moreover has custom `FilePath`
    and `DirectoryPath` which are wrapping for `pathlib.Path`. On the stage of config
    object creation this paths would be validated.
    """

    API_TITLE: str = Field(
        env="API_TITLE",
        default="Model Web API Service",
    )

    API_DESCRIPTION: str = Field(
        env="API_DESCRIPTION",
        default="Pet project. Heart atattack analyzis",
    )
