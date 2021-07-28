import pydantic

__all__ = (
    "api_settings",
    "mongo_settings",
)


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "Mapas - Telesalud"
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class MongoSettings(BaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = "mapas_telesalud"
    department_collections: str = "departments"
    province_collections: str = "provinces"
    district_collections: str = "districts"
    department_collections_point: str = "departments_point"
    province_collections_point: str = "provinces_point"
    district_collections_point: str = "districts_point"
    eess_collections: str = "eess"
    eess_base_collections: str = "eess_base"
    point_collections: str = "points"

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


api_settings = APISettings()
mongo_settings = MongoSettings()
