
# Getting Started with VONQ Hiring API

## Introduction

The VONQ Hiring API aims to provide all the basic VONQ Services through a comprehensive [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer) API. Systems would be able to
consume these services to list available VONQ Products and create Campaigns based on those Products.

### Overview

Our latest API version is currently version 2. It offers more search facets and filters,
a new recommendation engine, and a richer, evolving set of taxonomies so your users can find the most relevant,
best-performing products for their vacancies.

#### Schema

The API can be accessed at `https://marketplace.api.vonq.com` and is HTTPS-only. All requests must be
encoded in JSON, and all responses will be encoded in JSON as well.

#### Environments

We currently support two different environments for the Hiring API. The `Production` environment is
connected to our other `Production` backend services. That means that any order sent to this
environment is considered final and processed.

At the same time we support a `Sandbox` environment, accessible via `https://marketplace-sandbox.api.vonq.com`. You can safely test your API implementation here.
None of the orders sent to this environment are considered final, so they will not be executed nor charged. This
environment requires a different API Token to operate, which will be provided to you when available.

#### HTTP Methods

Whenever possible, the Hiring API uses RESTful `HTTP` methods for its actions.
| HTTP Method | Description                                      |
|:----------|--------------------------------------------------|
| `GET`     | Retrieve one or several Resources                |
| `POST`    | Create a new Resource. Eg: Create a new Campaign |
| `PATCH`   | Change part of the structure of a Resource       |

#### Pagination

Lists of multiple Resources will automatically paginate every 50 items by default. You can retrieve more elements by
specifying a value for the `offset` parameter (the default `offset` is 0). If you need to change the
number of elements returned by the default pagination, you can do so using the `limit` query parameter.

Example:

```

curl https://marketplace.api.vonq.com/portfolio?limit=100&offset=400

```

#### User-Agent

We recommend that every request made to the Hiring API includes a `User-Agent` header. This is not a mandatory
requirement at the moment, but this may change in the future. Specifying your User-Agent will allow us to provide you with more effective support.

#### Error Codes

The Hiring API uses standard HTTP Status codes for its responses to inform your system how the Hiring API handled your request.
Response codes in the range of `2xx` represent success codes (Eg, `201 Created`).
Codes in the `4xx` range indicates an error on the request performed, usually because the payload used doesn't contain
all the necessary information or is in an invalid format (Eg, `400 Bad Request`).
The error codes in the `5xx` range mean that an error occurred in the Hiring API and we were not able to handle your request.
It can also happen when our services are temporarily not available (Eg, `500 Internal Server Error`). These should be rare. We log these errors and investigate them as soon as possible.

The following Response coded are shared amongst all endpoints:

+ Response 400 (application/json)
  
        {
            "requestBody": "The request does not contain valid JSON."
        }

+ Response 401 (application/json)
  
        {
            "authentication": "Authentication Required"
        }

+ Response 401 (application/json)
  
        {
            "authentication": "Username could not be found."
        }

+ Response 500 (application/json)

#### Caching

We recommend avoiding using cached versions of portfolio and taxonomy data since it is subject to regular updates. Campaign ordeproducts  invalid taxonomy will be rejected.
If you do need to use caching, we recommend refreshing it daily.

#### Rate Limits

To prevent abuse and ensure service stability, all the API requests are rate limited. Rate limits specify
the maximum number of API calls (60) that can be made in 60 seconds. These limits reset every 60 seconds.
User of the API can make upto 60 request per 60 seconds.

## Building

You must have Python `3 >=3.7, <= 3.9` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&step=installDependencies)

## Installation

The following section explains how to use the hapi library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&projectName=hapi&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&projectName=hapi&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&projectName=hapi&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&projectName=hapi&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from hapi.hapi_client import HapiClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&projectName=hapi&libraryName=hapi.hapi_client&className=HapiClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Hapi-Python&projectName=hapi&libraryName=hapi.hapi_client&className=HapiClient&step=runProject)

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `nose` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
nosetests
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.SANDBOX`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `skip_ssl_cert_verification` | `boolean` | Set to true to allow skipping ssl certificate verification |
| `x_auth_token` | `string` |  |
| `x_customer_id` | `string` |  |

The API client can be initialized as follows:

```python
from hapi.hapi_client import HapiClient
from hapi.configuration import Environment

client = HapiClient(
    x_auth_token='X-Auth-Token',
    x_customer_id='X-Customer-Id',
    environment=Environment.SANDBOX,)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| sandbox | **Default** Sandbox |
| production | Production |

## Authorization

This API uses `Custom Header Signature`.

## List of APIs

* [Campaigns](doc/controllers/campaigns.md)
* [Contracts](doc/controllers/contracts.md)
* [Portfolio](doc/controllers/portfolio.md)
* [Taxonomy](doc/controllers/taxonomy.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

