from dataclasses import dataclass, field
from typing import List, Optional
from generated.common_v52_0.common import (
    Keyword,
    MarketingInformation,
    PointOfSale,
)
from generated.common_v52_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
    BaseSearchReq,
    BaseSearchRsp,
)
from generated.vehicle_v52_0.vehicle import (
    LocationInfo,
    Policy,
    Vehicle,
    VehicleDateLocation,
    VehicleLocation,
    VehiclePickupLocation,
    VehiclePolicy,
    VehicleReservation,
    VehicleSearchId,
    VehicleSearchModifiers,
    VehicleWithMediaItems,
    Vendor,
    VendorInfo,
    TypeDepositGuarantee,
    TypePickupDateLocation,
    TypeRentalPeriod,
    TypeStartEndTime,
    TypeVehicleCharge,
    TypeVehicleLocationInformation,
    TypeVehicleSearchDistance,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class BaseVehicleSearchAvailabilityReq(BaseSearchReq):
    """
    Base request to search for vehicle availability.
    """
    vehicle_date_location: Optional[VehicleDateLocation] = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "required": True,
        }
    )
    vehicle_search_modifiers: Optional[VehicleSearchModifiers] = field(
        default=None,
        metadata={
            "name": "VehicleSearchModifiers",
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


@dataclass
class BaseVehicleSearchAvailabilityRsp(BaseSearchRsp):
    """
    Base response of vehicle availability response.
    """
    vehicle_date_location: Optional[VehicleDateLocation] = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "required": True,
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


@dataclass
class VehicleKeywordReq(BaseSearchReq):
    """
    Used to request a list of keywords or specific keyword information for a car
    vendor.

    :ivar vendor:
    :ivar pickup_date_location: The date and location for which a list
        of vendors is requested.
    :ivar keyword: Used to request specific keyword details
    :ivar keyword_list: When true, a list of keywords should be
        returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: Optional[Vendor] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "required": True,
        }
    )
    pickup_date_location: Optional[TypePickupDateLocation] = field(
        default=None,
        metadata={
            "name": "PickupDateLocation",
            "type": "Element",
            "required": True,
        }
    )
    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 3,
        }
    )
    keyword_list: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeywordList",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleKeywordRsp(BaseRsp):
    """
    Used to respond with a list of keywords or specific keyword information.

    :ivar text: Information for this vendor not related to a keyword.
    :ivar keyword: A word that a vendor uses to describe corporate
        policy/information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )


@dataclass
class VehicleLocationDetailReq(BaseReq):
    """
    :ivar vendor:
    :ivar vehicle_date_location:
    :ivar point_of_sale:
    :ivar policy_reference: This attribute will be used to pass in a
        value on the request which would be used to link to a ‘Policy
        Group’ in a policy engine external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: Optional[Vendor] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "required": True,
        }
    )
    vehicle_date_location: Optional[VehicleDateLocation] = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "required": True,
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
class VehicleLocationDetailRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor_info: Optional[VendorInfo] = field(
        default=None,
        metadata={
            "name": "VendorInfo",
            "type": "Element",
            "required": True,
        }
    )
    location_info: List[LocationInfo] = field(
        default_factory=list,
        metadata={
            "name": "LocationInfo",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    vehicle_policy: Optional[VehiclePolicy] = field(
        default=None,
        metadata={
            "name": "VehiclePolicy",
            "type": "Element",
        }
    )


@dataclass
class VehicleLocationReq(BaseReq):
    """
    Used to request a list of vendors for a location (airport or city code).

    :ivar vendor:
    :ivar pickup_date_location: The date and location for which a list
        of vendors is requested.
    :ivar reference_point: Search Car by reference point
    :ivar search_distance: Distance from search location. Providers:
        1g/1v
    :ivar policy_reference: This attribute will be used to pass in a
        value on the request which would be used to link to a ‘Policy
        Group’ in a policy engine external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor: List[Vendor] = field(
        default_factory=list,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    pickup_date_location: Optional[TypePickupDateLocation] = field(
        default=None,
        metadata={
            "name": "PickupDateLocation",
            "type": "Element",
            "required": True,
        }
    )
    reference_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_length": 30,
        }
    )
    search_distance: Optional[TypeVehicleSearchDistance] = field(
        default=None,
        metadata={
            "name": "SearchDistance",
            "type": "Element",
        }
    )
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
class VehicleLocationRsp(BaseRsp):
    """
    Returns a list of vendors and their locations for an airport or city code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_location: List[VehicleLocation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleLocation",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleMediaLinksReq(BaseReq):
    """
    Used to request a list of images for a location (airport or city code) and
    vendor.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_search_id: Optional[VehicleSearchId] = field(
        default=None,
        metadata={
            "name": "VehicleSearchId",
            "type": "Element",
        }
    )
    vehicle_pickup_location: List[VehiclePickupLocation] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePickupLocation",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleMediaLinksRsp(BaseRsp):
    """
    Response for vehicle image search results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_with_media_items: List[VehicleWithMediaItems] = field(
        default_factory=list,
        metadata={
            "name": "VehicleWithMediaItems",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleRetrieveReq(BaseReq):
    """PNR Retrieve request for a vehicle booking.

    Given a provider code and a provider locator code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

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
class VehicleRetrieveRsp(BaseRsp):
    """
    Response to a VehicleRetrieveReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_reservation: List[VehicleReservation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleReservation",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleRulesReq(BaseSearchReq):
    """
    Used to request  rules for a specific vehicle and rate.

    :ivar vehicle_reservation_locator_code: Request vehicle rules using
        Locator code of existing vehicle reservation.
    :ivar vehicle_rules_lookup: Details to request Vehicle rate rules
        post shopping request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    vehicle_rules_lookup: Optional["VehicleRulesReq.VehicleRulesLookup"] = field(
        default=None,
        metadata={
            "name": "VehicleRulesLookup",
            "type": "Element",
        }
    )

    @dataclass
    class VehicleRulesLookup:
        vehicle_date_location: Optional[VehicleDateLocation] = field(
            default=None,
            metadata={
                "name": "VehicleDateLocation",
                "type": "Element",
                "required": True,
            }
        )
        vehicle_search_modifiers: Optional[VehicleSearchModifiers] = field(
            default=None,
            metadata={
                "name": "VehicleSearchModifiers",
                "type": "Element",
                "required": True,
            }
        )


@dataclass
class VehicleRulesRsp(BaseSearchRsp):
    """
    The rules associated with a vehicle rental rate.

    :ivar vehicle:
    :ivar operation_time:
    :ivar start_end_times: The earliest and latest pickup and dropoff
        times for this vehicle rental rate.
    :ivar rental_period_rules: The maximum and minimum rental periods.
    :ivar pre_pay_cancel_info: PrePayment cancellation Advisory Values
        use to construct custom Advisory text. 1P only.
    :ivar payment_rule: The Deposit, Guarantee or PrePayment rule for
        the vehicle rental.
    :ivar payment_credit_card: The two character code of a credit card
        accepted for payment.
    :ivar vehicle_charge: Charges associated with the vehicle rental.
    :ivar marketing_information:
    :ivar policy:
    :ivar pickup_location_information: Pickup Location  Information ,
        1P only.
    :ivar return_location_information: Return Location  Information ,
        1P only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "required": True,
        }
    )
    operation_time: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    start_end_times: Optional["VehicleRulesRsp.StartEndTimes"] = field(
        default=None,
        metadata={
            "name": "StartEndTimes",
            "type": "Element",
        }
    )
    rental_period_rules: Optional["VehicleRulesRsp.RentalPeriodRules"] = field(
        default=None,
        metadata={
            "name": "RentalPeriodRules",
            "type": "Element",
        }
    )
    pre_pay_cancel_info: List["VehicleRulesRsp.PrePayCancelInfo"] = field(
        default_factory=list,
        metadata={
            "name": "PrePayCancelInfo",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    payment_rule: List["VehicleRulesRsp.PaymentRule"] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRule",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    payment_credit_card: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PaymentCreditCard",
            "type": "Element",
            "max_occurs": 13,
            "length": 2,
        }
    )
    vehicle_charge: List[TypeVehicleCharge] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCharge",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    marketing_information: Optional[MarketingInformation] = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    policy: List[Policy] = field(
        default_factory=list,
        metadata={
            "name": "Policy",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    pickup_location_information: Optional[TypeVehicleLocationInformation] = field(
        default=None,
        metadata={
            "name": "PickupLocationInformation",
            "type": "Element",
        }
    )
    return_location_information: Optional[TypeVehicleLocationInformation] = field(
        default=None,
        metadata={
            "name": "ReturnLocationInformation",
            "type": "Element",
        }
    )

    @dataclass
    class StartEndTimes:
        """
        :ivar earliest_start: The earliest a vehicle may be picked up.
        :ivar latest_start: The latest a vehicle may be picked up.
        :ivar latest_end: The latest a vehicle may be dropped off.
        """
        earliest_start: Optional[TypeStartEndTime] = field(
            default=None,
            metadata={
                "name": "EarliestStart",
                "type": "Element",
            }
        )
        latest_start: Optional[TypeStartEndTime] = field(
            default=None,
            metadata={
                "name": "LatestStart",
                "type": "Element",
            }
        )
        latest_end: Optional[TypeStartEndTime] = field(
            default=None,
            metadata={
                "name": "LatestEnd",
                "type": "Element",
            }
        )

    @dataclass
    class RentalPeriodRules:
        """
        :ivar max_rental: The maximum rental period for this rate.
        :ivar min_rental: The minimum rental period for this rate.
        :ivar absolute_max: The absolute maximum rental period for this
            rate.
        """
        max_rental: Optional[TypeRentalPeriod] = field(
            default=None,
            metadata={
                "name": "MaxRental",
                "type": "Element",
            }
        )
        min_rental: Optional[TypeRentalPeriod] = field(
            default=None,
            metadata={
                "name": "MinRental",
                "type": "Element",
            }
        )
        absolute_max: Optional[TypeRentalPeriod] = field(
            default=None,
            metadata={
                "name": "AbsoluteMax",
                "type": "Element",
            }
        )

    @dataclass
    class PrePayCancelInfo:
        """
        :ivar code: Code value associated to policy line advisory
            cancellation text (values 001 up to 999) 1P only.
        :ivar amount: Rate amount preceded by the ISO currency code
            charged to cancel, e.g. USD25.00 1P only.
        :ivar percent: Percentage value (e.g. 010=10%     025=25%
            050=50%       100) 1P only.
        :ivar number_of_days_hours: Number of Days or Hours (e.g. 002
            days  024 hours), 1P only.
        :ivar rental_days: Number of rental days (e.g. 001 up to 365),
            1P only.
        """
        code: Optional[int] = field(
            default=None,
            metadata={
                "name": "Code",
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
        percent: Optional[int] = field(
            default=None,
            metadata={
                "name": "Percent",
                "type": "Attribute",
            }
        )
        number_of_days_hours: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumberOfDaysHours",
                "type": "Attribute",
            }
        )
        rental_days: Optional[int] = field(
            default=None,
            metadata={
                "name": "RentalDays",
                "type": "Attribute",
            }
        )

    @dataclass
    class PaymentRule(TypeDepositGuarantee):
        """
        :ivar credit_card: The two character credit card code.
        """
        credit_card: List[str] = field(
            default_factory=list,
            metadata={
                "name": "CreditCard",
                "type": "Element",
                "max_occurs": 13,
                "length": 2,
            }
        )


@dataclass
class VehicleSearchAvailabilityReq(BaseVehicleSearchAvailabilityReq):
    """
    :ivar return_media_links: Set indicator to true to retrieve the
        media links. Default False
    :ivar return_all_rates: Default, false.  If true, all available
        rates are returned if applicable for the specified provider.
    :ivar return_approximate_total: Applies only if ReturnAllRates is
        set to true.  If false, base rates are returned. If true,
        approximate total rates are returned as supported by the car
        vendor.  Default is false.
    :ivar return_extra_rate_info: Applies only if ReturnAllRates is set
        to true. If false, basic rate details are returned. If true,
        additional rate information is returned.  Default is false.
    :ivar policy_reference: This attribute will be used to pass in a
        value on the request which would be used to link to a ‘Policy
        Group’ in a policy engine external to UAPI.
    :ivar return_inclusion_details: Set indicator to true to retrieve
        the Rate Inclusion Details. Default False
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    return_media_links: bool = field(
        default=False,
        metadata={
            "name": "ReturnMediaLinks",
            "type": "Attribute",
        }
    )
    return_all_rates: bool = field(
        default=False,
        metadata={
            "name": "ReturnAllRates",
            "type": "Attribute",
        }
    )
    return_approximate_total: bool = field(
        default=False,
        metadata={
            "name": "ReturnApproximateTotal",
            "type": "Attribute",
        }
    )
    return_extra_rate_info: bool = field(
        default=False,
        metadata={
            "name": "ReturnExtraRateInfo",
            "type": "Attribute",
        }
    )
    policy_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    return_inclusion_details: bool = field(
        default=False,
        metadata={
            "name": "ReturnInclusionDetails",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleSearchAvailabilityRsp(BaseVehicleSearchAvailabilityRsp):
    """
    :ivar marketing_information: Marketing text or notices by Suppliers.
        1P only.
    :ivar media_links_search_id: Unique search id to retrieve the media
        links using VehicleMediaLinksReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    marketing_information: Optional[MarketingInformation] = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    media_links_search_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaLinksSearchId",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleUpsellSearchAvailabilityReq(BaseVehicleSearchAvailabilityReq):
    """
    Request to search Upsell offer availability for Vehicle.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleUpsellSearchAvailabilityRsp(BaseVehicleSearchAvailabilityRsp):
    """
    Response of search Vehicle Upsell offer availability.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"
