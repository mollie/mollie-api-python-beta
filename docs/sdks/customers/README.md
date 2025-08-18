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

Creates a simple minimal representation of a customer. Payments, recurring mandates, and subscriptions can be linked
to this customer object, which simplifies management of recurring payments.

Once registered, customers will also appear in your Mollie dashboard.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-customer" method="post" path="/customers" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.create(request={
        "name": "John Doe",
        "email": "example@email.com",
        "locale": mollie.CreateCustomerLocaleRequest.EN_US,
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateCustomerRequest](../../models/createcustomerrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateCustomerResponse](../../models/createcustomerresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.CreateCustomerHalJSONError | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## list

Retrieve a list of all customers.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/customers" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.list(from_="cst_5B8cwPMGnU", limit=50, sort=mollie.ListCustomersSort.DESC, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     | cst_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                 | [OptionalNullable[models.ListCustomersSort]](../../models/listcustomerssort.md)                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                                                                                             | desc                                                                                                                                                                                                                                                                                                                                                                                   |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListCustomersResponse](../../models/listcustomersresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| models.ListCustomersBadRequestHalJSONError | 400                                        | application/hal+json                       |
| models.ListCustomersNotFoundHalJSONError   | 404                                        | application/hal+json                       |
| models.APIError                            | 4XX, 5XX                                   | \*/\*                                      |

## get

Retrieve a single customer by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/customers/{customerId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.get(customer_id="cst_5B8cwPMGnU", include=mollie.GetCustomerInclude.EVENTS, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related customer.                                                                                                                                                                                                                                                                                                                                                | cst_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `include`                                                                                                                                                                                                                                                                                                                                                                              | [OptionalNullable[models.GetCustomerInclude]](../../models/getcustomerinclude.md)                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | This endpoint allows you to include additional information via the `include` query string parameter.                                                                                                                                                                                                                                                                                   | events                                                                                                                                                                                                                                                                                                                                                                                 |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetCustomerResponse](../../models/getcustomerresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.GetCustomerHalJSONError | 404                            | application/hal+json           |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## update

Update an existing customer.

For an in-depth explanation of each parameter, refer to the [Create customer](create-customer) endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-customer" method="patch" path="/customers/{customerId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.update(customer_id="cst_5B8cwPMGnU", request_body={
        "name": "John Doe",
        "email": "example@email.com",
        "locale": mollie.UpdateCustomerLocaleRequest.EN_US,
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `customer_id`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | Provide the ID of the related customer.                                                 | cst_5B8cwPMGnU                                                                          |
| `request_body`                                                                          | [Optional[models.UpdateCustomerRequestBody]](../../models/updatecustomerrequestbody.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[models.UpdateCustomerResponse](../../models/updatecustomerresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.UpdateCustomerHalJSONError | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## delete

Delete a customer. All mandates and subscriptions created for this customer will be canceled as well.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-customer" method="delete" path="/customers/{customerId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.delete(customer_id="cst_5B8cwPMGnU", request_body={
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `customer_id`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | Provide the ID of the related customer.                                                 | cst_5B8cwPMGnU                                                                          |
| `request_body`                                                                          | [Optional[models.DeleteCustomerRequestBody]](../../models/deletecustomerrequestbody.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.DeleteCustomerHalJSONError | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## create_payment

Creates a payment for the customer.

Linking customers to payments enables you to:

* Keep track of payment preferences for your customers
* Allow your customers to charge a previously used credit card with a single click in our hosted checkout
* Improve payment insights in the Mollie dashboard
* Use recurring payments

This endpoint is effectively an alias of the [Create payment endpoint](create-payment) with the `customerId`
parameter predefined.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-customer-payment" method="post" path="/customers/{customerId}/payments" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.create_payment(customer_id="cst_5B8cwPMGnU", request_body={
        "description": "Chess Board",
        "amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "redirect_url": "https://example.org/redirect",
        "cancel_url": "https://example.org/cancel",
        "webhook_url": "https://example.org/webhooks",
        "lines": [
            {
                "type": mollie.CreateCustomerPaymentLineTypeRequest.PHYSICAL,
                "description": "LEGO 4440 Forest Police Station",
                "quantity": 1,
                "quantity_unit": "pcs",
                "unit_price": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "discount_amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "total_amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "vat_rate": "21.00",
                "vat_amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "sku": "9780241661628",
                "categories": [
                    mollie.CreateCustomerPaymentCategoryRequest.MEAL,
                    mollie.CreateCustomerPaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreateCustomerPaymentIntervalRequest.DOT_DOT_DOT_MONTHS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
        ],
        "billing_address": {
            "title": "Mr.",
            "given_name": "Piet",
            "family_name": "Mondriaan",
            "organization_name": "Mollie B.V.",
            "street_and_number": "Keizersgracht 126",
            "street_additional": "Apt. 1",
            "postal_code": "1234AB",
            "email": "piet@example.org",
            "phone": "31208202070",
            "city": "Amsterdam",
            "region": "Noord-Holland",
            "country": "NL",
        },
        "shipping_address": {
            "title": "Mr.",
            "given_name": "Piet",
            "family_name": "Mondriaan",
            "organization_name": "Mollie B.V.",
            "street_and_number": "Keizersgracht 126",
            "street_additional": "Apt. 1",
            "postal_code": "1234AB",
            "email": "piet@example.org",
            "phone": "31208202070",
            "city": "Amsterdam",
            "region": "Noord-Holland",
            "country": "NL",
        },
        "locale": mollie.CreateCustomerPaymentLocaleRequest.EN_US,
        "method": mollie.CreateCustomerPaymentMethodRequest.IDEAL,
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": mollie.CreateCustomerPaymentCaptureModeRequest.MANUAL,
        "capture_delay": "8 hours",
        "application_fee": {
            "amount": {
                "currency": "EUR",
                "value": "10.00",
            },
            "description": "10",
        },
        "routing": [
            {
                "amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "destination": {
                    "type": mollie.CreateCustomerPaymentRoutingTypeRequest.ORGANIZATION,
                    "organization_id": "org_1234567",
                },
                "release_date": "2024-12-12",
                "links": {
                    "self_": {
                        "href": "https://...",
                        "type": "application/hal+json",
                    },
                    "payment": {
                        "href": "https://...",
                        "type": "application/hal+json",
                    },
                },
            },
            {
                "amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "destination": {
                    "type": mollie.CreateCustomerPaymentRoutingTypeRequest.ORGANIZATION,
                    "organization_id": "org_1234567",
                },
                "release_date": "2024-12-12",
                "links": {
                    "self_": {
                        "href": "https://...",
                        "type": "application/hal+json",
                    },
                    "payment": {
                        "href": "https://...",
                        "type": "application/hal+json",
                    },
                },
            },
        ],
        "sequence_type": mollie.CreateCustomerPaymentSequenceTypeRequest.ONEOFF,
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                         | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Provide the ID of the related customer.                                                               | cst_5B8cwPMGnU                                                                                        |
| `request_body`                                                                                        | [Optional[models.CreateCustomerPaymentRequestBody]](../../models/createcustomerpaymentrequestbody.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.CreateCustomerPaymentResponse](../../models/createcustomerpaymentresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.CreateCustomerPaymentUnprocessableEntityHalJSONError | 422                                                         | application/hal+json                                        |
| models.CreateCustomerPaymentServiceUnavailableHalJSONError  | 503                                                         | application/hal+json                                        |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## list_payments

Retrieve all payments linked to the customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-customer-payments" method="get" path="/customers/{customerId}/payments" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.list_payments(customer_id="cst_5B8cwPMGnU", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.ListCustomerPaymentsSort.DESC, profile_id="pfl_5B8cwPMGnU", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related customer.                                                                                                                                                                                                                                                                                                                                                | cst_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate<br/>the result set.                                                                                                                                                                                                                                                     | tr_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                 | [OptionalNullable[models.ListCustomerPaymentsSort]](../../models/listcustomerpaymentssort.md)                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                                                                                             | desc                                                                                                                                                                                                                                                                                                                                                                                   |
| `profile_id`                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The identifier referring to the [profile](get-profile) you wish to<br/>retrieve the resources for.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted. For<br/>organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.                                                     | pfl_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListCustomerPaymentsResponse](../../models/listcustomerpaymentsresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| models.ListCustomerPaymentsHalJSONError | 400                                     | application/hal+json                    |
| models.APIError                         | 4XX, 5XX                                | \*/\*                                   |