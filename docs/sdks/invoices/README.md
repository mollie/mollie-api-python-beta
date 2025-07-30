# Invoices
(*invoices*)

## Overview

### Available Operations

* [list](#list) - List invoices
* [get](#get) - Get invoice

## list

Retrieve a list of all your invoices, optionally filtered by year or by invoice reference.

The results are paginated.

> 🔑 Access with
>
> [Access token with **invoices.read**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="list-invoices" method="get" path="/invoices" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.invoices.list(reference="2024.10000", year="2024", month="01", from_="inv_xBEbP9rvAq", limit=50, sort="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                               | Type                                                                                                                                                                                    | Required                                                                                                                                                                                | Description                                                                                                                                                                             | Example                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `reference`                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | Filter for an invoice with a specific invoice reference, for example `2024.10000`.                                                                                                      | 2024.10000                                                                                                                                                                              |
| `year`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | Filter for invoices of a specific year, for example `2024`.                                                                                                                             | 2024                                                                                                                                                                                    |
| `month`                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | Filter for invoices of a specific month, for example `01`.                                                                                                                              | 01                                                                                                                                                                                      |
| `from_`                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set.                                                          | inv_xBEbP9rvAq                                                                                                                                                                          |
| `limit`                                                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | The maximum number of items to return. Defaults to 50 items.                                                                                                                            | 50                                                                                                                                                                                      |
| `sort`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                      | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from newest to oldest.<br/><br/>Possible values: `asc` `desc` (default: `desc`) | desc                                                                                                                                                                                    |
| `retries`                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                     |                                                                                                                                                                                         |

### Response

**[models.ListInvoicesResponseBody](../../models/listinvoicesresponsebody.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.ListInvoicesInvoicesResponseBody         | 400                                             | application/hal+json                            |
| models.ListInvoicesInvoicesResponseResponseBody | 404                                             | application/hal+json                            |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## get

Retrieve a single invoice by its ID.

If you want to retrieve the details of an invoice by its invoice number, call the [List invoices](list-invoices) endpoint with the `reference` parameter.

> 🔑 Access with
>
> [Access token with **invoices.read**](/reference/authentication)

### Example Usage

<!-- UsageSnippet language="python" operationID="get-invoice" method="get" path="/invoices/{id}" -->
```python
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.invoices.get(id="inv_FrvewDA3Pr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the item you want to perform this operation on.   | inv_FrvewDA3Pr                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetInvoiceResponseBody](../../models/getinvoiceresponsebody.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| models.GetInvoiceInvoicesResponseBody | 404                                   | application/hal+json                  |
| models.APIError                       | 4XX, 5XX                              | \*/\*                                 |