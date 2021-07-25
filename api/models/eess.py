from typing import List, Optional
import pydantic

from ..models.common import BaseModel
from ..fields.eess import EessFields

__all__ = (
    "EessUpdate",
    "EessRead",
    "EessCreate",
    "EesssRead",
)


class EessCreate(BaseModel):
    IdLocal: int = EessFields.IdLocal
    NombreLocal: str = EessFields.NombreLocal
    DireccionLocal: str = EessFields.DireccionLocal
    LatitudLocal: float = EessFields.LatitudLocal
    LongitudLocal: float = EessFields.LongitudLocal
    DepartamentoNombreLocal: str = EessFields.DepartamentoNombreLocal
    ProvinciaNombreLocal: str = EessFields.ProvinciaNombreLocal
    DistritoNombreLocal: str = EessFields.DistritoNombreLocal
    HorarioLocal: str = EessFields.HorarioLocal
    TelefonoLocal: str = EessFields.TelefonoLocal


class EessRead(EessCreate):
    pass


class EessUpdate(EessCreate):
    pass


class EessSearch(BaseModel):
    FiltroTipo: int
    FiltroValor: str


EesssRead = List[EessRead]
