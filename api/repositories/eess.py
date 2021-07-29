from fastapi.responses import JSONResponse
from ..models.eess import (
    EessRead,
    EessCreate,
    EessUpdate,
    EessSearch,
    EessBase,
    ProvincePointSearch,
    DistrictPointSearch,
    ProvinceSearch,
    DistrictSearch,
    DepartmentsList,
    ProvincesList,
    DistrictsList,
)

from ..models.department import Department

from ..models.point import (
    PointSearch,
    DepartmentPoints,
    ProvincePoints,
    DistrictPoints,
    EessPoints,
)
from ..schemas.eess import (
    pointsEntity,
    eessEntity,
    departmentPointsEntity,
    provincePointsEntity,
    districtPointsEntity,
    departmentEntity,
)
from ..database import (
    eess_collections as collection,
    eess_base_collections as collection_base,
)
from ..exceptions.exception import EessNotFoundException


class EessRespository:
    @staticmethod
    def search(search: EessSearch):
        """Retrieve a single EESS by its unique code"""
        document = collection_base.find_one({"code": search.FiltroValor},
                                            {'_id': 0})
        if not document:
            raise EessNotFoundException(search.FiltroValor)

        return {
            "IdLocal": document["code"],
            "NombreLocal": document["name"],
            "DireccionLocal": document["address"],
            "LatitudLocal": document["latitude"],
            "LongitudLocal": document["longitude"],
            "Capacidad": 0,
            "CapacidadDias": 0,
            "PoblacionObjetivo": 0,
            "RangoEdadInicial": 0,
            "RangoEdadFinal": 0,
            "DepartamentoNombreLocal": document["department"]["name"],
            "ProvinciaNombreLocal": document["province"]["name"],
            "DistritoNombreLocal": document["district"]["name"],
            "HorarioLocal": document["business_hours"],
            "Institucion": document["institution"],
            "TelefonoLocal": document["phone"],
            "Categoria": document["category"],
            "FiltroTipo": 0
        }

    @staticmethod
    def getById(eess_id: str) -> EessRead:
        """Retrieve a single EESS by its unique ID"""
        document = collection.find_one({"_id": eess_id})
        if not document:
            raise EessNotFoundException(eess_id)
        return EessRead(**document)

    @staticmethod
    def list() -> EessRead:
        """Retrieve all available EESS points"""
        cursor = collection.find()
        return [EessRead(**document) for document in cursor]

    @staticmethod
    def create(create: EessCreate) -> EessRead:
        """Create a EESS point and return its read object"""
        document = create.dict()
        result = collection.insert_one(document)
        assert result.acknowledged
        return EessRespository.getById(result.inserted_id)

    @staticmethod
    def getEessById(eess_id: str) -> EessRead:
        """Retrieve a single EESS by its unique ID"""
        document = collection_base.find_one({"_id": eess_id})
        if not document:
            raise EessNotFoundException(eess_id)
        return EessRead(**document)

    @staticmethod
    def eessCreate(create: EessBase) -> EessRead:
        """Create a EESS point and return its read object"""
        document = create.dict()
        result = collection_base.insert_one(document)
        assert result.acknowledged

        return EessRespository.getEessById(result.inserted_id)

    @staticmethod
    def listEess():
        """Retrieve all available EESS points"""
        return pointsEntity(collection_base.find())

    @staticmethod
    def listDepartments(disa_codigo: int):
        """Retrieve all available EESS points"""
        fields = {
            "department": 1,
            "_id": 0,
        }
        eess = collection_base.find({}, fields)
        departments = [
            DepartmentsList(IdDepartamento=row["department"]["code"],
                            NombDep=row["department"]["name"],
                            DisaCodigo=0) for row in eess
        ]
        return departments

    @staticmethod
    def listProvinces(search: ProvinceSearch):
        """Retrieve all available EESS points"""
        fields = {
            "province": 1,
            "_id": 0,
        }
        eess = collection_base.find({}, fields)
        departments = [
            ProvincesList(IdProvincia=row["province"]["code"],
                          NombProv=row["province"]["name"],
                          DisaCodigo=0) for row in eess
        ]
        return departments

    @staticmethod
    def listDistricts(search: DistrictSearch):
        """Retrieve all available EESS points"""
        fields = {
            "district": 1,
            "_id": 0,
        }
        eess = collection_base.find({}, fields)
        departments = [
            DistrictsList(IdDistrito=row["district"]["code"],
                          NombDis=row["district"]["name"],
                          DisaCodigo=0) for row in eess
        ]
        return departments

    @staticmethod
    def listEessPoints(search: PointSearch) -> EessPoints:
        """Retrieve all available EESS points"""
        fields = {
            "code": 1,
            "latitude": 1,
            "longitude": 1,
            "_id": 0,
        }
        eess = collection_base.find({}, fields)
        eess_points = [
            EessPoints(Total=0,
                       IdLocal=row["code"],
                       Latitud=row["latitude"],
                       Longitud=row["longitude"]) for row in eess
        ]
        return eess_points

    @staticmethod
    def listDepartmentPoints(department_code: str) -> DepartmentPoints:
        """Retrieve all available Departments points"""
        fields = {
            "department.code": 1,
            "code": 1,
            "latitude": 1,
            "longitude": 1,
            "_id": 0,
        }
        if department_code != "00":
            # eess = collection_base.find(
            #     {"department.code": department_code},
            #     fields,
            # )
            eess = collection_base.aggregate([
                {
                    "$match": {
                        "department.code": department_code
                    },
                },
                {
                    "$group": {
                        "_id": "$department.code",
                        "department": {
                            "$first": "$department.code"
                        },
                        "code": {
                            "$first": "$code"
                        },
                        "total": {
                            "$sum": 1
                        },
                        "latitude": {
                            "$first": "$latitude"
                        },
                        "longitude": {
                            "$first": "$longitude"
                        },
                    },
                },
            ])
        else:
            # eess = collection_base.find({}, fields)
            eess = collection_base.aggregate([
                {
                    "$group": {
                        "_id": "$department.code",
                        "department": {
                            "$first": "$department.code"
                        },
                        "code": {
                            "$first": "$code"
                        },
                        "total": {
                            "$sum": 1
                        },
                        "latitude": {
                            "$first": "$latitude"
                        },
                        "longitude": {
                            "$first": "$longitude"
                        },
                    },
                },
            ])
        department_points = [
            DepartmentPoints(IdDepartamento=row["department"],
                             Total=row["total"],
                             IdLocal=row["code"],
                             Latitud=row["latitude"],
                             Longitud=row["longitude"]) for row in eess
        ]
        return department_points

    @staticmethod
    def listProvincePoints(search: ProvincePointSearch) -> ProvincePoints:
        """Retrieve all available Provinces potins"""
        fields = {
            "department.code": 1,
            "province.code": 1,
            "code": 1,
            "latitude": 1,
            "longitude": 1,
            "_id": 0,
        }
        eess = collection_base.aggregate([
            {
                "$group": {
                    "_id": "$department.code",
                    "department": {
                        "$first": "$department.code"
                    },
                    "province": {
                        "$first": "$province.code"
                    },
                    "code": {
                        "$first": "$code"
                    },
                    "total": {
                        "$sum": 1
                    },
                    "latitude": {
                        "$first": "$latitude"
                    },
                    "longitude": {
                        "$first": "$longitude"
                    },
                },
            },
        ])
        province_points = [
            ProvincePoints(IdDepartamento=row["department"],
                           IdProvincia=row["province"],
                           Total=row["total"],
                           IdLocal=row["code"],
                           Latitud=row["latitude"],
                           Longitud=row["longitude"]) for row in eess
        ]
        return province_points

    @staticmethod
    def listDistrictPoints(search: DistrictPointSearch) -> DistrictPoints:
        """Retrieve all available Districts points"""
        fields = {
            "department.code": 1,
            "province.code": 1,
            "district.code": 1,
            "code": 1,
            "latitude": 1,
            "longitude": 1,
            "_id": 0,
        }
        # eess = collection_base.find({}, fields)
        eess = collection_base.aggregate([
            {
                "$group": {
                    "_id": "$department.code",
                    "department": {
                        "$first": "$department.code"
                    },
                    "province": {
                        "$first": "$province.code"
                    },
                    "district": {
                        "$first": "$district.code"
                    },
                    "code": {
                        "$first": "$code"
                    },
                    "total": {
                        "$sum": 1
                    },
                    "latitude": {
                        "$first": "$latitude"
                    },
                    "longitude": {
                        "$first": "$longitude"
                    },
                },
            },
        ])
        district_points = [
            DistrictPoints(IdDepartamento=row["department"],
                           IdProvincia=row["province"],
                           IdDistrito=row["district"],
                           Total=row["total"],
                           IdLocal=row["code"],
                           Latitud=row["latitude"],
                           Longitud=row["longitude"]) for row in eess
        ]
        return district_points
