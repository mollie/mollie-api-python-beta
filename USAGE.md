<!-- Start SDK Example Usage [usage] -->
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