# GetPaymentLinkPaymentsAmountChargedBack

The total amount that was charged back for this payment. Only available when the total charged back amount is not
zero.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `currency`                                                          | *str*                                                               | :heavy_check_mark:                                                  | A three-character ISO 4217 currency code.                           | EUR                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | A string containing an exact monetary amount in the given currency. | 10.00                                                               |