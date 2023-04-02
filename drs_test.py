import requests
import re
import json
import sys
from jsonschema import validate

# api-endpoint
URL = "http://localhost:5000/ga4gh/drs/v1/objects/"


def regex_test(obj_id):
    test_name = "Regex for object_id validity"

    if re.match(r"^[A-Za-z0-9\.\-_~]+$", obj_id):
        message = "valid object_id"
        pass_status = True
    else:
        message = "Invalid object_id"
        pass_status = False


    output = {
        "object_id": obj_id,
        "test_name": test_name,
        "pass": pass_status,
        "message": message
    }

    output_json = json.dumps(output)
    print(output_json)

def objID_existance(response):
    test_name = "Test for DRS object existance"
    status_code = response.status_code

    if status_code==200:
        message = "DRS object found"
        pass_status = True
    elif status_code==404:
        message = "DRS object not found"
        pass_status = False
    else:
        message = f"status code {status_code} error happened"
        pass_status = False


    output = {
        "object_id": obj_id,
        "test_name": test_name,
        "pass": pass_status,
        "message": message
    }

    output_json = json.dumps(output)
    print(output_json)

def schema_test(response):
    test_name = "Test for response schema"

    schema_for_200 = {
        "type" : "object",
        "properties": {
            "id" : {"type" : "string"},
            "description" : {"type" : "string"},
            "created_time": {"type" : "string"},
            "mime_type": {"type" : "string"},
            "name": {"type" : "string"},
            "size": {"type" : "integer"},
            "updated_time": {"type" : "string"},
            "version": {"type" : "string"},
            "aliases": {},
            "checksums": {},
            "contents":{},
            "self_uri": {"type" : "string"},
            "access_methods": {},
        },
        "required": ["id", "description", "created_time", "mime_type", "name", "size", "updated_time", "version", "aliases", "checksums", "self_uri", "access_methods"]
    }

    schema_for_others = {
        "type" : "object",
        "properties": {
            "msg": {"type" : "string"},
            "status_code": {"type" : "integer"}
        },
        "required": ["msg","status_code"]
    }
    data = response.json()
    status_code = response.status_code;
    if status_code == 200:
        try:
            validate(instance=data, schema=schema_for_200)
            pass_status = True
            message = "valid 200 response"
        except:
            pass_status = False
            message = "invalid 200 response"
    else:
        try:
            validate(instance=data, schema=schema_for_others)
            pass_status = True
            message = f"valid {status_code} response"
        except:
            pass_status = False
            message = f"invalid {status_code} response"

    output = {
        "object_id": obj_id,
        "test_name": test_name,
        "pass": pass_status,
        "message": message
    }
    output_json = json.dumps(output)
    print(output_json)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide object ID")
        sys.exit(1)
    obj_id = sys.argv[1]
    response = requests.get(URL+obj_id)
    regex_test(obj_id)
    objID_existance(response)
    schema_test(response)
