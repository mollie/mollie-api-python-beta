# CreatePaymentMobileAppCheckout

The deeplink URL to the app of the payment method. Currently only available for `bancontact`.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *str*                                                       | :heavy_check_mark:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *str*                                                       | :heavy_check_mark:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |