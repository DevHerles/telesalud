from typing import List

from ..models.common import BaseModel
from ..fields.department import DepartmentFields


class Department(BaseModel):
    code: str = DepartmentFields.code
    name: str = DepartmentFields.name


Departments = List[Department]
