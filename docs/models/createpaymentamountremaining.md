# CreatePaymentAmountRemaining

The remaining amount that can be refunded. Only available when refunds are available for this payment.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `currency`                                                          | *str*                                                               | :heavy_check_mark:                                                  | A three-character ISO 4217 currency code.                           | EUR                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | A string containing an exact monetary amount in the given currency. | 10.00                                                               |