# ListClientsClientLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.ClientSelf]](../models/clientself.md)                                     | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `organization`                                                                             | [Optional[models.ListClientsLinksOrganization]](../models/listclientslinksorganization.md) | :heavy_minus_sign:                                                                         | The API resource URL of the client's organization.                                         |
| `onboarding`                                                                               | [Optional[models.ListClientsLinksOnboarding]](../models/listclientslinksonboarding.md)     | :heavy_minus_sign:                                                                         | The API resource URL of the client's onboarding status.                                    |
| `documentation`                                                                            | [Optional[models.ClientDocumentation]](../models/clientdocumentation.md)                   | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |