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

    res = client_sdk.sales_invoices.create(request=mollie.EntitySalesInvoice(
        id="invoice_4Y0eZitmBnQ6IDoMqZQKh",
        testmode=False,
        profile_id="pfl_QkEhN94Ba",
        status=mollie.SalesInvoiceStatus.DRAFT,
        vat_scheme=mollie.SalesInvoiceVatScheme.STANDARD,
        vat_mode=mollie.SalesInvoiceVatMode.EXCLUSIVE,
        memo="This is a memo!",
        payment_term=mollie.SalesInvoicePaymentTerm.THIRTYDAYS,
        payment_details=mollie.SalesInvoicePaymentDetails(
            source=mollie.SalesInvoicePaymentDetailsSource.PAYMENT_LINK,
            source_reference="pl_d9fQur83kFdhH8hIhaZfq",
        ),
        email_details=mollie.SalesInvoiceEmailDetails(
            subject="Your invoice is available",
            body="Please find your invoice enclosed.",
        ),
        customer_id="cst_8wmqcHMN4U",
        mandate_id="mdt_pWUnw6pkBN",
        recipient_identifier="customer-xyz-0123",
        recipient=mollie.SalesInvoiceRecipient(
            type=mollie.SalesInvoiceRecipientType.CONSUMER,
            title="Mrs.",
            given_name="Jane",
            family_name="Doe",
            organization_name="Organization Corp.",
            organization_number="12345678",
            vat_number="NL123456789B01",
            email="example@email.com",
            phone="+0123456789",
            street_and_number="Keizersgracht 126",
            street_additional="4th floor",
            postal_code="5678AB",
            city="Amsterdam",
            region="Noord-Holland",
            country="NL",
            locale=mollie.SalesInvoiceRecipientLocale.NL_NL,
        ),
        lines=[],
        discount=mollie.SalesInvoiceDiscount(
            type=mollie.SalesInvoiceDiscountType.AMOUNT,
            value="10.00",
        ),
        amount_due=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        subtotal_amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        total_amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        total_vat_amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        discounted_subtotal_amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.EntitySalesInvoice](../../models/entitysalesinvoice.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EntitySalesInvoiceResponse](../../models/entitysalesinvoiceresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

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
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                        |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListSalesInvoicesResponse](../../models/listsalesinvoicesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

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
| `id`                                                                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the item you want to perform this operation on.                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | false                                                                                                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.EntitySalesInvoiceResponse](../../models/entitysalesinvoiceresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

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

    res = client_sdk.sales_invoices.update(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", update_values_sales_invoice={
        "testmode": False,
        "status": mollie.SalesInvoiceStatus.DRAFT,
        "memo": "An updated memo!",
        "payment_term": mollie.SalesInvoicePaymentTerm.THIRTYDAYS,
        "payment_details": {
            "source": mollie.SalesInvoicePaymentDetailsSource.PAYMENT_LINK,
            "source_reference": "pl_d9fQur83kFdhH8hIhaZfq",
        },
        "email_details": {
            "subject": "Your invoice is available",
            "body": "Please find your invoice enclosed.",
        },
        "recipient_identifier": "customer-xyz-0123",
        "recipient": {
            "type": mollie.SalesInvoiceRecipientType.CONSUMER,
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
            "locale": mollie.SalesInvoiceRecipientLocale.NL_NL,
        },
        "lines": [
            {
                "description": "LEGO 4440 Forest Police Station",
                "quantity": 1,
                "vat_rate": "21.00",
                "unit_price": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "discount": {
                    "type": mollie.SalesInvoiceDiscountType.AMOUNT,
                    "value": "10.00",
                },
            },
        ],
        "discount": {
            "type": mollie.SalesInvoiceDiscountType.AMOUNT,
            "value": "10.00",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | Provide the ID of the item you want to perform this operation on.                     |
| `update_values_sales_invoice`                                                         | [Optional[models.UpdateValuesSalesInvoice]](../../models/updatevaluessalesinvoice.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EntitySalesInvoiceResponse](../../models/entitysalesinvoiceresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

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

    res = client_sdk.sales_invoices.delete(id="invoice_4Y0eZitmBnQ6IDoMqZQKh", delete_values_sales_invoice={
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | Provide the ID of the item you want to perform this operation on.                     |
| `delete_values_sales_invoice`                                                         | [Optional[models.DeleteValuesSalesInvoice]](../../models/deletevaluessalesinvoice.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |