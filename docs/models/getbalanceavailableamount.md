# GetBalanceAvailableAmount

The amount directly available on the balance, e.g. `{"currency":"EUR", "value":"100.00"}`.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `currency`                                                          | *str*                                                               | :heavy_check_mark:                                                  | A three-character ISO 4217 currency code.                           | EUR                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | A string containing an exact monetary amount in the given currency. | 10.00                                                               |