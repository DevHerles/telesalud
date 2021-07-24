# # Native # #
from typing import Type

## Installed # #

from fastapi.responses import JSONResponse
from fastapi import status as statuscode

# # Package # #
from ..errors.errors import (
    BaseError,
    BaseIdentifiedError,
    NotFoundError,
    AlreadyExistsError,
)

__all__ = (
    "BaseAPIException",
    "BaseIdentifiedException",
    "NotFoundException",
    "AlreadyExistsException",
)


class BaseAPIException(Exception):
    """Base error for custom API exceptions"""
    message = "Generic error"
    code = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model = BaseError

    def __init__(self, **kwargs):
        kwargs.setdefault("message", self.message)
        self.message = kwargs["message"]
        self.data = self.model(**kwargs)

    def __str__(self):
        return self.message

    def response(self):
        return JSONResponse(content=self.data.dict(), status_code=self.code)

    @classmethod
    def response_model(cls):
        return {cls.code: {"model": cls.model}}


class BaseIdentifiedException(BaseAPIException):
    """Base error for exceptions related with entities, uniquely identified"""
    message = "Entity error"
    code = statuscode.HTTP_500_INTERNAL_SERVER_ERROR
    model = BaseIdentifiedError

    def __init__(self, identifier, **kwargs):
        super().__init__(identifier=identifier, **kwargs)


class NotFoundException(BaseIdentifiedException):
    """Base error for exceptions raised because an entity does not exist"""
    message = "The entity does not exist"
    code = statuscode.HTTP_404_NOT_FOUND
    model = NotFoundError


class AlreadyExistsException(BaseIdentifiedException):
    """Base error for exceptions raised because an entity already exists"""
    message = "The entity already exists"
    code = statuscode.HTTP_409_CONFLICT
    model = AlreadyExistsError


class DepartmentNotFoundException(NotFoundException):
    """Error raised when a department does not exist"""
    message = "The department does not exist"


class ProvinceNotFoundException(NotFoundException):
    """Error raised when a province does not exist"""
    message = "The province does not exist"


class DistrictNotFoundException(NotFoundException):
    """Error raised when a district does not exist"""
    message = "The district does not exist"


class DepartmentAlreadyExistsException(AlreadyExistsException):
    """Error raised when a department already exists"""
    message = "The department already exists"


class ProvinceAlreadyExistsException(AlreadyExistsException):
    """Error raised when a province already exists"""
    message = "The province already exists"


class DistrictAlreadyExistsException(AlreadyExistsException):
    """Error raised when a district already exists"""
    message = "The district already exists"


def get_exception_responses(*args: Type[BaseAPIException]) -> dict:
    """Given BaseAPIException classes, return a dict of responses used on FastAPI endpoint definition, with the format:
    {statuscode: schema, statuscode: schema, ...}"""
    responses = dict()
    for cls in args:
        responses.update(cls.response_model())
    return responses
