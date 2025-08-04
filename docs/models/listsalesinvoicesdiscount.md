# ListSalesInvoicesDiscount

The discount to be applied to the entire invoice, applied on top of any line item discounts.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            | Example                                                                                |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `type`                                                                                 | [models.ListSalesInvoicesDiscountType](../models/listsalesinvoicesdiscounttype.md)     | :heavy_check_mark:                                                                     | The type of discount.                                                                  | amount                                                                                 |
| `value`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | A string containing an exact monetary amount in the given currency, or the percentage. | 10.00                                                                                  |