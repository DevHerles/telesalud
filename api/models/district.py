from typing import List
import pydantic
from ..models.common import BaseModel
from ..fields.department import DepartmentFields
from ..fields.province import ProvinceFields
from ..fields.district import DistrictFields

__all__ = (
    "DistrictUpdate",
    "DistrictRead",
    "DistrictCreate",
    "DistrictsRead",
)


class DistrictUpdate(BaseModel):
    code: str = DistrictFields.code
    name: str = DistrictFields.name
    department_code: str = DepartmentFields.code
    province_code: str = ProvinceFields.code


class District(DistrictUpdate):
    pass


class DistrictCreate(DistrictUpdate):
    pass


class DistrictRead(DistrictCreate):
    pass

    class Config(DistrictCreate.Config):
        extra = pydantic.Extra.ignore


DistrictsRead = List[DistrictRead]
