# ClientLink

The link you can send your customer to, where they can either log in and link their account, or sign up and
proceed with onboarding.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *str*                                                       | :heavy_check_mark:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *str*                                                       | :heavy_check_mark:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |