# GetPaymentOrder

The API resource URL of the [order](get-order) this payment was created for. Not present if not created for an
order.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *str*                                                       | :heavy_check_mark:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *str*                                                       | :heavy_check_mark:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |