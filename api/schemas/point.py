from typing import Optional
from ..models.common import BaseModel


class PointSearchEntity(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]
    IdDistrito: Optional[str]


PointsSearchEntity = [PointSearchEntity]
