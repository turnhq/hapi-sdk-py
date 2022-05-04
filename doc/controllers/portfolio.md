# Portfolio

```python
portfolio_controller = client.portfolio
```

## Class Name

`PortfolioController`

## Methods

* [Calculate Order Delivery Time](../../doc/controllers/portfolio.md#calculate-order-delivery-time)
* [Retrieve Multiple Products](../../doc/controllers/portfolio.md#retrieve-multiple-products)
* [Retrieve Single Product](../../doc/controllers/portfolio.md#retrieve-single-product)
* [Search Products](../../doc/controllers/portfolio.md#search-products)


# Calculate Order Delivery Time

This endpoint calculates total number of days to process and setup a campaign containing a list of Products, given a comma-separated list of their ids.

```python
def calculate_order_delivery_time(self,
                                 products_ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `products_ids` | `List of string` | Template, Required | - |

## Response Type

[`List of ProductsDeliveryTimeModel`](../../doc/models/products-delivery-time-model.md)

## Example Usage

```python
products_ids = ['products_ids7', 'products_ids8']

result = portfolio_controller.calculate_order_delivery_time(products_ids)
```

## Example Response *(as JSON)*

```json
[
  {
    "days_to_process": 1,
    "days_to_setup": 1,
    "total_days": 2
  }
]
```


# Retrieve Multiple Products

Sometimes you already have access to the Identification codes of more than one Product and you want to retrieve the most up-to-date information about them.
Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.

```python
def retrieve_multiple_products(self,
                              products_ids,
                              accept_language=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `products_ids` | `List of string` | Template, Required | - |
| `accept_language` | [`AcceptLanguageEnum`](../../doc/models/accept-language-enum.md) | Header, Optional | - |

## Response Type

[`List of ProductModel`](../../doc/models/product-model.md)

## Example Usage

```python
products_ids = ['products_ids7', 'products_ids8']
accept_language = AcceptLanguageEnum.EN

result = portfolio_controller.retrieve_multiple_products(products_ids, accept_language)
```


# Retrieve Single Product

Sometimes you already have access to the Identification code of any particular Product and you want to retrieve the most up-to-date information about it.
Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.

```python
def retrieve_single_product(self,
                           product_id,
                           accept_language=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `string` | Template, Required | - |
| `accept_language` | [`AcceptLanguageEnum`](../../doc/models/accept-language-enum.md) | Header, Optional | - |

## Response Type

[`ProductModel`](../../doc/models/product-model.md)

## Example Usage

```python
product_id = 'product_id4'
accept_language = AcceptLanguageEnum.EN

result = portfolio_controller.retrieve_single_product(product_id, accept_language)
```


# Search Products

For a detailed tutorial on how to get started with portfolio search v2, check out our [Quickstart Tutorial](https://pkb.stoplight.io/docs/search/docs/Tutorial.md).
For an implementation demo of the product search experience, check out our [Developer Portal](http://vonq.io/pkb).
This endpoint exposes a list of Products with the options to search by Location, Job Title, Job Function and Industry.
Products are ranked by their relevancy to the search terms.
Optionally, products can filtered by Location.
Values for each parameter can be fetched by calling the other endpoints in this section.
Calling this endpoint will guarantee that the Products you see are configured for you as our Partner.
Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.

```python
def search_products(self,
                   limit=None,
                   offset=None,
                   include_location_id=None,
                   exact_location_id=None,
                   job_function_id=None,
                   job_title_id=None,
                   industry_id=None,
                   duration_from=None,
                   duration_to=None,
                   name=None,
                   currency=None,
                   sort_by='relevant',
                   recommended=None,
                   mc_enabled=None,
                   accept_language=None,
                   exclude_recommended=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `include_location_id` | `List of string` | Query, Optional | Id for a Location to search products against. If no exact matches exist, search will be expanded to the Location's region and country. Optionally, a (comma-separated) array of values can be passed. Passing multiple values increases the number of search results. |
| `exact_location_id` | `string` | Query, Optional | Match only products specifically assigned to a Location. |
| `job_function_id` | `string` | Query, Optional | Job Function id. Not to be used in conjunction with a Job Title id. |
| `job_title_id` | `string` | Query, Optional | Job title id |
| `industry_id` | `List of string` | Query, Optional | Industry Id |
| `duration_from` | `string` | Query, Optional | Match only products with a duration more or equal than a certain number of days |
| `duration_to` | `string` | Query, Optional | Match only products with a duration up to a certain number of days |
| `name` | `string` | Query, Optional | Search text for a product name |
| `currency` | `string` | Query, Optional | ISO-4217 code for a currency |
| `sort_by` | [`SortByEnum`](../../doc/models/sort-by-enum.md) | Query, Optional | Which products to show first. Defaults to 'relevant'<br>**Default**: `'relevant'` |
| `recommended` | `bool` | Query, Optional | Whether to display a list of recommended products for the search parameters. If true, returns a limited list of products for the types: Job board, social media, publication and community. |
| `mc_enabled` | `bool` | Query, Optional | Can be used to filter for products that are linked to a channel enabled for My Contracts orders |
| `accept_language` | [`AcceptLanguageEnum`](../../doc/models/accept-language-enum.md) | Header, Optional | - |
| `exclude_recommended` | `bool` | Query, Optional | Exclude recommended products from search results. Cannot be used in combination with 'recommended'.<br>**Default**: `False` |

## Response Type

[`List of ProductModel`](../../doc/models/product-model.md)

## Example Usage

```python
sort_by = SortByEnum.RELEVANT
accept_language = AcceptLanguageEnum.EN
exclude_recommended = False

result = portfolio_controller.search_products(None, None, None, None, None, None, None, None, None, None, None, sort_by, None, None, accept_language, exclude_recommended)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

