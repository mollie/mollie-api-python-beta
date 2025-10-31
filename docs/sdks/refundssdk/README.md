# RefundsSDK
(*refunds*)

## Overview

### Available Operations

* [create](#create) - Create payment refund
* [list](#list) - List payment refunds
* [get](#get) - Get payment refund
* [cancel](#cancel) - Cancel payment refund
* [all](#all) - List all refunds

## create

Creates a refund for a specific payment. The refunded amount is credited to your customer usually either via a bank
transfer or by refunding the amount to your customer's credit card.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-refund" method="post" path="/payments/{paymentId}/refunds" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.refunds.create(payment_id="tr_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426", entity_refund={
        "id": "re_5B8cwPMGnU",
        "description": "Refunding a Chess Board",
        "amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "settlement_amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "metadata": {

        },
        "payment_id": "tr_5B8cwPMGnU",
        "settlement_id": "stl_5B8cwPMGnU",
        "status": mollie.RefundStatus.QUEUED,
        "external_reference": {
            "type": mollie.RefundExternalReferenceType.ACQUIRER_REFERENCE,
            "id": "123456789012345",
        },
        "reverse_routing": False,
        "routing_reversals": [
            {
                "amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "source": {
                    "type": mollie.RefundRoutingReversalsSourceType.ORGANIZATION,
                    "organization_id": "org_1234567",
                },
            },
        ],
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `payment_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related payment.                                           | tr_5B8cwPMGnU                                                                    |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `entity_refund`                                                                  | [Optional[models.EntityRefund]](../../models/entityrefund.md)                    | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityRefundResponse](../../models/entityrefundresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 409, 422        | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

Retrieve a list of all refunds created for a specific payment.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-refunds" method="get" path="/payments/{paymentId}/refunds" -->
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

    res = client_sdk.refunds.list(payment_id="tr_5B8cwPMGnU", from_="re_5B8cwPMGnU", limit=50, embed="payment", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `payment_id`                                                                                                                   | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Provide the ID of the related payment.                                                                                         | tr_5B8cwPMGnU                                                                                                                  |
| `from_`                                                                                                                        | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set. | re_5B8cwPMGnU                                                                                                                  |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `embed`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter. |                                                                                                                                |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListRefundsResponse](../../models/listrefundsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single payment refund by its ID and the ID of its parent payment.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-refund" method="get" path="/payments/{paymentId}/refunds/{refundId}" -->
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

    res = client_sdk.refunds.get(payment_id="tr_5B8cwPMGnU", refund_id="re_5B8cwPMGnU", embed="payment", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                | Example                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `payment_id`                                                                                                               | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Provide the ID of the related payment.                                                                                     | tr_5B8cwPMGnU                                                                                                              |
| `refund_id`                                                                                                                | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | Provide the ID of the related refund.                                                                                      | re_5B8cwPMGnU                                                                                                              |
| `embed`                                                                                                                    | *OptionalNullable[str]*                                                                                                    | :heavy_minus_sign:                                                                                                         | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter. |                                                                                                                            |
| `idempotency_key`                                                                                                          | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                           | 123e4567-e89b-12d3-a456-426                                                                                                |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |                                                                                                                            |

### Response

**[models.EntityRefundResponse](../../models/entityrefundresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## cancel

Refunds will be executed with a delay of two hours. Until that time, refunds may be canceled manually via the
Mollie Dashboard, or by using this endpoint.

A refund can only be canceled while its `status` field is either `queued` or `pending`. See the
[Get refund endpoint](get-refund) for more information.

### Example Usage

<!-- UsageSnippet language="python" operationID="cancel-refund" method="delete" path="/payments/{paymentId}/refunds/{refundId}" -->
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

    res = client_sdk.refunds.cancel(payment_id="tr_5B8cwPMGnU", refund_id="re_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `payment_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related payment.                                           | tr_5B8cwPMGnU                                                                    |
| `refund_id`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related refund.                                            | re_5B8cwPMGnU                                                                    |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## all

Retrieve a list of all of your refunds.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-all-refunds" method="get" path="/refunds" -->
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

    res = client_sdk.refunds.all(from_="re_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, embed="payment", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.     | re_5B8cwPMGnU                                                                                                                          |
| `limit`                                                                                                                                | *OptionalNullable[int]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                           | 50                                                                                                                                     |
| `sort`                                                                                                                                 | [Optional[models.Sorting]](../../models/sorting.md)                                                                                    | :heavy_minus_sign:                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest. | desc                                                                                                                                   |
| `embed`                                                                                                                                | *OptionalNullable[str]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter.         |                                                                                                                                        |
| `idempotency_key`                                                                                                                      | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                       | 123e4567-e89b-12d3-a456-426                                                                                                            |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |

### Response

**[models.ListAllRefundsResponse](../../models/listallrefundsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |