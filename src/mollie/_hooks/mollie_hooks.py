import uuid
import sys

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
        # Create a copy of the headers
        headers = dict(request.headers or {})

        # Add the idempotency key if it doesn't already exist
        headers = self._handle_idempotency_key(headers)

        # Customize the User Agent header
        headers = self._customize_user_agent(headers, hook_ctx)

        return Request(
            method = request.method,
            url = request.url,
            headers = headers,
            content = request.content,
            extensions=request.extensions
        )
    
    def _handle_idempotency_key(self, headers: dict) -> dict:
        idempotency_key = "idempotency-key"
        if idempotency_key not in headers or not headers[idempotency_key]:
            headers[idempotency_key] = generate_idempotency_key()
        return headers
    
    def _customize_user_agent(self, headers: dict, hook_ctx: BeforeRequestContext) -> dict:
        user_agent_key = "user-agent"

        current_user_agent = headers.get(user_agent_key, None)

        if not current_user_agent:
            return headers

        # Get version information from the SDK configuration instead of parsing user agent
        sdk_version = hook_ctx.config.sdk_version
        gen_version = hook_ctx.config.gen_version
        python_version = sys.version.split(" ", maxsplit=1)[0]

        new_user_agent = f"Speakeasy/{gen_version} Python/{python_version} mollie-api-python-beta/{sdk_version}"
        if hook_ctx.config.globals.custom_user_agent:
            new_user_agent = f"{new_user_agent} {hook_ctx.config.globals.custom_user_agent}"

        headers[user_agent_key] = new_user_agent

        return headers
