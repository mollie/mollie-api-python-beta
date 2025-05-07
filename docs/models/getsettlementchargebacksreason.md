# GetSettlementChargebacksReason

Reason for the chargeback as given by the bank. Only available for chargebacks of SEPA Direct Debit payments.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `code`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | Technical code provided by the bank.             | AC01                                             |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | A more detailed human-friendly description.      | Account identifier incorrect (i.e. invalid IBAN) |