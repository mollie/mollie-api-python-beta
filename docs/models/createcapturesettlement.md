# CreateCaptureSettlement

The API resource URL of the [settlement](get-settlement) this capture has been settled with. Not present if
not yet settled.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `href`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | The actual URL string.                                      | https://...                                                 |
| `type`                                                      | *Optional[str]*                                             | :heavy_minus_sign:                                          | The content type of the page or endpoint the URL points to. | application/hal+json                                        |