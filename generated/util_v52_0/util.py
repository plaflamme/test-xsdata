from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from generated.air_v52_0.air import AirSegment
from generated.common_v52_0.common import (
    AccountCode,
    AccountingRemark,
    Airport,
    Carrier,
    CorporateDiscountId,
    CreditCard,
    CreditCardAuth,
    Email,
    Endorsement,
    FormOfPayment,
    FormOfPaymentRef,
    GeneralRemark,
    Mco,
    Name,
    RailLocation,
    ServiceFeeInfo,
    TypeDoorCount,
    TypeElementStatus,
    TypeFuel,
    TypeMcostatus,
    TypeMcotype,
    TypeRateCategory,
    TypeTimeRange,
    TypeTimeSpec,
    TypeVehicleCategory,
    TypeVehicleClass,
    TypeVehicleLocation,
    TypeVehicleTransmission,
)
from generated.common_v52_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AdditionalElement:
    """
    To add or update reference data master records.

    :ivar name: Please provide other column names. This should match
        with exact database column name
    :ivar value: Please provide corresponding value of the Name field
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: Optional[str] = field(
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
class AirUpsellDelete:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    qualify_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualifyRef",
            "type": "Attribute",
        }
    )
    offer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        }
    )


@dataclass
class BrandedFareSearchModifier:
    """
    Search modifiers for Upsell.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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


class ContentProviderAgencyCredentials(Enum):
    REQUIRED = "Required"
    OPTIONAL = "Optional"
    PROHIBITED = "Prohibited"


@dataclass
class CurrencyConversion:
    """
    :ivar from_value: From Currency Value for the Conversion
    :ivar to: To Currency Value for the Conversion
    :ivar original_amount: Amount to be converted
    :ivar converted_amount: Amount after the convertion
    :ivar bank_selling_rate: Currency Conversion Rate
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    original_amount: Optional[float] = field(
        default=None,
        metadata={
            "name": "OriginalAmount",
            "type": "Attribute",
        }
    )
    converted_amount: Optional[float] = field(
        default=None,
        metadata={
            "name": "ConvertedAmount",
            "type": "Attribute",
        }
    )
    bank_selling_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "BankSellingRate",
            "type": "Attribute",
        }
    )


@dataclass
class EffectiveDate:
    """Effective Date range.

    For specific date usage set both limits to same value.

    :ivar earliest_date: Earliest date of the Effective date
    :ivar latest_date: Latest date of the Effective date
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    earliest_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    latest_date: str = field(
        default="9999-12-31",
        metadata={
            "name": "LatestDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )


@dataclass
class ExpirationDate:
    """Expiration Date range.

    For specific date usage set both limits to same value.

    :ivar earliest_date: Earliest date of the Expiration date
    :ivar latest_date: Latest date of the Expiration date
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    earliest_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EarliestDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    latest_date: str = field(
        default="9999-12-31",
        metadata={
            "name": "LatestDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )


@dataclass
class FareFamilyCriteria:
    """
    It is a branded Fare for a carrier and given fare basis code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 32,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "max_length": 20,
        }
    )


@dataclass
class FareFamilyDelete:
    """
    Branded fare admin request element to delete a FareFamily for the given
    FareFamilyRef.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareFamilyRef",
            "type": "Attribute",
            "required": True,
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
class FlightCriteria:
    """
    Search criterion for UniversalRecordPolicyDataReq.

    :ivar value:
    :ivar carrier: Air segment carrier
    :ivar flight_number: Air segment flight number
    :ivar departure_date: AirSegment Departure date
    :ivar origin: AirSegment Origin
    :ivar destination: AirSegment destination
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    value: str = field(
        default="",
        metadata={
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
        }
    )
    departure_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "required": True,
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


@dataclass
class HotelUpsellDelete:
    """
    Delete command for deleting HotelUpsellQualify,HotelUpsellOffer using there
    persisted keys.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    qualify_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualifyRef",
            "type": "Attribute",
        }
    )
    offer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        }
    )


class MirReportRetrieveReqReportFormat(Enum):
    TRAMS = "TRAMS"
    CLIENTBASE = "CLIENTBASE"
    TRISEPT = "TRISEPT"


@dataclass
class ReferenceDataItem:
    """
    :ivar additional_info: Any additional information specific to a type
        of value being returned.
    :ivar code: The code of the reference data item.
    :ivar name: The name of the reference data item.
    :ivar description: The description of the reference data item.
    :ivar deprecated: Indicates if the reference data item is
        deprecated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    additional_info: List["ReferenceDataItem.AdditionalInfo"] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    deprecated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Deprecated",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class AdditionalInfo:
        """
        :ivar value:
        :ivar type_value: This will identify different additionalInfo.
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 255,
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
class ReferenceDataItemUpdate:
    """
    To add or update reference data items for a particular type.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"


class ReferenceDataSearchItemType(Enum):
    AIRPORT = "Airport"
    CARRIER = "Carrier"
    CITY = "City"
    COUNTRY = "Country"
    CURRENCY = "Currency"
    EQUIPMENT = "Equipment"
    PASSENGER_TYPE = "PassengerType"
    SSR_TYPE = "SsrType"
    STATE = "State"


class ReferenceDataUpdateReqAction(Enum):
    ADD = "Add"
    MODIFY = "Modify"


@dataclass
class RequestReferenceDataItem:
    """
    Limits the responses to the requested subcategories for a specific Reference
    Data Type, Currently supported only for @TypeCode="HotelAmenities".

    :ivar request_amenity: Requested decoded values only for the
        specified Hotel Amenity codes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    request_amenity: List["RequestReferenceDataItem.RequestAmenity"] = field(
        default_factory=list,
        metadata={
            "name": "RequestAmenity",
            "type": "Element",
            "max_occurs": 9,
        }
    )

    @dataclass
    class RequestAmenity:
        """
        :ivar type_value: Limits to the response to the requested
            amenity type. Can be a general type: “HA” (Hotel Property
            Amenity) or “RA” (Room Amenity). Or, a specific type, for
            example: “TR” (Transportation) or “BT” (Bed Type). If no
            type is specified, all amenity types are returned.
        """
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )


@dataclass
class TaxCalcInfo:
    """
    Container for a single segment for tax calculation purposes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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
    base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
            "required": True,
        }
    )
    qsurcharge: Optional[str] = field(
        default=None,
        metadata={
            "name": "QSurcharge",
            "type": "Attribute",
        }
    )
    stop_over_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopOverFee",
            "type": "Attribute",
        }
    )
    tax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Attribute",
        }
    )


@dataclass
class UpsellSearchModifier:
    """
    Upsell search modifier to hold values for start and max results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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


@dataclass
class VehicleUpsellDelete:
    """
    Delete command for deleting VehicleUpsellQualify,VehicleUpsellOffer using there
    persisted keys.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    qualify_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualifyRef",
            "type": "Attribute",
        }
    )
    offer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        }
    )


@dataclass
class TypeFlightNumberRange:
    """
    Specify a range of flight numbers.
    """
    class Meta:
        name = "typeFlightNumberRange"

    flight_number_range_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumberRangeStart",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    flight_number_range_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumberRangeEnd",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )


class TypeMctConnection(Enum):
    """
    Enumeration of the types of MCT exceptions (domestic or international)
    """
    DD = "DD"
    DI = "DI"
    ID = "ID"
    II = "II"


class TypeProviderSupplierCapabilityType(Enum):
    """
    Enumeration of ProviderSupplier capability.
    """
    YES = "Yes"
    NO = "No"
    PARTIAL = "Partial"


@dataclass
class TypeReferenceData:
    """
    :ivar code: The code of the reference data item.
    :ivar name: The name of the reference data item.
    :ivar description: The description of the reference data item.
    :ivar deprecated_date: Used to set deprecated date
    """
    class Meta:
        name = "typeReferenceData"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    deprecated_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DeprecatedDate",
            "type": "Attribute",
        }
    )


class TypeShowProvidersType(Enum):
    """Enumeration of reqested type of Provider Configuration requested.

    An error may be returned if 'All' and the user security level is not
    allowed this access
    """
    ALL = "All"
    PROVISIONED = "Provisioned"


@dataclass
class TypeSpecificFlightNumber:
    """
    Specify exact flight number.
    """
    class Meta:
        name = "typeSpecificFlightNumber"

    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )


@dataclass
class AgencyServiceFeeCreateReq(BaseReq):
    """
    Creates an Agency Service Fee to be charged through BSP or Airline Reporting
    Corporation (ARC)..

    :ivar service_fee_info:
    :ivar universal_record_locator_code: Service Fee to be applied to
        the UniversalRecord.
    :ivar provider_locator_code: Service Fees to be applied to the
        provider locator code of the PNR .
    :ivar provider_code: To be used with ProviderLocatorCode, which host
        the reservation being added to belongs to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    provider_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
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
        }
    )


@dataclass
class AgencyServiceFeeCreateRsp(BaseRsp):
    """
    Agency Service Fee issued through BSP or Airline Reporting Corporation (ARC)..
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    service_fee_info: List[ServiceFeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class AirUpsellOffer:
    """
    :ivar account_code:
    :ivar class_of_service:
    :ivar cabin_class:
    :ivar key:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )
    cabin_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinClass",
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
class AirUpsellOfferSearchCriteria:
    """
    Search criteria for AirUpsellOffers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class BrandedFareSearchReq(BaseReq):
    """
    Branded Fare search request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family_criteria: Optional[FareFamilyCriteria] = field(
        default=None,
        metadata={
            "name": "FareFamilyCriteria",
            "type": "Element",
            "required": True,
        }
    )
    branded_fare_search_modifier: Optional[BrandedFareSearchModifier] = field(
        default=None,
        metadata={
            "name": "BrandedFareSearchModifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CalculateTaxReq(BaseReq):
    """
    Request to calculate US taxes based on a series of segments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    tax_calc_info: List[TaxCalcInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxCalcInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class CalculateTaxResult:
    """
    Result container for a tax calculation.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    tax_calc_info: List[TaxCalcInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxCalcInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    total_base_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalBaseFare",
            "type": "Attribute",
            "required": True,
        }
    )
    total_tax: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Attribute",
            "required": True,
        }
    )
    total_fare: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalFare",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ContentProvider:
    """
    A content provider uniquely identified with its provider code and supplier
    code.If a given provider provides content for multiple suppliers, multiple
    elements will be returned for that provider.

    :ivar provider_code: The host for the content
        (e.g.1G,1P,1S,1A,ACH,MCH).
    :ivar supplier_code: Indicates the direct connect supplier (e.g. U2)
        when the provider is a hub (e.g. ACH).
    :ivar agency_credentials: Indicates whether agency (or agent )
        credentials are required to connect to the given
        provider/supplier.
    :ivar active: Status of the given provider/supplier . If not
        currently active, a user cannot connect to the given
        provider/supplier.
    :ivar provisionable: Indicates whether the given provider/supplier
        can be provisioned to an agency/branch/agent.
    :ivar merchandising_achadapter: ACH adapter for Merchandising ACH
        carrier.
    :ivar static_data_carrier: Returns "true" if it is StaticDataCarrier
        otherwise "false". Default value is "false".
    :ivar merchandising_achcarrier: Returns "true" if it is
        MerchandisingACHCarrier otherwise "false". Default value is
        "false".
    :ivar merchandising_hub_carrier: Returns "true" if it is
        MerchandisingHubCarrier otherwise "false". Default value is
        "false".
    :ivar booking_retrieve: Indication if a Provider and/or Supplier has
        booking retrieve capability.
    :ivar segment_modify: Indication if a Provider and/or Supplier has
        booking segment modify capability.
    :ivar optional_services_modify: Indication if a Provider and/or
        Supplier has booking optional service modify capability.
    :ivar traveler_info_modify: Indication if a Provider and/or Supplier
        has traveler information modify capability.
    :ivar additional_payment: Indication if a Provider and/or Supplier
        has additional payment capability.
    :ivar booking_cancel: Indication if a Provider and/or Supplier has
        booking cancel capability.
    :ivar seat_map: Indication if a Provider and/or Supplier has SeatMap
        capability.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
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
    agency_credentials: Optional[ContentProviderAgencyCredentials] = field(
        default=None,
        metadata={
            "name": "AgencyCredentials",
            "type": "Attribute",
            "required": True,
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Attribute",
            "required": True,
        }
    )
    provisionable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Provisionable",
            "type": "Attribute",
            "required": True,
        }
    )
    merchandising_achadapter: Optional[str] = field(
        default=None,
        metadata={
            "name": "MerchandisingACHAdapter",
            "type": "Attribute",
        }
    )
    static_data_carrier: bool = field(
        default=False,
        metadata={
            "name": "StaticDataCarrier",
            "type": "Attribute",
        }
    )
    merchandising_achcarrier: bool = field(
        default=False,
        metadata={
            "name": "MerchandisingACHCarrier",
            "type": "Attribute",
        }
    )
    merchandising_hub_carrier: bool = field(
        default=False,
        metadata={
            "name": "MerchandisingHubCarrier",
            "type": "Attribute",
        }
    )
    booking_retrieve: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "BookingRetrieve",
            "type": "Attribute",
        }
    )
    segment_modify: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "SegmentModify",
            "type": "Attribute",
        }
    )
    optional_services_modify: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "OptionalServicesModify",
            "type": "Attribute",
        }
    )
    traveler_info_modify: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "TravelerInfoModify",
            "type": "Attribute",
        }
    )
    additional_payment: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "AdditionalPayment",
            "type": "Attribute",
        }
    )
    booking_cancel: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "BookingCancel",
            "type": "Attribute",
        }
    )
    seat_map: TypeProviderSupplierCapabilityType = field(
        default=TypeProviderSupplierCapabilityType.YES,
        metadata={
            "name": "SeatMap",
            "type": "Attribute",
        }
    )


@dataclass
class ContentProviderRetrieveReq(BaseReq):
    """
    Retrieves all available providers with their suppliers.

    :ivar provider_code: If ProviderCode present, Retruns Data for the
        ProviderCode
    :ivar supplier_code: Represents SupplierCode or Carrier code. If
        SupplierCode Presents, returns Data for the SupplierCode.
    :ivar show_providers: Enumeration of reqested type of Provider
        Configuration requested - default is "Provisioned". An error may
        be returned if 'All' is requested and the user security level is
        not allowed this access
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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
    show_providers: TypeShowProvidersType = field(
        default=TypeShowProvidersType.PROVISIONED,
        metadata={
            "name": "ShowProviders",
            "type": "Attribute",
        }
    )


@dataclass
class CreateAgencyFeeMcoReq(BaseReq):
    """
    Manually create an Agency Fee MCO.

    :ivar name:
    :ivar form_of_payment:
    :ivar form_of_payment_ref:
    :ivar general_remark:
    :ivar accounting_remark:
    :ivar amount:
    :ivar location_code: The airport code where the MCO will be
        accepted, or the City code where the requesting agency resides.
        If not entered, the default location of the agency will be
        selected.
    :ivar locator_code: The locator code of the PNR that the MCO is
        created for.
    :ivar ticket_number: The ticket that this MCO was issued in
        connection with. Could be the ticket that caused the fee, a
        residual from an exchange, or an airline service fee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
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
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        }
    )


@dataclass
class CreateAgencyFeeMcoRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mco: Optional[Mco] = field(
        default=None,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )


@dataclass
class CreateAirlineFeeMcoReq(BaseReq):
    """
    Manually create an Airline Fee MCO.

    :ivar name:
    :ivar form_of_payment:
    :ivar form_of_payment_ref:
    :ivar general_remark:
    :ivar accounting_remark:
    :ivar endorsement:
    :ivar amount:
    :ivar location_code: The airport code where the MCO will be
        accepted, or the City code where the requesting agency resides.
        If not entered, the default location of the agency will be
        selected.
    :ivar locator_code: The locator code of the PNR that the MCO is
        created for.
    :ivar ticket_number: The ticket that this MCO was issued in
        connection with. Could be the ticket that caused the fee, a
        residual from an exchange, or an airline service fee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
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
    endorsement: List[Endorsement] = field(
        default_factory=list,
        metadata={
            "name": "Endorsement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 8,
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        }
    )


@dataclass
class CreateAirlineFeeMcoRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mco: Optional[Mco] = field(
        default=None,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )


@dataclass
class CreditCardAuthRsp(BaseRsp):
    """
    The response to the CreditCardAuthReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class CreditCardPaymentAuth:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    credit_card: Optional[CreditCard] = field(
        default=None,
        metadata={
            "name": "CreditCard",
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
    security_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecurityCode",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    perform_avs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PerformAVS",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CurrencyConversionReq(BaseReq):
    """
    Performs A Currency Conversion between two Currencies.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    currency_conversion: List[CurrencyConversion] = field(
        default_factory=list,
        metadata={
            "name": "CurrencyConversion",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class CurrencyConversionRsp(BaseRsp):
    """
    The response to the CurrencyConversionReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    currency_conversion: List[CurrencyConversion] = field(
        default_factory=list,
        metadata={
            "name": "CurrencyConversion",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class FindEmployeesOnFlightReq(BaseReq):
    """
    Request to retrieve the number of employees in a flight.

    :ivar flight_criteria:
    :ivar account_id: Identifier of the account owner of the employees
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    flight_criteria: List[FlightCriteria] = field(
        default_factory=list,
        metadata={
            "name": "FlightCriteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    account_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FindEmployeesOnFlightRsp(BaseRsp):
    """
    Response to retrieve the number of employees in a flight.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    employees_on_flight: List["FindEmployeesOnFlightRsp.EmployeesOnFlight"] = field(
        default_factory=list,
        metadata={
            "name": "EmployeesOnFlight",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class EmployeesOnFlight:
        """
        :ivar name:
        :ivar universal_record_locator: UniversalRecord Locator
        :ivar destination: Airsegment Destination
        :ivar origin: Airsegment Origin
        :ivar departure_date: Airsegment departure date
        :ivar flight_number: Air segment flight number
        :ivar carrier: Air Segment Carrier
        """
        name: List[Name] = field(
            default_factory=list,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )
        universal_record_locator: Optional[str] = field(
            default=None,
            metadata={
                "name": "UniversalRecordLocator",
                "type": "Attribute",
                "required": True,
                "min_length": 5,
                "max_length": 8,
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
        departure_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "DepartureDate",
                "type": "Attribute",
                "required": True,
            }
        )
        flight_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "FlightNumber",
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


@dataclass
class HotelUpsellOffer:
    """Offer data of Hotel which is used to send a Hotel Upsell request and match a
    hotel property in the response.

    Offer is found for a matching qualify.

    :ivar corporate_discount_id:
    :ivar rate_plan_type:
    :ivar key:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    corporate_discount_id: Optional[CorporateDiscountId] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rate_plan_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatePlanType",
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
class HotelUpsellOfferSearchCriteria:
    """
    Search criteria for HotelUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    corporate_discount_id: Optional[CorporateDiscountId] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rate_plan_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HotelUpsellQualify:
    """Qualify data of Hotel against which Hotel property details search is matched
    to get an upsell Offer.

    Each qualify should have an offer.

    :ivar corporate_discount_id:
    :ivar hotel_chain_code:
    :ivar hotel_code:
    :ivar hotel_location: The IATA location code for this entity.
    :ivar rate_plan_type:
    :ivar effective_date:
    :ivar expiration_date:
    :ivar key:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    :ivar offer_ref: Reference to the Offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    corporate_discount_id: Optional[CorporateDiscountId] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_chain_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelChainCode",
            "type": "Attribute",
            "required": True,
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
    hotel_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    rate_plan_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
        }
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    expiration_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
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
    offer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        }
    )


@dataclass
class McoCreateDate(TypeTimeRange):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class McoSearchModifiers:
    """
    Modifiers to narrow the MCO search results.

    :ivar type_value: Find all MCOs of a particular type
    :ivar status: Find all MCOs of a particular status.
    :ivar max_results: Used to limit the number of results returned,
        particularly in more 200809 searches that may return a large
        result set.
    :ivar start_from_result: Used to browse beyond the maximum number of
        results specified with the MaxResults parameter. Acts as an
        offset to skip the specified number of items from the begining
        of the result set.
    :ivar include_name: Should the McoSearchResult include the name on
        the MCO
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    type_value: Optional[TypeMcotype] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    status: Optional[TypeMcostatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    start_from_result: int = field(
        default=0,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    include_name: bool = field(
        default=False,
        metadata={
            "name": "IncludeName",
            "type": "Attribute",
        }
    )


@dataclass
class McoSearchResult:
    """
    :ivar name:
    :ivar create_date: The date the MCO was issued
    :ivar number: The MCO number
    :ivar status: The status of the MCO
    :ivar type_value: The Type of the MCO
    :ivar locator_code: The locator code that the MCO is linked to
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    status: Optional[TypeMcostatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: Optional[TypeMcotype] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
        }
    )


@dataclass
class McoVoidReq(BaseReq):
    """
    Void an MCO (of any type).

    :ivar general_remark:
    :ivar number: The number of the MCO to void
    :ivar return_mco:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    general_remark: List[GeneralRemark] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    return_mco: bool = field(
        default=False,
        metadata={
            "name": "ReturnMCO",
            "type": "Attribute",
        }
    )


@dataclass
class McoVoidRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mco: Optional[Mco] = field(
        default=None,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )


@dataclass
class MctCount:
    """
    The count of MCT exceptions for the given search criteria.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    connection: Optional[TypeMctConnection] = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Attribute",
            "required": True,
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
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MctException:
    """
    MCT Exception details.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    time: Optional[int] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )
    arrive_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveStation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    depart_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    connection: Optional[TypeMctConnection] = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Attribute",
            "required": True,
        }
    )
    arrive_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    depart_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    arrive_flight_range_begin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveFlightRangeBegin",
            "type": "Attribute",
        }
    )
    arrive_flight_range_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveFlightRangeEnd",
            "type": "Attribute",
        }
    )
    depart_flight_range_begin: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartFlightRangeBegin",
            "type": "Attribute",
        }
    )
    depart_flight_range_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartFlightRangeEnd",
            "type": "Attribute",
        }
    )
    arrive_equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveEquipment",
            "type": "Attribute",
        }
    )
    depart_equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartEquipment",
            "type": "Attribute",
        }
    )
    previous_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    next_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    previous_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    next_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    previous_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousState",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    next_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextState",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    arrive_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveTerminal",
            "type": "Attribute",
        }
    )
    depart_terminal: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartTerminal",
            "type": "Attribute",
        }
    )
    effective_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        }
    )
    discontinue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DiscontinueDate",
            "type": "Attribute",
        }
    )


@dataclass
class MctQuery:
    """
    Lookup the particular MCT time between two segments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )


@dataclass
class MctSearch:
    """
    Search the MCT data for exceptions.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    arrive_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveStation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    depart_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    connection: Optional[TypeMctConnection] = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Attribute",
        }
    )
    arrive_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    depart_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    arrive_flight: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArriveFlight",
            "type": "Attribute",
        }
    )
    depart_flight: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartFlight",
            "type": "Attribute",
        }
    )
    previous_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    next_station: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    previous_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    next_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    previous_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousState",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    next_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "NextState",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    travel_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
        }
    )


@dataclass
class MctStandard:
    """
    The standard MCT time for the given search criteria.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    type_value: Optional[TypeMctConnection] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    time: Optional[int] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MirReportRetrieveReq(BaseReq):
    """
    Retrieve a report.

    :ivar locator_code: The locator code of the PNR that the MIR is
        created for.
    :ivar report_format: MIR report format type
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 8,
        }
    )
    report_format: Optional[MirReportRetrieveReqReportFormat] = field(
        default=None,
        metadata={
            "name": "ReportFormat",
            "type": "Attribute",
        }
    )


@dataclass
class MirReportRetrieveRsp(BaseRsp):
    """
    Carries the report payload.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    report: Optional[str] = field(
        default=None,
        metadata={
            "name": "Report",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RailStationLocationModifiers:
    """
    Request object used to request specific rail station locations.

    :ivar rail_location:
    :ivar country_code: 2 character country code such as FR.
    :ivar distributor: 2 character Rail distributor code such as TL or
        2C.
    :ivar description: A city name or station name such as Paris or
        Paris Nord.
    :ivar active: The value “false” will return stations that are no
        longer active but remain on the table because existing bookings
        may reference them. The default is “true” which returns only
        active locations.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    rail_location: Optional[RailLocation] = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    distributor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Distributor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    active: bool = field(
        default=True,
        metadata={
            "name": "Active",
            "type": "Attribute",
        }
    )


@dataclass
class ReferenceDataRetrieveRsp(BaseRsp):
    """
    Response to retrieve code, name and description for a specific reference data
    type.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    reference_data_item: List[ReferenceDataItem] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceDataItem",
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
class ReferenceDataSearchItem:
    """
    Container for a Reference Data search item that includes its type and how to
    search / identify the item either via code or value.

    :ivar code: Code uniquely identifying the reference data item (e.g.
        ORD for Airport item).
    :ivar name: Value of the reference data item that may not uniquely
        identify a single Reference Data item (e.g. Chicago for Airport
        would return ORD and MDW).
    :ivar type_value: Reference data type
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "min_length": 1,
            "white_space": "collapse",
        }
    )
    type_value: Optional[ReferenceDataSearchItemType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ReferenceDataSearchRsp(BaseRsp):
    """
    Response the sought reference data item.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    airport: List["ReferenceDataSearchRsp.Airport"] = field(
        default_factory=list,
        metadata={
            "name": "Airport",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    carrier: List["ReferenceDataSearchRsp.Carrier"] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    city: List["ReferenceDataSearchRsp.City"] = field(
        default_factory=list,
        metadata={
            "name": "City",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    country: List["ReferenceDataSearchRsp.Country"] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    currency: List["ReferenceDataSearchRsp.Currency"] = field(
        default_factory=list,
        metadata={
            "name": "Currency",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    equipment: List["ReferenceDataSearchRsp.Equipment"] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passenger_type: List["ReferenceDataSearchRsp.PassengerType"] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    state: List["ReferenceDataSearchRsp.State"] = field(
        default_factory=list,
        metadata={
            "name": "State",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ssr_type: List["ReferenceDataSearchRsp.SsrType"] = field(
        default_factory=list,
        metadata={
            "name": "SsrType",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class Airport:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 3,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        city_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CityCode",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        country_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "length": 2,
            }
        )

    @dataclass
    class Carrier:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
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
    class City:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 3,
                "white_space": "collapse",
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
        state_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "StateCode",
                "type": "Attribute",
            }
        )
        country_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "length": 2,
            }
        )

    @dataclass
    class Country:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        extended_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ExtendedCode",
                "type": "Attribute",
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
            }
        )
        iata_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "IataCode",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        continent: Optional[str] = field(
            default=None,
            metadata={
                "name": "Continent",
                "type": "Attribute",
            }
        )

    @dataclass
    class Currency:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 3,
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
        decimal: Optional[str] = field(
            default=None,
            metadata={
                "name": "Decimal",
                "type": "Attribute",
            }
        )

    @dataclass
    class Equipment:
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
            }
        )

    @dataclass
    class PassengerType:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "min_length": 3,
                "max_length": 5,
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
    class State:
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "max_length": 6,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        country_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )

    @dataclass
    class SsrType:
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
        providers: Optional[str] = field(
            default=None,
            metadata={
                "name": "Providers",
                "type": "Attribute",
            }
        )
        level: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
                "required": True,
            }
        )
        free_text_required: Optional[str] = field(
            default=None,
            metadata={
                "name": "FreeTextRequired",
                "type": "Attribute",
                "required": True,
            }
        )
        pattern: Optional[str] = field(
            default=None,
            metadata={
                "name": "Pattern",
                "type": "Attribute",
            }
        )
        help_text: Optional[str] = field(
            default=None,
            metadata={
                "name": "HelpText",
                "type": "Attribute",
            }
        )


@dataclass
class ReferenceDataUpdateReq(BaseReq):
    """
    Request to update reference data.

    :ivar item:
    :ivar action:
    :ivar type_code: The type code of the reference data to update.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    item: List["ReferenceDataUpdateReq.Item"] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    action: Optional[ReferenceDataUpdateReqAction] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )

    @dataclass
    class Item(TypeReferenceData):
        """
        :ivar additional_element: To provide other optional values.
        """
        additional_element: List[AdditionalElement] = field(
            default_factory=list,
            metadata={
                "name": "AdditionalElement",
                "type": "Element",
                "max_occurs": 998001,
            }
        )


@dataclass
class ReferenceDataUpdateRsp(BaseRsp):
    """
    An empty response indicates success.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class UpsellSearchCriteria:
    """
    Search Element for Effective and Expiration dates.
    """
    effective_date: Optional[EffectiveDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
            "required": True,
        }
    )
    expiration_date: Optional[ExpirationDate] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
            "required": True,
        }
    )


@dataclass
class VehicleUpsellOffer:
    """Offer data of Vehicle which is used to send an upsell request.

    Offer is found for a matching qualify.

    :ivar air_conditioning:
    :ivar transmission_type:
    :ivar vehicle_class: Class of vehicle
    :ivar category: Category of vehicle. Each supplier decides how these
        categories map to a vehicle class.
    :ivar door_count: The number of doors on the vehicle. Could be a
        range like '2-4'
    :ivar rate_code:
    :ivar rate_category: The category of this rate (Best, etc)
    :ivar discount_number:
    :ivar fuel_type:
    :ivar key:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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
    door_count: Optional[TypeDoorCount] = field(
        default=None,
        metadata={
            "name": "DoorCount",
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
    fuel_type: Optional[TypeFuel] = field(
        default=None,
        metadata={
            "name": "FuelType",
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
class VehicleUpsellOfferSearchCriteria:
    """
    Search criteria for VehicleUpsellOffers.

    :ivar vehicle_class: Class of vehicle
    :ivar category: Category of vehicle. Each supplier decides how these
        categories map to a vehicle class.
    :ivar air_conditioning:
    :ivar transmission_type:
    :ivar door_count: The number of doors on the vehicle. Could be a
        range like '2-4'
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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
        }
    )
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
    door_count: Optional[TypeDoorCount] = field(
        default=None,
        metadata={
            "name": "DoorCount",
            "type": "Attribute",
        }
    )


@dataclass
class VehicleUpsellQualify:
    """Qualify data of Vehicle against which Vehicle Availability search is matched
    to get an upsell Offer.

    Each qualify should have an offer.

    :ivar key:
    :ivar vendor_code:
    :ivar effective_date:
    :ivar expiration_date:
    :ivar provider_code:
    :ivar pickup_date_time:
    :ivar pickup_location:
    :ivar return_date_time:
    :ivar return_location:
    :ivar pickup_location_type:
    :ivar return_location_type:
    :ivar pickup_location_number:
    :ivar return_location_number:
    :ivar air_conditioning:
    :ivar transmission_type:
    :ivar vehicle_class:
    :ivar category:
    :ivar door_count:
    :ivar rate_code:
    :ivar rate_category:
    :ivar discount_number:
    :ivar offer_ref:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
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
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    expiration_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
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
    pickup_date_time: Optional[str] = field(
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
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 10,
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
    offer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfferRef",
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
class TypeEmailAddress:
    class Meta:
        name = "typeEmailAddress"

    email: Optional[Email] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    simple_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SimpleName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )


@dataclass
class TypeFlightSpec:
    """
    Specifies flight number as either specific flight number or a flight number
    range.
    """
    class Meta:
        name = "typeFlightSpec"

    flight_number_range: Optional[TypeFlightNumberRange] = field(
        default=None,
        metadata={
            "name": "FlightNumberRange",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
        }
    )
    specific_flight_number: Optional[TypeSpecificFlightNumber] = field(
        default=None,
        metadata={
            "name": "SpecificFlightNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/util_v52_0",
        }
    )


@dataclass
class AirUpsellQualifySearchCriteria(UpsellSearchCriteria):
    """
    Search criteria for AirUpsellQualify.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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


@dataclass
class CalculateTaxRsp(BaseRsp):
    """
    Response containg calculated total of base prices and taxes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    calculate_tax_result: Optional[CalculateTaxResult] = field(
        default=None,
        metadata={
            "name": "CalculateTaxResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ContentProviderRetrieveRsp(BaseRsp):
    """
    Response with all available providers with their suppliers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    content_provider: List[ContentProvider] = field(
        default_factory=list,
        metadata={
            "name": "ContentProvider",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class CreditCardAuthReq(BaseReq):
    """
    Performs a credit card authorization to validate a credit card for use during
    booking.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_length": 1,
        }
    )
    credit_card_payment_auth: List[CreditCardPaymentAuth] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardPaymentAuth",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    plating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class FlightSpec(TypeFlightSpec):
    """
    Operating Flight number or Flight Range.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellAdd:
    """
    Add command for adding HotelUpsellQualify,HotelUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_qualify: Optional[HotelUpsellQualify] = field(
        default=None,
        metadata={
            "name": "HotelUpsellQualify",
            "type": "Element",
            "required": True,
        }
    )
    hotel_upsell_offer: Optional[HotelUpsellOffer] = field(
        default=None,
        metadata={
            "name": "HotelUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class HotelUpsellQualifySearchCriteria(UpsellSearchCriteria):
    """
    Search criteria for HotelUpsellQualify.

    :ivar corporate_discount_id:
    :ivar hotel_chain_code:
    :ivar hotel_code:
    :ivar hotel_location: The IATA location code for this entity.
    :ivar rate_plan_type:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    corporate_discount_id: Optional[CorporateDiscountId] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_chain_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelChainCode",
            "type": "Attribute",
            "required": True,
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
    hotel_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    rate_plan_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
        }
    )


@dataclass
class HotelUpsellRule:
    """
    Binds an HotelUpsellQualify and HotelUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_qualify: Optional[HotelUpsellQualify] = field(
        default=None,
        metadata={
            "name": "HotelUpsellQualify",
            "type": "Element",
        }
    )
    hotel_upsell_offer: Optional[HotelUpsellOffer] = field(
        default=None,
        metadata={
            "name": "HotelUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class HotelUpsellSearchResult:
    """
    Hotel upsell search criteria result having matching offer and qualifies.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_qualify: List[HotelUpsellQualify] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellQualify",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    hotel_upsell_offer: Optional[HotelUpsellOffer] = field(
        default=None,
        metadata={
            "name": "HotelUpsellOffer",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class HotelUpsellUpdate:
    """
    Update command for updating HotelUpsellQualify,HotelUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_qualify: Optional[HotelUpsellQualify] = field(
        default=None,
        metadata={
            "name": "HotelUpsellQualify",
            "type": "Element",
        }
    )
    hotel_upsell_offer: Optional[HotelUpsellOffer] = field(
        default=None,
        metadata={
            "name": "HotelUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class McoSearchReq(BaseReq):
    """
    Search for MCOs by certain criteria and return a list.

    :ivar name:
    :ivar carrier:
    :ivar airport:
    :ivar ticket_number: The ticket that this MCO was issued in
        connection with. Could be the ticket that caused the fee, a
        residual from an exchange, or an airline service fee.
    :ivar mco_create_date:
    :ivar mco_search_modifiers:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    airport: List[Airport] = field(
        default_factory=list,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
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
    mco_create_date: Optional[McoCreateDate] = field(
        default=None,
        metadata={
            "name": "McoCreateDate",
            "type": "Element",
        }
    )
    mco_search_modifiers: Optional[McoSearchModifiers] = field(
        default=None,
        metadata={
            "name": "McoSearchModifiers",
            "type": "Element",
        }
    )


@dataclass
class McoSearchRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mco_search_result: List[McoSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "McoSearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class MctCountReq(BaseReq):
    """
    Determine how many MCT exceptions exist for the search criteria.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_search: Optional[MctSearch] = field(
        default=None,
        metadata={
            "name": "MctSearch",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MctCountRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_count: List[MctCount] = field(
        default_factory=list,
        metadata={
            "name": "MctCount",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class MctLookupReq(BaseReq):
    """
    Search for MCT time values.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_search: Optional[MctSearch] = field(
        default=None,
        metadata={
            "name": "MctSearch",
            "type": "Element",
        }
    )
    mct_query: Optional[MctQuery] = field(
        default=None,
        metadata={
            "name": "MctQuery",
            "type": "Element",
        }
    )


@dataclass
class MctLookupRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_standard: List[MctStandard] = field(
        default_factory=list,
        metadata={
            "name": "MctStandard",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    mct_exception: List[MctException] = field(
        default_factory=list,
        metadata={
            "name": "MctException",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class OperatingFlightSpec(TypeFlightSpec):
    """
    Marketing Flight number or Flight Range.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ReferenceDataSearchModifiers:
    """
    Modifiers to narrow the reference data search results.

    :ivar rail_station_location_modifiers:
    :ivar max_results: Used to limit the number of results returned.
    :ivar start_from_result: Used to browse beyond the maximum number of
        results specified with the MaxResults parameter. Acts as an
        offset to skip the specified number of items from the begining
        of the result set.
    :ivar provider_code: Provider Specific restriction(e.g. 1G, 1P etc)
        .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    rail_station_location_modifiers: Optional[RailStationLocationModifiers] = field(
        default=None,
        metadata={
            "name": "RailStationLocationModifiers",
            "type": "Element",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    start_from_result: int = field(
        default=0,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 0,
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


@dataclass
class VehicleUpsellAdd:
    """
    Add command for adding VehicleUpsellQualify,VehicleUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_qualify: Optional[VehicleUpsellQualify] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellQualify",
            "type": "Element",
            "required": True,
        }
    )
    vehicle_upsell_offer: Optional[VehicleUpsellOffer] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class VehicleUpsellQualifySearchCriteria(UpsellSearchCriteria):
    """
    Search criteria for VehicleUpsellQualify.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

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
    door_count: Optional[TypeDoorCount] = field(
        default=None,
        metadata={
            "name": "DoorCount",
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
    discount_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )


@dataclass
class VehicleUpsellRule:
    """
    Binds an VehicleUpsellQualify and VehicleUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_qualify: Optional[VehicleUpsellQualify] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellQualify",
            "type": "Element",
        }
    )
    vehicle_upsell_offer: Optional[VehicleUpsellOffer] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class VehicleUpsellSearchResult:
    """
    Vehicle upsell search criteria result having matching offer and qualifies.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_qualify: List[VehicleUpsellQualify] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellQualify",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    vehicle_upsell_offer: Optional[VehicleUpsellOffer] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOffer",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class VehicleUpsellUpdate:
    """
    Update command for updating VehicleUpsellQualify,VehicleUpsellOffer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_qualify: Optional[VehicleUpsellQualify] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellQualify",
            "type": "Element",
        }
    )
    vehicle_upsell_offer: Optional[VehicleUpsellOffer] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class AirUpsellQualify:
    """
    :ivar departure_time:
    :ivar flight_spec:
    :ivar operating_flight_spec:
    :ivar account_code:
    :ivar carrier:
    :ivar effective_date:
    :ivar expiration_date:
    :ivar provider_code:
    :ivar origin:
    :ivar destination:
    :ivar class_of_service:
    :ivar operating_carrier:
    :ivar offer_ref:
    :ivar key:
    :ivar fare_basis:
    :ivar el_stat: This attribute is used to show the action results of
        an element. Possible values are "A" (when elements have been
        added to the UR) and "M" (when existing elements have been
        modified). Response only.
    :ivar key_override: If a duplicate key is found where we are adding
        elements in some cases like URAdd, then instead of erroring out
        set this attribute to true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    departure_time: Optional[TypeTimeSpec] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
        }
    )
    flight_spec: Optional[FlightSpec] = field(
        default=None,
        metadata={
            "name": "FlightSpec",
            "type": "Element",
        }
    )
    operating_flight_spec: Optional[OperatingFlightSpec] = field(
        default=None,
        metadata={
            "name": "OperatingFlightSpec",
            "type": "Element",
        }
    )
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    expiration_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
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
    class_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    offer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OfferRef",
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
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "max_length": 20,
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
class AirUpsellSearchCriteria:
    """
    Search criteria for AirUpsell.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_offer_search_criteria: Optional[AirUpsellOfferSearchCriteria] = field(
        default=None,
        metadata={
            "name": "AirUpsellOfferSearchCriteria",
            "type": "Element",
        }
    )
    air_upsell_qualify_search_criteria: Optional[AirUpsellQualifySearchCriteria] = field(
        default=None,
        metadata={
            "name": "AirUpsellQualifySearchCriteria",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FareFamily:
    """
    It is a branded Fare for a carrier and given fare basis code.

    :ivar flight_spec: Flight number range or specific flight number for
        which this fare family would qualify.
    :ivar carrier:
    :ivar label:
    :ivar fare_basis:
    :ivar key:
    :ivar version:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    flight_spec: Optional[FlightSpec] = field(
        default=None,
        metadata={
            "name": "FlightSpec",
            "type": "Element",
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
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 32,
        }
    )
    fare_basis: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
            "max_length": 20,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
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
class HotelUpsellCriteria:
    """
    Wraps all Upsell Admin commands related to Hotel.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_add: List[HotelUpsellAdd] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellAdd",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_upsell_update: List[HotelUpsellUpdate] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellUpdate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_upsell_delete: List[HotelUpsellDelete] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellDelete",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class HotelUpsellSearchCriteria:
    """
    Search criteria for HotelUpsell.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_offer_search_criteria: Optional[HotelUpsellOfferSearchCriteria] = field(
        default=None,
        metadata={
            "name": "HotelUpsellOfferSearchCriteria",
            "type": "Element",
        }
    )
    hotel_upsell_qualify_search_criteria: Optional[HotelUpsellQualifySearchCriteria] = field(
        default=None,
        metadata={
            "name": "HotelUpsellQualifySearchCriteria",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReferenceDataRetrieveReq(BaseReq):
    """
    Request to retrieve code, name and description for  a specific reference data
    type.

    :ivar reference_data_search_modifiers:
    :ivar request_reference_data_item:
    :ivar type_code: The code of the reference data type. Valid values
        are 'PaymentType', 'PaymentFormatType',
        'MerchandisingOfferType', 'HotelTaxType',
        'HotelAmenities','Airport','City','Country','CityAirport','BusinessType','Currency','PosChannel','StateProvince','SupplierType','RoleCategoryType','ResourceCategoryType','PaymentType','EmailType','HotelRateCategory','FulfillmentType','HotelRoomViewType',
        'HotelMealPlans' , 'GeoPoliticalAreaType', 'AirAndRailMiscType',
        'AirAndRailSupplierType', 'HotelMiscType' , 'HotelSupplierType'
        , 'VehicleMiscType' , 'VehicleSupplierType' ,
        'AccountingReferenceType' , 'TRMLocation' , 'Title' ,
        'PassengerTypeCode' , 'Gender' , 'PostalAddressType' ,
        'AccountingRemarkType' , 'VehicleSpecialEquipment',
        'ReferencePointSearch', 'RailStationLocation',
        'RailAccommodation', and 'RailDiscountLoyalty'.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    reference_data_search_modifiers: Optional[ReferenceDataSearchModifiers] = field(
        default=None,
        metadata={
            "name": "ReferenceDataSearchModifiers",
            "type": "Element",
        }
    )
    request_reference_data_item: Optional[RequestReferenceDataItem] = field(
        default=None,
        metadata={
            "name": "RequestReferenceDataItem",
            "type": "Element",
        }
    )
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )


@dataclass
class ReferenceDataSearchReq(BaseReq):
    """
    Request to lookup a specific reference data item.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    reference_data_search_modifiers: Optional[ReferenceDataSearchModifiers] = field(
        default=None,
        metadata={
            "name": "ReferenceDataSearchModifiers",
            "type": "Element",
        }
    )
    reference_data_search_item: List[ReferenceDataSearchItem] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceDataSearchItem",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleUpsellCriteria:
    """
    Wraps all Upsell Admin commands related to Vehicle.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_add: List[VehicleUpsellAdd] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellAdd",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_upsell_update: List[VehicleUpsellUpdate] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellUpdate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_upsell_delete: List[VehicleUpsellDelete] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellDelete",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class VehicleUpsellSearchCriteria:
    """
    Search criteria for VehicleUpsell.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_offer_search_criteria: Optional[VehicleUpsellOfferSearchCriteria] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellOfferSearchCriteria",
            "type": "Element",
        }
    )
    vehicle_upsell_qualify_search_criteria: Optional[VehicleUpsellQualifySearchCriteria] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellQualifySearchCriteria",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirUpsellAdd:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_qualify: Optional[AirUpsellQualify] = field(
        default=None,
        metadata={
            "name": "AirUpsellQualify",
            "type": "Element",
            "required": True,
        }
    )
    air_upsell_offer: Optional[AirUpsellOffer] = field(
        default=None,
        metadata={
            "name": "AirUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class AirUpsellRule:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_qualify: Optional[AirUpsellQualify] = field(
        default=None,
        metadata={
            "name": "AirUpsellQualify",
            "type": "Element",
        }
    )
    air_upsell_offer: Optional[AirUpsellOffer] = field(
        default=None,
        metadata={
            "name": "AirUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class AirUpsellSearchResult:
    """
    Air upsell search criteria result having matching offer and qualifies.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_qualify: List[AirUpsellQualify] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellQualify",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    air_upsell_offer: Optional[AirUpsellOffer] = field(
        default=None,
        metadata={
            "name": "AirUpsellOffer",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirUpsellUpdate:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_qualify: Optional[AirUpsellQualify] = field(
        default=None,
        metadata={
            "name": "AirUpsellQualify",
            "type": "Element",
        }
    )
    air_upsell_offer: Optional[AirUpsellOffer] = field(
        default=None,
        metadata={
            "name": "AirUpsellOffer",
            "type": "Element",
        }
    )


@dataclass
class BrandedFareAdminRsp(BaseRsp):
    """
    Response to BrandedFareAdminReq containing the FareFamily being added, deleted
    or updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family: List[FareFamily] = field(
        default_factory=list,
        metadata={
            "name": "FareFamily",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class BrandedFareSearchRsp(BaseRsp):
    """
    Branded Fare search response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family: List[FareFamily] = field(
        default_factory=list,
        metadata={
            "name": "FareFamily",
            "type": "Element",
            "min_occurs": 1,
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
class FareFamilyAdd:
    """
    Branded fare admin request element to add a FareFamily.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family: Optional[FareFamily] = field(
        default=None,
        metadata={
            "name": "FareFamily",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FareFamilyUpdate:
    """
    Branded fare admin request element to Update a FareFamily.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family: Optional[FareFamily] = field(
        default=None,
        metadata={
            "name": "FareFamily",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UpsellSearchReq(BaseReq):
    """
    Request to retrieve all upsell qualify/offers based on search criteria for
    air,hotel and vehicle.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_search_criteria: Optional[AirUpsellSearchCriteria] = field(
        default=None,
        metadata={
            "name": "AirUpsellSearchCriteria",
            "type": "Element",
        }
    )
    hotel_upsell_search_criteria: Optional[HotelUpsellSearchCriteria] = field(
        default=None,
        metadata={
            "name": "HotelUpsellSearchCriteria",
            "type": "Element",
        }
    )
    vehicle_upsell_search_criteria: Optional[VehicleUpsellSearchCriteria] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellSearchCriteria",
            "type": "Element",
        }
    )
    upsell_search_modifier: Optional[UpsellSearchModifier] = field(
        default=None,
        metadata={
            "name": "UpsellSearchModifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AirUpsellCriteria:
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_add: List[AirUpsellAdd] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellAdd",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_upsell_update: List[AirUpsellUpdate] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellUpdate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_upsell_delete: List[AirUpsellDelete] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellDelete",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class BrandedFareAdminReq(BaseReq):
    """
    Admin request to add/update or delete Branded fare.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family_add: List[FareFamilyAdd] = field(
        default_factory=list,
        metadata={
            "name": "FareFamilyAdd",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_family_update: List[FareFamilyUpdate] = field(
        default_factory=list,
        metadata={
            "name": "FareFamilyUpdate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_family_delete: List[FareFamilyDelete] = field(
        default_factory=list,
        metadata={
            "name": "FareFamilyDelete",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class UpsellAdminRsp(BaseRsp):
    """
    Response to add/delete/update of offer/qualify.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_rule: List[AirUpsellRule] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_upsell_rule: List[VehicleUpsellRule] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_upsell_rule: List[HotelUpsellRule] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellRule",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class UpsellSearchRsp(BaseRsp):
    """
    Response containing qualify and offer for the matching search criteria.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_search_result: List[AirUpsellSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellSearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_upsell_search_result: List[HotelUpsellSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellSearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_upsell_search_result: List[VehicleUpsellSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellSearchResult",
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
class UpsellAdminReq(BaseReq):
    """
    Request to add/delete/update qualify/offer.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_criteria: Optional[AirUpsellCriteria] = field(
        default=None,
        metadata={
            "name": "AirUpsellCriteria",
            "type": "Element",
        }
    )
    vehicle_upsell_criteria: Optional[VehicleUpsellCriteria] = field(
        default=None,
        metadata={
            "name": "VehicleUpsellCriteria",
            "type": "Element",
        }
    )
    hotel_upsell_criteria: Optional[HotelUpsellCriteria] = field(
        default=None,
        metadata={
            "name": "HotelUpsellCriteria",
            "type": "Element",
        }
    )
