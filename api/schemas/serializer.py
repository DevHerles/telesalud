def serializerDict(key) -> dict:
    return {
        **{value: str(key[value])
           for value in key if value == '_id'},
        **{value: key[value]
           for value in key if value != '_id'}
    }


def serializerList(entity) -> list:
    return [serializerDict(key) for key in entity]
