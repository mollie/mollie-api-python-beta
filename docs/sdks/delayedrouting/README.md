# DelayedRouting
(*delayed_routing*)

## Overview

### Available Operations

* [create](#create) - Create a delayed route
* [list](#list) - List payment routes

## create

Create a route for a specific payment. The routed amount is credited to the account of your customer.

> 🔑 Access with
>
> [API key](/reference/authentication)

### Example Usage

```python
import mollie_api_python_alpha
from mollie_api_python_alpha import Client
import os


with Client(
    security=mollie_api_python_alpha.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.delayed_routing.create(payment_id="tr_5B8cwPMGnU6qLbRvo7qEZo", amount={
        "currency": "EUR",
        "value": "10.00",
    }, description="Payment for Order #12345", destination={
        "organization_id": "org_123",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `payment_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | Provide the ID of the related payment.                                                             | tr_5B8cwPMGnU6qLbRvo7qEZo                                                                          |
| `amount`                                                                                           | [Optional[models.PaymentCreateRouteAmount]](../../models/paymentcreaterouteamount.md)              | :heavy_minus_sign:                                                                                 | The portion of the total payment amount being routed. Currently only `EUR` payments can be routed. |                                                                                                    |
| `description`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The description of the route. This description is shown in the reports.                            | Payment for Order #12345                                                                           |
| `destination`                                                                                      | [Optional[models.PaymentCreateRouteDestination]](../../models/paymentcreateroutedestination.md)    | :heavy_minus_sign:                                                                                 | The destination of this portion of the payment.                                                    |                                                                                                    |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |                                                                                                    |

### Response

**[models.PaymentCreateRouteResponseBody](../../models/paymentcreaterouteresponsebody.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.PaymentCreateRouteDelayedRoutingResponseBody | 404                                                 | application/hal+json                                |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## list

Retrieve a list of all routes created for a specific payment.

> 🔑 Access with
>
> [API key](/reference/authentication)

### Example Usage

```python
import mollie_api_python_alpha
from mollie_api_python_alpha import Client
import os


with Client(
    security=mollie_api_python_alpha.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.delayed_routing.list(payment_id="tr_5B8cwPMGnU6qLbRvo7qEZo")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `payment_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the related payment.                              | tr_5B8cwPMGnU6qLbRvo7qEZo                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PaymentListRoutesResponseBody](../../models/paymentlistroutesresponsebody.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.PaymentListRoutesDelayedRoutingResponseBody | 404                                                | application/hal+json                               |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |