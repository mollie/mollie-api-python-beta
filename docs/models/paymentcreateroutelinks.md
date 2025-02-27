# PaymentCreateRouteLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `self_`                                                                                          | [Optional[models.PaymentCreateRouteSelf]](../models/paymentcreaterouteself.md)                   | :heavy_minus_sign:                                                                               | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.       |
| `documentation`                                                                                  | [Optional[models.PaymentCreateRouteDocumentation]](../models/paymentcreateroutedocumentation.md) | :heavy_minus_sign:                                                                               | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.       |