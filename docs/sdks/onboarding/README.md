# Onboarding
(*onboarding*)

## Overview

### Available Operations

* [get](#get) - Get onboarding status
* [submit](#submit) - Submit onboarding data

## get

Retrieve the onboarding status of the currently authenticated organization.

> 🔑 Access with
>
> [Access token with **onboarding.read**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="get-onboarding-status" method="get" path="/onboarding/me" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.onboarding.get()

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

## submit

**⚠️ We no longer recommend implementing this endpoint. Please refer to the Client Links API instead to kick off the onboarding process for your merchants.**

Submit data that will be prefilled in the merchant's onboarding. The data you submit will only be processed when the onboarding status is `needs-data`. Information that the merchant has entered in their dashboard will not be overwritten.

> 🔑 Access with
>
> [Access token with **onboarding.write**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="submit-onboarding-data" method="post" path="/onboarding/me" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.onboarding.submit(request={
        "organization": {
            "name": "Mollie B.V.",
            "registration_number": "30204462",
            "vat_number": "NL815839091B01",
            "vat_regulation": "dutch",
        },
        "profile": {
            "name": "Mollie",
            "url": "https://www.mollie.com",
            "email": "info@mollie.com",
            "phone": "+31208202070",
            "description": "Payment service provider",
            "business_category": "MONEY_SERVICES",
        },
    })

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