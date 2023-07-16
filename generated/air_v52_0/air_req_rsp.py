from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from generated.air_v52_0.air import (
    ApisrequirementsList,
    AirExchangeBundle,
    AirExchangeBundleTotal,
    AirExchangeModifiers,
    AirExchangeMulitQuoteList,
    AirFareDisplayModifiers,
    AirFareDisplayRuleKey,
    AirFareRulesModifier,
    AirItinerary,
    AirItinerarySolution,
    AirPricePointList,
    AirPriceResult,
    AirPricingCommand,
    AirPricingModifiers,
    AirPricingSolution,
    AirRefundBundle,
    AirRefundModifiers,
    AirSearchModifiers,
    AirSegment,
    AirSegmentList,
    AirSegmentTicketingModifiers,
    AirSolution,
    AirSolutionChangedInfo,
    AirTicketingModifiers,
    AlternateLocationDistanceList,
    AlternateRouteList,
    BookingCode,
    Brand,
    Co2Emissions,
    ContractCode,
    DetailedBillingInformation,
    Emdinfo,
    EmdsummaryInfo,
    Etr,
    EmbargoList,
    Enumeration,
    ExchangeEligibilityInfo,
    ExpertSolutionList,
    FareBasis,
    FareDisplay,
    FareInfoList,
    FareInfoMessage,
    FareInfoRef,
    FareNoteList,
    FareRemarkList,
    FareRule,
    FareRuleKey,
    FareRuleLookup,
    FareRulesFilterCategory,
    FareType,
    FaxDetailsInformation,
    FlexExploreModifiers,
    FlightDetailsList,
    FlightInfo,
    FlightInfoCriteria,
    FlightTimeDetail,
    FlightTimeTableCriteria,
    HostReservation,
    HostTokenList,
    IncludeAddlBookingCodeInfo,
    IssuanceModifiers,
    JourneyData,
    MerchandisingAvailabilityDetails,
    MerchandisingDetails,
    MerchandisingPricingModifiers,
    OfferAvailabilityModifiers,
    OptionalServiceModifiers,
    OptionalServices,
    OriginalItineraryDetails,
    Pcc,
    PersonNameSearch,
    PrePayProfileInfo,
    RepricingModifiers,
    RouteList,
    Rows,
    SearchAirLeg,
    SearchTraveler,
    SeatInformation,
    SelectionModifiers,
    SpecificSeatAssignment,
    SplitTicketingSearch,
    Tcr,
    TcrrefundBundle,
    TicketFailureInfo,
    VoidDocumentInfo,
    VoidResultInfo,
    WaiverCode,
    TypeAirReservationWithFop,
    TypeApplicableSegment,
    TypeFailureInfo,
    TypeFareRuleType,
    TypeMileOrRouteBasedFare,
    TypeTicketFailureInfo,
    TypeTicketingModifiersRef,
)
from generated.common_v52_0.common import (
    AccountCode,
    AddSvc,
    AgencySellInfo,
    BookingTraveler,
    BookingTravelerRef,
    CabinClass,
    Carrier,
    Commission,
    FormOfPayment,
    FormOfPaymentRef,
    HostToken,
    LoyaltyCard,
    Mco,
    OverridePcc,
    PaymentRestriction,
    PointOfCommencement,
    PointOfSale,
    ProviderReservationDetail,
    Remark,
    Ssr,
    Ssrinfo,
    SearchPassenger,
    ServiceFeeInfo,
    TypeDistance,
    TypePassengerType,
)
from generated.common_v52_0.common_req_rsp import (
    BaseCoreReq,
    BaseCoreSearchReq,
    BaseReq,
    BaseRsp,
    BaseSearchReq,
    BaseSearchRsp,
)
from generated.rail_v52_0.rail import (
    RailFareIdlist,
    RailFareList,
    RailFareNoteList,
    RailJourneyList,
    RailPricingSolution,
    RailSegmentList,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SearchSpecificAirSegment:
    """
    :ivar departure_time: The date and time at which this entity
        departs. This does not include time zone information since it
        can be derived from the origin location.
    :ivar carrier: The carrier that is marketing this segment
    :ivar flight_number: The flight number under which the marketing
        carrier is marketing this flight
    :ivar origin: The IATA location code for this origination of this
        entity.
    :ivar destination: The IATA location code for this destination of
        this entity.
    :ivar segment_index: The sequential AirSegment number that this
        segment connected to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    departure_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    segment_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
        }
    )


@dataclass
class AirBaseReq(BaseReq):
    """
    Context for Requests and Responses.
    """


@dataclass
class AirExchangeEligibilityReq(BaseReq):
    """
    Request to determine if the fares in an itinerary are exchangeable.

    :ivar provider_reservation_info: Provider:1P - Represents a valid
        Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar type_value: Type choices are "Detail" or "Summary"  Default
        will be Summary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    provider_reservation_info: Optional["AirExchangeEligibilityReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "required": True,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
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
class AirExchangeEligibilityRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    exchange_eligibility_info: Optional[ExchangeEligibilityInfo] = field(
        default=None,
        metadata={
            "name": "ExchangeEligibilityInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirExchangeQuoteRsp(BaseRsp):
    """
    :ivar ticket_number:
    :ivar air_pricing_solution: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle_total:
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P
    :ivar host_token: Encrypted data from the host. Required to send the
        HostToken from the AirExchangeQuoteRsp in the AirExchangeReq.
        Providers ACH/1G/1V/1P.
    :ivar optional_services: Provider: ACH.
    :ivar fare_rule: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
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
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeReq(BaseReq):
    """
    Request to exchange an itinerary.

    :ivar air_reservation_locator_code: Identifies the PNR locator code.
        Providers ACH/1G/1V/1P
    :ivar ticket_number:
    :ivar specific_seat_assignment: Identifies the standard seat.
        Providers ACH/1G/1V/1P
    :ivar air_pricing_solution: Providers ACH/1G/1V/1P.
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar air_exchange_bundle_total: Provider: 1G/1V/1P/1S/1A.
    :ivar air_exchange_bundle: Bundle exchange, pricing, and penalty
        information. Providers ACH/1G/1V/1P.
    :ivar host_token: Encrypted data from the host. Required to send the
        HostToken from the AirExchangeQuoteRsp in the AirExchangeReq.
        Providers ACH/1G/1V/1P
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Form of Payment for any additional collection
        charges for the Exchange. For ACH, most carriers will only allow
        refund amounts to the original form of payment. Providers
        ACH/1G/1V/1P
    :ivar form_of_payment_ref: Provider: ACH-Universal Record reference
        to Form of Payment for any Additional Collection charges or
        Refund due for the itinerary exchange
    :ivar ssrinfo: Providers ACH, 1G, 1V, 1P.
    :ivar add_svc: 1P - Add SVC segments to collect additional fee
    :ivar return_reservation: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
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
    specific_seat_assignment: List[SpecificSeatAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificSeatAssignment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
        }
    )
    air_exchange_bundle_total: Optional[AirExchangeBundleTotal] = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
        }
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
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
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
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
    form_of_payment_ref: Optional[FormOfPaymentRef] = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    ssrinfo: List[Ssrinfo] = field(
        default_factory=list,
        metadata={
            "name": "SSRInfo",
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
    return_reservation: bool = field(
        default=False,
        metadata={
            "name": "ReturnReservation",
            "type": "Attribute",
        }
    )


@dataclass
class AirExchangeRsp(BaseRsp):
    """
    :ivar ticket_number:
    :ivar booking_traveler: Provider: ACH.
    :ivar air_reservation: Provider: ACH.
    :ivar exchange_failure_info: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    air_reservation: Optional[TypeAirReservationWithFop] = field(
        default=None,
        metadata={
            "name": "AirReservation",
            "type": "Element",
        }
    )
    exchange_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangeFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeTicketingReq(BaseReq):
    """Request to ticket an exchanged itinerary.

    Providers 1G, 1V, 1P.

    :ivar air_reservation_locator_code: Identifies the PNR to ticket.
        Providers 1G, 1V, 1P.
    :ivar ticket_number: Ticket number to reissue. Providers 1G, 1V, 1P.
    :ivar ticketing_modifiers_ref: Provider: 1P-Reference to a shared
        list of Ticketing Modifiers. This is supported for Worldspan
        provider only. When AirPricingInfoRef is used along with
        TicketingModifiersRef means that particular TicketingModifiers
        will to be applied while ticketing the Stored fare corresponding
        to the AirPricingInfo. Absence of AirPricingInfoRef means that
        particular TicketingModifiers will be applied to all Stored
        fares which are requested to be ticketed.
    :ivar waiver_code:
    :ivar detailed_billing_information: Providers 1G, 1V, 1P.
    :ivar air_ticketing_modifiers: Provider: 1G,1V,1P.
    :ivar bulk_ticket: Providers 1G, 1V, 1P.
    :ivar change_fee_on_ticket: Applies the change fee/penalty to the
        original form of payment. Providers: 1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
            "min_length": 1,
            "max_length": 13,
        }
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    change_fee_on_ticket: bool = field(
        default=True,
        metadata={
            "name": "ChangeFeeOnTicket",
            "type": "Attribute",
        }
    )


@dataclass
class AirExchangeTicketingRsp(BaseRsp):
    """
    Response to reissue a ticket.

    :ivar air_solution_changed_info:
    :ivar etr: Provider 1G, 1V, 1P.
    :ivar ticket_failure_info: Provider 1G, 1V, 1P.
    :ivar detailed_billing_information: Providers 1G, 1V, 1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_solution_changed_info: Optional[AirSolutionChangedInfo] = field(
        default=None,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
        }
    )
    etr: Optional[Etr] = field(
        default=None,
        metadata={
            "name": "ETR",
            "type": "Element",
        }
    )
    ticket_failure_info: Optional[TicketFailureInfo] = field(
        default=None,
        metadata={
            "name": "TicketFailureInfo",
            "type": "Element",
        }
    )
    detailed_billing_information: Optional[DetailedBillingInformation] = field(
        default=None,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
        }
    )


@dataclass
class AirFareDisplayReq(BaseReq):
    """
    Request to display a tariff for based on origin, destination, and other
    options.

    :ivar fare_type: Provider: 1G,1V,1P.
    :ivar passenger_type: Provider: 1G,1V,1P.
    :ivar booking_code: Provider: 1G,1V,1P.
    :ivar include_addl_booking_code_info: Provider: 1G,1V,1P.
    :ivar fare_basis: Provider: 1G,1V,1P.
    :ivar carrier: Provider: 1G,1V,1P.
    :ivar account_code: Provider: 1G,1V,1P.
    :ivar contract_code: Provider: 1G,1V.
    :ivar air_fare_display_modifiers: Provider: 1G,1V,1P.
    :ivar point_of_sale: Provider: 1G,1V.
    :ivar air_fare_display_rule_key: Provider: 1G,1V,1P.
    :ivar origin: Provider: 1G,1V,1P.
    :ivar destination: Provider: 1G,1V,1P.
    :ivar provider_code: Provider: 1G,1V,1P.
    :ivar include_mile_route_information: Provider: 1G,1V,1P-Used to
        request Mile/Route Information in follow on (Mile, Route, Both)
    :ivar un_saleable_fares_only: Provider: 1G,1V,1P-Used to request
        unsaleable fares only also known as place of sale fares.
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to
        activate the Search Control Console filter for a specific group
        of travelers being served by the agency credential.
    :ivar nscc: 1 to 3 numeric that define a Search Control Console
        filter.This attribute is used to override that filter.
    :ivar return_mm: If this attribute is set to true, Fare Control
        Manager processing will be invoked.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_type: List[FareType] = field(
        default_factory=list,
        metadata={
            "name": "FareType",
            "type": "Element",
            "max_occurs": 5,
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
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    include_addl_booking_code_info: Optional[IncludeAddlBookingCodeInfo] = field(
        default=None,
        metadata={
            "name": "IncludeAddlBookingCodeInfo",
            "type": "Element",
        }
    )
    fare_basis: Optional[FareBasis] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Element",
        }
    )
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
        }
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    contract_code: Optional[ContractCode] = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Element",
        }
    )
    air_fare_display_modifiers: Optional[AirFareDisplayModifiers] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayModifiers",
            "type": "Element",
        }
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
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
    include_mile_route_information: Optional[TypeMileOrRouteBasedFare] = field(
        default=None,
        metadata={
            "name": "IncludeMileRouteInformation",
            "type": "Attribute",
        }
    )
    un_saleable_fares_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnSaleableFaresOnly",
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
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        }
    )


@dataclass
class AirFareDisplayRsp(BaseRsp):
    """
    Response to an AirFareDisplayReq.

    :ivar fare_display: Provider: 1G,1V,1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_display: List[FareDisplay] = field(
        default_factory=list,
        metadata={
            "name": "FareDisplay",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirFareRulesReq(BaseReq):
    """
    Request to display the full text fare rules.

    :ivar air_reservation_selector: Provider: 1G,1V,1P,ACH-Parameters to
        use for a fare rule lookup associated with an Air Reservation
        Locator Code
    :ivar fare_rule_lookup: Used to look up fare rules based on the
        origin, destination, and carrier of the air segment, the fare
        basis code and the provider code.  Providers: 1P.
    :ivar fare_rule_key: Used to look up fare rules based on a fare rule
        key. Providers: 1G, 1V, 1P, ACH.
    :ivar air_fare_display_rule_key: Provider: 1G,1V,1P.
    :ivar air_fare_rules_modifier: Provider: 1G,1V.
    :ivar fare_rules_filter_category: Structured Fare Rules Filter if
        requested will return rules for requested categories in the
        response. Applicable for providers 1G, 1V.
    :ivar fare_rule_type: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_selector: Optional["AirFareRulesReq.AirReservationSelector"] = field(
        default=None,
        metadata={
            "name": "AirReservationSelector",
            "type": "Element",
        }
    )
    fare_rule_lookup: Optional[FareRuleLookup] = field(
        default=None,
        metadata={
            "name": "FareRuleLookup",
            "type": "Element",
        }
    )
    fare_rule_key: List[FareRuleKey] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleKey",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_fare_display_rule_key: Optional[AirFareDisplayRuleKey] = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        }
    )
    air_fare_rules_modifier: Optional[AirFareRulesModifier] = field(
        default=None,
        metadata={
            "name": "AirFareRulesModifier",
            "type": "Element",
        }
    )
    fare_rules_filter_category: List["AirFareRulesReq.FareRulesFilterCategory"] = field(
        default_factory=list,
        metadata={
            "name": "FareRulesFilterCategory",
            "type": "Element",
            "max_occurs": 16,
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.LONG,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        }
    )

    @dataclass
    class FareRulesFilterCategory:
        """
        :ivar category_code: Structured Fare Rules can be requested for
            "ADV", "MIN", "MAX",  "STP", and "CHG".
        :ivar fare_info_ref: Key reference for multiple fare rule
        """
        category_code: List[object] = field(
            default_factory=list,
            metadata={
                "name": "CategoryCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 35,
            }
        )
        fare_info_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "FareInfoRef",
                "type": "Attribute",
            }
        )

    @dataclass
    class AirReservationSelector:
        """
        :ivar fare_info_ref:
        :ivar air_reservation_locator_code: The Air Reservation locator
            code which is an unique identifier for the reservation
        """
        fare_info_ref: List[FareInfoRef] = field(
            default_factory=list,
            metadata={
                "name": "FareInfoRef",
                "type": "Element",
                "max_occurs": 999,
            }
        )
        air_reservation_locator_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AirReservationLocatorCode",
                "type": "Attribute",
                "required": True,
                "min_length": 5,
                "max_length": 8,
            }
        )


@dataclass
class AirFareRulesRsp(BaseRsp):
    """
    Response to an AirFareRuleReq.

    :ivar fare_rule: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirMerchandisingDetailsReq(BaseReq):
    """
    Request to retrieve brand details and optional services included in the brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    merchandising_details: Optional[MerchandisingDetails] = field(
        default=None,
        metadata={
            "name": "MerchandisingDetails",
            "type": "Element",
        }
    )
    optional_service_modifiers: Optional[OptionalServiceModifiers] = field(
        default=None,
        metadata={
            "name": "OptionalServiceModifiers",
            "type": "Element",
        }
    )
    merchandising_availability_details: Optional[MerchandisingAvailabilityDetails] = field(
        default=None,
        metadata={
            "name": "MerchandisingAvailabilityDetails",
            "type": "Element",
        }
    )


@dataclass
class AirMerchandisingDetailsRsp(BaseRsp):
    """
    Response for retrieved brand details and optional services included in them.

    :ivar optional_services:
    :ivar brand:
    :ivar unassociated_booking_code_list: Lists classes of service by
        segment sent in the request which are not associated to a brand.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    unassociated_booking_code_list: Optional["AirMerchandisingDetailsRsp.UnassociatedBookingCodeList"] = field(
        default=None,
        metadata={
            "name": "UnassociatedBookingCodeList",
            "type": "Element",
        }
    )

    @dataclass
    class UnassociatedBookingCodeList:
        applicable_segment: List[TypeApplicableSegment] = field(
            default_factory=list,
            metadata={
                "name": "ApplicableSegment",
                "type": "Element",
                "max_occurs": 99,
            }
        )


@dataclass
class AirMerchandisingOfferAvailabilityReq(BaseReq):
    """
    Check with the supplier whether or not the reservation or air solution supports
    any merchandising offerings.

    :ivar agency_sell_info: Provider: 1G,1V,1P,ACH.
    :ivar air_solution: Provider: 1G,1V,1P,ACH.
    :ivar host_reservation: Provider: 1G,1V,1P,ACH.
    :ivar offer_availability_modifiers: Provider: 1G,1V,1P,ACH.
    :ivar merchandising_pricing_modifiers: Used to provide additional
        pricing modifiers. Provider:ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
        }
    )
    host_reservation: List[HostReservation] = field(
        default_factory=list,
        metadata={
            "name": "HostReservation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    offer_availability_modifiers: List[OfferAvailabilityModifiers] = field(
        default_factory=list,
        metadata={
            "name": "OfferAvailabilityModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
        }
    )


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp):
    """
    Contains the merchandising offerings for the given passenger and itinerary.

    :ivar air_solution: Provider: 1G,1V,1P,ACH.
    :ivar remark: Provider: 1G,1V,1P,ACH.
    :ivar optional_services:
    :ivar embargo_list:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_solution: Optional[AirSolution] = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
            "required": True,
        }
    )
    remark: Optional[Remark] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    embargo_list: Optional[EmbargoList] = field(
        default=None,
        metadata={
            "name": "EmbargoList",
            "type": "Element",
        }
    )


@dataclass
class AirPrePayReq(BaseReq):
    """
    Flight Pass Request.

    :ivar list_search: Provider: ACH.
    :ivar pre_pay_retrieve: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    list_search: Optional["AirPrePayReq.ListSearch"] = field(
        default=None,
        metadata={
            "name": "ListSearch",
            "type": "Element",
        }
    )
    pre_pay_retrieve: Optional["AirPrePayReq.PrePayRetrieve"] = field(
        default=None,
        metadata={
            "name": "PrePayRetrieve",
            "type": "Element",
        }
    )

    @dataclass
    class ListSearch:
        """
        :ivar person_name_search: Customer name detail for searching
            flight pass content.
        :ivar loyalty_card: Customer loyalty card for searching flight
            pass content.
        :ivar start_from_result: Start index of the section of flight
            pass numbers that is being requested.
        :ivar max_results: Max Number of Flight Passes being requested
            for.
        """
        person_name_search: Optional[PersonNameSearch] = field(
            default=None,
            metadata={
                "name": "PersonNameSearch",
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
        start_from_result: Optional[int] = field(
            default=None,
            metadata={
                "name": "StartFromResult",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
            }
        )
        max_results: Optional[int] = field(
            default=None,
            metadata={
                "name": "MaxResults",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 200,
            }
        )

    @dataclass
    class PrePayRetrieve:
        """
        :ivar id: Pre pay id to retrieved,example flight pass  number
        :ivar type_value: Pre pay id type,example 'FlightPass'
        """
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 36,
            }
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )


@dataclass
class AirPrePayRsp(BaseRsp):
    """
    Flight Pass Response.

    :ivar pre_pay_profile_info: Provider: ACH.
    :ivar max_results: Provider: ACH-Max Number of Flight Passes being
        returned.
    :ivar more_indicator: Provider: ACH-Indicates if there are more
        flight passes to be offered
    :ivar more_data_start_index: Provider: ACH-Indicates start index of
        the next flight Passes
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    pre_pay_profile_info: List[PrePayProfileInfo] = field(
        default_factory=list,
        metadata={
            "name": "PrePayProfileInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    max_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    more_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreIndicator",
            "type": "Attribute",
        }
    )
    more_data_start_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoreDataStartIndex",
            "type": "Attribute",
        }
    )


@dataclass
class AirRefundQuoteReq(BaseReq):
    """
    Request to quote a refund for an itinerary.

    :ivar ticket_number: Provider: ACH.
    :ivar tcrnumber: Provider: ACH-The identifying number for a
        Ticketless Air Reservation
    :ivar air_refund_modifiers: Provider: ACH.
    :ivar host_token: Provider: ACH.
    :ivar provider_reservation_info: Provider: 1P - Represents a valid
        Provider Reservation/PNR whose itinerary is to be requested
    :ivar ignore: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

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
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_refund_modifiers: Optional[AirRefundModifiers] = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
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
    provider_reservation_info: List["AirRefundQuoteReq.ProviderReservationInfo"] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ignore: bool = field(
        default=False,
        metadata={
            "name": "Ignore",
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
class AirRefundQuoteRsp(BaseRsp):
    """
    :ivar air_refund_bundle:
    :ivar tcrrefund_bundle: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "TCRRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirRefundReq(BaseReq):
    """
    Request to refund an itinerary for the amount previously quoted.

    :ivar air_refund_bundle: Provider: ACH.
    :ivar tcrrefund_bundle: Provider: ACH.
    :ivar air_refund_modifiers:
    :ivar commission: Provider: ACH.
    :ivar form_of_payment: Provider: ACH-Form of Payment for any
        Additional Collection charges for the Refund.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_refund_bundle: List[AirRefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcrrefund_bundle: List[TcrrefundBundle] = field(
        default_factory=list,
        metadata={
            "name": "TCRRefundBundle",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_refund_modifiers: Optional[AirRefundModifiers] = field(
        default=None,
        metadata={
            "name": "AirRefundModifiers",
            "type": "Element",
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
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


@dataclass
class AirRefundRsp(BaseRsp):
    """
    :ivar etr: Provider: ACH.
    :ivar tcr: Provider: ACH.
    :ivar refund_failure_info: Provider: ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata={
            "name": "TCR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    refund_failure_info: List[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "RefundFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirRepriceRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirRetrieveDocumentReq(BaseReq):
    """Retrieve the post booking information for a PNR.

    ETRs will be returned for standard carriers. TCRs will be returned
    for Ticketless carriers. If the locator is send on a standard
    carrier, all ETRs will be retrieved.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P.
    :ivar ticket_number: Provider: 1G,1V,1P.
    :ivar tcrnumber: Provider: 1G,1V,1P-The identifying number for a
        Ticketless Air Reservation.
    :ivar return_restrictions: Will return a response which includes a
        set of restrictions associated with the document.
    :ivar return_pricing: Provider: 1G,1V,1P-Will return a response
        which includes the pricing associated with the ETR.
    :ivar retrieve_mco: When true, returns MCO Information. The default
        value is false.
    :ivar universal_record_locator_code: Contains the Locator Code of
        the Universal Record that houses this reservation.
    :ivar provider_code: Contains the Provider Code of the provider that
        houses this reservation.
    :ivar provider_locator_code: Contains the Locator Code of the
        Provider Reservation that houses this reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
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
    tcrnumber: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    return_restrictions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnRestrictions",
            "type": "Attribute",
        }
    )
    return_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnPricing",
            "type": "Attribute",
        }
    )
    retrieve_mco: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RetrieveMCO",
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


@dataclass
class AirRetrieveDocumentRsp(BaseRsp):
    """
    :ivar etr: Provider: 1G,1V,1P.
    :ivar mco: Provider: 1G,1V,1P.
    :ivar tcr: Provider: 1G,1V,1P.
    :ivar document_failure_info: Provider: 1G,1V,1P-Will be optionally
        returned if there are duplicate ticket numbers.
    :ivar service_fee_info: Provider: 1G,1V
    :ivar universal_record_locator_code: Provider: 1G,1V,1P-Represents a
        valid Universal Record locator code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    mco: List[Mco] = field(
        default_factory=list,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    tcr: List[Tcr] = field(
        default_factory=list,
        metadata={
            "name": "TCR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    document_failure_info: List[TypeFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "DocumentFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
class AirSearchReq(BaseSearchReq):
    """
    Base Request for Air Search.
    """
    point_of_commencement: Optional[PointOfCommencement] = field(
        default=None,
        metadata={
            "name": "PointOfCommencement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchAirLeg",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 16,
        }
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "name": "SearchSpecificAirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_search_modifiers: Optional[AirSearchModifiers] = field(
        default=None,
        metadata={
            "name": "AirSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    journey_data: Optional[JourneyData] = field(
        default=None,
        metadata={
            "name": "JourneyData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )


@dataclass
class AirTicketingRsp(BaseRsp):
    """
    Response to ticket a previously stored reservation.

    :ivar air_solution_changed_info:
    :ivar etr: Provider: 1G,1V,1P.
    :ivar ticket_failure_info: Provider: 1G,1V,1P.
    :ivar detailed_billing_information: Provider: 1G,1V,1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_solution_changed_info: Optional[AirSolutionChangedInfo] = field(
        default=None,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
        }
    )
    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticket_failure_info: List[TicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "TicketFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirVoidDocumentReq(BaseReq):
    """
    Request to void all previously issued tickets for the PNR.

    :ivar air_reservation_locator_code: Provider: 1G,1V.
    :ivar void_document_info: Provider: 1G,1V-All tickets that belong to
        this PNR must be enumerated here. Voiding only some tickets of a
        multi-ticket PNR not currently supported.
    :ivar show_etr: Provider: 1G,1V-If set as true, response will
        display the detailed ETR for successfully voided E-Tickets.
    :ivar provider_code: Provider: 1G,1V-Provider code of a specific
        host.
    :ivar provider_locator_code: Provider: 1G,1V-Contains the locator of
        the host reservation.
    :ivar validate_spanish_residency: Provider: 1G - If set as true,
        Spanish Residency will be validated for Provisioned Customers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    void_document_info: List[VoidDocumentInfo] = field(
        default_factory=list,
        metadata={
            "name": "VoidDocumentInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    show_etr: bool = field(
        default=False,
        metadata={
            "name": "ShowETR",
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
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        }
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
        }
    )


@dataclass
class AirVoidDocumentRsp(BaseRsp):
    """Result of void ticket request.

    Includes ticket number of voided tickets and air segments with
    updated status.

    :ivar etr: Provider: 1G,1V.
    :ivar void_result_info: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    etr: List[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    void_result_info: List[VoidResultInfo] = field(
        default_factory=list,
        metadata={
            "name": "VoidResultInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class BaseAirExchangeMultiQuoteReq(BaseCoreReq):
    """
    :ivar ticket_number:
    :ivar provider_reservation_info: Provider: 1P - Represents a valid
        Provider Reservation/PNR whose itinerary is to be exchanged
    :ivar air_pricing_solution:
    :ivar repricing_modifiers:
    :ivar original_itinerary_details:
    :ivar override_pcc:
    """
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
    provider_reservation_info: Optional["BaseAirExchangeMultiQuoteReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 2,
        }
    )
    repricing_modifiers: Optional[RepricingModifiers] = field(
        default=None,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    override_pcc: Optional[OverridePcc] = field(
        default=None,
        metadata={
            "name": "OverridePCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
class BaseAirExchangeQuoteReq(BaseCoreReq):
    """
    :ivar ticket_number:
    :ivar provider_reservation_info: Provider: 1G/1V/1P/ACH - Represents
        a valid Provider Reservation/PNR whose itinerary is to be
        exchanged
    :ivar air_pricing_solution:
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar host_token: Provider: ACH.
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Provider: ACH-This would allow a user to see
        the fees if they are changing from one Form Of Payment to other
        .
    :ivar repricing_modifiers:
    :ivar original_itinerary_details:
    :ivar pcc:
    :ivar fare_rule_type: Provider: ACH.
    """
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
    provider_reservation_info: Optional["BaseAirExchangeQuoteReq.ProviderReservationInfo"] = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 2,
        }
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    repricing_modifiers: Optional[RepricingModifiers] = field(
        default=None,
        metadata={
            "name": "RepricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    original_itinerary_details: Optional[OriginalItineraryDetails] = field(
        default=None,
        metadata={
            "name": "OriginalItineraryDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
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
class BaseAirPriceReq(BaseCoreReq):
    """
    :ivar air_itinerary: Provider: 1G,1V,1P,ACH.
    :ivar air_pricing_modifiers: Provider: 1G,1V,1P,ACH.
    :ivar search_passenger: Provider: 1G,1V,1P,ACH-Maxinumber of
        passenger increased in to 18 to support 9 INF passenger along
        with 9 ADT,CHD,INS                                   passenger
    :ivar air_pricing_command: Provider: 1G,1V,1P,ACH.
    :ivar air_reservation_locator_code: Provider: ACH,1P
    :ivar optional_services: Provider: ACH.
    :ivar form_of_payment: Provider: 1G,1V,1P,ACH.
    :ivar pcc:
    :ivar ssr: Special Service Request for GST tax details. Provider:
        ACH
    :ivar check_obfees: A flag to return fees for ticketing and for
        various forms of payment. The default is “TicketingOnly” and
        will return only ticketing fees.  The value “All” will return
        ticketing fees and the applicable form of payment fees for the
        form of payment information specified in the request.  “FOPOnly”
        will return the applicable form of payment fees for the form of
        payment information specified in the request. Form of payment
        fees are never included in the total unless specific card
        details are in the request.Provider notes:ACH - CheckOBFees is
        valid only for LowFareSearch.  The valid values are “All”,
        “TicketingOnly” and “None” and the default value is “None”. 1P
        -The valid values are “All”, “None” and “TicketingOnly”.1G – All
        four values are supported.1V/RCH – CheckOBFees are not
        supported.”
    :ivar fare_rule_type: Provider: 1G,1V,1P,ACH.
    :ivar supplier_code: Specifies the supplier/ vendor for vendor
        specific price requests
    :ivar ticket_date: YYYY-MM-DD Using a date in the past is a request
        for an historical fare
    :ivar check_flight_details: To Include FlightDetails in Response set
        to “true” the Default value is “false”.
    :ivar return_mm: If this attribute is set to “true”, Fare Control
        Manager processing will be invoked.
    :ivar nscc: 1 to 3 numeric that defines a Search Control Console
        filter.This attribute is used to override that filter.
    :ivar split_pricing: Indicates whether the AirSegments should be
        priced together or separately. Set ‘true’ for split pricing. Set
        ‘false’ for pricing together.SplitPricing is not supported with
        post book re-pricing.
    :ivar most_restrictive_penalties: Boolean flag used to request the
        MostRestrictivePenalties in the response
    :ivar fare_rule_validation: A boolean flag used to request host to
        return the lowest fare which matches the specified fare basis
        code and passes rule validation
    :ivar pricing_preference: An attribute to return the Lowest
        Price/Ignore availability for a booked itinerary with the valid
        preferences "PriceIgnoreAvailability" and
        "PriceWithAvailability"
    """
    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        }
    )
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    air_pricing_command: List[AirPricingCommand] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingCommand",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )
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
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    pcc: Optional[Pcc] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    check_obfees: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
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
    ticket_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        }
    )
    check_flight_details: bool = field(
        default=False,
        metadata={
            "name": "CheckFlightDetails",
            "type": "Attribute",
        }
    )
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
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
    split_pricing: bool = field(
        default=False,
        metadata={
            "name": "SplitPricing",
            "type": "Attribute",
        }
    )
    most_restrictive_penalties: bool = field(
        default=False,
        metadata={
            "name": "MostRestrictivePenalties",
            "type": "Attribute",
        }
    )
    fare_rule_validation: bool = field(
        default=False,
        metadata={
            "name": "FareRuleValidation",
            "type": "Attribute",
        }
    )
    pricing_preference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingPreference",
            "type": "Attribute",
        }
    )


@dataclass
class BaseAirPriceRsp(BaseRsp):
    """
    :ivar air_itinerary: Provider: 1G,1V,1P,ACH.
    :ivar air_price_result: Provider: 1G,1V,1P,ACH.
    """
    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        }
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "name": "AirPriceResult",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )


@dataclass
class BaseAirSearchReq(BaseCoreSearchReq):
    """
    Base Request for Low fare air Search.
    """
    search_air_leg: List[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchAirLeg",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 9,
        }
    )
    search_specific_air_segment: List[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "name": "SearchSpecificAirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_search_modifiers: Optional[AirSearchModifiers] = field(
        default=None,
        metadata={
            "name": "AirSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    split_ticketing_search: Optional[SplitTicketingSearch] = field(
        default=None,
        metadata={
            "name": "SplitTicketingSearch",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    journey_data: Optional[JourneyData] = field(
        default=None,
        metadata={
            "name": "JourneyData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp):
    """
    Availability Search response.
    """
    flight_details_list: Optional[FlightDetailsList] = field(
        default=None,
        metadata={
            "name": "FlightDetailsList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_segment_list: Optional[AirSegmentList] = field(
        default=None,
        metadata={
            "name": "AirSegmentList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_info_list: Optional[FareInfoList] = field(
        default=None,
        metadata={
            "name": "FareInfoList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_remark_list: Optional[FareRemarkList] = field(
        default=None,
        metadata={
            "name": "FareRemarkList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_itinerary_solution: List[AirItinerarySolution] = field(
        default_factory=list,
        metadata={
            "name": "AirItinerarySolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    host_token_list: Optional[HostTokenList] = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    apisrequirements_list: Optional[ApisrequirementsList] = field(
        default=None,
        metadata={
            "name": "APISRequirementsList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    distance_units: Optional[TypeDistance] = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Attribute",
        }
    )


@dataclass
class BrandList:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    brand: List[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class EmdissuanceReq(BaseReq):
    """
    Electronic Miscellaneous Document issuance request.Supported providers are
    1V/1G/1P.

    :ivar provider_reservation_detail: PNR information for which EMD is
        going to be issued.
    :ivar ticket_number: Ticket number for which EMD is going to be
        issued.Required for EMD-A issuance.
    :ivar issuance_modifiers: General modifiers related to EMD issuance.
    :ivar selection_modifiers: Modifiers related to selection of
        services during EMD issuance.
    :ivar universal_record_locator_code: Represents a valid Universal
        Record locator code.
    :ivar show_details: This attribute gives the control to request for
        complete information on Issued EMDs or minimal
        information.Requesting complete information leads to possible
        multiple supplier calls for fetching all the details.
    :ivar issue_all_open_svc: Issues EMDS to all SVC segments. If it is
        true, TicketNumber and SVC segment reference need not be
        provided. Supported provider 1P.
    """
    class Meta:
        name = "EMDIssuanceReq"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    provider_reservation_detail: Optional[ProviderReservationDetail] = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_length": 1,
            "max_length": 13,
        }
    )
    issuance_modifiers: Optional[IssuanceModifiers] = field(
        default=None,
        metadata={
            "name": "IssuanceModifiers",
            "type": "Element",
        }
    )
    selection_modifiers: Optional[SelectionModifiers] = field(
        default=None,
        metadata={
            "name": "SelectionModifiers",
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
    show_details: bool = field(
        default=False,
        metadata={
            "name": "ShowDetails",
            "type": "Attribute",
        }
    )
    issue_all_open_svc: bool = field(
        default=False,
        metadata={
            "name": "IssueAllOpenSVC",
            "type": "Attribute",
        }
    )


@dataclass
class EmdissuanceRsp(BaseRsp):
    """
    Electronic Miscellaneous Document issuance response.Supported providers are
    1V/1G/1P.

    :ivar emdsummary_info: List of EMDSummaryInfo elements to show
        minimal information in issuance response. Appears for
        ShowDetails=false in the request.This is the default behaviour.
    :ivar emdinfo: List of EMDInfo elements to show detailoed
        information in issuance response. Appears for ShowDetails=true
        in the request.
    """
    class Meta:
        name = "EMDIssuanceRsp"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    emdinfo: List[Emdinfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class EmdretrieveReq(BaseReq):
    """
    Electronic Miscellaneous Document retrieve request.Supported providers are
    1G/1V/1P.

    :ivar list_retrieve: Provider: 1G/1V/1P-Information required for
        retrieval of list of EMDs
    :ivar detail_retrieve: Provider: 1G/1V/1P-Information required for a
        detailed EMD retrieve
    """
    class Meta:
        name = "EMDRetrieveReq"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    list_retrieve: Optional["EmdretrieveReq.ListRetrieve"] = field(
        default=None,
        metadata={
            "name": "ListRetrieve",
            "type": "Element",
        }
    )
    detail_retrieve: Optional["EmdretrieveReq.DetailRetrieve"] = field(
        default=None,
        metadata={
            "name": "DetailRetrieve",
            "type": "Element",
        }
    )

    @dataclass
    class ListRetrieve:
        """
        :ivar provider_reservation_detail: Provider reservation details
            to be provided to fetch list of EMDs associated with it.
        """
        provider_reservation_detail: Optional[ProviderReservationDetail] = field(
            default=None,
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "required": True,
            }
        )

    @dataclass
    class DetailRetrieve:
        """
        :ivar provider_reservation_detail: Provider reservation locator
            to be specified for display operation, if mentioned along
            woth the EMD number then synchronization of that EMD is
            performed considering the same to be associated with the
            mentioned PNR.
        :ivar emdnumber: EMD number to be specified for display
            operation. If mentioned along with provider reservation
            detail then synchronization of that EMD is performed
            considering the same to be associated with the mentioned
            PNR.
        """
        provider_reservation_detail: Optional[ProviderReservationDetail] = field(
            default=None,
            metadata={
                "name": "ProviderReservationDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            }
        )
        emdnumber: Optional[str] = field(
            default=None,
            metadata={
                "name": "EMDNumber",
                "type": "Element",
                "required": True,
                "length": 13,
            }
        )


@dataclass
class EmdretrieveRsp(BaseRsp):
    """
    Electronic Miscellaneous Document list and detail retrieve response.Supported
    providers are 1G/1V/1P.

    :ivar emdinfo: Provider: 1G/1V/1P.
    :ivar emdsummary_info: Provider: 1G/1V/1P.
    """
    class Meta:
        name = "EMDRetrieveRsp"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    emdinfo: Optional[Emdinfo] = field(
        default=None,
        metadata={
            "name": "EMDInfo",
            "type": "Element",
        }
    )
    emdsummary_info: List[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class FlightDetailsReq(BaseReq):
    """
    Request for the Flight Details of segments.

    :ivar air_segment: Provider: 1G,1V,1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FlightDetailsRsp(BaseRsp):
    """
    :ivar air_segment: Provider: 1G,1V,1P.
    :ivar co2_emissions:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    co2_emissions: List[Co2Emissions] = field(
        default_factory=list,
        metadata={
            "name": "CO2Emissions",
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class FlightInformationReq(BaseReq):
    """
    Request for the Flight Info of segments.

    :ivar flight_info_criteria: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_info_criteria: List[FlightInfoCriteria] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoCriteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FlightInformationRsp(BaseRsp):
    """
    :ivar flight_info: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_info: List[FlightInfo] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class FlightTimeTableReq(BaseSearchReq):
    """
    Request for Flight Time Table.

    :ivar flight_time_table_criteria: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_time_table_criteria: Optional[FlightTimeTableCriteria] = field(
        default=None,
        metadata={
            "name": "FlightTimeTableCriteria",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FlightTimeTableRsp(BaseSearchRsp):
    """
    Response for Flight Time Table.

    :ivar flight_time_table_list: Provider: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_time_table_list: Optional["FlightTimeTableRsp.FlightTimeTableList"] = field(
        default=None,
        metadata={
            "name": "FlightTimeTableList",
            "type": "Element",
        }
    )

    @dataclass
    class FlightTimeTableList:
        flight_time_detail: List[FlightTimeDetail] = field(
            default_factory=list,
            metadata={
                "name": "FlightTimeDetail",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class SeatMapReq(BaseReq):
    """
    Request a seat map for the give flight information.

    :ivar agency_sell_info: Provider: ACH-Required if the user
        requesting the seat map is not the same agent authenticated in
        the request.
    :ivar air_segment: Provider: 1G,1V,1P,ACH,MCH.
    :ivar host_token: Provider: ACH-Required if the carrier has multiple
        adapters.
    :ivar search_traveler: Provider: 1G,1V,ACH,MCH.
    :ivar host_reservation: Provider: ACH,MCH-Required when seat price
        is requested.
    :ivar merchandising_pricing_modifiers: Used to provide additional
        pricing options. Provider:ACH.
    :ivar return_seat_pricing: Provider: 1G,1V,1P,ACH-When set to true
        the price of the seat will be returned if it exists.
    :ivar return_branding_info: A value of true will return the
        BrandingInfo block in the response if applicable. A value of
        false will not return the BrandingInfo block in the response.
        Providers: 1G, 1V, 1P, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    agency_sell_info: Optional[AgencySellInfo] = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
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
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_reservation: Optional[HostReservation] = field(
        default=None,
        metadata={
            "name": "HostReservation",
            "type": "Element",
        }
    )
    merchandising_pricing_modifiers: Optional[MerchandisingPricingModifiers] = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
        }
    )
    return_seat_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnSeatPricing",
            "type": "Attribute",
            "required": True,
        }
    )
    return_branding_info: bool = field(
        default=False,
        metadata={
            "name": "ReturnBrandingInfo",
            "type": "Attribute",
        }
    )


@dataclass
class SeatMapRsp(BaseRsp):
    """
    :ivar host_token: Provider: ACH,MCH.
    :ivar cabin_class: Provider: 1G,1V,1P,ACH,MCH.
    :ivar air_segment: Provider: ACH,MCH.
    :ivar search_traveler: Provider: ACH,MCH.
    :ivar optional_services: A wrapper for all the information regarding
        each of the Optional Services. Provider: 1G,1V,1P,ACH.
    :ivar remark: Provider: 1G,1V,1P,ACH,MCH.
    :ivar rows:
    :ivar payment_restriction: Provider: MCH-Information regarding valid
        payment types, if restrictions apply(supplier specific)
    :ivar seat_information:
    :ivar copyright: Copyright text applicable for some seat content.
        Providers: 1G, 1V, 1P,ACH
    :ivar group_seat_price: Provider: 1G,1V-Seat price for the all
        passengers traveling together only when supplier provides group
        flat fee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    cabin_class: Optional[CabinClass] = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    optional_services: Optional[OptionalServices] = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    remark: Optional[Remark] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rows: List[Rows] = field(
        default_factory=list,
        metadata={
            "name": "Rows",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    payment_restriction: List[PaymentRestriction] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    seat_information: List[SeatInformation] = field(
        default_factory=list,
        metadata={
            "name": "SeatInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    copyright: Optional[str] = field(
        default=None,
        metadata={
            "name": "Copyright",
            "type": "Element",
        }
    )
    group_seat_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupSeatPrice",
            "type": "Attribute",
        }
    )


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """Request multiple quotes for the exchange of an itinerary.

    1P transactions only

    :ivar type_value: Type choices are "Detail" or "Summary"  Default
        will be Summary
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: str = field(
        default="Summary",
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class AirExchangeMultiQuoteRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_list: List[AirSegmentList] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentList",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    brand_list: List[BrandList] = field(
        default_factory=list,
        metadata={
            "name": "BrandList",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_exchange_mulit_quote_list: List[AirExchangeMulitQuoteList] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeMulitQuoteList",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AirExchangeQuoteReq(BaseAirExchangeQuoteReq):
    """
    Request to quote the exchange of an itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPriceReq(BaseAirPriceReq):
    """Request to price an itinerary in one to many ways.

    Pricing commands can be specified globally, or specifically per
    command.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPriceRsp(BaseAirPriceRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRepriceReq(AirBaseReq):
    """
    Request to reprice a solution.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    air_pricing_solution: Optional[AirPricingSolution] = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        }
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        }
    )
    ignore_availability: bool = field(
        default=False,
        metadata={
            "name": "IgnoreAvailability",
            "type": "Attribute",
        }
    )


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """
    Base Response for Air Search.
    """
    fare_note_list: Optional[FareNoteList] = field(
        default=None,
        metadata={
            "name": "FareNoteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    expert_solution_list: Optional[ExpertSolutionList] = field(
        default=None,
        metadata={
            "name": "ExpertSolutionList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    route_list: Optional[RouteList] = field(
        default=None,
        metadata={
            "name": "RouteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    alternate_route_list: Optional[AlternateRouteList] = field(
        default=None,
        metadata={
            "name": "AlternateRouteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    alternate_location_distance_list: Optional[AlternateLocationDistanceList] = field(
        default=None,
        metadata={
            "name": "AlternateLocationDistanceList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_info_message: List[FareInfoMessage] = field(
        default_factory=list,
        metadata={
            "name": "FareInfoMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
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
    air_price_point_list: Optional[AirPricePointList] = field(
        default=None,
        metadata={
            "name": "AirPricePointList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    rail_segment_list: Optional[RailSegmentList] = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_journey_list: Optional[RailJourneyList] = field(
        default=None,
        metadata={
            "name": "RailJourneyList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
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
    rail_fare_idlist: Optional[RailFareIdlist] = field(
        default=None,
        metadata={
            "name": "RailFareIDList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_fare_list: Optional[RailFareList] = field(
        default=None,
        metadata={
            "name": "RailFareList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
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


@dataclass
class AirTicketingReq(AirBaseReq):
    """
    Request to ticket a previously stored reservation.

    :ivar air_reservation_locator_code: Provider: 1G,1V,1P.
    :ivar air_pricing_info_ref: Provider: 1G,1V,1P-Indicates air pricing
        infos to be ticketed.
    :ivar ticketing_modifiers_ref: Provider: 1P-Reference to a shared
        list of Ticketing Modifiers. This is supported for Worldspan
        providers only. When AirPricingInfoRef is used along with
        TicketingModifiersRef means that particular TicketingModifiers
        will to be applied while ticketing the Stored fare corresponding
        to the AirPricingInfo. Absence of AirPricingInfoRef means that
        particular TicketingModifiers will be applied to all Stored
        fares which are requested to be ticketed.
    :ivar waiver_code:
    :ivar commission:
    :ivar detailed_billing_information: Provider: 1G,1V.
    :ivar fax_details_information: Provider: 1V.
    :ivar air_ticketing_modifiers: Provider: 1G,1V,1P.
    :ivar air_segment_ticketing_modifiers: Provider: 1P.
    :ivar return_info_on_fail:
    :ivar bulk_ticket: Provider: 1G,1V,1P.
    :ivar validate_spanish_residency: Provider: 1G - If set as true,
        Spanish Residency will be validated for Provisioned Customers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    air_pricing_info_ref: List["AirTicketingReq.AirPricingInfoRef"] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ticketing_modifiers_ref: List[TypeTicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    waiver_code: Optional[WaiverCode] = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 18,
        }
    )
    detailed_billing_information: List[DetailedBillingInformation] = field(
        default_factory=list,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fax_details_information: Optional[FaxDetailsInformation] = field(
        default=None,
        metadata={
            "name": "FaxDetailsInformation",
            "type": "Element",
        }
    )
    air_ticketing_modifiers: List[AirTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_ticketing_modifiers: List[AirSegmentTicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentTicketingModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    return_info_on_fail: bool = field(
        default=True,
        metadata={
            "name": "ReturnInfoOnFail",
            "type": "Attribute",
        }
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        }
    )
    validate_spanish_residency: bool = field(
        default=False,
        metadata={
            "name": "ValidateSpanishResidency",
            "type": "Attribute",
        }
    )

    @dataclass
    class AirPricingInfoRef:
        booking_traveler_ref: List[BookingTravelerRef] = field(
            default_factory=list,
            metadata={
                "name": "BookingTravelerRef",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "max_occurs": 9,
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
class AirUpsellSearchReq(AirBaseReq):
    """
    Request to search for Upsell Offers based on the Itinerary.

    :ivar air_itinerary: Provider: 1G,1V,1P,ACH-AirItinerary of the
        pricing request.
    :ivar air_price_result: Provider: 1G,1V,1P,ACH-Result of AirPrice
        request. Upsell uses this to search for new offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_itinerary: Optional[AirItinerary] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "required": True,
        }
    )
    air_price_result: List[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "name": "AirPriceResult",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        }
    )


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """
    Response of Upsell Offers search for the given Itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AvailabilitySearchReq(AirSearchReq):
    """
    Availability Search request.

    :ivar search_passenger: Provider: 1G,1V,1P,ACH-Maxinumber of
        passenger increased in to 18 to support 9 INF passenger along
        with 9 ADT,CHD,INS
        passenger
    :ivar point_of_sale: Provider: ACH.
    :ivar return_brand_indicator: When set to “true”, the Brand
        Indicator can be returned in the availability search response.
        Provider: 1G, 1V, 1P, ACH
    :ivar channel_id: A Channel ID is 4 alpha-numeric characters used to
        activate the Search Control Console filter for a specific group
        of travelers being served by the agency credential.
    :ivar nscc: Allows the agency to bypass/override the Search Control
        Console rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    search_passenger: List[SearchPassenger] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 18,
        }
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    return_brand_indicator: bool = field(
        default=False,
        metadata={
            "name": "ReturnBrandIndicator",
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


@dataclass
class AvailabilitySearchRsp(BaseAvailabilitySearchRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """
    Base Low Fare Search Request.

    :ivar search_passenger: Provider: 1G,1V,1P,ACH-Maxinumber of
        passenger increased in to 18 to support 9 INF passenger along
        with 9 ADT,CHD,INS                                   passenger
    :ivar air_pricing_modifiers: Provider: 1G,1V,1P,ACH.
    :ivar enumeration: Provider: 1G,1V,1P,ACH.
    :ivar air_exchange_modifiers: Provider: ACH.
    :ivar flex_explore_modifiers: This is the container for a set of
        modifiers which allow the user to perform a special kind of low
        fare search, depicted as flex explore, based on different
        parameters like Area, Zone, Country, State, Specific locations,
        Distance around the actual destination of the itinerary.
        Applicable for providers 1G,1V,1P.
    :ivar pcc:
    :ivar fare_rules_filter_category:
    :ivar form_of_payment: Provider: 1P
    :ivar enable_point_to_point_search: Provider: 1G,1V,1P,ACH-Indicates
        that low cost providers should be queried for top connection
        options and the results returned with the search.
    :ivar enable_point_to_point_alternates: Provider: 1G,1V,1P,ACH-
        Indicates that suggestions for alternate connection cities for
        low cost providers should be returned with the search.
    :ivar max_number_of_expert_solutions: Provider: 1G,1V,1P,ACH-
        Indicates the Maximum Number of Expert Solutions to be returned
        from the Knowledge Base for the provided search criteria
    :ivar solution_result: Provider: 1G,1V,1P,ACH-Indicates whether the
        response will contain Solution result (AirPricingSolution) or
        Non Solution Result (AirPricingPoints). The default value is
        false. This attribute cannot be combined with
        EnablePointToPointSearch, EnablePointToPointAlternates and
        MaxNumberOfExpertSolutions.
    :ivar prefer_complete_itinerary: Provider: ACH-This attribute is
        only supported for ACH .It works in conjunction with the
        @SolutionResult flag
    :ivar meta_option_identifier: Invoke Meta Search.  Valid values are
        00 to 99, or D for the default meta search configuration.  When
        Meta Search not requested, normal LowFareSearch applies.
        Supported Providers;  1g/1v/1p
    :ivar return_upsell_fare: When set to “true”, Upsell information
        will be returned in the shop response. Provider supported : 1G,
        1V, 1P
    :ivar include_fare_info_messages: Set to True to return
        FareInfoMessageList. Providers supported: 1G/1V/1P
    :ivar return_branded_fares: When ReturnBrandedFares is set to
        “false”, Rich Content and Branding will not be returned in the
        shop response.  When ReturnBrandedFares it is set to “true” or
        is not sent, Rich Content and Branding will be returned in the
        shop response.  Provider: 1P/ACH.
    :ivar multi_gdssearch: A "true" value indicates MultiGDSSearch.
        Specific provisioning is required.
    :ivar return_mm: If this attribute is set to “true”, Fare Control
        Manager processing will be invoked.
    :ivar check_obfees: A flag to return fees for ticketing and for
        various forms of payment. The default is “TicketingOnly” and
        will return only ticketing fees.  The value “All” will return
        ticketing fees and the applicable form of payment fees for the
        form of payment information specified in the request.  “FOPOnly”
        will return the applicable form of payment fees for the form of
        payment information specified in the request. Form of payment
        fees are never included in the total unless specific card
        details are in the request.Provider notes:ACH - CheckOBFees is
        valid only for LowFareSearch.  The valid values are “All”,
        “TicketingOnly” and “None” and the default value is “None”. 1P
        -The valid values are “All”, “None” and “TicketingOnly”.1G – All
        four values are supported.1V/RCH – CheckOBFees are not
        supported.”
    :ivar nscc: 1 to 3 numeric that defines a Search Control Console
        filter.This attribute is used to override that filter.
    :ivar fare_info_rules: Returns ChangePenalty and CancelPenalty
        values at the FareInfo level. If FareRulesFilterCategory is sent
        FareRulesFilter will be returned at FareInfo level.  Provider:
        1G/1V.
    :ivar most_restrictive_penalties: Boolean flag used to request the
        MostRestrictivePenalties in the response
    """
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
    air_pricing_modifiers: Optional[AirPricingModifiers] = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    enumeration: Optional[Enumeration] = field(
        default=None,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_exchange_modifiers: Optional[AirExchangeModifiers] = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    flex_explore_modifiers: Optional[FlexExploreModifiers] = field(
        default=None,
        metadata={
            "name": "FlexExploreModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    pcc: Optional[Pcc] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_rules_filter_category: Optional[FareRulesFilterCategory] = field(
        default=None,
        metadata={
            "name": "FareRulesFilterCategory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    enable_point_to_point_search: bool = field(
        default=False,
        metadata={
            "name": "EnablePointToPointSearch",
            "type": "Attribute",
        }
    )
    enable_point_to_point_alternates: bool = field(
        default=False,
        metadata={
            "name": "EnablePointToPointAlternates",
            "type": "Attribute",
        }
    )
    max_number_of_expert_solutions: int = field(
        default=0,
        metadata={
            "name": "MaxNumberOfExpertSolutions",
            "type": "Attribute",
        }
    )
    solution_result: bool = field(
        default=False,
        metadata={
            "name": "SolutionResult",
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
    meta_option_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetaOptionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    return_upsell_fare: bool = field(
        default=False,
        metadata={
            "name": "ReturnUpsellFare",
            "type": "Attribute",
        }
    )
    include_fare_info_messages: bool = field(
        default=False,
        metadata={
            "name": "IncludeFareInfoMessages",
            "type": "Attribute",
        }
    )
    return_branded_fares: bool = field(
        default=True,
        metadata={
            "name": "ReturnBrandedFares",
            "type": "Attribute",
        }
    )
    multi_gdssearch: bool = field(
        default=False,
        metadata={
            "name": "MultiGDSSearch",
            "type": "Attribute",
        }
    )
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        }
    )
    check_obfees: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
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
    fare_info_rules: bool = field(
        default=False,
        metadata={
            "name": "FareInfoRules",
            "type": "Attribute",
        }
    )
    most_restrictive_penalties: bool = field(
        default=False,
        metadata={
            "name": "MostRestrictivePenalties",
            "type": "Attribute",
        }
    )


@dataclass
class ScheduleSearchReq(AirSearchReq):
    """
    Schedule Search request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class LowFareSearchReq(BaseLowFareSearchReq):
    """
    Low Fare Search request.

    :ivar policy_reference: This attribute will be used to pass in a
        value on the request which would be used to link to a ‘Policy
        Group’ in a policy engine external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    policy_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Response.

    :ivar brand_list:
    :ivar currency_type: Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    brand_list: Optional[BrandList] = field(
        default=None,
        metadata={
            "name": "BrandList",
            "type": "Element",
        }
    )
    currency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )


@dataclass
class ScheduleSearchRsp(AirSearchRsp):
    """
    Schedule Search response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
