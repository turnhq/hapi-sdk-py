
# Posting Details Errors Model

## Structure

`PostingDetailsErrorsModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `List of string` | Required | - |
| `description` | `List of string` | Required | - |
| `years_of_experience` | `List of string` | Required | - |
| `employment_type` | `List of string` | Required | - |
| `organization` | [`OrganizationModel`](../../doc/models/organization-model.md) | Required | - |
| `working_location` | [`WorkingLocationModel`](../../doc/models/working-location-model.md) | Required | - |
| `weekly_working_hours` | [`WeeklyWorkingHoursModel`](../../doc/models/weekly-working-hours-model.md) | Required | - |
| `salary_indication` | [`SalaryIndicationModel`](../../doc/models/salary-indication-model.md) | Required | - |
| `job_page_url` | `List of string` | Required | - |
| `application_url` | `List of string` | Required | - |

## Example (as JSON)

```json
{
  "title": [
    "A Title of the Posting is required"
  ],
  "description": [
    "A Description of the Posting is required"
  ],
  "yearsOfExperience": [
    "This value should not be blank."
  ],
  "employmentType": [
    "A Posting needs a type of employment"
  ],
  "organization": {
    "name": [
      "This value should not be blank."
    ],
    "companyLogo": [
      "This value should not be blank."
    ]
  },
  "workingLocation": {
    "addressLine1": [
      "This value should not be blank."
    ],
    "postcode": [
      "This value should not be blank."
    ],
    "city": [
      "This value should not be blank."
    ],
    "country": [
      "This value should not be blank."
    ]
  },
  "weeklyWorkingHours": {
    "to": [
      "This value should not be blank."
    ]
  },
  "salaryIndication": {
    "period": [
      "A SalaryIndication needs a period"
    ],
    "range": {
      "to": [
        "This value should not be blank."
      ]
    }
  },
  "jobPageUrl": [
    "This value should not be blank."
  ],
  "applicationUrl": [
    "This value should not be blank."
  ]
}
```

