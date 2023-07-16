from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from generated.common_v52_0.common import (
    NextResultReference,
    QueueSelector,
)
from generated.common_v52_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)
from generated.universal_v52_0.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class DateRangeInfo:
    """
    The information related to date range .

    :ivar date_range: Date range number where the PNR should be queued.
        Possible values are 1,2,1-4 etc.
    :ivar title: Title of a date range.
    :ivar count: The PNR count of date range.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    date_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PseudoCityCode:
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )


@dataclass
class QueueAgentRecord:
    """
    The information related to a particular category.

    :ivar universal_record_locator_code:
    :ivar pseudo_city_code:
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    :ivar queue_number:
    :ivar lastupdated:
    :ivar target_branch:
    :ivar category: Queue Category Number. 2 Character Alpha or Numeric
        Number. Either Alpha or Numeric Number is allowed.
    :ivar date_range: Date range number where the PNR should be queued.
        Possible values are 1,2,1-4 etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
            "required": True,
        }
    )
    queue_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    lastupdated: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lastupdated",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    target_branch: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetBranch",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    date_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
        }
    )


@dataclass
class QueueElement:
    """
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar departure_date:
    :ivar queue_date: Denotes the GDS formatted Date a PNR is placed in
        queue.
    :ivar queue_time: Time a PNR placed in queue.
    :ivar name: Name as in queue
    :ivar universal_record_locator_code: Present if there is an
        associated UR
    :ivar created_by_agent_code: Agent who created UR - Present if there
        is an associated UR
    :ivar modified_by_agent_code: Agent who modified UR - Present if
        there is an associated UR with modifications
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    queue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueDate",
            "type": "Attribute",
        }
    )
    queue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "QueueTime",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
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
    created_by_agent_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedByAgentCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )
    modified_by_agent_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedByAgentCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )


@dataclass
class QueueSelectorType:
    """
    :ivar queue: Queue Number . Possible values are 01, AA , A1 etc.
    :ivar category: Queue Category Number. 2 Character Alpha or Numeric
        Number. Either Alpha or Numeric Number is allowed. If using for
        Sabre is mandatory and is Prefatory Instruction Code value of
        0-999.
    :ivar date_range: Date range number where the PNR should be queued.
        Possible values are 1,2,1-4 etc.
    :ivar surname: Surname as in queue ,supports alpha characters only.
    """
    queue: Optional[str] = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    date_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
        }
    )


@dataclass
class CategoryInfo:
    """
    The information related to a particular category.

    :ivar date_range_info:
    :ivar title: Title of a particular category.
    :ivar category: Queue Category Number. 2 Character Alpha or Numeric
        Number. Either Alpha or Numeric Number is allowed.
    :ivar count: The PNR count of a particular category.
    :ivar total_count: The PNR count of a all categories.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    date_range_info: List[DateRangeInfo] = field(
        default_factory=list,
        metadata={
            "name": "DateRangeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        }
    )
    total_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCount",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GdsEnterQueueReq(BaseReq):
    """
    Use this request to enter a GDS queue.

    :ivar queue_selector:
    :ivar pseudo_city_code:
    :ivar provider_code: The IATA assigned airline/GDS code.
    :ivar provider_locator_code: If providerLocatorCode is not specified
        then the first PNR on the Queue will be retrieved.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: Optional[QueueSelector] = field(
        default=None,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
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


@dataclass
class GdsEnterQueueRsp(BaseRsp):
    """
    The response containing the Universal Record.

    :ivar universal_record: Refers to the Universal Record , system
        would automatically import a PNR if it doesn't exist in the
        sytem otherwise will display existing Universal Record.
    :ivar title: Title of the queue.
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )


@dataclass
class GdsExitQueueRsp(BaseRsp):
    """
    An empty response indicates success.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsNextOnQueueRsp(BaseRsp):
    """
    The response from the host for a NextOnQueueReq.

    :ivar universal_record: Refers to the Universal Record , system
        would automatically import a PNR if it doesn't exist exist in
        the sytem otherwise would display existing Universal Record.
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )


@dataclass
class GdsQueueAgentListReq(BaseReq):
    """
    Use this request to list items stuck on the Queue.

    :ivar agent_id: The Agent ID for the applicable supplier/vendor
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    agent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class GdsQueueAgentListRsp(BaseRsp):
    """
    Use this request to list items stuck on the Queue.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_agent_record: List[QueueAgentRecord] = field(
        default_factory=list,
        metadata={
            "name": "QueueAgentRecord",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class GdsQueueListReq(BaseReq):
    """
    Use this request to list the pnrs on a queue.

    :ivar next_result_reference: Container to send reference to
        additional queue list results (Providers: 1P) Error returned,
        "NextResultReference is not supported by the Provider."
        (Providers: 1V, 1G)
    :ivar gds_queue_selector:
    :ivar provider_code: The IATA assigned airline/GDS code.
    :ivar pseudo_city_code:
    :ivar retrieve_all: Set to true to retrieve all PNRs ,if not set or
        set to false system would display PNRs as returned from GDS .
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    next_result_reference: Optional[NextResultReference] = field(
        default=None,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    gds_queue_selector: Optional[QueueSelectorType] = field(
        default=None,
        metadata={
            "name": "GdsQueueSelector",
            "type": "Element",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    retrieve_all: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RetrieveAll",
            "type": "Attribute",
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )


@dataclass
class GdsQueueListRsp(BaseRsp):
    """
    The response from the host for a queue list.

    :ivar next_result_reference: Container to return reference to
        additional queue list results (Providers: 1P)
    :ivar queue_element:
    :ivar more_pnrexists: This is an indicator which indicates there are
        more PNRs in queue than what is returned. If true means more
        PNRs exist in the Queue. If false or not present means all PNRs
        are already returned in response from the queue.
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    next_result_reference: Optional[NextResultReference] = field(
        default=None,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    queue_element: List[QueueElement] = field(
        default_factory=list,
        metadata={
            "name": "QueueElement",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    more_pnrexists: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MorePNRExists",
            "type": "Attribute",
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )


@dataclass
class GdsQueuePlaceReq(BaseReq):
    """
    Use this request to place a UR on a queue.

    :ivar queue_selector: Identifies the Queue Information to be
        selected for placing the UR An UR can be placed into multiple
        Queues
    :ivar pseudo_city_code: Input PCC optional value for placing the UR
        into Queue
    :ivar provider_code:
    :ivar provider_locator_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: List[QueueSelector] = field(
        default_factory=list,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )


@dataclass
class GdsQueuePlaceRsp(BaseRsp):
    """
    An empty response indicates success.

    :ivar universal_record: The Queue Place Response will return the UR
        Record
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )


@dataclass
class GdsQueueRemoveReq(BaseReq):
    """
    Use this request to Clear a GDS queue.

    :ivar queue_selector:
    :ivar queue_session_token: Host session Token
    :ivar pseudo_city_code:
    :ivar provider_code:
    :ivar provider_locator_code: ProviderLocatorCode of the PNR to be
        removed from the Queue
    :ivar remove_duplicates: Remove duplicate PNRs from queues. Provider
        Supported 1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: Optional[QueueSelector] = field(
        default=None,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
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
    remove_duplicates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RemoveDuplicates",
            "type": "Attribute",
        }
    )


@dataclass
class GdsQueueRemoveRsp(BaseRsp):
    """
    An empty response indicates success.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class QueuePseudoCitySelector:
    """
    Need to specify the PseudoCityCode and Queue details.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: Optional[QueueSelector] = field(
        default=None,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )


@dataclass
class GdsExitQueueReq(BaseReq):
    """
    Use this request to close a session you no longer need.

    :ivar queue_pseudo_city_selector: Target Queue where the current PNR
        needs to be placed. Supported Providers: Worldspan
    :ivar remove_current: If specified and set to true, the pnr
        currently in context will be removed, if set to false then the
        current PNR will be placed back on the Queue.
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    :ivar provider_code: The IATA assigned airline/GDS code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_pseudo_city_selector: Optional[QueuePseudoCitySelector] = field(
        default=None,
        metadata={
            "name": "QueuePseudoCitySelector",
            "type": "Element",
        }
    )
    remove_current: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RemoveCurrent",
            "type": "Attribute",
            "required": True,
        }
    )
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class GdsNextOnQueueReq(BaseReq):
    """
    Use this request to get the 'next' pnr on queue.

    :ivar queue_pseudo_city_selector: Target Queue where the current PNR
        needs to be placed. Supported Providers: Worldspan
    :ivar remove_current: If specified and set to true, the pnr
        currently in context will be removed, if set to false then the
        current PNR will be placed back on the Queue.
    :ivar provider_locator_code: If providerLocatorCode is not specified
        then the next PNR on the Queue will be retrieved.
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    :ivar queue_continue: Should be used only when the bottom of the
        queue has been reached. If set to true, will get the PNR from
        the top of the queue. Applicable Provider: Worldspan
    :ivar provider_code: The IATA assigned airline/GDS code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_pseudo_city_selector: Optional[QueuePseudoCitySelector] = field(
        default=None,
        metadata={
            "name": "QueuePseudoCitySelector",
            "type": "Element",
        }
    )
    remove_current: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RemoveCurrent",
            "type": "Attribute",
            "required": True,
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
    queue_session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        }
    )
    queue_continue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "QueueContinue",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class GdsQueueCountReq(BaseReq):
    """Use this request to get the number of pnrs on a queue.

    If no queue is given, all queues for the pcc will be returned If no
    pseudocitycode is

    :ivar queue_pseudo_city_selector:
    :ivar provider_code: The IATA assigned airline/GDS code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_pseudo_city_selector: List[QueuePseudoCitySelector] = field(
        default_factory=list,
        metadata={
            "name": "QueuePseudoCitySelector",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )


@dataclass
class QueueInfo:
    """
    :ivar category_info:
    :ivar queue:
    :ivar pseudo_city_code:
    :ivar total_pnrcount:
    :ivar pnrcount:
    :ivar title: Title of a queue.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    category_info: List[CategoryInfo] = field(
        default_factory=list,
        metadata={
            "name": "CategoryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    queue: Optional[str] = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
            "required": True,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    total_pnrcount: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalPNRCount",
            "type": "Attribute",
            "required": True,
        }
    )
    pnrcount: Optional[int] = field(
        default=None,
        metadata={
            "name": "PNRCount",
            "type": "Attribute",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
        }
    )


@dataclass
class GdsQueueCountRsp(BaseRsp):
    """
    The response from the host for a queue count.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_info: List[QueueInfo] = field(
        default_factory=list,
        metadata={
            "name": "QueueInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
