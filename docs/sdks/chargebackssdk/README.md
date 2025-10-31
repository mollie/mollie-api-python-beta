# ChargebacksSDK
(*chargebacks*)

## Overview

### Available Operations

* [list](#list) - List payment chargebacks
* [get](#get) - Get payment chargeback
* [all](#all) - List all chargebacks

## list

Retrieve the chargebacks initiated for a specific payment.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-chargebacks" method="get" path="/payments/{paymentId}/chargebacks" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.chargebacks.list(payment_id="tr_5B8cwPMGnU", from_="chb_xFzwUN4ci8HAmSGUACS4J", limit=50, embed="payment", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `payment_id`                                                                                                                   | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Provide the ID of the related payment.                                                                                         | tr_5B8cwPMGnU                                                                                                                  |
| `from_`                                                                                                                        | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set. | chb_xFzwUN4ci8HAmSGUACS4J                                                                                                      |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `embed`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter. |                                                                                                                                |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListChargebacksResponse](../../models/listchargebacksresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single payment chargeback by its ID and the ID of its parent payment.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-chargeback" method="get" path="/payments/{paymentId}/chargebacks/{chargebackId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.chargebacks.get(payment_id="tr_5B8cwPMGnU", chargeback_id="chb_xFzwUN4ci8HAmSGUACS4J", embed="payment", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                | Example                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `payment_id`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Provide the ID of the related payment.                                                                                     | tr_5B8cwPMGnU                                                                                                              |
| `chargeback_id`                                                                                                            | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Provide the ID of the related chargeback.                                                                                  | chb_xFzwUN4ci8HAmSGUACS4J                                                                                                  |
| `embed`                                                                                                                    | *OptionalNullable[str]*                                                                                                    | :heavy_minus_sign:                                                                                                         | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter. |                                                                                                                            |
| `idempotency_key`                                                                                                          | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                           | 123e4567-e89b-12d3-a456-426                                                                                                |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |                                                                                                                            |

### Response

**[models.EntityChargeback](../../models/entitychargeback.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## all

Retrieve all chargebacks initiated for all your payments.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-all-chargebacks" method="get" path="/chargebacks" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    profile_id="pfl_5B8cwPMGnU",
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.chargebacks.all(from_="chb_xFzwUN4ci8HAmSGUACS4J", limit=50, embed="payment", sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.     | chb_xFzwUN4ci8HAmSGUACS4J                                                                                                              |
| `limit`                                                                                                                                | *OptionalNullable[int]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                           | 50                                                                                                                                     |
| `embed`                                                                                                                                | *OptionalNullable[str]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter.         |                                                                                                                                        |
| `sort`                                                                                                                                 | [Optional[models.Sorting]](../../models/sorting.md)                                                                                    | :heavy_minus_sign:                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest. | desc                                                                                                                                   |
| `idempotency_key`                                                                                                                      | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                       | 123e4567-e89b-12d3-a456-426                                                                                                            |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |

### Response

**[models.ListAllChargebacksResponse](../../models/listallchargebacksresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |