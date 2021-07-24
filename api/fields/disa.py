from pydantic import Field

_string = dict(min_length=2)
"""Common attributes for all String fields"""


class DisaFields:
    code = Field(description="DISA code", example=1)
    name = Field(description="DISA name", example="DISA")
