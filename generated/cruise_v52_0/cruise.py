from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from generated.common_v52_0.common import (
    BaseReservation,
    BookingTravelerRef,
    LoyaltyCardRef,
    Payment,
    ProviderReservationInfoRef,
    Segment,
)

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class Balance:
    """
    Indicates balance dates.

    :ivar due_date: Date when deposit or balance is due.
    :ivar received_date: Date when deposit or balance is received, if
        received.
    :ivar credit_card_due_amount: Balance due via credit card payment
    :ivar check_due_amount: Balance due via personal check
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Attribute",
        }
    )
    received_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Attribute",
        }
    )
    credit_card_due_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreditCardDueAmount",
            "type": "Attribute",
        }
    )
    check_due_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckDueAmount",
            "type": "Attribute",
        }
    )


@dataclass
class CabinInfo:
    """
    Cruise Cabin Details.

    :ivar category: Vendor defined Cabin category
    :ivar number: Vendor defined cabin designator Or Cabin Number
    :ivar location: Cabin Category , can be of the following values :
        ''I' - Inside Cabins, 'O' - Outside Cabins, 'M' - Inside and
        Outside Cabins (mixed)
    :ivar relative_location: Position of the cabin relative to the
        layout of the ship, e.g. OUT,AFT,PORT
    :ivar deck_name: Ship's deck on which cabin resides.
    :ivar bed_configuration: Description of the cabin bed configuration
        e.g. TWIN BEDS
    :ivar smoking_indicator: Whether user has specified his smoking
        preference.Can be of the following values : true' - Smoking'
        'false' - Non-smoking
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 1,
        }
    )
    relative_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "RelativeLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 12,
        }
    )
    deck_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeckName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 15,
        }
    )
    bed_configuration: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedConfiguration",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    smoking_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmokingIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class Charges:
    """
    Container for various Charges assocaited with the Cruise Booking.

    :ivar air_charge: Total Amount of Air Charges associated with Cruise
    :ivar optional_charge: Total Amount of Optional Charges associated
        with Cruise
    :ivar waiver_charge: Total Waiver/Insurance charges associated with
        Cruise
    :ivar waiver_charge_type: Use to determine if the amount is Waiver
        Charges or Insurance Charges.(Values - Waiver/Insurance)
    :ivar port_charge: Amount of Port tax associated with Cruise
    :ivar port_charge_description: Text explaining Port charges
    :ivar penalty_charge: Amount of penalty charged with Cruise
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    air_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirCharge",
            "type": "Attribute",
        }
    )
    optional_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptionalCharge",
            "type": "Attribute",
        }
    )
    waiver_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "WaiverCharge",
            "type": "Attribute",
        }
    )
    waiver_charge_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "WaiverChargeType",
            "type": "Attribute",
            "length": 1,
        }
    )
    port_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortCharge",
            "type": "Attribute",
        }
    )
    port_charge_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortChargeDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )
    penalty_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "PenaltyCharge",
            "type": "Attribute",
        }
    )


@dataclass
class Commission:
    """
    Cruise Commission.

    :ivar amount: Total amount of commission associated with cruise
    :ivar miscellaneous_amount: Total amount of other Commission
        associated with cruise
    :ivar miscellaneous_description: Text explaining other Commission
        amount
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    miscellaneous_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiscellaneousAmount",
            "type": "Attribute",
        }
    )
    miscellaneous_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiscellaneousDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )


@dataclass
class CruiseFees:
    """
    Cruise Fees amount.

    :ivar amount: Total amount of fees associated for cruise
    :ivar description: Text explaining fee amount
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )


@dataclass
class CruiseItinerary:
    """
    Contains one day's journey Record.

    :ivar departure_date: The date at which this entity departs.
    :ivar departure_time: The  time at which this entity departs.
    :ivar arrival_date: The date at which this entity arrives at the
        destination.
    :ivar arrival_time: The time at which this entity arrives at the
        destination.
    :ivar boarding_date: The date at which this passenger boards the
        entity.
    :ivar boarding_time: The time at which this passenger boards the
        entity.
    :ivar status: Port of call status .Possible Values (List): SS - New
        item, LL - Waitlisted item, NN - Item is no need/need status, IX
        - Canceled item, HK - Booked item, HL - Booked item, HN - Booked
        item, UC - Unconfirmed item
    :ivar port_name: Port of call name
    :ivar port_indicator: Port of call type. Can be of the following
        values : P - Port of Cal, S - At Sea, E - Embarkation Port, D -
        Disembarkation Port
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ArrivalDate",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    boarding_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BoardingDate",
            "type": "Attribute",
        }
    )
    boarding_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "BoardingTime",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        }
    )
    port_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    port_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortIndicator",
            "type": "Attribute",
            "length": 1,
        }
    )


@dataclass
class Deposit:
    """
    Indicates Deposit dates.

    :ivar amount: Amount of Deposit
    :ivar due_date: Date when deposit or balance is due.
    :ivar received_date: Date when deposit or balance is received, if
        received.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Attribute",
        }
    )
    received_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Attribute",
        }
    )


@dataclass
class Discount:
    """
    Cruise Discount Amount.

    :ivar amount: Amount of Discount
    :ivar description: Text explaining discount amount
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        }
    )


@dataclass
class Due:
    """
    Due balance Amount on Booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class Fare:
    """
    Cruise Fare info.

    :ivar fare_specific: Category is fare specific or not
    :ivar multiple_fare_indicator: Multiple fare are used or not
    :ivar rate_code: Vendor defined rate code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    fare_specific: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FareSpecific",
            "type": "Attribute",
        }
    )
    multiple_fare_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MultipleFareIndicator",
            "type": "Attribute",
        }
    )
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class OptionJourneyDetails:
    """
    Contains PickUp Return Details for that Cruise Feature/Option Service.

    :ivar pick_up_location: IATA/Non-IATA Location Code for Pickup.
        Examples:YVR
    :ivar pick_up_time: PickUp Time
    :ivar pick_up_description: PickUp Location Description
    :ivar pick_up_carrier: The carrier that is marketing this segment.
    :ivar pick_up_flight_number: The flight number under which the
        marketing carrier is marketing carrier is marketing this flight
    :ivar return_location: IATA/Non-IATA Location Code for Drop Off.
        Examples:YVR
    :ivar return_time: Return time
    :ivar return_description: Return Location Description
    :ivar return_carrier: The carrier that is marketing this segment.
    :ivar return_flight_number: The flight number under which the
        marketing carrier is marketing carrier is marketing this flight
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    pick_up_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickUpLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    pick_up_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "PickUpTime",
            "type": "Attribute",
        }
    )
    pick_up_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickUpDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    pick_up_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickUpCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    pick_up_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickUpFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    return_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    return_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ReturnTime",
            "type": "Attribute",
        }
    )
    return_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    return_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    return_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )


@dataclass
class CruiseBookingTravelerRef:
    """
    Reference Element for Booking Traveler and Loyalty cards.

    :ivar loyalty_card_ref:
    :ivar key:
    :ivar waiver_indicator: Indicates Passenger accepts/rejects waiver
        or insurance from vendor.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    loyalty_card_ref: List[LoyaltyCardRef] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
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
        }
    )
    waiver_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WaiverIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class CruiseStay:
    """
    Provides Cruise information.

    :ivar package: Cruise package Details
    :ivar cabin_info:
    :ivar dining_info: Cruise Dining Details
    :ivar ship_name: Ship name
    :ivar duration_of_stay: Length of stay
    :ivar unit_of_stay: Unit of duration of stay in Days or Night(Value
        - Day/Night)
    :ivar booking_date: Date when cruise was booked
    :ivar booking_agent: Name of the travel agent booking itinerary.
    :ivar booking_credit: Credit Paid at the time of booking
    :ivar other_party_conf_nbr: Confirm number of the other parties
        travelling with this party.
    :ivar passenger_origin: Origination city for passenger (not
        necessarily the city from which the cruise embarks).
    :ivar confirmation_number: Confirmation number of cruise segment.
    :ivar linked_conf_number: Linked Cruise Confirmation Number.
    :ivar cancellation_number: Cancellation Number of Cruise Segment.
    :ivar cancellation_date: The date  at which the booking was
        cancelled.
    :ivar cancellation_time: The time at which the booking was
        cancelled.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    package: Optional["CruiseStay.Package"] = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Element",
        }
    )
    cabin_info: Optional[CabinInfo] = field(
        default=None,
        metadata={
            "name": "CabinInfo",
            "type": "Element",
        }
    )
    dining_info: Optional["CruiseStay.DiningInfo"] = field(
        default=None,
        metadata={
            "name": "DiningInfo",
            "type": "Element",
        }
    )
    ship_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    duration_of_stay: Optional[int] = field(
        default=None,
        metadata={
            "name": "DurationOfStay",
            "type": "Attribute",
        }
    )
    unit_of_stay: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitOfStay",
            "type": "Attribute",
        }
    )
    booking_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    booking_agent: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingAgent",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 12,
        }
    )
    booking_credit: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingCredit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    other_party_conf_nbr: Optional[int] = field(
        default=None,
        metadata={
            "name": "OtherPartyConfNbr",
            "type": "Attribute",
        }
    )
    passenger_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerOrigin",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    confirmation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    linked_conf_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinkedConfNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    cancellation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancellationNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    cancellation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CancellationDate",
            "type": "Attribute",
        }
    )
    cancellation_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "CancellationTime",
            "type": "Attribute",
        }
    )

    @dataclass
    class Package:
        """
        :ivar name: Cruise package Name
        :ivar identifier: Vendor Package/Tour identifier
        :ivar passenger_count: Number in party
        :ivar package_identifier: Vendor Package/Tour Identifier
        """
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 30,
            }
        )
        identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "Identifier",
                "type": "Attribute",
                "max_length": 30,
            }
        )
        passenger_count: Optional[int] = field(
            default=None,
            metadata={
                "name": "PassengerCount",
                "type": "Attribute",
            }
        )
        package_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "PackageIdentifier",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 14,
            }
        )

    @dataclass
    class DiningInfo:
        """
        :ivar seating: Seating Arrangement. Can be of the following
            values : '1' - First seating, '2' - Second seating
        :ivar status: Status of this dining
        :ivar table_size: Size of the table in number of persons
        """
        seating: Optional[str] = field(
            default=None,
            metadata={
                "name": "Seating",
                "type": "Attribute",
                "length": 1,
            }
        )
        status: Optional[str] = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Attribute",
                "length": 2,
                "white_space": "collapse",
            }
        )
        table_size: Optional[int] = field(
            default=None,
            metadata={
                "name": "TableSize",
                "type": "Attribute",
            }
        )


@dataclass
class OptionalService:
    """
    Featues/Optionals supported with the cruise booked.

    :ivar option_journey_details: Contains PickUp Return Details for
        that Cruise Option Service.
    :ivar booking_traveler_ref:
    :ivar feature_type: Type of Optional Service. F: Feature, O: Option
    :ivar status: Status of of the Optional Service
    :ivar quantity: Number of Features/Options Requested.
    :ivar provider_defined_type: Unique ID on vendors system
    :ivar description: Descriptive Name of Feature or Option
    :ivar start_date: Feature/Option Begin Date
    :ivar end_date: Feature/Option End Date
    :ivar booking_date: Date Cruise Booked
    :ivar set_identifier: Feature/Option Unique ID Examples: B2NOXFR
    :ivar set_name: Feature/Option Set Name Examples: PRE-CRUISE
    :ivar total_price: Feature/Option Price
    :ivar transport_indicator: Whether Features/ Options Affects
        TransportationIndicator. True - This Feature or Option group
        affects transportation False - This Feature or Option group does
        not affect transportation.
    :ivar air_city_indicator: Feature/option is air or city dependent.
    :ivar purchase_indicator: Option purchased by someone other than the
        passenger
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    option_journey_details: Optional[OptionJourneyDetails] = field(
        default=None,
        metadata={
            "name": "OptionJourneyDetails",
            "type": "Element",
        }
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    feature_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Attribute",
            "required": True,
            "length": 1,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )
    provider_defined_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )
    booking_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    set_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SetIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    set_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SetName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    total_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    transport_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransportIndicator",
            "type": "Attribute",
        }
    )
    air_city_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirCityIndicator",
            "type": "Attribute",
        }
    )
    purchase_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PurchaseIndicator",
            "type": "Attribute",
        }
    )


@dataclass
class CruisePricingInfo:
    """Cruise pricing Information.

    Contains all related pricing data for travelers.

    :ivar fare:
    :ivar charges:
    :ivar discount:
    :ivar deposit:
    :ivar balance:
    :ivar commission:
    :ivar cruise_fees:
    :ivar cruise_booking_traveler_ref:
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
    :ivar net_fare: Net Fare amount (Base price plus
        miscellaneouscharges less discounts)
    :ivar received_amount: Amount of money Recieved
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    fare: Optional[Fare] = field(
        default=None,
        metadata={
            "name": "Fare",
            "type": "Element",
        }
    )
    charges: Optional[Charges] = field(
        default=None,
        metadata={
            "name": "Charges",
            "type": "Element",
        }
    )
    discount: List[Discount] = field(
        default_factory=list,
        metadata={
            "name": "Discount",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    deposit: List[Deposit] = field(
        default_factory=list,
        metadata={
            "name": "Deposit",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    balance: Optional[Balance] = field(
        default=None,
        metadata={
            "name": "Balance",
            "type": "Element",
        }
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        }
    )
    cruise_fees: Optional[CruiseFees] = field(
        default=None,
        metadata={
            "name": "CruiseFees",
            "type": "Element",
        }
    )
    cruise_booking_traveler_ref: List[CruiseBookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "CruiseBookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
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
    net_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetFare",
            "type": "Attribute",
        }
    )
    received_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceivedAmount",
            "type": "Attribute",
        }
    )


@dataclass
class CruiseSegment(Segment):
    """
    An Cruise marketable travel segment.

    :ivar cruise_stay:
    :ivar vendor: Cruise Vendor Code.
    :ivar vendor_name: Cruise Vendor Name.
    :ivar origin: The location code for the origin of cruise segment.
    :ivar destination: The location code for the destination of cruise
        segment.
    :ivar departure_time: The date and time at which this cruise segment
        departs from the origin.
    :ivar arrival_time: The date and time at which this cruise segment
        arrives at the destination.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    cruise_stay: Optional[CruiseStay] = field(
        default=None,
        metadata={
            "name": "CruiseStay",
            "type": "Element",
            "required": True,
        }
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )
    vendor_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )


@dataclass
class CruiseReservation(BaseReservation):
    """
    The parent container for all cruise booking data.

    :ivar cruise_segment:
    :ivar cruise_itinerary:
    :ivar cruise_pricing_info: Cruise pricing Information. Contains all
        related pricing data for travelers.
    :ivar optional_service:
    :ivar booking_traveler_ref:
    :ivar provider_reservation_info_ref:
    :ivar payment:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    cruise_segment: Optional[CruiseSegment] = field(
        default=None,
        metadata={
            "name": "CruiseSegment",
            "type": "Element",
        }
    )
    cruise_itinerary: List[CruiseItinerary] = field(
        default_factory=list,
        metadata={
            "name": "CruiseItinerary",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    cruise_pricing_info: Optional[CruisePricingInfo] = field(
        default=None,
        metadata={
            "name": "CruisePricingInfo",
            "type": "Element",
        }
    )
    optional_service: List[OptionalService] = field(
        default_factory=list,
        metadata={
            "name": "OptionalService",
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
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    provider_reservation_info_ref: Optional[ProviderReservationInfoRef] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
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
            "max_occurs": 999,
        }
    )
