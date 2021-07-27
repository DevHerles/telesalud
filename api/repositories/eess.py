from ..models.eess import (
    EessRead,
    EessCreate,
    EessUpdate,
    EessSearch,
)

from ..models.point import (PointRead)
from ..schemas.eess import pointsEntity, eessEntity
from ..database import (
    eess_collections as collection, )
from ..exceptions.exception import EessNotFoundException


class EessRespository:
    @staticmethod
    def search(search: EessSearch) -> EessRead:
        """Retrieve a single EESS by its unique ID"""
        print(search.FiltroValor)
        document = eessEntity(
            collection.find_one({"code": int(search.FiltroValor)}, {'_id': 0}))
        if not document:
            raise EessNotFoundException(search.FiltroValor)
        return document

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
    def listEessPoints() -> PointRead:
        """Retrieve all available EESS points"""
        return pointsEntity(collection.find())
