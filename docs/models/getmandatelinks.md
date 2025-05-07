# GetMandateLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetMandateSelf]](../models/getmandateself.md)                             | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `customer`                                                                                 | [Optional[models.GetMandateCustomer]](../models/getmandatecustomer.md)                     | :heavy_minus_sign:                                                                         | The API resource URL of the [customer](get-customer) that this mandate belongs to.         |
| `documentation`                                                                            | [Optional[models.GetMandateDocumentation]](../models/getmandatedocumentation.md)           | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |