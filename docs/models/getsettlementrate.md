# GetSettlementRate

The service rates, further divided into `fixed` and `percentage` costs.


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `fixed`                                                                                           | [Optional[models.GetSettlementFixed]](../models/getsettlementfixed.md)                            | :heavy_minus_sign:                                                                                | In v2 endpoints, monetary amounts are represented as objects with a `currency` and `value` field. |
| `percentage`                                                                                      | [Optional[models.GetSettlementPercentage]](../models/getsettlementpercentage.md)                  | :heavy_minus_sign:                                                                                | In v2 endpoints, monetary amounts are represented as objects with a `currency` and `value` field. |