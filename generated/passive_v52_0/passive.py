from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.common_v52_0.common import (
    BaseReservation,
    BookingTravelerRef,
    SupplierLocator,
    ThirdPartyInformation,
    TypeAssociatedRemarkWithSegmentRef,
    TypeElementStatus,
)

__NAMESPACE__ = "http://www.travelport.com/schema/passive_v52_0"


class AmountType(Enum):
    """
    :cvar DUE: Amount is Due
    :cvar PAID: Amount is Paid
    :cvar TEXT: Amount field has text.
    """
    DUE = "Due"
    PAID = "Paid"
    TEXT = "Text"


@dataclass
class PassiveRemark:
    """
    :ivar text:
    :ivar type_value:
    :ivar passive_segment_ref: The Passive Segment key that this remark
        refers to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        }
    )
    passive_segment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PassiveSegmentRef:
    """
    :ivar key: The Key of Passive Segment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AssociatedRemark(TypeAssociatedRemarkWithSegmentRef):
    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"


@dataclass
class PassiveSegment:
    """
    :ivar amount:
    :ivar supplier_code: Vendor Code. This could have values outside
        what is defined as a carrier. (eg:ZZ as in case for vendor in
        case of Due paid)
    :ivar status:
    :ivar start_date:
    :ivar end_date:
    :ivar origin: Origin for Air, but City for all other Types.
    :ivar destination: This optional, except when Type is Air, then it
        is required.
    :ivar availability_source: Indicates Availability source of
        AirSegment.
    :ivar polled_availability_option: Indicates if carrier has
        inside(polled) availability option.
    :ivar availability_display_type: The type of availability from which
        the segment is sold. E.g., General, Carrier Specific/Direct
        Access, Fare Shop/Optimal Shop, etc.
    :ivar flight_number:
    :ivar class_of_service:
    :ivar number_of_items:
    :ivar segment_type: The Type of Passive segment being entered (
        Car,Hotel,Tour,Air,Surface,Bus,Rail,Cruise,Helicopter,Limousine,Transfers,Miscellaneous,ProcessingFee,Insurance,
        AirTaxi,Currency,Fees,Forms,Group,Include,Leisure,Land,Other,Package,RailRoad,SeaPlane,Software,Supply,Service,
        Theater,Ticket,Transfer,Taxi,Charter,CorporatePlane,UnitedPassive,AccountingInfo,BookingFee,ServiceCharge,ServiceFee,TicketFees
        ,TelexCharge)
    :ivar key: The Key of Passive Segment.
    :ivar vehicle_type: The Type of Vehicle in Passive Segment.
    :ivar passive_provider_reservation_info_ref: Passive Provider
        Reservation reference key.
    :ivar group: Unique Identifier used for grouping together identical
        segments.
    :ivar travel_order: To identify the appropriate travel sequence for
        Air/Car/Hotel/Passive segments/reservations based on travel
        dates. This ordering is applicable across the UR not provider or
        traveler specific
    :ivar provider_segment_order: To identify the appropriate travel
        sequence for Air/Car/Hotel/Rail segments/reservations in the
        provider reservation.
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    :ivar passive_group: Used for grouping 2 sets of identical passive
        segments with different remark information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

    amount: Optional["PassiveSegment.Amount"] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 20,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
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
    availability_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
        }
    )
    polled_availability_option: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolledAvailabilityOption",
            "type": "Attribute",
        }
    )
    availability_display_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityDisplayType",
            "type": "Attribute",
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
        }
    )
    number_of_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfItems",
            "type": "Attribute",
        }
    )
    segment_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SegmentType",
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
    vehicle_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleType",
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
    group: Optional[int] = field(
        default=None,
        metadata={
            "name": "Group",
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
    provider_segment_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
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
    passive_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveGroup",
            "type": "Attribute",
        }
    )

    @dataclass
    class Amount:
        type_value: Optional[AmountType] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        amount_due_paid: Optional[str] = field(
            default=None,
            metadata={
                "name": "AmountDuePaid",
                "type": "Attribute",
            }
        )


@dataclass
class PassiveReservation(BaseReservation):
    """
    The parent container for all passive booking data.

    :ivar supplier_locator:
    :ivar third_party_information:
    :ivar booking_traveler_ref:
    :ivar passive_segment:
    :ivar passive_remark:
    :ivar associated_remark:
    :ivar provider_reservation_info_ref: Provider Reservation reference
        key.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/passive_v52_0"

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
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    passive_segment: List[PassiveSegment] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    passive_remark: List[PassiveRemark] = field(
        default_factory=list,
        metadata={
            "name": "PassiveRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    associated_remark: List[AssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )
