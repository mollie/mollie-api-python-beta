# Orders
(*orders*)

## Overview

### Available Operations

* [create](#create) - Create order
* [list](#list) - List orders
* [get](#get) - Get order
* [update](#update) - Update order
* [cancel](#cancel) - Cancel order
* [manage_lines](#manage_lines) - Manage order lines
* [cancel_lines](#cancel_lines) - Cancel order lines
* [update_line](#update_line) - Update order line
* [create_payment](#create_payment) - Create order payment

## create

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

When creating an order, a payment will automatically be created to allow your customer to pay for the order. You can then redirect your customer to the URL in the `_links.checkout` property from the response, similar to the Payments API.

Unlike the Payments API, if a payment fails, expires, or is canceled, you can create a new payment under the same order using the [Create order payment endpoint](create-order-payment). This is only possible for orders that still have the `created` status.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.write**](/reference/authentication)

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

    res = client.orders.create(embed="payments", request_body={
        "order_number": "<value>",
        "lines": [
            {
                "name": "<value>",
                "quantity": 638424,
                "unit_price": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "total_amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "discount_amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "vat_amount": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "category": "meal",
            },
        ],
        "amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "billing_address": {
            "street_and_number": "<value>",
            "city": "Briaton",
            "country": "Seychelles",
        },
        "locale": "el",
        "profile_id": "pfl_QkEhN94Ba",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            | Example                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `embed`                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                     | This endpoint allows embedding related API items by appending the following values via the `embed` query string parameter.<br/><br/>* `payments`: Include all payments created for this order. | payments                                                                                                                                                                               |
| `request_body`                                                                                                                                                                         | [Optional[models.CreateOrderRequestBody]](../../models/createorderrequestbody.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                                     | N/A                                                                                                                                                                                    |                                                                                                                                                                                        |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |                                                                                                                                                                                        |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| models.CreateOrderResponseBody | 422                            | application/hal+json           |
| models.APIError                | 4XX, 5XX                       | \*/\*                          |

## list

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

Retrieve all orders.

The results are paginated.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.read**](/reference/authentication)

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

    res = client.orders.list(from_="ord_pbjz8x", sort="desc", profile_id="pfl_QkEhN94Ba")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set.                                                                                                                                                                                                                                                         | ord_pbjz8x                                                                                                                                                                                                                                                                                                                                                                             |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from newest to oldest.<br/><br/>Possible values: `asc` `desc` (default: `desc`)                                                                                                                                                                                        | desc                                                                                                                                                                                                                                                                                                                                                                                   |
| `profile_id`                                                                                                                                                                                                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The identifier referring to the [profile](get-profile) you wish to retrieve orders for.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` is already implied.<br/><br/>To retrieve all orders across the organization, use an organization-level API credential and omit the `profileId` parameter.                                         | pfl_QkEhN94Ba                                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListOrdersResponseBody](../../models/listordersresponsebody.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.ListOrdersOrdersResponseBody | 400                                 | application/hal+json                |
| models.APIError                     | 4XX, 5XX                            | \*/\*                               |

## get

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

Retrieve a single order object by its ID.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.read**](/reference/authentication)

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

    res = client.orders.get(id="ord_vsKJpSsabw", embed="payments")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | ord_vsKJpSsabw                                                                                                                                                                                                                                                                                                                                                                         |
| `embed`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | This endpoint allows embedding related API items by appending the following values via the `embed` query string parameter.<br/><br/>* `payments`: Include all payments created for this order.<br/>* `refunds`: Include all refunds created for this order.<br/>* `shipments`: Include all shipments created for this order.                                                           | payments                                                                                                                                                                                                                                                                                                                                                                               |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetOrderResponseBody](../../models/getorderresponsebody.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.GetOrderOrdersResponseBody | 404                               | application/hal+json              |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

Certain details of an existing order can be updated.

For an in-depth explanation of each parameter, see [Create order](create-order).

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.write**](/reference/authentication)

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

    res = client.orders.update(id="ord_vsKJpSsabw")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                    | ord_vsKJpSsabw                                                                                                                                                                                                                                                                                       |
| `order_number`                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `redirect_url`                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Can be updated while the order is not yet finalized.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                      |
| `cancel_url`                                                                                                                                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Can be updated while the order is not yet finalized.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                      |
| `webhook_url`                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `billing_address`                                                                                                                                                                                                                                                                                    | [OptionalNullable[models.UpdateOrderBillingAddress]](../../models/updateorderbillingaddress.md)                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | If a payment method has already been selected, the original shipping address may have already been forwarded to the payment method provider.                                                                                                                                                         |                                                                                                                                                                                                                                                                                                      |
| `shipping_address`                                                                                                                                                                                                                                                                                   | [OptionalNullable[models.UpdateOrderShippingAddress]](../../models/updateordershippingaddress.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | If a payment method has already been selected, the original billing address may have already been forwarded to the payment method provider.                                                                                                                                                          |                                                                                                                                                                                                                                                                                                      |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.UpdateOrderResponseBody       | 404                                  | application/hal+json                 |
| models.UpdateOrderOrdersResponseBody | 422                                  | application/hal+json                 |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## cancel

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

An open order may be canceled if it does not have any open payments yet, and while its status is either `created`, `authorized`, or `shipping`.

If the order was already authorized, the authorization will be released.

For an order with status `shipping`, only the order lines that were still pending will be canceled if possible. If a payment method was used that does not support authorizations, cancelation is no longer possible. You will have to issue a refund instead.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.write**](/reference/authentication)

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

    res = client.orders.cancel(id="ord_vsKJpSsabw")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | ord_vsKJpSsabw                                                                                                                                                                                                                                                                                                                                                                         |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.CancelOrderResponseBody       | 404                                  | application/hal+json                 |
| models.CancelOrderOrdersResponseBody | 422                                  | application/hal+json                 |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## manage_lines

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

Use this endpoint to update, cancel, or add one or more order lines of a `created`, `pending`, or `authorized` order.

For an already authorized order, updating the order lines will trigger an additional authorization request to the payment method provider.

For example, your customer placed an order that contains two order lines:

* Order line A contains two items and amounts to €100.00.
* Order line B contains a discount of 10% applicable to the items in order line A, which amounts to -€10.00.

The order total is €90.00.

You only have one item of type A left, and therefore contact your customer to find another solution. The customer opts to replace one of order line A's items with item C. Item C costs €40.00, however, discount B does not apply to item C.

Using this endpoint, you can create a request to update the order lines, where:

* Order line A is updated to quantity 1.
* Order line B is updated to discount amount -€5.00.
* Order line C is added with amount €40.00.

The updated order totals €85.00.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.write**](/reference/authentication)

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

    res = client.orders.manage_lines(order_id="ord_pbjz8x", operations=[

    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the related order.                                                                                                                                                                                                                                                                 | ord_pbjz8x                                                                                                                                                                                                                                                                                           |
| `operations`                                                                                                                                                                                                                                                                                         | List[[models.Operations](../../models/operations.md)]                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | List of operations to be performed on the order's line items.                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                      |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.ManageOrderLinesResponseBody | 404                                 | application/hal+json                |
| models.APIError                     | 4XX, 5XX                            | \*/\*                               |

## cancel_lines

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

Cancel one or more order lines that were previously authorized. To cancel the entire order, please refer to the [Cancel order](cancel-order) endpoint instead.

Canceling or partially canceling an order line will immediately release the authorization held for that amount. You should cancel an order line if you do not intend to (fully) ship it.

If the order line was already authorized, the authorization will be released.

For an order line with status `shipping`, the authorization for the quantity that is still pending will be released.

Afterwards, the order line will be marked `completed`.

If the order line is `paid` or already `completed`, you can create a refund using the [Create order refund](create-order-refund) endpoint instead.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.write**](/reference/authentication)

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

    res = client.orders.cancel_lines(order_id="ord_pbjz8x", lines=[
        {
            "id": "<id>",
            "amount": {
                "currency": "EUR",
                "value": "10.00",
            },
        },
        {
            "id": "<id>",
            "amount": {
                "currency": "EUR",
                "value": "10.00",
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the related order.                                                                                                                                                                                                                                                                 | ord_pbjz8x                                                                                                                                                                                                                                                                                           |
| `lines`                                                                                                                                                                                                                                                                                              | List[[models.CancelOrderLinesLines](../../models/cancelorderlineslines.md)]                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| models.CancelOrderLinesResponseBody       | 404                                       | application/hal+json                      |
| models.CancelOrderLinesOrdersResponseBody | 422                                       | application/hal+json                      |
| models.APIError                           | 4XX, 5XX                                  | \*/\*                                     |

## update_line

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

Update an order line belonging to an order. Only lines with status `created`, `pending`, or `authorized` can be updated.

This endpoint is useful for cases where specific details of an order line are changed. For example, if a customer changes a red shirt for a blue one of the same model. In this case only specific properties of the order line need to be updated, such as the `name`, the `imageUrl`, and perhaps the `amount`.

To swap out an order line for an entirely new order line, use the [Manage order lines](manage-order-lines) endpoint instead.

For an in-depth explanation of each parameter, refer to the `lines` parameter of the [Create order](create-order) endpoint.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **orders.write**](/reference/authentication)

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

    res = client.orders.update_line(order_id="ord_pbjz8x", id="odl_dgtxyl", unit_price={
        "currency": "EUR",
        "value": "10.00",
    }, discount_amount={
        "currency": "EUR",
        "value": "10.00",
    }, total_amount={
        "currency": "EUR",
        "value": "10.00",
    }, vat_amount={
        "currency": "EUR",
        "value": "10.00",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_id`                                                                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the related order.                                                                                                                                                                                                                                                                 | ord_pbjz8x                                                                                                                                                                                                                                                                                           |
| `id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                    | odl_dgtxyl                                                                                                                                                                                                                                                                                           |
| `name`                                                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `image_url`                                                                                                                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `product_url`                                                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `sku`                                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `metadata`                                                                                                                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `quantity`                                                                                                                                                                                                                                                                                           | *OptionalNullable[int]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Required when a `unitPrice`, `discountAmount`, `totalAmount`, `vatAmount`, or `vatRate` is also provided in the same request.                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                      |
| `unit_price`                                                                                                                                                                                                                                                                                         | [OptionalNullable[models.UpdateOrderLineUnitPrice]](../../models/updateorderlineunitprice.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Required when a `quantity`, `discountAmount`, `totalAmount`, `vatAmount`, or `vatRate` is also provided in the same request.                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                      |
| `discount_amount`                                                                                                                                                                                                                                                                                    | [OptionalNullable[models.UpdateOrderLineDiscountAmount]](../../models/updateorderlinediscountamount.md)                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | In v2 endpoints, monetary amounts are represented as objects with a `currency` and `value` field.                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      |
| `total_amount`                                                                                                                                                                                                                                                                                       | [OptionalNullable[models.UpdateOrderLineTotalAmount]](../../models/updateorderlinetotalamount.md)                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Required when a `quantity`, `unitPrice`, `discountAmount`, `vatAmount`, or `vatRate` is also provided in the same request.                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                      |
| `vat_amount`                                                                                                                                                                                                                                                                                         | [OptionalNullable[models.UpdateOrderLineVatAmount]](../../models/updateorderlinevatamount.md)                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Required when a `quantity`, `unitPrice`, `discountAmount`, `totalAmount`, or `vatRate` is also provided in the same request.                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                      |
| `vat_rate`                                                                                                                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Required when a `quantity`, `unitPrice`, `discountAmount`, `totalAmount`, or `vatAmount` is also provided in the same request.                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                      |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.UpdateOrderLineResponseBody       | 404                                      | application/hal+json                     |
| models.UpdateOrderLineOrdersResponseBody | 422                                      | application/hal+json                     |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## create_payment

**⚠️ We no longer recommend implementing the Orders API. Please refer to the Payments API instead. We are actively working on adding support for Klarna, Billie, in3 and Vouchers to the Payments API later this year.**

An order has an automatically created payment that your customer can use to pay for the order. When the payment expires you can create a new payment for the order using this endpoint. A maximum of 25 payments can be created for an order.

A new payment can only be created while the status of the order is `created`, and when the status of the existing payment is either `expired`, `canceled` or `failed`.

The endpoint accepts virtually all parameters accepted by the regular [Create payment](create-payment) endpoint. Please refer to that endpoint for the full documentation of all parameters.

The payment inherits certain properties, such as the `amount` and `webhookUrl`, directly from the order. These cannot be changed via this endpoint.

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

    res = client.orders.create_payment(order_id="ord_pbjz8x")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `order_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the related order.                                | ord_pbjz8x                                                          |
| `request_body`                                                      | *Optional[Any]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.CreateOrderPaymentResponseBody | 404                                   | application/hal+json                  |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |