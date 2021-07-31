from typing import List, Optional

from ..models.common import BaseModel
from ..fields.eess import EessFields
from ..fields.location import LocationFields


class EessPoints(BaseModel):
    Total: int = LocationFields.total
    IdLocal: str = EessFields.code
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class DepartmentPoints(BaseModel):
    IdDepartamento: str = EessFields.department_code,
    Total: int = LocationFields.total
    IdLocal: str = EessFields.code
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class ProvincePoints(BaseModel):
    IdDepartamento: str = EessFields.department_code,
    IdProvincia: str = EessFields.province_code,
    Total: int = LocationFields.total
    IdLocal: str = EessFields.code
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class DistrictPoints(BaseModel):
    IdDepartamento: str = EessFields.department_code,
    IdProvincia: str = EessFields.province_code,
    IdDistrito: str = EessFields.district_code,
    Total: int = LocationFields.total
    IdLocal: str = EessFields.code
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class PointSearch(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]
    IdDistrito: Optional[str]
