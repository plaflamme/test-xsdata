from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.uprofile_common_v30_0.uprofile_common import (
    AgentIdoverride,
    BillingPointOfSaleInfo,
    NextResultReference,
    OverridePcc,
    ResponseMessage,
    TypeErrorInfo,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


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


class TypeParentProfileLevel(Enum):
    """Returns parent’s data up to specified hierarchy.

    Valid values are ‘Agency’, ‘AgencyGroup’, ‘BranchGroup’, ‘Branch’,
    ‘Account’ and ‘Traveler Group’.
    """
    AGENCY_GROUP = "AgencyGroup"
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"


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
    :ivar language_code: ISO  639 Language Code used to receive specific
        information in the requested  language. Supported  Provider:
        ACH. Supported Carriers:U2
    """
    billing_point_of_sale_info: Optional[BillingPointOfSaleInfo] = field(
        default=None,
        metadata={
            "name": "BillingPointOfSaleInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
            "required": True,
        }
    )
    agent_idoverride: List[AgentIdoverride] = field(
        default_factory=list,
        metadata={
            "name": "AgentIDOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        }
    )
    terminal_session_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminalSessionInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
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
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
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
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"


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
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        }
    )


@dataclass
class BaseReq(BaseCoreReq):
    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
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
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        }
    )


@dataclass
class BaseSearchReq(BaseReq):
    next_result_reference: List[NextResultReference] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        }
    )
