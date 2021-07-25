from ..models.point import (
    PointRead,
    PointCreate,
    PointUpdate,
    PointsRead,
)

from ..database import (
    point_collections as collection, )
from ..exceptions.exception import PointNotFoundException


class PointRepository:
    @staticmethod
    def getById(point_id: str) -> PointRead:
        """Retrieve a single Point by its unique ID"""
        document = collection.find_one({"_id": point_id})
        if not document:
            raise PointNotFoundException(point_id)
        return PointRead(**document)

    @staticmethod
    def list() -> PointRead:
        """Retrieve all available Points"""
        _points = []
        cursor = collection.find({}, {"_id": 0})
        # for document in cursor:
        #     print(document)
        return [PointRead(**document) for document in cursor]

    @staticmethod
    def create(create: PointCreate) -> PointRead:
        """Create a Point and return its read object"""
        document = create.dict()
        result = collection.insert_one(document)
        assert result.acknowledged
        return PointRepository.getById(result.inserted_id)
