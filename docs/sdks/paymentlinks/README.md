# PaymentLinks
(*payment_links*)

## Overview

### Available Operations

* [create](#create) - Create payment link
* [list](#list) - List payment links
* [get](#get) - Get payment link
* [update](#update) - Update payment link
* [delete](#delete) - Delete payment link
* [list_payments](#list_payments) - Get payment link payments

## create

With the Payment links API you can generate payment links that by default, unlike regular payments, do not expire.
The payment link can be shared with your customers and will redirect them to them the payment page where they can
complete the payment. A [payment](get-payment) will only be created once the customer initiates the payment.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-payment-link" method="post" path="/payment-links" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.create(request={
        "description": "Chess Board",
        "amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "minimum_amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "redirect_url": "https://webshop.example.org/payment-links/redirect/",
        "webhook_url": "https://webshop.example.org/payment-links/webhook/",
        "lines": [
            {
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
                    mollie.CreatePaymentLinkCategoryRequest.MEAL,
                    mollie.CreatePaymentLinkCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
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
        "profile_id": "pfl_QkEhN94Ba",
        "expires_at": "2025-12-24T11:00:16+00:00",
        "allowed_methods": [
            "ideal",
        ],
        "application_fee": {
            "amount": {
                "currency": "EUR",
                "value": "10.00",
            },
            "description": "Platform fee",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreatePaymentLinkRequest](../../models/createpaymentlinkrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreatePaymentLinkResponse](../../models/createpaymentlinkresponse.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.CreatePaymentLinkNotFoundHalJSONError            | 404                                                     | application/hal+json                                    |
| models.CreatePaymentLinkUnprocessableEntityHalJSONError | 422                                                     | application/hal+json                                    |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## list

Retrieve a list of all payment links.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-payment-links" method="get" path="/payment-links" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.list(from_="pl_d9fQur83kFdhH8hIhaZfq", limit=50, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                               |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListPaymentLinksResponse](../../models/listpaymentlinksresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.ListPaymentLinksHalJSONError | 400                                 | application/hal+json                |
| models.APIError                     | 4XX, 5XX                            | \*/\*                               |

## get

Retrieve a single payment link by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-payment-link" method="get" path="/payment-links/{paymentLinkId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.get(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related payment link.                                                                                                                                                                                                                                                                                                                                            | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                               |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetPaymentLinkResponse](../../models/getpaymentlinkresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.GetPaymentLinkHalJSONError | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update

Certain details of an existing payment link can be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-payment-link" method="patch" path="/payment-links/{paymentLinkId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.update(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", description="Chess Board", minimum_amount={
        "currency": "EUR",
        "value": "10.00",
    }, archived=False, allowed_methods=[
        "ideal",
    ], lines=[
        {
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
                mollie.UpdatePaymentLinkCategoryRequest.MEAL,
                mollie.UpdatePaymentLinkCategoryRequest.ECO,
            ],
            "image_url": "https://...",
            "product_url": "https://...",
        },
    ], billing_address={
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
    }, shipping_address={
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
    }, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `payment_link_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Provide the ID of the related payment link.                                                                                                                                                                                                                                                                                                                                                                                                                                    | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `description`                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | A short description of the payment link. The description is visible in the Dashboard and will be shown<br/>on the customer's bank or card statement when possible.<br/><br/>Updating the description does not affect any previously existing payments created for this payment link.                                                                                                                                                                                           | Chess Board                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `minimum_amount`                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Optional[models.UpdatePaymentLinkMinimumAmountRequest]](../../models/updatepaymentlinkminimumamountrequest.md)                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The minimum amount of the payment link. This property is only allowed when there is no amount provided.<br/>The customer will be prompted to enter a value greater than or equal to the minimum amount.                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `archived`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Whether the payment link is archived. Customers will not be able to complete payments on archived<br/>payment links.                                                                                                                                                                                                                                                                                                                                                           | false                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `allowed_methods`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | An array of payment methods that are allowed to be used for this payment link. When this parameter is<br/>not provided or is an empty array, all enabled payment methods will be available.<br/><br/>Enum: 'applepay', 'bancomatpay', 'bancontact', 'banktransfer', 'belfius', 'blik', 'creditcard', 'eps', 'giftcard',<br/>'ideal', 'kbc', 'mybank', 'paybybank', 'paypal', 'paysafecard', 'pointofsale', 'przelewy24', 'satispay', 'trustly', 'twint',<br/>'in3', 'riverty', 'klarna', 'billie'. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `lines`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | List[[models.UpdatePaymentLinkLineRequest](../../models/updatepaymentlinklinerequest.md)]                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Optionally provide the order lines for the payment. Each line contains details such as a description of the item<br/>ordered and its price.<br/><br/>All lines must have the same currency as the payment.<br/><br/>Required for payment methods `billie`, `in3`, `klarna`, `riverty` and `voucher`.                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `billing_address`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Optional[models.UpdatePaymentLinkBillingAddressRequest]](../../models/updatepaymentlinkbillingaddressrequest.md)                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The customer's billing address details. We advise to provide these details to improve fraud protection and<br/>conversion.<br/><br/>Should include `email` or a valid postal address consisting of `streetAndNumber`, `postalCode`, `city` and<br/>`country`.<br/><br/>Required for payment method `in3`, `klarna`, `billie` and `riverty`.                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `shipping_address`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [Optional[models.UpdatePaymentLinkShippingAddressRequest]](../../models/updatepaymentlinkshippingaddressrequest.md)                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The customer's shipping address details. We advise to provide these details to improve fraud protection and<br/>conversion.<br/><br/>Should include `email` or a valid postal address consisting of `streetAndNumber`, `postalCode`, `city` and<br/>`country`.                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials<br/>such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.                                                                                                                                                               | false                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.UpdatePaymentLinkResponse](../../models/updatepaymentlinkresponse.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.UpdatePaymentLinkNotFoundHalJSONError            | 404                                                     | application/hal+json                                    |
| models.UpdatePaymentLinkUnprocessableEntityHalJSONError | 422                                                     | application/hal+json                                    |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## delete

Payment links which have not been opened and no payments have been made yet can be deleted entirely.
This can be useful for removing payment links that have been incorrectly configured or that are no longer relevant.

Once deleted, the payment link will no longer show up in the API or Mollie dashboard.

To simply disable a payment link without fully deleting it, you can use the `archived` parameter on the
[Update payment link](update-payment-link) endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-payment-link" method="delete" path="/payment-links/{paymentLinkId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.delete(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the related payment link.                                                                                                                                                                                                                                                          | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                             |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials<br/>such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.DeletePaymentLinkNotFoundHalJSONError            | 404                                                     | application/hal+json                                    |
| models.DeletePaymentLinkUnprocessableEntityHalJSONError | 422                                                     | application/hal+json                                    |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## list_payments

Retrieve the list of payments for a specific payment link.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-payment-link-payments" method="get" path="/payment-links/{paymentLinkId}/payments" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.list_payments(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.GetPaymentLinkPaymentsSort.DESC, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related payment link.                                                                                                                                                                                                                                                                                                                                            | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                               |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     | tr_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                 | [OptionalNullable[models.GetPaymentLinkPaymentsSort]](../../models/getpaymentlinkpaymentssort.md)                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                                                                                             | desc                                                                                                                                                                                                                                                                                                                                                                                   |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetPaymentLinkPaymentsResponse](../../models/getpaymentlinkpaymentsresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| models.GetPaymentLinkPaymentsHalJSONError | 400                                       | application/hal+json                      |
| models.APIError                           | 4XX, 5XX                                  | \*/\*                                     |