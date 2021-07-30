from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import status as statuscode
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from ..exceptions.exception import EessNotFoundException
from api.repositories.eess import EessRespository
from ..models.eess import (
    EesssRead,
    EessRead,
    EessCreate,
    EessUpdate,
    EessSearch,
    EessPointsRead,
    EessPointSearch,
    ProvincePointSearch,
    DistrictPointSearch,
    EessBase,
    ProvinceSearch,
    DistrictSearch,
)
from ..models.point import (PointSearch)
__all__ = ("router")

router = APIRouter()


class ResponseValue(BaseModel):
    message: str


class APIResponse():
    @staticmethod
    def error(value: ResponseValue):
        return {
            "Data": {
                "message": value.message,
                "Success": False,
            }
        }

    @staticmethod
    def success(value: list):
        return {
            "Data": value,
            "Success": True,
        }


@router.post(
    '/api/CentroVacunacionGis/Buscar',
    description="Get a EESS by its unique ID",
    tags=["points"],
)
def search_eess_point(data: EessSearch):
    try:
        return APIResponse.success([EessRespository.search(data)])
    except EessNotFoundException as identifier:
        response = APIResponse.error(
            ResponseValue(message=identifier.message, ))
        return JSONResponse(content=response, status_code=404)


@router.post(
    '/api/CentroVacunacionGis/Puntos',
    description="Get all available EESS locations",
    # response_model=EessPointsRead,
    tags=["demo"],
)
def listEessPoints(search: EessPointSearch):
    return {"Data": EessRespository.listEessPoints(search)}


@router.post(
    "/api/CentroVacunacionGis/DepartamentoPuntos",
    tags=["layers"],
)
def listDepartmentPoints(department_code: str = "00"):
    return {"Data": EessRespository.listDepartmentPoints(department_code)}


@router.post(
    "/api/CentroVacunacionGis/ProvinciasPuntos",
    tags=["layers"],
)
def listProvincePoints(search: ProvincePointSearch):
    return {"Data": EessRespository.listProvincePoints(search)}


@router.post(
    "/api/CentroVacunacionGis/DistritosPuntos",
    tags=["layers"],
)
def listDistrictPoints(search: DistrictPointSearch):
    return {"Data": EessRespository.listDistrictPoints(search)}


@router.post(
    "/api/eess",
    tags=["EESS"],
)
def postEess(eess: EessBase):
    return EessRespository.eessCreate(eess)


@router.post(
    "/api/CentroVacunacionGis/Puntos",
    tags=["layers"],
)
def listEess(search: PointSearch):
    return EessRespository.listEessPoints(search)


@router.post(
    "/api/Departamento/Listar",
    tags=["list"],
)
def listDepartments(disa_codigo: int = 0):
    return {"Data": EessRespository.listDepartments(disa_codigo)}


@router.post(
    "/api/Provincia/Listar",
    tags=["list"],
)
def listProvinces(search: ProvinceSearch):
    return {"Data": EessRespository.listProvinces(search)}


@router.post(
    "/api/Distrito/Listar",
    tags=["list"],
)
def listDistricts(search: DistrictSearch):
    return {"Data": EessRespository.listDistricts(search)}
