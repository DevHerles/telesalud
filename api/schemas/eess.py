def pointEntity(item) -> dict:
    return {
        'Total': 0,
        'IdLocal': item['code'],
        'Latitud': item['latitude'],
        'Longitud': item['longitude'],
    }


def pointsEntity(entity) -> list:
    return [pointEntity(item) for item in entity]


def eessEntity(item) -> dict:
    return {
        "IdLocal": item["code"],
        "NombreLocal": item["name"],
        "DireccionLocal": item["address"],
        "LatitudLocal": item["latitude"],
        "LongitudLocal": item["longitude"],
        "Capacidad": 0,
        "CapacidadDias": 0,
        "PoblacionObjetivo": 0,
        "RangoEdadInicial": 0,
        "RangoEdadFinal": 0,
        "DepartamentoNombreLocal": item["department"],
        "ProvinciaNombreLocal": item["province"],
        "DistritoNombreLocal": item["district"],
        "HorarioLocal": item["business_hours"],
        "Institucion": item["institution"],
        "TelefonoLocal": item["phone"],
        "Categoria": item["category"],
        "FiltroTipo": 0
    }
