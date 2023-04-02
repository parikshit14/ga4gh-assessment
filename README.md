## Test Description
There are three basic test coverage in this repository:
1. **Test to validate whether the object_id entered is correct:**
 - According to the documentation [ref](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/#:~:text=follows%20these%20guidelines%3A-,DRS%20IDs,-are%20strings%20made) the allowed characters are [A-Za-z0-9.-_~]
 - This has been implemented using regular expression matching library re
 - Sample output:
    - Valid case `{"object_id": "xx18bfb64168994489bc9e7fda0acd4f", "test_name": "Regex for object_id validity", "pass": true, "message": "valid object_id"}`
    - Invalid case `{"object_id": "xx18bfb64168994489bc9e7fda0acd4f*dcdc", "test_name": "Regex for object_id validity", "pass": false, "message": "Invalid object_id"}`


2. **Test to check if the entered object_id exist in the Database:**
 - The reponse code received for the given object_id tells about the existance of that object_id's existance in the db
 - If response code is 404 then that particular object_id doesn't exist otherwise it exist
 - Sample output:
     - Valid case `{"object_id": "ecbb0b5131051c41f1c302287c13495c", "test_name": "Test for DRS object existance", "pass": true, "message": "DRS object found"}`
     - Invalid case `{"object_id": "xx18", "test_name": "Test for DRS object existance", "pass": false, "message": "DRS object not found"}`


3. **Test to check if Schema of response is correct or not:**
 - The reponse data passes throught a predefined schema which validates its correctness
 - The schemas are segregated into two main categories i.e. schema for 200 response code and schema for other response
 - Sample output:
     - Valid case for 200 `{"object_id": "ecbb0b5131051c41f1c302287c13495c", "test_name": "Test for response schema", "pass": true, "message": "valid 200 response"}`
     - Valid case for other response code `{"object_id": "xx18bfb64168994489bc9e7fda0acd4f", "test_name": "Test for response schema", "pass": true, "message": "valid 404 response"}`
     - Havent tested for invalid test cases because of unavailability of them


## Installation
python version 3.8.10

```
pip install -r requirements.txt
```

**Note:** Considering GA4GH starter kit DRS deployed and up endpoint `http://localhost:5000/ga4gh/drs/v1/objects/`

## Usage
**Syntax:**
```
python drs_test.py <object_id>
```

**Output:**
```
{"object_id" : "obj-id", "test_name" : "Regex for object_id validity", "pass" : flag, "message" : "Log message"}

{"object_id" : "obj-id", "test_name" : "Test for DRS object existance", "pass" : flag, "message" : "Log message"}

{"object_id" : "obj-id", "test_name" : "Test for response schema", "pass" : flag, "message" : "Log message"}
```

## Next Step
1. **Packaging the application:**
  - Creating a python package with redefining the structure of the project, adding license, configuration files and deploy on pypi using twine
  - Containerizing the project by creating dockerfile, docker-compose.yml and mentioning the requirments and exposing the port. Then using third party library like **requests** to access the port where application is listening


2. **Improvement/Additional tests:**
  - Currently just validating till the level-1 of response schema, can include more depth
  - Have tested for 200 and 404 response code currently and made assumtions for other response code, can make more concrete tests for them based on few more object_id response examples.
