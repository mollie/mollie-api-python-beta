# Data

Operation data depending on the type of operation.

For an `add` operation, provide the fields for the new order line in the same format as in the [Create order](create-order) endpoint.

For an `update` operation, provide the `id` of the order line, along with any fields you would like to update.

For a `cancel` operation, provide the `id` of the order line. Optionally, a `quantity` or `amount` can be provided to only partially cancel an order line.


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`                                                                                              | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | Required for `update` and `cancel` operations. For example: `odl_dgtxyl`.                         |
| `quantity`                                                                                        | *OptionalNullable[int]*                                                                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `amount`                                                                                          | [OptionalNullable[models.ManageOrderLinesAmount]](../models/manageorderlinesamount.md)            | :heavy_minus_sign:                                                                                | In v2 endpoints, monetary amounts are represented as objects with a `currency` and `value` field. |