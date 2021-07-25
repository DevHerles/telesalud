from fastapi import APIRouter
from fastapi import status as statuscode

from api.repositories.eess import EessRespository
from ..models.eess import (
    EesssRead,
    EessRead,
    EessCreate,
    EessUpdate,
    EessSearch,
)

__all__ = ("router")

router = APIRouter()


@router.post('/api/CentroVacunacionGis/Buscar',
             description="Get a EESS by its unique ID",
             tags=["points"])
def search_eess_point(data: EessSearch):
    return {"Data": [EessRespository.search(data)]}
