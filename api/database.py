from pymongo import MongoClient
from pymongo.collection import Collection

from .settings import mongo_settings as settings

__all__ = (
    "client",
    "department_collections",
    "province_collections",
    "district_collections",
    "department_collections_point",
    "province_collections_point",
    "district_collections_point",
    "eess_collections",
    "point_collections",
)

client = MongoClient(settings.uri)

department_collections: Collection = client[settings.database][
    settings.department_collections]

province_collections: Collection = client[settings.database][
    settings.province_collections]

district_collections: Collection = client[settings.database][
    settings.district_collections]

department_collections_point: Collection = client[settings.database][
    settings.department_collections_point]

province_collections_point: Collection = client[settings.database][
    settings.province_collections_point]

district_collections_point: Collection = client[settings.database][
    settings.district_collections_point]

eess_collections: Collection = client[settings.database][
    settings.eess_collections]
eess_base_collections: Collection = client[settings.database][
    settings.eess_base_collections]
point_collections: Collection = client[settings.database][
    settings.point_collections]
