from pydantic import Field


class LocationFields:
    latitude = Field(description="Latitude", example=-14.02813593)
    longitude = Field(description="Longitude", example=-72.9753793)
    total = Field(description="Total", example=10)
