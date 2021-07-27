from typing import List, Optional
import pydantic

from ..models.common import BaseModel
from ..fields.eess import EessFields
from ..fields.location import LocationFields
__all__ = (
    "EessUpdate",
    "EessRead",
    "EessCreate",
    "EesssRead",
)


class EessCreate(BaseModel):
    code: str = EessFields.code
    name: str = EessFields.name
    department: str = EessFields.department
    province: str = EessFields.province
    district: str = EessFields.district
    category: str = EessFields.category
    institution: str = EessFields.institution
    latitude: float = EessFields.latitude
    longitude: float = EessFields.longitude
    address: str = EessFields.address
    business_hours: str = EessFields.business_hours
    phone: str = EessFields.phone


class EessRead(BaseModel):
    IdLocal: int = EessFields.code
    NombreLocal: str = EessFields.name
    DireccionLocal: str = EessFields.address
    LatitudLocal: float = EessFields.latitude
    LongitudLocal: float = EessFields.longitude
    DepartamentoNombreLocal: str = EessFields.department
    ProvinciaNombreLocal: str = EessFields.province
    DistritoNombreLocal: str = EessFields.district
    HorarioLocal: str = EessFields.business_hours
    TelefonoLocal: str = EessFields.phone
    Institucion: str = EessFields.institution
    Categoria: str = EessFields.category


class EessUpdate(EessCreate):
    pass


class EessSearch(BaseModel):
    FiltroTipo: int
    FiltroValor: str


class EessPointRead(BaseModel):
    Total: int = LocationFields.total
    IdLocal: int = EessFields.IdLocal
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class EessPointSearch(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]
    IdDistrito: Optional[str]


EesssRead = List[EessRead]
EessPointsRead = List[EessPointRead]
