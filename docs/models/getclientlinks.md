# GetClientLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetClientSelf]](../models/getclientself.md)                               | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `organization`                                                                             | [Optional[models.GetClientOrganization]](../models/getclientorganization.md)               | :heavy_minus_sign:                                                                         | The API resource URL of the client's organization.                                         |
| `onboarding`                                                                               | [Optional[models.GetClientClientsOnboarding]](../models/getclientclientsonboarding.md)     | :heavy_minus_sign:                                                                         | The API resource URL of the client's onboarding status.                                    |
| `documentation`                                                                            | [Optional[models.GetClientDocumentation]](../models/getclientdocumentation.md)             | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |