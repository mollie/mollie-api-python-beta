# GetInvoiceLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.GetInvoiceSelf]](../models/getinvoiceself.md)                             | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |
| `pdf`                                                                                      | [Optional[models.Pdf]](../models/pdf.md)                                                   | :heavy_minus_sign:                                                                         | URL to a downloadable PDF of the invoice.                                                  |
| `documentation`                                                                            | [Optional[models.GetInvoiceDocumentation]](../models/getinvoicedocumentation.md)           | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |