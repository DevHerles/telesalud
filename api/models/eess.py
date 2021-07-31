from typing import List, Optional
import pydantic

from ..models.common import BaseModel
from ..models.department import Department
from ..models.province import Province
from ..models.district import District
from ..models.institution import Institution
from ..fields.eess import EessFields
from ..fields.location import LocationFields


class EessBase(BaseModel):
    code: str = EessFields.code
    name: str = EessFields.name
    department: Department
    province: Province
    district: District
    institution: Institution
    category: str = EessFields.category
    latitude: float = EessFields.latitude
    longitude: float = EessFields.longitude
    address: str = EessFields.address
    business_hours: str = EessFields.business_hours
    phone: str = EessFields.phone


class EessCreate(BaseModel):
    code: str = EessFields.code
    name: str = EessFields.name
    department: str = EessFields.department
    department_code: str = EessFields.department_code
    province: str = EessFields.province
    province_code: str = EessFields.province_code
    district: str = EessFields.district
    district_code: str = EessFields.district_code
    category: str = EessFields.category
    institution: str = EessFields.institution
    latitude: float = EessFields.latitude
    longitude: float = EessFields.longitude
    address: str = EessFields.address
    business_hours: str = EessFields.business_hours
    phone: str = EessFields.phone


class EessRead(BaseModel):
    IdLocal: str = EessFields.code
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
    IdLocal: str = EessFields.code
    Latitud: float = LocationFields.latitude
    Longitud: float = LocationFields.longitude


class EessPointSearch(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]
    IdDistrito: Optional[str]


class DepartmentsList(BaseModel):
    IdDepartamento: str
    NombDep: str
    DisaCodigo: int


class ProvincesList(BaseModel):
    IdProvincia: str
    NombProv: str
    DisaCodigo: int


class DistrictsList(BaseModel):
    IdDistrito: str
    NombDis: str
    DisaCodigo: int


class ProvincePointSearch(BaseModel):
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]


class ProvinceSearch(BaseModel):
    DisaCodigo: Optional[int]
    IdDepartamento: Optional[str]


class DistrictSearch(BaseModel):
    DisaCodigo: Optional[int]
    IdDepartamento: Optional[str]
    IdProvincia: Optional[str]


class DistrictPointSearch(EessPointSearch):
    pass


EesssRead = List[EessRead]
EessPointsRead = List[EessPointRead]
