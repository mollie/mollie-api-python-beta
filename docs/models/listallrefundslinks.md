# ListAllRefundsLinks

Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [models.ListAllRefundsSelf](../models/listallrefundsself.md)                               | :heavy_check_mark:                                                                         | The URL to the current set of items.                                                       |
| `previous`                                                                                 | [Nullable[models.ListAllRefundsPrevious]](../models/listallrefundsprevious.md)             | :heavy_check_mark:                                                                         | The previous set of items, if available.                                                   |
| `next`                                                                                     | [Nullable[models.ListAllRefundsNext]](../models/listallrefundsnext.md)                     | :heavy_check_mark:                                                                         | The next set of items, if available.                                                       |
| `documentation`                                                                            | [models.ListAllRefundsDocumentation](../models/listallrefundsdocumentation.md)             | :heavy_check_mark:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |