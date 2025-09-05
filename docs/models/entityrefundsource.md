# EntityRefundSource

Where the funds will be pulled back from.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `type`                                                                          | [Optional[models.RoutingReversalType]](../models/routingreversaltype.md)        | :heavy_minus_sign:                                                              | The type of source. Currently only the source type `organization` is supported. | organization                                                                    |
| `organization_id`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             | org_1234567                                                                     |