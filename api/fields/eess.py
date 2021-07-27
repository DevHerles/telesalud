from pydantic import Field


class EessFields:
    IdLocal = Field(description="EESS code", example="010101")
    NombreLocal = Field(description="EESS name", example="ESTADO PACHACAMAC")
    DireccionLocal = Field(
        description="EESS address",
        example="Carretera Central Km 20 A 3 Cuadras Del Cmi Miguel Grau, Chaclacayo")
    LatitudLocal = Field(description="EESS latitude", example=-11.9847789)
    LongitudLocal = Field(description="EESS longitude", example=-76.809623251)
    DepartamentoNombreLocal = Field(description="EESS Department",
                                    example="LIMA")
    ProvinciaNombreLocal = Field(description="EESS Province", example="LIMA")
    DistritoNombreLocal = Field(description="EESS District",
                                example="CHACLACAYO")
    HorarioLocal = Field(description="EESS business hours",
                         example="07:00 AM - 07:00 PM")
    TelefonoLocal = Field(description="EESS phone number", example="93913428")

    code = Field(description="EESS code", example="010101")
    name = Field(description="EESS name", example="ESTADO PACHACAMAC")
    address = Field(description="EESS address",
                    example="""Carretera Central Km 20
                            A 3 Cuadras Del Cmi Miguel Grau, Chaclacayo""")
    institution = Field(description="EESS institution", example="MINSA")
    category = Field(description="EESS Category", example="I-2")
    department = Field(description="EESS Department", example="LIMA")
    province = Field(description="EESS Province", example="LIMA")
    district = Field(description="EESS District", example="CHACLACAYO")
    latitude = Field(description="EESS latitude", example=-11.9847789)
    longitude = Field(description="EESS longitude", example=-76.809623251)
    business_hours = Field(description="EESS business hours",
                           example="07:00 AM - 07:00 PM")
    phone = Field(description="EESS phone number", example="93913428")
