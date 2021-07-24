from pydantic import Field

_string = dict(min_length=2)
"""Common attributes for all String fields"""


class DepartmentFields:
    code = Field(description="Department code", example="01", **_string)
    name = Field(description="Department name", example="AMAZONAS", **_string)
    total = Field(description="Total", example=20)
