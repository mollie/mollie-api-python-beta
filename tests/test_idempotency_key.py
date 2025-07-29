from mollie import Client
from unittest.mock import patch
from httpx import Response, Request

class TestIdempotencyKey:
    def test_idempotency_key_is_added(self, client: Client, create_payment_payload: dict):
        def mock_send(request: Request, stream = False):
            assert request.method == "POST"
            assert request.url.path.endswith("/payments")

            headers = dict(request.headers or {})

            print("Request Headers:", headers)

            assert "idempotency-ke" in headers
            assert headers["idempotency-key"] is not None

            return Response(
                status_code=201,
                request=request,
                headers={
                    'Content-Type': 'application/hal+json',
                },
                json=create_payment_payload
            )

        with patch.object(client.sdk_configuration.client, 'send', side_effect=mock_send):
            response = client.payments.create(
                request_body={
                    "description": "Chess Board",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "redirect_url": "https://example.org/redirect"
                }
            )

    def test_idempotency_key_is_not_replaced(self, client: Client, create_payment_payload: dict):
        idempotency_key = "some-key"

        def mock_send(request: Request, stream = False):
            assert request.method == "POST"
            assert request.url.path.endswith("/payments")

            headers = dict(request.headers or {})

            print("Request Headers:", headers)

            assert "idempotency-key" in headers
            assert headers["idempotency-key"] == idempotency_key

            return Response(
                status_code=201,
                request=request,
                headers={
                    'Content-Type': 'application/hal+json',
                },
                json=create_payment_payload
            )

        with patch.object(client.sdk_configuration.client, 'send', side_effect=mock_send):
            response = client.payments.create(
                http_headers={"Idempotency-Key": idempotency_key},
                request_body={
                    "description": "Chess Board",
                    "amount": {
                        "currency": "EUR",
                        "value": "10.00",
                    },
                    "redirect_url": "https://example.org/redirect"
                }
            )