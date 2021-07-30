from typing import List, Optional

from ..models.common import BaseModel
from ..fields.institution import InstitucionFields


class Institution(BaseModel):
    code: str = InstitucionFields.code
    name: str = InstitucionFields.name


Institutions = List[Institution]
