# CancelSubscriptionPayments

The API resource URL of the [payments](list-payments) created for this subscription. Omitted if no such
payments exist (yet).


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |