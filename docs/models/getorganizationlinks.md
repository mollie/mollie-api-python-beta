# GetOrganizationLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetOrganizationSelf]](../models/getorganizationself.md)                   | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `dashboard`                                                                                | [Optional[models.GetOrganizationDashboard]](../models/getorganizationdashboard.md)         | :heavy_minus_sign:                                                                         | Direct link to the organization's Mollie dashboard.                                        |
| `documentation`                                                                            | [Optional[models.GetOrganizationDocumentation]](../models/getorganizationdocumentation.md) | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |