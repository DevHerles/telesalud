from typing import List, Optional

from ..models.common import BaseModel
from ..fields.eess import EessFields
from ..fields.location import LocationFields
from ..fields.department import DepartmentFields
from ..fields.province import ProvinceFields
from ..fields.district import DistrictFields
__all__ = (
    "PointUpdate",
    "PointRead",
    "PointCreate",
    "PointsRead",
    "PointSearch",
)


class PointUpdate(BaseModel):
    Total: int = LocationFields.total
    IdLocal: int = EessFields.IdLocal
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class PointCreate(PointUpdate):
    pass


class PointRead(PointCreate):
    pass


class PointSearch(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]
    IdDistrito: Optional[str]


PointsRead = List[PointRead]
