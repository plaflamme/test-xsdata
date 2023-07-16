from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from generated.common_v52_0.common import (
    BaseReservation,
    BookingSource,
    BookingTravelerRef,
    CoordinateLocation,
    Distance,
    Email,
    Guarantee,
    LocationAddress,
    LoyaltyCard,
    MediaItem,
    PhoneNumber,
    ReservationName,
    SpecialEquipment,
    ThirdPartyInformation,
    VendorLocation,
    TypeAssociatedRemark,
    TypeDistance,
    TypeDoorCount,
    TypeFuel,
    TypeKeyword,
    TypePolicyCodesList,
    TypeRateCategory,
    TypeRateGuarantee,
    TypeRateTimePeriod,
    TypeReserveRequirement,
    TypeResultMessage,
    TypeStructuredAddress,
    TypeTrinary,
    TypeVehicleCategory,
    TypeVehicleClass,
    TypeVehicleLocation,
    TypeVehicleTransmission,
    TypeVendorLocation,
    TypeVoucherInformation,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class Charge:
    """
    Charge information associated to Special Equipment.

    :ivar amount: Special Equipment Charge Amount.
    :ivar rate_period: Rate Period associated to the Special Equipment
        Charge Amount.e.g. Daily, Weekly, Rental
    :ivar included_in_est_total_ind: Special Equipment Amount is
        included in the Estimated Total Amount
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    rate_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatePeriod",
            "type": "Attribute",
            "required": True,
        }
    )
    included_in_est_total_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludedInEstTotalInd",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DriverInfo:
    """
    :ivar age: This is used to specify Primary Driver’s age in years. 1P
        only. Required.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 99,
        }
    )


@dataclass
class Equipment:
    """
    Requested Special Equipment Information.

    :ivar type_value: The Type of Special Equipment requested
    :ivar description: Special Equipment description
    :ivar quantity: Special Equipment quantity
    :ivar status: Status of the request returned by the supplier. Valid
        Values KK (Confirmed), UC (Unable to Confirm and NN (On request)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
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


@dataclass
class FlightArrivalInformation:
    """
    The flight arrival information (airline code and flight number) for the
    airport/city at which the rental car will be picked up.

    :ivar carrier: The carrier that is marketing this segment
    :ivar flight_number: The flight number under which the marketing
        carrier is marketing this flight
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

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
            "max_length": 30,
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
class IncludedItem:
    """
    Provides details of included item.

    :ivar code: Code for included item.
    :ivar description: Description of included item.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OperationTime:
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class RateModifiers:
    """
    :ivar rate_code:
    :ivar discount_number:
    :ivar vendor_code:
    :ivar promotional_code: Specific coupon or promotion code
    :ivar vendor_location_ref:
    :ivar tour_code: Tour number or code.  Providers: 1P, 1G, 1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    discount_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
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
    promotional_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PromotionalCode",
            "type": "Attribute",
        }
    )
    vendor_location_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorLocationRef",
            "type": "Attribute",
        }
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleRateInfo:
    """Container for adding and modifying Vehicle Rate related information.

    For Modify operation :
    If a value is passed in any of the attributes they will be updated,
    If an empty string is passed then the attributed's value will be deleted,
    If the attribute is not passed no action will be taken.

    :ivar tour_code: Tour Number for the Vehicle Booking
    :ivar discount_number: Corporate Discount Number for the Vehicle
        Booking
    :ivar promotional_code: Promotional Code for the Vehicle Booking
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        }
    )
    discount_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    promotional_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PromotionalCode",
            "type": "Attribute",
        }
    )


class VehicleRateRequiredPayment(Enum):
    GUARANTEE = "Guarantee"
    DEPOSIT = "Deposit"
    PRE_PAYMENT = "PrePayment"


@dataclass
class VehicleSearchId:
    """
    A container for Vehicle Media Links Search Id.

    :ivar media_links_search_id: The search id  from
        VehicleSearchAvailabilityRsp to be used to retrieve the media
        links.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    media_links_search_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MediaLinksSearchId",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VehicleSpecialRequest:
    """
    Make a textual request to the Vehicle supplier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 250,
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
class Vendor:
    """
    The supplier code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

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
class VendorInfo:
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

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
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )


class TypeAreaInfo(Enum):
    """
    The type of area category, such as AirportMain, AirportSecondary.
    """
    AIRPORT_MAIN = "AirportMain"
    AIRPORT_SECONDARY = "AirportSecondary"
    CITY_CENTER_DOWNTOWN = "CityCenterDowntown"
    EAST_OF_CITY_CENTER = "EastOfCityCenter"
    SOUTH_OF_CITY_CENTER = "SouthOfCityCenter"
    WEST_OF_CITY_CENTER = "WestOfCityCenter"
    NORTH_OF_CITY_CENTER = "NorthOfCityCenter"
    PORT_OR_FERRY = "PortOrFerry"
    NEAR_RESORT = "NearResort"
    RAILWAY_STATION = "RailwayStation"


class TypeDepositGuaranteeOptionType(Enum):
    AFTER_BOOKING = "AfterBooking"
    PRIOR_TO_PICKUP = "PriorToPickup"


class TypeDepositGuaranteeType(Enum):
    NUMBER_OF_DAYS = "NumberOfDays"
    AMOUNT = "Amount"
    PERCENT = "Percent"


class TypeRateAvailability(Enum):
    AVAILABLE = "Available"
    CALL = "Call"
    CLOSED = "Closed"


@dataclass
class TypeRateHostIndicator:
    """
    Host-specific info for vendors.

    :ivar inventory_token: Vendor info about rate to adjust pricing as
        needed
    :ivar rate_token: Assocates shop response to sell request
    """
    class Meta:
        name = "typeRateHostIndicator"

    inventory_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "InventoryToken",
            "type": "Attribute",
        }
    )
    rate_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateToken",
            "type": "Attribute",
        }
    )


@dataclass
class TypeRateVariance:
    """
    :ivar type_value: Supported values are 'percentage.1P. Future
        release 'amopunt'.
    :ivar value: Represents value of user permitted variance for sell
        success. eg. "5.00" = 5%  variance on the supplier estimated
        total amount response will be successful. 1P.
    :ivar apply: Variance to response amount;  'high', 'low' or 'both.
        1P.
    """
    class Meta:
        name = "typeRateVariance"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    apply: Optional[str] = field(
        default=None,
        metadata={
            "name": "Apply",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeRentalPeriodRentalUnit(Enum):
    DAYS = "Days"
    HOURS = "Hours"


@dataclass
class TypeStartEndTime:
    """
    Used to specify earliest and latest pickup/dropoff times for a vehicle.

    :ivar time: The time in 24 hour clock format.
    :ivar requirement_passed: When true, the time requirement has been
        met.
    :ivar mon:
    :ivar tue:
    :ivar wed:
    :ivar thu:
    :ivar fri:
    :ivar sat:
    :ivar sun:
    """
    class Meta:
        name = "typeStartEndTime"

    time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )
    requirement_passed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequirementPassed",
            "type": "Attribute",
        }
    )
    mon: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mon",
            "type": "Attribute",
        }
    )
    tue: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Tue",
            "type": "Attribute",
        }
    )
    wed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Wed",
            "type": "Attribute",
        }
    )
    thu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Thu",
            "type": "Attribute",
        }
    )
    fri: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Fri",
            "type": "Attribute",
        }
    )
    sat: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sat",
            "type": "Attribute",
        }
    )
    sun: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sun",
            "type": "Attribute",
        }
    )


class TypeVehicleChargeIncludedInRate(Enum):
    NOT_INCLUDED = "NotIncluded"
    INCLUDED_IN_BASE = "IncludedInBase"
    INCLUDED_IN_TOTAL = "IncludedInTotal"


class TypeVehicleChargeType(Enum):
    NO_CHARGE = "NoCharge"
    PERCENT = "Percent"
    RENTAL = "Rental"
    PER_CONTRACT = "PerContract"
    PER_HOUR = "PerHour"
    PER_DAY = "PerDay"
    PER_WEEK = "PerWeek"
    PER_MONTH = "PerMonth"


class TypeVehicleDisclaimer(Enum):
    VEHICLES = "Vehicles"
    SHUTTLE = "Shuttle"
    AGE_REQUIREMENTS = "AgeRequirements"
    ADDL_DRIVER_INFO = "AddlDriverInfo"
    ADDL_DRIVER_FEES = "AddlDriverFees"
    PAYMENT = "Payment"
    GUARANTEE = "Guarantee"
    DEPOSIT = "Deposit"
    VOUCHER = "Voucher"
    LICENSE = "License"
    PICKUP = "Pickup"
    DROP_OFF = "DropOff"
    FUEL = "Fuel"
    GEOGRAPHIC = "Geographic"
    LIABILITIES = "Liabilities"
    SPECIAL_EQUIPMENT = "SpecialEquipment"
    INSURANCE = "Insurance"
    ELIGIBILITY = "Eligibility"
    FEES = "Fees"
    OTHER = "Other"


@dataclass
class TypeVehicleRateDescription:
    """
    :ivar text:
    :ivar name: Optional context name of the text block being returned
        i.e. Room details
    """
    class Meta:
        name = "typeVehicleRateDescription"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )


@dataclass
class TypeVehicleRates:
    """
    :ivar estimated_total_amount: The estimated total amount
    :ivar base_rate: Rate for the entire rent without the required
        charges
    :ivar rate_for_period: The rate for the period
    :ivar drop_off_charge: The additional fee for dropping off a vehicle
        at a different location.
    :ivar young_driver_charge: The additional amount charged for young
        drivers
    :ivar senior_driver_charge: The additional amount charged for senior
        drivers
    :ivar fuel_surcharge: The additional amount charged for fuel
    :ivar extra_mileage_charge: Cost per mile over allowance for rate
    :ivar pay_now: Pay Now is added for Future Functionality
    :ivar pay_later: Pay later is added for Future Functionality
    """
    class Meta:
        name = "typeVehicleRates"

    estimated_total_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedTotalAmount",
            "type": "Attribute",
        }
    )
    base_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseRate",
            "type": "Attribute",
        }
    )
    rate_for_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateForPeriod",
            "type": "Attribute",
        }
    )
    drop_off_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "DropOffCharge",
            "type": "Attribute",
        }
    )
    young_driver_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "YoungDriverCharge",
            "type": "Attribute",
        }
    )
    senior_driver_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeniorDriverCharge",
            "type": "Attribute",
        }
    )
    fuel_surcharge: Optional[str] = field(
        default=None,
        metadata={
            "name": "FuelSurcharge",
            "type": "Attribute",
        }
    )
    extra_mileage_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtraMileageCharge",
            "type": "Attribute",
        }
    )
    pay_now: Optional[str] = field(
        default=None,
        metadata={
            "name": "PayNow",
            "type": "Attribute",
        }
    )
    pay_later: Optional[str] = field(
        default=None,
        metadata={
            "name": "PayLater",
            "type": "Attribute",
        }
    )


class TypeVehicleTypes(Enum):
    """
    :cvar ANY_VEHICLE: Any vehicle - GDS Pseudo Code ACAR
    :cvar ANY2_3_DOOR_VEHICLE: Any 2-3 door vehicle - GDS Pseudo Code
        ALLB
    :cvar ANY2_3_DOOR_PASSENGER_CAR: Any 2-3 door passenger cars - GDS
        Pseudo Code ALBC
    :cvar ANY2_4_DOOR_VEHICLE: Any 2-4 door vehicle - GDS Pseudo Code
        ALLC
    :cvar ANY2_4_DOOR_PASSENGER_CAR: Any 2-4 door passenger cars - GDS
        Pseudo Code ALCC
    :cvar ANY4_5_DOOR_VEHICLE: Any 4-5 door vehicle - GDS Pseudo Code
        ALLD
    :cvar ANY4_DOOR_PASSENGER_CAR: Any 4 door passenger cars - GDS
        Pseudo Code ALDC
    :cvar ANY_ELITE: Any elite - GDS Pseudo Code AELT
    :cvar ANY_COUPE_ROADSTER: Any Coupe and/or Roadster - GDS Pseudo
        Code ACPR
    :cvar ANY_SPECIAL: Any Special - GDS Pseudo Code ASPC
    :cvar ANY_PICK_UP: Any PickUp - GDS Pseudo Code APUP
    :cvar ANY_WAGON: Any Wagon - GDS Pseudo Code AWGN
    :cvar ANY_RECREATIONAL_VEHICLE: Any Recreational Vehicle - GDS
        Pseudo Code AREC
    :cvar ANY_SUV: Any SUV - GDS Pseudo Code ASUV
    :cvar ANY_PASSENGER_VAN: Any Passenger Van - GDS Pseudo Code AVAN
    :cvar ANY6_PASSENGER_VAN_OR_SUV: Any 6 Passenger Van or SUV - GDS
        Pseudo Code ASIX
    :cvar ANY7_PASSENGER_VAN_OR_SUV: Any 7 Passenger Van or SUV - GDS
        Pseudo Code ASEV
    :cvar ANY8_PASSENGER_VAN_OR_SUV: Any 8 Passenger Van or SUV - GDS
        Pseudo Code AEIG
    :cvar ANY4_OR_ALL_WHEEL_DRIVE: Any 4 or all wheel drive- GDS Pseudo
        Code AFWD
    :cvar ANY_ALL_TERRAIN_VEHICLE: Any all Terrain Vehicle- GDS Pseudo
        Code ATRV
    :cvar ANY_COMMERCIAL_TRUCK: Any commercial truck- GDS Pseudo Code
        ACGO
    :cvar ANY_LIMOUSINE: Any Limousine- GDS Pseudo Code ALMO
    :cvar ANY_SPORT: Any Sport- GDS Pseudo Code ASPT
    :cvar ANY_CONVERTIBLE: Any Convertible- GDS Pseudo Code ACNV
    :cvar ANY_SPECIAL_OFFER_VEHICLE: Any Special Offer Vehicle- GDS
        Pseudo Code AOFR
    :cvar ANY_MONOSPACE: Any Monospace- GDS Pseudo Code AMNO
    :cvar ANY_MOTOR_HOME: Any Motor Home- GDS Pseudo Code AMTO
    :cvar ANY2_WHEEL_VEHICLE: Any 2-Wheel Vehicle- GDS Pseudo Code AMCY
    :cvar ANY_CROSSOVER: Any Crossover- GDS Pseudo Code ACRS
    :cvar ALL_MANUAL_TRANSMISSION_VEHICLES: All Manual Transmission
        Vehicles- GDS Pseudo Code AMAN
    :cvar ALL_AUTOMATIC_TRANSMISSION_VEHICLES: All Automatic
        Transmission Vehicles- GDS Pseudo Code AUTO
    :cvar ALL_GASOLINE_VEHICLES: All Gasoline Powered Vehicles- GDS
        Pseudo Code AGAS
    :cvar ALL_PETROL_VEHICLES: All Petrol Powered Vehicles- GDS Pseudo
        Code APET
    :cvar ALL_DIESEL_VEHICLES: All Diesel Powered Vehicles- GDS Pseudo
        Code ADSL
    :cvar ANY_GREEN_VEHICLE: Any Green vehicle (hybrid, electric, LPG,
        hydrogen, multi-fuel)- GDS Pseudo Code AGRN
    :cvar ALL_HYBRID_VEHICLES: All Hybrid Vehicles- GDS Pseudo Code AHYB
    :cvar ALL_ELECTRIC_VEHICLES: All Electric powered vehicles- GDS
        Pseudo Code AELC
    :cvar ALL_HYDROGEN_VEHICLES: All Hydrogen powered vehicles- GDS
        Pseudo Code AHYD
    :cvar ALL_MULTI_FUEL_VEHICLES: All Multi-Fuel powered vehicles- GDS
        Pseudo Code AMFP
    :cvar ALL_LPGVEHICLES: All LPG/Compressed Gas powered vehicles- GDS
        Pseudo Code ACPG
    :cvar ALL_ETHANOL_VEHICLES: All Ethanol powered vehicles   - GDS
        Pseudo Code AETH
    """
    ANY_VEHICLE = "AnyVehicle"
    ANY2_3_DOOR_VEHICLE = "Any2-3DoorVehicle"
    ANY2_3_DOOR_PASSENGER_CAR = "Any2-3DoorPassengerCar"
    ANY2_4_DOOR_VEHICLE = "Any2-4DoorVehicle"
    ANY2_4_DOOR_PASSENGER_CAR = "Any2-4DoorPassengerCar"
    ANY4_5_DOOR_VEHICLE = "Any4-5DoorVehicle"
    ANY4_DOOR_PASSENGER_CAR = "Any4DoorPassengerCar"
    ANY_ELITE = "AnyElite"
    ANY_COUPE_ROADSTER = "AnyCoupe-Roadster"
    ANY_SPECIAL = "AnySpecial"
    ANY_PICK_UP = "AnyPickUp"
    ANY_WAGON = "AnyWagon"
    ANY_RECREATIONAL_VEHICLE = "AnyRecreationalVehicle"
    ANY_SUV = "AnySUV"
    ANY_PASSENGER_VAN = "AnyPassengerVan"
    ANY6_PASSENGER_VAN_OR_SUV = "Any6PassengerVanOrSUV"
    ANY7_PASSENGER_VAN_OR_SUV = "Any7PassengerVanOrSUV"
    ANY8_PASSENGER_VAN_OR_SUV = "Any8PassengerVanOrSUV"
    ANY4_OR_ALL_WHEEL_DRIVE = "Any4OrAllWheelDrive"
    ANY_ALL_TERRAIN_VEHICLE = "AnyAllTerrainVehicle"
    ANY_COMMERCIAL_TRUCK = "AnyCommercialTruck"
    ANY_LIMOUSINE = "AnyLimousine"
    ANY_SPORT = "AnySport"
    ANY_CONVERTIBLE = "AnyConvertible"
    ANY_SPECIAL_OFFER_VEHICLE = "AnySpecialOfferVehicle"
    ANY_MONOSPACE = "AnyMonospace"
    ANY_MOTOR_HOME = "AnyMotorHome"
    ANY2_WHEEL_VEHICLE = "Any2WheelVehicle"
    ANY_CROSSOVER = "AnyCrossover"
    ALL_MANUAL_TRANSMISSION_VEHICLES = "AllManualTransmissionVehicles"
    ALL_AUTOMATIC_TRANSMISSION_VEHICLES = "AllAutomaticTransmissionVehicles"
    ALL_GASOLINE_VEHICLES = "AllGasolineVehicles"
    ALL_PETROL_VEHICLES = "AllPetrolVehicles"
    ALL_DIESEL_VEHICLES = "AllDieselVehicles"
    ANY_GREEN_VEHICLE = "AnyGreenVehicle"
    ALL_HYBRID_VEHICLES = "AllHybridVehicles"
    ALL_ELECTRIC_VEHICLES = "AllElectricVehicles"
    ALL_HYDROGEN_VEHICLES = "AllHydrogenVehicles"
    ALL_MULTI_FUEL_VEHICLES = "AllMultiFuelVehicles"
    ALL_LPGVEHICLES = "AllLPGVehicles"
    ALL_ETHANOL_VEHICLES = "AllEthanolVehicles"


class TypeVehicleVendorLocationType(Enum):
    PICKUP = "Pickup"
    RETURN = "Return"


@dataclass
class AssociatedRemark(TypeAssociatedRemark):
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class CollectionAddress(TypeStructuredAddress):
    """
    An address from which a rental car should be picked up at the end of a rental
    period and a phone number associated with the address.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )


@dataclass
class DeliveryAddress(TypeStructuredAddress):
    """
    An address to which a rental car should be delivered and a phone number
    associated with the address.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )


@dataclass
class LocationInfo:
    """
    :ivar location_address:
    :ivar phone_number:
    :ivar operation_time:
    :ivar shuttle_info:
    :ivar name: A descriptive name (Los Angeles Intl Airport)
    :ivar counter_location: Where is the counter located
    :ivar preferred_option: Preferred Option marker for Location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    location_address: List[LocationAddress] = field(
        default_factory=list,
        metadata={
            "name": "LocationAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    operation_time: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    shuttle_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShuttleInfo",
            "type": "Element",
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
    counter_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "CounterLocation",
            "type": "Attribute",
        }
    )
    preferred_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )


@dataclass
class LocationInformation:
    """
    The type of location and the location address.

    :ivar address: The address of the rental location.
    :ivar location_type: Specifies the type of location, such as city
        center, airport, or near resort.
    :ivar area_group: Unique area group code. like A, B etc.
    :ivar location: Location corresponding to the group.
    :ivar area_type: Location type corresponding to the group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )
    area_group: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaGroup",
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
    area_type: Optional[TypeAreaInfo] = field(
        default=None,
        metadata={
            "name": "AreaType",
            "type": "Attribute",
        }
    )


@dataclass
class Policy(TypeKeyword):
    """Policy category code, e.g. “AGE”.

    Valid for 1P only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class PricedEquip:
    """
    Special Equipment detail and charge for rental.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    equipment: Optional[Equipment] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
        }
    )
    charge: Optional[Charge] = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
        }
    )


@dataclass
class RateInclusions:
    """Provides the list of additional charges included in Rate.

    e.g Tax, Airport Surcharge, CDW etc
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    included_item: List[IncludedItem] = field(
        default_factory=list,
        metadata={
            "name": "IncludedItem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class SupplierRate(TypeVehicleRates):
    """
    :ivar discount_amount: Discount Amount 1P only
    :ivar mandatory_charge_total: Total Mandatory Charges, which may
        include taxes, surcharges, and fees. 1P only.
    :ivar approximate_total: The total sum of all mandatory, optional
        and conditional charges
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    discount_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Attribute",
        }
    )
    mandatory_charge_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "MandatoryChargeTotal",
            "type": "Attribute",
        }
    )
    approximate_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTotal",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleDetail:
    """
    Make, model, etc information about the available vehicles.

    :ivar code: The industry standard code for this vehicle
    :ivar supplier_code: The supplier specific code for this vehicle.
    :ivar passenger_count: Number of passengers this car can hold (e.g.
        4-5)
    :ivar number_of_doors: The number of doors on vehicle.  Ex:
        TwoToThreeDoors, TwoToFourDoors, FourToFiveDoors
    :ivar bag_count: The number of bags
    :ivar class_value:
    :ivar category:
    :ivar air_conditioning: True or False.
    :ivar transmission: Automatic, Manual
    :ivar make_model: The Make and Model description of this vehicle
    :ivar fuel_type: The fuel type of vehicle
    :ivar acriss_vehicle_code: The Association of Car Rental Industry
        System Standards (ACRISS), develops standards to avoid
        misleading information when making a car rental booking online
        or via any electronic means. ACRISS provides an industry
        standard vehicle matrix to define car models ensuring a like to
        like comparison of vehicle. Each ACRISS code defining a car
        model consists of four characters as defined. 1st character
        denotes the vehicle category – based on size, cost, power and
        luxury factor.2nd character defines the vehicle type – chassis
        type (van, SUV, wagon, convertible).3rd character defines the
        transmission and drive – automatic / manual and 2WD / 4WD / AWD.
        4th character defines the fuel type (petrol / diesel / hybrid…)
        and whether air conditioned.Examples are ICAR,ECAR,etc.
    :ivar preferred_option: Preferred Option marker for Location
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
        }
    )
    passenger_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerCount",
            "type": "Attribute",
        }
    )
    number_of_doors: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfDoors",
            "type": "Attribute",
        }
    )
    bag_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "BagCount",
            "type": "Attribute",
        }
    )
    class_value: Optional[TypeVehicleClass] = field(
        default=None,
        metadata={
            "name": "Class",
            "type": "Attribute",
            "required": True,
        }
    )
    category: Optional[TypeVehicleCategory] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    air_conditioning: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
            "required": True,
        }
    )
    transmission: Optional[TypeVehicleTransmission] = field(
        default=None,
        metadata={
            "name": "Transmission",
            "type": "Attribute",
            "required": True,
        }
    )
    make_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "MakeModel",
            "type": "Attribute",
            "required": True,
        }
    )
    fuel_type: Optional[TypeFuel] = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Attribute",
        }
    )
    acriss_vehicle_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcrissVehicleCode",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    preferred_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleDisclaimer:
    """
    Textual information related to this rental location.

    :ivar value:
    :ivar type_value: The disclaimer category
    :ivar sub_type: Extra information about this category of disclaimer
    :ivar description: A verbal description of this disclaimer
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: Optional[TypeVehicleDisclaimer] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    sub_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubType",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleModifier:
    """
    :ivar air_conditioning: Request vehicles with Air Conditioning Valid
        values: true, false.
    :ivar transmission_type: Requested Transmission Type. Valid
        Values:  Automatic, Automatic4WD, ManualAWD, AutomaticAWD,
        Manual, Manual4WD.
    :ivar vehicle_class: Class of vehicle
    :ivar category: Category of vehicle. Each supplier decides how these
        categories map to a vehicle class.
    :ivar door_count: The number of doors on vehicle.  Ex:
        TwoToThreeDoors, TwoToFourDoors, FourToFiveDoors
    :ivar fuel_type: The fuel type of vehicle
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    air_conditioning: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
        }
    )
    transmission_type: Optional[TypeVehicleTransmission] = field(
        default=None,
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
        }
    )
    vehicle_class: Optional[TypeVehicleClass] = field(
        default=None,
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
        }
    )
    category: Optional[TypeVehicleCategory] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    door_count: Optional[TypeDoorCount] = field(
        default=None,
        metadata={
            "name": "DoorCount",
            "type": "Attribute",
        }
    )
    fuel_type: Optional[TypeFuel] = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Attribute",
        }
    )


@dataclass
class VehiclePickupDateLocation:
    """Used to update PickupDateTime and location of an existing Vehicle Booking.

    1g/1v only supports modification of PickupDateTime. PickupDateTime
    cannot be deleted.

    :ivar pickup_date_time: Providers: 1g/1v/1p
    :ivar pickup_location: Providers: 1p
    :ivar pickup_location_type: Providers: 1p
    :ivar pickup_location_number: Providers: 1p
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    pickup_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PickupDateTime",
            "type": "Attribute",
        }
    )
    pickup_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickupLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    pickup_location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "PickupLocationType",
            "type": "Attribute",
        }
    )
    pickup_location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickupLocationNumber",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleReturnDateLocation:
    """Used to update Return Location and Return Date of existing Vehicle Booking.

    Modify operation : Only modification of ReturnDateTime is supported.
    Deletion of ReturnDateTime is not supported.
    If values passed in ReturnLocation, ReturnLocationType and
    ReturnLocationNumber are exactly same as PickupLocation,
    PickupLocationType and PickupLocationNumber of existing booking then
    ReturnLocation, ReturnLocationType and ReturnLocationNumber will be
    deleted.
    If values passed in ReturnLocation, ReturnLocationType and
    ReturnLocationNumber are not same as PickupLocation,
    PickupLocationType and PickupLocationNumber of existing booking then ReturnLocation,
    ReturnLocationType and ReturnLocationNumber will be updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    return_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnDateTime",
            "type": "Attribute",
        }
    )
    return_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    return_location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "ReturnLocationType",
            "type": "Attribute",
        }
    )
    return_location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLocationNumber",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleType:
    """
    A standard list or classification of vehicle types .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    value: Optional[TypeVehicleTypes] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class VehicleTypeIdentifier:
    """Used to update Vehicle segment details of existing Vehicle Booking.

    Modify operation : Only modification of Vehicle segment details is supported.

    :ivar air_conditioning:
    :ivar transmission_type:
    :ivar vehicle_class: Class of vehicle
    :ivar category: Category of vehicle. Each supplier decides how these
        categories map to a vehicle class.
    :ivar door_count: The number of doors on vehicle.  Ex:
        TwoToThreeDoors, TwoToFourDoors, FourToFiveDoors
    :ivar fuel_type: The fuel type of vehicle
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    air_conditioning: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
            "required": True,
        }
    )
    transmission_type: Optional[TypeVehicleTransmission] = field(
        default=None,
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
        }
    )
    vehicle_class: Optional[TypeVehicleClass] = field(
        default=None,
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
        }
    )
    category: Optional[TypeVehicleCategory] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    door_count: Optional[TypeDoorCount] = field(
        default=None,
        metadata={
            "name": "DoorCount",
            "type": "Attribute",
        }
    )
    fuel_type: Optional[TypeFuel] = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Attribute",
        }
    )


@dataclass
class TypeDepositGuarantee:
    """
    The deposit and guarantee information for a vehicle rental.

    :ivar purpose: Specifies if this is guarantee, deposit and
        Prepayment information. Values: “Guarantee”, “Deposit”,
        “PrePayment” “Other”.
    :ivar type_value: Specifies if deposit or guarantee rule is for a
        specified amount, the amount for a specific number of days or a
        percentage of the rental.
    :ivar amount: The amount of money required for a guarantee or
        deposit.
    :ivar percent: The percentage of the rental amount for the guarantee
        or deposit.
    :ivar due_date: The date a deposit is due.
    :ivar number_of_days: Specifies the number of days from booking or
        prior to pickup by which the deposit should be made.
    :ivar option_type: Specifies if the number of days is after booking
        or prior to pickup.
    :ivar required: If “true” a Guarantee, Deposit or Prepayment is
        required. 1P, 1G, 1V only.
    :ivar requirement_passed: If true, the rental information passes the
        guarantee or deposit requirements.
    """
    class Meta:
        name = "typeDepositGuarantee"

    purpose: Optional[TypeReserveRequirement] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: Optional[TypeDepositGuaranteeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    percent: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percent",
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
    number_of_days: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfDays",
            "type": "Attribute",
        }
    )
    option_type: Optional[TypeDepositGuaranteeOptionType] = field(
        default=None,
        metadata={
            "name": "OptionType",
            "type": "Attribute",
        }
    )
    required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Required",
            "type": "Attribute",
        }
    )
    requirement_passed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequirementPassed",
            "type": "Attribute",
        }
    )


@dataclass
class TypePaymentInformation:
    """
    :ivar voucher:
    :ivar billing_number: A Billing Number that may be associated to the
        Voucher.
    :ivar billing_reference_number: A Number Assigned for Billing
        reconciliation processes that may also include a Corporate
        Account ID
    :ivar pre_payment: Amount paid in advance for  vehicle reservation.
        Can contain other non Money information to the vehicle supplier.
    """
    class Meta:
        name = "typePaymentInformation"

    voucher: Optional[TypeVoucherInformation] = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    billing_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BillingNumber",
            "type": "Attribute",
        }
    )
    billing_reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BillingReferenceNumber",
            "type": "Attribute",
        }
    )
    pre_payment: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrePayment",
            "type": "Attribute",
            "max_length": 90,
        }
    )


@dataclass
class TypePickupDateLocation:
    """
    A complexType for the pickup date, location, and location type.

    :ivar date: The start date for the vehicle rental.
    :ivar location: The location (airport code) at which the vehicle
        will be picked up.
    :ivar location_type: The type of location requested, such as resort,
        city center.
    :ivar pickup_location_number: Unique identifier for vehicle location
    """
    class Meta:
        name = "typePickupDateLocation"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
            "required": True,
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
    location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )
    pickup_location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickupLocationNumber",
            "type": "Attribute",
        }
    )


@dataclass
class TypeRateInfo:
    """
    Additional information for extra days or hours.

    :ivar rate_for_period: The rate for the period
    :ivar number_of_periods: Define how many periods (e.g. number of
        days or weeks)
    :ivar unlimited_mileage: True if unlimited miles allowed. Not set if
        unknown
    :ivar mileage_allowance: Number of miles or kilometers allowed for
        rate if not unlimited
    :ivar units: Describes distance units for MileageAllowance or
        ExtraMileageCharge
    :ivar extra_mileage_charge: Cost per mile or kilometer over
        allowance for rate
    """
    class Meta:
        name = "typeRateInfo"

    rate_for_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateForPeriod",
            "type": "Attribute",
        }
    )
    number_of_periods: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfPeriods",
            "type": "Attribute",
        }
    )
    unlimited_mileage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Attribute",
        }
    )
    mileage_allowance: Optional[int] = field(
        default=None,
        metadata={
            "name": "MileageAllowance",
            "type": "Attribute",
        }
    )
    units: Optional[TypeDistance] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Attribute",
        }
    )
    extra_mileage_charge: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtraMileageCharge",
            "type": "Attribute",
        }
    )


@dataclass
class TypeRentalPeriod:
    """
    Rental period information concerning minimum and max rental periods.

    :ivar rental_unit: The rental unit period, such as days or hours.
    :ivar length: The number of rental units.
    :ivar requirement_passed: If true, the rental period requirements
        have been met.
    """
    class Meta:
        name = "typeRentalPeriod"

    rental_unit: Optional[TypeRentalPeriodRentalUnit] = field(
        default=None,
        metadata={
            "name": "RentalUnit",
            "type": "Attribute",
            "required": True,
        }
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Attribute",
            "required": True,
        }
    )
    requirement_passed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequirementPassed",
            "type": "Attribute",
        }
    )


@dataclass
class TypeVehicleCharge:
    """
    Charges associated with a vehicle rental.

    :ivar amount: The amount of the charge.
    :ivar percentage: The amount of the charge in percentage.
    :ivar category: The type of charge information for the vehicle
        rental.
    :ivar name: Identifies the type of charge information for the
        category. For 1P , when category is “Special”, Name attribute
        will have Special Equipment code enumeration, which can be used
        in booking vehicle on 1P host.
    :ivar description: Special Equipment Charge description text of the
        rental charge. 1P only.
    :ivar type_value: Used to specify how a charge is applied, such as
        per rental, per day, etc.
    :ivar included_in_rate: Specifies whether the charge is included in
        the rate and if it is, if it is in the base or total rate.
    """
    class Meta:
        name = "typeVehicleCharge"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    type_value: Optional[TypeVehicleChargeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    included_in_rate: Optional[TypeVehicleChargeIncludedInRate] = field(
        default=None,
        metadata={
            "name": "IncludedInRate",
            "type": "Attribute",
        }
    )


@dataclass
class TypeVehicleLocationInformation:
    """
    Valid for VehicleRulesRsp 1P only.

    :ivar address: Pickup/Return Location Address.Data is not always
        returned by the vendor.
    :ivar phone_number: Pickup location phone numbers.Data is not always
        returned by the vendor.
    :ivar operation_time: Pickup/Return Location Hours of operation.
        Data is not always returned by the vendor.
    :ivar location_name: Pickup/Return Location Name.
    :ivar counter_location: Pickup CounterLocation Name .
    :ivar vendor_code: Pickup/Return Location Vendor Code.
    :ivar location_code: Pickup/Return Location City/Airport  Code .
    :ivar location_type: Pickup/Return Location .
    :ivar location_number: Pickup/Return Location Number.
    """
    class Meta:
        name = "typeVehicleLocationInformation"

    address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    phone_number: List[PhoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 3,
        }
    )
    operation_time: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 100,
        }
    )
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationName",
            "type": "Attribute",
        }
    )
    counter_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "CounterLocation",
            "type": "Attribute",
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
    location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )
    location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationNumber",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        }
    )


@dataclass
class TypeVehicleSearchDistance:
    """
    :ivar units: MI or KM. Defaults to miles
    :ivar direction: Valid values: N, S, E, W, NE, NW, SE, SW.  Default:
        direction will not be specified.
    :ivar min_distance: Minimum distance.  Defaults to 0.
    :ivar max_distance: Maximum distance
    """
    class Meta:
        name = "typeVehicleSearchDistance"

    units: Optional[TypeDistance] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Attribute",
        }
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    min_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinDistance",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    max_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxDistance",
            "type": "Attribute",
            "required": True,
            "max_inclusive": 999,
        }
    )


@dataclass
class TypeVehicleVendorLocation(TypeVendorLocation):
    """
    :ivar location_type: Rental counter location such as Terminal,
        CityCenterDowntown,
    :ivar location_code: Airport or City Code
    :ivar type_value: Pickup or Return
    """
    class Meta:
        name = "typeVehicleVendorLocation"

    location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )
    location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    type_value: Optional[TypeVehicleVendorLocationType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class PaymentInformation(TypePaymentInformation):
    """
    The payment information for a vehicle reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleDateLocation:
    """
    :ivar vendor_location: Specific vendor rental locations.  Applicable
        only for VehicleSearchAvailability.
    :ivar pickup_date_time:
    :ivar pickup_location: PickUpLocation is optional if Reference point
        is specified
    :ivar return_date_time:
    :ivar return_location: If not specified, the PickupLocation will be
        assumed
    :ivar pickup_location_type: Required if use VendorLocationID. Ex:
        Terminal, ShuttleOnAirport, ShuttleOffAirport, RailwayStation,
        Hotel, CarDealer, CityCenterDowntown, EastOfCityCenter,
        SouthOfCityCenter, WestOfCityCenter, NorthOfCityCenter,
        PortOrFerry, NearResort, Airport, Unknown
    :ivar return_location_type: Defaults to Pickup Location. Same
        options as Pickup Location.
    :ivar pickup_location_number: The value of this attribute should be
        the same as the value of VendorLocationID returned as part of
        VendorLocation@VendorLocationID in a VehicleLocationRsp.
    :ivar return_location_number:
    :ivar key:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor_location: List["VehicleDateLocation.VendorLocation"] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    pickup_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickupDateTime",
            "type": "Attribute",
            "required": True,
        }
    )
    pickup_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickupLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    return_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnDateTime",
            "type": "Attribute",
            "required": True,
        }
    )
    return_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    pickup_location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "PickupLocationType",
            "type": "Attribute",
        }
    )
    return_location_type: Optional[TypeVehicleLocation] = field(
        default=None,
        metadata={
            "name": "ReturnLocationType",
            "type": "Attribute",
        }
    )
    pickup_location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickupLocationNumber",
            "type": "Attribute",
        }
    )
    return_location_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLocationNumber",
            "type": "Attribute",
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
    class VendorLocation(TypeVehicleVendorLocation):
        distance: Optional[Distance] = field(
            default=None,
            metadata={
                "name": "Distance",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            }
        )


@dataclass
class VehicleLocation:
    """
    The information for a rental car location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vendor_location: Optional[VendorLocation] = field(
        default=None,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    coordinate_location: Optional[CoordinateLocation] = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    location_information: Optional[LocationInformation] = field(
        default=None,
        metadata={
            "name": "LocationInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class VehiclePickupLocation:
    """
    A container for Vehicle Location ,Vendor and Vehicle Modifier.

    :ivar vendor:
    :ivar vehicle_modifier:
    :ivar pick_up_location: The location (city or airport code) at which
        the vehicle will be picked up.
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
    vehicle_modifier: List[VehicleModifier] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    pick_up_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "PickUpLocation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )


@dataclass
class VehiclePolicy:
    """Policy information provided by the Vehicle Supplier.

    Usually relative to a specific location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_disclaimer: List[VehicleDisclaimer] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDisclaimer",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_detail: List[VehicleDetail] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleRate:
    """
    Rate summary.

    :ivar supplier_rate:
    :ivar rate_variance: Used on VehicleCreateReservationReq ONLY.
        @MandatoryRateMatch ='true' is required for this element to be
        applied. 1P.
    :ivar approximate_rate: Monetary amounts expressed in another
        currency
    :ivar vehicle_charge: Charges associated with the vehicle rental.
    :ivar vehicle_rate_description:
    :ivar rate_host_indicator:
    :ivar hourly_late_charge:
    :ivar daily_late_charge:
    :ivar priced_equip:
    :ivar rate_inclusions:
    :ivar weekly_late_charge: Extra Week Charges information. Supported
        providers:1P only
    :ivar print_text: Informational text provided by the supplier that
        may be related to the reservation. This is applicable in
        response messages only, 1p only.
    :ivar rate_period: The period for the rate (daily, weekly, etc)
    :ivar number_of_periods: Define how many periods (e.g. number of
        days or weeks)
    :ivar unlimited_mileage: True if unlimited miles for rate
    :ivar mileage_allowance: Only set if UnlimitedMileage is false.
        Number of miles allowed for rate
    :ivar units: Describes distance units for MileageAllowance or
        ExtraMileageCharge
    :ivar rate_source: The rate source indicator for GWS
    :ivar rate_availability: Rate is available to sell, Need to Call or
        Closed
    :ivar required_charges:
    :ivar rate_code: Rate Code of the vehicle. Supported Providers
        1P,1G,1V.
    :ivar requested_rate_code_applied: The requested Rate Code applied
        to the Rate. Valid values: "true", "false", "unknown". Supported
        Providers 1P.
    :ivar rate_category: The category of this rate (Best, etc)
    :ivar discount_number: Corporate Discount number used to request a
        specified discount. Supported Providers Requests: 1P,1G,1V,
        Responses only 1P.
    :ivar discount_number_applied: Discount Number has been applied to
        the Rate. Valid values: "true", "false", "unknown". Supported
        Providers 1P.
    :ivar vendor_code:
    :ivar rate_guaranteed: Guarantee indicator for vehicle rate.
    :ivar rate_code_period: RateCodePeriod
    :ivar promotional_code: Specific coupon or promotion code. Providers
        1P,1V,1G.
    :ivar promotional_code_applied: Promotional/Coupon Number has been
        applied to the Rate. Valid values: "true", "false", "unknown".
        Supported Providers 1P.
    :ivar tour_code: Tour Number for the Vehicle Booking
    :ivar tour_code_applied: Tour Code Number has been applied to the
        Rate. Valid values: "true", "false", "unknown". Supported
        Providers 1P.
    :ivar rate_guarantee_type: To identify whether rate is already
        guaranteed or rate quoted or agent entered
    :ivar required_payment: Returns Payment information required by
        vendor at the time og booking.
    :ivar drop_off_charges_included: If true: Drop off charges are
        included. If false, not included. If not specified, additional
        drop off charges MAY apply (but this has not been confirmed by
        vendor)
    :ivar corporate_rate: If "true" a Corporate Discount has been
        applied to the rate.  Applicable to 1P
    :ivar advanced_booking: Indicates the number of Hours or Days a rate
        must be booked in advance. Values are for Days = number followed
        by “D” e.g., "002D" and Hours = number followed by “H” e.g.,
        002H” 1P/1G/1V only.
    :ivar rental_restriction: RentalRestriction attribute value is true
        if vehicle rate has rental restrictions. Rental restrictions can
        be obtained from the Vehicle Rules. 1P only.
    :ivar flight_restriction: Flight restriction indicator is true if
        flight information is required at booking. 1P/1G/1V only.
    :ivar card_number: Vehicle Loyalty Card Number. Supported Provider
        1P.
    :ivar card_number_applied: Loyalty Card Number has been applied to
        the Rate. Values: "true", "false", "unknown". Supported
        Providers 1P.
    :ivar rate_qualifier_ind: Indicates whether rates comply with CD,
        ID, or Drop Off requested. 1 is fully qualified, 2 is partly
        qualified, and 3 is other rates. 1G, 1V only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    supplier_rate: Optional[SupplierRate] = field(
        default=None,
        metadata={
            "name": "SupplierRate",
            "type": "Element",
        }
    )
    rate_variance: Optional[TypeRateVariance] = field(
        default=None,
        metadata={
            "name": "RateVariance",
            "type": "Element",
        }
    )
    approximate_rate: Optional[TypeVehicleRates] = field(
        default=None,
        metadata={
            "name": "ApproximateRate",
            "type": "Element",
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
    vehicle_rate_description: List[TypeVehicleRateDescription] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRateDescription",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    rate_host_indicator: Optional[TypeRateHostIndicator] = field(
        default=None,
        metadata={
            "name": "RateHostIndicator",
            "type": "Element",
        }
    )
    hourly_late_charge: Optional[TypeRateInfo] = field(
        default=None,
        metadata={
            "name": "HourlyLateCharge",
            "type": "Element",
        }
    )
    daily_late_charge: Optional[TypeRateInfo] = field(
        default=None,
        metadata={
            "name": "DailyLateCharge",
            "type": "Element",
        }
    )
    priced_equip: List[PricedEquip] = field(
        default_factory=list,
        metadata={
            "name": "PricedEquip",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rate_inclusions: Optional[RateInclusions] = field(
        default=None,
        metadata={
            "name": "RateInclusions",
            "type": "Element",
        }
    )
    weekly_late_charge: Optional[TypeRateInfo] = field(
        default=None,
        metadata={
            "name": "WeeklyLateCharge",
            "type": "Element",
        }
    )
    print_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrintText",
            "type": "Element",
        }
    )
    rate_period: Optional[TypeRateTimePeriod] = field(
        default=None,
        metadata={
            "name": "RatePeriod",
            "type": "Attribute",
        }
    )
    number_of_periods: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfPeriods",
            "type": "Attribute",
        }
    )
    unlimited_mileage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Attribute",
        }
    )
    mileage_allowance: Optional[int] = field(
        default=None,
        metadata={
            "name": "MileageAllowance",
            "type": "Attribute",
        }
    )
    units: Optional[TypeDistance] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Attribute",
        }
    )
    rate_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateSource",
            "type": "Attribute",
        }
    )
    rate_availability: Optional[TypeRateAvailability] = field(
        default=None,
        metadata={
            "name": "RateAvailability",
            "type": "Attribute",
        }
    )
    required_charges: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredCharges",
            "type": "Attribute",
        }
    )
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    requested_rate_code_applied: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "RequestedRateCodeApplied",
            "type": "Attribute",
        }
    )
    rate_category: Optional[TypeRateCategory] = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Attribute",
        }
    )
    discount_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    discount_number_applied: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "DiscountNumberApplied",
            "type": "Attribute",
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
    rate_guaranteed: bool = field(
        default=False,
        metadata={
            "name": "RateGuaranteed",
            "type": "Attribute",
        }
    )
    rate_code_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCodePeriod",
            "type": "Attribute",
        }
    )
    promotional_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PromotionalCode",
            "type": "Attribute",
        }
    )
    promotional_code_applied: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "PromotionalCodeApplied",
            "type": "Attribute",
        }
    )
    tour_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        }
    )
    tour_code_applied: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "TourCodeApplied",
            "type": "Attribute",
        }
    )
    rate_guarantee_type: Optional[TypeRateGuarantee] = field(
        default=None,
        metadata={
            "name": "RateGuaranteeType",
            "type": "Attribute",
        }
    )
    required_payment: Optional[VehicleRateRequiredPayment] = field(
        default=None,
        metadata={
            "name": "RequiredPayment",
            "type": "Attribute",
        }
    )
    drop_off_charges_included: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DropOffChargesIncluded",
            "type": "Attribute",
        }
    )
    corporate_rate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CorporateRate",
            "type": "Attribute",
        }
    )
    advanced_booking: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdvancedBooking",
            "type": "Attribute",
        }
    )
    rental_restriction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RentalRestriction",
            "type": "Attribute",
        }
    )
    flight_restriction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FlightRestriction",
            "type": "Attribute",
        }
    )
    card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 36,
        }
    )
    card_number_applied: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "CardNumberApplied",
            "type": "Attribute",
        }
    )
    rate_qualifier_ind: Optional[int] = field(
        default=None,
        metadata={
            "name": "RateQualifierInd",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleSearchModifiers:
    """
    Controls and switches for the Vehicle Search request.

    :ivar permitted_vendors:
    :ivar prohibited_vendors:
    :ivar vehicle_modifier:
    :ivar vehicle_type:
    :ivar rate_modifiers:
    :ivar rate_host_indicator:
    :ivar loyalty_card:
    :ivar reference_point: Search Car by reference point
    :ivar booking_source: Supported Providers: 1P. Only type IataNumber
        is valid.
    :ivar special_equipment: Allows vehicle search with Special
        equipment by specifying special equipment type. e.g. “BikeRack”.
        Not supported by all vendors. 1P only.
    :ivar search_distance: Distance from search location. Supported for
        standard car search.  Providers: 1g/1v
    :ivar policy:
    :ivar driver_info: Use to specify Driver's age. Supported Providers:
        1P.
    :ivar key:
    :ivar preferred_currency: Alternate currency
    :ivar unlimited_mileage: Set to true to search for rates with
        unlimited mileage.Defaults to false.
    :ivar rate_category: The category of this rate (Best, etc)
    :ivar rate_guaranteed: Guarantee indicator for vehicle rate.
    :ivar rate_period: The period for the rate code (daily, weekly, etc)
    :ivar sellable_rates_only: Set to true to search for sellable rates
        only.  Default is to search for all rates.  Providers: 1p
    :ivar return_source_currency: Set to true to return the rate details
        in Vendor filed currency. Defaults to false. Supported
        Providers: 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    permitted_vendors: Optional["VehicleSearchModifiers.PermittedVendors"] = field(
        default=None,
        metadata={
            "name": "PermittedVendors",
            "type": "Element",
        }
    )
    prohibited_vendors: Optional["VehicleSearchModifiers.ProhibitedVendors"] = field(
        default=None,
        metadata={
            "name": "ProhibitedVendors",
            "type": "Element",
        }
    )
    vehicle_modifier: List[VehicleModifier] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_type: List[TypeVehicleTypes] = field(
        default_factory=list,
        metadata={
            "name": "VehicleType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rate_modifiers: List[RateModifiers] = field(
        default_factory=list,
        metadata={
            "name": "RateModifiers",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rate_host_indicator: Optional[TypeRateHostIndicator] = field(
        default=None,
        metadata={
            "name": "RateHostIndicator",
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
    reference_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_length": 30,
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
    special_equipment: List[SpecialEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        }
    )
    search_distance: Optional[TypeVehicleSearchDistance] = field(
        default=None,
        metadata={
            "name": "SearchDistance",
            "type": "Element",
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
    driver_info: Optional[DriverInfo] = field(
        default=None,
        metadata={
            "name": "DriverInfo",
            "type": "Element",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    preferred_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferredCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    unlimited_mileage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Attribute",
        }
    )
    rate_category: Optional[TypeRateCategory] = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Attribute",
        }
    )
    rate_guaranteed: bool = field(
        default=False,
        metadata={
            "name": "RateGuaranteed",
            "type": "Attribute",
        }
    )
    rate_period: Optional[TypeRateTimePeriod] = field(
        default=None,
        metadata={
            "name": "RatePeriod",
            "type": "Attribute",
        }
    )
    sellable_rates_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SellableRatesOnly",
            "type": "Attribute",
        }
    )
    return_source_currency: bool = field(
        default=False,
        metadata={
            "name": "ReturnSourceCurrency",
            "type": "Attribute",
        }
    )

    @dataclass
    class PermittedVendors:
        """
        :ivar vendor: 1G/1V max 4 vendors, 1P max 99 vendors
        """
        vendor: List[Vendor] = field(
            default_factory=list,
            metadata={
                "name": "Vendor",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedVendors:
        vendor: List[Vendor] = field(
            default_factory=list,
            metadata={
                "name": "Vendor",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )


@dataclass
class Vehicle:
    """
    Information related to single vehicle.

    :ivar policy_codes_list: A list of codes that indicate why an item
        was determined to be ‘out of policy’.
    :ivar vehicle_rate:
    :ivar vendor_code:
    :ivar air_conditioning: True or False.
    :ivar transmission_type: Automatic, Manual
    :ivar vehicle_class: Class of vehicle
    :ivar category: Category of vehicle. Each supplier decides how these
        categories map to a vehicle class.
    :ivar description: Car type Description such as 'CHRYSLER SEBRING OR
        SIMILAR'
    :ivar door_count: The number of doors on vehicle.  Ex:
        TwoToThreeDoors, TwoToFourDoors, FourToFiveDoors
    :ivar location: Location of the Vehicle or Counter
    :ivar counter_location_code: Four character Code to identify the
        Location of the Rental Counter, e.g. OMSO, PHON.
    :ivar vendor_location_key: Identifies the specific vendor location
    :ivar vendor_name: The vendor's name
    :ivar alternate_vendor: A vendor renting the vehicle on behalf of
        another company
    :ivar fuel_type: The fuel type of vehicle
    :ivar acriss_vehicle_code: The Association of Car Rental Industry
        System Standards (ACRISS), develops standards to avoid
        misleading information when making a car rental booking online
        or via any electronic means. ACRISS provides an industry
        standard vehicle matrix to define car models ensuring a like to
        like comparison of vehicle. Each ACRISS code defining a car
        model consists of four characters as defined. 1st character
        denotes the vehicle category – based on size, cost, power and
        luxury factor.2nd character defines the vehicle type – chassis
        type (van, SUV, wagon, convertible).3rd character defines the
        transmission and drive – automatic / manual and 2WD / 4WD / AWD.
        4th character defines the fuel type (petrol / diesel / hybrid…)
        and whether air conditioned.Examples are ICAR,ECAR,etc.
    :ivar key:
    :ivar return_at_pickup: Indicates whether vehicle can be returned at
        any location or pickup point only. If ReturnAtPickup = false
        then vehicle can be returned at any location else if
        ReturnAtPickup = true, vehicle should be returned in Pickup
        point only. Supported Providers : 1G/1V
    :ivar in_policy: This attribute will be used to indicate if a fare
        or rate has been determined to be ‘in policy’ based on the
        associated policy settings.
    :ivar policy_code: This attribute is used to provide a code that can
        be used to determine why an item was determined to be ‘out of
        policy’.
    :ivar preferred_option: This attribute is used to indicate if the
        vendors responsible for the fare or rate being returned have
        been determined to be ‘preferred’ based on the associated policy
        settings.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    policy_codes_list: Optional[TypePolicyCodesList] = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        }
    )
    vehicle_rate: Optional[VehicleRate] = field(
        default=None,
        metadata={
            "name": "VehicleRate",
            "type": "Element",
        }
    )
    vendor_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    air_conditioning: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Attribute",
            "required": True,
        }
    )
    transmission_type: Optional[TypeVehicleTransmission] = field(
        default=None,
        metadata={
            "name": "TransmissionType",
            "type": "Attribute",
            "required": True,
        }
    )
    vehicle_class: Optional[TypeVehicleClass] = field(
        default=None,
        metadata={
            "name": "VehicleClass",
            "type": "Attribute",
            "required": True,
        }
    )
    category: Optional[TypeVehicleCategory] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    door_count: Optional[TypeDoorCount] = field(
        default=None,
        metadata={
            "name": "DoorCount",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
        }
    )
    counter_location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CounterLocationCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        }
    )
    vendor_location_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorLocationKey",
            "type": "Attribute",
        }
    )
    vendor_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    alternate_vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateVendor",
            "type": "Attribute",
        }
    )
    fuel_type: Optional[TypeFuel] = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Attribute",
        }
    )
    acriss_vehicle_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcrissVehicleCode",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    return_at_pickup: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnAtPickup",
            "type": "Attribute",
        }
    )
    in_policy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InPolicy",
            "type": "Attribute",
        }
    )
    policy_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "PolicyCode",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 9999,
        }
    )
    preferred_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleReservation(BaseReservation):
    """
    :ivar booking_traveler_ref:
    :ivar reservation_name:
    :ivar email:
    :ivar phone_number:
    :ivar vehicle_date_location:
    :ivar vehicle:
    :ivar special_equipment:
    :ivar vehicle_special_request:
    :ivar payment_information:
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
    :ivar third_party_information:
    :ivar sell_message:
    :ivar supplier_code:
    :ivar booking_confirmation:
    :ivar status:
    :ivar provider_reservation_info_ref: Provider reservation reference
        key.
    :ivar passive_provider_reservation_info_ref: Passive Provider
        reservation reference key.
    :ivar travel_order: To identify the appropriate sequence for
        Air/Car/Hotel segments based on travel dates.
    :ivar provider_segment_order: To identify the appropriate travel
        sequence for Air/Car/Hotel/Rail segments/reservations in the
        provider reservation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
            "required": True,
        }
    )
    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "required": True,
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
    vehicle_special_request: Optional[VehicleSpecialRequest] = field(
        default=None,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
        }
    )
    payment_information: Optional[PaymentInformation] = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
        }
    )
    delivery_address: Optional[DeliveryAddress] = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
        }
    )
    collection_address: Optional[CollectionAddress] = field(
        default=None,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
        }
    )
    flight_arrival_information: Optional[FlightArrivalInformation] = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
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
    associated_remark: List[AssociatedRemark] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
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
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    sell_message: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SellMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
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
    provider_segment_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
        }
    )


@dataclass
class VehicleWithMediaItems:
    """
    A container for displaying vehicle details,media urls and errors.

    :ivar vehicle:
    :ivar media_item: Photos and other media urls for the item
        referenced above.
    :ivar media_result_message: Errors, Warnings and informational
        messages for the property referenced above.
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
    media_item: List[MediaItem] = field(
        default_factory=list,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    media_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "name": "MediaResultMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
