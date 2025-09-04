# GetWebhookEventLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [models.GetWebhookEventSelf](../models/getwebhookeventself.md)                             | :heavy_check_mark:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `documentation`                                                                            | [models.GetWebhookEventDocumentation](../models/getwebhookeventdocumentation.md)           | :heavy_check_mark:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `entity`                                                                                   | [Optional[models.LinksEntity]](../models/linksentity.md)                                   | :heavy_minus_sign:                                                                         | The API resource URL of the entity that this event belongs to.                             |