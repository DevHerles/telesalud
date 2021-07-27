from fastapi import APIRouter
from fastapi import status as statuscode

from api.repositories.point import PointRepository
from ..schemas.point import (
    PointSearchEntity,
    PointsSearchEntity,
)

__all__ = ("router")

router = APIRouter()


@router.post(
    '/api/CentroVacunacionGis/Puntos',
    # response_model=PointsSearchEntity,
    description="List all available points",
    tags=["points"])
def list_points(data: PointSearchEntity):
    return {"Data": PointRepository.list()}
