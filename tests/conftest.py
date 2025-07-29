import pytest

from mollie import Client, Security

@pytest.fixture
def client() -> Client:
    """
    Fixture to create a test client for the Mollie API.

    :return: An instance of the Mollie Client with API key.
    """
    return Client(
        security=Security(
            api_key="test_api_key"
        )
    )

@pytest.fixture
def create_payment_payload() -> dict:
    return {
        "resource": "payment",
        "id": "tr_g3e58pyMUGs558SAuz4CJ",
        "mode": "live",
        "createdAt": "2025-07-29T12:41:15+00:00",
        "amount": {
            "value": "0.01",
            "currency": "EUR"
        },
        "description": "AO - Test payment ok",
        "method": None,
        "metadata": None,
        "status": "open",
        "isCancelable": False,
        "expiresAt": "2025-07-29T12:56:15+00:00",
        "profileId": "pfl_i3ZjRpPRbJ",
        "sequenceType": "oneoff",
        "redirectUrl": "https://example.com",
        "_links": {
            "self": {
                "href": "https://api.mollie.localhost/v2/payments/tr_g3e58pyMUGs558SAuz4CJ",
                "type": "application/hal+json"
            },
            "checkout": {
                "href": "https://mp.mollie.localhost/checkout/select-method/g3e58pyMUGs558SAuz4CJ",
                "type": "text/html"
            },
            "dashboard": {
                "href": "https://my.mollie.localhost/dashboard/org_7/payments/tr_g3e58pyMUGs558SAuz4CJ",
                "type": "text/html"
            },
            "documentation": {
                "href": "https://docs.mollie.com/reference/create-payment",
                "type": "text/html"
            }
        }
    }