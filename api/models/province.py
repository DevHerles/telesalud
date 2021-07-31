from typing import List
from ..models.common import BaseModel
from ..fields.department import DepartmentFields
from ..fields.province import ProvinceFields


class Province(BaseModel):
    code: str = ProvinceFields.code
    name: str = ProvinceFields.name
    department_code: str = DepartmentFields.code


Provinces = List[Province]
