from ..models.province import (
    ProvinceRead,
    ProvinceCreate,
    ProvinceUpdate,
)
from ..database import province_collections as collection
from ..exceptions.exception import ProvinceNotFoundException


class ProvinceRepository:
    @staticmethod
    def getByCode(code: str) -> ProvinceRead:
        """Retrieve a single Province by its unique code"""
        document = collection.find_one({"code": code})
        if not document:
            raise ProvinceNotFoundException(code)
        return ProvinceRead(**document)

    @staticmethod
    def getById(province_id: str) -> ProvinceRead:
        """Retrieve a single Province by its unique ID"""
        document = collection.find_one({"_id": province_id})
        if not document:
            raise ProvinceNotFoundException(province_id)
        return ProvinceRead(**document)

    @staticmethod
    def getByDepartmentCode(code: str) -> ProvinceRead:
        """Retrieve all the available provinces filtered by department code"""
        cursor = collection.find({
            "department_code": code
        }).sort([
            ("code", 1),
        ])
        return [ProvinceRead(**document) for document in cursor]

    @staticmethod
    def list() -> ProvinceRead:
        """Retrieve all the available provinces"""
        cursor = collection.find().sort([
            ("code", 1),
        ])
        return [ProvinceRead(**document) for document in cursor]

    @staticmethod
    def create(create: ProvinceCreate) -> ProvinceRead:
        """Create a province and return its read object"""
        document = create.dict()
        result = collection.insert_one(document)
        assert result.acknowledged
        return ProvinceRepository.getById(result.inserted_id)

    @staticmethod
    def update(code: str, update: ProvinceUpdate):
        """Update a province by giving only the fields to update"""
        document = update.dict()
        result = collection.update_one(
            {"code": code},
            {"$set": document},
        )
        if not result.modified_count:
            raise ProvinceNotFoundException(identifier=code)

    @staticmethod
    def delete(code: str):
        """Delete a province given its unique code"""
        result = collection.delete_one({"code": code})
        if not result.deleted_count:
            raise ProvinceNotFoundException(identifier=code)
