from typing import List
import pydantic
from ..models.common import BaseModel
from ..fields.department import DepartmentFields
from ..fields.province import ProvinceFields

__all__ = (
    "ProvinceUpdate",
    "ProvinceRead",
    "ProvinceCreate",
    "ProvincesRead",
)


class ProvinceUpdate(BaseModel):
    code: str = ProvinceFields.code
    name: str = ProvinceFields.name
    department_code: str = DepartmentFields.code


class Province(ProvinceUpdate):
    pass


class ProvinceCreate(ProvinceUpdate):
    pass


class ProvinceRead(ProvinceCreate):
    """Body of Province GET and POST responses"""
    code: str = ProvinceFields.code
    name: str = ProvinceFields.name
    department_code: str = DepartmentFields.code

    class Config(ProvinceCreate.Config):
        extra = pydantic.Extra.ignore


ProvincesRead = List[ProvinceRead]
