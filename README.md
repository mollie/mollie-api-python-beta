# mollie-api-python-beta

Developer-friendly & type-safe Python SDK specifically catered to leverage *mollie-api-python-beta* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=mollie-api-python-beta&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

## Migration
This documentation is for the new Mollie's SDK. You can find more details on how to migrate from the old version to the new one [here](/MIGRATION.md).

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [mollie-api-python-beta](#mollie-api-python-beta)
  * [Migration](#migration)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [Idempotency Key](#idempotency-key)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add mollie
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install mollie
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add mollie
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from mollie python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "mollie",
# ]
# ///

from mollie import ClientSDK

sdk = ClientSDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from datetime import date
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payments.create(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
        "locale": mollie.CreatePaymentLocaleRequest.EN_US,
        "method": mollie.CreatePaymentMethodRequest.IDEAL,
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
        "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
        "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
        "company": {
            "registration_number": "12345678",
            "vat_number": "NL123456789B01",
        },
        "card_token": "tkn_12345",
        "voucher_number": "1234567890",
        "voucher_pin": "1234",
        "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
        "digital_goods": True,
        "customer_reference": "1234567890",
        "terminal_id": "term_1234567890",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from datetime import date
import mollie
from mollie import ClientSDK
import os

async def main():

    async with ClientSDK(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client_sdk:

        res = await client_sdk.payments.create_async(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                    "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                        mollie.CreatePaymentCategoryRequest.MEAL,
                        mollie.CreatePaymentCategoryRequest.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
                {
                    "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                        mollie.CreatePaymentCategoryRequest.MEAL,
                        mollie.CreatePaymentCategoryRequest.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
                {
                    "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                        mollie.CreatePaymentCategoryRequest.MEAL,
                        mollie.CreatePaymentCategoryRequest.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
            "locale": mollie.CreatePaymentLocaleRequest.EN_US,
            "method": mollie.CreatePaymentMethodRequest.IDEAL,
            "issuer": "ideal_INGBNL2A",
            "restrict_payment_methods_to_country": "NL",
            "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                        "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                        "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
            "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
            "mandate_id": "mdt_5B8cwPMGnU",
            "customer_id": "cst_5B8cwPMGnU",
            "profile_id": "pfl_5B8cwPMGnU",
            "due_date": "2025-01-01",
            "testmode": False,
            "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
            "company": {
                "registration_number": "12345678",
                "vat_number": "NL123456789B01",
            },
            "card_token": "tkn_12345",
            "voucher_number": "1234567890",
            "voucher_pin": "1234",
            "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
            "digital_goods": True,
            "customer_reference": "1234567890",
            "terminal_id": "term_1234567890",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name      | Type   | Scheme       | Environment Variable |
| --------- | ------ | ------------ | -------------------- |
| `api_key` | http   | HTTP Bearer  | `CLIENT_API_KEY`     |
| `o_auth`  | oauth2 | OAuth2 token | `CLIENT_O_AUTH`      |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from datetime import date
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payments.create(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
        "locale": mollie.CreatePaymentLocaleRequest.EN_US,
        "method": mollie.CreatePaymentMethodRequest.IDEAL,
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
        "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
        "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
        "company": {
            "registration_number": "12345678",
            "vat_number": "NL123456789B01",
        },
        "card_token": "tkn_12345",
        "voucher_number": "1234567890",
        "voucher_pin": "1234",
        "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
        "digital_goods": True,
        "customer_reference": "1234567890",
        "terminal_id": "term_1234567890",
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [balances](docs/sdks/balances/README.md)

* [list](docs/sdks/balances/README.md#list) - List balances
* [get](docs/sdks/balances/README.md#get) - Get balance
* [get_primary](docs/sdks/balances/README.md#get_primary) - Get primary balance
* [get_report](docs/sdks/balances/README.md#get_report) - Get balance report
* [list_transactions](docs/sdks/balances/README.md#list_transactions) - List balance transactions

### [capabilities](docs/sdks/capabilitiessdk/README.md)

* [list](docs/sdks/capabilitiessdk/README.md#list) - List capabilities

### [captures](docs/sdks/capturessdk/README.md)

* [create](docs/sdks/capturessdk/README.md#create) - Create capture
* [list](docs/sdks/capturessdk/README.md#list) - List captures
* [get](docs/sdks/capturessdk/README.md#get) - Get capture

### [chargebacks](docs/sdks/chargebackssdk/README.md)

* [list](docs/sdks/chargebackssdk/README.md#list) - List payment chargebacks
* [get](docs/sdks/chargebackssdk/README.md#get) - Get payment chargeback
* [all](docs/sdks/chargebackssdk/README.md#all) - List all chargebacks

### [client_links](docs/sdks/clientlinkssdk/README.md)

* [create](docs/sdks/clientlinkssdk/README.md#create) - Create client link

### [clients](docs/sdks/clients/README.md)

* [list](docs/sdks/clients/README.md#list) - List clients
* [get](docs/sdks/clients/README.md#get) - Get client


### [customers](docs/sdks/customers/README.md)

* [create](docs/sdks/customers/README.md#create) - Create customer
* [list](docs/sdks/customers/README.md#list) - List customers
* [get](docs/sdks/customers/README.md#get) - Get customer
* [update](docs/sdks/customers/README.md#update) - Update customer
* [delete](docs/sdks/customers/README.md#delete) - Delete customer
* [create_payment](docs/sdks/customers/README.md#create_payment) - Create customer payment
* [list_payments](docs/sdks/customers/README.md#list_payments) - List customer payments

### [delayed_routing](docs/sdks/delayedrouting/README.md)

* [create](docs/sdks/delayedrouting/README.md#create) - Create a delayed route
* [list](docs/sdks/delayedrouting/README.md#list) - List payment routes

### [invoices](docs/sdks/invoices/README.md)

* [list](docs/sdks/invoices/README.md#list) - List invoices
* [get](docs/sdks/invoices/README.md#get) - Get invoice

### [mandates](docs/sdks/mandatessdk/README.md)

* [create](docs/sdks/mandatessdk/README.md#create) - Create mandate
* [list](docs/sdks/mandatessdk/README.md#list) - List mandates
* [get](docs/sdks/mandatessdk/README.md#get) - Get mandate
* [revoke](docs/sdks/mandatessdk/README.md#revoke) - Revoke mandate

### [methods](docs/sdks/methodssdk/README.md)

* [list](docs/sdks/methodssdk/README.md#list) - List payment methods
* [all](docs/sdks/methodssdk/README.md#all) - List all payment methods
* [get](docs/sdks/methodssdk/README.md#get) - Get payment method

### [onboarding](docs/sdks/onboardingsdk/README.md)

* [get](docs/sdks/onboardingsdk/README.md#get) - Get onboarding status
* [submit](docs/sdks/onboardingsdk/README.md#submit) - Submit onboarding data

### [organizations](docs/sdks/organizations/README.md)

* [get](docs/sdks/organizations/README.md#get) - Get organization
* [get_current](docs/sdks/organizations/README.md#get_current) - Get current organization
* [get_partner](docs/sdks/organizations/README.md#get_partner) - Get partner status

### [payment_links](docs/sdks/paymentlinks/README.md)

* [create](docs/sdks/paymentlinks/README.md#create) - Create payment link
* [list](docs/sdks/paymentlinks/README.md#list) - List payment links
* [get](docs/sdks/paymentlinks/README.md#get) - Get payment link
* [update](docs/sdks/paymentlinks/README.md#update) - Update payment link
* [delete](docs/sdks/paymentlinks/README.md#delete) - Delete payment link
* [list_payments](docs/sdks/paymentlinks/README.md#list_payments) - Get payment link payments

### [payments](docs/sdks/paymentssdk/README.md)

* [create](docs/sdks/paymentssdk/README.md#create) - Create payment
* [list](docs/sdks/paymentssdk/README.md#list) - List payments
* [get](docs/sdks/paymentssdk/README.md#get) - Get payment
* [update](docs/sdks/paymentssdk/README.md#update) - Update payment
* [cancel](docs/sdks/paymentssdk/README.md#cancel) - Cancel payment
* [release_authorization](docs/sdks/paymentssdk/README.md#release_authorization) - Release payment authorization

### [permissions](docs/sdks/permissions/README.md)

* [list](docs/sdks/permissions/README.md#list) - List permissions
* [get](docs/sdks/permissions/README.md#get) - Get permission

### [profiles](docs/sdks/profiles/README.md)

* [create](docs/sdks/profiles/README.md#create) - Create profile
* [list](docs/sdks/profiles/README.md#list) - List profiles
* [get](docs/sdks/profiles/README.md#get) - Get profile
* [update](docs/sdks/profiles/README.md#update) - Update profile
* [delete](docs/sdks/profiles/README.md#delete) - Delete profile
* [get_current](docs/sdks/profiles/README.md#get_current) - Get current profile

### [refunds](docs/sdks/refundssdk/README.md)

* [create](docs/sdks/refundssdk/README.md#create) - Create payment refund
* [list](docs/sdks/refundssdk/README.md#list) - List payment refunds
* [get](docs/sdks/refundssdk/README.md#get) - Get payment refund
* [cancel](docs/sdks/refundssdk/README.md#cancel) - Cancel payment refund
* [all](docs/sdks/refundssdk/README.md#all) - List all refunds

### [sales_invoices](docs/sdks/salesinvoices/README.md)

* [create](docs/sdks/salesinvoices/README.md#create) - Create sales invoice
* [list](docs/sdks/salesinvoices/README.md#list) - List sales invoices
* [get](docs/sdks/salesinvoices/README.md#get) - Get sales invoice
* [update](docs/sdks/salesinvoices/README.md#update) - Update sales invoice
* [delete](docs/sdks/salesinvoices/README.md#delete) - Delete sales invoice

### [settlements](docs/sdks/settlements/README.md)

* [list](docs/sdks/settlements/README.md#list) - List settlements
* [get](docs/sdks/settlements/README.md#get) - Get settlement
* [get_open](docs/sdks/settlements/README.md#get_open) - Get open settlement
* [get_next](docs/sdks/settlements/README.md#get_next) - Get next settlement
* [list_payments](docs/sdks/settlements/README.md#list_payments) - List settlement payments
* [list_captures](docs/sdks/settlements/README.md#list_captures) - List settlement captures
* [list_refunds](docs/sdks/settlements/README.md#list_refunds) - List settlement refunds
* [list_chargebacks](docs/sdks/settlements/README.md#list_chargebacks) - List settlement chargebacks

### [subscriptions](docs/sdks/subscriptionssdk/README.md)

* [create](docs/sdks/subscriptionssdk/README.md#create) - Create subscription
* [list](docs/sdks/subscriptionssdk/README.md#list) - List customer subscriptions
* [get](docs/sdks/subscriptionssdk/README.md#get) - Get subscription
* [update](docs/sdks/subscriptionssdk/README.md#update) - Update subscription
* [cancel](docs/sdks/subscriptionssdk/README.md#cancel) - Cancel subscription
* [all](docs/sdks/subscriptionssdk/README.md#all) - List all subscriptions
* [list_payments](docs/sdks/subscriptionssdk/README.md#list_payments) - List subscription payments

### [terminals](docs/sdks/terminals/README.md)

* [list](docs/sdks/terminals/README.md#list) - List terminals
* [get](docs/sdks/terminals/README.md#get) - Get terminal

### [wallets](docs/sdks/wallets/README.md)

* [request_apple_pay_session](docs/sdks/wallets/README.md#request_apple_pay_session) - Request Apple Pay payment session

### [webhook_events](docs/sdks/webhookevents/README.md)

* [get](docs/sdks/webhookevents/README.md#get) - Get a Webhook Event

### [webhooks](docs/sdks/webhooks/README.md)

* [create](docs/sdks/webhooks/README.md#create) - Create a webhook
* [list](docs/sdks/webhooks/README.md#list) - List all webhooks
* [update](docs/sdks/webhooks/README.md#update) - Update a webhook
* [get](docs/sdks/webhooks/README.md#get) - Get a webhook
* [delete](docs/sdks/webhooks/README.md#delete) - Delete a webhook
* [test](docs/sdks/webhooks/README.md#test) - Test a webhook

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from datetime import date
import mollie
from mollie import ClientSDK
from mollie.utils import BackoffStrategy, RetryConfig
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payments.create(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
        "locale": mollie.CreatePaymentLocaleRequest.EN_US,
        "method": mollie.CreatePaymentMethodRequest.IDEAL,
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
        "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
        "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
        "company": {
            "registration_number": "12345678",
            "vat_number": "NL123456789B01",
        },
        "card_token": "tkn_12345",
        "voucher_number": "1234567890",
        "voucher_pin": "1234",
        "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
        "digital_goods": True,
        "customer_reference": "1234567890",
        "terminal_id": "term_1234567890",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from datetime import date
import mollie
from mollie import ClientSDK
from mollie.utils import BackoffStrategy, RetryConfig
import os


with ClientSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payments.create(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
        "locale": mollie.CreatePaymentLocaleRequest.EN_US,
        "method": mollie.CreatePaymentMethodRequest.IDEAL,
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
        "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
        "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
        "company": {
            "registration_number": "12345678",
            "vat_number": "NL123456789B01",
        },
        "card_token": "tkn_12345",
        "voucher_number": "1234567890",
        "voucher_pin": "1234",
        "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
        "digital_goods": True,
        "customer_reference": "1234567890",
        "terminal_id": "term_1234567890",
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ClientError`](./src/mollie/models/clienterror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from datetime import date
import mollie
from mollie import ClientSDK, models
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:
    res = None
    try:

        res = client_sdk.payments.create(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                    "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                        mollie.CreatePaymentCategoryRequest.MEAL,
                        mollie.CreatePaymentCategoryRequest.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
                {
                    "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                        mollie.CreatePaymentCategoryRequest.MEAL,
                        mollie.CreatePaymentCategoryRequest.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
                {
                    "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                        mollie.CreatePaymentCategoryRequest.MEAL,
                        mollie.CreatePaymentCategoryRequest.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
            "locale": mollie.CreatePaymentLocaleRequest.EN_US,
            "method": mollie.CreatePaymentMethodRequest.IDEAL,
            "issuer": "ideal_INGBNL2A",
            "restrict_payment_methods_to_country": "NL",
            "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                        "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                        "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
            "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
            "mandate_id": "mdt_5B8cwPMGnU",
            "customer_id": "cst_5B8cwPMGnU",
            "profile_id": "pfl_5B8cwPMGnU",
            "due_date": "2025-01-01",
            "testmode": False,
            "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
            "company": {
                "registration_number": "12345678",
                "vat_number": "NL123456789B01",
            },
            "card_token": "tkn_12345",
            "voucher_number": "1234567890",
            "voucher_pin": "1234",
            "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
            "digital_goods": True,
            "customer_reference": "1234567890",
            "terminal_id": "term_1234567890",
        })

        # Handle response
        print(res)


    except models.ClientError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.CreatePaymentUnprocessableEntityHalJSONError):
            print(e.data.status)  # int
            print(e.data.title)  # str
            print(e.data.detail)  # str
            print(e.data.field)  # Optional[str]
            print(e.data.links)  # mollie.CreatePaymentUnprocessableEntityLinks
```

### Error Classes
**Primary error:**
* [`ClientError`](./src/mollie/models/clienterror.py): The base class for HTTP error responses.

<details><summary>Less common errors (131)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ClientError`](./src/mollie/models/clienterror.py)**:
* [`ListPaymentsHalJSONError`](./src/mollie/models/listpaymentshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListMethodsHalJSONError`](./src/mollie/models/listmethodshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListAllMethodsHalJSONError`](./src/mollie/models/listallmethodshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`GetMethodBadRequestHalJSONError`](./src/mollie/models/getmethodbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListRefundsBadRequestHalJSONError`](./src/mollie/models/listrefundsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListAllRefundsHalJSONError`](./src/mollie/models/listallrefundshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListChargebacksBadRequestHalJSONError`](./src/mollie/models/listchargebacksbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListAllChargebacksBadRequestHalJSONError`](./src/mollie/models/listallchargebacksbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListCapturesBadRequestHalJSONError`](./src/mollie/models/listcapturesbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListPaymentLinksHalJSONError`](./src/mollie/models/listpaymentlinkshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`GetPaymentLinkPaymentsHalJSONError`](./src/mollie/models/getpaymentlinkpaymentshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListTerminalsHalJSONError`](./src/mollie/models/listterminalshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListCustomersBadRequestHalJSONError`](./src/mollie/models/listcustomersbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListCustomerPaymentsHalJSONError`](./src/mollie/models/listcustomerpaymentshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListMandatesBadRequestHalJSONError`](./src/mollie/models/listmandatesbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSubscriptionsBadRequestHalJSONError`](./src/mollie/models/listsubscriptionsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListAllSubscriptionsBadRequestHalJSONError`](./src/mollie/models/listallsubscriptionsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSubscriptionPaymentsHalJSONError`](./src/mollie/models/listsubscriptionpaymentshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListPermissionsHalJSONError`](./src/mollie/models/listpermissionshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListProfilesHalJSONError`](./src/mollie/models/listprofileshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListClientsBadRequestHalJSONError`](./src/mollie/models/listclientsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListWebhooksHalJSONError`](./src/mollie/models/listwebhookshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListBalancesBadRequestHalJSONError`](./src/mollie/models/listbalancesbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListBalanceTransactionsBadRequestHalJSONError`](./src/mollie/models/listbalancetransactionsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSettlementsBadRequestHalJSONError`](./src/mollie/models/listsettlementsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSettlementPaymentsHalJSONError`](./src/mollie/models/listsettlementpaymentshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSettlementCapturesBadRequestHalJSONError`](./src/mollie/models/listsettlementcapturesbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSettlementRefundsBadRequestHalJSONError`](./src/mollie/models/listsettlementrefundsbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSettlementChargebacksBadRequestHalJSONError`](./src/mollie/models/listsettlementchargebacksbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListInvoicesBadRequestHalJSONError`](./src/mollie/models/listinvoicesbadrequesthaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`ListSalesInvoicesHalJSONError`](./src/mollie/models/listsalesinvoiceshaljsonerror.py): An error response object. Status code `400`. Applicable to 1 of 93 methods.*
* [`GetPaymentHalJSONError`](./src/mollie/models/getpaymenthaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdatePaymentNotFoundHalJSONError`](./src/mollie/models/updatepaymentnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CancelPaymentNotFoundHalJSONError`](./src/mollie/models/cancelpaymentnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ReleaseAuthorizationNotFoundHalJSONError`](./src/mollie/models/releaseauthorizationnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetMethodNotFoundHalJSONError`](./src/mollie/models/getmethodnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateRefundNotFoundHalJSONError`](./src/mollie/models/createrefundnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListRefundsNotFoundHalJSONError`](./src/mollie/models/listrefundsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetRefundHalJSONError`](./src/mollie/models/getrefundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CancelRefundHalJSONError`](./src/mollie/models/cancelrefundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListChargebacksNotFoundHalJSONError`](./src/mollie/models/listchargebacksnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetChargebackHalJSONError`](./src/mollie/models/getchargebackhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListAllChargebacksNotFoundHalJSONError`](./src/mollie/models/listallchargebacksnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateCaptureNotFoundHalJSONError`](./src/mollie/models/createcapturenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListCapturesNotFoundHalJSONError`](./src/mollie/models/listcapturesnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetCaptureHalJSONError`](./src/mollie/models/getcapturehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreatePaymentLinkNotFoundHalJSONError`](./src/mollie/models/createpaymentlinknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetPaymentLinkHalJSONError`](./src/mollie/models/getpaymentlinkhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdatePaymentLinkNotFoundHalJSONError`](./src/mollie/models/updatepaymentlinknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`DeletePaymentLinkNotFoundHalJSONError`](./src/mollie/models/deletepaymentlinknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetTerminalHalJSONError`](./src/mollie/models/getterminalhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`PaymentCreateRouteHalJSONError`](./src/mollie/models/paymentcreateroutehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`PaymentListRoutesHalJSONError`](./src/mollie/models/paymentlistrouteshaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateCustomerHalJSONError`](./src/mollie/models/createcustomerhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListCustomersNotFoundHalJSONError`](./src/mollie/models/listcustomersnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetCustomerHalJSONError`](./src/mollie/models/getcustomerhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdateCustomerHalJSONError`](./src/mollie/models/updatecustomerhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`DeleteCustomerHalJSONError`](./src/mollie/models/deletecustomerhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateMandateHalJSONError`](./src/mollie/models/createmandatehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListMandatesNotFoundHalJSONError`](./src/mollie/models/listmandatesnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetMandateHalJSONError`](./src/mollie/models/getmandatehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`RevokeMandateHalJSONError`](./src/mollie/models/revokemandatehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateSubscriptionHalJSONError`](./src/mollie/models/createsubscriptionhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListSubscriptionsNotFoundHalJSONError`](./src/mollie/models/listsubscriptionsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetSubscriptionHalJSONError`](./src/mollie/models/getsubscriptionhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdateSubscriptionHalJSONError`](./src/mollie/models/updatesubscriptionhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CancelSubscriptionHalJSONError`](./src/mollie/models/cancelsubscriptionhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListAllSubscriptionsNotFoundHalJSONError`](./src/mollie/models/listallsubscriptionsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetPermissionHalJSONError`](./src/mollie/models/getpermissionhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetOrganizationHalJSONError`](./src/mollie/models/getorganizationhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetProfileNotFoundHalJSONError`](./src/mollie/models/getprofilenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdateProfileNotFoundHalJSONError`](./src/mollie/models/updateprofilenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`DeleteProfileNotFoundHalJSONError`](./src/mollie/models/deleteprofilenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListClientsNotFoundHalJSONError`](./src/mollie/models/listclientsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetClientHalJSONError`](./src/mollie/models/getclienthaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateClientLinkNotFoundHalJSONError`](./src/mollie/models/createclientlinknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdateWebhookNotFoundHalJSONError`](./src/mollie/models/updatewebhooknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetWebhookNotFoundHalJSONError`](./src/mollie/models/getwebhooknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`DeleteWebhookNotFoundHalJSONError`](./src/mollie/models/deletewebhooknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`TestWebhookNotFoundHalJSONError`](./src/mollie/models/testwebhooknotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetWebhookEventHalJSONError`](./src/mollie/models/getwebhookeventhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListBalancesNotFoundHalJSONError`](./src/mollie/models/listbalancesnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetBalanceHalJSONError`](./src/mollie/models/getbalancehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetBalanceReportNotFoundHalJSONError`](./src/mollie/models/getbalancereportnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListBalanceTransactionsNotFoundHalJSONError`](./src/mollie/models/listbalancetransactionsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListSettlementsNotFoundHalJSONError`](./src/mollie/models/listsettlementsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetSettlementHalJSONError`](./src/mollie/models/getsettlementhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListSettlementCapturesNotFoundHalJSONError`](./src/mollie/models/listsettlementcapturesnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListSettlementRefundsNotFoundHalJSONError`](./src/mollie/models/listsettlementrefundsnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListSettlementChargebacksNotFoundHalJSONError`](./src/mollie/models/listsettlementchargebacksnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ListInvoicesNotFoundHalJSONError`](./src/mollie/models/listinvoicesnotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetInvoiceHalJSONError`](./src/mollie/models/getinvoicehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`CreateSalesInvoiceNotFoundHalJSONError`](./src/mollie/models/createsalesinvoicenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`GetSalesInvoiceHalJSONError`](./src/mollie/models/getsalesinvoicehaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`UpdateSalesInvoiceNotFoundHalJSONError`](./src/mollie/models/updatesalesinvoicenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`DeleteSalesInvoiceNotFoundHalJSONError`](./src/mollie/models/deletesalesinvoicenotfoundhaljsonerror.py): An error response object. Status code `404`. Applicable to 1 of 93 methods.*
* [`ConflictHalJSONError`](./src/mollie/models/conflicthaljsonerror.py): An error response object. Status code `409`. Applicable to 1 of 93 methods.*
* [`GetProfileGoneHalJSONError`](./src/mollie/models/getprofilegonehaljsonerror.py): An error response object. Status code `410`. Applicable to 1 of 93 methods.*
* [`UpdateProfileGoneHalJSONError`](./src/mollie/models/updateprofilegonehaljsonerror.py): An error response object. Status code `410`. Applicable to 1 of 93 methods.*
* [`DeleteProfileGoneHalJSONError`](./src/mollie/models/deleteprofilegonehaljsonerror.py): An error response object. Status code `410`. Applicable to 1 of 93 methods.*
* [`CreatePaymentUnprocessableEntityHalJSONError`](./src/mollie/models/createpaymentunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`UpdatePaymentUnprocessableEntityHalJSONError`](./src/mollie/models/updatepaymentunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CancelPaymentUnprocessableEntityHalJSONError`](./src/mollie/models/cancelpaymentunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`ReleaseAuthorizationUnprocessableEntityHalJSONError`](./src/mollie/models/releaseauthorizationunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateRefundUnprocessableEntityHalJSONError`](./src/mollie/models/createrefundunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateCaptureUnprocessableEntityHalJSONError`](./src/mollie/models/createcaptureunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`RequestApplePayPaymentSessionHalJSONError`](./src/mollie/models/requestapplepaypaymentsessionhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreatePaymentLinkUnprocessableEntityHalJSONError`](./src/mollie/models/createpaymentlinkunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`UpdatePaymentLinkUnprocessableEntityHalJSONError`](./src/mollie/models/updatepaymentlinkunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`DeletePaymentLinkUnprocessableEntityHalJSONError`](./src/mollie/models/deletepaymentlinkunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateCustomerPaymentUnprocessableEntityHalJSONError`](./src/mollie/models/createcustomerpaymentunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateProfileHalJSONError`](./src/mollie/models/createprofilehaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`UpdateProfileUnprocessableEntityHalJSONError`](./src/mollie/models/updateprofileunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateClientLinkUnprocessableEntityHalJSONError`](./src/mollie/models/createclientlinkunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateWebhookHalJSONError`](./src/mollie/models/createwebhookhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`UpdateWebhookUnprocessableEntityHalJSONError`](./src/mollie/models/updatewebhookunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`GetWebhookUnprocessableEntityHalJSONError`](./src/mollie/models/getwebhookunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`DeleteWebhookUnprocessableEntityHalJSONError`](./src/mollie/models/deletewebhookunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`TestWebhookUnprocessableEntityHalJSONError`](./src/mollie/models/testwebhookunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`GetBalanceReportUnprocessableEntityHalJSONError`](./src/mollie/models/getbalancereportunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`CreateSalesInvoiceUnprocessableEntityHalJSONError`](./src/mollie/models/createsalesinvoiceunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`UpdateSalesInvoiceUnprocessableEntityHalJSONError`](./src/mollie/models/updatesalesinvoiceunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`DeleteSalesInvoiceUnprocessableEntityHalJSONError`](./src/mollie/models/deletesalesinvoiceunprocessableentityhaljsonerror.py): An error response object. Status code `422`. Applicable to 1 of 93 methods.*
* [`TooManyRequestsHalJSONError`](./src/mollie/models/toomanyrequestshaljsonerror.py): An error response object. Status code `429`. Applicable to 1 of 93 methods.*
* [`CreatePaymentServiceUnavailableHalJSONError`](./src/mollie/models/createpaymentserviceunavailablehaljsonerror.py): An error response object. Status code `503`. Applicable to 1 of 93 methods.*
* [`CreateCustomerPaymentServiceUnavailableHalJSONError`](./src/mollie/models/createcustomerpaymentserviceunavailablehaljsonerror.py): An error response object. Status code `503`. Applicable to 1 of 93 methods.*
* [`ResponseValidationError`](./src/mollie/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from datetime import date
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    server_url="https://api.mollie.com/v2",
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payments.create(include=mollie.CreatePaymentInclude.DETAILS_QR_CODE, request_body={
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
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_WEEKS,
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
            {
                "type": mollie.CreatePaymentLineTypeRequest.PHYSICAL,
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
                    mollie.CreatePaymentCategoryRequest.MEAL,
                    mollie.CreatePaymentCategoryRequest.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": mollie.CreatePaymentIntervalRequest.DOT_DOT_DOT_DAYS,
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
        "locale": mollie.CreatePaymentLocaleRequest.EN_US,
        "method": mollie.CreatePaymentMethodRequest.IDEAL,
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": mollie.CreatePaymentCaptureModeRequest.MANUAL,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
                    "type": mollie.CreatePaymentRoutingTypeRequest.ORGANIZATION,
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
        "sequence_type": mollie.CreatePaymentSequenceTypeRequest.ONEOFF,
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
        "apple_pay_payment_token": "{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
        "company": {
            "registration_number": "12345678",
            "vat_number": "NL123456789B01",
        },
        "card_token": "tkn_12345",
        "voucher_number": "1234567890",
        "voucher_pin": "1234",
        "consumer_date_of_birth": date.fromisoformat("2000-01-01"),
        "digital_goods": True,
        "customer_reference": "1234567890",
        "terminal_id": "term_1234567890",
    })

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from mollie import ClientSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = ClientSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from mollie import ClientSDK
from mollie.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = ClientSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `ClientSDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import mollie
from mollie import ClientSDK
import os
def main():

    with ClientSDK(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client_sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with ClientSDK(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client_sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from mollie import ClientSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = ClientSDK(debug_logger=logging.getLogger("mollie"))
```

You can also enable a default debug logger by setting an environment variable `CLIENT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

## Idempotency Key

You can setup an Idempotency Key.

```
import os
from mollie import ClientSDK, Security

client = ClientSDK(
    security = Security(
        api_key = os.getenv("MOLLIE_API_KEY", "test_..."),
    )
)

payload = {
    "description": "Some Description",
    "amount": {
        "currency": "EUR",
        "value": "0.01",
    },
    "redirect_url": "https://example.org/redirect",
}

idempotency_key = "unique-idempotency-key-12345"
payment1 = client.payments.create(
    request_body=payload,
    http_headers={
        "Idempotency-Key": idempotency_key
    }
)

payment2 = client.payments.create(
    request_body=payload,
    http_headers={
        "Idempotency-Key": idempotency_key
    }
)
print(f"Payment created with ID: {payment1.id}")
print(f"Payment created with ID: {payment2.id}")
print("Payments are the same" if payment1.id == payment2.id else "Payments are different")
```

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=mollie-api-python-beta&utm_campaign=python)
