# Profiles
(*profiles*)

## Overview

### Available Operations

* [create](#create) - Create profile
* [list](#list) - List profiles
* [get](#get) - Get profile
* [update](#update) - Update profile
* [delete](#delete) - Delete profile
* [get_current](#get_current) - Get current profile

## create

Create a profile to process payments on.

Profiles are required for payment processing. Normally they are created via the Mollie dashboard. Alternatively, you
can use this endpoint to automate profile creation.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-profile" method="post" path="/profiles" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.create(name="My website name", website="https://example.com", email="test@mollie.com", phone="+31208202070", description="My website description", countries_of_activity=[
        "NL",
        "GB",
    ], business_category="OTHER_MERCHANDISE")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                      | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The profile's name, this will usually reflect the trade name or brand name of the profile's website or<br/>application.                                                     | My website name                                                                                                                                                             |
| `website`                                                                                                                                                                   | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The URL to the profile's website or application. Only `https` or `http` URLs are allowed. No `@` signs are<br/>allowed.                                                     | https://example.com                                                                                                                                                         |
| `email`                                                                                                                                                                     | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The email address associated with the profile's trade name or brand.                                                                                                        | test@mollie.com                                                                                                                                                             |
| `phone`                                                                                                                                                                     | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | The phone number associated with the profile's trade name or brand.                                                                                                         | +31208202070                                                                                                                                                                |
| `description`                                                                                                                                                               | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The products or services offered by the profile's website or application.                                                                                                   | My website description                                                                                                                                                      |
| `countries_of_activity`                                                                                                                                                     | List[*str*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of countries where you expect that the majority of the profile's customers reside,<br/>in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. | [<br/>"NL",<br/>"GB"<br/>]                                                                                                                                                  |
| `business_category`                                                                                                                                                         | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | The industry associated with the profile's trade name or brand. Please refer to the<br/>[business category list](common-data-types#business-category) for all possible options. | OTHER_MERCHANDISE                                                                                                                                                           |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.CreateProfileResponse](../../models/createprofileresponse.md)**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| models.CreateProfileHalJSONError | 422                              | application/hal+json             |
| models.APIError                  | 4XX, 5XX                         | \*/\*                            |

## list

Retrieve a list of all of your profiles.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-profiles" method="get" path="/profiles" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.list(from_="pfl_QkEhN94Ba", limit=50)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `from_`                                                                                                                        | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set. | pfl_QkEhN94Ba                                                                                                                  |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListProfilesResponse](../../models/listprofilesresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ListProfilesHalJSONError | 400                             | application/hal+json            |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## get

Retrieve a single profile by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-profile" method="get" path="/profiles/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.get(id="pfl_QkEhN94Ba", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | pfl_QkEhN94Ba                                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetProfileResponse](../../models/getprofileresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.GetProfileNotFoundHalJSONError | 404                                   | application/hal+json                  |
| models.GetProfileGoneHalJSONError     | 410                                   | application/hal+json                  |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## update

Update an existing profile.

Profiles are required for payment processing. Normally they are created and updated via the Mollie dashboard.
Alternatively, you can use this endpoint to automate profile management.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-profile" method="patch" path="/profiles/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.update(id="pfl_QkEhN94Ba", name="My new website name", website="https://example.com", email="test@mollie.com", phone="+31208202071", description="My website description", countries_of_activity=[
        "NL",
        "GB",
    ], business_category="OTHER_MERCHANDISE", mode=mollie.ModeRequest.LIVE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 | Example                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                        | *str*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                          | Provide the ID of the item you want to perform this operation on.                                                                                                           | pfl_QkEhN94Ba                                                                                                                                                               |
| `name`                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The profile's name, this will usually reflect the trade name or brand name of the profile's website or<br/>application.                                                     | My new website name                                                                                                                                                         |
| `website`                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The URL to the profile's website or application. Only `https` or `http` URLs are allowed. No `@` signs<br/>are allowed.                                                     | https://example.com                                                                                                                                                         |
| `email`                                                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The email address associated with the profile's trade name or brand.                                                                                                        | test@mollie.com                                                                                                                                                             |
| `phone`                                                                                                                                                                     | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The phone number associated with the profile's trade name or brand.                                                                                                         | +31208202071                                                                                                                                                                |
| `description`                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The products or services offered by the profile's website or application.                                                                                                   | My website description                                                                                                                                                      |
| `countries_of_activity`                                                                                                                                                     | List[*str*]                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                          | A list of countries where you expect that the majority of the profile's customers reside,<br/>in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. | [<br/>"NL",<br/>"GB"<br/>]                                                                                                                                                  |
| `business_category`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                          | The industry associated with the profile's trade name or brand. Please refer to the<br/>[business category list](common-data-types) for all possible options.               | OTHER_MERCHANDISE                                                                                                                                                           |
| `mode`                                                                                                                                                                      | [OptionalNullable[models.ModeRequest]](../../models/moderequest.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                          | Updating a profile from `test` mode to `live` mode will trigger a verification process, where we review<br/>the profile before it can start accepting payments.             | live                                                                                                                                                                        |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |                                                                                                                                                                             |

### Response

**[models.UpdateProfileResponse](../../models/updateprofileresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.UpdateProfileNotFoundHalJSONError            | 404                                                 | application/hal+json                                |
| models.UpdateProfileGoneHalJSONError                | 410                                                 | application/hal+json                                |
| models.UpdateProfileUnprocessableEntityHalJSONError | 422                                                 | application/hal+json                                |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## delete

Delete a profile. A deleted profile and its related credentials can no longer be used for accepting payments.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-profile" method="delete" path="/profiles/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.delete(id="pfl_QkEhN94Ba")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the item you want to perform this operation on.   | pfl_QkEhN94Ba                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.DeleteProfileNotFoundHalJSONError | 404                                      | application/hal+json                     |
| models.DeleteProfileGoneHalJSONError     | 410                                      | application/hal+json                     |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## get_current

Retrieve the currently authenticated profile. A convenient alias of the [Get profile](get-profile)
endpoint.

For a complete reference of the profile object, refer to the [Get profile](get-profile) endpoint
documentation.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-current-profile" method="get" path="/profiles/me" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.get_current()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCurrentProfileResponse](../../models/getcurrentprofileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |