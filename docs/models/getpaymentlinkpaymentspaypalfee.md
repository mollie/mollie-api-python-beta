# GetPaymentLinkPaymentsPaypalFee

An amount object containing the fee PayPal will charge for this transaction. The field may be omitted if
PayPal will not charge a fee for this transaction.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `currency`                                                          | *str*                                                               | :heavy_check_mark:                                                  | A three-character ISO 4217 currency code.                           | EUR                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | A string containing an exact monetary amount in the given currency. | 10.00                                                               |