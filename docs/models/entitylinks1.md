# EntityLinks1

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `self_`                                                                                                    | [models.EntitySelf1](../models/entityself1.md)                                                             | :heavy_check_mark:                                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.                 |
| `payment_link`                                                                                             | [models.GetWebhookEventLinksPaymentLink](../models/getwebhookeventlinkspaymentlink.md)                     | :heavy_check_mark:                                                                                         | The URL your customer should visit to make the payment. This is where you should redirect the customer to. |