# ListPermissionsLinks

An object with several relevant URLs. Every URL object will contain an `href` and a `type` field.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `self_`                                                                                    | [Optional[models.ListPermissionsSelf]](../models/listpermissionsself.md)                   | :heavy_minus_sign:                                                                         | The URL to the current set of items.                                                       |
| `documentation`                                                                            | [Optional[models.ListPermissionsDocumentation]](../models/listpermissionsdocumentation.md) | :heavy_minus_sign:                                                                         | In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field. |