import json
from jsonschema import validate


def validate_json(instance, schema):
    try:
        validate(json.loads(instance), json.loads(schema))
        return True
    except Exception as ex:
        print(ex)
        return False
