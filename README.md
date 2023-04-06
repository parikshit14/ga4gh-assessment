## Test Description
There is three basic test coverage in this repository:
1. **Test to validate whether the object_id entered is correct:**
 - According to the documentation [ref](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/#:~:text=follows%20these%20guidelines%3A-,DRS%20IDs,-are%20strings%20made) the allowed characters are [A-Za-z0-9.-_~]
 - This has been implemented using regular expression matching library re
 - Sample output:
    - Valid case `{"object_id": "xx18bfb64168994489bc9e7fda0acd4f", "test_name": "Regex for object_id validity", "pass": true, "message": "valid object_id"}`
    - Invalid case `{"object_id": "xx18bfb64168994489bc9e7fda0acd4f*dcdc", "test_name": "Regex for object_id validity", "pass": false, "message": "Invalid object_id"}`


2. **Test to check if the entered object_id exists in the Database:**
 - The response code received for the given object_id tells about the existence of that object_id in the db
 - If response code is 404 then that particular object_id doesn't exist otherwise it exists
 - Sample output:
     - Valid case `{"object_id": "ecbb0b5131051c41f1c302287c13495c", "test_name": "Test for DRS object existance", "pass": true, "message": "DRS object found"}`
     - Invalid case `{"object_id": "xx18", "test_name": "Test for DRS object existance", "pass": false, "message": "DRS object not found"}`


3. **Test to check if Schema of response is correct or not:**
 - The response data passes through a predefined schema which validates its correctness
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
  - Creating Docker Image:
  
    **EDIT1: Running application as a docker image**
    Modified the project so it can be containerized, only added a dockerfile with requirements to create the image.
    Steps for regenerating the result:
    1. Build the docker image: `docker build -t drs_test_image .`
    2. Run the docker image: `docker run --add-host=localhost:host-gateway drs_test_image <obj_id>`
    This returns the same result:
    ```
    {"object_id": "8e18bfb64168994489bc9e7fda0acd4f", "test_name": "Regex for object_id validity", "pass": true, "message": "valid object_id"}
    {"object_id": "8e18bfb64168994489bc9e7fda0acd4f", "test_name": "Test for DRS object existance", "pass": true, "message": "DRS object found"}
    {"object_id": "8e18bfb64168994489bc9e7fda0acd4f", "test_name": "Test for response schema", "pass": true, "message": "valid 200 response"}
    ```


2. **Improvement/Additional tests:**
  - Currently just validating till the level-1 of response schema, can include more depth
  - Have tested for 200 and 404 response code currently and made assumptions for other response codes, can make more concrete tests for them based on few more object_id response examples.
