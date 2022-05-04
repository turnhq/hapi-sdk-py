
# Target Group Model

## Structure

`TargetGroupModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `education_level` | [`List of TargetGroupElementModel`](../../doc/models/target-group-element-model.md) | Required | Education Level required by the Candidate. You can specify only one value. |
| `seniority` | [`List of TargetGroupElementModel`](../../doc/models/target-group-element-model.md) | Required | Seniority Level expected by the Candidate. You can specify only one value. |
| `industry` | [`List of TargetGroupElementModel`](../../doc/models/target-group-element-model.md) | Required | The Industry related to the Position open. You can specify only one value. |
| `job_category` | [`List of TargetGroupElementModel`](../../doc/models/target-group-element-model.md) | Required | Job Category indicates the type of Position that's open. You can specify only one value. |

## Example (as JSON)

```json
{
  "educationLevel": {
    "description": "Element name",
    "vonqId": "23"
  },
  "seniority": {
    "description": "Element name",
    "vonqId": "23"
  },
  "industry": {
    "description": "Element name",
    "vonqId": "23"
  },
  "jobCategory": {
    "description": "Element name",
    "vonqId": "23"
  }
}
```

