from fastapi import APIRouter
from fastapi import status as statuscode

from api.repositories.point import PointRepository
from ..models.point import (
    PointRead,
    PointSearch,
)

__all__ = ("router")

router = APIRouter()


@router.post(
    '/api/CentroVacunacionGis/Puntos',
    # response_model=PointRead,
    description="List all available points",
    tags=["points"])
def list_points(data: PointSearch):
    return {"Data": PointRepository.list()}
