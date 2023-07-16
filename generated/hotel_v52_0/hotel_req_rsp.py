from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.common_v52_0.common import (
    HostToken,
    Keyword,
    MarketingInformation,
    NextResultReference,
    PermittedProviders,
    PointOfSale,
    VendorLocation,
)
from generated.common_v52_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
    BaseSearchReq,
    BaseSearchRsp,
)
from generated.hotel_v52_0.hotel import (
    CurrencyRateConversion,
    GuestReviews,
    HotelAlternateProperties,
    HotelDetailItem,
    HotelDetailsModifiers,
    HotelProperty,
    HotelPropertyWithMediaItems,
    HotelRateDetail,
    HotelReservation,
    HotelRuleItem,
    HotelRulesModifiers,
    HotelSearchLocation,
    HotelSearchModifiers,
    HotelSearchResult,
    HotelStay,
    HotelSuperShopperResults,
    HotelType,
    QuickResponse,
    RequestedHotelDetails,
    TypeHotelReferencePoint,
    TypeRequestedImageSize,
)

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class HotelRulesLookupRulesDetailReqd(Enum):
    RULES = "Rules"
    DETAILS = "Details"
    ALL = "All"


@dataclass
class RatesAndDates:
    """Contains the rates that apply over a date range, all with the same status.

    May represent multiple rooms.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    low: Optional[str] = field(
        default=None,
        metadata={
            "name": "Low",
            "type": "Attribute",
            "required": True,
        }
    )
    high: Optional[str] = field(
        default=None,
        metadata={
            "name": "High",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BaseHotelDetailsReq(BaseReq):
    """
    Base request for all hotel details search request..
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
    hotel_details_modifiers: Optional[HotelDetailsModifiers] = field(
        default=None,
        metadata={
            "name": "HotelDetailsModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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
class BaseHotelDetailsRsp(BaseRsp):
    """
    Base response for all hotel details search response.

    :ivar hotel_property:
    :ivar hotel_detail_item:
    :ivar hotel_rate_detail: Only returned if number of adults and
        checkin/checkout given on request
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
    hotel_detail_item: List[HotelDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailItem",
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


@dataclass
class BaseHotelSearchReq(BaseSearchReq):
    """
    Base hotel Search Request.

    :ivar hotel_search_location:
    :ivar hotel_search_modifiers:
    :ivar hotel_stay:
    :ivar point_of_sale:
    :ivar policy_reference: This attribute will be used to pass in a
        value on the request which would be used to link to a ‘Policy
        Group’ in a policy engine external to UAPI.
    """
    hotel_search_location: Optional[HotelSearchLocation] = field(
        default=None,
        metadata={
            "name": "HotelSearchLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    hotel_search_modifiers: Optional[HotelSearchModifiers] = field(
        default=None,
        metadata={
            "name": "HotelSearchModifiers",
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
class BaseHotelSearchRsp(BaseSearchRsp):
    """
    Base hotel Search Response.

    :ivar reference_point: Hotel reference point.  Applicable for
        1G,1V,1P.
    :ivar hotel_search_result:
    :ivar marketing_information:
    :ivar host_token:
    :ivar address_search_quality: Indicates the address matching level
        success for hotel address or Postal Code searches. Valid values:
        "1"-"8". Providers 1G, 1V.
    """
    reference_point: Optional[TypeHotelReferencePoint] = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        }
    )
    hotel_search_result: List[HotelSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "HotelSearchResult",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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
    host_token: Optional[HostToken] = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    address_search_quality: Optional[int] = field(
        default=None,
        metadata={
            "name": "AddressSearchQuality",
            "type": "Attribute",
        }
    )


@dataclass
class HotelDetailsRsp(BaseRsp):
    """
    Response showing details of a given hotel property.

    :ivar next_result_reference:
    :ivar host_token:
    :ivar requested_hotel_details: Supported Provider GDS – 1G, 1V, 1P.
    :ivar hotel_alternate_properties:
    :ivar guest_reviews:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    next_result_reference: Optional[NextResultReference] = field(
        default=None,
        metadata={
            "name": "NextResultReference",
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
    requested_hotel_details: Optional[RequestedHotelDetails] = field(
        default=None,
        metadata={
            "name": "RequestedHotelDetails",
            "type": "Element",
        }
    )
    hotel_alternate_properties: Optional[HotelAlternateProperties] = field(
        default=None,
        metadata={
            "name": "HotelAlternateProperties",
            "type": "Element",
        }
    )
    guest_reviews: Optional[GuestReviews] = field(
        default=None,
        metadata={
            "name": "GuestReviews",
            "type": "Element",
        }
    )


@dataclass
class HotelKeywordReq(BaseReq):
    """
    Request to retrieve the hotel keyword details of a hotel chain or property.

    :ivar keyword: Used to request specific keyword details.
    :ivar permitted_providers:
    :ivar hotel_chain:
    :ivar hotel_code:
    :ivar checkin_date:
    :ivar return_keyword_list: When true, a list of keyword names should
        be returned. If false then list of keyword details should be
        returned
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 15,
        }
    )
    permitted_providers: Optional[PermittedProviders] = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_chain: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelChain",
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
    checkin_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckinDate",
            "type": "Attribute",
            "pattern": r"[^:Z].*",
        }
    )
    return_keyword_list: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnKeywordList",
            "type": "Attribute",
        }
    )


@dataclass
class HotelKeywordRsp(BaseRsp):
    """
    Response showing keyword details of a given hotel chain or property.

    :ivar marketing_information:
    :ivar keyword: A word that a vendor uses to describe corporate
        policy/information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    marketing_information: Optional[MarketingInformation] = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )


@dataclass
class HotelMediaLinksReq(BaseReq):
    """Retrieves all image links from the Galileo Web Services Image Viewer eBL for
    up to 20 properties.

    Only the attributes of the HotelProperty are used in this request.

    :ivar permitted_providers:
    :ivar hotel_property:
    :ivar secure_links: Request URLs returned use secured site (https)
        references. Default is true
    :ivar size_code: Requested image size. Default is to get ALL images
    :ivar rich_media: Request the Rich Media link. Default is true
    :ivar gallery: Request the Image Gallery link. Default is true
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    permitted_providers: Optional[PermittedProviders] = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_property: List[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )
    secure_links: bool = field(
        default=True,
        metadata={
            "name": "SecureLinks",
            "type": "Attribute",
        }
    )
    size_code: TypeRequestedImageSize = field(
        default=TypeRequestedImageSize.A,
        metadata={
            "name": "SizeCode",
            "type": "Attribute",
        }
    )
    rich_media: bool = field(
        default=True,
        metadata={
            "name": "RichMedia",
            "type": "Attribute",
        }
    )
    gallery: bool = field(
        default=True,
        metadata={
            "name": "Gallery",
            "type": "Attribute",
        }
    )


@dataclass
class HotelMediaLinksRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property_with_media_items: List[HotelPropertyWithMediaItems] = field(
        default_factory=list,
        metadata={
            "name": "HotelPropertyWithMediaItems",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )


@dataclass
class HotelRetrieveReq(BaseReq):
    """Retrieve request for a hotel booking.

    Given a provider code and a provider locator code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

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
class HotelRetrieveRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_reservation: List[HotelReservation] = field(
        default_factory=list,
        metadata={
            "name": "HotelReservation",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class HotelRulesReq(BaseReq):
    """
    Retrieves hotel rules using hotel property code, chain code and hotel room rate
    type.

    :ivar hotel_reservation_locator_code: Request hotel rules using
        Locator code of existing hotel reservation.
    :ivar hotel_rules_lookup: Details to request Hotel rate rules post
        shopping request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_reservation_locator_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    hotel_rules_lookup: Optional["HotelRulesReq.HotelRulesLookup"] = field(
        default=None,
        metadata={
            "name": "HotelRulesLookup",
            "type": "Element",
        }
    )

    @dataclass
    class HotelRulesLookup:
        """
        :ivar hotel_property:
        :ivar hotel_stay:
        :ivar hotel_rules_modifiers:
        :ivar rate_plan_type: This is room rate plan type for a
            particular rate plan
        :ivar base: This is the Base Amount for the selected rate plan
            type as received in Hotel Details/Book/Modify Response.
        :ivar rules_detail_reqd: Request details for Rules, Details, or
            All.  Default is All. Applicable for 1p.
        """
        hotel_property: Optional[HotelProperty] = field(
            default=None,
            metadata={
                "name": "HotelProperty",
                "type": "Element",
                "required": True,
            }
        )
        hotel_stay: Optional[HotelStay] = field(
            default=None,
            metadata={
                "name": "HotelStay",
                "type": "Element",
                "required": True,
            }
        )
        hotel_rules_modifiers: Optional[HotelRulesModifiers] = field(
            default=None,
            metadata={
                "name": "HotelRulesModifiers",
                "type": "Element",
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
        base: Optional[str] = field(
            default=None,
            metadata={
                "name": "Base",
                "type": "Attribute",
                "required": True,
            }
        )
        rules_detail_reqd: Optional[HotelRulesLookupRulesDetailReqd] = field(
            default=None,
            metadata={
                "name": "RulesDetailReqd",
                "type": "Attribute",
            }
        )


@dataclass
class HotelRulesRsp(BaseRsp):
    """
    Response showing rule details of a given hotel property and room rate code.

    :ivar hotel_rate_detail: Returns hotels rate and rule details.
    :ivar hotel_rule_item: Return rules and policies related to the
        property (Like Cancellation, Accepted FOP etc.).
    :ivar hotel_type: Supported Providers:1G/1V/1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_rate_detail: List[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rule_item: List[HotelRuleItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelRuleItem",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_type: Optional[HotelType] = field(
        default=None,
        metadata={
            "name": "HotelType",
            "type": "Element",
        }
    )


@dataclass
class HotelSuperShopperReq(BaseSearchReq):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_search_location: Optional[HotelSearchLocation] = field(
        default=None,
        metadata={
            "name": "HotelSearchLocation",
            "type": "Element",
        }
    )
    hotel_search_modifiers: Optional[HotelSearchModifiers] = field(
        default=None,
        metadata={
            "name": "HotelSearchModifiers",
            "type": "Element",
        }
    )
    hotel_stay: Optional[HotelStay] = field(
        default=None,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "required": True,
        }
    )
    quick_response: Optional[QuickResponse] = field(
        default=None,
        metadata={
            "name": "QuickResponse",
            "type": "Element",
        }
    )


@dataclass
class HotelSuperShopperRsp(BaseSearchRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    vendor_location: List[VendorLocation] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    currency_rate_conversion: List[CurrencyRateConversion] = field(
        default_factory=list,
        metadata={
            "name": "CurrencyRateConversion",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_super_shopper_results: List[HotelSuperShopperResults] = field(
        default_factory=list,
        metadata={
            "name": "HotelSuperShopperResults",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    quick_response: Optional[QuickResponse] = field(
        default=None,
        metadata={
            "name": "QuickResponse",
            "type": "Element",
        }
    )


@dataclass
class HotelUpsellDetailsReq(BaseReq):
    """
    Upsell Request to retrieve the details of a hotel property.

    :ivar hotel_property:
    :ivar hotel_rate_detail: Only returned if number of adults and
        checkin/checkout given on request
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property: Optional[HotelProperty] = field(
        default=None,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "required": True,
        }
    )
    hotel_rate_detail: Optional[HotelRateDetail] = field(
        default=None,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
        }
    )


@dataclass
class HotelDetailsReq(BaseHotelDetailsReq):
    """
    Request to retrieve the details of a hotel property.

    :ivar host_token:
    :ivar next_result_reference:
    :ivar return_media_links: If true, return the media links. Not
        supported by all providers
    :ivar return_guest_reviews: If true, return reviews and comments for
        the hotel property.  Not supported by all providers
    :ivar policy_reference: This attribute will be used to pass in a
        value on the request which would be used to link to a ‘Policy
        Group’ in a policy engine external to UAPI.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    host_token: Optional[HostToken] = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    next_result_reference: Optional[NextResultReference] = field(
        default=None,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    return_media_links: bool = field(
        default=False,
        metadata={
            "name": "ReturnMediaLinks",
            "type": "Attribute",
        }
    )
    return_guest_reviews: bool = field(
        default=False,
        metadata={
            "name": "ReturnGuestReviews",
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


@dataclass
class HotelSearchAvailabilityReq(BaseHotelSearchReq):
    """
    Request to search for hotel availability.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSearchAvailabilityRsp(BaseHotelSearchRsp):
    """
    Hotel availablity search response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelUpsellDetailsRsp(BaseHotelDetailsRsp):
    """
    Upsell Response showing details of a given hotel property.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"
