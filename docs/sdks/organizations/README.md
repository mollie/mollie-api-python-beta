# Organizations
(*organizations*)

## Overview

### Available Operations

* [get](#get) - Get organization
* [get_current](#get_current) - Get current organization
* [get_partner_status](#get_partner_status) - Get partner status

## get

Retrieve a single organization by its ID.

You can normally only retrieve the currently authenticated organization with this endpoint. This is primarily useful for OAuth apps. See also [Get current organization](get-current-organization).

If you have a *partner account*', you can retrieve organization details of connected organizations.

> 🔑 Access with
>
> [Access token with **organizations.read**](/reference/authentication)

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

    res = client.organizations.get(id="org_12345678")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | org_12345678                                                                                                                                                                                                                                                                                                                                                                           |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetOrganizationResponseBody](../../models/getorganizationresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.GetOrganizationOrganizationsResponseBody | 404                                             | application/hal+json                            |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## get_current

Retrieve the currently authenticated organization. A convenient alias of the [Get organization](get-organization) endpoint.

For a complete reference of the organization object, refer to the [Get organization](get-organization) endpoint documentation.

> 🔑 Access with
>
> [Access token with **organizations.read**](/reference/authentication)

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

    res = client.organizations.get_current()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_partner_status

Retrieve partnership details about the currently authenticated organization. Only relevant for so-called *partner accounts*.

> 🔑 Access with
>
> [Access token with **organizations.read**](/reference/authentication)

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

    res = client.organizations.get_partner_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPartnerStatusResponseBody](../../models/getpartnerstatusresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |