from pydantic import Field

_string = dict(min_length=2)
"""Common attributes for all String fields"""


class InstitucionFields:
    code = Field(description="Institution code", example="01", **_string)
    name = Field(description="Institution name", example="MINSA", **_string)
