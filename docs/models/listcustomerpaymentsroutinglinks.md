# ListCustomerPaymentsRoutingLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `self_`                                                                                      | [models.ListCustomerPaymentsRoutingSelf](../models/listcustomerpaymentsroutingself.md)       | :heavy_check_mark:                                                                           | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.   |
| `payment`                                                                                    | [models.ListCustomerPaymentsRoutingPayment](../models/listcustomerpaymentsroutingpayment.md) | :heavy_check_mark:                                                                           | The API resource URL of the [payment](get-payment) that belong to this route.                |