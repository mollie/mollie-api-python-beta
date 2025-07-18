"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from mollie.models import ClientError
from mollie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from mollie.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateWebhookEventTypes(str, Enum):
    r"""The list of events to enable for this webhook. You may specify `'*'` to add all events, except those that require explicit selection. Separate multiple event types with a comma."""

    PAYMENT_LINK_PAID = "payment-link.paid"
    SALES_INVOICE_CREATED = "sales-invoice.created"
    SALES_INVOICE_ISSUED = "sales-invoice.issued"
    SALES_INVOICE_CANCELED = "sales-invoice.canceled"
    SALES_INVOICE_PAID = "sales-invoice.paid"


class UpdateWebhookRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""A name that identifies the webhook."""
    url: NotRequired[str]
    r"""The URL Mollie will send the events to. This URL must be publicly accessible."""
    event_types: NotRequired[UpdateWebhookEventTypes]
    r"""The list of events to enable for this webhook. You may specify `'*'` to add all events, except those that require explicit selection. Separate multiple event types with a comma."""
    testmode: NotRequired[Nullable[bool]]
    r"""Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.

    Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.
    """


class UpdateWebhookRequestBody(BaseModel):
    name: Optional[str] = None
    r"""A name that identifies the webhook."""

    url: Optional[str] = None
    r"""The URL Mollie will send the events to. This URL must be publicly accessible."""

    event_types: Annotated[
        Optional[UpdateWebhookEventTypes], pydantic.Field(alias="eventTypes")
    ] = None
    r"""The list of events to enable for this webhook. You may specify `'*'` to add all events, except those that require explicit selection. Separate multiple event types with a comma."""

    testmode: OptionalNullable[bool] = UNSET
    r"""Most API credentials are specifically created for either live mode or test mode. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting `testmode` to `true`.

    Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "url", "eventTypes", "testmode"]
        nullable_fields = ["testmode"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class UpdateWebhookRequestTypedDict(TypedDict):
    id: str
    r"""Provide the ID of the item you want to perform this operation on."""
    request_body: NotRequired[UpdateWebhookRequestBodyTypedDict]


class UpdateWebhookRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Provide the ID of the item you want to perform this operation on."""

    request_body: Annotated[
        Optional[UpdateWebhookRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class UpdateWebhookWebhooksDocumentationTypedDict(TypedDict):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str
    type: str


class UpdateWebhookWebhooksDocumentation(BaseModel):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str

    type: str


class UpdateWebhookWebhooksLinksTypedDict(TypedDict):
    documentation: UpdateWebhookWebhooksDocumentationTypedDict
    r"""The URL to the generic Mollie API error handling guide."""


class UpdateWebhookWebhooksLinks(BaseModel):
    documentation: UpdateWebhookWebhooksDocumentation
    r"""The URL to the generic Mollie API error handling guide."""


class UpdateWebhookWebhooksResponseResponseBodyData(BaseModel):
    status: int
    r"""The status code of the error message. This is always the same code as the status code of the HTTP message itself."""

    title: str
    r"""The HTTP reason phrase of the error. For example, for a `404` error, the `title` will be `Not Found`."""

    detail: str
    r"""A detailed human-readable description of the error that occurred."""

    links: Annotated[UpdateWebhookWebhooksLinks, pydantic.Field(alias="_links")]

    field: Optional[str] = None
    r"""If the error was caused by a value provided by you in a specific field, the `field` property will contain the name of the field that caused the issue."""


class UpdateWebhookWebhooksResponseResponseBody(ClientError):
    r"""An error response object."""

    data: UpdateWebhookWebhooksResponseResponseBodyData

    def __init__(
        self,
        data: UpdateWebhookWebhooksResponseResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data


class UpdateWebhookDocumentationTypedDict(TypedDict):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str
    type: str


class UpdateWebhookDocumentation(BaseModel):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str

    type: str


class UpdateWebhookLinksTypedDict(TypedDict):
    documentation: UpdateWebhookDocumentationTypedDict
    r"""The URL to the generic Mollie API error handling guide."""


class UpdateWebhookLinks(BaseModel):
    documentation: UpdateWebhookDocumentation
    r"""The URL to the generic Mollie API error handling guide."""


class UpdateWebhookWebhooksResponseBodyData(BaseModel):
    status: int
    r"""The status code of the error message. This is always the same code as the status code of the HTTP message itself."""

    title: str
    r"""The HTTP reason phrase of the error. For example, for a `404` error, the `title` will be `Not Found`."""

    detail: str
    r"""A detailed human-readable description of the error that occurred."""

    links: Annotated[UpdateWebhookLinks, pydantic.Field(alias="_links")]

    field: Optional[str] = None
    r"""If the error was caused by a value provided by you in a specific field, the `field` property will contain the name of the field that caused the issue."""


class UpdateWebhookWebhooksResponseBody(ClientError):
    r"""An error response object."""

    data: UpdateWebhookWebhooksResponseBodyData

    def __init__(
        self,
        data: UpdateWebhookWebhooksResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data


class UpdateWebhookResponseBodyTypedDict(TypedDict):
    r"""The webhook object."""

    resource: NotRequired[str]
    r"""Indicates the response contains a webhook subscription object. Will always contain the string `webhook` for this endpoint."""
    id: NotRequired[str]
    r"""The identifier uniquely referring to this subscription."""
    url: NotRequired[str]
    r"""The subscription's events destination."""
    profile_id: NotRequired[str]
    r"""The identifier uniquely referring to the profile that created the subscription."""
    created_at: NotRequired[str]
    r"""The subscription's date time of creation."""
    name: NotRequired[str]
    r"""The subscription's name."""
    event_types: NotRequired[List[str]]
    r"""The events types that are subscribed."""
    status: NotRequired[str]
    r"""The subscription's current status.

    Possible values: `enabled` `blocked` `disabled`
    """
    mode: NotRequired[str]
    r"""The subscription's mode.

    Possible values: `live` `test`
    """


class UpdateWebhookResponseBody(BaseModel):
    r"""The webhook object."""

    resource: Optional[str] = "webhook"
    r"""Indicates the response contains a webhook subscription object. Will always contain the string `webhook` for this endpoint."""

    id: Optional[str] = None
    r"""The identifier uniquely referring to this subscription."""

    url: Optional[str] = None
    r"""The subscription's events destination."""

    profile_id: Annotated[Optional[str], pydantic.Field(alias="profileId")] = None
    r"""The identifier uniquely referring to the profile that created the subscription."""

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None
    r"""The subscription's date time of creation."""

    name: Optional[str] = None
    r"""The subscription's name."""

    event_types: Annotated[Optional[List[str]], pydantic.Field(alias="eventTypes")] = (
        None
    )
    r"""The events types that are subscribed."""

    status: Optional[str] = None
    r"""The subscription's current status.

    Possible values: `enabled` `blocked` `disabled`
    """

    mode: Optional[str] = None
    r"""The subscription's mode.

    Possible values: `live` `test`
    """
