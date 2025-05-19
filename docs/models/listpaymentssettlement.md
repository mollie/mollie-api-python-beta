# ListPaymentsSettlement

The API resource URL of the [settlement](get-settlement) this payment has been settled with. Not present if not yet settled.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *str*                                                       | :heavy_check_mark:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *str*                                                       | :heavy_check_mark:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |