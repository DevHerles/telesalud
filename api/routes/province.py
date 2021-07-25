from fastapi import APIRouter
from fastapi import status as statuscode

from api.repositories.province import ProvinceRepository
from ..models.province import (
    ProvincesRead,
    ProvinceRead,
    ProvinceCreate,
    ProvinceUpdate,
)
__all__ = ("router")

router = APIRouter()


@router.get("/api/Provincia/Listar")
@router.get(
    "/provinces",
    response_model=ProvincesRead,
    description="List all available provinces",
    tags=["provinces"],
)
def list_provinces():
    return ProvinceRepository.list()


@router.get(
    "/provinces/{code}",
    response_model=ProvinceRead,
    description="Get a unique province by code",
    tags=["provinces"],
)
def get_province(code: str):
    return ProvinceRepository.getByCode(code)


@router.get("/api/provinces/{code}/department")
@router.get(
    "/provinces/{code}/department",
    response_model=ProvincesRead,
    description="List all available province by department code",
    tags=["provinces"],
)
def get_provinces_by_department_code(code: str):
    _provinces = []
    provinces = ProvinceRepository.getByDepartmentCode(code)
    for province in provinces:
        _provinces.append({
            "IdProvincia": province.code,
            "NombProv": province.name,
        })
    return {"Data": _provinces}
