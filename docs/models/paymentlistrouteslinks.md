# PaymentListRoutesLinks

Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `self_`                                                                                        | [Optional[models.PaymentListRoutesSelf]](../models/paymentlistroutesself.md)                   | :heavy_minus_sign:                                                                             | The URL to the current set of items.                                                           |
| `documentation`                                                                                | [Optional[models.PaymentListRoutesDocumentation]](../models/paymentlistroutesdocumentation.md) | :heavy_minus_sign:                                                                             | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.     |