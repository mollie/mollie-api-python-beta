# WebhookEvents
(*webhook_events*)

## Overview

### Available Operations

* [get](#get) - Get a Webhook Event

## get

Retrieve a single webhook event object by its event ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-webhook-event" method="get" path="/events/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.webhook_events.get(id="event_jd9v34P5YqN9pT8n3HJyH")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the item you want to perform this operation on.   | event_jd9v34P5YqN9pT8n3HJyH                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetWebhookEventResponse](../../models/getwebhookeventresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.GetWebhookEventHalJSONError | 404                                | application/hal+json               |
| models.APIError                    | 4XX, 5XX                           | \*/\*                              |