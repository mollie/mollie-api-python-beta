# CreateSalesInvoiceLineDiscountRequest

The discount to be applied to the line item.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `type`                                                                                     | [models.CreateSalesInvoiceLineTypeRequest](../models/createsalesinvoicelinetyperequest.md) | :heavy_check_mark:                                                                         | The type of discount.                                                                      | amount                                                                                     |
| `value`                                                                                    | *str*                                                                                      | :heavy_check_mark:                                                                         | A string containing an exact monetary amount in the given currency, or the percentage.     | 10.00                                                                                      |