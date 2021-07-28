from typing import List, Optional

from ..models.common import BaseModel
from ..fields.eess import EessFields
from ..fields.location import LocationFields
from ..fields.department import DepartmentFields
from ..fields.province import ProvinceFields
from ..fields.district import DistrictFields
__all__ = (
    "PointSearch",
)


class EessPoints(BaseModel):
    Total: int = LocationFields.total
    IdLocal: str = EessFields.IdLocal
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class DepartmentPoints(BaseModel):
    IdDepartamento: str = EessFields.department_code,
    Total: int = LocationFields.total
    IdLocal: str = EessFields.IdLocal
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class ProvincePoints(BaseModel):
    IdDepartamento: str = EessFields.department_code,
    IdProvincia: str = EessFields.province_code,
    Total: int = LocationFields.total
    IdLocal: str = EessFields.IdLocal
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class DistrictPoints(BaseModel):
    IdDepartamento: str = EessFields.department_code,
    IdProvincia: str = EessFields.province_code,
    IdDistrito: str = EessFields.district_code,
    Total: int = LocationFields.total
    IdLocal: str = EessFields.IdLocal
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class PointSearch(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]
    IdDistrito: Optional[str]
