from fastapi import APIRouter
from fastapi import status as statuscode
from ..models.department import (
    DepartmentsRead,
    DepartmentRead,
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentPoint,
    DepartmentsPoint,
)
from ..repositories.department import DepartmentRepository

from ..exceptions.exception import (
    DepartmentAlreadyExistsException,
    DepartmentNotFoundException,
    get_exception_responses,
)

__all__ = ("router")

router = APIRouter()


@router.get(
    "/departments/points/{code}",
    description="List all available department points filtered by code",
    tags=["points"],
)
def list_department_points_by_code(code: str):
    departments = DepartmentRepository.getPointsByCode(code)
    return departments


@router.get(
    "/api/departments/points",
    description="List all available department points",
    tags=["points"],
)
def list_department_points():
    departments = DepartmentRepository.getPoints()
    return {"Data": departments}


@router.get("/api/Departamento/Listar")
@router.get(
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


@router.post(
    "/departments",
    description="Create a new department",
    response_model=DepartmentRead,
    status_code=statuscode.HTTP_201_CREATED,
    responses=get_exception_responses(DepartmentAlreadyExistsException),
    tags=["departments"],
)
def create_department(create: DepartmentCreate):
    return DepartmentRepository.create(create)


@router.patch(
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


@router.delete(
    "/departments/{code}",
    description="Delete a single department by its unique code",
    status_code=statuscode.HTTP_204_NO_CONTENT,
    responses=get_exception_responses(DepartmentNotFoundException),
    tags=["departments"],
)
def delete_department(code: str):
    DepartmentRepository.delete(code)
