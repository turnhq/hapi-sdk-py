
# Posting Working Location Model

## Structure

`PostingWorkingLocationModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `string` | Required | - |
| `address_line_2` | `string` | Optional | - |
| `postcode` | `string` | Required | - |
| `city` | `string` | Required | - |
| `country` | `string` | Required | - |
| `allows_remote_work` | `float` | Optional | Optional parameter allowing remote work, possible values are 0 and 1, defaults to 0 |

## Example (as JSON)

```json
{
  "addressLine1": "Westblaak 175",
  "postcode": "3012 KJ",
  "city": "Rotterdam",
  "country": "The Netherlands"
}
```

