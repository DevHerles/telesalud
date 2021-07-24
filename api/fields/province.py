from pydantic import Field

_string = dict(min_length=2)
"""Common attributes for all String fields"""


class ProvinceFields:
    code = Field(description="Province code", example="0101", **_string)
    name = Field(description="Province name", example="CHACHAPOYAS", **_string)
