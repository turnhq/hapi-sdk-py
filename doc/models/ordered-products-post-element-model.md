
# Ordered Products Post Element Model

## Structure

`OrderedProductsPostElementModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `string` | Optional | Product Identification |
| `utm` | `string` | Optional | Query string for UTM parameters<br><br>**Pattern:** `/^([%.-_!*a-zA-Z0-9]{1,}=[%.-_!*+,;$()a-zA-Z0-9]{1,}[&]{0,}){1,}$/` |
| `contract_id` | `string` | Optional | Contract Identifier needed for My Contracts product |
| `posting_requirements` | [`PostingRequirementsModel`](../../doc/models/posting-requirements-model.md) | Optional | - |

## Example (as JSON)

```json
{
  "productId": null,
  "utm": null,
  "contractId": null,
  "postingRequirements": null
}
```

