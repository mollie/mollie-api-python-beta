# mollie-api-python-alpha

Developer-friendly & type-safe Python SDK specifically catered to leverage *mollie-api-python-alpha* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=mollie-api-python-alpha&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [mollie-api-python-alpha](https://github.com/mollie/mollie-api-python-alpha/blob/master/#mollie-api-python-alpha)
  * [SDK Installation](https://github.com/mollie/mollie-api-python-alpha/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/mollie/mollie-api-python-alpha/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/mollie/mollie-api-python-alpha/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/mollie/mollie-api-python-alpha/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/mollie/mollie-api-python-alpha/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/mollie/mollie-api-python-alpha/blob/master/#retries)
  * [Error Handling](https://github.com/mollie/mollie-api-python-alpha/blob/master/#error-handling)
  * [Server Selection](https://github.com/mollie/mollie-api-python-alpha/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/mollie/mollie-api-python-alpha/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/mollie/mollie-api-python-alpha/blob/master/#resource-management)
  * [Debugging](https://github.com/mollie/mollie-api-python-alpha/blob/master/#debugging)
* [Development](https://github.com/mollie/mollie-api-python-alpha/blob/master/#development)
  * [Maturity](https://github.com/mollie/mollie-api-python-alpha/blob/master/#maturity)
  * [Contributions](https://github.com/mollie/mollie-api-python-alpha/blob/master/#contributions)

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
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [balances](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/balances/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/balances/README.md#list) - List balances
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/balances/README.md#get) - Get balance
* [get_primary](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/balances/README.md#get_primary) - Get primary balance
* [get_report](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/balances/README.md#get_report) - Get balance report
* [list_transactions](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/balances/README.md#list_transactions) - List balance transactions

### [capabilities](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/capabilities/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/capabilities/README.md#list) - List capabilities

### [captures](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/captures/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/captures/README.md#create) - Create capture
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/captures/README.md#list) - List captures
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/captures/README.md#get) - Get capture

### [chargebacks](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/chargebacks/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/chargebacks/README.md#list) - List payment chargebacks
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/chargebacks/README.md#get) - Get payment chargeback
* [all](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/chargebacks/README.md#all) - List all chargebacks


### [client_links](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/clientlinks/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/clientlinks/README.md#create) - Create client link

### [clients](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/clients/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/clients/README.md#list) - List clients
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/clients/README.md#get) - Get client

### [customers](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#create) - Create customer
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#list) - List customers
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#get) - Get customer
* [update](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#update) - Update customer
* [delete](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#delete) - Delete customer
* [create_payment](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#create_payment) - Create customer payment
* [list_payments](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/customers/README.md#list_payments) - List customer payments

### [delayed_routing](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/delayedrouting/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/delayedrouting/README.md#create) - Create a delayed route
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/delayedrouting/README.md#list) - List payment routes

### [invoices](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/invoices/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/invoices/README.md#list) - List invoices
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/invoices/README.md#get) - Get invoice

### [mandates](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/mandates/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/mandates/README.md#create) - Create mandate
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/mandates/README.md#list) - List mandates
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/mandates/README.md#get) - Get mandate
* [revoke](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/mandates/README.md#revoke) - Revoke mandate

### [methods](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/methods/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/methods/README.md#list) - List payment methods
* [all](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/methods/README.md#all) - List all payment methods
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/methods/README.md#get) - Get payment method

### [onboarding](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/onboarding/README.md)

* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/onboarding/README.md#get) - Get onboarding status
* [submit](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/onboarding/README.md#submit) - Submit onboarding data

### [organizations](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/organizations/README.md)

* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/organizations/README.md#get) - Get organization
* [get_current](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/organizations/README.md#get_current) - Get current organization
* [get_partner](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/organizations/README.md#get_partner) - Get partner status

### [payment_links](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md#create) - Create payment link
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md#list) - List payment links
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md#get) - Get payment link
* [update](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md#update) - Update payment link
* [delete](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md#delete) - Delete payment link
* [list_payments](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/paymentlinks/README.md#list_payments) - Get payment link payments

### [payments](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md#create) - Create payment
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md#list) - List payments
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md#get) - Get payment
* [update](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md#update) - Update payment
* [cancel](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md#cancel) - Cancel payment
* [release_authorization](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/payments/README.md#release_authorization) - Release payment authorization

### [permissions](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/permissions/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/permissions/README.md#list) - List permissions
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/permissions/README.md#get) - Get permission

### [profiles](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md#create) - Create profile
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md#list) - List profiles
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md#get) - Get profile
* [update](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md#update) - Update profile
* [delete](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md#delete) - Delete profile
* [get_current](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/profiles/README.md#get_current) - Get current profile

### [refunds](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#create) - Create payment refund
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#list) - List payment refunds
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#get) - Get payment refund
* [cancel](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#cancel) - Cancel payment refund
* [create_order](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#create_order) - Create order refund
* [list_for_order](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#list_for_order) - List order refunds
* [all](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/refunds/README.md#all) - List all refunds

### [settlements](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#list) - List settlements
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#get) - Get settlement
* [get_open](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#get_open) - Get open settlement
* [get_next](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#get_next) - Get next settlement
* [list_payments](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#list_payments) - Get settlement payments
* [list_captures](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#list_captures) - Get settlement captures
* [list_refunds](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#list_refunds) - Get settlement refunds
* [list_chargebacks](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/settlements/README.md#list_chargebacks) - Get settlement chargebacks

### [subscriptions](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md)

* [create](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#create) - Create subscription
* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#list) - List customer subscriptions
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#get) - Get subscription
* [update](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#update) - Update subscription
* [cancel](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#cancel) - Cancel subscription
* [all](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#all) - List all subscriptions
* [list_payments](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/subscriptions/README.md#list_payments) - List subscription payments

### [terminals](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/terminals/README.md)

* [list](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/terminals/README.md#list) - List terminals
* [get](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/terminals/README.md#get) - Get terminal

### [wallets](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/wallets/README.md)

* [request_apple_pay_session](https://github.com/mollie/mollie-api-python-alpha/blob/master/docs/sdks/wallets/README.md#request_apple_pay_session) - Request Apple Pay payment session

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
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type                                       | Status Code | Content Type         |
| ------------------------------------------------ | ----------- | -------------------- |
| models.CreatePaymentPaymentsResponseBody         | 422         | application/hal+json |
| models.CreatePaymentPaymentsResponseResponseBody | 503         | application/hal+json |
| models.APIError                                  | 4XX, 5XX    | \*/\*                |

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
        })

        # Handle response
        print(res)

    except models.CreatePaymentPaymentsResponseBody as e:
        # handle e.data: models.CreatePaymentPaymentsResponseBodyData
        raise(e)
    except models.CreatePaymentPaymentsResponseResponseBody as e:
        # handle e.data: models.CreatePaymentPaymentsResponseResponseBodyData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
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

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=mollie-api-python-alpha&utm_campaign=python)
