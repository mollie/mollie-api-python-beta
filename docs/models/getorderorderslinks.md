# GetOrderOrdersLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetOrderOrdersSelf]](../models/getorderordersself.md)                     | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `image_url`                                                                                | [Optional[models.ImageURL]](../models/imageurl.md)                                         | :heavy_minus_sign:                                                                         | A link pointing to an image of the product sold.                                           |
| `product_url`                                                                              | [Optional[models.ProductURL]](../models/producturl.md)                                     | :heavy_minus_sign:                                                                         | A link pointing to the product page in your web shop of the product sold.                  |