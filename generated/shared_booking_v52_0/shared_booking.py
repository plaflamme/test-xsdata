from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.air_v52_0.air import (
    AirPricingAdjustment,
    AirPricingInfo,
    AirPricingPayment,
    AirPricingTicketingModifiers,
    AirSegment,
    AssociatedRemark as AirAirAssociatedRemark,
    AutoPricingInfo,
    AutoSeatAssignment,
    SpecificSeatAssignment,
)
from generated.common_v52_0.common import (
    AccountingRemark,
    ActionStatus,
    BookingSource,
    BookingTraveler,
    CorporateDiscountId,
    CreditCardAuth,
    FormOfPayment,
    GeneralRemark,
    Guarantee,
    HostToken,
    LoyaltyCard,
    Osi,
    ReservationName,
    Ssr,
    TravelComplianceData,
    UnassociatedRemark,
    TypeNonAirReservationRef,
    TypeSegmentRef,
)
from generated.hotel_v52_0.hotel import (
    AssociatedRemark as HotelHotelAssociatedRemark,
    GuestInformation,
    HotelBedding,
    HotelProperty,
    HotelRateDetail,
    HotelRateInfo,
    HotelStay,
    PromotionCode,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class Command:
    """
    The command to pass to the host.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class TypeAirPnrElement(Enum):
    """
    Defines the list of available data types for modifications.
    """
    PAYMENT = "Payment"
    ASSOCIATED_REMARK = "AssociatedRemark"
    TICKETING_MODIFIERS = "TicketingModifiers"
    CREDIT_CARD_AUTHORIZATION = "CreditCardAuthorization"
    SSR = "SSR"
    LOYALTY_CARD = "LoyaltyCard"
    TRAVEL_COMPLIANCE = "TravelCompliance"


class TypeBookingTravelerElement(Enum):
    """
    Defines the list of available data types for modifications.
    """
    BOOKING_TRAVELER = "BookingTraveler"
    PHONE_NUMBER = "PhoneNumber"
    EMAIL = "Email"
    NAME_REMARK = "NameRemark"
    DELIVERY_INFO = "DeliveryInfo"
    ADDRESS = "Address"
    APPLIED_PROFILE = "AppliedProfile"
    CUSTOMIZED_NAME_DATA = "CustomizedNameData"


class TypeHotelPnrElement(Enum):
    """
    Defines the list of available data types for modifications.
    """
    GUARANTEE = "Guarantee"
    ASSOCIATED_REMARK = "AssociatedRemark"
    HOTEL_SPECIAL_REQUEST = "HotelSpecialRequest"
    CORPORATE_DISCOUNT_ID = "CorporateDiscountID"
    TRAVEL_PURPOSE = "TravelPurpose"
    LOYALTY_CARD = "LoyaltyCard"
    TRAVEL_COMPLIANCE = "TravelCompliance"


class TypePnrElement(Enum):
    """
    Defines the list of available data types for modifications.
    """
    FORM_OF_PAYMENT = "FormOfPayment"
    OSI = "OSI"
    ACCOUNTING_REMARK = "AccountingRemark"
    GENERAL_REMARK = "GeneralRemark"
    UNASSOCIATED_REMARK = "UnassociatedRemark"


@dataclass
class TypeTextBlock:
    class Meta:
        name = "typeTextBlock"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )


@dataclass
class AddAirPnrElement:
    """
    Container for PNR elements to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_pricing_payment: List[AirPricingPayment] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 30,
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
    air_pricing_ticketing_modifiers: List[AirPricingTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingTicketingModifiers",
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
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
class AddAirSegment:
    """
    Container for Air Segment to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 8,
        }
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 8,
        }
    )


@dataclass
class AddHotelPnrElement:
    """
    Container for Hotel PNR elements to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

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
            "max_occurs": 99,
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
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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
class AddHotelSegment:
    """
    Container for Hotel Segment to be added.

    :ivar hotel_rate_detail:
    :ivar hotel_property:
    :ivar hotel_stay:
    :ivar hotel_bedding:
    :ivar guest_information:
    :ivar promotion_code: Used to specify promotional code include in
        the booking
    :ivar guarantee:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    hotel_rate_detail: Optional[HotelRateDetail] = field(
        default=None,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    hotel_property: Optional[HotelProperty] = field(
        default=None,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    hotel_stay: Optional[HotelStay] = field(
        default=None,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 4,
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
    promotion_code: Optional[PromotionCode] = field(
        default=None,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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


@dataclass
class AddPnrElement:
    """
    Container for PNR elements to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )


@dataclass
class AddPricing:
    """
    Container for Pricing to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 100,
        }
    )
    auto_pricing_info: List[AutoPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AutoPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 100,
        }
    )


@dataclass
class AddSeats:
    """
    Container for Seats to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    auto_seat_assignment: List[AutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 20,
        }
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 20,
        }
    )


@dataclass
class AddTraveler:
    """
    Container for Travelers or its contents to be added.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 18,
        }
    )


@dataclass
class CommandResponse(TypeTextBlock):
    """The response from the host.

    Usually pre-formatted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class DeleteAirPnrElement:
    """
    Container for Air PNR elements to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: Optional[TypeAirPnrElement] = field(
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
            "required": True,
        }
    )


@dataclass
class DeleteAirSegment:
    """
    Container for Air Segment to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 8,
        }
    )


@dataclass
class DeleteHotelPnrElement:
    """
    Container for Hotel PNR elements to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

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
    element: Optional[TypeHotelPnrElement] = field(
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
            "required": True,
        }
    )


@dataclass
class DeleteHotelSegment:
    """
    Container for Hotel Segment to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    hotel_reservation_ref: Optional[TypeNonAirReservationRef] = field(
        default=None,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DeletePnrElement:
    """
    Container for PNR elements to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: Optional[TypePnrElement] = field(
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
            "required": True,
        }
    )


@dataclass
class DeletePricing:
    """
    Container for Pricing to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_pricing_info_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 8,
        }
    )


@dataclass
class DeleteSeats:
    """
    Container for Seats to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    seat_assignment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SeatAssignmentRef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )


@dataclass
class DeleteTraveler:
    """
    Container for Booking Traveler or its contents to be deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: Optional[TypeBookingTravelerElement] = field(
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
            "required": True,
        }
    )


@dataclass
class UpdateAirPnrElement:
    """
    Container for Air PNR elements to be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_pricing_payment: List[AirPricingPayment] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 30,
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
    air_pricing_ticketing_modifiers: List[AirPricingTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingTicketingModifiers",
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
    air_pricing_adjustment: List[AirPricingAdjustment] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingAdjustment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
class UpdateAirSegment:
    """
    Container for Air Segment to be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 8,
        }
    )


@dataclass
class UpdateHotelPnrElement:
    """
    Container for Hotel PNR elements to be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

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
            "max_occurs": 99,
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
    travel_compliance_data: List[TravelComplianceData] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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
class UpdatePnrElement:
    """
    Container for PNR elements to be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
    osi: List[Osi] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    accounting_remark: List[AccountingRemark] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    unassociated_remark: List[UnassociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )


@dataclass
class UpdateSeats:
    """
    Container for Seats to be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    auto_seat_assignment: List[AutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 20,
        }
    )
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 20,
        }
    )


@dataclass
class UpdateTraveler:
    """
    Container for Travelers or its contents to be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 18,
        }
    )
