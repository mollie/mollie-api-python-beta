# Totals

Totals are grouped according to the chosen grouping rule. The example response should give a good idea of what a
typical grouping looks like.

If grouping `status-balances` is chosen, the main grouping is as follows:

* `pendingBalance` containing an `open`, `pending`, `movedToAvailable`, and `close` sub-group
* `availableBalance` containing an `open`, `movedFromPending`, `immediatelyAvailable`, and `close` sub-group

If grouping `transaction-categories` is chosen, the main grouping is as follows:

* `open` and `close` groups, each containing a `pending` and `available` sub-group
* Transaction type groups such as `payments`, `refunds`, `chargebacks`, `capital`, `transfers`, `fee-prepayments`, `corrections`, `topups`
each containing a `pending`, `movedToAvailable`, and
`immediatelyAvailable` sub-group

Each sub-group typically has:

* An `amount` object containing the group's total amount
* A `count` integer if relevant (for example, counting the number of refunds)
* A `subtotals` array containing more sub-group objects if applicable


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `pending_balance`                                                                        | [OptionalNullable[models.PendingBalance]](../models/pendingbalance.md)                   | :heavy_minus_sign:                                                                       | The pending balance. Only available if grouping is `status-balances`.                    |
| `available_balance`                                                                      | [OptionalNullable[models.AvailableBalance]](../models/availablebalance.md)               | :heavy_minus_sign:                                                                       | The available balance. Only available if grouping is `status-balances`.                  |
| `open`                                                                                   | [Optional[models.Open]](../models/open.md)                                               | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `close`                                                                                  | [Optional[models.Close]](../models/close.md)                                             | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `payments`                                                                               | [Optional[models.GetBalanceReportPayments]](../models/getbalancereportpayments.md)       | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `refunds`                                                                                | [Optional[models.GetBalanceReportRefunds]](../models/getbalancereportrefunds.md)         | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `chargebacks`                                                                            | [Optional[models.GetBalanceReportChargebacks]](../models/getbalancereportchargebacks.md) | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `capital`                                                                                | [Optional[models.Capital]](../models/capital.md)                                         | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `transfers`                                                                              | [Optional[models.Transfers]](../models/transfers.md)                                     | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `fee_prepayments`                                                                        | [Optional[models.FeePrepayments]](../models/feeprepayments.md)                           | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `corrections`                                                                            | [Optional[models.Corrections]](../models/corrections.md)                                 | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |
| `topups`                                                                                 | [Optional[models.Topups]](../models/topups.md)                                           | :heavy_minus_sign:                                                                       | Only available on `transaction-categories` grouping.                                     |