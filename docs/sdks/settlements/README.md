# Settlements
(*settlements*)

## Overview

### Available Operations

* [list](#list) - List settlements
* [get](#get) - Get settlement
* [get_open](#get_open) - Get open settlement
* [get_next](#get_next) - Get next settlement
* [get_payments](#get_payments) - Get settlement payments
* [get_captures](#get_captures) - Get settlement captures
* [get_refunds](#get_refunds) - Get settlement refunds
* [get_chargebacks](#get_chargebacks) - Get settlement chargebacks

## list

Retrieve a list of all your settlements.

The results are paginated.

> 🔑 Access with
>
> [Access token with **settlements.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.list(from_="stl_jDk30akdN", balance_id="bal_3kUf4yU2nT")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `from_`                                                                                                                        | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set. | stl_jDk30akdN                                                                                                                  |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `balance_id`                                                                                                                   | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | Provide the token of the balance to filter the settlements by. This is the balance token that the settlement was settled to.   | bal_3kUf4yU2nT                                                                                                                 |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListSettlementsResponseBody](../../models/listsettlementsresponsebody.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| models.ListSettlementsSettlementsResponseBody         | 400                                                   | application/hal+json                                  |
| models.ListSettlementsSettlementsResponseResponseBody | 404                                                   | application/hal+json                                  |
| models.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## get

Retrieve a single settlement by its ID.

To lookup settlements by their bank reference, replace the ID in the URL by a reference. For example: `1234567.2404.03`.

A settlement represents a transfer of your balance funds to your external bank account.

Settlements will typically include a report that details what balance transactions have taken place between this settlement and the previous one.

For more accurate bookkeeping, refer to the [balance report](get-balance-report) endpoint or the [balance transactions](list-balance-transactions) endpoint.

> 🔑 Access with
>
> [Access token with **settlements.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get(id="stl_jDk30akdN")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the item you want to perform this operation on.   | stl_jDk30akdN                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetSettlementResponseBody](../../models/getsettlementresponsebody.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.GetSettlementSettlementsResponseBody | 404                                         | application/hal+json                        |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |

## get_open

Retrieve the details of the open balance of the organization. This will return a settlement object representing your organization's balance.

For a complete reference of the settlement object, refer to the [Get settlement endpoint](get-settlement) documentation.

For more accurate bookkeeping, refer to the [balance report](get-balance-report) endpoint or the [balance transactions](list-balance-transactions) endpoint.

> 🔑 Access with
>
> [Access token with **settlements.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get_open()

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

## get_next

Retrieve the details of the current settlement, that has not yet been paid out.

For a complete reference of the settlement object, refer to the [Get settlement endpoint](get-settlement) documentation.

For more accurate bookkeeping, refer to the [balance report](get-balance-report) endpoint or the [balance transactions](list-balance-transactions) endpoint.

> 🔑 Access with
>
> [Access token with **settlements.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get_next()

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

## get_payments

Retrieve all payments included in the given settlement.

The response is in the same format as the response of the [List payments endpoint](list-payments). Refer to that endpoint's documentation for more details.

For capture-based payment methods such as Klarna, the payments are not listed here. Refer to the [List captures endpoint](list-captures) endpoint instead.

> 🔑 Access with
>
> [Access token with **settlements.read** **payments.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get_payments(settlement_id="stl_jDk30akdN")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `settlement_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the related settlement.                           | stl_jDk30akdN                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.GetSettlementPaymentsResponseBody | 404                                      | application/hal+json                     |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## get_captures

Retrieve all captures included in the given settlement.

The response is in the same format as the response of the [List captures endpoint](list-captures). Refer to that endpoint's documentation for more details.

> 🔑 Access with
>
> [Access token with **settlements.read** **payments.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get_captures(settlement_id="stl_jDk30akdN")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `settlement_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the related settlement.                           | stl_jDk30akdN                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| models.GetSettlementCapturesResponseBody | 404                                      | application/hal+json                     |
| models.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## get_refunds

Retrieve all refunds 'deducted' from the given settlement.

The response is in the same format as the response of the [List refunds endpoint](list-refunds). Refer to that endpoint's documentation for more details.

> 🔑 Access with
>
> [Access token with **settlements.read** **refunds.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get_refunds(settlement_id="stl_jDk30akdN")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `settlement_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the related settlement.                           | stl_jDk30akdN                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| models.GetSettlementRefundsResponseBody | 404                                     | application/hal+json                    |
| models.APIError                         | 4XX, 5XX                                | \*/\*                                   |

## get_chargebacks

Retrieve all chargebacks 'deducted' from the given settlement.

The response is in the same format as the response of the [List chargebacks endpoint](list-chargebacks). Refer to that endpoint's documentation for more details.

> 🔑 Access with
>
> [Access token with **settlements.read** **payments.read**](/reference/authentication)

### Example Usage

```python
import mollie_api_python_beta
from mollie_api_python_beta import Mollie
import os

with Mollie(
    security=mollie_api_python_beta.Security(
        api_key=os.getenv("MOLLIE_API_KEY", ""),
    ),
) as mollie:

    res = mollie.settlements.get_chargebacks(settlement_id="stl_jDk30akdN")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `settlement_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Provide the ID of the related settlement.                           | stl_jDk30akdN                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.GetSettlementChargebacksResponseBody | 404                                         | application/hal+json                        |
| models.APIError                             | 4XX, 5XX                                    | \*/\*                                       |