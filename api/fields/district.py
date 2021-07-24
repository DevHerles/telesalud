from pydantic import Field

_string = dict(min_length=2)
"""Common attributes for all String fields"""


class DistrictFields:
    code = Field(description="District code", example="010101", **_string)
    name = Field(description="District name", example="BAGUA", **_string)
