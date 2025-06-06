# WebhookEvents
(*webhook_events*)

## Overview

### Available Operations

* [get_event](#get_event) - Get a Webhook Event

## get_event

Retrieve a single webhook event object by its event ID.

> 🔑 Access with
>
> [Access token with **events.read**](/reference/authentication)

### Example Usage

```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.webhook_events.get_event(id="event_jd9v34P5YqN9pT8n3HJyH")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the item you want to perform this operation on.   | event_jd9v34P5YqN9pT8n3HJyH                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetWebhookEventResponseBody](../../models/getwebhookeventresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.GetWebhookEventWebhookEventsResponseBody | 404                                             | application/hal+json                            |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |