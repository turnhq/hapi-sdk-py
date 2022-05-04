# Taxonomy

```python
taxonomy_controller = client.taxonomy
```

## Class Name

`TaxonomyController`

## Methods

* [List Industries](../../doc/controllers/taxonomy.md#list-industries)
* [Retrieve Education Levels](../../doc/controllers/taxonomy.md#retrieve-education-levels)
* [Retrieve Job Functions Tree](../../doc/controllers/taxonomy.md#retrieve-job-functions-tree)
* [Retrieve Seniorities](../../doc/controllers/taxonomy.md#retrieve-seniorities)
* [Search Job Titles](../../doc/controllers/taxonomy.md#search-job-titles)
* [Search Locations](../../doc/controllers/taxonomy.md#search-locations)


# List Industries

This endpoint returns a list of supported industry names that can be used to search for products. Results are ordered alphabetically.
Use the `id` key of any Industry in the response to search for a product.
Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.

```python
def list_industries(self,
                   limit=None,
                   offset=None,
                   accept_language=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `float` | Query, Optional | Number of results to return per page. |
| `offset` | `float` | Query, Optional | The initial index from which to return the results. |
| `accept_language` | [`AcceptLanguageEnum`](../../doc/models/accept-language-enum.md) | Header, Optional | - |

## Response Type

[`List of IndustryModel`](../../doc/models/industry-model.md)

## Example Usage

```python
accept_language = AcceptLanguageEnum.EN

result = taxonomy_controller.list_industries(None, None, accept_language)
```


# Retrieve Education Levels

Retrieve all Education Level possible values.

```python
def retrieve_education_levels(self)
```

## Response Type

[`List of EducationLevelModel`](../../doc/models/education-level-model.md)

## Example Usage

```python
result = taxonomy_controller.retrieve_education_levels()
```

## Example Response *(as JSON)*

```json
[
  {
    "id": 1,
    "name": [
      {
        "languageCode": "nl_NL",
        "value": "Master / Postdoctoraal"
      }
    ]
  }
]
```


# Retrieve Job Functions Tree

This endpoint returns a tree-like structure of supported Job Functions that can be used to search for Products.
Use the `id` key of any Job Function in the response to search for a Product.
Each Job Function is associated with [**`Job Titles`**](b3A6MzM0NDA3MzY-job-titles) in a one-to-many fashion.
Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.

```python
def retrieve_job_functions_tree(self,
                               accept_language=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept_language` | [`AcceptLanguageEnum`](../../doc/models/accept-language-enum.md) | Header, Optional | - |

## Response Type

[`List of JobFunctionModel`](../../doc/models/job-function-model.md)

## Example Usage

```python
accept_language = AcceptLanguageEnum.EN

result = taxonomy_controller.retrieve_job_functions_tree(accept_language)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": 8,
    "name": "Education",
    "children": [
      {
        "id": 5,
        "name": "Teaching",
        "children": []
      }
    ]
  }
]
```


# Retrieve Seniorities

Retrieve all Seniority possible values.

```python
def retrieve_seniorities(self)
```

## Response Type

[`List of SeniorityModel`](../../doc/models/seniority-model.md)

## Example Usage

```python
result = taxonomy_controller.retrieve_seniorities()
```

## Example Response *(as JSON)*

```json
[
  {
    "id": 3,
    "name": [
      {
        "languageCode": "en_GB",
        "value": "Manager"
      }
    ]
  }
]
```


# Search Job Titles

This endpoint takes any text as input and returns a list of supported Job Titles matching the query, ordered by popularity.
Use the `id` key of each object in the response to search for a Product.
Currently, we support 4,000 job titles for each of the following languages: English, Dutch and German.
Each Job Title is associated with a [**`Job Function`**](b3A6MzM0NDA3MzU-job-functions) in a many-to-one fashion.
Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.

```python
def search_job_titles(self,
                     text,
                     limit=None,
                     offset=None,
                     accept_language=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `string` | Query, Required | Search text for a job title name |
| `limit` | `float` | Query, Optional | Number of results to return per page. |
| `offset` | `float` | Query, Optional | The initial index from which to return the results. |
| `accept_language` | [`AcceptLanguageEnum`](../../doc/models/accept-language-enum.md) | Header, Optional | - |

## Response Type

[`List of JobTitleModel`](../../doc/models/job-title-model.md)

## Example Usage

```python
text = 'text0'
accept_language = AcceptLanguageEnum.EN

result = taxonomy_controller.search_job_titles(text, None, None, accept_language)
```


# Search Locations

This endpoint takes any text as input and returns a list of Locations matching the query, ordered by popularity.
Each response will include the entire world as a Location, even no Locations match the text query.
Use the `id` key of each object in the response to search for a Product.
Supports text input in English, Dutch and German.

```python
def search_locations(self,
                    text)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `string` | Query, Required | Search text for a location name in either English, Dutch, German, French and Italian. Partial recognition of 20 other languages. |

## Response Type

[`List of LocationModel`](../../doc/models/location-model.md)

## Example Usage

```python
text = 'text0'

result = taxonomy_controller.search_locations(text)
```

