from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.common_v38_0.common import (
    AccountingRemark,
    AgencyContactInfo,
    AgentIdoverride,
    BillingPointOfSaleInfo,
    BookingTraveler,
    CommissionRemark,
    ConsolidatorRemark,
    ContinuityCheckOverride,
    CustomerId,
    EmailNotification,
    FileFinishingInfo,
    FormOfPayment,
    GeneralRemark,
    InvoiceRemark,
    LinkedUniversalRecord,
    NextResultReference,
    Osi,
    OverridePcc,
    PassiveInfo,
    Postscript,
    QueuePlace,
    ResponseMessage,
    Ssr,
    UnassociatedRemark,
    Xmlremark,
    TypeErrorInfo,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class TypeLoggingLevel(Enum):
    """
    The type of various Logging levels.
    """
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


@dataclass
class BaseCoreReq:
    """
    :ivar billing_point_of_sale_info:
    :ivar agent_idoverride:
    :ivar terminal_session_info:
    :ivar trace_id: Unique identifier for this atomic transaction traced
        by the user. Use is optional.
    :ivar token_id: Authentication Token ID used when running in
        statefull operation. Obtained from the LoginRsp. Use is
        optional.
    :ivar authorized_by: Used in showing who authorized the request. Use
        is optional.
    :ivar target_branch: Used for Emulation - If authorised will execute
        the request as if the agent's parent branch is the TargetBranch
        specified.
    :ivar override_logging: Use to override the default logging level
    :ivar language_code: ISO 639 two-character language codes are used
        to retrieve specific information in the requested language. For
        Rich Content and Branding, language codes ZH-HANT (Chinese
        Traditional), ZH-HANS (Chinese Simplified), FR-CA (French
        Canadian) and PT-BR (Portuguese Brazil) can also be used. For
        RCH, language codes ENGB, ENUS, DEDE, DECH can also be used.
        Only certain services support this attribute. Providers: ACH,
        RCH, 1G, 1V, 1P, 1J.
    """
    billing_point_of_sale_info: Optional[BillingPointOfSaleInfo] = field(
        default=None,
        metadata={
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "required": True,
        }
    )
    agent_idoverride: List[AgentIdoverride] = field(
        default_factory=list,
        metadata={
            "name": "AgentIDOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    terminal_session_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminalSessionInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    trace_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
        }
    )
    token_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TokenId",
            "type": "Attribute",
        }
    )
    authorized_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthorizedBy",
            "type": "Attribute",
        }
    )
    target_branch: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetBranch",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    override_logging: Optional[TypeLoggingLevel] = field(
        default=None,
        metadata={
            "name": "OverrideLogging",
            "type": "Attribute",
        }
    )
    language_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Attribute",
        }
    )


@dataclass
class BaseRsp:
    """
    The base type for all responses.

    :ivar response_message:
    :ivar trace_id: Unique identifier for this atomic transaction traced
        by the user. Use is optional.
    :ivar transaction_id: System generated unique identifier for this
        atomic transaction.
    :ivar response_time: The time (in ms) the system spent processing
        this request, not including transmission times.
    :ivar command_history: HTTP link to download command history and
        debugging information of the request that generated this
        response. Must be enabled on the system.
    """
    response_message: List[ResponseMessage] = field(
        default_factory=list,
        metadata={
            "name": "ResponseMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    trace_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TraceId",
            "type": "Attribute",
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Attribute",
        }
    )
    response_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "ResponseTime",
            "type": "Attribute",
        }
    )
    command_history: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommandHistory",
            "type": "Attribute",
        }
    )


@dataclass
class ErrorInfo(TypeErrorInfo):
    """
    Container for error data when there is an application error.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class BaseCoreSearchReq(BaseCoreReq):
    """
    Base Request for Air Search.
    """
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BaseReq(BaseCoreReq):
    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    retrieve_provider_reservation_details: bool = field(
        default=False,
        metadata={
            "name": "RetrieveProviderReservationDetails",
            "type": "Attribute",
        }
    )


@dataclass
class BaseSearchRsp(BaseRsp):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BaseCreateReservationReq(BaseReq):
    """
    :ivar linked_universal_record:
    :ivar booking_traveler:
    :ivar osi:
    :ivar accounting_remark:
    :ivar general_remark:
    :ivar xmlremark:
    :ivar unassociated_remark:
    :ivar postscript:
    :ivar passive_info:
    :ivar continuity_check_override: This element will be used if user
        wants to override segment continuity check.
    :ivar agency_contact_info:
    :ivar customer_id:
    :ivar file_finishing_info:
    :ivar commission_remark:
    :ivar consolidator_remark:
    :ivar invoice_remark:
    :ivar ssr: SSR element outside Booking Traveler without any Segment
        Ref or Booking Traveler Ref.
    :ivar email_notification:
    :ivar queue_place: Allow queue placement of a PNR at the time of
        booking in
        AirCreateReservationReq,HotelCreateReservationReq,PassiveCreateReservationReq
        and VehicleCreateReservationReq for providers 1G,1V,1P and 1J.
    :ivar rule_name: This attribute is meant to attach a mandatory
        custom check rule name to a PNR. A non-mandatory custom check
        rule too can be attached to a PNR.
    :ivar universal_record_locator_code: Which UniversalRecord should
        this new reservation be applied to.  If blank, then a new one is
        created.
    :ivar provider_locator_code: Which Provider reservation does this
        reservation get added to.
    :ivar provider_code: To be used with ProviderLocatorCode, which host
        the reservation being added to belongs to.
    :ivar customer_number: Optional client centric customer identifier
    :ivar version:
    """
    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    postscript: Optional[Postscript] = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    passive_info: Optional[PassiveInfo] = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    continuity_check_override: Optional[ContinuityCheckOverride] = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    agency_contact_info: Optional[AgencyContactInfo] = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    customer_id: Optional[CustomerId] = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    commission_remark: Optional[CommissionRemark] = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    consolidator_remark: Optional[ConsolidatorRemark] = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
    email_notification: Optional[EmailNotification] = field(
        default=None,
        metadata={
            "name": "EmailNotification",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    queue_place: Optional[QueuePlace] = field(
        default=None,
        metadata={
            "name": "QueuePlace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    rule_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        }
    )
    customer_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        }
    )


@dataclass
class BaseSearchReq(BaseReq):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )


@dataclass
class BaseCreateWithFormOfPaymentReq(BaseCreateReservationReq):
    """
    Container for BaseCreateReservation along with Form Of Payment.

    :ivar form_of_payment: Provider:1G,1V,1P,1J,ACH,SDK.
    """
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        }
    )
