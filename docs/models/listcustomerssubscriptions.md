# ListCustomersSubscriptions

The API resource URL of the [subscriptions](list-subscriptions) linked to this customer. Omitted if no such
subscriptions exist (yet).


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |