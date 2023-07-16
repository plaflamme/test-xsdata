from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.common_v52_0.common import (
    ContinuityCheckOverride,
    FormOfPayment,
    HostTokenList,
    Mco,
    Payment,
    SearchPassenger,
)
from generated.common_v52_0.common_req_rsp import (
    BaseCreateWithFormOfPaymentReq,
    BaseReq,
    BaseRsp,
)
from generated.rail_v52_0.rail import (
    Coach,
    RailAutoSeatAssignment,
    RailExchangeSolution,
    RailFareIdlist,
    RailFareList,
    RailFareNoteList,
    RailInfo,
    RailJourneyList,
    RailPricingModifiers,
    RailPricingSolution,
    RailRefundInfo,
    RailSearchModifiers,
    RailSegmentList,
    SearchRailLeg,
    TypeResponseType,
)
from generated.universal_v52_0.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class RailRefundReqRefundOption(Enum):
    RETAIN = "Retain"
    REFUND = "Refund"


@dataclass
class RailAvailabilitySearchReq(BaseReq):
    """
    Queries the host for availability.

    :ivar search_rail_leg:
    :ivar search_passenger: Maxinumber of passenger increased in to 18
        to support 9 INF passenger along with 9 ADT,CHD,INS
        passenger
    :ivar rail_search_modifiers:
    :ivar rail_pricing_modifiers:
    :ivar host_token_list:
    :ivar response_type: Indicates the type of information to be
        returned in RailShopAPIResponse.  Values are “Schedules” or
        “Availability” or “Fares”.  If not sent, “Fares” will be mapped
        if the request is for a specific rail segments, otherwise
        “Availability” will be mapped.”
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    search_rail_leg: List[SearchRailLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchRailLeg",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 18,
        }
    )
    rail_search_modifiers: Optional[RailSearchModifiers] = field(
        default=None,
        metadata={
            "name": "RailSearchModifiers",
            "type": "Element",
        }
    )
    rail_pricing_modifiers: Optional[RailPricingModifiers] = field(
        default=None,
        metadata={
            "name": "RailPricingModifiers",
            "type": "Element",
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    response_type: Optional[TypeResponseType] = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        }
    )


@dataclass
class RailAvailabilitySearchRsp(BaseRsp):
    """
    Returns the result of an availability search on host.

    :ivar rail_segment_list:
    :ivar rail_journey_list:
    :ivar rail_pricing_solution:
    :ivar rail_fare_note_list:
    :ivar rail_fare_idlist:
    :ivar rail_fare_list:
    :ivar host_token_list:
    :ivar response_type: Indicates the type of information returned in
        RailShopAPIResponse(Schedules/Availability).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment_list: Optional[RailSegmentList] = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
        }
    )
    rail_journey_list: Optional[RailJourneyList] = field(
        default=None,
        metadata={
            "name": "RailJourneyList",
            "type": "Element",
        }
    )
    rail_pricing_solution: List[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_note_list: Optional[RailFareNoteList] = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    rail_fare_idlist: Optional[RailFareIdlist] = field(
        default=None,
        metadata={
            "name": "RailFareIDList",
            "type": "Element",
        }
    )
    rail_fare_list: Optional[RailFareList] = field(
        default=None,
        metadata={
            "name": "RailFareList",
            "type": "Element",
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    response_type: Optional[TypeResponseType] = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        }
    )


@dataclass
class RailExchangeQuoteReq(BaseReq):
    """
    Queries the host for availability.

    :ivar search_rail_leg:
    :ivar rail_search_modifiers:
    :ivar search_passenger: Maxinumber of passenger increased in to 18
        to support 9 INF passenger along with 9 ADT,CHD,INS
        passenger
    :ivar host_token_list:
    :ivar rail_pricing_solution:
    :ivar rail_fare_note_list: List of RailFareNote(s) that is
        referenced by key in RailFare.
    :ivar locator_code: The unique identifier for this rail reservation
    :ivar response_type: Indicates the type of information to be
        returned in RailShopModifyAPIResponse.  Values are “Schedules”
        or “Availability” or “Fares”.  If not sent, “Fares” will be
        mapped if the request is for a specific rail segments, otherwise
        “Availability” will be mapped. Provider Supported RCH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    search_rail_leg: List[SearchRailLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchRailLeg",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    rail_search_modifiers: Optional[RailSearchModifiers] = field(
        default=None,
        metadata={
            "name": "RailSearchModifiers",
            "type": "Element",
        }
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 18,
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rail_pricing_solution: Optional[RailPricingSolution] = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
        }
    )
    rail_fare_note_list: Optional[RailFareNoteList] = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    response_type: Optional[TypeResponseType] = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        }
    )


@dataclass
class RailExchangeQuoteRsp(BaseRsp):
    """
    Returns the result of an availability search on host.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment_list: Optional[RailSegmentList] = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
        }
    )
    rail_journey_list: Optional[RailJourneyList] = field(
        default=None,
        metadata={
            "name": "RailJourneyList",
            "type": "Element",
        }
    )
    rail_exchange_solution: List[RailExchangeSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailExchangeSolution",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_note_list: Optional[RailFareNoteList] = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    rail_fare_idlist: Optional[RailFareIdlist] = field(
        default=None,
        metadata={
            "name": "RailFareIDList",
            "type": "Element",
        }
    )
    rail_fare_list: Optional[RailFareList] = field(
        default=None,
        metadata={
            "name": "RailFareList",
            "type": "Element",
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )


@dataclass
class RailExchangeReq(BaseCreateWithFormOfPaymentReq):
    """
    Creates a rail exchange reservation request with the host.

    :ivar rail_exchange_solution:
    :ivar payment:
    :ivar rail_fare_note_list: List of RailFareNote(s) that is
        referenced by key in RailFare.
    :ivar host_token_list:
    :ivar rail_auto_seat_assignment:
    :ivar locator_code: The unique identifier for this rail reservation
    :ivar booking_action_type: The action associated with this booking.
        Three options are:Final (used to book with no ticket issuance),
        FinalTicket (used to book and issue the ticket), Initiate (used
        for a provisional booking). Provider is RCH
    :ivar refund_option: If the exchange results in money returned to
        the customer, ‘Refund’ is sent to return the money to the
        original form or payment or ‘Retain’ is sent if the money should
        be returned in the form of an eVoucher for future use.  This
        attribute is supported by Amtrak/2V and ignored for all others.”
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_exchange_solution: Optional[RailExchangeSolution] = field(
        default=None,
        metadata={
            "name": "RailExchangeSolution",
            "type": "Element",
        }
    )
    payment: Optional[Payment] = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rail_fare_note_list: Optional[RailFareNoteList] = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rail_auto_seat_assignment: List[RailAutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RailAutoSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_action_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingActionType",
            "type": "Attribute",
            "required": True,
        }
    )
    refund_option: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundOption",
            "type": "Attribute",
        }
    )


@dataclass
class RailRefundQuoteReq(BaseReq):
    """
    Request to quote a refund for an itinerary.

    :ivar locator_code: The unique identifier for this rail reservation
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class RailRefundQuoteRsp(BaseRsp):
    """
    Returns rail refund information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_refund_info: List[RailRefundInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailRefundInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class RailRefundReq(BaseReq):
    """
    Request to cancel the booking.

    :ivar continuity_check_override: This element will be used if user
        wants to override segment continuity check.
    :ivar form_of_payment:
    :ivar locator_code: The unique identifier for this rail reservation
    :ivar refund_option: Customers choice to select the refund amount or
        retain as EVoucher for future use.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    continuity_check_override: Optional[ContinuityCheckOverride] = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    form_of_payment: Optional[FormOfPayment] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    refund_option: Optional[RailRefundReqRefundOption] = field(
        default=None,
        metadata={
            "name": "RefundOption",
            "type": "Attribute",
        }
    )


@dataclass
class RailRefundRsp(BaseRsp):
    """
    Returns rail cancel information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    payment: Optional[Payment] = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    mco: Optional[Mco] = field(
        default=None,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )


@dataclass
class RailSeatMapReq(BaseReq):
    """
    Request a rail seat map/coach map.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_info: Optional[RailInfo] = field(
        default=None,
        metadata={
            "name": "RailInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RailSeatMapRsp(BaseRsp):
    """
    Returns rail seat map/coach map.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    coach: List[Coach] = field(
        default_factory=list,
        metadata={
            "name": "Coach",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class TypeRailReservationRsp(BaseRsp):
    class Meta:
        name = "typeRailReservationRsp"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )


@dataclass
class RailExchangeRsp(TypeRailReservationRsp):
    """
    Returns rail exchange reservation information with ticketing/refund info etc..
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"
