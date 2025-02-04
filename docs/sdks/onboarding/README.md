# Onboarding
(*onboarding*)

## Overview

### Available Operations

* [get](#get) - Get onboarding status
* [create](#create) - Submit onboarding data

## get

Retrieve the onboarding status of the currently authenticated organization.

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

    res = mollie.onboarding.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOnboardingStatusResponseBody](../../models/getonboardingstatusresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

**⚠️ We no longer recommend implementing this endpoint. Please refer to the Client Links API instead to kick off the onboarding process for your merchants.**

Submit data that will be prefilled in the merchant's onboarding. The data you submit will only be processed when the onboarding status is `needs-data`. Information that the merchant has entered in their dashboard will not be

overwritten.

> 🔑 Access with
>
> [Access token with **onboarding.write**](/reference/authentication)

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

    res = mollie.onboarding.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.SubmitOnboardingDataRequestBody](../../models/submitonboardingdatarequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |