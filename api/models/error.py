from pydantic import BaseModel, Field

__all__ = (
    "BaseError",
    "BaseIdentifiedError",
    "NotFoundError",
    "AlreadyExistsError",
)


class BaseError(BaseModel):
    message: str = Field(..., description="Error message or description")


class BaseIdentifiedError(BaseError):
    identifier: str = Field(
        ...,
        description="Unique identifier wich this error references to",
    )


class NotFoundError(BaseIdentifiedError):
    "The entity does not exists"
    pass


class AlreadyExistsError(BaseIdentifiedError):
    """An entity being created already exists"""
    pass
