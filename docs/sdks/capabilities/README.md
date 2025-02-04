# Capabilities
(*capabilities*)

## Overview

### Available Operations

* [list](#list) - List capabilities

## list

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a list of capabilities for an organization.

This API provides detailed insights into the specific requirements and status of each client's onboarding journey.

Capabilities are at the organization level, indicating if the organization can perform a given capability.

For payments, regardless them being at the profile level, the capability is listed at the organization level. This means that if at least one of the clients's profiles can receive payments, the payments capability is enabled, communicating that the organization can indeed receive payments.

> 🔑 Access with
>
> [Access token with **onboarding.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.capabilities.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListCapabilitiesResponseBody](../../models/listcapabilitiesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |