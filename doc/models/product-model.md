
# Product Model

## Structure

`ProductModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `string` | Required | - |
| `locations` | [`List of LocationModel`](../../doc/models/location-model.md) | Required | **Constraints**: *Unique Items Required* |
| `job_functions` | [`List of JobFunctionModel`](../../doc/models/job-function-model.md) | Required | **Constraints**: *Unique Items Required* |
| `industries` | [`List of IndustryModel`](../../doc/models/industry-model.md) | Required | **Constraints**: *Unique Items Required* |
| `description` | `string` | Optional | - |
| `homepage` | `string` | Optional | - |
| `logo_url` | `string` | Optional | - |
| `logo_square_url` | `string` | Optional | - |
| `logo_rectangle_url` | `string` | Optional | - |
| `duration` | `object` | Optional | - |
| `time_to_process` | [`TimeToProcessModel`](../../doc/models/time-to-process-model.md) | Required | - |
| `time_to_setup` | [`TimeToSetupModel`](../../doc/models/time-to-setup-model.md) | Required | - |
| `product_id` | `uuid\|string` | Required | - |
| `vonq_price` | [`List of PriceModel`](../../doc/models/price-model.md) | Required | the price to be displayed to customers |
| `ratecard_price` | [`List of PriceModel`](../../doc/models/price-model.md) | Required | - |
| `mtype` | [`ChannelTypeEnum`](../../doc/models/channel-type-enum.md) | Required | The type of a channel |
| `cross_postings` | `List of string` | Required | - |
| `channel` | [`ChannelModel`](../../doc/models/channel-model.md) | Required | - |
| `audience_group` | [`AudienceGroupEnum`](../../doc/models/audience-group-enum.md) | Required | The product's audience group (niche/generic) |
| `mc_enabled` | `bool` | Required | is My Contract enabled for the channel |
| `mc_only` | `bool` | Required | is the product available only for My Contract order |
| `allow_orders` | `bool` | Required | is the product available for order. a campaign cannot be ordered with a product having `allow_orders` set to `false`. |

## Example (as JSON)

```json
{
  "title": null,
  "locations": {
    "id": null,
    "fully_qualified_place_name": null,
    "canonical_name": null,
    "bounding_box": null,
    "area": null,
    "place_type": "place",
    "within": {
      "id": null,
      "fully_qualified_place_name": null,
      "canonical_name": null,
      "bounding_box": null,
      "area": null,
      "place_type": "place",
      "within": null
    }
  },
  "job_functions": null,
  "industries": null,
  "time_to_process": null,
  "time_to_setup": null,
  "product_id": null,
  "vonq_price": null,
  "ratecard_price": null,
  "type": "job board",
  "cross_postings": null,
  "channel": {
    "name": "Linkedin",
    "url": "www.linkedin.com",
    "type": "job board",
    "mc_enabled": false,
    "contract_credentials": null,
    "contract_facets": null,
    "posting_requirements": {
      "name": null,
      "label": null,
      "sort": null,
      "required": null,
      "type": "AUTOCOMPLETE",
      "options": null
    },
    "manual_setup_required": null
  },
  "audience_group": null,
  "mc_enabled": null,
  "mc_only": null,
  "allow_orders": null
}
```

