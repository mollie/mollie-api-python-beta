"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from mollie.models import ClientError
from mollie.types import BaseModel
from mollie.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PaymentCreateRouteAmountTypedDict(TypedDict):
    r"""The amount of the route. That amount that will be routed to the specified destination."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class PaymentCreateRouteAmount(BaseModel):
    r"""The amount of the route. That amount that will be routed to the specified destination."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class PaymentCreateRouteDestinationTypedDict(TypedDict):
    r"""The destination of the route."""

    type: str
    r"""The type of destination. Currently only the destination type `organization` is supported.

    Possible values: `organization`
    """
    organization_id: str
    r"""Required for destination type `organization`. The ID of the connected organization the funds should be routed to."""


class PaymentCreateRouteDestination(BaseModel):
    r"""The destination of the route."""

    type: str
    r"""The type of destination. Currently only the destination type `organization` is supported.

    Possible values: `organization`
    """

    organization_id: Annotated[str, pydantic.Field(alias="organizationId")]
    r"""Required for destination type `organization`. The ID of the connected organization the funds should be routed to."""


class PaymentCreateRouteRequestBodyTypedDict(TypedDict):
    amount: NotRequired[PaymentCreateRouteAmountTypedDict]
    r"""The amount of the route. That amount that will be routed to the specified destination."""
    description: NotRequired[str]
    r"""The description of the route. This description is shown in the reports."""
    destination: NotRequired[PaymentCreateRouteDestinationTypedDict]
    r"""The destination of the route."""


class PaymentCreateRouteRequestBody(BaseModel):
    amount: Optional[PaymentCreateRouteAmount] = None
    r"""The amount of the route. That amount that will be routed to the specified destination."""

    description: Optional[str] = None
    r"""The description of the route. This description is shown in the reports."""

    destination: Optional[PaymentCreateRouteDestination] = None
    r"""The destination of the route."""


class PaymentCreateRouteRequestTypedDict(TypedDict):
    payment_id: str
    r"""Provide the ID of the related payment."""
    request_body: NotRequired[PaymentCreateRouteRequestBodyTypedDict]


class PaymentCreateRouteRequest(BaseModel):
    payment_id: Annotated[
        str,
        pydantic.Field(alias="paymentId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Provide the ID of the related payment."""

    request_body: Annotated[
        Optional[PaymentCreateRouteRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class PaymentCreateRouteDelayedRoutingDocumentationTypedDict(TypedDict):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str
    type: str


class PaymentCreateRouteDelayedRoutingDocumentation(BaseModel):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str

    type: str


class PaymentCreateRouteDelayedRoutingLinksTypedDict(TypedDict):
    documentation: PaymentCreateRouteDelayedRoutingDocumentationTypedDict
    r"""The URL to the generic Mollie API error handling guide."""


class PaymentCreateRouteDelayedRoutingLinks(BaseModel):
    documentation: PaymentCreateRouteDelayedRoutingDocumentation
    r"""The URL to the generic Mollie API error handling guide."""


class PaymentCreateRouteDelayedRoutingResponseBodyData(BaseModel):
    status: int
    r"""The status code of the error message. This is always the same code as the status code of the HTTP message itself."""

    title: str
    r"""The HTTP reason phrase of the error. For example, for a `404` error, the `title` will be `Not Found`."""

    detail: str
    r"""A detailed human-readable description of the error that occurred."""

    links: Annotated[
        PaymentCreateRouteDelayedRoutingLinks, pydantic.Field(alias="_links")
    ]

    field: Optional[str] = None
    r"""If the error was caused by a value provided by you in a specific field, the `field` property will contain the name of the field that caused the issue."""


class PaymentCreateRouteDelayedRoutingResponseBody(ClientError):
    r"""An error response object."""

    data: PaymentCreateRouteDelayedRoutingResponseBodyData

    def __init__(
        self,
        data: PaymentCreateRouteDelayedRoutingResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data


class PaymentCreateRouteDelayedRoutingAmountTypedDict(TypedDict):
    r"""The amount of the route. That amount that will be routed to the specified destination."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class PaymentCreateRouteDelayedRoutingAmount(BaseModel):
    r"""The amount of the route. That amount that will be routed to the specified destination."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class PaymentCreateRouteDelayedRoutingDestinationTypedDict(TypedDict):
    r"""The destination of the route."""

    type: str
    r"""The type of destination. Currently only the destination type `organization` is supported.

    Possible values: `organization`
    """
    organization_id: str
    r"""Required for destination type `organization`. The ID of the connected organization the funds should be routed to."""


class PaymentCreateRouteDelayedRoutingDestination(BaseModel):
    r"""The destination of the route."""

    type: str
    r"""The type of destination. Currently only the destination type `organization` is supported.

    Possible values: `organization`
    """

    organization_id: Annotated[str, pydantic.Field(alias="organizationId")]
    r"""Required for destination type `organization`. The ID of the connected organization the funds should be routed to."""


class PaymentCreateRouteSelfTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class PaymentCreateRouteSelf(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class PaymentCreateRouteDocumentationTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class PaymentCreateRouteDocumentation(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class PaymentCreateRouteLinksTypedDict(TypedDict):
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    self_: PaymentCreateRouteSelfTypedDict
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""
    documentation: PaymentCreateRouteDocumentationTypedDict
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""


class PaymentCreateRouteLinks(BaseModel):
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    self_: Annotated[PaymentCreateRouteSelf, pydantic.Field(alias="self")]
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    documentation: PaymentCreateRouteDocumentation
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""


class PaymentCreateRouteResponseBodyTypedDict(TypedDict):
    r"""The route object."""

    id: str
    r"""The identifier uniquely referring to this route. Mollie assigns this identifier at route creation time. Mollie will always refer to the route by this ID. Example: `crt_dyARQ3JzCgtPDhU2Pbq3J`."""
    payment_id: str
    r"""The unique identifier of the payment. For example: `tr_5B8cwPMGnU6qLbRvo7qEZo`. The full payment object can be retrieved via the payment URL in the `_links` object."""
    amount: PaymentCreateRouteDelayedRoutingAmountTypedDict
    r"""The amount of the route. That amount that will be routed to the specified destination."""
    description: str
    r"""The description of the route. This description is shown in the reports."""
    destination: PaymentCreateRouteDelayedRoutingDestinationTypedDict
    r"""The destination of the route."""
    links: PaymentCreateRouteLinksTypedDict
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""
    resource: NotRequired[str]
    r"""Indicates the response contains a route object. Will always contain the string `route` for this endpoint."""


class PaymentCreateRouteResponseBody(BaseModel):
    r"""The route object."""

    id: str
    r"""The identifier uniquely referring to this route. Mollie assigns this identifier at route creation time. Mollie will always refer to the route by this ID. Example: `crt_dyARQ3JzCgtPDhU2Pbq3J`."""

    payment_id: Annotated[str, pydantic.Field(alias="paymentId")]
    r"""The unique identifier of the payment. For example: `tr_5B8cwPMGnU6qLbRvo7qEZo`. The full payment object can be retrieved via the payment URL in the `_links` object."""

    amount: PaymentCreateRouteDelayedRoutingAmount
    r"""The amount of the route. That amount that will be routed to the specified destination."""

    description: str
    r"""The description of the route. This description is shown in the reports."""

    destination: PaymentCreateRouteDelayedRoutingDestination
    r"""The destination of the route."""

    links: Annotated[PaymentCreateRouteLinks, pydantic.Field(alias="_links")]
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    resource: Optional[str] = "route"
    r"""Indicates the response contains a route object. Will always contain the string `route` for this endpoint."""
