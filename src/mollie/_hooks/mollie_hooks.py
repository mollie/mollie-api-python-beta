import uuid

from httpx import Request
from typing import Union

from .types import (
    BeforeRequestHook,
    BeforeRequestContext,
)

def generate_idempotency_key() -> str:
    """
    Generates a UUID4 to be used as an idempotency key.
    @see https://docs.mollie.com/reference/api-idempotency#using-an-idempotency-key

    :return: A string representation of a UUID4.
    """
    return str(uuid.uuid4())


class MollieHooks(BeforeRequestHook):
    def before_request(self, hook_ctx: BeforeRequestContext, request: Request) -> Union[Request, Exception]:
        """
        Modify the request before sending.

        :param hook_ctx: Context for the hook, containing request metadata.
        :param request: The HTTP request to modify.
        :return: The modified request or an exception.
        """
        idempotency_key = "idempotency-key"

        # Create a copy of the headers
        headers = dict(request.headers or {})

        # Add the idempotency key if it doesn't already exist
        if idempotency_key not in headers or not headers[idempotency_key]:
            headers[idempotency_key] = generate_idempotency_key()

        return Request(
            method = request.method,
            url = request.url,
            headers = headers,
            content = request.content,
            extensions=request.extensions
        )
