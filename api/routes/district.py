from fastapi import APIRouter
from fastapi import status as statuscode

from api.repositories.district import DistrictRepository

from ..models.district import (
    DistrictsRead,
    DistrictRead,
    DistrictCreate,
    DistrictUpdate,
)

__all__ = ("router")

router = APIRouter()


@router.get("/districts",
            response_model=DistrictsRead,
            description="List all available districts",
            tags=["districts"])
def list_districts():
    return DistrictRepository.list()


@router.get(
    "/api/districts/{department_code}/department/{province_code}/province", )
@router.get(
    "/districts/{department_code}/department/{province_code}/province",
    response_model=DistrictsRead,
    description="List all available districts by department and province code",
    tags=["districts"])
def list_districts_by_department_and_province_code(department_code: str,
                                                   province_code: str):
    _districts = []
    districts = DistrictRepository.getByDepartmentAndProvinceCode(
        department_code, province_code)
    for district in districts:
        _districts.append({
            "IdDistrito": district.code,
            "NombDis": district.name,
        })
    return {"Data": _districts}
