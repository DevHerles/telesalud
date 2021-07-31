from typing import List
from ..models.common import BaseModel
from ..fields.department import DepartmentFields
from ..fields.province import ProvinceFields
from ..fields.district import DistrictFields


class District(BaseModel):
    code: str = DistrictFields.code
    name: str = DistrictFields.name
    department_code: str = DepartmentFields.code
    province_code: str = ProvinceFields.code


Districts = List[District]
