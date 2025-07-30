# SalesInvoices
(*sales_invoices*)

## Overview

### Available Operations

* [create](#create) - Create sales invoice
* [list](#list) - List sales invoices
* [get](#get) - Get sales invoice
* [update](#update) - Update sales invoice
* [delete](#delete) - Delete sales invoice

## create

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

With the Sales Invoice API you can generate sales invoices to send to your customers.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **sales-invoices.write**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="create-sales-invoice" method="post" path="/sales-invoices" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.sales_invoices.create(request={
        "testmode": False,
        "profile_id": "pfl_QkEhN94Ba",
        "status": "draft",
        "memo": "This is a memo!",
        "payment_details": {
            "source": "payment-link",
            "source_reference": "pl_d9fQur83kFdhH8hIhaZfq",
        },
        "email_details": {
            "subject": "Your invoice is available",
            "body": "Please find your invoice enclosed.",
        },
        "customer_id": "cst_8wmqcHMN4U",
        "mandate_id": "mdt_pWUnw6pkBN",
        "recipient_identifier": "customer-xyz-0123",
        "recipient": {
            "type": "consumer",
            "title": "Mrs.",
            "given_name": "Jane",
            "family_name": "Doe",
            "organization_name": "Organization Corp.",
            "organization_number": "12345678",
            "vat_number": "NL123456789B01",
            "email": "example@email.com",
            "phone": "+0123456789",
            "street_and_number": "Keizersgracht 126",
            "street_additional": "4th floor",
            "postal_code": "5678AB",
            "city": "Amsterdam",
            "region": "Noord-Holland",
            "country": "NL",
            "locale": "nl_NL",
        },
        "lines": [],
        "discount": {
            "type": "amount",
            "value": "10.00",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.CreateSalesInvoiceRequestBody](../../models/createsalesinvoicerequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.CreateSalesInvoiceResponseBody](../../models/createsalesinvoiceresponsebody.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.CreateSalesInvoiceSalesInvoicesResponseBody         | 404                                                        | application/hal+json                                       |
| models.CreateSalesInvoiceSalesInvoicesResponseResponseBody | 422                                                        | application/hal+json                                       |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## list

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a list of all sales invoices created through the API.

The results are paginated.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **sales-invoices.read**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="list-sales-invoices" method="get" path="/sales-invoices" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.sales_invoices.list(from_="invoice_4Y0eZitmBnQ6IDoMqZQKh", limit=50, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set.                                                                                                                                                                                                                                                         | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListSalesInvoicesResponseBody](../../models/listsalesinvoicesresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.ListSalesInvoicesSalesInvoicesResponseBody | 400                                               | application/hal+json                              |
| models.APIError                                   | 4XX, 5XX                                          | \*/\*                                             |

## get

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a single sales invoice by its ID.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **sales-invoice.read**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="get-sales-invoice" method="get" path="/sales-invoices/{id}" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.sales_invoices.get(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetSalesInvoiceResponseBody](../../models/getsalesinvoiceresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.GetSalesInvoiceSalesInvoicesResponseBody | 404                                             | application/hal+json                            |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## update

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Certain details of an existing sales invoice can be updated. For `draft` it is all values listed below, but for statuses `paid` and `issued` there are certain additional requirements (`paymentDetails` and `emailDetails`, respectively).

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **sales-invoices.write**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="update-sales-invoice" method="patch" path="/sales-invoices/{id}" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.sales_invoices.update(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", testmode=False, status="paid", memo="An updated memo!", payment_details={
        "source": "payment-link",
        "source_reference": "pl_d9fQur83kFdhH8hIhaZfq",
    }, email_details={
        "subject": "Your invoice is available",
        "body": "Please find your invoice enclosed.",
    }, recipient_identifier="customer-xyz-0123", recipient={
        "type": "consumer",
        "title": "Mrs.",
        "given_name": "Jane",
        "family_name": "Doe",
        "organization_name": "Organization Corp.",
        "organization_number": "12345678",
        "vat_number": "NL123456789B01",
        "email": "example@email.com",
        "phone": "+0123456789",
        "street_and_number": "Keizersgracht 126",
        "street_additional": "4th floor",
        "postal_code": "5678AB",
        "city": "Amsterdam",
        "region": "Noord-Holland",
        "country": "NL",
        "locale": "nl_NL",
    }, lines=[
        {
            "description": "LEGO 4440 Forest Police Station",
            "quantity": 1,
            "vat_rate": "21.00",
            "unit_price": {
                "currency": "EUR",
                "value": "10.00",
            },
            "discount": {
                "type": "amount",
                "value": "10.00",
            },
        },
    ], discount={
        "type": "amount",
        "value": "10.00",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                    | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                |
| `status`                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The status for the invoice to end up in.<br/><br/>Dependent parameters: `paymentDetails` for `paid`, `emailDetails` for `issued` and `paid`.<br/><br/>Possible values: `draft` `issued` `paid`                                                                                                       | paid                                                                                                                                                                                                                                                                                                 |
| `memo`                                                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | A free-form memo you can set on the invoice, and will be shown on the invoice PDF.                                                                                                                                                                                                                   | An updated memo!                                                                                                                                                                                                                                                                                     |
| `payment_term`                                                                                                                                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The payment term to be set on the invoice.<br/><br/>Possible values: `7 days` `14 days` `30 days` `45 days` `60 days` `90 days` `120 days` (default: `30 days`)                                                                                                                                      |                                                                                                                                                                                                                                                                                                      |
| `payment_details`                                                                                                                                                                                                                                                                                    | [OptionalNullable[models.UpdateSalesInvoicePaymentDetails]](../../models/updatesalesinvoicepaymentdetails.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Used when setting an invoice to status of `paid`, and will store a payment that fully pays the invoice with the provided details. Required for `paid` status.                                                                                                                                        |                                                                                                                                                                                                                                                                                                      |
| `email_details`                                                                                                                                                                                                                                                                                      | [OptionalNullable[models.UpdateSalesInvoiceEmailDetails]](../../models/updatesalesinvoiceemaildetails.md)                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Used when setting an invoice to status of either `issued` or `paid`. Will be used to issue the invoice to the recipient with the provided `subject` and `body`. Required for `issued` status.                                                                                                        |                                                                                                                                                                                                                                                                                                      |
| `recipient_identifier`                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | An identifier tied to the recipient data. This should be a unique value based on data your system contains, so that both you and us know who we're referring to. It is a value you provide to us so that recipient management is not required to send a first invoice to a recipient.                | customer-xyz-0123                                                                                                                                                                                                                                                                                    |
| `recipient`                                                                                                                                                                                                                                                                                          | [OptionalNullable[models.UpdateSalesInvoiceRecipient]](../../models/updatesalesinvoicerecipient.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The recipient object should contain all the information relevant to create an invoice for an intended recipient. This data will be stored, updated, and re-used as appropriate, based on the `recipientIdentifier`.                                                                                  |                                                                                                                                                                                                                                                                                                      |
| `lines`                                                                                                                                                                                                                                                                                              | List[[models.UpdateSalesInvoiceLines](../../models/updatesalesinvoicelines.md)]                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Provide the line items for the invoice. Each line contains details such as a description of the item ordered and its price.<br/><br/>All lines must have the same currency as the invoice.                                                                                                           |                                                                                                                                                                                                                                                                                                      |
| `discount`                                                                                                                                                                                                                                                                                           | [OptionalNullable[models.UpdateSalesInvoiceSalesInvoicesDiscount]](../../models/updatesalesinvoicesalesinvoicesdiscount.md)                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The discount to be applied to the entire invoice, possibly on top of the line item discounts.                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[models.UpdateSalesInvoiceResponseBody](../../models/updatesalesinvoiceresponsebody.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.UpdateSalesInvoiceSalesInvoicesResponseBody         | 404                                                        | application/hal+json                                       |
| models.UpdateSalesInvoiceSalesInvoicesResponseResponseBody | 422                                                        | application/hal+json                                       |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## delete

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Sales invoices which are in status `draft` can be deleted. For all other statuses, please use the [Update sales invoice](update-sales-invoice) endpoint instead.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **sales-invoices.write**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-sales-invoice" method="delete" path="/sales-invoices/{id}" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.sales_invoices.delete(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                    | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DeleteSalesInvoiceResponseBody              | 404                                                | application/hal+json                               |
| models.DeleteSalesInvoiceSalesInvoicesResponseBody | 422                                                | application/hal+json                               |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |