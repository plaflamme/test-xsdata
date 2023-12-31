from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from generated.common_v52_0.common import (
    BaseReservation,
    BookingTravelerRef,
    ConnectionPoint,
    DiscountCard,
    HostToken,
    Payment,
    Remark,
    Segment,
    SupplierLocator,
    TypeElementStatus,
    TypeFlexibleTimeSpec,
    TypePassengerType,
    TypeSearchLocation,
    TypeTimeSpec,
)

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class FareValidity:
    """
    Associates fare validity dates with journeys.

    :ivar rail_journey_ref: Reference to a journey to which this fare
        validity refers.
    :ivar not_valid_before: Fare not valid before this date.
    :ivar not_valid_after: Fare not valid after this date.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailJourneyRef",
            "type": "Attribute",
            "required": True,
        }
    )
    not_valid_before: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )


@dataclass
class FulFillmentType:
    """Fulfillment options for this segment.

    the options will be one of "Ticket on Departure", "Ticketless",
    "Ticket By Email", "Travel Agency"
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "min_length": 0,
            "max_length": 255,
        }
    )


@dataclass
class JourneyRemark:
    """
    A Remark for a Journey.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )


@dataclass
class OperatingCompany:
    """
    A textual remark identifying the OperatingCompany/Train Service other than BN
    orTL.

    :ivar value:
    :ivar code: Company Short Text
    :ivar name: Name Identifying the Train Service other than BN orTL
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailAutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type.

    :ivar seat_type: Indicates codeset of values such as Seat Type like
        Place,Position, Smoking Choice, Place Arrangement, Place
        Direction, Compartment.
    :ivar seat_value: Indicates the value specific to the selected type.
    :ivar rail_segment_ref: The rail segment that this assignment
        belongs to
    :ivar booking_traveler_ref: The booking traveler that this seat
        assignment is for. If not entered, this applies to the primary
        booking traveler and other passengers are adjacent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    seat_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatType",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 255,
        }
    )
    seat_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatValue",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 255,
        }
    )
    rail_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
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
class RailAvailInfo:
    """
    :ivar class_code: A booking code or fare basis code or fare class.
    :ivar quantity: Available fare basis code or fare class quantity.
    :ivar cabin_class: The fare basis code or fare class for this fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    class_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class RailBookingInfo:
    """
    Links journeys and fares together.

    :ivar rail_fare_ref: Reference to a fare that applies to the journey
        below.
    :ivar rail_journey_ref: Reference to a journeys on which the above
        fare applies.
    :ivar optional_service: Indicate the OfferFareItem elements  will be
        Optional or not.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailFareRef",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailJourneyRef",
            "type": "Attribute",
            "required": True,
        }
    )
    optional_service: bool = field(
        default=False,
        metadata={
            "name": "OptionalService",
            "type": "Attribute",
        }
    )


@dataclass
class RailExchangeInfo:
    """
    Exchange information for the rail booking.

    :ivar refund_amount:
    :ivar cancellation_fee:
    :ivar exchange_amount:
    :ivar approximate_refund_amount:
    :ivar approximate_cancellation_fee:
    :ivar approximate_exchange_amount: The Converted total price in
        Default Currency for this entity including base price and all
        taxes.
    :ivar retain_amount: Amount retained by a rail vendor for future use
        at the vendor’s site.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    refund_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    cancellation_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancellationFee",
            "type": "Attribute",
        }
    )
    exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        }
    )
    approximate_refund_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateRefundAmount",
            "type": "Attribute",
        }
    )
    approximate_cancellation_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateCancellationFee",
            "type": "Attribute",
        }
    )
    approximate_exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
        }
    )
    retain_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        }
    )


@dataclass
class RailFareIdref:
    """
    Reference to a complete FareID from a shared list.
    """
    class Meta:
        name = "RailFareIDRef"
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailFareNoteRef:
    """A reference to a fare note from a shared list.

    Used to minimize xml results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailFareRef:
    """
    Reference to a complete FareInfo from a shared list.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailInfo:
    """
    Container for rail-related information required for retrieving a rail seat
    map/coach map.

    :ivar origin: The IATA location code for this origination of this
        entity.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which
        uniquely identifies a train station.
    :ivar destination: The IATA location code for this destination of
        this entity.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a
        UCodes) which uniquely identifies a train station.
    :ivar departure_time: The date and time at which this entity
        departs. This does not include time zone information since it
        can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives
        at the destination. This does not include time zone information
        since it can be derived from the origin location.
    :ivar train_number:
    :ivar provider_code:
    :ivar supplier_code:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    rail_loc_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
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
    rail_loc_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
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
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class RailJourneyRef:
    """
    Reference to a RailJourney.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailRefundInfo:
    """
    Information about refund.

    :ivar refund_amount: Amount refunded back to customer.
    :ivar cancellation_fee: Cancellation penalty imposed by the
        distributor.
    :ivar refund: Indicates whether vendor offers refund on rail
        reservation.
    :ivar retain: Indicates whether vendor retains the amount to be used
        later.
    :ivar retain_amount: Amount retained by rail vendor for futute
        exchange/rail book at rail vendor site.
    :ivar net_amount: Net total amount to be refunded or retained by the
        vendor.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    refund_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefundAmount",
            "type": "Attribute",
        }
    )
    cancellation_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancellationFee",
            "type": "Attribute",
        }
    )
    refund: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Refund",
            "type": "Attribute",
        }
    )
    retain: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Retain",
            "type": "Attribute",
        }
    )
    retain_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "RetainAmount",
            "type": "Attribute",
        }
    )
    net_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetAmount",
            "type": "Attribute",
        }
    )


@dataclass
class RailSegmentRef:
    """
    Reference to a RaiLSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


class RailSolutionChangedInfoReasonCode(Enum):
    PRICE = "Price"
    SCHEDULE = "Schedule"
    BOTH = "Both"


@dataclass
class RailSpecificSeatAssignment:
    """
    Request object used to request a specific coach and seat number or a seat near-
    to a specific seat number.

    :ivar coach_label: The coach number of the train being requested.
    :ivar place_label: The actual seat number or the close-to seat
        number based on the Assignment.
    :ivar assignment: Defines how the PlaceLabel should be applied.  The
        values are 6.STP for actual seat or 2.STP for close-to seat.
        Default is 2.STP.
    :ivar rail_segment_ref: The rail segment to which this assignment
        belongs.
    :ivar booking_traveler_ref: The BookingTraveler for this seat
        assignment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    coach_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoachLabel",
            "type": "Attribute",
            "required": True,
        }
    )
    place_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceLabel",
            "type": "Attribute",
            "required": True,
        }
    )
    assignment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assignment",
            "type": "Attribute",
            "required": True,
        }
    )
    rail_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
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
class RailSupplier:
    """
    :ivar code: 2 character Rail distributor code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )


@dataclass
class TicketAdvisory:
    """
    Additional ticket information.

    :ivar value:
    :ivar key:
    :ivar language_code: ISO 639 two-character language codes are used
        to retrieve specific information in the requested language. For
        Rich Content and Branding, language codes ZH-HANT (Chinese
        Traditional), ZH-HANS (Chinese Simplified), FR-CA (French
        Canadian) and PT-BR (Portuguese Brazil) can also be used. For
        RCH, language codes ENGB, ENUS, DEDE, DECH can also be used.
        Only certain services support this attribute. Providers: ACH,
        RCH, 1G, 1V, 1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 500,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
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


class TypeCoachClassType(Enum):
    """
    Values for accommodation class.
    """
    FIRST_CLASS = "First Class"
    STANDARD_CLASS = "Standard Class"
    FIRST_AND_STANDARD_CLASS = "First and Standard Class"
    OTHER = "Other"


class TypeJourneyDirection(Enum):
    """
    Outbound and Return directions.
    """
    OUTWARD = "Outward"
    RETURN = "Return"


class TypeRailDirection(Enum):
    """
    The direction of travel.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"
    BOTH = "Both"


class TypeRailSegmentInfo(Enum):
    """
    Extra for ExtraSegmentInfo and Vendor for VendorMessages.
    """
    EXTRA = "Extra"
    VENDOR = "Vendor"
    SERVICES = "Services"


class TypeResponseType(Enum):
    """Indicates the type of information to be returned in
    RailShopModifyAPIResponse.

    Values are “Schedules” or “Availability” or “Fares”.  If not sent,
    “Fares” will be mapped if the request is for a specific rail
    segments, otherwise “Availability” will be mapped. Provider
    Supported RCH.
    """
    AVAILABILITY = "Availability"
    SCHEDULES = "Schedules"
    FARES = "Fares"


class TypeTransportMode(Enum):
    """
    Enumeration of all Train Transport Modes.
    """
    BICYCLE = "Bicycle"
    BOAT = "Boat"
    BUS = "Bus"
    CABLE_CAR = "Cable Car"
    CAR = "Car"
    CARRIAGE = "Carriage"
    COURTESY_CAR = "Courtesy car"
    HELICOPTER = "Helicopter"
    LIMOUSINE = "Limousine"
    METRO = "Metro"
    MONORAIL = "Monorail"
    MOTORBIKE = "Motorbike"
    PACK_ANIMAL = "Pack Animal"
    PLANE = "Plane"
    RENTAL_CAR = "Rental Car"
    RICKSHAW = "Rickshaw"
    SHUTTLE = "Shuttle"
    SUBWAY = "Subway"
    SEDAN_CHAIR = "Sedan Chair"
    TAXI = "Taxi"
    TRAIN = "Train"
    TROLLEY = "Trolley"
    TUBE = "Tube"
    WALK = "Walk"
    WATER_TAXI = "Water Taxi"
    OTHER = "Other"
    CAR_RUSH_HOUR = "Car/Rush hour"
    TAXI_RUSH_HOUR = "Taxi/Rush hour"
    NO_TRANSPORTATION = "No Transportation"
    EXPRESS_TRAIN = "Express Train"
    PUBLIC = "Public"
    SHIP_FERRY = "Ship/Ferry"
    UNDERGROUND = "Underground"
    TRAM_LIGHT_RAIL = "Tram/light rail"
    SHARED_TAXI = "Shared Taxi"


@dataclass
class Characteristic:
    """
    Defines coach characteristics such as accommodation class, smoking choice, etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        }
    )
    class_value: Optional[TypeCoachClassType] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        }
    )


@dataclass
class RailFareComponent:
    """
    Contains fare and discount information for each passenger type.

    :ivar discount: Discount information specific to the fare component
    :ivar key:
    :ivar amount: FareComponent amount
    :ivar age:
    :ivar passenger_type_code: The three character passenger code
    :ivar supplier_passenger_type: Supplier passenger type code
    :ivar quantity:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    discount: List["RailFareComponent.Discount"] = field(
        default_factory=list,
        metadata={
            "name": "Discount",
            "type": "Element",
            "max_occurs": 5,
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
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    supplier_passenger_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierPassengerType",
            "type": "Attribute",
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )

    @dataclass
    class Discount:
        discount_card: List[DiscountCard] = field(
            default_factory=list,
            metadata={
                "name": "DiscountCard",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 9,
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
class RailFareId:
    """
    :ivar value:
    :ivar key:
    :ivar category:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        name = "RailFareID"
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
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


@dataclass
class RailFareNote:
    """A simple textual fare note.

    Used within several other objects.

    :ivar value:
    :ivar key:
    :ivar note_name:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    note_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoteName",
            "type": "Attribute",
            "required": True,
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


@dataclass
class RailLegModifiers:
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    permitted_connection_points: Optional["RailLegModifiers.PermittedConnectionPoints"] = field(
        default=None,
        metadata={
            "name": "PermittedConnectionPoints",
            "type": "Element",
        }
    )
    prohibited_connection_points: Optional["RailLegModifiers.ProhibitedConnectionPoints"] = field(
        default=None,
        metadata={
            "name": "ProhibitedConnectionPoints",
            "type": "Element",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        }
    )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class RailPricingModifiers:
    """
    Search flexibiity criteria .

    :ivar discount_card: Discount request for rail.
    :ivar prohibit_non_refundable_fares: Indicates whether it prohibits
        NonRefundable Fares.
    :ivar prohibit_non_exchangeable_fares: Indicates whether it
        prohibits NonExchangeable Fares .
    :ivar currency_type: 3 Letter Currency Code
    :ivar rail_search_type: RailSearchType options are "All Fares"
        "Fastest"  "Lowest Fare" "One Fare Per Class" "Seasons".
        Supported by NTV/VF only for "All Fares" "Lowest Fare" and "One
        Fare Per Class". Provider : RCH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
        }
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        }
    )
    prohibit_non_exchangeable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonExchangeableFares",
            "type": "Attribute",
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )
    rail_search_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailSearchType",
            "type": "Attribute",
        }
    )


@dataclass
class RailSearchModifiers:
    """
    Controls and switches for the Rail Availability Search request.

    :ivar preferred_suppliers:
    :ivar max_changes: The maximum number of stops within a connection.
    :ivar direction: The direction of travel.
    :ivar class_value:
    :ivar max_solutions: The maximum number of solutions to return.
        Decreasing this number
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    preferred_suppliers: Optional["RailSearchModifiers.PreferredSuppliers"] = field(
        default=None,
        metadata={
            "name": "PreferredSuppliers",
            "type": "Element",
        }
    )
    max_changes: int = field(
        default=2,
        metadata={
            "name": "MaxChanges",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 3,
        }
    )
    direction: Optional[TypeRailDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
        }
    )
    max_solutions: int = field(
        default=300,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
        }
    )

    @dataclass
    class PreferredSuppliers:
        rail_supplier: List[RailSupplier] = field(
            default_factory=list,
            metadata={
                "name": "RailSupplier",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class RailSegmentInfo:
    """A textual remark container to hold any printable text.

    (max 512 chars) Holds the ExtraSegmentInfo and VendorMessages from
    RCH response.

    :ivar value:
    :ivar category: Supplier specific category.
    :ivar type_value: Either Extra for ExtraSegmentInfo or Vendor for
        VendorMessages.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    type_value: Optional[TypeRailSegmentInfo] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RailTicketInfo:
    """
    :ivar rail_journey_ref:
    :ivar ticket_advisory:
    :ivar number: Ticket number.
    :ivar issue_location: Issue location is internal distributor code
        associated with the PCC.
    :ivar ticket_status: Status of Ticket.
    :ivar ticket_form_type: FormType of Ticket.
    :ivar traffic_type: Type of traffic.
    :ivar issued_date: Ticket issue date.
    :ivar ticket_type: Type of ticket. Paper, eTicket etc.
    :ivar booking_traveler_ref: Reference to a BookingTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "RailJourneyRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticket_advisory: List[TicketAdvisory] = field(
        default_factory=list,
        metadata={
            "name": "TicketAdvisory",
            "type": "Element",
            "max_occurs": 10,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 19,
        }
    )
    issue_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssueLocation",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 128,
        }
    )
    ticket_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    ticket_form_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketFormType",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
        }
    )
    traffic_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrafficType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    issued_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
        }
    )
    ticket_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
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
class Coach:
    """
    Captures rail seat map/coach map information.

    :ivar characteristic:
    :ivar remark:
    :ivar coach_number: Coach number for which seat map/coach map is
        returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    characteristic: Optional[Characteristic] = field(
        default=None,
        metadata={
            "name": "Characteristic",
            "type": "Element",
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    coach_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoachNumber",
            "type": "Attribute",
        }
    )


@dataclass
class RailFare:
    """
    Information about this fare component.

    :ivar rail_fare_note_ref: Key reference to RailFareNote present in
        RailFareNotList
    :ivar rail_fare_id:
    :ivar rail_fare_idref:
    :ivar fare_validity:
    :ivar host_token:
    :ivar ful_fillment_type:
    :ivar rail_fare_component:
    :ivar key:
    :ivar fare_basis: The fare basis code  or fare description for this
        fare
    :ivar cabin_class: The fare basis code or fare class for this fare
    :ivar passenger_type_code: The PTC that is associated with this
        fare. Default to ADT
    :ivar origin: Returns the airport or city code that defines the
        origin market for this fare.
    :ivar destination: Returns the airport or city code that defines the
        destination market for this fare.
    :ivar effective_date: Returns the date on which this fare was
        quoted. Set as current date
    :ivar amount:
    :ivar route_description: Describes the route of the train fare.
    :ivar ticket_type_code: Describes the main identifier code of the
        fare.
    :ivar fare_reference: Unique reference for the fare that is required
        in RailExchangeQuote request.
    :ivar cross_city_fare: Set to 'true' if the fare is valid across a
        Metropolitan Area, eg. Cross-London travel via the London
        Underground.
    :ivar origin_station_name: The origin station name for the Rail
        Fare.
    :ivar destination_station_name: The destination station name for the
        Rail Fare.
    :ivar reservation_required: Set to true if a seat reservation is
        required while booking.
    :ivar journey_direction: The direction of the Journey (Outward or
        Return) associated with the Rail fare.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which
        uniquely identifies a train station.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a
        UCodes) which uniquely identifies a train station.
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_note_ref: List[RailFareNoteRef] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNoteRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata={
            "name": "RailFareID",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_idref: List[RailFareIdref] = field(
        default_factory=list,
        metadata={
            "name": "RailFareIDRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_validity: List[FareValidity] = field(
        default_factory=list,
        metadata={
            "name": "FareValidity",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: Optional[HostToken] = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    ful_fillment_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FulFillmentType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 0,
            "max_length": 255,
        }
    )
    rail_fare_component: List[RailFareComponent] = field(
        default_factory=list,
        metadata={
            "name": "RailFareComponent",
            "type": "Element",
            "max_occurs": 99,
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
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    passenger_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
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
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    route_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
        }
    )
    ticket_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketTypeCode",
            "type": "Attribute",
        }
    )
    fare_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    cross_city_fare: bool = field(
        default=False,
        metadata={
            "name": "CrossCityFare",
            "type": "Attribute",
        }
    )
    origin_station_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    reservation_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
        }
    )
    journey_direction: Optional[TypeJourneyDirection] = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
        }
    )
    rail_loc_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
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


@dataclass
class RailFareIdlist:
    """
    The shared object list of FareIDs.
    """
    class Meta:
        name = "RailFareIDList"
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_id: List[RailFareId] = field(
        default_factory=list,
        metadata={
            "name": "RailFareID",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class RailFareNoteList:
    """
    The shared object list of Notes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_note: List[RailFareNote] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNote",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailSegment(Segment):
    """
    Rail Segment.

    :ivar rail_segment_info:
    :ivar operating_company:
    :ivar rail_avail_info:
    :ivar ful_fillment_type:
    :ivar train_number:
    :ivar origin: The IATA location code for this origination of this
        entity.
    :ivar destination: The IATA location code for this destination of
        this entity.
    :ivar departure_time: The date and time at which this entity
        departs. This does not include time zone information since it
        can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives
        at the destination. This does not include time zone information
        since it can be derived from the origin location.
    :ivar origin_station_name: The origin station name for the Journey.
    :ivar destination_station_name: The destination station name for the
        Journey.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which
        uniquely identifies a train station.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a
        UCodes) which uniquely identifies a train station.
    :ivar train_type: Type of train used. Same as TrainServiceType.
    :ivar train_type_code: Code for type of train used. Same as
        TrainServiceType.
    :ivar transport_mode: Type of Transport Mode used.
    :ivar seat_assignable: Set to true if there exists seats to be
        booked
    :ivar transport_code: Supplier specific train code
    :ivar reservation_required: Set to true if a reservation is required
        for booking.
    :ivar travel_time: Total time spent (minutes) traveling
    :ivar host_token_ref: The reference key for the host token. From the
        HostTokenList Providers RCH.
    :ivar cabin_class: Rail Cabin class specification. The valid values
        are Economy, Business, First and Other
    :ivar class_code: A booking code or fare basis code or fare class.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment_info: List[RailSegmentInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailSegmentInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    operating_company: Optional[OperatingCompany] = field(
        default=None,
        metadata={
            "name": "OperatingCompany",
            "type": "Element",
        }
    )
    rail_avail_info: List[RailAvailInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailAvailInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ful_fillment_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FulFillmentType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 0,
            "max_length": 255,
        }
    )
    train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
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
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    origin_station_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    rail_loc_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    train_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainType",
            "type": "Attribute",
        }
    )
    train_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainTypeCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    transport_mode: Optional[TypeTransportMode] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Attribute",
        }
    )
    seat_assignable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SeatAssignable",
            "type": "Attribute",
        }
    )
    transport_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportCode",
            "type": "Attribute",
        }
    )
    reservation_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Attribute",
        }
    )
    travel_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    class_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class RailFareList:
    """
    The shared object list of FareInfos.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata={
            "name": "RailFare",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class RailJourney:
    """
    Captures all journey-related data.

    :ivar rail_segment:
    :ivar rail_segment_ref:
    :ivar journey_remark:
    :ivar host_token:
    :ivar key:
    :ivar origin: The IATA location code for this origination of this
        entity.
    :ivar destination: The IATA location code for this destination of
        this entity.
    :ivar departure_time: The date and time at which this entity
        departs. This does not include time zone information since it
        can be derived from the origin location.
    :ivar arrival_time: The date and time at which this entity arrives
        at the destination. This does not include time zone information
        since it can be derived from the origin location.
    :ivar origin_station_name: The origin station name for the Journey.
    :ivar destination_station_name: The destination station name for the
        Journey.
    :ivar rail_loc_origin: RCH specific origin code (a.k.a UCodes) which
        uniquely identifies a train station.
    :ivar rail_loc_destination: RCH specific destination code (a.k.a
        UCodes) which uniquely identifies a train station.
    :ivar route_description: The description of the route.
    :ivar journey_direction: The direction of the Journey (Outward or
        Return).
    :ivar journey_duration: The duration of the entire Journey in
        minutes
    :ivar total_price: The total price for this entity including base
        price and all taxes.
    :ivar base_price: Represents the base price for this entity. This
        does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default
        Currency for this entity. This does not include any taxes or
        surcharges.
    :ivar equivalent_base_price: Represents the base price in the
        related currency for this entity. This does not include any
        taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are
        associated with this entity. See the associated TaxInfo array
        for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are
        associated with this entity. See the associated FeeInfo array
        for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default
        Currency.
    :ivar approximate_fees: The Converted fee amount in Default
        Currency.
    :ivar provider_code:
    :ivar supplier_code:
    :ivar status: Status of this Journey.
    :ivar provider_reservation_info_ref: Provider reservation reference
        key.
    :ivar passive_provider_reservation_info_ref: Passive provider
        reservation reference key.
    :ivar travel_order: To identify the appropriate travel sequence for
        Air/Car/Hotel/Rail segments/reservations/Journeys based on
        travel dates. This ordering is applicable across the UR not
        provider or traveler specific
    :ivar route_reference: RouteReference is required in seat assignment
        purpose
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    :ivar operation: "Type of exchange. Add - Add new Journey. Update -
        Modify existing Journey. Delete - Remove existing Journey"
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata={
            "name": "RailSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_segment_ref: List[RailSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RailSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    journey_remark: List[JourneyRemark] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRemark",
            "type": "Element",
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
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    origin_station_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        }
    )
    destination_station_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        }
    )
    rail_loc_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    rail_loc_destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        }
    )
    route_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Attribute",
            "max_length": 255,
        }
    )
    journey_direction: Optional[TypeJourneyDirection] = field(
        default=None,
        metadata={
            "name": "JourneyDirection",
            "type": "Attribute",
        }
    )
    journey_duration: Optional[int] = field(
        default=None,
        metadata={
            "name": "JourneyDuration",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
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
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    passive_provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    travel_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        }
    )
    route_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteReference",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 255,
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
    operation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Attribute",
        }
    )


@dataclass
class RailPricingInfo:
    """
    Per traveler type pricing breakdown.

    :ivar rail_fare:
    :ivar rail_fare_ref:
    :ivar rail_booking_info:
    :ivar passenger_type:
    :ivar booking_traveler_ref:
    :ivar key:
    :ivar exchange_amount: The amount to pay to cover the exchange of
        the fare (includes penalties).
    :ivar approximate_exchange_amount:
    :ivar total_price: The total price for this entity including base
        price and all taxes.
    :ivar base_price: Represents the base price for this entity. This
        does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default
        Currency for this entity. This does not include any taxes or
        surcharges.
    :ivar equivalent_base_price: Represents the base price in the
        related currency for this entity. This does not include any
        taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are
        associated with this entity. See the associated TaxInfo array
        for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are
        associated with this entity. See the associated FeeInfo array
        for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default
        Currency.
    :ivar approximate_fees: The Converted fee amount in Default
        Currency.
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare: List[RailFare] = field(
        default_factory=list,
        metadata={
            "name": "RailFare",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_fare_ref: List[RailFareRef] = field(
        default_factory=list,
        metadata={
            "name": "RailFareRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_booking_info: List[RailBookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailBookingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passenger_type: List[TypePassengerType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        }
    )
    approximate_exchange_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateExchangeAmount",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
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


@dataclass
class RailSegmentList:
    """
    List of Rail Segments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment: List[RailSegment] = field(
        default_factory=list,
        metadata={
            "name": "RailSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailJourneyList:
    """
    List of Rail Journeys.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailReservation(BaseReservation):
    """
    The parent container for all Rail booking data.

    :ivar booking_traveler_ref:
    :ivar rail_journey:
    :ivar rail_pricing_info:
    :ivar payment:
    :ivar rail_ticket_info:
    :ivar rail_fare_note_list: List of RailFareNote(s) that is
        referenced by key in RailFare.
    :ivar supplier_locator:
    :ivar booking_status: The Current Status of the rail booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    rail_ticket_info: List[RailTicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailTicketInfo",
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
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    booking_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingStatus",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SearchRailLeg:
    """
    Holds Origin, Destination, and Departure times for a Rail Leg to search for.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "name": "SearchOrigin",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata={
            "name": "SearchDestination",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    rail_segment_list: Optional[RailSegmentList] = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
        }
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata={
            "name": "SearchDepTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata={
            "name": "SearchArvTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_leg_modifiers: Optional[RailLegModifiers] = field(
        default=None,
        metadata={
            "name": "RailLegModifiers",
            "type": "Element",
        }
    )


@dataclass
class TypeRailPricingSolution:
    """
    Common RailPricingSolution container.

    :ivar rail_journey:
    :ivar rail_journey_ref:
    :ivar rail_pricing_info:
    :ivar key:
    :ivar offer_id: OfferID must be included if the RailCreateReq
        contains a price.  If the RailCreateReq is used for the Direct
        Book function, the OfferID is not included.
    :ivar total_price: The total price for this entity including base
        price and all taxes.
    :ivar base_price: Represents the base price for this entity. This
        does not include any taxes or surcharges.
    :ivar approximate_total_price: The Converted total price in Default
        Currency for this entity including base price and all taxes.
    :ivar approximate_base_price: The Converted base price in Default
        Currency for this entity. This does not include any taxes or
        surcharges.
    :ivar equivalent_base_price: Represents the base price in the
        related currency for this entity. This does not include any
        taxes or surcharges.
    :ivar taxes: The aggregated amount of all the taxes that are
        associated with this entity. See the associated TaxInfo array
        for a breakdown of the individual taxes.
    :ivar fees: The aggregated amount of all the fees that are
        associated with this entity. See the associated FeeInfo array
        for a breakdown of the individual fees.
    :ivar services: The total cost for all optional services.
    :ivar approximate_taxes: The Converted tax amount in Default
        Currency.
    :ivar approximate_fees: The Converted fee amount in Default
        Currency.
    :ivar provider_code:
    :ivar supplier_code:
    :ivar host_token_ref: HostTokenRef will reference the value in
        HostTokenList/HostToken @ Key
    :ivar reference: Offer Reference required for Booking(eg.TL).
    """
    class Meta:
        name = "typeRailPricingSolution"

    rail_journey: List[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
    rail_journey_ref: List[RailJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "RailJourneyRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
    rail_pricing_info: List[RailPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
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
    offer_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OfferId",
            "type": "Attribute",
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: Optional[str] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
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
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    host_token_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
        }
    )


@dataclass
class RailExchangeSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_exchange_info: Optional[RailExchangeInfo] = field(
        default=None,
        metadata={
            "name": "RailExchangeInfo",
            "type": "Element",
        }
    )


@dataclass
class RailPricingSolution(TypeRailPricingSolution):
    """
    Contains the fares and segments for a particular offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailSolutionChangedInfo:
    """If RetainReservation is None, this will contain the new values returned from
    the provider.

    If RetainReservation is Price, Schedule, or Both and there is a
    price/schedule change, this will contain the new values that were
    returned from the provider.  If RetainReservation is Price,
    Schedule, or Both and there isn’t a price/schedule change, this
    element will not be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_pricing_solution: Optional[RailPricingSolution] = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: Optional[RailSolutionChangedInfoReasonCode] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )
