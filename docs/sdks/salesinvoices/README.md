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

### Example Usage

<!-- UsageSnippet language="python" operationID="create-sales-invoice" method="post" path="/sales-invoices" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.create(request={
        "testmode": False,
        "profile_id": "pfl_QkEhN94Ba",
        "status": mollie.CreateSalesInvoiceStatusRequest.DRAFT,
        "memo": "This is a memo!",
        "payment_details": {
            "source": mollie.CreateSalesInvoiceSourceRequest.PAYMENT_LINK,
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
            "type": mollie.CreateSalesInvoiceRecipientTypeRequest.CONSUMER,
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
            "locale": mollie.CreateSalesInvoiceLocaleRequest.NL_NL,
        },
        "lines": [],
        "discount": {
            "type": mollie.CreateSalesInvoiceDiscountTypeRequest.AMOUNT,
            "value": "10.00",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.CreateSalesInvoiceRequest](../../models/createsalesinvoicerequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CreateSalesInvoiceResponse](../../models/createsalesinvoiceresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| models.CreateSalesInvoiceNotFoundHalJSONError            | 404                                                      | application/hal+json                                     |
| models.CreateSalesInvoiceUnprocessableEntityHalJSONError | 422                                                      | application/hal+json                                     |
| models.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## list

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a list of all sales invoices created through the API.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-sales-invoices" method="get" path="/sales-invoices" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.list(from_="invoice_4Y0eZitmBnQ6IDoMqZQKh", limit=50, testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListSalesInvoicesResponse](../../models/listsalesinvoicesresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| models.ListSalesInvoicesHalJSONError | 400                                  | application/hal+json                 |
| models.APIError                      | 4XX, 5XX                             | \*/\*                                |

## get

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a single sales invoice by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-sales-invoice" method="get" path="/sales-invoices/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.get(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetSalesInvoiceResponse](../../models/getsalesinvoiceresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| models.GetSalesInvoiceHalJSONError | 404                                | application/hal+json               |
| models.APIError                    | 4XX, 5XX                           | \*/\*                              |

## update

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Certain details of an existing sales invoice can be updated. For `draft` it is all values listed below, but for
statuses `paid` and `issued` there are certain additional requirements (`paymentDetails` and `emailDetails`,
respectively).

### Example Usage

<!-- UsageSnippet language="python" operationID="update-sales-invoice" method="patch" path="/sales-invoices/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.update(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", testmode=False, status=mollie.UpdateSalesInvoiceStatusRequest.PAID, memo="An updated memo!", payment_term=mollie.UpdateSalesInvoicePaymentTermRequest.THIRTYDAYS, payment_details={
        "source": mollie.UpdateSalesInvoiceSourceRequest.PAYMENT_LINK,
        "source_reference": "pl_d9fQur83kFdhH8hIhaZfq",
    }, email_details={
        "subject": "Your invoice is available",
        "body": "Please find your invoice enclosed.",
    }, recipient_identifier="customer-xyz-0123", recipient={
        "type": mollie.UpdateSalesInvoiceRecipientTypeRequest.CONSUMER,
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
        "locale": mollie.UpdateSalesInvoiceLocaleRequest.NL_NL,
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
                "type": mollie.UpdateSalesInvoiceLineTypeRequest.AMOUNT,
                "value": "10.00",
            },
        },
    ], discount={
        "type": mollie.UpdateSalesInvoiceDiscountTypeRequest.AMOUNT,
        "value": "10.00",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                    | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials<br/>such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                |
| `status`                                                                                                                                                                                                                                                                                             | [Optional[models.UpdateSalesInvoiceStatusRequest]](../../models/updatesalesinvoicestatusrequest.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The status for the invoice to end up in.<br/><br/>Dependent parameters: `paymentDetails` for `paid`, `emailDetails` for `issued` and `paid`.                                                                                                                                                         | paid                                                                                                                                                                                                                                                                                                 |
| `memo`                                                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | A free-form memo you can set on the invoice, and will be shown on the invoice PDF.                                                                                                                                                                                                                   | An updated memo!                                                                                                                                                                                                                                                                                     |
| `payment_term`                                                                                                                                                                                                                                                                                       | [OptionalNullable[models.UpdateSalesInvoicePaymentTermRequest]](../../models/updatesalesinvoicepaymenttermrequest.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The payment term to be set on the invoice.                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                      |
| `payment_details`                                                                                                                                                                                                                                                                                    | [OptionalNullable[models.UpdateSalesInvoicePaymentDetailsRequest]](../../models/updatesalesinvoicepaymentdetailsrequest.md)                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Used when setting an invoice to status of `paid`, and will store a payment that fully pays the invoice with the<br/>provided details. Required for `paid` status.                                                                                                                                    |                                                                                                                                                                                                                                                                                                      |
| `email_details`                                                                                                                                                                                                                                                                                      | [OptionalNullable[models.UpdateSalesInvoiceEmailDetailsRequest]](../../models/updatesalesinvoiceemaildetailsrequest.md)                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Used when setting an invoice to status of either `issued` or `paid`. Will be used to issue the invoice to the<br/>recipient with the provided `subject` and `body`. Required for `issued` status.                                                                                                    |                                                                                                                                                                                                                                                                                                      |
| `recipient_identifier`                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | An identifier tied to the recipient data. This should be a unique value based on data your system contains,<br/>so that both you and us know who we're referring to. It is a value you provide to us so that recipient management<br/>is not required to send a first invoice to a recipient.        | customer-xyz-0123                                                                                                                                                                                                                                                                                    |
| `recipient`                                                                                                                                                                                                                                                                                          | [OptionalNullable[models.UpdateSalesInvoiceRecipientRequest]](../../models/updatesalesinvoicerecipientrequest.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The recipient object should contain all the information relevant to create an invoice for an intended<br/>recipient. This data will be stored, updated, and re-used as appropriate, based on the `recipientIdentifier`.                                                                              |                                                                                                                                                                                                                                                                                                      |
| `lines`                                                                                                                                                                                                                                                                                              | List[[models.UpdateSalesInvoiceLineRequest](../../models/updatesalesinvoicelinerequest.md)]                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Provide the line items for the invoice. Each line contains details such as a description of the item<br/>ordered and its price.<br/><br/>All lines must have the same currency as the invoice.                                                                                                       |                                                                                                                                                                                                                                                                                                      |
| `discount`                                                                                                                                                                                                                                                                                           | [OptionalNullable[models.UpdateSalesInvoiceDiscountRequest]](../../models/updatesalesinvoicediscountrequest.md)                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | The discount to be applied to the entire invoice, possibly on top of the line item discounts.                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[models.UpdateSalesInvoiceResponse](../../models/updatesalesinvoiceresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| models.UpdateSalesInvoiceNotFoundHalJSONError            | 404                                                      | application/hal+json                                     |
| models.UpdateSalesInvoiceUnprocessableEntityHalJSONError | 422                                                      | application/hal+json                                     |
| models.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## delete

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Sales invoices which are in status `draft` can be deleted. For all other statuses, please use the
[Update sales invoice](update-sales-invoice) endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-sales-invoice" method="delete" path="/sales-invoices/{id}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.delete(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", testmode=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                   | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                    | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Most API credentials are specifically created for either live mode or test mode. For organization-level credentials<br/>such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                      |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| models.DeleteSalesInvoiceNotFoundHalJSONError            | 404                                                      | application/hal+json                                     |
| models.DeleteSalesInvoiceUnprocessableEntityHalJSONError | 422                                                      | application/hal+json                                     |
| models.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |