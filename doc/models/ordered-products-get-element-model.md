
# Ordered Products Get Element Model

## Structure

`OrderedProductsGetElementModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `string` | Optional | Product Identification |
| `status` | `string` | Optional | Status per product |
| `status_description` | `string` | Optional | Status description, additional status information |
| `delivered_on` | `string` | Optional | Date when the channel went online |
| `duration` | `string` | Optional | How long will the `Product` be online. [DEPRECATED] please instead use the `durationPeriod` |
| `duration_period` | [`DurationModel`](../../doc/models/duration-model.md) | Optional | - |
| `utm` | `string` | Optional | Tracking codes |
| `job_board_link` | `string` | Optional | Link to the job ad on the channel. Sometimes this link is not available from a job board, then the product homepage is returned. |
| `contract_id` | `string` | Optional | Contract Identifier for My Contracts product |
| `posting_requirements` | [`PostingRequirementsModel`](../../doc/models/posting-requirements-model.md) | Optional | - |

## Example (as JSON)

```json
{
  "productId": null,
  "status": null,
  "statusDescription": null,
  "deliveredOn": null,
  "duration": null,
  "durationPeriod": null,
  "utm": null,
  "jobBoardLink": null,
  "contractId": null,
  "postingRequirements": null
}
```

