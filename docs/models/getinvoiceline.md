# GetInvoiceLine


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `period`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The administrative period in `YYYY-MM` on which the line should be booked. |
| `description`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | Description of the product.                                                |
| `count`                                                                    | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | Number of products invoiced. For example, the number of payments.          |
| `vat_percentage`                                                           | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | VAT percentage rate that applies to this product.                          |
| `amount`                                                                   | [Optional[models.GetInvoiceAmount]](../models/getinvoiceamount.md)         | :heavy_minus_sign:                                                         | Line item amount excluding VAT.                                            |