from ..models.district import (
    DistrictRead,
    DistrictCreate,
    DistrictUpdate,
)
from ..database import district_collections as collection
from ..exceptions.exception import DistrictNotFoundException


class DistrictRepository:
    @staticmethod
    def getByCode(code: str) -> DistrictRead:
        """Retrieve a single District by its unique code"""
        document = collection.find_one({"code": code})
        if not document:
            raise DistrictNotFoundException(code)
        return DistrictRead(**document)

    def getById(district_id: str) -> DistrictRead:
        """Retrieve a single District by its unique ID"""
        document = collection.find_one({"_id": district_id})
        if not document:
            raise DistrictNotFoundException(district_id)
        return DistrictRead(**document)

    @staticmethod
    def getByDepartmentAndProvinceCode(department_code: str,
                                       province_code: str) -> DistrictRead:
        """Retrieve all the available districts filtered by province and department code"""
        cursor = collection.find({
            "department_code": department_code,
            "province_code": province_code,
        }).sort([
            ("code", 1),
        ])
        return [DistrictRead(**document) for document in cursor]

    @staticmethod
    def list() -> DistrictRead:
        """Retrieve all the available districts"""
        cursor = collection.find().sort([
            ("code", 1),
        ])
        return [DistrictRead(**document) for document in cursor]

    @staticmethod
    def create(create: DistrictCreate) -> DistrictRead:
        """Create a district and return its read object"""
        document = create.dict()
        result = collection.insert_one(document)
        assert result.acknowledged
        return DistrictRepository.getById(result.inserted_id)

    @staticmethod
    def update(code: str, update: DistrictUpdate):
        """Update a district by givin only the fields to update"""
        document = update.dict()
        result = collection.update_one(
            {"code": code},
            {"$set": document},
        )
        if not result.modified_count:
            raise DistrictNotFoundException(identifier=code)

    @staticmethod
    def delete(code: str):
        """Delete a district given its unique code"""
        result = collection.delete_one({"code": code})
        if not result.deleted_count:
            raise DistrictNotFoundException(identifier=code)
