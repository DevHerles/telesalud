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


def districtPointEntity(item) -> dict:
    return {
        "IdDepartmento": item["department"],
        "IdProvincia": item["province"],
        "IdDistrito": item["district"],
        "Total": 0,
        "IdLocal": item["code"],
        "Latitud": item["latitude"],
        "Longitud": item["longitude"]
    }


def districtPointsEntity(entity) -> list:
    return [districtPointEntity(item) for item in entity]


def provincePointEntity(item) -> dict:
    return {
        "IdDepartmento": item["department"],
        "IdProvincia": item["province"],
        "Total": 0,
        "IdLocal": item["code"],
        "Latitud": item["latitude"],
        "Longitud": item["longitude"]
    }


def provincePointsEntity(entity) -> list:
    return [provincePointEntity(item) for item in entity]


def departmentPointEntity(item) -> dict:
    return {
        "IdDepartmento": item["department"],
        "Total": 0,
        "IdLocal": item["code"],
        "Latitud": item["latitude"],
        "Longitud": item["longitude"]
    }


def departmentPointsEntity(entity) -> list:
    return [departmentPointEntity(item) for item in entity]


def departmentEntity(item) -> dict:
    print(item)
    print("xxxxxx")
    return {
        "IdDepartmento": item["department"]["code"],
        "NombDep": item["department"]["name"],
        "DisaCodigo": 0
    }


def departmentEntityList(entity) -> list:
    return [departmentEntity(item) for item in entity]
