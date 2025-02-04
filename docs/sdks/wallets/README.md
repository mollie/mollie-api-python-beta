# Wallets
(*wallets*)

## Overview

### Available Operations

* [request_apple_pay_payment_session](#request_apple_pay_payment_session) - Request Apple Pay payment session

## request_apple_pay_payment_session

When integrating Apple Pay in your own checkout on the web, you need to [provide merchant validation](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation). This is normally done using Apple's [Requesting an Apple Pay Session](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session). The merchant validation proves to Apple that a validated merchant is calling the Apple Pay Javascript APIs.

To integrate Apple Pay via Mollie, you will have to call the Mollie API instead of Apple's API. The response of this API call can then be passed as-is to the completion method, `completeMerchantValidation`.

Before requesting an Apple Pay Payment Session, you must place the domain validation file on your server at: `https://[domain]/.well-known/apple-developer-merchantid-domain-association`. Without this file, it will not be possible to use Apple Pay on your domain.

Each new transaction requires a new payment session object. Merchant session objects are not reusable, and they expire after five minutes.

Payment sessions cannot be requested directly from the browser. The request must be sent from your server. For the full documentation, see the official [Apple Pay JS API](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api) documentation.

> 🔑 Access with
>
> [API key](/reference/authentication)
>
> [Access token with **payments.write**](/reference/authentication)

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

    res = mollie.wallets.request_apple_pay_payment_session(request={
        "validation_url": "https://dark-suv.org",
        "domain": "cheap-contractor.info",
        "profile_id": "pfl_QkEhN94Ba",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.RequestApplePayPaymentSessionRequestBody](../../models/requestapplepaypaymentsessionrequestbody.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.RequestApplePayPaymentSessionResponseBody | 422                                              | application/hal+json                             |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |