"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from mollie.models import ClientError
from mollie.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from mollie.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class QueryParamEmbed(str, Enum):
    r"""This endpoint allows embedding related API items by appending the following values via the `embed` query string parameter."""

    PAYMENT = "payment"


class ListAllRefundsRequestTypedDict(TypedDict):
    from_: NotRequired[str]
    r"""Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set."""
    limit: NotRequired[Nullable[int]]
    r"""The maximum number of items to return. Defaults to 50 items."""
    sort: NotRequired[Nullable[str]]
    r"""Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from newest to oldest.

    Possible values: `asc` `desc` (default: `desc`)
    """
    embed: NotRequired[QueryParamEmbed]
    r"""This endpoint allows embedding related API items by appending the following values via the `embed` query string parameter."""
    profile_id: NotRequired[str]
    r"""The identifier referring to the [profile](get-profile) you wish to retrieve the resources for.

    Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted. For organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.
    """
    testmode: NotRequired[Nullable[bool]]
    r"""Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.

    Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.
    """


class ListAllRefundsRequest(BaseModel):
    from_: Annotated[
        Optional[str],
        pydantic.Field(alias="from"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the result set."""

    limit: Annotated[
        OptionalNullable[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50
    r"""The maximum number of items to return. Defaults to 50 items."""

    sort: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from newest to oldest.

    Possible values: `asc` `desc` (default: `desc`)
    """

    embed: Annotated[
        Optional[QueryParamEmbed],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""This endpoint allows embedding related API items by appending the following values via the `embed` query string parameter."""

    profile_id: Annotated[
        Optional[str],
        pydantic.Field(alias="profileId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The identifier referring to the [profile](get-profile) you wish to retrieve the resources for.

    Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted. For organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.
    """

    testmode: Annotated[
        OptionalNullable[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by setting the `testmode` query parameter to `true`.

    Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["from", "limit", "sort", "embed", "profileId", "testmode"]
        nullable_fields = ["limit", "sort", "testmode"]
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


class ListAllRefundsRefundsDocumentationTypedDict(TypedDict):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str
    type: str


class ListAllRefundsRefundsDocumentation(BaseModel):
    r"""The URL to the generic Mollie API error handling guide."""

    href: str

    type: str


class ListAllRefundsRefundsLinksTypedDict(TypedDict):
    documentation: ListAllRefundsRefundsDocumentationTypedDict
    r"""The URL to the generic Mollie API error handling guide."""


class ListAllRefundsRefundsLinks(BaseModel):
    documentation: ListAllRefundsRefundsDocumentation
    r"""The URL to the generic Mollie API error handling guide."""


class ListAllRefundsRefundsResponseBodyData(BaseModel):
    status: int
    r"""The status code of the error message. This is always the same code as the status code of the HTTP message itself."""

    title: str
    r"""The HTTP reason phrase of the error. For example, for a `404` error, the `title` will be `Not Found`."""

    detail: str
    r"""A detailed human-readable description of the error that occurred."""

    links: Annotated[ListAllRefundsRefundsLinks, pydantic.Field(alias="_links")]

    field: Optional[str] = None
    r"""If the error was caused by a value provided by you in a specific field, the `field` property will contain the name of the field that caused the issue."""


class ListAllRefundsRefundsResponseBody(ClientError):
    r"""An error response object."""

    data: ListAllRefundsRefundsResponseBodyData

    def __init__(
        self,
        data: ListAllRefundsRefundsResponseBodyData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        self.data = data


class ListAllRefundsAmountTypedDict(TypedDict):
    r"""The amount refunded to your customer with this refund. The amount is allowed to be lower than the original payment amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class ListAllRefundsAmount(BaseModel):
    r"""The amount refunded to your customer with this refund. The amount is allowed to be lower than the original payment amount."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class ListAllRefundsSettlementAmountTypedDict(TypedDict):
    r"""This optional field will contain the approximate amount that will be deducted from your account balance, converted to the currency your account is settled in.

    The amount is a **negative** amount.

    If the refund is not directly processed by Mollie, for example for PayPal refunds, the settlement amount will be zero.

    Since the field contains an estimated amount during refund processing, it may change over time. For example, while the refund is queued the settlement amount is likely not yet available.

    To retrieve accurate settlement amounts we recommend using the [List balance transactions endpoint](list-balance-transactions) instead.
    """

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class ListAllRefundsSettlementAmount(BaseModel):
    r"""This optional field will contain the approximate amount that will be deducted from your account balance, converted to the currency your account is settled in.

    The amount is a **negative** amount.

    If the refund is not directly processed by Mollie, for example for PayPal refunds, the settlement amount will be zero.

    Since the field contains an estimated amount during refund processing, it may change over time. For example, while the refund is queued the settlement amount is likely not yet available.

    To retrieve accurate settlement amounts we recommend using the [List balance transactions endpoint](list-balance-transactions) instead.
    """

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class ListAllRefundsMetadata2TypedDict(TypedDict):
    pass


class ListAllRefundsMetadata2(BaseModel):
    pass


ListAllRefundsMetadataTypedDict = TypeAliasType(
    "ListAllRefundsMetadataTypedDict",
    Union[ListAllRefundsMetadata2TypedDict, str, List[str]],
)
r"""Provide any data you like, for example a string or a JSON object. We will save the data alongside the entity. Whenever you fetch the entity with our API, we will also include the metadata. You can use up to approximately 1kB."""


ListAllRefundsMetadata = TypeAliasType(
    "ListAllRefundsMetadata", Union[ListAllRefundsMetadata2, str, List[str]]
)
r"""Provide any data you like, for example a string or a JSON object. We will save the data alongside the entity. Whenever you fetch the entity with our API, we will also include the metadata. You can use up to approximately 1kB."""


class ListAllRefundsExternalReferenceTypedDict(TypedDict):
    type: NotRequired[str]
    r"""Specifies the reference type

    Possible values: `acquirer-reference`
    """
    id: NotRequired[str]
    r"""Unique reference from the payment provider"""


class ListAllRefundsExternalReference(BaseModel):
    type: Optional[str] = None
    r"""Specifies the reference type

    Possible values: `acquirer-reference`
    """

    id: Optional[str] = None
    r"""Unique reference from the payment provider"""


class ListAllRefundsRefundsAmountTypedDict(TypedDict):
    r"""The amount that will be pulled back."""

    currency: str
    r"""A three-character ISO 4217 currency code."""
    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class ListAllRefundsRefundsAmount(BaseModel):
    r"""The amount that will be pulled back."""

    currency: str
    r"""A three-character ISO 4217 currency code."""

    value: str
    r"""A string containing an exact monetary amount in the given currency."""


class ListAllRefundsSourceTypedDict(TypedDict):
    r"""Where the funds will be pulled back from."""

    organization_id: NotRequired[str]
    r"""Required for source type `organization`. The ID of the connected organization the funds should be pulled back from."""


class ListAllRefundsSource(BaseModel):
    r"""Where the funds will be pulled back from."""

    organization_id: Annotated[
        Optional[str], pydantic.Field(alias="organizationId")
    ] = None
    r"""Required for source type `organization`. The ID of the connected organization the funds should be pulled back from."""


class ListAllRefundsRoutingReversalsTypedDict(TypedDict):
    amount: NotRequired[ListAllRefundsRefundsAmountTypedDict]
    r"""The amount that will be pulled back."""
    source: NotRequired[ListAllRefundsSourceTypedDict]
    r"""Where the funds will be pulled back from."""


class ListAllRefundsRoutingReversals(BaseModel):
    amount: Optional[ListAllRefundsRefundsAmount] = None
    r"""The amount that will be pulled back."""

    source: Optional[ListAllRefundsSource] = None
    r"""Where the funds will be pulled back from."""


class ListAllRefundsRefundsSelfTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsRefundsSelf(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsPaymentTypedDict(TypedDict):
    r"""The API resource URL of the [payment](get-payment) that this refund belongs to."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsPayment(BaseModel):
    r"""The API resource URL of the [payment](get-payment) that this refund belongs to."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsSettlementTypedDict(TypedDict):
    r"""The API resource URL of the [settlement](get-settlement) this refund has been settled with. Not present if not yet settled."""

    href: NotRequired[str]
    r"""The actual URL string."""
    type: NotRequired[str]
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsSettlement(BaseModel):
    r"""The API resource URL of the [settlement](get-settlement) this refund has been settled with. Not present if not yet settled."""

    href: Optional[str] = None
    r"""The actual URL string."""

    type: Optional[str] = None
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsRefundsResponseDocumentationTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsRefundsResponseDocumentation(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsRefundsResponseLinksTypedDict(TypedDict):
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    self_: NotRequired[ListAllRefundsRefundsSelfTypedDict]
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""
    payment: NotRequired[ListAllRefundsPaymentTypedDict]
    r"""The API resource URL of the [payment](get-payment) that this refund belongs to."""
    settlement: NotRequired[Nullable[ListAllRefundsSettlementTypedDict]]
    r"""The API resource URL of the [settlement](get-settlement) this refund has been settled with. Not present if not yet settled."""
    documentation: NotRequired[ListAllRefundsRefundsResponseDocumentationTypedDict]
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""


class ListAllRefundsRefundsResponseLinks(BaseModel):
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    self_: Annotated[
        Optional[ListAllRefundsRefundsSelf], pydantic.Field(alias="self")
    ] = None
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    payment: Optional[ListAllRefundsPayment] = None
    r"""The API resource URL of the [payment](get-payment) that this refund belongs to."""

    settlement: OptionalNullable[ListAllRefundsSettlement] = UNSET
    r"""The API resource URL of the [settlement](get-settlement) this refund has been settled with. Not present if not yet settled."""

    documentation: Optional[ListAllRefundsRefundsResponseDocumentation] = None
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["self", "payment", "settlement", "documentation"]
        nullable_fields = ["settlement"]
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


class ListAllRefundsRefundsTypedDict(TypedDict):
    resource: NotRequired[str]
    r"""Indicates the response contains a refund object. Will always contain the string `refund` for this endpoint."""
    id: NotRequired[str]
    r"""The identifier uniquely referring to this refund. Mollie assigns this identifier at refund creation time. Mollie will always refer to the refund by this ID. Example: `re_4qqhO89gsT`."""
    mode: NotRequired[str]
    r"""Whether this entity was created in live mode or in test mode.

    Possible values: `live` `test`
    """
    description: NotRequired[str]
    r"""The description of the refund that may be shown to your customer, depending on the payment method used."""
    amount: NotRequired[ListAllRefundsAmountTypedDict]
    r"""The amount refunded to your customer with this refund. The amount is allowed to be lower than the original payment amount."""
    settlement_amount: NotRequired[Nullable[ListAllRefundsSettlementAmountTypedDict]]
    r"""This optional field will contain the approximate amount that will be deducted from your account balance, converted to the currency your account is settled in.

    The amount is a **negative** amount.

    If the refund is not directly processed by Mollie, for example for PayPal refunds, the settlement amount will be zero.

    Since the field contains an estimated amount during refund processing, it may change over time. For example, while the refund is queued the settlement amount is likely not yet available.

    To retrieve accurate settlement amounts we recommend using the [List balance transactions endpoint](list-balance-transactions) instead.
    """
    metadata: NotRequired[Nullable[ListAllRefundsMetadataTypedDict]]
    r"""Provide any data you like, for example a string or a JSON object. We will save the data alongside the entity. Whenever you fetch the entity with our API, we will also include the metadata. You can use up to approximately 1kB."""
    payment_id: NotRequired[str]
    r"""The unique identifier of the payment this refund was created for. The full payment object can be retrieved via the payment URL in the `_links` object."""
    settlement_id: NotRequired[Nullable[str]]
    r"""The identifier referring to the settlement this refund was settled with. This field is omitted if the refund is not settled (yet)."""
    status: NotRequired[str]
    r"""Refunds may take some time to get confirmed.

    Possible values: `queued` `pending` `processing` `refunded` `failed` `canceled`
    """
    created_at: NotRequired[str]
    r"""The entity's date and time of creation, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format."""
    external_reference: NotRequired[ListAllRefundsExternalReferenceTypedDict]
    routing_reversals: NotRequired[
        Nullable[List[ListAllRefundsRoutingReversalsTypedDict]]
    ]
    r"""*This feature is only available to marketplace operators.*

    When creating refunds for *routed* payments, by default the full amount is deducted from your balance.

    If you want to pull back funds from the connected merchant(s), you can use this parameter to specify what amount needs to be reversed from which merchant(s).

    If you simply want to fully reverse the routed funds, you can also use the `reverseRouting` parameter instead.
    """
    links: NotRequired[ListAllRefundsRefundsResponseLinksTypedDict]
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""


class ListAllRefundsRefunds(BaseModel):
    resource: Optional[str] = "refund"
    r"""Indicates the response contains a refund object. Will always contain the string `refund` for this endpoint."""

    id: Optional[str] = None
    r"""The identifier uniquely referring to this refund. Mollie assigns this identifier at refund creation time. Mollie will always refer to the refund by this ID. Example: `re_4qqhO89gsT`."""

    mode: Optional[str] = None
    r"""Whether this entity was created in live mode or in test mode.

    Possible values: `live` `test`
    """

    description: Optional[str] = None
    r"""The description of the refund that may be shown to your customer, depending on the payment method used."""

    amount: Optional[ListAllRefundsAmount] = None
    r"""The amount refunded to your customer with this refund. The amount is allowed to be lower than the original payment amount."""

    settlement_amount: Annotated[
        OptionalNullable[ListAllRefundsSettlementAmount],
        pydantic.Field(alias="settlementAmount"),
    ] = UNSET
    r"""This optional field will contain the approximate amount that will be deducted from your account balance, converted to the currency your account is settled in.

    The amount is a **negative** amount.

    If the refund is not directly processed by Mollie, for example for PayPal refunds, the settlement amount will be zero.

    Since the field contains an estimated amount during refund processing, it may change over time. For example, while the refund is queued the settlement amount is likely not yet available.

    To retrieve accurate settlement amounts we recommend using the [List balance transactions endpoint](list-balance-transactions) instead.
    """

    metadata: OptionalNullable[ListAllRefundsMetadata] = UNSET
    r"""Provide any data you like, for example a string or a JSON object. We will save the data alongside the entity. Whenever you fetch the entity with our API, we will also include the metadata. You can use up to approximately 1kB."""

    payment_id: Annotated[Optional[str], pydantic.Field(alias="paymentId")] = None
    r"""The unique identifier of the payment this refund was created for. The full payment object can be retrieved via the payment URL in the `_links` object."""

    settlement_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="settlementId")
    ] = UNSET
    r"""The identifier referring to the settlement this refund was settled with. This field is omitted if the refund is not settled (yet)."""

    status: Optional[str] = None
    r"""Refunds may take some time to get confirmed.

    Possible values: `queued` `pending` `processing` `refunded` `failed` `canceled`
    """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None
    r"""The entity's date and time of creation, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format."""

    external_reference: Annotated[
        Optional[ListAllRefundsExternalReference],
        pydantic.Field(alias="externalReference"),
    ] = None

    routing_reversals: Annotated[
        OptionalNullable[List[ListAllRefundsRoutingReversals]],
        pydantic.Field(alias="routingReversals"),
    ] = UNSET
    r"""*This feature is only available to marketplace operators.*

    When creating refunds for *routed* payments, by default the full amount is deducted from your balance.

    If you want to pull back funds from the connected merchant(s), you can use this parameter to specify what amount needs to be reversed from which merchant(s).

    If you simply want to fully reverse the routed funds, you can also use the `reverseRouting` parameter instead.
    """

    links: Annotated[
        Optional[ListAllRefundsRefundsResponseLinks], pydantic.Field(alias="_links")
    ] = None
    r"""An object with several relevant URLs. Every URL object will contain an `href` and a `type` field."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "resource",
            "id",
            "mode",
            "description",
            "amount",
            "settlementAmount",
            "metadata",
            "paymentId",
            "settlementId",
            "status",
            "createdAt",
            "externalReference",
            "routingReversals",
            "_links",
        ]
        nullable_fields = [
            "settlementAmount",
            "metadata",
            "settlementId",
            "routingReversals",
        ]
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


class ListAllRefundsEmbeddedTypedDict(TypedDict):
    refunds: NotRequired[List[ListAllRefundsRefundsTypedDict]]
    r"""An array of refund objects. For a complete reference of the refund object, refer to the [Get refund endpoint](get-refund) documentation."""


class ListAllRefundsEmbedded(BaseModel):
    refunds: Optional[List[ListAllRefundsRefunds]] = None
    r"""An array of refund objects. For a complete reference of the refund object, refer to the [Get refund endpoint](get-refund) documentation."""


class ListAllRefundsSelfTypedDict(TypedDict):
    r"""The URL to the current set of items."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsSelf(BaseModel):
    r"""The URL to the current set of items."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsPreviousTypedDict(TypedDict):
    r"""The previous set of items, if available."""

    href: NotRequired[str]
    r"""The actual URL string."""
    type: NotRequired[str]
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsPrevious(BaseModel):
    r"""The previous set of items, if available."""

    href: Optional[str] = None
    r"""The actual URL string."""

    type: Optional[str] = None
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsNextTypedDict(TypedDict):
    r"""The next set of items, if available."""

    href: NotRequired[str]
    r"""The actual URL string."""
    type: NotRequired[str]
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsNext(BaseModel):
    r"""The next set of items, if available."""

    href: Optional[str] = None
    r"""The actual URL string."""

    type: Optional[str] = None
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsDocumentationTypedDict(TypedDict):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""
    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsDocumentation(BaseModel):
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    href: str
    r"""The actual URL string."""

    type: str
    r"""The content type of the page or endpoint the URL points to."""


class ListAllRefundsLinksTypedDict(TypedDict):
    r"""Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field."""

    self_: NotRequired[ListAllRefundsSelfTypedDict]
    r"""The URL to the current set of items."""
    previous: NotRequired[Nullable[ListAllRefundsPreviousTypedDict]]
    r"""The previous set of items, if available."""
    next: NotRequired[Nullable[ListAllRefundsNextTypedDict]]
    r"""The next set of items, if available."""
    documentation: NotRequired[ListAllRefundsDocumentationTypedDict]
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""


class ListAllRefundsLinks(BaseModel):
    r"""Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field."""

    self_: Annotated[Optional[ListAllRefundsSelf], pydantic.Field(alias="self")] = None
    r"""The URL to the current set of items."""

    previous: OptionalNullable[ListAllRefundsPrevious] = UNSET
    r"""The previous set of items, if available."""

    next: OptionalNullable[ListAllRefundsNext] = UNSET
    r"""The next set of items, if available."""

    documentation: Optional[ListAllRefundsDocumentation] = None
    r"""In v2 endpoints, URLs are commonly represented as objects with an `href` and `type` field."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["self", "previous", "next", "documentation"]
        nullable_fields = ["previous", "next"]
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


class ListAllRefundsResponseBodyTypedDict(TypedDict):
    r"""A list of refund objects. For a complete reference of the refund object, refer to the [Get refund endpoint](get-refund) documentation."""

    count: NotRequired[int]
    r"""The number of items in this result set. If more items are available, a `_links.next` URL will be present in the result as well.

    The maximum number of items per result set is controlled by the `limit` property provided in the request. The default limit is 50 items.
    """
    embedded: NotRequired[ListAllRefundsEmbeddedTypedDict]
    links: NotRequired[ListAllRefundsLinksTypedDict]
    r"""Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field."""


class ListAllRefundsResponseBody(BaseModel):
    r"""A list of refund objects. For a complete reference of the refund object, refer to the [Get refund endpoint](get-refund) documentation."""

    count: Optional[int] = None
    r"""The number of items in this result set. If more items are available, a `_links.next` URL will be present in the result as well.

    The maximum number of items per result set is controlled by the `limit` property provided in the request. The default limit is 50 items.
    """

    embedded: Annotated[
        Optional[ListAllRefundsEmbedded], pydantic.Field(alias="_embedded")
    ] = None

    links: Annotated[Optional[ListAllRefundsLinks], pydantic.Field(alias="_links")] = (
        None
    )
    r"""Links to help navigate through the lists of items. Every URL object will contain an `href` and a `type` field."""
