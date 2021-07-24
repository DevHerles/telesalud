from ..models.department import (
    DepartmentRead,
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentPoint,
    DepartmentPointRead,
)
from ..database import (
    department_collections as collection,
    department_collections_point as collection_points,
)
from ..exceptions.exception import DepartmentNotFoundException


class DepartmentRepository:
    @staticmethod
    def getPointsByCode(code: str) -> DepartmentPointRead:
        """Retrieve all the available departments point"""
        _departments = []
        cursor = collection_points.find({
            "IdDepartamento": code
        }).sort([("IdDepartamento", 1)])
        for document in cursor:
            document.pop("_id")
            _departments.append(document)
        return {"Data": _departments}

    @staticmethod
    def getPoints() -> DepartmentPointRead:
        """Retrieve all the available departments point"""
        cursor = collection_points.find({}, {
            "_id": 0
        }).sort([("IdDepartamento", 1)])
        return [DepartmentPointRead(**document) for document in cursor]

    @staticmethod
    def getByCode(code: str) -> DepartmentRead:
        """Retrieve a single Department by its code"""
        document = collection.find_one({"code": code})
        if not document:
            raise DepartmentNotFoundException(code)
        return DepartmentRead(**document)

    @staticmethod
    def getById(department_id: str) -> DepartmentRead:
        """Retrieve a single Department by its unique ID"""
        document = collection.find_one({"_id": department_id})
        if not document:
            raise DepartmentNotFoundException(department_id)
        return DepartmentRead(**document)

    @staticmethod
    def list() -> DepartmentRead:
        """Retrieve all the available departments"""
        cursor = collection.find().sort([("code", 1)])
        return [DepartmentRead(**document) for document in cursor]

    @staticmethod
    def create(create: DepartmentCreate) -> DepartmentRead:
        """Create a department and return its read object"""
        document = create.dict()
        result = collection.insert_one(document)
        assert result.acknowledged

        return DepartmentRepository.getById(result.inserted_id)

    @staticmethod
    def update(code: str, update: DepartmentUpdate):
        """Update a department by giving only the fields to udpate"""
        document = update.dict()
        result = collection.update_one(
            {"code": code},
            {"$set": document},
        )
        if not result.modified_count:
            raise DepartmentNotFoundException(identifier=code)

    @staticmethod
    def delete(code: str):
        """Delete a department given its unique code"""
        result = collection.delete_one({"code": code})
        if not result.deleted_count:
            raise DepartmentNotFoundException(identifier=code)
