# ListPaymentsLinks

Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.ListPaymentsSelf]](../models/listpaymentsself.md)                         | :heavy_minus_sign:                                                                         | The URL to the current set of items.                                                       |
| `previous`                                                                                 | [OptionalNullable[models.ListPaymentsPrevious]](../models/listpaymentsprevious.md)         | :heavy_minus_sign:                                                                         | The previous set of items, if available.                                                   |
| `next`                                                                                     | [OptionalNullable[models.ListPaymentsNext]](../models/listpaymentsnext.md)                 | :heavy_minus_sign:                                                                         | The next set of items, if available.                                                       |
| `documentation`                                                                            | [Optional[models.ListPaymentsDocumentation]](../models/listpaymentsdocumentation.md)       | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |