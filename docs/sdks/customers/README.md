# Customers
(*customers*)

## Overview

### Available Operations

* [create](#create) - Create customer
* [list](#list) - List customers
* [get](#get) - Get customer
* [update](#update) - Update customer
* [delete](#delete) - Delete customer
* [create_payment](#create_payment) - Create customer payment
* [list_payments](#list_payments) - List customer payments

## create

Creates a simple minimal representation of a customer. Payments, recurring mandates, and subscriptions can be linked to this customer object, which simplifies management of recurring payments.

Once registered, customers will also appear in your Mollie dashboard.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **customers.write**](/reference/authentication)

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

    res = client.customers.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.CreateCustomerRequestBody](../../models/createcustomerrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.CreateCustomerResponseBody | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## list

Retrieve a list of all customers.

The results are paginated.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **customers.read**](/reference/authentication)

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

    res = client.customers.list(from_="cst_8wmqcHMN4U")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set.                                                                                                                                                                                                                                                         | cst_8wmqcHMN4U                                                                                                                                                                                                                                                                                                                                                                         |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListCustomersResponseBody](../../models/listcustomersresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.ListCustomersCustomersResponseBody         | 400                                               | application/hal+json                              |
| models.ListCustomersCustomersResponseResponseBody | 404                                               | application/hal+json                              |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## get

Retrieve a single customer by its ID.

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

    res = client.customers.get(id="cst_8wmqcHMN4U")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | cst_8wmqcHMN4U                                                                                                                                                                                                                                                                                                                                                                         |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetCustomerResponseBody](../../models/getcustomerresponsebody.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| models.GetCustomerCustomersResponseBody | 404                                     | application/hal+json                    |
| models.APIError                         | 4XX, 5XX                                | \*/\*                                   |

## update

Update an existing customer.

For an in-depth explanation of each parameter, refer to the [Create customer](create-customer) endpoint.

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

    res = client.customers.update(id="cst_8wmqcHMN4U")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the item you want to perform this operation on.   | cst_8wmqcHMN4U                                                      |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `email`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `locale`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `metadata`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.UpdateCustomerResponseBody | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## delete

Delete a customer. All mandates and subscriptions created for this customer will be canceled as well.

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

    res = client.customers.delete(id="cst_8wmqcHMN4U")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | cst_8wmqcHMN4U                                                                                                                                                                                                                                                                                                                                                                         |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.DeleteCustomerResponseBody | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## create_payment

Creates a payment for the customer.

Linking customers to payments enables you to:

* Keep track of payment preferences for your customers
* Allow your customers to charge a previously used credit card with a single click in our hosted checkout
* Improve payment insights in the Mollie dashboard
* Use recurring payments

This endpoint is effectively an alias of the [Create payment endpoint](create-payment) with the `customerId` parameter predefined. Please refer to the documentation of that endpoint for all possible parameters.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **payments.write**](/reference/authentication)

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

    res = client.customers.create_payment(customer_id="cst_8wmqcHMN4U", profile_id="pfl_QkEhN94Ba")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                         | Provide the ID of the related customer.                                                                                                                                                                                                                                                                                    | cst_8wmqcHMN4U                                                                                                                                                                                                                                                                                                             |
| `profile_id`                                                                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | The identifier referring to the [profile](get-profile) this entity belongs to.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted in the creation request. For organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required. | pfl_QkEhN94Ba                                                                                                                                                                                                                                                                                                              |
| `testmode`                                                                                                                                                                                                                                                                                                                 | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.               |                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                            |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.CreateCustomerPaymentResponseBody | 404                                      | application/hal+json                     |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## list_payments

Retrieve all payments linked to the customer.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **payments.read**](/reference/authentication)

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

    res = client.customers.list_payments(customer_id="cst_8wmqcHMN4U", profile_id="pfl_QkEhN94Ba")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related customer.                                                                                                                                                                                                                                                                                                                                                | cst_8wmqcHMN4U                                                                                                                                                                                                                                                                                                                                                                         |
| `profile_id`                                                                                                                                                                                                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The identifier referring to the [profile](get-profile) this entity belongs to.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted in the creation request. For organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.                                                     | pfl_QkEhN94Ba                                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListCustomerPaymentsResponseBody](../../models/listcustomerpaymentsresponsebody.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.ListCustomerPaymentsCustomersResponseBody | 404                                              | application/hal+json                             |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |