
# Create Contract Response Model

## Structure

`CreateContractResponseModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Required | - |
| `contract_id` | `string` | Required | - |
| `channel_id` | `int` | Required | - |
| `credentials` | `string` | Required | - |
| `class_name` | `string` | Required | - |
| `facets` | `object` | Required | - |
| `product` | [`ProductLiteModel`](../../doc/models/product-lite-model.md) | Required | - |
| `posting_requirements` | `string` | Required | - |
| `expiry_date` | `datetime` | Optional | - |
| `credits` | `int` | Optional | - |
| `purchase_price` | [`PurchasePriceModel`](../../doc/models/purchase-price-model.md) | Optional | - |

## Example (as JSON)

```json
{
  "customer_id": "76e124d4-ae69-4753-bede-259d505258b7",
  "contract_id": "3a283b8f-1670-404b-b804-92f67e66b71c",
  "channel_id": 13,
  "credentials": "",
  "class_name": "",
  "facets": {},
  "product": {
    "product_id": "2e8c3c17-179b-4db1-9e2b-d48369b5e409",
    "title": "product title"
  },
  "posting_requirements": ""
}
```

