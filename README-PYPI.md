# mollie-api-python-beta

Developer-friendly & type-safe Python SDK specifically catered to leverage *mollie-api-python-beta* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=mollie-api-python-beta&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

## Migration
This documentation is for the new Mollie's SDK. You can find more details on how to migrate from the old version to the new one [here](https://github.com/mollie/mollie-api-python-beta/blob/master//MIGRATION.md).

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [mollie-api-python-beta](https://github.com/mollie/mollie-api-python-beta/blob/master/#mollie-api-python-beta)
  * [Migration](https://github.com/mollie/mollie-api-python-beta/blob/master/#migration)
  * [SDK Installation](https://github.com/mollie/mollie-api-python-beta/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/mollie/mollie-api-python-beta/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/mollie/mollie-api-python-beta/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/mollie/mollie-api-python-beta/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/mollie/mollie-api-python-beta/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/mollie/mollie-api-python-beta/blob/master/#retries)
  * [Error Handling](https://github.com/mollie/mollie-api-python-beta/blob/master/#error-handling)
  * [Server Selection](https://github.com/mollie/mollie-api-python-beta/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/mollie/mollie-api-python-beta/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/mollie/mollie-api-python-beta/blob/master/#resource-management)
  * [Debugging](https://github.com/mollie/mollie-api-python-beta/blob/master/#debugging)
* [Development](https://github.com/mollie/mollie-api-python-beta/blob/master/#development)
  * [Maturity](https://github.com/mollie/mollie-api-python-beta/blob/master/#maturity)
  * [Contributions](https://github.com/mollie/mollie-api-python-beta/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

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

from mollie import Client

sdk = Client(
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
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.payments.create(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
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
        "locale": "en_US",
        "method": "ideal",
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": "manual",
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
                    "type": "organization",
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
                    "type": "organization",
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
        "sequence_type": "oneoff",
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import mollie
from mollie import Client
import os

async def main():

    async with Client(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client:

        res = await client.payments.create_async(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                        mollie.Categories.MEAL,
                        mollie.Categories.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": "12 months",
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
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
                        mollie.Categories.MEAL,
                        mollie.Categories.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": "12 months",
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
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
                        mollie.Categories.MEAL,
                        mollie.Categories.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": "12 months",
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
            "locale": "en_US",
            "method": "ideal",
            "issuer": "ideal_INGBNL2A",
            "restrict_payment_methods_to_country": "NL",
            "capture_mode": "manual",
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
                        "type": "organization",
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
                        "type": "organization",
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
            "sequence_type": "oneoff",
            "mandate_id": "mdt_5B8cwPMGnU",
            "customer_id": "cst_5B8cwPMGnU",
            "profile_id": "pfl_5B8cwPMGnU",
            "due_date": "2025-01-01",
            "testmode": False,
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
import mollie
from mollie import Client
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.payments.create(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
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
        "locale": "en_US",
        "method": "ideal",
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": "manual",
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
                    "type": "organization",
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
                    "type": "organization",
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
        "sequence_type": "oneoff",
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [balances](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/balances/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/balances/README.md#list) - List balances
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/balances/README.md#get) - Get balance
* [get_primary](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/balances/README.md#get_primary) - Get primary balance
* [get_report](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/balances/README.md#get_report) - Get balance report
* [list_transactions](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/balances/README.md#list_transactions) - List balance transactions

### [capabilities](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/capabilities/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/capabilities/README.md#list) - List capabilities

### [captures](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/captures/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/captures/README.md#create) - Create capture
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/captures/README.md#list) - List captures
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/captures/README.md#get) - Get capture

### [chargebacks](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/chargebacks/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/chargebacks/README.md#list) - List payment chargebacks
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/chargebacks/README.md#get) - Get payment chargeback
* [all](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/chargebacks/README.md#all) - List all chargebacks


### [client_links](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/clientlinks/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/clientlinks/README.md#create) - Create client link

### [clients](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/clients/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/clients/README.md#list) - List clients
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/clients/README.md#get) - Get client

### [customers](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#create) - Create customer
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#list) - List customers
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#get) - Get customer
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#update) - Update customer
* [delete](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#delete) - Delete customer
* [create_payment](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#create_payment) - Create customer payment
* [list_payments](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/customers/README.md#list_payments) - List customer payments

### [delayed_routing](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/delayedrouting/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/delayedrouting/README.md#create) - Create a delayed route
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/delayedrouting/README.md#list) - List payment routes

### [invoices](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/invoices/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/invoices/README.md#list) - List invoices
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/invoices/README.md#get) - Get invoice

### [mandates](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/mandates/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/mandates/README.md#create) - Create mandate
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/mandates/README.md#list) - List mandates
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/mandates/README.md#get) - Get mandate
* [revoke](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/mandates/README.md#revoke) - Revoke mandate

### [methods](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/methods/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/methods/README.md#list) - List payment methods
* [all](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/methods/README.md#all) - List all payment methods
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/methods/README.md#get) - Get payment method

### [onboarding](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/onboarding/README.md)

* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/onboarding/README.md#get) - Get onboarding status
* [submit](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/onboarding/README.md#submit) - Submit onboarding data

### [organizations](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/organizations/README.md)

* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/organizations/README.md#get) - Get organization
* [get_current](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/organizations/README.md#get_current) - Get current organization
* [get_partner](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/organizations/README.md#get_partner) - Get partner status

### [payment_links](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md#create) - Create payment link
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md#list) - List payment links
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md#get) - Get payment link
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md#update) - Update payment link
* [delete](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md#delete) - Delete payment link
* [list_payments](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/paymentlinks/README.md#list_payments) - Get payment link payments

### [payments](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md#create) - Create payment
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md#list) - List payments
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md#get) - Get payment
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md#update) - Update payment
* [cancel](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md#cancel) - Cancel payment
* [release_authorization](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/payments/README.md#release_authorization) - Release payment authorization

### [permissions](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/permissions/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/permissions/README.md#list) - List permissions
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/permissions/README.md#get) - Get permission

### [profiles](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md#create) - Create profile
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md#list) - List profiles
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md#get) - Get profile
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md#update) - Update profile
* [delete](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md#delete) - Delete profile
* [get_current](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/profiles/README.md#get_current) - Get current profile

### [refunds](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#create) - Create payment refund
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#list) - List payment refunds
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#get) - Get payment refund
* [cancel](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#cancel) - Cancel payment refund
* [create_order](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#create_order) - Create order refund
* [list_for_order](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#list_for_order) - List order refunds
* [all](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/refunds/README.md#all) - List all refunds

### [sales_invoices](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/salesinvoices/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/salesinvoices/README.md#create) - Create sales invoice
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/salesinvoices/README.md#list) - List sales invoices
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/salesinvoices/README.md#get) - Get sales invoice
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/salesinvoices/README.md#update) - Update sales invoice
* [delete](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/salesinvoices/README.md#delete) - Delete sales invoice

### [settlements](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#list) - List settlements
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#get) - Get settlement
* [get_open](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#get_open) - Get open settlement
* [get_next](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#get_next) - Get next settlement
* [list_payments](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#list_payments) - Get settlement payments
* [list_captures](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#list_captures) - Get settlement captures
* [list_refunds](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#list_refunds) - Get settlement refunds
* [list_chargebacks](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/settlements/README.md#list_chargebacks) - Get settlement chargebacks

### [subscriptions](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#create) - Create subscription
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#list) - List customer subscriptions
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#get) - Get subscription
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#update) - Update subscription
* [cancel](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#cancel) - Cancel subscription
* [all](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#all) - List all subscriptions
* [list_payments](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/subscriptions/README.md#list_payments) - List subscription payments

### [terminals](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/terminals/README.md)

* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/terminals/README.md#list) - List terminals
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/terminals/README.md#get) - Get terminal

### [wallets](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/wallets/README.md)

* [request_apple_pay_session](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/wallets/README.md#request_apple_pay_session) - Request Apple Pay payment session

### [webhook_events](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhookevents/README.md)

* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhookevents/README.md#get) - Get a Webhook Event

### [webhooks](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md)

* [create](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md#create) - Create a webhook
* [list](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md#list) - List all webhooks
* [update](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md#update) - Update a webhook
* [get](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md#get) - Get a webhook
* [delete](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md#delete) - Delete a webhook
* [test](https://github.com/mollie/mollie-api-python-beta/blob/master/docs/sdks/webhooks/README.md#test) - Test a webhook

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import mollie
from mollie import Client
from mollie.utils import BackoffStrategy, RetryConfig
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.payments.create(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
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
        "locale": "en_US",
        "method": "ideal",
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": "manual",
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
                    "type": "organization",
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
                    "type": "organization",
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
        "sequence_type": "oneoff",
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import mollie
from mollie import Client
from mollie.utils import BackoffStrategy, RetryConfig
import os


with Client(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.payments.create(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
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
        "locale": "en_US",
        "method": "ideal",
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": "manual",
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
                    "type": "organization",
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
                    "type": "organization",
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
        "sequence_type": "oneoff",
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ClientError`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/clienterror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/mollie/mollie-api-python-beta/blob/master/#error-classes). |

### Example
```python
import mollie
from mollie import Client, models
import os


with Client(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:
    res = None
    try:

        res = client.payments.create(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                        mollie.Categories.MEAL,
                        mollie.Categories.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": "12 months",
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
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
                        mollie.Categories.MEAL,
                        mollie.Categories.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": "12 months",
                        "amount": {
                            "currency": "EUR",
                            "value": "10.00",
                        },
                        "times": 1,
                        "start_date": "2024-12-12",
                    },
                },
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
                        mollie.Categories.MEAL,
                        mollie.Categories.ECO,
                    ],
                    "image_url": "https://...",
                    "product_url": "https://...",
                    "recurring": {
                        "description": "Gym subscription",
                        "interval": "12 months",
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
            "locale": "en_US",
            "method": "ideal",
            "issuer": "ideal_INGBNL2A",
            "restrict_payment_methods_to_country": "NL",
            "capture_mode": "manual",
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
                        "type": "organization",
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
                        "type": "organization",
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
            "sequence_type": "oneoff",
            "mandate_id": "mdt_5B8cwPMGnU",
            "customer_id": "cst_5B8cwPMGnU",
            "profile_id": "pfl_5B8cwPMGnU",
            "due_date": "2025-01-01",
            "testmode": False,
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
        if isinstance(e, models.CreatePaymentPaymentsResponseBody):
            print(e.data.status)  # int
            print(e.data.title)  # str
            print(e.data.detail)  # str
            print(e.data.field)  # Optional[str]
            print(e.data.links)  # mollie.CreatePaymentPaymentsResponseLinks
```

### Error Classes
**Primary error:**
* [`ClientError`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/clienterror.py): The base class for HTTP error responses.

<details><summary>Less common errors (133)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ClientError`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/clienterror.py)**:
* [`ListPaymentsPaymentsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listpaymentspaymentsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListMethodsMethodsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listmethodsmethodsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListAllMethodsMethodsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listallmethodsmethodsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetMethodMethodsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getmethodmethodsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListRefundsRefundsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listrefundsrefundsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListOrderRefundsRefundsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listorderrefundsrefundsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListAllRefundsRefundsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listallrefundsrefundsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListChargebacksChargebacksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listchargebackschargebacksresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListAllChargebacksChargebacksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listallchargebackschargebacksresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListCapturesCapturesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listcapturescapturesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListPaymentLinksPaymentLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listpaymentlinkspaymentlinksresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetPaymentLinkPaymentsPaymentLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getpaymentlinkpaymentspaymentlinksresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListTerminalsTerminalsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listterminalsterminalsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListCustomersCustomersResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listcustomerscustomersresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListCustomerPaymentsCustomersResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listcustomerpaymentscustomersresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListMandatesMandatesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listmandatesmandatesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListSubscriptionsSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listsubscriptionssubscriptionsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListAllSubscriptionsSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listallsubscriptionssubscriptionsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListSubscriptionPaymentsSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listsubscriptionpaymentssubscriptionsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListPermissionsPermissionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listpermissionspermissionsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListProfilesProfilesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listprofilesprofilesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListClientsClientsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listclientsclientsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListWebhooksWebhooksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listwebhookswebhooksresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListBalancesBalancesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listbalancesbalancesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListBalanceTransactionsBalancesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listbalancetransactionsbalancesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListSettlementsSettlementsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listsettlementssettlementsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetSettlementPaymentsSettlementsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementpaymentssettlementsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetSettlementCapturesSettlementsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementcapturessettlementsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetSettlementRefundsSettlementsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementrefundssettlementsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetSettlementChargebacksSettlementsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementchargebackssettlementsresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListInvoicesInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listinvoicesinvoicesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`ListSalesInvoicesSalesInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listsalesinvoicessalesinvoicesresponsebody.py): An error response object. Status code `400`. Applicable to 1 of 95 methods.*
* [`GetPaymentPaymentsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getpaymentpaymentsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdatePaymentPaymentsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatepaymentpaymentsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CancelPaymentPaymentsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/cancelpaymentpaymentsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ReleaseAuthorizationResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/releaseauthorizationresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetMethodMethodsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getmethodmethodsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateRefundRefundsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createrefundrefundsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListRefundsRefundsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listrefundsrefundsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetRefundRefundsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getrefundrefundsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CancelRefundResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/cancelrefundresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateOrderRefundRefundsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createorderrefundrefundsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListChargebacksChargebacksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listchargebackschargebacksresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetChargebackChargebacksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getchargebackchargebacksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListAllChargebacksChargebacksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listallchargebackschargebacksresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateCaptureCapturesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createcapturecapturesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListCapturesCapturesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listcapturescapturesresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetCaptureCapturesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getcapturecapturesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreatePaymentLinkPaymentLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createpaymentlinkpaymentlinksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetPaymentLinkPaymentLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getpaymentlinkpaymentlinksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdatePaymentLinkPaymentLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatepaymentlinkpaymentlinksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`DeletePaymentLinkResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletepaymentlinkresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetTerminalTerminalsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getterminalterminalsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`PaymentCreateRouteDelayedRoutingResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/paymentcreateroutedelayedroutingresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`PaymentListRoutesDelayedRoutingResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/paymentlistroutesdelayedroutingresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateCustomerCustomersResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createcustomercustomersresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListCustomersCustomersResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listcustomerscustomersresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetCustomerCustomersResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getcustomercustomersresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdateCustomerCustomersResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatecustomercustomersresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`DeleteCustomerResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletecustomerresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateMandateMandatesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createmandatemandatesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListMandatesMandatesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listmandatesmandatesresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetMandateMandatesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getmandatemandatesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`RevokeMandateResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/revokemandateresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateSubscriptionSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createsubscriptionsubscriptionsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListSubscriptionsSubscriptionsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listsubscriptionssubscriptionsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetSubscriptionSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsubscriptionsubscriptionsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdateSubscriptionSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatesubscriptionsubscriptionsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CancelSubscriptionSubscriptionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/cancelsubscriptionsubscriptionsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetPermissionPermissionsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getpermissionpermissionsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetOrganizationOrganizationsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getorganizationorganizationsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetProfileProfilesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getprofileprofilesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdateProfileProfilesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updateprofileprofilesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`DeleteProfileResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deleteprofileresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListClientsClientsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listclientsclientsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetClientClientsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getclientclientsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateClientLinkClientLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createclientlinkclientlinksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdateWebhookWebhooksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatewebhookwebhooksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetWebhookWebhooksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getwebhookwebhooksresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`DeleteWebhookResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletewebhookresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`TestWebhookResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/testwebhookresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetWebhookEventWebhookEventsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getwebhookeventwebhookeventsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListBalancesBalancesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listbalancesbalancesresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetBalanceBalancesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getbalancebalancesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetBalanceReportBalancesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getbalancereportbalancesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListBalanceTransactionsBalancesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listbalancetransactionsbalancesresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListSettlementsSettlementsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listsettlementssettlementsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetSettlementSettlementsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementsettlementsresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetSettlementCapturesSettlementsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementcapturessettlementsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetSettlementRefundsSettlementsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementrefundssettlementsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetSettlementChargebacksSettlementsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsettlementchargebackssettlementsresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`ListInvoicesInvoicesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listinvoicesinvoicesresponseresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetInvoiceInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getinvoiceinvoicesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateSalesInvoiceSalesInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createsalesinvoicesalesinvoicesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`GetSalesInvoiceSalesInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getsalesinvoicesalesinvoicesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`UpdateSalesInvoiceSalesInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatesalesinvoicesalesinvoicesresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`DeleteSalesInvoiceResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletesalesinvoiceresponsebody.py): An error response object. Status code `404`. Applicable to 1 of 95 methods.*
* [`CreateRefundRefundsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createrefundrefundsresponseresponsebody.py): An error response object. Status code `409`. Applicable to 1 of 95 methods.*
* [`GetProfileProfilesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getprofileprofilesresponseresponsebody.py): An error response object. Status code `410`. Applicable to 1 of 95 methods.*
* [`UpdateProfileProfilesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updateprofileprofilesresponseresponsebody.py): An error response object. Status code `410`. Applicable to 1 of 95 methods.*
* [`DeleteProfileProfilesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deleteprofileprofilesresponsebody.py): An error response object. Status code `410`. Applicable to 1 of 95 methods.*
* [`CreatePaymentPaymentsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createpaymentpaymentsresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`UpdatePaymentPaymentsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatepaymentpaymentsresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CancelPaymentPaymentsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/cancelpaymentpaymentsresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`ReleaseAuthorizationPaymentsResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/releaseauthorizationpaymentsresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateRefundRefundsResponse422ResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createrefundrefundsresponse422responsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateOrderRefundRefundsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createorderrefundrefundsresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateCaptureCapturesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createcapturecapturesresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`RequestApplePayPaymentSessionResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/requestapplepaypaymentsessionresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreatePaymentLinkPaymentLinksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createpaymentlinkpaymentlinksresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`UpdatePaymentLinkPaymentLinksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatepaymentlinkpaymentlinksresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`DeletePaymentLinkPaymentLinksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletepaymentlinkpaymentlinksresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateCustomerPaymentCustomersResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createcustomerpaymentcustomersresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateProfileProfilesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createprofileprofilesresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`UpdateProfileProfilesResponse422ResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updateprofileprofilesresponse422responsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateClientLinkClientLinksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createclientlinkclientlinksresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateWebhookWebhooksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createwebhookwebhooksresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`UpdateWebhookWebhooksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatewebhookwebhooksresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`GetWebhookWebhooksResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getwebhookwebhooksresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`DeleteWebhookWebhooksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletewebhookwebhooksresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`TestWebhookWebhooksResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/testwebhookwebhooksresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`GetBalanceReportBalancesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/getbalancereportbalancesresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`CreateSalesInvoiceSalesInvoicesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createsalesinvoicesalesinvoicesresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`UpdateSalesInvoiceSalesInvoicesResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/updatesalesinvoicesalesinvoicesresponseresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`DeleteSalesInvoiceSalesInvoicesResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/deletesalesinvoicesalesinvoicesresponsebody.py): An error response object. Status code `422`. Applicable to 1 of 95 methods.*
* [`ListBalanceTransactionsBalancesResponse429ResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/listbalancetransactionsbalancesresponse429responsebody.py): An error response object. Status code `429`. Applicable to 1 of 95 methods.*
* [`CreatePaymentPaymentsResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createpaymentpaymentsresponseresponsebody.py): An error response object. Status code `503`. Applicable to 1 of 95 methods.*
* [`CreateCustomerPaymentCustomersResponseResponseBody`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/createcustomerpaymentcustomersresponseresponsebody.py): An error response object. Status code `503`. Applicable to 1 of 95 methods.*
* [`ResponseValidationError`](https://github.com/mollie/mollie-api-python-beta/blob/master/./src/mollie/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/mollie/mollie-api-python-beta/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import mollie
from mollie import Client
import os


with Client(
    server_url="https://api.mollie.com/v2",
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client:

    res = client.payments.create(include=mollie.Include.DETAILS_QR_CODE, request_body={
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "times": 1,
                    "start_date": "2024-12-12",
                },
            },
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
                    mollie.Categories.MEAL,
                    mollie.Categories.ECO,
                ],
                "image_url": "https://...",
                "product_url": "https://...",
                "recurring": {
                    "description": "Gym subscription",
                    "interval": "12 months",
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
        "locale": "en_US",
        "method": "ideal",
        "issuer": "ideal_INGBNL2A",
        "restrict_payment_methods_to_country": "NL",
        "capture_mode": "manual",
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
                    "type": "organization",
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
                    "type": "organization",
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
        "sequence_type": "oneoff",
        "mandate_id": "mdt_5B8cwPMGnU",
        "customer_id": "cst_5B8cwPMGnU",
        "profile_id": "pfl_5B8cwPMGnU",
        "due_date": "2025-01-01",
        "testmode": False,
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
from mollie import Client
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Client(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from mollie import Client
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

s = Client(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Client` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import mollie
from mollie import Client
import os
def main():

    with Client(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Client(
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from mollie import Client
import logging

logging.basicConfig(level=logging.DEBUG)
s = Client(debug_logger=logging.getLogger("mollie"))
```

You can also enable a default debug logger by setting an environment variable `CLIENT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=mollie-api-python-beta&utm_campaign=python)
