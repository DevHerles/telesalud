from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status as statuscode

from api.models.department import (
    DepartmentsRead,
    DepartmentRead,
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentPoint,
    DepartmentsPoint,
)
from api.models.province import (
    ProvincesRead,
    ProvinceRead,
    ProvinceCreate,
    ProvinceUpdate,
)
from api.models.district import (
    DistrictsRead,
    DistrictRead,
    DistrictCreate,
    DistrictUpdate,
)
from api.models.province import Province
from api.models.district import District

from api.repositories.department import DepartmentRepository
from api.repositories.province import ProvinceRepository
from api.repositories.district import DistrictRepository

from api.exceptions.exception import (
    DepartmentAlreadyExistsException,
    DepartmentNotFoundException,
    get_exception_responses,
)
from api.settings import api_settings as settings

app = FastAPI(title=settings.title)

origins = [
    'https://localhost:3000',
    'http://localhost:11501',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return "(C) MINSA - 2021"


@app.get(
    "/departments/points/{code}",
    description="List all available department points filtered by code",
    tags=["points"],
)
def list_department_points_by_code(code: str):
    departments = DepartmentRepository.getPointsByCode(code)
    return departments


@app.get(
    "/api/departments/points",
    description="List all available department points",
    tags=["points"],
)
def list_department_points():
    departments = DepartmentRepository.getPoints()
    return {"Data": departments}


@app.get("/api/Departamento/Listar")
@app.get(
    "/departments",
    response_model=DepartmentsRead,
    description="List all available departments",
    tags=["departments"],
)
def list_departments():
    _departments = []
    departments = DepartmentRepository.list()
    for department in departments:
        _departments.append({
            "IdDepartamento": department.code,
            "NombDep": department.name,
        })
    return {"Data": _departments}


@app.post(
    "/departments",
    description="Create a new department",
    response_model=DepartmentRead,
    status_code=statuscode.HTTP_201_CREATED,
    responses=get_exception_responses(DepartmentAlreadyExistsException),
    tags=["departments"],
)
def create_department(create: DepartmentCreate):
    return DepartmentRepository.create(create)


@app.patch(
    "/departments/{code}",
    description="Update a single department by its unique code, providing the fields to update",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(
        DepartmentNotFoundException,
        DepartmentAlreadyExistsException,
    ),
    tags=["departments"],
)
def update_department(code: str, update: DepartmentUpdate):
    DepartmentRepository.update(code, update)


@app.delete(
    "/departments/{code}",
    description="Delete a single department by its unique code",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(DepartmentNotFoundException),
    tags=["departments"],
)
def delete_department(code: str):
    DepartmentRepository.delete(code)


@app.get("/api/Provincia/Listar")
@app.get(
    "/provinces",
    response_model=ProvincesRead,
    description="List all available provinces",
    tags=["provinces"],
)
def list_provinces():
    return ProvinceRepository.list()


@app.get(
    "/provinces/{code}",
    response_model=ProvinceRead,
    description="Get a unique province by code",
    tags=["provinces"],
)
def get_province(code: str):
    return ProvinceRepository.getByCode(code)


@app.get("/api/provinces/{code}/department")
@app.get(
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


@app.get("/districts",
         response_model=DistrictsRead,
         description="List all available districts",
         tags=["districts"])
def list_districts():
    return DistrictRepository.list()


@app.get(
    "/api/districts/{department_code}/department/{province_code}/province", )
@app.get(
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
