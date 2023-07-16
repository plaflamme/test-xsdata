from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.air_v52_0.air import (
    AirExchangeBundle,
    AirExchangeBundleTotal,
    AirPricingSolution,
    AirSegmentSellFailureInfo,
    Etr,
    OriginalItineraryDetails,
    RepricingModifiers,
    TypeFailureInfo,
)
from generated.common_v52_0.common import (
    AddSvc,
    HostToken,
    QueueSelector,
)
from generated.common_v52_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)
from generated.shared_booking_v52_0.shared_booking import (
    AddAirPnrElement,
    AddAirSegment,
    AddHotelPnrElement,
    AddHotelSegment,
    AddPnrElement,
    AddPricing,
    AddSeats,
    AddTraveler,
    CommandResponse,
    DeleteAirPnrElement,
    DeleteAirSegment,
    DeleteHotelPnrElement,
    DeleteHotelSegment,
    DeletePnrElement,
    DeletePricing,
    DeleteSeats,
    DeleteTraveler,
    UpdateAirPnrElement,
    UpdateAirSegment,
    UpdateHotelPnrElement,
    UpdatePnrElement,
    UpdateSeats,
    UpdateTraveler,
)
from generated.universal_v52_0.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


class BookingEndReqSessionActivity(Enum):
    END = "End"
    END_QUEUE = "EndQueue"
    IGNORE = "Ignore"


@dataclass
class BookingBaseReq(BaseReq):
    """
    Context for Requests.

    :ivar session_key: System generated session token. Token contains
        the session information of the user. User must supply this in
        the resquest to use the current session they are working on.
    """
    session_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "SessionKey",
            "type": "Attribute",
        }
    )


@dataclass
class BookingBaseRsp(BaseRsp):
    """
    Context for Responses.

    :ivar universal_record:
    :ivar session_key: Session Token that was used to do the transaction
        echoed back.
    """
    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    session_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "SessionKey",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BookingStartReq(BaseReq):
    """
    Used to start session.

    :ivar provider_code: Provider with which session needs to be
        started.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

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
class BookingAirExchangeQuoteReq(BookingBaseReq):
    """
    Quotes the new exchange based on the new segments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
            "min_length": 1,
            "max_length": 13,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    repricing_modifiers: List[RepricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        }
    )


@dataclass
class BookingAirExchangeQuoteRsp(BookingBaseRsp):
    """
    :ivar ticket_number:
    :ivar air_pricing_solution: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle_total:
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P
    :ivar host_token: Encrypted data from the host. Required to send the
        HostToken from the AirExchangeQuoteRsp in the AirExchangeReq.
        Providers ACH/1G/1V/1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
            "min_length": 1,
            "max_length": 13,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )


@dataclass
class BookingAirExchangeReq(BookingBaseReq):
    """
    Performs exchange on existing reservations.

    :ivar air_reservation_locator_code: Identifies the PNR locator code.
        Providers 1G/1V/1P
    :ivar ticket_number:
    :ivar air_pricing_solution: Providers ACH/1G/1V/1P.
    :ivar air_exchange_bundle_total: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P.
    :ivar host_token: Encrypted data from the host. Required to send the
        HostToken from the AirExchangeQuoteRsp in the AirExchangeReq.
        Providers ACH/1G/1V/1P
    :ivar add_svc: 1P - Add SVC segments to collect additional fee
    :ivar override_warnings: Set to true will allow multiple end
        transact attempts. Set to false only one end transact is done
        and warnings are returned for follow up action. Supported
        Providers: 1G/1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 13,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 99,
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    add_svc: Optional[AddSvc] = field(
        default=None,
        metadata={
            "name": "AddSvc",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    override_warnings: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OverrideWarnings",
            "type": "Attribute",
        }
    )


@dataclass
class BookingAirExchangeRsp(BookingBaseRsp):
    """
    Returns exchanged itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirPnrElementReq(BookingBaseReq):
    """
    Adds, Modifies air elements like Stored fare FOP, Credit Card Auth, Ticketing
    Modifiers etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_air_pnr_element: Optional[AddAirPnrElement] = field(
        default=None,
        metadata={
            "name": "AddAirPnrElement",
            "type": "Element",
        }
    )
    update_air_pnr_element: Optional[UpdateAirPnrElement] = field(
        default=None,
        metadata={
            "name": "UpdateAirPnrElement",
            "type": "Element",
        }
    )
    delete_air_pnr_element: Optional[DeleteAirPnrElement] = field(
        default=None,
        metadata={
            "name": "DeleteAirPnrElement",
            "type": "Element",
        }
    )


@dataclass
class BookingAirPnrElementRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirSegmentReq(BookingBaseReq):
    """
    Used for Air Segment Sell and modification.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_air_segment: Optional[AddAirSegment] = field(
        default=None,
        metadata={
            "name": "AddAirSegment",
            "type": "Element",
        }
    )
    update_air_segment: Optional[UpdateAirSegment] = field(
        default=None,
        metadata={
            "name": "UpdateAirSegment",
            "type": "Element",
        }
    )
    delete_air_segment: Optional[DeleteAirSegment] = field(
        default=None,
        metadata={
            "name": "DeleteAirSegment",
            "type": "Element",
        }
    )


@dataclass
class BookingAirSegmentRsp(BookingBaseRsp):
    """
    Returns sold segments and sell messages.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment_sell_failure_info: Optional[AirSegmentSellFailureInfo] = field(
        default=None,
        metadata={
            "name": "AirSegmentSellFailureInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )


@dataclass
class BookingDisplayReq(BookingBaseReq):
    """
    Retrieves the current contents of data in session , or PNR if it is specified.

    :ivar provider_reservation_info: Bring an existent PNR in session to
        work on it.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    provider_reservation_info: Optional["BookingDisplayReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
        }
    )

    @dataclass
    class ProviderReservationInfo:
        """
        :ivar provider_code:
        :ivar provider_locator_code:
        :ivar supplier_code: Represents Carrier Code for ACH PNR
            Retrieve.
        """
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
        supplier_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 5,
            }
        )


@dataclass
class BookingDisplayRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingEndReq(BookingBaseReq):
    """Ends the session.

    Will end transact the booking on the host and create a UR, or will
    ignore the current activity.

    :ivar session_activity: Current values supported are  Ignore, End
        and EndQueue (QueueNumber must follow)
    :ivar queue_selector:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    session_activity: Optional[BookingEndReqSessionActivity] = field(
        default=None,
        metadata={
            "name": "SessionActivity",
            "type": "Element",
            "required": True,
        }
    )
    queue_selector: List[QueueSelector] = field(
        default_factory=list,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 4,
        }
    )


@dataclass
class BookingEndRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingHotelPnrElementReq(BookingBaseReq):
    """
    Adds, Modifies hotel elements like Guarantee, BookingSource, etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_hotel_pnr_element: Optional[AddHotelPnrElement] = field(
        default=None,
        metadata={
            "name": "AddHotelPnrElement",
            "type": "Element",
        }
    )
    update_hotel_pnr_element: Optional[UpdateHotelPnrElement] = field(
        default=None,
        metadata={
            "name": "UpdateHotelPnrElement",
            "type": "Element",
        }
    )
    delete_hotel_pnr_element: Optional[DeleteHotelPnrElement] = field(
        default=None,
        metadata={
            "name": "DeleteHotelPnrElement",
            "type": "Element",
        }
    )


@dataclass
class BookingHotelPnrElementRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingHotelSegmentReq(BookingBaseReq):
    """
    Used for Hotel Segment Sell and modification.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_hotel_segment: Optional[AddHotelSegment] = field(
        default=None,
        metadata={
            "name": "AddHotelSegment",
            "type": "Element",
        }
    )
    delete_hotel_segment: Optional[DeleteHotelSegment] = field(
        default=None,
        metadata={
            "name": "DeleteHotelSegment",
            "type": "Element",
        }
    )


@dataclass
class BookingHotelSegmentRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingPnrElementReq(BookingBaseReq):
    """
    Adds, Modifies PNR elemnts like OSI, FOP, review booking, remarks, and action
    status.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_pnr_element: Optional[AddPnrElement] = field(
        default=None,
        metadata={
            "name": "AddPnrElement",
            "type": "Element",
        }
    )
    update_pnr_element: Optional[UpdatePnrElement] = field(
        default=None,
        metadata={
            "name": "UpdatePnrElement",
            "type": "Element",
        }
    )
    delete_pnr_element: Optional[DeletePnrElement] = field(
        default=None,
        metadata={
            "name": "DeletePnrElement",
            "type": "Element",
        }
    )


@dataclass
class BookingPnrElementRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingPricingReq(BookingBaseReq):
    """
    Stores/Modifies pricing.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_pricing: Optional[AddPricing] = field(
        default=None,
        metadata={
            "name": "AddPricing",
            "type": "Element",
        }
    )
    delete_pricing: Optional[DeletePricing] = field(
        default=None,
        metadata={
            "name": "DeletePricing",
            "type": "Element",
        }
    )


@dataclass
class BookingPricingRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingRetrieveDocumentReq(BookingBaseReq):
    """
    Used view Ticket Details of the PNR.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P.
    :ivar ticket_number: Provider: 1G,1V,1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
            "min_length": 1,
            "max_length": 13,
        }
    )


@dataclass
class BookingRetrieveDocumentRsp(BookingBaseRsp):
    """
    :ivar etr: Provider: 1G,1V,1P.
    :ivar document_failure_info: Provider: 1G,1V,1P -Will be optionally
        returned if there are duplicate ticket numbers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    document_failure_info: List[TypeFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "DocumentFailureInfo",
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class BookingSeatAssignmentReq(BookingBaseReq):
    """
    Used to request auto or specific seat assignments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_seats: Optional[AddSeats] = field(
        default=None,
        metadata={
            "name": "AddSeats",
            "type": "Element",
        }
    )
    update_seats: Optional[UpdateSeats] = field(
        default=None,
        metadata={
            "name": "UpdateSeats",
            "type": "Element",
        }
    )
    delete_seats: Optional[DeleteSeats] = field(
        default=None,
        metadata={
            "name": "DeleteSeats",
            "type": "Element",
        }
    )


@dataclass
class BookingSeatAssignmentRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingStartRsp(BookingBaseRsp):
    """Returns the session key.

    User must use the session key in the subsequent transactions to use
    the created session.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingTerminalReq(BookingBaseReq):
    """
    Allow terminal commands to be run in the session.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    command: Optional[str] = field(
        default=None,
        metadata={
            "name": "Command",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BookingTerminalRsp(BookingBaseRsp):
    """
    Returns the terminal response and UR with the changes based on the Terminal
    Req.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    command_response: Optional[CommandResponse] = field(
        default=None,
        metadata={
            "name": "CommandResponse",
            "type": "Element",
        }
    )


@dataclass
class BookingTravelerReq(BookingBaseReq):
    """
    Used to add update delete booking traveler and its contents.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_traveler: Optional[AddTraveler] = field(
        default=None,
        metadata={
            "name": "AddTraveler",
            "type": "Element",
        }
    )
    update_traveler: Optional[UpdateTraveler] = field(
        default=None,
        metadata={
            "name": "UpdateTraveler",
            "type": "Element",
        }
    )
    delete_traveler: Optional[DeleteTraveler] = field(
        default=None,
        metadata={
            "name": "DeleteTraveler",
            "type": "Element",
        }
    )


@dataclass
class BookingTravelerRsp(BookingBaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"
