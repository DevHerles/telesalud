from typing import List, Optional

import pydantic
from ..models.common import BaseModel
from ..fields.department import DepartmentFields
from ..fields.disa import DisaFields
from ..fields.location import LocationFields

__all__ = (
    "DepartmentUpdate",
    "DepartmentRead",
    "DepartmentCreate",
    "DepartmentsRead",
    "DepartmentPoint",
    "DepartmentsPoint",
)


class DepartmentPoint(BaseModel):
    IdDepartamento: Optional[str] = DepartmentFields.code
    Total: Optional[int] = DepartmentFields.total
    IdLocal: Optional[int] = DisaFields.code,
    Latitud: Optional[float] = LocationFields.latitude
    Longitud: Optional[float] = LocationFields.longitude


class DepartmentPointRead(DepartmentPoint):
    pass


class Department(BaseModel):
    code: str = DepartmentFields.code
    name: str = DepartmentFields.name


DepartmentsPoint = List[DepartmentPoint]
