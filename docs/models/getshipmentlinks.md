# GetShipmentLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetShipmentSelf]](../models/getshipmentself.md)                           | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `order`                                                                                    | [Optional[models.Order]](../models/order.md)                                               | :heavy_minus_sign:                                                                         | The API resource URL of the [order](get-order) that this shipment belongs to.              |
| `documentation`                                                                            | [Optional[models.GetShipmentDocumentation]](../models/getshipmentdocumentation.md)         | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |