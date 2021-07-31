from pydantic import Field


class EessFields:
    code = Field(description="EESS code", example="010101")
    name = Field(description="EESS name", example="ESTADO PACHACAMAC")
    address = Field(
        description="EESS address",
        example="""Carretera Central Km 20 A 3 Cuadras Del Cmi Miguel Grau, Chaclacayo"""
    )
    institution = Field(description="EESS institution", example="MINSA")
    institution_code = Field(description="EESS institution code", example="01")
    category = Field(description="EESS Category", example="I-2")
    department = Field(description="EESS Department", example="LIMA")
    department_code = Field(description="Department code", example="15")
    province = Field(description="EESS Province", example="LIMA")
    province_code = Field(description="Province code", example="01")
    district = Field(description="EESS District", example="CHACLACAYO")
    district_code = Field(description="District code", example="01")
    latitude = Field(description="EESS latitude", example=-11.9847789)
    longitude = Field(description="EESS longitude", example=-76.809623251)
    business_hours = Field(description="EESS business hours",
                           example="07:00 AM - 07:00 PM")
    phone = Field(description="EESS phone number", example="93913428")
