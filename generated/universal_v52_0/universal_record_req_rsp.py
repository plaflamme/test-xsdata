from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from generated.air_v52_0.air import (
    AirPricingSolution,
    AirPricingTicketingModifiers,
    AirSegment,
    AirSegmentRef,
    AirSegmentSellFailureInfo,
    AirSolution,
    AirSolutionChangedInfo,
    AssociatedRemark as AirAirAssociatedRemark,
    AutoSeatAssignment,
    HostReservation,
    MerchandisingPricingModifiers,
    OptionalServices,
    PocketItineraryRemark,
    SpecificSeatAssignment,
)
from generated.common_v52_0.common import (
    ActionStatus,
    AgencyPayment,
    AgencySellInfo,
    BookingSource,
    BookingTravelerName,
    ContinuityCheckOverride,
    CreditCard,
    DeliveryInfo,
    Email,
    FileFinishingInfo,
    GeneralRemark,
    Guarantee,
    HostToken,
    HostTokenList,
    Payment,
    PhoneNumber,
    PointOfSale,
    ReservationName,
    ReviewBooking,
    SpecialEquipment,
    SupplierLocator,
    ThirdPartyInformation,
    UrticketStatus,
    TypeErrorInfo,
    TypeRecordStatus,
)
from generated.common_v52_0.common_req_rsp import (
    BaseCreateReservationReq,
    BaseCreateWithFormOfPaymentReq,
    BaseReq,
    BaseRsp,
)
from generated.hotel_v52_0.hotel import (
    AssociatedRemark as HotelHotelAssociatedRemark,
    GuestInformation,
    HotelBedding,
    HotelProperty,
    HotelRateDetail,
    HotelStay,
    PromotionCode,
)
from generated.passive_v52_0.passive import (
    AssociatedRemark as PassivePassiveAssociatedRemark,
    PassiveRemark,
    PassiveSegment,
    PassiveSegmentRef,
)
from generated.rail_v52_0.rail import (
    RailAutoSeatAssignment,
    RailFareNoteList,
    RailPricingSolution,
    RailSolutionChangedInfo,
    RailSpecificSeatAssignment,
)
from generated.universal_v52_0.universal_record import (
    AirReservationCriteria,
    DisplayDetails,
    HotelReservationCriteria,
    ProviderReservationStatus,
    QueueNextModifiers,
    RailReservationCriteria,
    RecordIdentifier,
    SavedTrip,
    SavedTripSearchModifiers,
    SavedTripSearchResult,
    SearchAccount,
    SearchAgent,
    TravelerCriteria,
    UniversalModifyCmd,
    UniversalModifyFailureInfo,
    UniversalRecord,
    UniversalRecordHistorySearchModifiers,
    UniversalRecordHistorySearchResult,
    UniversalRecordSearchModifiers,
    UniversalRecordSearchResult,
    VehicleReservationCriteria,
    TypeRetainReservation,
    TypeSavedTripRecordStatus,
)
from generated.vehicle_v52_0.vehicle import (
    AssociatedRemark as VehicleVehicleAssociatedRemark,
    CollectionAddress,
    DeliveryAddress,
    FlightArrivalInformation,
    PaymentInformation,
    Vehicle,
    VehicleDateLocation,
    VehicleSpecialRequest,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class AirCreateReservationReqCheckPriceVarianceType(Enum):
    PERCENTAGE = "Percentage"
    AMOUNT = "Amount"


class ProviderReservationDivideReqCreateChildUniversalRecord(Enum):
    EXISTING = "Existing"
    NEW = "New"


@dataclass
class AckScheduleChangeReq(BaseReq):
    """
    Request to acknowledge you have received the schedule change notification.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
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
    reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AckScheduleChangeRsp(BaseRsp):
    """
    Return the updated air portion of the Universal Record when accepting the
    Schedule Change.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirCancelReq(BaseReq):
    """Air Cancel request is used to cancel all or part of an AirReservation.

    Given only a locator code, everything within the AirReservation
    would be canceled. If particular segments are specified, then only
    those segments will be canceled.

    :ivar continuity_check_override: Provider: 1G,1V,1P,ACH.
    :ivar air_reservation_locator_code: Provider: 1G,1V,1P,ACH.
    :ivar air_segment: Provider: 1G,1V,1P,ACH.
    :ivar air_segment_ref: Provider: 1G,1V,1P,ACH.
    :ivar file_finishing_info: Provider: 1G,1V,1P,ACH.
    :ivar version: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    continuity_check_override: Optional[ContinuityCheckOverride] = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
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
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AirCancelRsp(BaseRsp):
    """Response to an AirCancelReq.

    AirReservation returned reflects the requested modifications.

    :ivar universal_record: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )


@dataclass
class AirCreateReservationReq(BaseCreateWithFormOfPaymentReq):
    """
    Request to store an air itinerary and create initial PNR.

    :ivar supplier_locator: Provider: 1G,1V,1P,ACH,SDK.
    :ivar third_party_information: Provider: SDK.
    :ivar point_of_sale: Provider: 1G,1V.
    :ivar air_pricing_solution: Provider: 1G,1V,1P,ACH,SDK.
        SplitReservation can include up 16 AirPricingSolutions.
    :ivar action_status: Provider: 1G,1V,1P,ACH,SDK.
    :ivar payment: Provider: 1G,1V,1P,ACH.
    :ivar delivery_info: Provider: ACH.
    :ivar auto_seat_assignment: Provider: 1G,1V,1P.
    :ivar specific_seat_assignment: Provider: 1G,1V,1P,ACH.
    :ivar associated_remark: Provider: 1G,1V,1P,ACH,SDK.
    :ivar pocket_itinerary_remark: Provider: 1P.
    :ivar review_booking: Provider: 1G,1V-Review Booking or Queue
        Minders is to add the reminders in the Provider Reservation
        along with the date time and Queue details. On the date time
        defined in reminders, the message along with the PNR goes to the
        desired Queue.
    :ivar air_pricing_ticketing_modifiers: AirPricing TicketingModifier
        information used to associate Ticketing Modifiers with one or
        more AirPricingInfos/ProviderReservationInfo for 1G,1V,1P
    :ivar retain_reservation: Provider: 1G,1V,1P
    :ivar source:
    :ivar override_mct: Provider: 1G,1V.
    :ivar restrict_waitlist: Restrict Book if it sells a Waitlisted
        AirSegment. Provider: 1G,1V
    :ivar create_passive_for_hold: Creates a background passive segment
        for an ACH hold booking.
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to
        activate the Search Control Console filter for a specific group
        of travelers being served by the agency credential.
    :ivar nscc: Allows the agency to bypass/override the Search Control
        Console rule.
    :ivar check_price_variance_type: Valid values are "Amount" (default)
        or "Percentage".
    :ivar check_price_variance_value: Price variance tolerance in
        currency or percentage. Booking allowed if Price Difference ≤
        Price Variance.
    :ivar split_reservation: Creates multi host PNRs per
        AirPricingSolution if true,Creates single host PNR if false or
        not included in the request.
    :ivar prefer_complete_itinerary: Applicable only for book requests
        with multiple AirPricingSolutions. True – Cancel the booking
        request if there is a booking failure for one of the
        AirPricingSolutions. False – Continue booking other
        AirPricingSolutions even if there is a booking failure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

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
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 16,
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
    payment: List[Payment] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    auto_seat_assignment: List[AutoSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "AutoSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
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
    review_booking: List[ReviewBooking] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    retain_reservation: TypeRetainReservation = field(
        default=TypeRetainReservation.NONE,
        metadata={
            "name": "RetainReservation",
            "type": "Attribute",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    override_mct: bool = field(
        default=False,
        metadata={
            "name": "OverrideMCT",
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
    create_passive_for_hold: bool = field(
        default=False,
        metadata={
            "name": "CreatePassiveForHold",
            "type": "Attribute",
        }
    )
    channel_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        }
    )
    nscc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        }
    )
    check_price_variance_type: AirCreateReservationReqCheckPriceVarianceType = field(
        default=AirCreateReservationReqCheckPriceVarianceType.AMOUNT,
        metadata={
            "name": "CheckPriceVarianceType",
            "type": "Attribute",
        }
    )
    check_price_variance_value: Decimal = field(
        default=Decimal("0.0"),
        metadata={
            "name": "CheckPriceVarianceValue",
            "type": "Attribute",
        }
    )
    split_reservation: bool = field(
        default=False,
        metadata={
            "name": "SplitReservation",
            "type": "Attribute",
        }
    )
    prefer_complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "PreferCompleteItinerary",
            "type": "Attribute",
        }
    )


@dataclass
class AirCreateReservationRsp(BaseRsp):
    """
    :ivar universal_record:
    :ivar air_solution_changed_info: Provider: 1G,1V,1P,ACH.
    :ivar air_segment_sell_failure_info: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )
    air_solution_changed_info: List[AirSolutionChangedInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
class AirMerchandisingFulfillmentReq(BaseReq):
    """This will fulfill the merchandised items as specified in the request.

    The host PNR will be updated with the services and any required
    charges will be added.

    :ivar host_token: Provider: ACH.
    :ivar host_reservation: Provider: 1G,1V,1P,ACH.
    :ivar agency_sell_info: Provider: 1G,1V,1P,ACH.
    :ivar air_solution: Provider: 1G,1V,1P,ACH.
    :ivar credit_card: Provider: 1G,1V,1P,ACH.
    :ivar agency_payment: Provider: ACH
    :ivar optional_services:
    :ivar specific_seat_assignment: Provider: 1G,1V,1P,ACH.
    :ivar general_remark: Provider: 1G,1V,1P,ACH.
    :ivar confirmation_email: Provider: 1G,1V,1P,ACH.
    :ivar merchandising_pricing_modifiers: Used to provide additional
        pricing modifiers. Provider:ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    host_reservation: List[HostReservation] = field(
        default_factory=list,
        metadata={
            "name": "HostReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    agency_sell_info: Optional[AgencySellInfo] = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_solution: Optional[AirSolution] = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        }
    )
    credit_card: Optional[CreditCard] = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    agency_payment: Optional[AgencyPayment] = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
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
    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    confirmation_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationEmail",
            "type": "Element",
        }
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )


@dataclass
class AirMerchandisingFulfillmentRsp(BaseRsp):
    """
    :ivar universal_record: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )


@dataclass
class HotelCancelReq(BaseReq):
    """Cancel request for a hotel booking.

    Given a provider code and a provider locator code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    hotel_property: Optional[HotelProperty] = field(
        default=None,
        metadata={
            "name": "HotelProperty",
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
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        }
    )
    supplier_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
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
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HotelCancelRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )


@dataclass
class HotelCreateReservationReq(BaseCreateWithFormOfPaymentReq):
    """
    Request to create a hotel reservation.

    :ivar email:
    :ivar phone_number:
    :ivar hotel_rate_detail:
    :ivar hotel_property:
    :ivar third_party_information:
    :ivar hotel_stay:
    :ivar guarantee:
    :ivar hotel_special_request:
    :ivar point_of_sale:
    :ivar promotion_code: Used to specify promotional code include in
        the booking
    :ivar booking_source: Specify alternate booking source
    :ivar hotel_bedding:
    :ivar guest_information:
    :ivar associated_remark:
    :ivar reservation_name: If specified then it will be used for GDS
        reservation otherwise first booking traveler will be used.
    :ivar action_status:
    :ivar host_token:
    :ivar review_booking: Review Booking or Queue Minders is to add the
        reminders in the Provider Reservation along with the date time
        and Queue details. On the date time defined in reminders, the
        message along with the PNR goes to the desired Queue.
    :ivar hotel_commission: This element indicates hotel commission
        applied during hotel booking.  Provider supported 1P.
    :ivar user_acceptance: If true, traveler has reviewed and accepted
        all policies, restrictions, and terms and conditions prior to
        booking. Default, false.
    :ivar mandatory_rate_match: If true, hotel will not be booked if
        there is a rate discrepancy.  Default is false. Supported
        providers: 1g,1v,1p.
    :ivar status_code: Hotel Segment Status Code.Supported Providers:1P.
    :ivar booking_confirmation: Hotel Booking Confirmation Number for
        passive hotel segment. Supported Providers:1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    email: List[Email] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_rate_detail: List[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "min_occurs": 1,
            "max_occurs": 99,
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
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    guarantee: Optional[Guarantee] = field(
        default=None,
        metadata={
            "name": "Guarantee",
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
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    booking_source: Optional[BookingSource] = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    associated_remark: List[HotelHotelAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 9999,
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
    action_status: Optional[ActionStatus] = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    review_booking: List[ReviewBooking] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9999,
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
    user_acceptance: bool = field(
        default=False,
        metadata={
            "name": "UserAcceptance",
            "type": "Attribute",
        }
    )
    mandatory_rate_match: bool = field(
        default=False,
        metadata={
            "name": "MandatoryRateMatch",
            "type": "Attribute",
        }
    )
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        }
    )
    booking_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Attribute",
            "max_length": 32,
        }
    )


@dataclass
class HotelCreateReservationRsp(BaseRsp):
    """
    :ivar universal_record:
    :ivar hotel_rate_changed_info: Applicable for 1G, 1V, 1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )
    hotel_rate_changed_info: Optional["HotelCreateReservationRsp.HotelRateChangedInfo"] = field(
        default=None,
        metadata={
            "name": "HotelRateChangedInfo",
            "type": "Element",
        }
    )

    @dataclass
    class HotelRateChangedInfo:
        """
        :ivar hotel_property:
        :ivar hotel_rate_detail:
        :ivar reason: Reason to represent whether rate change in hotel
            rules.Applicable for 1G, 1V, 1P
        """
        hotel_property: Optional[HotelProperty] = field(
            default=None,
            metadata={
                "name": "HotelProperty",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
                "required": True,
            }
        )
        hotel_rate_detail: Optional[HotelRateDetail] = field(
            default=None,
            metadata={
                "name": "HotelRateDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            }
        )
        reason: Optional[str] = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Attribute",
            }
        )


@dataclass
class PnrdivideInfo:
    class Meta:
        name = "PNRDivideInfo"

    booking_traveler_name: List[BookingTravelerName] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
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
class PassiveCancelReq(BaseReq):
    """Request for cancellation of Passive reservation/segment.

    Given the ProviderReservationInfo and PassiveReservationLocatorCode
    , it will cancel the Passive Reservation An optional attribute of
    'Key' will enable cancellation of a particular PassiveSegment in the
    Passive Reservation

    :ivar passive_segment_ref: PassiveSegmentRef element refers the Key
        of the PassiveSegment to be canceled.
    :ivar file_finishing_info:
    :ivar passive_reservation_locator_code: Locator Code of the passive
        reservation to be canceled.
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar version:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    passive_segment_ref: List[PassiveSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        }
    )
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    passive_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveReservationLocatorCode",
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
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PassiveCancelRsp(BaseRsp):
    """Response to a PassiveCancelReq.

    The UniversalRecord returned reflects the requested modifications.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )


@dataclass
class PassiveCreateReservationReq(BaseCreateReservationReq):
    """
    Request to create a passive reservation.

    :ivar supplier_locator:
    :ivar third_party_information:
    :ivar passive_segment:
    :ivar passive_remark:
    :ivar associated_remark:
    :ivar action_status:
    :ivar review_booking: Review Booking or Queue Minders is to add the
        reminders in the Provider Reservation along with the date time
        and Queue details. On the date time defined in reminders, the
        message along with the PNR goes to the desired Queue.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

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
    passive_segment: List[PassiveSegment] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "min_occurs": 1,
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


@dataclass
class PassiveCreateReservationRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProviderReservationDisplayDetailsReq(BaseReq):
    """
    Request to display the addtional details of provider reservation information .

    :ivar provider_code:
    :ivar provider_locator_code:
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
class ProviderReservationDisplayDetailsRsp(BaseRsp):
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
class ProviderReservationDivideReq(BaseReq):
    """
    Request to split a PNR containing atleast 1 air reservation .

    :ivar booking_traveler_ref: Reference Element for Booking Traveler
    :ivar universal_record_locator_code: Represents a valid Universal
        Record locator code
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar create_child_universal_record: Represents the options given to
        the user to store the Child PNR inside existing  UR or in new UR
        after split.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler_ref: List["ProviderReservationDivideReq.BookingTravelerRef"] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
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
    create_child_universal_record: Optional[ProviderReservationDivideReqCreateChildUniversalRecord] = field(
        default=None,
        metadata={
            "name": "CreateChildUniversalRecord",
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
class RailCreateReservationReq(BaseCreateWithFormOfPaymentReq):
    """
    Creates a rail reservation with the host.

    :ivar rail_pricing_solution:
    :ivar payment:
    :ivar rail_fare_note_list: List of RailFareNote(s) that is
        referenced by key in RailFare.
    :ivar host_token_list:
    :ivar rail_auto_seat_assignment:
    :ivar rail_specific_seat_assignment:
    :ivar booking_action_type: the action associated with this booking.
        Four options are: Final (used to book with no ticket issuance)
        FinalTicket (used to book and issue ticket, default if FOP is
        included) Ticket (used to ticket an existing booking) Initiate
        (used for a provisional booking, default if no FOP is included)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    rail_pricing_solution: Optional[RailPricingSolution] = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "required": True,
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
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
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
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
    rail_specific_seat_assignment: List[RailSpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "RailSpecificSeatAssignment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
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


@dataclass
class SavedTripCreateReq(BaseReq):
    """
    Request to create a SavedTrip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: Optional[SavedTrip] = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        }
    )


@dataclass
class SavedTripCreateRsp(BaseRsp):
    """Response to SavedTripCreateReq.

    Contains the SavedTrip successfully created.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: Optional[SavedTrip] = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        }
    )


@dataclass
class SavedTripDeleteReq(BaseReq):
    """
    Request to delete saved Trip.

    :ivar locator_code: Represents a valid Saved Trip locator code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class SavedTripDeleteRsp(BaseRsp):
    """
    Response to delete saved Trip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripModifyReq(BaseReq):
    """
    Request to modify an existing SavedTrip using the LocatorCode of the SavedTrip
    as the SavedTrip identifier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: Optional[SavedTrip] = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        }
    )


@dataclass
class SavedTripModifyRsp(BaseRsp):
    """Response to SavedTripModifyReq.

    Contains the SavedTrip successfully modified.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: Optional[SavedTrip] = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        }
    )


@dataclass
class SavedTripRetrieveReq(BaseReq):
    """
    Request to Retrieve saved Trip based on locatorcode.

    :ivar locator_code: Represents a valid Saved Trip locatorcode.
    :ivar traveler_last_name: Match Traveler Last Name.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    traveler_last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerLastName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )


@dataclass
class SavedTripRetrieveRsp(BaseRsp):
    """Response to SavedTripRetrieveReq.

    Contains the SavedTrip successfully Retrieved.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: Optional[SavedTrip] = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        }
    )


@dataclass
class SavedTripSearchReq(BaseReq):
    """
    Request to retrieve a summary information for reservations under a SavedTrip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip_search_modifiers: Optional[SavedTripSearchModifiers] = field(
        default=None,
        metadata={
            "name": "SavedTripSearchModifiers",
            "type": "Element",
        }
    )
    traveler_criteria: Optional[TravelerCriteria] = field(
        default=None,
        metadata={
            "name": "TravelerCriteria",
            "type": "Element",
        }
    )
    search_agent: Optional[SearchAgent] = field(
        default=None,
        metadata={
            "name": "SearchAgent",
            "type": "Element",
        }
    )
    air_reservation_criteria: Optional[AirReservationCriteria] = field(
        default=None,
        metadata={
            "name": "AirReservationCriteria",
            "type": "Element",
        }
    )
    hotel_reservation_criteria: Optional[HotelReservationCriteria] = field(
        default=None,
        metadata={
            "name": "HotelReservationCriteria",
            "type": "Element",
        }
    )
    vehicle_reservation_criteria: Optional[VehicleReservationCriteria] = field(
        default=None,
        metadata={
            "name": "VehicleReservationCriteria",
            "type": "Element",
        }
    )
    rail_reservation_criteria: Optional[RailReservationCriteria] = field(
        default=None,
        metadata={
            "name": "RailReservationCriteria",
            "type": "Element",
        }
    )
    record_status: Optional[TypeSavedTripRecordStatus] = field(
        default=None,
        metadata={
            "name": "RecordStatus",
            "type": "Attribute",
        }
    )


@dataclass
class SavedTripSearchRsp(BaseRsp):
    """
    Response containing summary information of savedTrip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip_search_result: List[SavedTripSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "SavedTripSearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class UniversalRecordCancelReq(BaseReq):
    """
    Request to Cancel an Universal Record.

    :ivar file_finishing_info:
    :ivar universal_record_locator_code: Represents a valid Universal
        Record locator code
    :ivar version:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class UniversalRecordCancelRsp(BaseRsp):
    """
    Return status for each provider reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    provider_reservation_status: List[ProviderReservationStatus] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationStatus",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class UniversalRecordErrorInfo(TypeErrorInfo):
    """
    :ivar locator_code: Universal Record Locator Code.
    :ivar version: Version of Universal Record.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UniversalRecordHistorySearchReq(BaseReq):
    """
    Search the history of a Universal Record.

    :ivar universal_record_history_search_modifiers:
    :ivar universal_record_locator_code: Represents a valid Universal
        Record locator code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_history_search_modifiers: Optional[UniversalRecordHistorySearchModifiers] = field(
        default=None,
        metadata={
            "name": "UniversalRecordHistorySearchModifiers",
            "type": "Element",
        }
    )
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class UniversalRecordHistorySearchRsp(BaseRsp):
    """
    :ivar universal_record_history_search_result:
    :ivar last_result: Indicate when the search query reached the last
        result.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_history_search_result: List[UniversalRecordHistorySearchResult] = field(
        default_factory=list,
        metadata={
            "name": "UniversalRecordHistorySearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    last_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastResult",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalRecordImportReq(BaseReq):
    """
    Imports a external reservation into a G2 Universal Record.

    :ivar file_finishing_info:
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar universal_record_locator_code: Required if to be imported in
        existing UniversalRecord.
    :ivar return_unmasked_data: When set as True in the request and AAT
        settings are set to display Unmasked details in the host, then
        details will be shown in the response. Only supports credit card
        and debit card. Default value of ReturnUnmaskedData is false.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    return_unmasked_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnUnmaskedData",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalRecordImportRsp(BaseRsp):
    """
    Return the new Universal Record that was created from an external reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UniversalRecordModifyReq(BaseReq):
    """
    Update the universal record.

    :ivar continuity_check_override:
    :ivar record_identifier:
    :ivar universal_modify_cmd:
    :ivar file_finishing_info:
    :ivar queue_next_modifiers:
    :ivar return_record: Either the updated UniversalRecord or Universal
        Record for next on queue should be returned in the response
    :ivar version:
    :ivar override_mct:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    continuity_check_override: Optional[ContinuityCheckOverride] = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    record_identifier: Optional[RecordIdentifier] = field(
        default=None,
        metadata={
            "name": "RecordIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    universal_modify_cmd: List[UniversalModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "UniversalModifyCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    queue_next_modifiers: Optional[QueueNextModifiers] = field(
        default=None,
        metadata={
            "name": "QueueNextModifiers",
            "type": "Element",
        }
    )
    return_record: bool = field(
        default=False,
        metadata={
            "name": "ReturnRecord",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    override_mct: bool = field(
        default=False,
        metadata={
            "name": "OverrideMCT",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalRecordModifyRsp(BaseRsp):
    """
    Return a Universal Record.

    :ivar universal_record:
    :ivar air_solution_changed_info:
    :ivar universal_modify_failure_info:
    :ivar queue_session_token: Queue Session Token to hold session token
        for multiple queue
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )
    air_solution_changed_info: List[AirSolutionChangedInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    universal_modify_failure_info: Optional[UniversalModifyFailureInfo] = field(
        default=None,
        metadata={
            "name": "UniversalModifyFailureInfo",
            "type": "Element",
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
class UniversalRecordRetrieveReq(BaseReq):
    """
    Request to retrieve a summary information for reservations under a Universal
    Record.

    :ivar universal_record_locator_code: Represents a valid Universal
        Recordlocator code
    :ivar provider_reservation_info: Represents a valid Provider
        Reservation/PNR.
    :ivar view_only_ind: True-Retrieves the PNR in UR Format, but
        doesn't create an actual UR in UAPI. False-Creates and Retrieves
        an actual UR. Default false.
    :ivar traveler_last_name: Match Traveler Last Name.
    :ivar traveler_first_name: Represents Traveler First Name for ACH
        PNR Retrieve.
    :ivar return_unmasked_data: When set as True in the request and AAT
        settings are set to display Unmasked details in the host, then
        details will be shown in the response. Only supports credit card
        and debit card. Default value of ReturnUnmaskedData is false.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_reservation_info: Optional["UniversalRecordRetrieveReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
        }
    )
    view_only_ind: bool = field(
        default=False,
        metadata={
            "name": "ViewOnlyInd",
            "type": "Attribute",
        }
    )
    traveler_last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerLastName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )
    traveler_first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerFirstName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        }
    )
    return_unmasked_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnUnmaskedData",
            "type": "Attribute",
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
class UniversalRecordRetrieveRsp(BaseRsp):
    """
    Return a Universal Record.

    :ivar universal_record:
    :ivar updated: Returns true if the underlying reservation has
        changed since it was last accessed
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "required": True,
        }
    )
    updated: bool = field(
        default=False,
        metadata={
            "name": "Updated",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalRecordSearchReq(BaseReq):
    """
    Request to retrieve a summary information for reservations under a Universal
    Record.

    :ivar universal_record_search_modifiers:
    :ivar traveler_criteria:
    :ivar search_agent:
    :ivar air_reservation_criteria:
    :ivar hotel_reservation_criteria:
    :ivar vehicle_reservation_criteria:
    :ivar rail_reservation_criteria:
    :ivar search_account:
    :ivar action_date:
    :ivar record_status:
    :ivar client_id:
    :ivar provider_code:
    :ivar provider_locator_code:
    :ivar external_search_index:
    :ivar restrict_to_profile_id: Used to restrict the search to a
        specific Branch, Branch Group or Agency
    :ivar passive_only: Search for Passives Only
    :ivar ticket_status: Search universal record with Ticket Status
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_search_modifiers: Optional[UniversalRecordSearchModifiers] = field(
        default=None,
        metadata={
            "name": "UniversalRecordSearchModifiers",
            "type": "Element",
        }
    )
    traveler_criteria: Optional[TravelerCriteria] = field(
        default=None,
        metadata={
            "name": "TravelerCriteria",
            "type": "Element",
        }
    )
    search_agent: Optional[SearchAgent] = field(
        default=None,
        metadata={
            "name": "SearchAgent",
            "type": "Element",
        }
    )
    air_reservation_criteria: Optional[AirReservationCriteria] = field(
        default=None,
        metadata={
            "name": "AirReservationCriteria",
            "type": "Element",
        }
    )
    hotel_reservation_criteria: Optional[HotelReservationCriteria] = field(
        default=None,
        metadata={
            "name": "HotelReservationCriteria",
            "type": "Element",
        }
    )
    vehicle_reservation_criteria: Optional[VehicleReservationCriteria] = field(
        default=None,
        metadata={
            "name": "VehicleReservationCriteria",
            "type": "Element",
        }
    )
    rail_reservation_criteria: Optional[RailReservationCriteria] = field(
        default=None,
        metadata={
            "name": "RailReservationCriteria",
            "type": "Element",
        }
    )
    search_account: Optional[SearchAccount] = field(
        default=None,
        metadata={
            "name": "SearchAccount",
            "type": "Element",
        }
    )
    action_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ActionDate",
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
    client_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClientId",
            "type": "Attribute",
        }
    )
    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
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
    restrict_to_profile_id: Optional[object] = field(
        default=None,
        metadata={
            "name": "RestrictToProfileId",
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
    ticket_status: Optional[UrticketStatus] = field(
        default=None,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        }
    )


@dataclass
class UniversalRecordSearchRsp(BaseRsp):
    """
    Response containing summary information for reservations under a Universal
    Record.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_search_result: List[UniversalRecordSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "UniversalRecordSearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    more_results: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VehicleCancelReq(BaseReq):
    """PNR Cancel request for a vehicle booking.

    Given a provider code and a provider locator code. This will cancel
    one or more vehicle segments based on the criteria given.  If more
    than one segment matches, then all matching will be removed.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    vehicle_date_location: Optional[VehicleDateLocation] = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    file_finishing_info: Optional[FileFinishingInfo] = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        }
    )
    supplier_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
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
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VehicleCancelRsp(BaseRsp):
    """Response to a VehicleCancelReq.

    PNR returned reflects the requested modifications.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )


@dataclass
class VehicleCreateReservationReq(BaseCreateWithFormOfPaymentReq):
    """
    :ivar email:
    :ivar phone_number:
    :ivar vehicle_date_location:
    :ivar vehicle:
    :ivar special_equipment:
    :ivar vehicle_special_request:
    :ivar payment_information:
    :ivar point_of_sale:
    :ivar delivery_address: An address to which a rental car should be
        delivered and a phone number associated with the address.
    :ivar collection_address: An address from which a rental car should
        be picked up at the end of a rental period and a phone number
        associated with the address.
    :ivar flight_arrival_information: The flight arrival information
        (airline code and flight number) for the airport/city at which
        the rental car will be picked up
    :ivar guarantee:
    :ivar associated_remark:
    :ivar booking_source: Specify alternate booking source
    :ivar reservation_name: If specified then it will be used for GDS
        reservation otherwise first booking traveler will be used.
    :ivar third_party_information:
    :ivar action_status:
    :ivar review_booking: Review Booking or Queue Minders is to add the
        reminders in the Provider Reservation along with the date time
        and Queue details. On the date time defined in reminders, the
        message along with the PNR goes to the desired Queue.
    :ivar mandatory_rate_match: If true, vehicle will not be booked if
        there is a rate discrepancy.  Default is false. Supported
        providers: 1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    email: List[Email] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_date_location: Optional[VehicleDateLocation] = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "name": "Vehicle",
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
            "max_occurs": 6,
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
    payment_information: Optional[PaymentInformation] = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    point_of_sale: Optional[PointOfSale] = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    flight_arrival_information: Optional[FlightArrivalInformation] = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
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
    associated_remark: List[VehicleVehicleAssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
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
    mandatory_rate_match: bool = field(
        default=False,
        metadata={
            "name": "MandatoryRateMatch",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleCreateReservationRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        }
    )


@dataclass
class TypeRailCreateReservationRsp(BaseRsp):
    class Meta:
        name = "typeRailCreateReservationRsp"

    universal_record: Optional[UniversalRecord] = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    rail_solution_changed_info: List[RailSolutionChangedInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailSolutionChangedInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )


@dataclass
class ChildProviderReservationInfo(PnrdivideInfo):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniversalLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )


@dataclass
class ParentProviderReservationInfo(PnrdivideInfo):
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


@dataclass
class RailCreateReservationRsp(TypeRailCreateReservationRsp):
    """
    Returns rail reservation information with ticketing info etc..
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ProviderReservationDivideRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    parent_provider_reservation_info: Optional[ParentProviderReservationInfo] = field(
        default=None,
        metadata={
            "name": "ParentProviderReservationInfo",
            "type": "Element",
            "required": True,
        }
    )
    child_provider_reservation_info: Optional[ChildProviderReservationInfo] = field(
        default=None,
        metadata={
            "name": "ChildProviderReservationInfo",
            "type": "Element",
            "required": True,
        }
    )
