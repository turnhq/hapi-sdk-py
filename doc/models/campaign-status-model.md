
# Campaign Status Model

## Structure

`CampaignStatusModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_id` | `string` | Required | - |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Status of the campaign. One of the following |
| `ordered_products_statuses` | [`List of OrderedProductsStatusItemModel`](../../doc/models/ordered-products-status-item-model.md) | Optional | - |

## Example (as JSON)

```json
{
  "campaignId": "dd1c5be0-b0e1-41c8-ba92-e876da16c38b"
}
```

