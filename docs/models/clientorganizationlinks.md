# ClientOrganizationLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `self_`                                                                                            | [Optional[models.ClientOrganizationSelf]](../models/clientorganizationself.md)                     | :heavy_minus_sign:                                                                                 | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.         |
| `dashboard`                                                                                        | [Optional[models.ListClientsOrganizationDashboard]](../models/listclientsorganizationdashboard.md) | :heavy_minus_sign:                                                                                 | Direct link to the organization's Mollie dashboard.                                                |
| `documentation`                                                                                    | [Optional[models.ClientOrganizationDocumentation]](../models/clientorganizationdocumentation.md)   | :heavy_minus_sign:                                                                                 | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.         |