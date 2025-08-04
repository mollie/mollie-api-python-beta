# CreateSubscriptionApplicationFeeResponse

With Mollie Connect you can charge fees on payments that your app is processing on behalf of other Mollie
merchants.

Setting an application fee on the subscription will ensure this fee is charged on each individual payment.

Refer to the `applicationFee` parameter on the [Get payment endpoint](get-payment) documentation for more
information.


## Fields

| Field                                                                                                                          | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `amount`                                                                                                                       | [Optional[models.CreateSubscriptionApplicationFeeAmountResponse]](../models/createsubscriptionapplicationfeeamountresponse.md) | :heavy_minus_sign:                                                                                                             | In v2 endpoints, monetary amounts are represented as objects with a `currency` and `value` field.                              |                                                                                                                                |
| `description`                                                                                                                  | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | N/A                                                                                                                            | Platform fee                                                                                                                   |