# GetBalanceReportPayments

Only available on `transaction-categories` grouping.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `pending`                                                                                  | [Optional[models.PaymentsPending]](../models/paymentspending.md)                           | :heavy_minus_sign:                                                                         | N/A                                                                                        |
| `moved_to_available`                                                                       | [Optional[models.PaymentsMovedToAvailable]](../models/paymentsmovedtoavailable.md)         | :heavy_minus_sign:                                                                         | N/A                                                                                        |
| `immediately_available`                                                                    | [Optional[models.PaymentsImmediatelyAvailable]](../models/paymentsimmediatelyavailable.md) | :heavy_minus_sign:                                                                         | N/A                                                                                        |