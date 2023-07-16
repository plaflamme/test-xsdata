from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime
from generated.air_v52_0.air import (
    AirPricingAdjustment,
    AirPricingInfo,
    AirPricingModifiers,
    AirPricingPayment,
    AirPricingSolution,
    AirPricingTicketingModifiers,
    AirReservation,
    AirSegment,
    AirSegmentError,
    AirSegmentPricingModifiers,
    AirSegmentSellFailureInfo,
    AssociatedRemark as AirAirAssociatedRemark,
    AutoSeatAssignment,
    BrandInfo,
    EmdsummaryInfo,
    FeeInfo,
    InvoluntaryChange,
    OptionalServicesInfo,
    PocketItineraryRemark,
    SpecificSeatAssignment,
)
from generated.common_v52_0.common import (
    AccountingRemark,
    ActionStatus,
    AgencyContactInfo,
    AgencyInfo,
    AppliedProfile,
    BookingSource,
    BookingTraveler,
    BookingTravelerInfo,
    CommissionRemark,
    ConsolidatorRemark,
    CorporateDiscountId,
    CreditCardAuth,
    CustomerId,
    DeliveryInfo,
    DriversLicense,
    FormOfPayment,
    GeneralRemark,
    Group,
    Guarantee,
    HostToken,
    InvoiceData,
    InvoiceRemark,
    LinkedUniversalRecord,
    LoyaltyCard,
    Name,
    Osi,
    OwnershipChange,
    Payment,
    PointOfSale,
    Postscript,
    ProviderArnksegment,
    ReservationName,
    ReviewBooking,
    Ssr,
    SearchPassenger,
    ServiceFeeInfo,
    SpecialEquipment,
    SupplierLocator,
    ThirdPartyInformation,
    TravelComplianceData,
    UrticketStatus,
    UnassociatedRemark,
    VendorLocation,
    Xmlremark,
    TypeDateRange,
    TypeElement,
    TypeElementStatus,
    TypeErrorInfo,
    TypeProduct,
    TypeRecordStatus,
    TypeResultMessage,
)
from generated.cruise_v52_0.cruise import CruiseReservation
from generated.hotel_v52_0.hotel import (
    AssociatedRemark as HotelHotelAssociatedRemark,
    GuestInformation,
    HotelBedding,
    HotelDetailsModifiers,
    HotelProperty,
    HotelRateDetail,
    HotelRateInfo,
    HotelReservation,
    HotelRulesModifiers,
    HotelStay,
    PromotionCode,
)
from generated.passive_v52_0.passive import (
    AssociatedRemark as PassivePassiveAssociatedRemark,
    PassiveRemark,
    PassiveReservation,
    PassiveSegment,
)
from generated.rail_v52_0.rail import (
    RailFareNote,
    RailPricingSolution,
    RailReservation,
)
from generated.vehicle_v52_0.vehicle import (
    AssociatedRemark as VehicleVehicleAssociatedRemark,
    CollectionAddress,
    DeliveryAddress,
    FlightArrivalInformation,
    PaymentInformation,
    Vehicle,
    VehicleDateLocation,
    VehiclePickupDateLocation,
    VehicleRateInfo,
    VehicleReservation,
    VehicleReturnDateLocation,
    VehicleSearchModifiers,
    VehicleSpecialRequest,
    VehicleTypeIdentifier,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class AirSegmentSpecialUpdateAction(Enum):
    APPROVE_SCHEDULE_CHANGE = "ApproveScheduleChange"
    APPROVE_SCHEDULE_CHANGE_OVERRIDE_MCT = "ApproveScheduleChangeOverrideMCT"


@dataclass
class AppliedProfileCriteria:
    """
    Traveler Applied Profile Id for Searching misc traveler information.

    :ivar traveler_profile_id: Search with Traveler Applied Profile Id
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    traveler_profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelerProfileId",
            "type": "Attribute",
        }
    )


@dataclass
class ArvlUnknSegment:
    """
    An ARNK segment that identifies a missing travel information.

    :ivar booking_traveler_ref: Reference Element for Booking Traveler
    :ivar key:
    :ivar origin: The IATA CITY code for this origination of this
        entity.
    :ivar destination: The IATA CITY code for this destination of this
        entity.
    :ivar travel_order: To identify the appropriate travel sequence for
        Air/Car/Hotel segments/reservations based on travel dates. This
        ordering is applicable across the UR not provider or traveler
        specific
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler_ref: List["ArvlUnknSegment.BookingTravelerRef"] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 255,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    travel_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        }
    )

    @dataclass
    class BookingTravelerRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class BranchId:
    """
    Branch ID to restrict search.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ContinuityOverrideRemark:
    """A textual remark container to hold any printable text.

    (max 512 chars)

    :ivar value:
    :ivar category: This is remark category is always MCT. 'Minimum
        Connect Time'
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    category: str = field(
        default="MCT",
        metadata={
            "name": "Category",
            "type": "Attribute",
            "max_length": 10,
        }
    )


@dataclass
class DisplayContents:
    """
    Display the contents in GDS format.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class NameCriteria:
    """
    Traveler First Name and Last Name for Searching misc traveler information.

    :ivar first_name: Search with Traveler First Name
    :ivar last_name: Search with Traveler Last Name
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )


class PreferenceOwner(Enum):
    TRAVELER = "Traveler"
    ACCOUNT = "Account"
    AGENT = "Agent"
    BRANCH = "Branch"
    AGENCY = "Agency"


@dataclass
class ProfileAssociation:
    """
    Profile information associated with SavedTrip.

    :ivar traveler_id: Traveler ID associated with saved Trip.
    :ivar booking_traveler_ref: Booking Traveler associated with
        Profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    traveler_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProviderReservationDetails:
    """
    Indicates the type of content in PNR,to retrieve the display only content use
    ProviderReservationDisplayDetailsReq.

    :ivar provider_reservation_detail: Provider Reservation data exists.
    :ivar custom_check: Custom check data exists.
    :ivar provider_profile: Provider Profile data exists.
    :ivar divide_details: Divide Details data exists.
    :ivar enhanced_itin_modifiers: Enhanced itinerary modifiers data
        exists
    :ivar integrated_content: Integrated content data exists
    :ivar cruise: Cruise data exists.
    :ivar rail_segment: Rail Segment data exists.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    provider_reservation_detail: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetail",
            "type": "Attribute",
        }
    )
    custom_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CustomCheck",
            "type": "Attribute",
        }
    )
    provider_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProviderProfile",
            "type": "Attribute",
        }
    )
    divide_details: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DivideDetails",
            "type": "Attribute",
        }
    )
    enhanced_itin_modifiers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnhancedItinModifiers",
            "type": "Attribute",
        }
    )
    integrated_content: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntegratedContent",
            "type": "Attribute",
        }
    )
    cruise: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cruise",
            "type": "Attribute",
        }
    )
    rail_segment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RailSegment",
            "type": "Attribute",
        }
    )


@dataclass
class ProviderReservationSearchModifiers:
    """
    Controls and switches for the PNR Search request.

    :ivar include_all_names: If true, include all the passenger names in
        the results. Otherwise include only the name of the primary
        passenger.
    :ivar include_agent_info: Include information about the agent who
        created, modified or ticketed the PNR.
    :ivar max_results:
    :ivar start_from_result:
    :ivar exclude_air: Exclude Air reservations from the results
    :ivar exclude_vehicle: Exclude Vehicle reservations from the results
    :ivar exclude_hotel: Exclude Hotel reservations from the results
    :ivar exclude_ground: Exclude Ground reservations from the results
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    include_all_names: bool = field(
        default=False,
        metadata={
            "name": "IncludeAllNames",
            "type": "Attribute",
        }
    )
    include_agent_info: bool = field(
        default=False,
        metadata={
            "name": "IncludeAgentInfo",
            "type": "Attribute",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    start_from_result: int = field(
        default=1,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    exclude_air: bool = field(
        default=False,
        metadata={
            "name": "ExcludeAir",
            "type": "Attribute",
        }
    )
    exclude_vehicle: bool = field(
        default=False,
        metadata={
            "name": "ExcludeVehicle",
            "type": "Attribute",
        }
    )
    exclude_hotel: bool = field(
        default=False,
        metadata={
            "name": "ExcludeHotel",
            "type": "Attribute",
        }
    )
    exclude_ground: bool = field(
        default=False,
        metadata={
            "name": "ExcludeGround",
            "type": "Attribute",
        }
    )


@dataclass
class QueueNextModifiers:
    """
    Can only be used when modifying an Universal Record in Queue mode.If not
    specified along with ReturnRecord as false then current PNR in queue context
    will be removed.

    :ivar next_on_queue: Set to true to retrieve the next PNR on Queue
        ,if not set or set to false system would return the current
        PNR.NextOnQueue cannot be combined with Provider Locator Code
        and ReturnRecord as true
    :ivar provider_locator_code: If providerLocatorCode is specified
        then system would return the specified locator code in Queue
        mode .Provider Locator Code cannot be combined with NextOnQueue
        and ReturnRecord as true
    :ivar re_queue_current: Set to true to place the current PNR back on
        Queue
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    next_on_queue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NextOnQueue",
            "type": "Attribute",
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
    re_queue_current: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReQueueCurrent",
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
class RecordIdentifier:
    """
    The information that uniquly identifies a particular supplier reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )


class SavedTripActivityType(Enum):
    LOW_FARE_SEARCH = "LowFareSearch"
    AIR_PRICE = "AirPrice"
    VEHICLE_SEARCH_AVAILABILITY = "VehicleSearchAvailability"
    VEHICLE_BOOK = "VehicleBook"
    HOTEL_DETAILS_SEARCH = "HotelDetailsSearch"
    HOTEL_RULES_SEARCH = "HotelRulesSearch"
    HOTEL_SEARCH = "HotelSearch"


@dataclass
class SearchAccount:
    """
    Search restriction by Account.

    :ivar client_id: Identifier of the corporation this account is for.
    :ivar branch_id: Account Branch ID.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    client_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClientID",
            "type": "Attribute",
        }
    )
    branch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )


@dataclass
class SearchAgent:
    """
    Search restriction by Agent.

    :ivar branch_id:
    :ivar created_by_agent: The Agent ID that created a PNR.
    :ivar modified_by_agent: The Agent ID that modified a PNR last.
    :ivar ticketed_by_agent: The Agent ID that ticketed a PNR.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    branch_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BranchId",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    created_by_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedByAgent",
            "type": "Attribute",
        }
    )
    modified_by_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedByAgent",
            "type": "Attribute",
        }
    )
    ticketed_by_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketedByAgent",
            "type": "Attribute",
        }
    )


@dataclass
class SupportedVersions:
    """
    SOAP Header element that determines what version a particular request supports.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    ur_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "urVersion",
            "type": "Attribute",
        }
    )
    air_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "airVersion",
            "type": "Attribute",
        }
    )
    hotel_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "hotelVersion",
            "type": "Attribute",
        }
    )
    vehicle_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleVersion",
            "type": "Attribute",
        }
    )
    passive_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "passiveVersion",
            "type": "Attribute",
        }
    )
    rail_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "railVersion",
            "type": "Attribute",
        }
    )
    cruise_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "cruiseVersion",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalModifyCommandError:
    """
    Container to return modify command failures.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    universal_modify_cmd_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalModifyCmdKey",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class UniversalRecordHistorySearchModifiers:
    """
    Controls and switches for the Universal Record history request.

    :ivar element_type: The Type of History that is to be searched for.
    :ivar modified_date: Only search for modifications that occured on
        that date.
    :ivar modified_range: Only search for modifications that occured
        between the two dates (inclusive).
    :ivar max_results:
    :ivar start_from_result:
    :ivar modified_by: Agent code that modified the Universal Record
    :ivar debug_mode: Returns Debug info. Travelport Internal Usage
        Only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    element_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementType",
            "type": "Element",
        }
    )
    modified_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Element",
        }
    )
    modified_range: Optional["UniversalRecordHistorySearchModifiers.ModifiedRange"] = field(
        default=None,
        metadata={
            "name": "ModifiedRange",
            "type": "Element",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    start_from_result: int = field(
        default=1,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    modified_by: Optional[object] = field(
        default=None,
        metadata={
            "name": "ModifiedBy",
            "type": "Attribute",
        }
    )
    debug_mode: bool = field(
        default=False,
        metadata={
            "name": "DebugMode",
            "type": "Attribute",
        }
    )

    @dataclass
    class ModifiedRange:
        modified_start: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "ModifiedStart",
                "type": "Element",
                "required": True,
            }
        )
        modified_end: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "ModifiedEnd",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class UniversalRecordHistorySearchResult:
    """
    Container for Universal Record history result.

    :ivar old: Representation of the element before the modification
        took place.
    :ivar new: Representation of the element after the modification took
        place.
    :ivar modified_by: The agent or entity that performed the
        modification
    :ivar modified_date: When the Universal Record was modified.
    :ivar element_type: The type of element that was added or deleted
    :ivar action: The action that was taken on the defined element
    :ivar transaction_id: System generated unique identifier for this
        atomic transaction. Travelport Internal Usage Only.
    :ivar agent_override: AgentSine value that was used during PNR
        creation or End Transact.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    old: Optional[str] = field(
        default=None,
        metadata={
            "name": "Old",
            "type": "Element",
        }
    )
    new: Optional[str] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
        }
    )
    modified_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedBy",
            "type": "Attribute",
        }
    )
    modified_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    element_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementType",
            "type": "Attribute",
            "required": True,
        }
    )
    action: Optional[str] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Attribute",
        }
    )
    agent_override: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentOverride",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


class UniversalUpdateStatus(Enum):
    ARCHIVED = "Archived"
    RETAINED = "Retained"


class TypeDisplayDetailName(Enum):
    """
    :cvar OWNING_AGENCY_PCC: The pseudo city code of the agency owning
        the PNR
    :cvar CREATING_AGENT_SIGN_ON: Sign on code of the agent created the
        PNR
    :cvar CREATING_AGENT_DUTY: Duty code of the agent created the PNR
    :cvar CREATING_AGENCY_IATA: IATA number of the agency  created the
        PNR
    :cvar PREPAID_TICKET_ADVICE_INDICATOR: Indicates whether Prepaid
        Ticket Advice is attached to PNR
    :cvar BFBORROWED: Indicates the current PNR as borrowed
    :cvar GLOBAL_PNR: Indicates whether current PNR is Global PNR
    :cvar READ_ONLY_PNR: Indicates PNR as read only
    :cvar PAST_DATE_QUICK_RETRIEVED_PNR: Indicates PNR retrieved from
        offline archival process
    :cvar SUPER_PNR: Indicates whether current PNR is Super PNR
    :cvar PNRPURGE_DATE: Purge date of the PNR
    :cvar ORIGINAL_RECEIVED_FIELD_VALUE: The original data in the
        received field
    :cvar DIV_PSGR_NAME: Passenger Name in a divided PNR
    :cvar TRUNC_IND: Indicator for Truncated names
    :cvar DIV_TYPE_IND: Divide Type Indicator if it pertains to child or
        parent booking
    :cvar RLOC: Record Locator of parent or child booking
    :cvar DIV_DT: Date of divide action
    :cvar DIV_TM: Time of day of divide action
    :cvar TRAVEL_ORDER: Travel order of the segment
    :cvar SEGMENT_STATUS: Status of associated segment
    :cvar START_DATE: Date of departure of the rail segment
    :cvar DAY_CHANGE: Indicates arrival date as number of days before or
        after departure date
    :cvar VENDOR: Vendor code of the segment
    :cvar START_TIME: Start Time of the segment
    :cvar END_TIME: End Time of the segment
    :cvar BOOKING_CODE: The booking code of the rail segment seating
        area
    :cvar TRAIN_NUMBER: Denotes Train number
    :cvar NUMBER_OF_SEATS: Number of seats sold for the trip
    :cvar SELL_TYPE: The mode of selling the segment
    :cvar TARIFF_TYPE: Type of Tariff for the segment
    :cvar CONFIRMATION_NUMBER: The confirmation number of the segment
    :cvar BOARDING_INFORMATION: Information related to boarding point of
        the segment
    :cvar ARRIVAL_INFORMATION: Information related to arrival point of
        the segment
    :cvar TEXT: Additional   information
    """
    OWNING_AGENCY_PCC = "OwningAgencyPCC"
    CREATING_AGENT_SIGN_ON = "CreatingAgentSignOn"
    CREATING_AGENT_DUTY = "CreatingAgentDuty"
    CREATING_AGENCY_IATA = "CreatingAgencyIATA"
    PREPAID_TICKET_ADVICE_INDICATOR = "PrepaidTicketAdviceIndicator"
    BFBORROWED = "BFBorrowed"
    GLOBAL_PNR = "GlobalPNR"
    READ_ONLY_PNR = "ReadOnlyPNR"
    PAST_DATE_QUICK_RETRIEVED_PNR = "PastDateQuickRetrievedPNR"
    SUPER_PNR = "SuperPNR"
    PNRPURGE_DATE = "PNRPurgeDate"
    ORIGINAL_RECEIVED_FIELD_VALUE = "OriginalReceivedFieldValue"
    DIV_PSGR_NAME = "DivPsgrName"
    TRUNC_IND = "TruncInd"
    DIV_TYPE_IND = "DivTypeInd"
    RLOC = "RLoc"
    DIV_DT = "DivDt"
    DIV_TM = "DivTm"
    TRAVEL_ORDER = "TravelOrder"
    SEGMENT_STATUS = "SegmentStatus"
    START_DATE = "StartDate"
    DAY_CHANGE = "DayChange"
    VENDOR = "Vendor"
    START_TIME = "StartTime"
    END_TIME = "EndTime"
    BOOKING_CODE = "BookingCode"
    TRAIN_NUMBER = "TrainNumber"
    NUMBER_OF_SEATS = "NumberOfSeats"
    SELL_TYPE = "SellType"
    TARIFF_TYPE = "TariffType"
    CONFIRMATION_NUMBER = "ConfirmationNumber"
    BOARDING_INFORMATION = "BoardingInformation"
    ARRIVAL_INFORMATION = "ArrivalInformation"
    TEXT = "Text"


class TypeReservationTicketed(Enum):
    """
    Information on whether the reservation is ticketed.
    """
    YES = "Yes"
    NO = "No"
    NOT_APPLICABLE = "Not Applicable"


class TypeRetainReservation(Enum):
    """
    Retain the Reservation (do not cancel) in the the event of a schedule or price
    change.
    """
    NONE = "None"
    SCHEDULE = "Schedule"
    PRICE = "Price"
    BOTH = "Both"


@dataclass
class TypeSavedTripNote:
    """
    :ivar text: Custom free Text related to SavedTrip.
    """
    class Meta:
        name = "typeSavedTripNote"

    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "required": True,
            "max_length": 333,
        }
    )


class TypeSavedTripRecordStatus(Enum):
    """
    Specifies the status of the Saved Trip record.
    """
    ALL = "All"
    PAST = "Past"
    CURRENT = "Current"


@dataclass
class AirAdd:
    """
    :ivar accounting_remark:
    :ivar supplier_locator:
    :ivar air_segment:
    :ivar air_pricing_info:
    :ivar credit_card_auth:
    :ivar delivery_info:
    :ivar payment:
    :ivar ssr:
    :ivar loyalty_card:
    :ivar auto_seat_assignment:
    :ivar specific_seat_assignment:
    :ivar general_remark:
    :ivar fee_info:
    :ivar host_token:
    :ivar air_pricing_ticketing_modifiers:
    :ivar optional_services_info:
    :ivar air_pricing_payment:
    :ivar associated_remark:
    :ivar pocket_itinerary_remark:
    :ivar third_party_information:
    :ivar air_segment_pricing_modifiers:
    :ivar travel_compliance_data:
    :ivar brand_info:
    :ivar involuntary_change:
    :ivar reservation_locator_code:
    :ivar booking_traveler_ref:
    :ivar restrict_waitlist: Restrict Update if it sells a Waitlisted
        AirSegment. Provider: 1G,1V,1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    delivery_info: Optional[DeliveryInfo] = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    auto_seat_assignment: Optional[AutoSeatAssignment] = field(
        default=None,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
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
    air_pricing_ticketing_modifiers: List[AirPricingTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingTicketingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    optional_services_info: Optional[OptionalServicesInfo] = field(
        default=None,
        metadata={
            "name": "OptionalServicesInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_pricing_payment: Optional[AirPricingPayment] = field(
        default=None,
        metadata={
            "name": "AirPricingPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    associated_remark: List[AirAirAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    pocket_itinerary_remark: List[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "name": "PocketItineraryRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    brand_info: List[BrandInfo] = field(
        default_factory=list,
        metadata={
            "name": "BrandInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    involuntary_change: Optional[InvoluntaryChange] = field(
        default=None,
        metadata={
            "name": "InvoluntaryChange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    restrict_waitlist: bool = field(
        default=False,
        metadata={
            "name": "RestrictWaitlist",
            "type": "Attribute",
        }
    )


@dataclass
class AirDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    element: Optional[TypeElement] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class AirSegmentSpecialUpdate:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    air_segment: Optional[AirSegment] = field(
        default=None,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    action: Optional[AirSegmentSpecialUpdateAction] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DisplayDetail:
    """Display the contents for requested MCO,Cruise etc.

    details
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name: Optional[TypeDisplayDetailName] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HotelAdd:
    """
    :ivar loyalty_card:
    :ivar guarantee:
    :ivar guest_information:
    :ivar associated_remark:
    :ivar booking_source:
    :ivar hotel_special_request:
    :ivar corporate_discount_id:
    :ivar reservation_name:
    :ivar third_party_information:
    :ivar travel_compliance_data:
    :ivar hotel_bedding: Specify desired optional bed types. Applicable
        for optional bed types:RollawayAdult,RollawayChild,or Crib if
        supported by the hotel supplier. Providers :1G/1V/1P
    :ivar booking_confirmation:
    :ivar reservation_locator_code:
    :ivar booking_traveler_ref: BookingTravelerRef will be used to
        specify BookingTraveler in UR. Currently this will be used to
        LoyaltyCard modification. Later this can used for other elements
        which are associated with BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    guarantee: Optional[Guarantee] = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    guest_information: Optional[GuestInformation] = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    associated_remark: List[HotelHotelAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    booking_source: Optional[BookingSource] = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_special_request: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 250,
        }
    )
    corporate_discount_id: Optional[CorporateDiscountId] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    reservation_name: Optional[ReservationName] = field(
        default=None,
        metadata={
            "name": "ReservationName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    booking_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 32,
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class HotelDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    element: Optional[TypeElement] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class HotelUpdate:
    """
    :ivar loyalty_card:
    :ivar guarantee:
    :ivar guest_information:
    :ivar associated_remark:
    :ivar booking_source:
    :ivar hotel_special_request:
    :ivar hotel_rate_info:
    :ivar hotel_stay:
    :ivar hotel_commission:
    :ivar corporate_discount_id:
    :ivar reservation_name:
    :ivar third_party_information:
    :ivar travel_compliance_data:
    :ivar hotel_bedding: Specify desired optional bed types. Applicable
        for optional bed types:RollawayAdult,RollawayChild,or Crib if
        supported by the hotel supplier. Providers :1G/1V/1P
    :ivar booking_confirmation:
    :ivar reservation_locator_code:
    :ivar booking_traveler_ref: BookingTravelerRef will be used to
        specify BookingTraveler in UR. Currently this will be used to
        LoyaltyCard modification. Later this can used for other elements
        which are associated with BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    guarantee: Optional[Guarantee] = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    guest_information: Optional[GuestInformation] = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    associated_remark: List[HotelHotelAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    booking_source: Optional[BookingSource] = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_special_request: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 250,
        }
    )
    hotel_rate_info: Optional[HotelRateInfo] = field(
        default=None,
        metadata={
            "name": "HotelRateInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    hotel_stay: Optional[HotelStay] = field(
        default=None,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    hotel_commission: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelCommission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    corporate_discount_id: Optional[CorporateDiscountId] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    reservation_name: Optional[ReservationName] = field(
        default=None,
        metadata={
            "name": "ReservationName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    booking_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_length": 32,
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class PassiveAdd:
    """
    :ivar passive_segment: This represents a Passive Segment  of type
        Car,Hotel, Tour,Surface,Air etc.
    :ivar passive_remark: This contains Remark corresponding to any
        PassiveSegment
    :ivar associated_remark: This contains Associated Remark
        corresponding to any PassiveSegment.
    :ivar supplier_locator: SupplierLocator to be added to the host for
        Air Passive.
    :ivar third_party_information:
    :ivar travel_compliance_data:
    :ivar reservation_locator_code: This represents a Passive
        Reservation Locator Code
    :ivar booking_traveler_ref: BookingTravelerRef will be used to
        specify BookingTraveler in UR. Currently this will be used to
        add TravelComplianceData. Later this can used for other elements
        which are associated with BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    passive_segment: List[PassiveSegment] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        }
    )
    passive_remark: List[PassiveRemark] = field(
        default_factory=list,
        metadata={
            "name": "PassiveRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        }
    )
    associated_remark: List[PassivePassiveAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        }
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class PassiveDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    element: Optional[TypeElement] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class Preference:
    """
    Preferences of the segment related to the profile (Agent, Branch, etc.).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    owner: Optional[PreferenceOwner] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProviderReservationStatus:
    """
    Status of the cancellation for this provider reservation.

    :ivar cancel_info: If the provider reservation was not successfully
        cancelled or cancelled with warnings the provider system might
        provides some textual information describing the reason.
    :ivar create_date: The date and time that this reservation was
        created.
    :ivar modified_date: The date and time that this reservation was
        last modified for any reason.
    :ivar provider_code: Contains the Provider Code of the entity
        housing the actual reservation in the event this is a passive
        one.
    :ivar locator_code: Contains the Locator Code of the actual
        reservation in the event this is a passive reservation.
    :ivar cancelled: Will be true if the reservation was successfuly
        cancelled on the provider system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    cancel_info: Optional[TypeResultMessage] = field(
        default=None,
        metadata={
            "name": "CancelInfo",
            "type": "Element",
        }
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
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
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    cancelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancelled",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailUpdate:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_action: Optional["RailUpdate.BookingAction"] = field(
        default=None,
        metadata={
            "name": "BookingAction",
            "type": "Element",
            "required": True,
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )

    @dataclass
    class BookingAction:
        """
        :ivar form_of_payment:
        :ivar payment:
        :ivar type_value: the action associated with this booking. Four
            options are: Final (used to book with no ticket issuance)
            FinalTicket (used to book and issue ticket, default if FOP
            is included) Ticket (used to ticket an existing booking)
        """
        form_of_payment: Optional[FormOfPayment] = field(
            default=None,
            metadata={
                "name": "FormOfPayment",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
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
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SavedTripActivity:
    """
    This element ties together related objects for a saved trip.

    :ivar booking_traveler_ref: Reference to the associated travelers.
    :ivar search_passenger_ref: Reference to the associated travelers.
    :ivar point_of_sale_ref: Reference to the point of sale present in
        the saved trip.
    :ivar accounting_remark_ref: Reference to the AccountingRemark
        present in the saved trip.
    :ivar general_remark_ref: Reference to the GeneralRemark present in
        the saved trip.
    :ivar air_pricing_modifier_ref: Reference to the Air Pricing
        modifier present in the saved trip.
    :ivar air_pricing_solution_ref: Reference to the air pricing
        solution present in the saved trip.
    :ivar vehicle_search_modifiers_ref: Reference to the
        VehicleSearchModifiers present in the saved trip.
    :ivar vehicle_date_location_ref: Reference to the
        VehicleDateLocation present in the saved trip.
    :ivar special_equipment_ref: Reference to the SpecialEquipment
        present in the saved trip.
    :ivar vehicle_special_request_ref: Reference to the
        VehicleSpecialRequest present in the saved trip.
    :ivar payment_information_ref: Reference to the PaymentInformation
        present in the saved trip.
    :ivar delivery_address_ref: Reference to the DeliveryAddress present
        in the saved trip.
    :ivar collection_address_ref: Reference to the CollectionAddress
        present in the saved trip.
    :ivar flight_arrival_information_ref: Reference to the
        FlightArrivalInformation present in the saved trip.
    :ivar vehicle_ref: Reference to the Vehicle present in the saved
        trip.
    :ivar vendor_location_ref: Reference to the VendorLocation present
        in the saved trip.
    :ivar hotel_property_ref: Reference to the HotelProperty present in
        the saved trip.
    :ivar hotel_stay_ref: Reference to the HotelStay present in the
        saved trip.
    :ivar hotel_rules_modifiers_ref: Reference to the
        HotelRulesModifiers present in the saved trip.
    :ivar hotel_details_modifiers_ref: Reference to the
        HotelDetailsModifiers present in the saved trip.
    :ivar hotel_rate_detail_ref: Reference to the HotelRateDetail
        present in the saved trip.
    :ivar promotion_code_ref: Reference to the PromotionCode present in
        the saved trip.
    :ivar rail_pricing_solution_ref: Reference to the rail pricing
        solution present in the saved trip.
    :ivar type_value: Service which is the source for the references
        present in this element.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler_ref: List["SavedTripActivity.BookingTravelerRef"] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_passenger_ref: List["SavedTripActivity.SearchPassengerRef"] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassengerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    point_of_sale_ref: List["SavedTripActivity.PointOfSaleRef"] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSaleRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    accounting_remark_ref: List["SavedTripActivity.AccountingRemarkRef"] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemarkRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    general_remark_ref: List["SavedTripActivity.GeneralRemarkRef"] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemarkRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_modifier_ref: List["SavedTripActivity.AirPricingModifierRef"] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingModifierRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_solution_ref: List["SavedTripActivity.AirPricingSolutionRef"] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolutionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_search_modifiers_ref: List["SavedTripActivity.VehicleSearchModifiersRef"] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSearchModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_date_location_ref: List["SavedTripActivity.VehicleDateLocationRef"] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDateLocationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    special_equipment_ref: List["SavedTripActivity.SpecialEquipmentRef"] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_special_request_ref: List["SavedTripActivity.VehicleSpecialRequestRef"] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSpecialRequestRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    payment_information_ref: List["SavedTripActivity.PaymentInformationRef"] = field(
        default_factory=list,
        metadata={
            "name": "PaymentInformationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    delivery_address_ref: List["SavedTripActivity.DeliveryAddressRef"] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryAddressRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    collection_address_ref: List["SavedTripActivity.CollectionAddressRef"] = field(
        default_factory=list,
        metadata={
            "name": "CollectionAddressRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    flight_arrival_information_ref: List["SavedTripActivity.FlightArrivalInformationRef"] = field(
        default_factory=list,
        metadata={
            "name": "FlightArrivalInformationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_ref: List["SavedTripActivity.VehicleRef"] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vendor_location_ref: List["SavedTripActivity.VendorLocationRef"] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocationRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_property_ref: List["SavedTripActivity.HotelPropertyRef"] = field(
        default_factory=list,
        metadata={
            "name": "HotelPropertyRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_stay_ref: List["SavedTripActivity.HotelStayRef"] = field(
        default_factory=list,
        metadata={
            "name": "HotelStayRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rules_modifiers_ref: List["SavedTripActivity.HotelRulesModifiersRef"] = field(
        default_factory=list,
        metadata={
            "name": "HotelRulesModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_details_modifiers_ref: List["SavedTripActivity.HotelDetailsModifiersRef"] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailsModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rate_detail_ref: List["SavedTripActivity.HotelRateDetailRef"] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetailRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    promotion_code_ref: List["SavedTripActivity.PromotionCodeRef"] = field(
        default_factory=list,
        metadata={
            "name": "PromotionCodeRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_pricing_solution_ref: List["SavedTripActivity.RailPricingSolutionRef"] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolutionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    type_value: Optional[SavedTripActivityType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class BookingTravelerRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SearchPassengerRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PointOfSaleRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AccountingRemarkRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class GeneralRemarkRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AirPricingModifierRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AirPricingSolutionRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleSearchModifiersRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleDateLocationRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SpecialEquipmentRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleSpecialRequestRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PaymentInformationRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DeliveryAddressRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class CollectionAddressRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class FlightArrivalInformationRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VehicleRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class VendorLocationRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelPropertyRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelStayRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelRulesModifiersRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelDetailsModifiersRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class HotelRateDetailRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PromotionCodeRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class RailPricingSolutionRef:
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SegmentContinuityInfo:
    """
    This container holds Arnks and segment continuity remarks.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    arvl_unkn_segment: List[ArvlUnknSegment] = field(
        default_factory=list,
        metadata={
            "name": "ArvlUnknSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    continuity_override_remark: List[ContinuityOverrideRemark] = field(
        default_factory=list,
        metadata={
            "name": "ContinuityOverrideRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    arrival_unknown_segment_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ArrivalUnknownSegmentCount",
            "type": "Attribute",
        }
    )


@dataclass
class TravelerCriteria:
    """
    Criteria for Searching misc traveler information.

    :ivar name_criteria:
    :ivar applied_profile_criteria:
    :ivar phone_number: To Search for Phone Number match
    :ivar viponly: To Search for VIP traveler
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name_criteria: Optional[NameCriteria] = field(
        default=None,
        metadata={
            "name": "NameCriteria",
            "type": "Element",
        }
    )
    applied_profile_criteria: Optional[AppliedProfileCriteria] = field(
        default=None,
        metadata={
            "name": "AppliedProfileCriteria",
            "type": "Element",
        }
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Attribute",
        }
    )
    viponly: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VIPOnly",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalAdd:
    """
    :ivar accounting_remark:
    :ivar general_remark:
    :ivar osi:
    :ivar unassociated_remark:
    :ivar xmlremark:
    :ivar postscript:
    :ivar booking_traveler_info:
    :ivar service_fee_info:
    :ivar linked_universal_record:
    :ivar agency_contact_info:
    :ivar customer_id:
    :ivar commission_remark:
    :ivar consolidator_remark:
    :ivar invoice_remark:
    :ivar action_status:
    :ivar review_booking: Element to add Review booking to a PNR .
    :ivar form_of_payment:
        Provider:1G,1V,1P,ACH,SDK.Product:Air,Hotel,Vehicle,Cruise
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    postscript: Optional[Postscript] = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_traveler_info: Optional[BookingTravelerInfo] = field(
        default=None,
        metadata={
            "name": "BookingTravelerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    agency_contact_info: Optional[AgencyContactInfo] = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    customer_id: Optional[CustomerId] = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    commission_remark: Optional[CommissionRemark] = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    consolidator_remark: Optional[ConsolidatorRemark] = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    action_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    review_booking: List[ReviewBooking] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )


@dataclass
class UniversalDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    element: Optional[TypeElement] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalModifyErrorInfo(TypeErrorInfo):
    """
    Container to return modify command errors.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_modify_command_error: List[UniversalModifyCommandError] = field(
        default_factory=list,
        metadata={
            "name": "UniversalModifyCommandError",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentError",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )


@dataclass
class UniversalModifyFailureInfo:
    """
    Container to return air segment sell failures.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_modify_command_error: List[UniversalModifyCommandError] = field(
        default_factory=list,
        metadata={
            "name": "UniversalModifyCommandError",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_sell_failure_info: Optional[AirSegmentSellFailureInfo] = field(
        default=None,
        metadata={
            "name": "AirSegmentSellFailureInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )


@dataclass
class UniversalUpdate:
    """
    :ivar accounting_remark:
    :ivar general_remark:
    :ivar osi:
    :ivar unassociated_remark:
    :ivar xmlremark:
    :ivar postscript:
    :ivar booking_traveler_info:
    :ivar service_fee_info:
    :ivar status: Flag that determines whether UR and History are
        accessible.
    :ivar agency_contact_info:
    :ivar customer_id:
    :ivar commission_remark:
    :ivar consolidator_remark:
    :ivar invoice_remark:
    :ivar action_status:
    :ivar review_booking: Element to Update an existing Review booking
        of a PNR .
    :ivar ownership_change: Element to change the ownership of the PNR.
        PROVIDER SUPPORTED: Worldspan.
    :ivar form_of_payment: Provider: 1G,1V,1P,ACH,SDK. Product : Air,
        Hotel, Vehicle, Cruise
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    postscript: Optional[Postscript] = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_traveler_info: Optional[BookingTravelerInfo] = field(
        default=None,
        metadata={
            "name": "BookingTravelerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    status: Optional[UniversalUpdateStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    agency_contact_info: Optional[AgencyContactInfo] = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    customer_id: Optional[CustomerId] = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    commission_remark: Optional[CommissionRemark] = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    consolidator_remark: Optional[ConsolidatorRemark] = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    action_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    review_booking: List[ReviewBooking] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    ownership_change: Optional[OwnershipChange] = field(
        default=None,
        metadata={
            "name": "OwnershipChange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleAdd:
    """
    :ivar loyalty_card:
    :ivar drivers_license:
    :ivar vehicle_special_request:
    :ivar special_equipment:
    :ivar payment_information:
    :ivar guarantee:
    :ivar booking_source:
    :ivar associated_remark:
    :ivar delivery_address:
    :ivar collection_address:
    :ivar third_party_information:
    :ivar travel_compliance_data:
    :ivar flight_arrival_information: The flight arrival
        information(airline code and flight number) for the airport/city
        at which the rental car will be picked up || Addition and Update
        in UR Modify is currently implemented only for Galileo(1G) and
        Apollo(1V).
    :ivar reservation_locator_code:
    :ivar booking_traveler_ref: BookingTravelerRef will be used to
        specify BookingTraveler in UR. Currently this will be used to
        LoyaltyCard modification. Later this can used for other elements
        which are associated with BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    drivers_license: Optional[DriversLicense] = field(
        default=None,
        metadata={
            "name": "DriversLicense",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    vehicle_special_request: Optional[VehicleSpecialRequest] = field(
        default=None,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    special_equipment: List[SpecialEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    payment_information: Optional[PaymentInformation] = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    guarantee: Optional[Guarantee] = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_source: Optional[BookingSource] = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    associated_remark: List[VehicleVehicleAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    delivery_address: Optional[DeliveryAddress] = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    collection_address: Optional[CollectionAddress] = field(
        default=None,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    flight_arrival_information: Optional[FlightArrivalInformation] = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    element: Optional[TypeElement] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleUpdate:
    """
    :ivar loyalty_card:
    :ivar drivers_license:
    :ivar guarantee:
    :ivar booking_source:
    :ivar vehicle_rate_info:
    :ivar payment_information:
    :ivar associated_remark:
    :ivar vehicle_special_request:
    :ivar delivery_address:
    :ivar collection_address:
    :ivar vehicle_return_date_location:
    :ivar vehicle_pickup_date_location:
    :ivar third_party_information: Third party supplier locator
        information. Specifically applicable for SDK booking. Previously
        saved values can be updated for SupplierCode, SupplierName and
        SupplierLocatorCode. If an attribute is not passed here, then
        previously saved value for that attribute will be deleted.
    :ivar travel_compliance_data:
    :ivar vehicle_type_identifier:
    :ivar flight_arrival_information: The flight arrival
        information(airline code and flight number) for the airport/city
        at which the rental car will be picked up || Addition and Update
        in UR Modify is currently implemented only for Galileo(1G) and
        Apollo(1V).
    :ivar reservation_locator_code:
    :ivar booking_traveler_ref: BookingTravelerRef will be used to
        specify BookingTraveler in UR. Currently this will be used to
        LoyaltyCard modification. Later this can used for other elements
        which are associated with BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    drivers_license: Optional[DriversLicense] = field(
        default=None,
        metadata={
            "name": "DriversLicense",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    guarantee: Optional[Guarantee] = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_source: Optional[BookingSource] = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    vehicle_rate_info: Optional[VehicleRateInfo] = field(
        default=None,
        metadata={
            "name": "VehicleRateInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    payment_information: Optional[PaymentInformation] = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    associated_remark: List[VehicleVehicleAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_special_request: Optional[VehicleSpecialRequest] = field(
        default=None,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    delivery_address: Optional[DeliveryAddress] = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    collection_address: Optional[CollectionAddress] = field(
        default=None,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle_return_date_location: Optional[VehicleReturnDateLocation] = field(
        default=None,
        metadata={
            "name": "VehicleReturnDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle_pickup_date_location: Optional[VehiclePickupDateLocation] = field(
        default=None,
        metadata={
            "name": "VehiclePickupDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_type_identifier: Optional[VehicleTypeIdentifier] = field(
        default=None,
        metadata={
            "name": "VehicleTypeIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    flight_arrival_information: Optional[FlightArrivalInformation] = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )


@dataclass
class TypeDateSpec:
    """
    Specifies dates as either specific date or a date range.
    """
    class Meta:
        name = "typeDateSpec"

    date_range: Optional[TypeDateRange] = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    specific_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SpecificDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )


@dataclass
class TypeProductInfo:
    """
    Information on the product type and its provider.

    :ivar product_type: The type of product returned
    :ivar vendor_code: The code of the vendor. For Air, Car and Hotel
        this will be an IATA vendor code.
    :ivar provider_code:
    :ivar provider_locator_code:
    """
    class Meta:
        name = "typeProductInfo"

    product_type: Optional[TypeProduct] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Attribute",
            "required": True,
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeSavedTripProductInfo:
    """
    Information on the product type and its provider.

    :ivar product_type: The type of product returned
    :ivar vendor_code: The code of the vendor. For Air, Car and Hotel
        this will be an IATA vendor code.
    :ivar provider_code:
    """
    class Meta:
        name = "typeSavedTripProductInfo"

    product_type: Optional[TypeProduct] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Attribute",
            "required": True,
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirReservationCriteria:
    """
    Criteria for searching the Air reservations.

    :ivar departure_date: Flight Departure Date or Date Range
    :ivar arrival_date: Flight Arrival Date or Date Range
    :ivar origin: The IATA location code for this origination of this
        entity.
    :ivar destination: The IATA location code for this destination of
        this entity.
    :ivar flight_number:
    :ivar carrier:
    :ivar passive_only: Search for Passives Only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    departure_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Element",
        }
    )
    arrival_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "ArrivalDate",
            "type": "Element",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        }
    )


@dataclass
class AirUpdate:
    """
    :ivar accounting_remark:
    :ivar air_segment:
    :ivar credit_card_auth:
    :ivar air_pricing_adjustment:
    :ivar air_pricing_ticketing_modifiers: Ticketing modifiers to be
        updated.
    :ivar delivery_info:
    :ivar air_segment_special_update:
    :ivar loyalty_card:
    :ivar ssr:
    :ivar general_remark:
    :ivar auto_seat_assignment:
    :ivar specific_seat_assignment:
    :ivar air_pricing_payment:
    :ivar associated_remark:
    :ivar pocket_itinerary_remark:
    :ivar optional_services_info:
    :ivar third_party_information:
    :ivar travel_compliance_data:
    :ivar reservation_locator_code:
    :ivar booking_traveler_ref:
    :ivar restrict_waitlist: Restrict Update if it modifies a Waitlisted
        AirSegment. Provider: 1G,1V,1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    air_pricing_adjustment: List[AirPricingAdjustment] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingAdjustment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_pricing_ticketing_modifiers: List[AirPricingTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingTicketingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    delivery_info: Optional[DeliveryInfo] = field(
        default=None,
        metadata={
            "name": "DeliveryInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_segment_special_update: Optional[AirSegmentSpecialUpdate] = field(
        default=None,
        metadata={
            "name": "AirSegmentSpecialUpdate",
            "type": "Element",
        }
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    auto_seat_assignment: Optional[AutoSeatAssignment] = field(
        default=None,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_pricing_payment: Optional[AirPricingPayment] = field(
        default=None,
        metadata={
            "name": "AirPricingPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    associated_remark: List[AirAirAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    pocket_itinerary_remark: List[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "name": "PocketItineraryRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    optional_services_info: Optional[OptionalServicesInfo] = field(
        default=None,
        metadata={
            "name": "OptionalServicesInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
    restrict_waitlist: bool = field(
        default=False,
        metadata={
            "name": "RestrictWaitlist",
            "type": "Attribute",
        }
    )


@dataclass
class BaseSearchModifiers:
    """
    Controls and switches for the Universal Record Search and Saved Trip search
    request.

    :ivar travel_date: Matched with flight departure date or hotel
        check-in date or vehicle pick-up date. For Rail, travel date
        should be between journey start and end dates, Cannot be
        combined with any date in product level ReservationCriteria
    :ivar include_all_names: If true, include all the passenger names in
        the results. Otherwise include only the name of the primary
        passenger.
    :ivar include_agent_info: Include information about the agent who
        created, modified or ticketed the Universal Record.
    :ivar max_results:
    :ivar start_from_result:
    :ivar exclude_air: Exclude Air reservations from the results
    :ivar exclude_vehicle: Exclude Vehicle reservations from the results
    :ivar exclude_hotel: Exclude Hotel reservations from the results.
    """
    travel_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    include_all_names: bool = field(
        default=False,
        metadata={
            "name": "IncludeAllNames",
            "type": "Attribute",
        }
    )
    include_agent_info: bool = field(
        default=False,
        metadata={
            "name": "IncludeAgentInfo",
            "type": "Attribute",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    start_from_result: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    exclude_air: bool = field(
        default=False,
        metadata={
            "name": "ExcludeAir",
            "type": "Attribute",
        }
    )
    exclude_vehicle: bool = field(
        default=False,
        metadata={
            "name": "ExcludeVehicle",
            "type": "Attribute",
        }
    )
    exclude_hotel: bool = field(
        default=False,
        metadata={
            "name": "ExcludeHotel",
            "type": "Attribute",
        }
    )


@dataclass
class DisplayDetails:
    """
    The container to display the contents of PNR in GDS format.

    :ivar display_detail:
    :ivar display_contents:
    :ivar provider_reservation_detail: Provider Reservation data exists.
    :ivar custom_check: Custom check data exists.
    :ivar provider_profile: Provider Profile data exists.
    :ivar divide_details: Divide Details data exists.
    :ivar enhanced_itin_modifiers: Enhanced itinerary modifiers data
        exists
    :ivar integrated_content: Integrated content data exists
    :ivar cruise: Cruise data exists.
    :ivar rail_segment: Rail Segment data exists.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    display_detail: List[DisplayDetail] = field(
        default_factory=list,
        metadata={
            "name": "DisplayDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    display_contents: Optional[str] = field(
        default=None,
        metadata={
            "name": "DisplayContents",
            "type": "Element",
        }
    )
    provider_reservation_detail: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetail",
            "type": "Attribute",
        }
    )
    custom_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CustomCheck",
            "type": "Attribute",
        }
    )
    provider_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProviderProfile",
            "type": "Attribute",
        }
    )
    divide_details: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DivideDetails",
            "type": "Attribute",
        }
    )
    enhanced_itin_modifiers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnhancedItinModifiers",
            "type": "Attribute",
        }
    )
    integrated_content: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntegratedContent",
            "type": "Attribute",
        }
    )
    cruise: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cruise",
            "type": "Attribute",
        }
    )
    rail_segment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RailSegment",
            "type": "Attribute",
        }
    )


@dataclass
class HotelReservationCriteria:
    """
    Criteria for searching the Hotel reservations.

    :ivar check_in_date: Hotel Check In Date or Date Range
    :ivar hotel_chain_code: Hotel Chain Code
    :ivar hotel_code:
    :ivar hotel_confirmation:
    :ivar location:
    :ivar passive_only: Search for Passives Only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    check_in_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "CheckInDate",
            "type": "Element",
        }
    )
    hotel_chain_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelChainCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    hotel_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "max_length": 32,
        }
    )
    hotel_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelConfirmation",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        }
    )


@dataclass
class ProviderReservationSearchResult:
    """
    Container for reservations that match the search criteria.

    :ivar name:
    :ivar product_info:
    :ivar agency_info:
    :ivar universal_record_locator_code:
    :ivar created_date: The date the resevation record was created
    :ivar earliest_travel_date: The date on which th earliest travel can
        occur
    :ivar ticketed: If the reservation is ticketed. Applies to an AIR
        reservation only
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar external_search_index:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    product_info: List[TypeProductInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProductInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
        }
    )
    created_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        }
    )
    earliest_travel_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestTravelDate",
            "type": "Attribute",
        }
    )
    ticketed: Optional[TypeReservationTicketed] = field(
        default=None,
        metadata={
            "name": "Ticketed",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        }
    )
    external_search_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalSearchIndex",
            "type": "Attribute",
        }
    )


@dataclass
class RailReservationCriteria:
    """
    Criteria for searching the Rail reservations.

    :ivar journey_departure_date: Hotel Check In Date or Date Range
    :ivar journey_arrival_date: Hotel Check In Date or Date Range
    :ivar segment_departure_date: Hotel Check In Date or Date Range
    :ivar segment_arrival_date: Hotel Check In Date or Date Range
    :ivar journey_origin: The IATA location code for this origination of
        this entity.
    :ivar journey_destination: The IATA location code for this
        destination of this entity.
    :ivar journey_rail_loc_origin: RCH specific origin code (a.k.a
        UCodes) which uniquely identifies a train station.
    :ivar journey_rail_loc_destination: RCH specific destination code
        (a.k.a UCodes) which uniquely identifies a train station.
    :ivar supplier_code:
    :ivar train_number:
    :ivar passive_only: Search for Passives Only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    journey_departure_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "JourneyDepartureDate",
            "type": "Element",
        }
    )
    journey_arrival_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "JourneyArrivalDate",
            "type": "Element",
        }
    )
    segment_departure_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "SegmentDepartureDate",
            "type": "Element",
        }
    )
    segment_arrival_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "SegmentArrivalDate",
            "type": "Element",
        }
    )
    journey_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyOrigin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    journey_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyDestination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    journey_rail_loc_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyRailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    journey_rail_loc_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyRailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        }
    )
    train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
        }
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        }
    )


@dataclass
class SavedTripSearchResult:
    """
    Container for SavedTrp that match the search criteria.

    :ivar product_info:
    :ivar earliest_travel_date: The date on which the earliest travel
        can occur.
    :ivar created_date: The date the SavedTrip was created.
    :ivar saved_trip_name:
    :ivar locator_code:
    :ivar universal_record_locator_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    product_info: List["SavedTripSearchResult.ProductInfo"] = field(
        default_factory=list,
        metadata={
            "name": "ProductInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    earliest_travel_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestTravelDate",
            "type": "Attribute",
        }
    )
    created_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        }
    )
    saved_trip_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SavedTripName",
            "type": "Attribute",
            "required": True,
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
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )

    @dataclass
    class ProductInfo(TypeSavedTripProductInfo):
        name: List[Name] = field(
            default_factory=list,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 999,
            }
        )


@dataclass
class UniversalRecordSearchResult:
    """
    Container for reservations that match the search criteria.

    :ivar product_info:
    :ivar universal_record_locator_code:
    :ivar earliest_travel_date: The date on which th earliest travel can
        occur
    :ivar created_date: The date the resevation record was created
    :ivar saved_trip_locator_code: Locator Code of the Saved Trip that
        is associated to the Universal Record.
    :ivar ticketed: If the universal record is ticketed or not or
        partially ticketed
    :ivar record_status: Status of Universal Record e.g.
        Current,Past,Cancelled
    :ivar ticket_status: If the universal record is ticketed or not or
        partially ticketed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    product_info: List["UniversalRecordSearchResult.ProductInfo"] = field(
        default_factory=list,
        metadata={
            "name": "ProductInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
        }
    )
    earliest_travel_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestTravelDate",
            "type": "Attribute",
        }
    )
    created_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        }
    )
    saved_trip_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SavedTripLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticketed: Optional[TypeReservationTicketed] = field(
        default=None,
        metadata={
            "name": "Ticketed",
            "type": "Attribute",
        }
    )
    record_status: Optional[TypeRecordStatus] = field(
        default=None,
        metadata={
            "name": "RecordStatus",
            "type": "Attribute",
        }
    )
    ticket_status: Optional[UrticketStatus] = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProductInfo(TypeProductInfo):
        name: List[Name] = field(
            default_factory=list,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 999,
            }
        )


@dataclass
class VehicleReservationCriteria:
    """
    Criteria for searching the Vehicle reservations.

    :ivar pick_up_date: Vehicle PickUp Date or Date Range
    :ivar vehicle_confirmation:
    :ivar location:
    :ivar vendor_code: Vehicle Vendor Code
    :ivar location_number:
    :ivar passive_only: Search for Passives Only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    pick_up_date: Optional[TypeDateSpec] = field(
        default=None,
        metadata={
            "name": "PickUpDate",
            "type": "Element",
        }
    )
    vehicle_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleConfirmation",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationNumber",
            "type": "Attribute",
        }
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        }
    )


@dataclass
class TypeSegmentPolicy:
    """
    :ivar preference:
    :ivar segment_ref: Reference to the original segment.
    :ivar in_policy: Determine if this segment is In or Out of policy.
        By default it is InPolicy.
    :ivar in_contract: Determine if this segment is In or Out of
        contract. By default it is InContract.
    """
    class Meta:
        name = "typeSegmentPolicy"

    preference: List[Preference] = field(
        default_factory=list,
        metadata={
            "name": "Preference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
            "max_occurs": 999,
        }
    )
    segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "required": True,
        }
    )
    in_policy: bool = field(
        default=True,
        metadata={
            "name": "InPolicy",
            "type": "Attribute",
        }
    )
    in_contract: bool = field(
        default=True,
        metadata={
            "name": "InContract",
            "type": "Attribute",
        }
    )


@dataclass
class PolicyInformation:
    """
    Policy information associated with SavedTrip.

    :ivar air_policy:
    :ivar rail_policy:
    :ivar hotel_policy:
    :ivar vehicle_policy:
    :ivar booking_traveler_ref: Booking Traveler associated to this
        policy information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    air_policy: List[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "AirPolicy",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_policy: List[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "RailPolicy",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_policy: List[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "HotelPolicy",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_policy: List[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePolicy",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_traveler_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProviderReservationDisplayDetailsList:
    """
    Response to display the addtional details of provider reservation information
    .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    display_details: List[DisplayDetails] = field(
        default_factory=list,
        metadata={
            "name": "DisplayDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class SavedTripSearchModifiers(BaseSearchModifiers):
    """
    Controls and switches for the SavedTrip Search request.

    :ivar saved_trip_name: Represents name of a savedTrip.
    :ivar exclude_urassociated: Exclude SavedTrips associated with a
        UniversalRecord.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SavedTripName",
            "type": "Attribute",
        }
    )
    exclude_urassociated: bool = field(
        default=True,
        metadata={
            "name": "ExcludeURAssociated",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalModifyCmd:
    """
    Container for the elements that will be batch updated to a UniversalRecord.

    :ivar vehicle_add:
    :ivar vehicle_delete:
    :ivar vehicle_update:
    :ivar air_add:
    :ivar air_delete:
    :ivar air_update:
    :ivar universal_add:
    :ivar universal_delete:
    :ivar universal_update:
    :ivar hotel_add:
    :ivar hotel_update:
    :ivar hotel_delete:
    :ivar passive_add:
    :ivar passive_delete:
    :ivar rail_update:
    :ivar key: Refers the universal modify command key. It should be
        unique in the request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    vehicle_add: Optional[VehicleAdd] = field(
        default=None,
        metadata={
            "name": "VehicleAdd",
            "type": "Element",
        }
    )
    vehicle_delete: Optional[VehicleDelete] = field(
        default=None,
        metadata={
            "name": "VehicleDelete",
            "type": "Element",
        }
    )
    vehicle_update: Optional[VehicleUpdate] = field(
        default=None,
        metadata={
            "name": "VehicleUpdate",
            "type": "Element",
        }
    )
    air_add: Optional[AirAdd] = field(
        default=None,
        metadata={
            "name": "AirAdd",
            "type": "Element",
        }
    )
    air_delete: Optional[AirDelete] = field(
        default=None,
        metadata={
            "name": "AirDelete",
            "type": "Element",
        }
    )
    air_update: Optional[AirUpdate] = field(
        default=None,
        metadata={
            "name": "AirUpdate",
            "type": "Element",
        }
    )
    universal_add: Optional[UniversalAdd] = field(
        default=None,
        metadata={
            "name": "UniversalAdd",
            "type": "Element",
        }
    )
    universal_delete: Optional[UniversalDelete] = field(
        default=None,
        metadata={
            "name": "UniversalDelete",
            "type": "Element",
        }
    )
    universal_update: Optional[UniversalUpdate] = field(
        default=None,
        metadata={
            "name": "UniversalUpdate",
            "type": "Element",
        }
    )
    hotel_add: Optional[HotelAdd] = field(
        default=None,
        metadata={
            "name": "HotelAdd",
            "type": "Element",
        }
    )
    hotel_update: Optional[HotelUpdate] = field(
        default=None,
        metadata={
            "name": "HotelUpdate",
            "type": "Element",
        }
    )
    hotel_delete: Optional[HotelDelete] = field(
        default=None,
        metadata={
            "name": "HotelDelete",
            "type": "Element",
        }
    )
    passive_add: Optional[PassiveAdd] = field(
        default=None,
        metadata={
            "name": "PassiveAdd",
            "type": "Element",
        }
    )
    passive_delete: Optional[PassiveDelete] = field(
        default=None,
        metadata={
            "name": "PassiveDelete",
            "type": "Element",
        }
    )
    rail_update: Optional[RailUpdate] = field(
        default=None,
        metadata={
            "name": "RailUpdate",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class UniversalRecordSearchModifiers(BaseSearchModifiers):
    """
    Controls and switches for the Universal Record Search request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ProviderReservationInfo:
    """
    Provider Reservation informations.

    :ivar provider_reservation_details:
    :ivar provider_reservation_display_details_list:
    :ivar key: Key value of the provider reservation
    :ivar provider_code: Contains the Provider Code of the entity
        housing the actual reservation in the event this is a passive
        one.
    :ivar locator_code: Contains the Locator Code of the actual
        reservation in the event this is a passive reservation.
    :ivar create_date: The date and time that this reservation was
        created.
    :ivar host_create_date: The date that this reservation was created
        in the host system.
    :ivar host_create_time: The Time that this reservation was created
        in the host system for 1P.
    :ivar modified_date: The date and time that this reservation was
        last modified for any reason.
    :ivar imported: Identifies a reservation that was originally created
        elsewhere and imported into a Universal Record.
    :ivar ticketing_modifiers_ref: Reference to a Ticketing Modifers
        which is attached to this PNR. Ticketing Modifers referred  by
        this Key is a Primary Ticketing Modifers. Worldspan Primary DI
        line will be supported using this feature.
    :ivar in_queue_mode: Identifies whether the gds pnr is being
        processed from the GDS queue.
    :ivar group_ref: Represents a traveler group for Group booking and
        all their accompanying data. SUPPORTED PROVIDER: Worldspan.
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    :ivar owning_pcc: Indentifies the owning PCC of the PNR. PROVIDER
        SUPPORTED: Worldspan,Galileo and Apollo
    :ivar agent_override: AgentSine value that was used during PNR
        creation or End Transact.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    provider_reservation_details: Optional[ProviderReservationDetails] = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetails",
            "type": "Element",
        }
    )
    provider_reservation_display_details_list: Optional[ProviderReservationDisplayDetailsList] = field(
        default=None,
        metadata={
            "name": "ProviderReservationDisplayDetailsList",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
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
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    host_create_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "HostCreateDate",
            "type": "Attribute",
        }
    )
    host_create_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "HostCreateTime",
            "type": "Attribute",
        }
    )
    modified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    imported: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Imported",
            "type": "Attribute",
        }
    )
    ticketing_modifiers_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Attribute",
        }
    )
    in_queue_mode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InQueueMode",
            "type": "Attribute",
        }
    )
    group_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupRef",
            "type": "Attribute",
        }
    )
    el_stat: Optional[TypeElementStatus] = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    owning_pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwningPCC",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    agent_override: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentOverride",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class SavedTrip:
    """
    SavedTrip holds a draft Itinerary/booking which can be used at later point of
    time to do a booking.

    :ivar booking_traveler:
    :ivar agency_contact_info:
    :ivar search_passenger:
    :ivar point_of_sale:
    :ivar accounting_remark:
    :ivar general_remark:
    :ivar agency_info:
    :ivar reservation_name:
    :ivar air_pricing_modifiers:
    :ivar air_pricing_solution:
    :ivar air_trip_note:
    :ivar vehicle_search_modifiers:
    :ivar vehicle_date_location:
    :ivar special_equipment:
    :ivar vehicle_special_request:
    :ivar payment_information:
    :ivar delivery_address:
    :ivar collection_address:
    :ivar flight_arrival_information:
    :ivar vehicle:
    :ivar vehicle_trip_note:
    :ivar vendor_location:
    :ivar hotel_property:
    :ivar hotel_stay:
    :ivar hotel_rules_modifiers:
    :ivar hotel_details_modifiers:
    :ivar hotel_rate_detail:
    :ivar promotion_code:
    :ivar hotel_trip_note:
    :ivar rail_pricing_solution:
    :ivar rail_fare_note:
    :ivar rail_trip_note:
    :ivar saved_trip_note:
    :ivar saved_trip_activity:
    :ivar profile_association:
    :ivar policy_information:
    :ivar locator_code: Alpha numeric String to identify a SavedTrip
        uniquely.
    :ivar universal_record_locator_code: Alpha numeric String to
        identify a the UniversalRecord created using this SavedTrip.
    :ivar name: Name of the Saved Trip.
    :ivar create_date: The date and time that this SavedTrip was
        created.
    :ivar modified_date: The date and time that this SavedTrip was
        Modified.
    :ivar version:
    :ivar status:
    :ivar created_by_agent: The Agent Code who created the SavedTrip.
    :ivar modified_by_agent: The Agent Code that modified the SavedTrip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    agency_contact_info: Optional[AgencyContactInfo] = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    reservation_name: Optional[ReservationName] = field(
        default=None,
        metadata={
            "name": "ReservationName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_pricing_modifiers: List[AirPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_trip_note: List[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "AirTripNote",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    vehicle_search_modifiers: List[VehicleSearchModifiers] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_date_location: List[VehicleDateLocation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    special_equipment: List[SpecialEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_special_request: List[VehicleSpecialRequest] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    payment_information: List[PaymentInformation] = field(
        default_factory=list,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    delivery_address: List[DeliveryAddress] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    collection_address: List[CollectionAddress] = field(
        default_factory=list,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    flight_arrival_information: List[FlightArrivalInformation] = field(
        default_factory=list,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_trip_note: List[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTripNote",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    vendor_location: List[VendorLocation] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_property: List[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_stay: List[HotelStay] = field(
        default_factory=list,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_rules_modifiers: List[HotelRulesModifiers] = field(
        default_factory=list,
        metadata={
            "name": "HotelRulesModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_details_modifiers: List[HotelDetailsModifiers] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailsModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_rate_detail: List[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    promotion_code: List[PromotionCode] = field(
        default_factory=list,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_trip_note: List[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "HotelTripNote",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    rail_pricing_solution: List[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
    rail_fare_note: List[RailFareNote] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNote",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
    rail_trip_note: List[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "RailTripNote",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    saved_trip_note: List[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "SavedTripNote",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    saved_trip_activity: List[SavedTripActivity] = field(
        default_factory=list,
        metadata={
            "name": "SavedTripActivity",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_association: List[ProfileAssociation] = field(
        default_factory=list,
        metadata={
            "name": "ProfileAssociation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    policy_information: Optional[PolicyInformation] = field(
        default=None,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        }
    )
    modified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    created_by_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedByAgent",
            "type": "Attribute",
        }
    )
    modified_by_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedByAgent",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalRecord:
    """
    Universal Record holds one or more provider reservations.

    :ivar linked_universal_record:
    :ivar group:
    :ivar booking_traveler:
    :ivar service_fee_info: Travel Agency Service Fees (TASF) are
        charged by the agency through BSP or Airline Reporting
        Corporation (ARC). FOP will appear directly inside
        UniversalRecord
    :ivar osi:
    :ivar action_status:
    :ivar provider_reservation_info:
    :ivar air_reservation:
    :ivar hotel_reservation:
    :ivar vehicle_reservation:
    :ivar passive_reservation:
    :ivar rail_reservation:
    :ivar cruise_reservation: The parent container for all cruise
        booking data. Supported Providers :1V
    :ivar emdsummary_info: List of EMDs to be shown as part of UR.
        Supported providers are 1V/1G/1P
    :ivar provider_arnksegment:
    :ivar segment_continuity_info:
    :ivar xmlremark:
    :ivar general_remark:
    :ivar accounting_remark:
    :ivar unassociated_remark:
    :ivar postscript:
    :ivar agency_info:
    :ivar applied_profile:
    :ivar agency_contact_info:
    :ivar customer_id:
    :ivar commission_remark:
    :ivar consolidator_remark:
    :ivar invoice_remark:
    :ivar review_booking: Review Booking or Queue Minders is to add the
        reminders in the Provider Reservation along with the date time
        and Queue details. On the date time defined in reminders, the
        message along with the PNR goes to the desired Queue.
    :ivar ssr: SSR's having no bookingTravelerRef need to add at
        providerReservation level outside bookingTraveler
    :ivar invoice_data:
    :ivar form_of_payment: Provider:
        1G,1V,1P,ACH,SDK.Product:Air,Hotel,Vehicle,Cruise
    :ivar locator_code: Unique Identifier of a Universal Record. If this
        is ViewOnly UR then Locator Code is '999999'.
    :ivar saved_trip_locator_code:
    :ivar lock_reason: The reason for which the reservation is currently
        locked for modifications
    :ivar create_date: The date and time that this reservation was
        created.
    :ivar version:
    :ivar status:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    linked_universal_record: List[LinkedUniversalRecord] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    action_status: List[ActionStatus] = field(
        default_factory=list,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    provider_reservation_info: List[ProviderReservationInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_reservation: List[AirReservation] = field(
        default_factory=list,
        metadata={
            "name": "AirReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_reservation: List[HotelReservation] = field(
        default_factory=list,
        metadata={
            "name": "HotelReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_reservation: List[VehicleReservation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    passive_reservation: List[PassiveReservation] = field(
        default_factory=list,
        metadata={
            "name": "PassiveReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        }
    )
    rail_reservation: List[RailReservation] = field(
        default_factory=list,
        metadata={
            "name": "RailReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
    cruise_reservation: List[CruiseReservation] = field(
        default_factory=list,
        metadata={
            "name": "CruiseReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/cruise_v52_0",
            "max_occurs": 999,
        }
    )
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    provider_arnksegment: List[ProviderArnksegment] = field(
        default_factory=list,
        metadata={
            "name": "ProviderARNKSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    segment_continuity_info: Optional[SegmentContinuityInfo] = field(
        default=None,
        metadata={
            "name": "SegmentContinuityInfo",
            "type": "Element",
        }
    )
    xmlremark: List[Xmlremark] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    postscript: List[Postscript] = field(
        default_factory=list,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    applied_profile: Optional[AppliedProfile] = field(
        default=None,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    agency_contact_info: Optional[AgencyContactInfo] = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    customer_id: List[CustomerId] = field(
        default_factory=list,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    commission_remark: List[CommissionRemark] = field(
        default_factory=list,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    consolidator_remark: List[ConsolidatorRemark] = field(
        default_factory=list,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    invoice_remark: List[InvoiceRemark] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    review_booking: List[ReviewBooking] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    ssr: List[Ssr] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    invoice_data: List[InvoiceData] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    saved_trip_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SavedTripLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    lock_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "LockReason",
            "type": "Attribute",
        }
    )
    create_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateDate",
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
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
