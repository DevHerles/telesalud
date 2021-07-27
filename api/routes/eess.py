from fastapi import APIRouter
from fastapi import status as statuscode

from api.repositories.eess import EessRespository
from ..models.eess import (
    EesssRead,
    EessRead,
    EessCreate,
    EessUpdate,
    EessSearch,
    EessPointsRead,
    EessPointSearch,
)
from ..models.point import (PointSearch, PointsRead)
__all__ = ("router")

router = APIRouter()


@router.post(
    '/api/CentroVacunacionGis/Buscar',
    description="Get a EESS by its unique ID",
    tags=["points"],
)
def search_eess_point(data: EessSearch):
    return {"Data": [EessRespository.search(data)]}


@router.post(
    '/api/CentroVacunacionGis/Puntos',
    description="Get all available EESS locations",
    # response_model=EessPointsRead,
    tags=["demo"],
)
def listEessPoints(data: EessPointSearch):
    return {"Data": EessRespository.listEessPoints()}
