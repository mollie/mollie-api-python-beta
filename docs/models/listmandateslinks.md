# ListMandatesLinks

Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [models.ListMandatesSelf](../models/listmandatesself.md)                                   | :heavy_check_mark:                                                                         | The URL to the current set of items.                                                       |
| `previous`                                                                                 | [Nullable[models.ListMandatesPrevious]](../models/listmandatesprevious.md)                 | :heavy_check_mark:                                                                         | The previous set of items, if available.                                                   |
| `next`                                                                                     | [Nullable[models.ListMandatesNext]](../models/listmandatesnext.md)                         | :heavy_check_mark:                                                                         | The next set of items, if available.                                                       |
| `documentation`                                                                            | [models.ListMandatesDocumentation](../models/listmandatesdocumentation.md)                 | :heavy_check_mark:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |