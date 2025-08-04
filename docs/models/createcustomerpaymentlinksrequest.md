# CreateCustomerPaymentLinksRequest

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `self_`                                                                                        | [models.CreateCustomerPaymentSelfRequest](../models/createcustomerpaymentselfrequest.md)       | :heavy_check_mark:                                                                             | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field.     |
| `payment`                                                                                      | [models.CreateCustomerPaymentPaymentRequest](../models/createcustomerpaymentpaymentrequest.md) | :heavy_check_mark:                                                                             | The API resource URL of the [payment](get-payment) that belong to this route.                  |