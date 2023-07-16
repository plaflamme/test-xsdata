from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from generated.common_v52_0.common import (
    BaseReservation,
    BookingSource,
    BookingTravelerRef,
    CoordinateLocation,
    CorporateDiscountId,
    Distance,
    Email,
    Guarantee,
    LoyaltyCard,
    MediaItem,
    PermittedProviders,
    PhoneNumber,
    ReservationName,
    ThirdPartyInformation,
    VendorLocation,
    TypeAssociatedRemark,
    TypePolicyCodesList,
    TypeReserveRequirement,
    TypeResultMessage,
    TypeStructuredAddress,
    TypeTrinary,
)

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class AcceptedPayment:
    """
    :ivar payment_code: The issuer of the form of payment, such as the
        credit card bank.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    payment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
        }
    )


@dataclass
class Amenity:
    """
    :ivar code:
    :ivar amenity_type: Amenity type code. “HA” (Hotel Property Amenity)
        or “RA” (Room Amenity). Defaults to “HA” if no value is sent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 999,
        }
    )
    amenity_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmenityType",
            "type": "Attribute",
            "length": 2,
        }
    )


@dataclass
class BookingConfirmation:
    """Hotel Booking Confirmation Number for hotel segment.

    Supported Providers:1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "max_length": 32,
        }
    )


class CriteriaType(Enum):
    CORPORATE_DISCOUNT_ID = "CorporateDiscountID"
    PERMITTED_CHAINS = "PermittedChains"
    HOTEL_NAME = "HotelName"
    DISTANCE = "Distance"
    RATE_CATEGORY = "RateCategory"
    HOTEL_RATING = "HotelRating"
    AMENITIES = "Amenities"
    HOTEL_TRANSPORTATION = "HotelTransportation"


@dataclass
class CurrencyRateConversion:
    """Currency rate conversion from the supplier’s source currency to a preferred
    currency.

    For hotels, applicable only to Hotel Super Shopper (1G/1V).

    :ivar rate_conversion: Rate multiplier from the supplier’s local or
        quoted currency to requested currency. Used to derive the
        requested conversion currency amount.
    :ivar source_currency_code: 3-character ISO currency code for
        supplier's local or quoted currency.
    :ivar requested_currency_code: 3-character ISO currency code for the
        requester's preferred currency
    :ivar decimal_places: The number of decimal places for the requested
        currency at conversion.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    rate_conversion: Optional[float] = field(
        default=None,
        metadata={
            "name": "RateConversion",
            "type": "Attribute",
        }
    )
    source_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    requested_currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedCurrencyCode",
            "type": "Attribute",
            "length": 3,
        }
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        }
    )


@dataclass
class DepositAmount:
    """
    Amount required for deposit/prepayment.

    :ivar amount: Supplier deposit amount required for
        deposit/prepayment.Supported by all Providers when supported by
        supplier
    :ivar approximate_amount: Approximate deposit amount required for
        deposit/prepayment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    approximate_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateAmount",
            "type": "Attribute",
        }
    )


class GuaranteeInfoGuaranteeType(Enum):
    DEPOSIT = "Deposit"
    GUARANTEE = "Guarantee"
    PREPAYMENT = "Prepayment"


@dataclass
class GuaranteePaymentType:
    """Accepted payment types.

    Applicable only for HotelSupershopper, Hotel Details and Hotel
    rules.

    :ivar value:
    :ivar type_value: Accepted payment types: CreditCard,
        AgencyIATA/ARC, FrequentGuest, SpecialIndustry, CDNumber,
        HomeAddress, CompanyAddress, Override, Other, or None
    :ivar description:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
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
        }
    )


@dataclass
class GuestReviews:
    """
    Comments and Reviews from hotel guests.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    comments: List["GuestReviews.Comments"] = field(
        default_factory=list,
        metadata={
            "name": "Comments",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )

    @dataclass
    class Comments:
        """
        :ivar value:
        :ivar comment_id: Unique comment identifier. For internal
            Travelport use only.
        :ivar date: date that the comment was entered.
        :ivar commenter_language: Language of the commenter.
        :ivar source: Source code of the comment entry. Example: 'NB'
            for Nightsbridge, ‘RG’, ‘AG’ for Agrialla,‘TO’.
        :ivar comment_source_name: Name of the source for the comment.
        :ivar commenter: Name of the comment's poster.
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
        )
        comment_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "CommentId",
                "type": "Attribute",
            }
        )
        date: Optional[str] = field(
            default=None,
            metadata={
                "name": "Date",
                "type": "Attribute",
                "pattern": r"[^:Z].*",
            }
        )
        commenter_language: Optional[str] = field(
            default=None,
            metadata={
                "name": "CommenterLanguage",
                "type": "Attribute",
                "length": 2,
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "name": "Source",
                "type": "Attribute",
            }
        )
        comment_source_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "CommentSourceName",
                "type": "Attribute",
            }
        )
        commenter: Optional[str] = field(
            default=None,
            metadata={
                "name": "Commenter",
                "type": "Attribute",
            }
        )


@dataclass
class HotelBedding:
    """
    Specify desired bedding.

    :ivar type_value: Queen, King, double, etc
    :ivar number_of_beds: Number of beds of desired Type in room. Use
        '0' to delete the hotel Optional Beds ( Only RA RC CR )
    :ivar amount: Fee for bed type.  Providers:  1g/1v/1p
    :ivar content: Additional information Providers: 1p
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    number_of_beds: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfBeds",
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
    content: Optional[str] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Attribute",
        }
    )


@dataclass
class HotelChain:
    """
    The hotel chain code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )


@dataclass
class HotelCommission:
    """Indicates the commission during Hotel reservation.

    Provider supoorted 1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class HotelDetailItem:
    """
    Textual information about the hotel.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
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
class HotelRateByDate:
    """
    The daily rate details.

    :ivar effective_date:
    :ivar expire_date:
    :ivar base: This attribute is used to describe the Hotel Supplier
        Base Rate
    :ivar tax: This attribute used to describe Tax associated with the
        room
    :ivar total: This attribute used to describe Hotel Supplier Total
        Rate
    :ivar surcharge: This attribute used to describe Surcharge
        associated with the room
    :ivar approximate_base: Hotel base rate expressed in another
        currency
    :ivar approximate_total: Hotel total rate expressed in another
        currency.  Supported Providers: 1P
    :ivar contents: Contents will be representing all unformatted data
        returned by HOST, those are not uAPI supported. Support provider
        1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        }
    )
    expire_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "name": "Base",
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
    total: Optional[str] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
        }
    )
    surcharge: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surcharge",
            "type": "Attribute",
        }
    )
    approximate_base: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBase",
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
    contents: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contents",
            "type": "Attribute",
        }
    )


@dataclass
class HotelRateInfo:
    """
    This is a wrapper element for updating Rate Modifiers.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    rate_plan_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
        }
    )


@dataclass
class HotelRuleItem:
    """
    Textual information about the hotel rule.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
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
class HotelSpecialRequest:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 250,
        }
    )


@dataclass
class HotelStay:
    """
    Arrival and Departure dates.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    checkin_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckinDate",
            "type": "Element",
            "required": True,
            "pattern": r"[^:Z].*",
        }
    )
    checkout_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckoutDate",
            "type": "Element",
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


@dataclass
class HotelType:
    """
    :ivar source_link: Indicates whether results are  returned from the
        vendor or  from the database.  If true, vendor results were
        returned. Supported providers:1G, 1V
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    source_link: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SourceLink",
            "type": "Attribute",
        }
    )


@dataclass
class MarketingMessage:
    """
    Marketing information provided by the supplier.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class NumberOfAdults:
    """
    Number of Adults.

    :ivar value:
    :ivar extra_adults: The number of extra adults in the room ,use '0'
        to delete the extra adults
    :ivar amount: Fee for extra adults.  Providers: 1g/1v/1p
    :ivar content: Additional information.  Providers 1p
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    extra_adults: Optional[int] = field(
        default=None,
        metadata={
            "name": "ExtraAdults",
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
    content: Optional[str] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Attribute",
        }
    )


@dataclass
class NumberOfChildren:
    """
    Number of Children.

    :ivar age: The Ages of the Children. . The defined age of a Child
        traveler may vary by supplier, but is typically 1 to 17 years.
        Supported Providers 1G/1V.
    :ivar count: The total number of children in the booking. Supported
        Providers 1P.
    :ivar amount: Fee per child. Providers: 1g/1v
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    age: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Age",
            "type": "Element",
            "max_occurs": 99,
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
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )


@dataclass
class PromotionCode:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
class PropertyDescription:
    """
    :ivar value:
    :ivar provider_code: The host associated with this token
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    value: str = field(
        default="",
        metadata={
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


@dataclass
class QuickResponse:
    """
    :ivar fast_result: Set to true on initial request to have results
        returned immediately and may contain fewer hotels. Default is
        false.
    :ivar more_token: Token is returned for use in subsequent request to
        retrieve complete results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    fast_result: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FastResult",
            "type": "Attribute",
        }
    )
    more_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoreToken",
            "type": "Attribute",
        }
    )


class RateMatchIndicatorStatus(Enum):
    """
    :cvar AVAILABLE: Number of items requested for the IndicatorType is
        available
    :cvar NOT_AVAILABLE: Number of items requested for the IndicatorType
        is not available. The actual number available is provided
        against Value
    :cvar SUBSTITUTE_OFFERED: A substitute has been offered for the
        originally requested number and/or type. The substituted
        available is provided in against Value
    :cvar MAXIMUM_EXCEEDED: Number of items requested for the
        IndicatorType exceeds the maximum applicable value. The
        substituted available is provided in against Value
    """
    AVAILABLE = "Available"
    NOT_AVAILABLE = "NotAvailable"
    SUBSTITUTE_OFFERED = "SubstituteOffered"
    MAXIMUM_EXCEEDED = "MaximumExceeded"


class RateMatchIndicatorType(Enum):
    RATE_CATEGORY = "RateCategory"
    ROOM_COUNT = "RoomCount"
    ADULT_COUNT = "AdultCount"
    CHILD_COUNT = "ChildCount"
    ADULT_ROLLAWAY = "AdultRollaway"
    CHILD_ROLLAWAY = "ChildRollaway"
    CRIB = "Crib"


@dataclass
class RatingRange:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    minimum_rating: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumRating",
            "type": "Attribute",
        }
    )
    maximum_rating: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumRating",
            "type": "Attribute",
        }
    )


@dataclass
class RoomView:
    """
    :ivar code: OTA code represents different hotel room views.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )


@dataclass
class Tax:
    """
    :ivar amount:
    :ivar percentage:
    :ivar code: Code identifying fee (e.g. agency fee, bed tax etc.).
        Refer to OPEN Travel Code List for Fee Tax Type. Possible values
        are OTA Code against FTT.
    :ivar effective_date:
    :ivar expiration_date:
    :ivar term: Indicates how the tax is applied. Values can be
        PerPerson, PerNight and PerStay
    :ivar collection_freq: Indicates how often the tax is collected.
        Values can be Once or Daily
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        }
    )
    percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
        }
    )
    code: Optional[int] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    effective_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        }
    )
    expiration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
        }
    )
    term: Optional[str] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Attribute",
        }
    )
    collection_freq: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollectionFreq",
            "type": "Attribute",
        }
    )


class TypeAmenityLevel(Enum):
    PROPERTY = "Property"
    ROOM = "Room"


@dataclass
class TypeGuestChildInformation:
    """
    Infomration about the Child guest.

    :ivar age: Age of the Child.
    """
    class Meta:
        name = "typeGuestChildInformation"

    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        }
    )


class TypeHotelAvailability(Enum):
    """
    Availability status of hotel Hotel is Available NotAvailable Available, but not
    for the rates requested On request Unknown.
    """
    AVAILABLE = "Available"
    NOT_AVAILABLE = "NotAvailable"
    AVAILABLE_FOR_OTHER_RATES = "AvailableForOtherRates"
    ON_REQUEST = "OnRequest"
    UNKNOWN = "Unknown"


class TypeHotelLocation(Enum):
    CITY = "City"
    AIRPORT = "Airport"


@dataclass
class TypeHotelRateDescription:
    """
    :ivar text:
    :ivar name: Optional context name of the text block being returned
        i.e. Room details
    """
    class Meta:
        name = "typeHotelRateDescription"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
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
class TypeHotelReferencePoint:
    """
    :ivar value:
    :ivar country: Country code.
    :ivar state: State or Province Code.
    """
    class Meta:
        name = "typeHotelReferencePoint"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 30,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "max_length": 6,
        }
    )


class TypeNetTransCommission(Enum):
    """Type to support net trans commission indicator.

    Supported for 1G and 1V provider. A stands for Excellent. B stands
    for Good. C stands for Poor. P stands for Payment Bureau X stands
    for Unknown. To support any other value than A,B,C and P.
    """
    A = "A"
    B = "B"
    C = "C"
    P = "P"
    X = "X"


class TypeRateRuleDetail(Enum):
    """'None' returns hotel property descriptive information-supported for
    1p,1g/1v.

    'Complete' returns the complete hotel and room rate information-supported for 1p,1g/1v, 'RatePlansOnly' returns hotel rate information only - supported for 1p.
    """
    NONE = "None"
    COMPLETE = "Complete"
    RATE_PLANS_ONLY = "RatePlansOnly"


class TypeRequestedImageSize(Enum):
    T = "T"
    I = "I"
    S = "S"
    M = "M"
    L = "L"
    E = "E"
    G = "G"
    F = "F"
    B = "B"
    J = "J"
    O = "O"
    H = "H"
    C = "C"
    A = "A"


@dataclass
class TypeUnstructuredAddress:
    """
    A simple unstructured address (e.g. 123 South State Avenue, Chicago, IL 60612)
    """
    class Meta:
        name = "typeUnstructuredAddress"

    address: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "min_occurs": 1,
            "max_occurs": 6,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class Amenities:
    """
    Amenity information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    amenity: List[Amenity] = field(
        default_factory=list,
        metadata={
            "name": "Amenity",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AssociatedRemark(TypeAssociatedRemark):
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class CancelInfo:
    """Returns cancellation information for certain hotel returned in response.

    This information is available through GDS transactions

    :ivar cancellation_policy: Return cancellation policy text by the
        aggregator.
    :ivar text: The informational text provided by the supplier to
        cancel the booking, if @Method="INFO". For all other values of
        @Method, Text is not returned.
    :ivar non_refundable_stay_indicator: True if Deposit or Payment is
        non-refundable
    :ivar cancel_deadline: Last date/time the reservation can be
        canceled without penalty.
    :ivar tax_inclusive: Indicates whether or not the Penalty amount
        includes taxes.
    :ivar fee_inclusive: Indicates whether or not the Penalty amount
        includes fees.
    :ivar cancel_penalty_amount: This will contain the cancellation
        penalty amount.
    :ivar number_of_nights: This will contain the number of nights that
        will be assessed as the cancelation penalty.
    :ivar cancel_penalty_percent: This will contain the cancellation
        penalty expressed as a percentage.
    :ivar cancel_penalty_percent_applies_to: This will contain the cost
        qualifier that explains what the percentage is applied to in
        order to calculate the cancel penalty.
    :ivar method: Cancellation method, either "API", "URL", "INFO", or
        "NONE".
    :ivar supported: If true, the booking can be canceled. If false, the
        booking cannot be canceled.
    :ivar url: The URL provided by the supplier to cancel the booking,
        if @Method="URL". For all other values of @Method, @URL is not
        returned.
    :ivar offset_time_unit: The units of time, e.g: days, hours, etc
        that apply to the deadline. Enumerated values are “Year”,
        “Month”, “Day”, and “Hour”.
    :ivar offset_unit_multiplier: The number of units of
        DeadlineTimeUnit.
    :ivar offset_drop_time: An enumerated type indicating when the
        deadline drop time goes into effect. Enumerated values are
        “AfterBooking” and “BeforeArrival”.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    cancellation_policy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancellationPolicy",
            "type": "Element",
        }
    )
    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    non_refundable_stay_indicator: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "NonRefundableStayIndicator",
            "type": "Attribute",
        }
    )
    cancel_deadline: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CancelDeadline",
            "type": "Attribute",
        }
    )
    tax_inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxInclusive",
            "type": "Attribute",
        }
    )
    fee_inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FeeInclusive",
            "type": "Attribute",
        }
    )
    cancel_penalty_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancelPenaltyAmount",
            "type": "Attribute",
        }
    )
    number_of_nights: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfNights",
            "type": "Attribute",
        }
    )
    cancel_penalty_percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "CancelPenaltyPercent",
            "type": "Attribute",
        }
    )
    cancel_penalty_percent_applies_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancelPenaltyPercentAppliesTo",
            "type": "Attribute",
        }
    )
    method: Optional[str] = field(
        default=None,
        metadata={
            "name": "Method",
            "type": "Attribute",
        }
    )
    supported: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Supported",
            "type": "Attribute",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
        }
    )
    offset_time_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffsetTimeUnit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    offset_unit_multiplier: Optional[int] = field(
        default=None,
        metadata={
            "name": "OffsetUnitMultiplier",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    offset_drop_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffsetDropTime",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )


@dataclass
class Commission:
    """
    :ivar indicator: Indicates if the Rate Plan is commissionable.True:
        Rate is commissionable.False: Rate is not
        commissionable.Unknown: Commission indicator is not returned by
        the hotel supplier (chain or property).
    :ivar percent: The percentage applied to the commissionable amount
        to determine the payable commission amount.
    :ivar commission_amount: The commission amount in the aggregator’s
        or supplier’s currency.
    :ivar approx_commission_amount: The approximate commission amount in
        the agency’s provisioned or requested currency.
    :ivar commission_on_surcharges: Commission on surcharges in the
        aggregator’s or supplier’s currency.
    :ivar approx_commission_on_surcharges: The approximate commission on
        surcharges in the agency’s provisioned or requested currency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    indicator: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
        }
    )
    commission_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommissionAmount",
            "type": "Attribute",
        }
    )
    approx_commission_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproxCommissionAmount",
            "type": "Attribute",
        }
    )
    commission_on_surcharges: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommissionOnSurcharges",
            "type": "Attribute",
        }
    )
    approx_commission_on_surcharges: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproxCommissionOnSurcharges",
            "type": "Attribute",
        }
    )


@dataclass
class GuaranteeInfo:
    """
    :ivar deposit_amount: Amount required for deposit/prepayment
    :ivar deposit_nights: Number of Nights required for
        deposit/prepayment
    :ivar deposit_percent: Percentage of stay required for
        deposit/prepayment
    :ivar guarantee_payment_type: Accepted payment types
    :ivar absolute_deadline: Latest date/time when
        deposit/payment/guarantee is required.
    :ivar credentials_required: Identification required at
        booking/checkin. Not supported by 1P.
    :ivar hold_time: Expiration time for room reservation held without
        deposit/guarantee.
    :ivar guarantee_type: Deposit, Guarantee, or Prepayment required to
        hold/book the room. Applicable only for HotelSupershopper, Hotel
        Details and Hotel rules.
    :ivar offset_time_unit: The units of time, e.g: days, hours, etc
        that apply to the deadline. Enumerated values are “Year”,
        “Month”, “Day”, and “Hour”.
    :ivar offset_unit_multiplier: The number of units of
        DeadlineTimeUnit.
    :ivar offset_drop_time: An enumerated type indicating when the
        deadline drop time goes into effect. Enumerated values are
        “AfterBooking” and “BeforeArrival”.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    deposit_amount: Optional[DepositAmount] = field(
        default=None,
        metadata={
            "name": "DepositAmount",
            "type": "Element",
        }
    )
    deposit_nights: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepositNights",
            "type": "Element",
        }
    )
    deposit_percent: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepositPercent",
            "type": "Element",
        }
    )
    guarantee_payment_type: List[GuaranteePaymentType] = field(
        default_factory=list,
        metadata={
            "name": "GuaranteePaymentType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    absolute_deadline: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AbsoluteDeadline",
            "type": "Attribute",
        }
    )
    credentials_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CredentialsRequired",
            "type": "Attribute",
        }
    )
    hold_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "HoldTime",
            "type": "Attribute",
        }
    )
    guarantee_type: Optional[GuaranteeInfoGuaranteeType] = field(
        default=None,
        metadata={
            "name": "GuaranteeType",
            "type": "Attribute",
        }
    )
    offset_time_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffsetTimeUnit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    offset_unit_multiplier: Optional[int] = field(
        default=None,
        metadata={
            "name": "OffsetUnitMultiplier",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    offset_drop_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffsetDropTime",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )


@dataclass
class GuestInformation:
    """
    The information like number of rooms ,number of adults,children to be provided
    while booking the  hotel.

    :ivar number_of_adults:
    :ivar number_of_children:
    :ivar extra_child: Providers: 1p
    :ivar number_of_rooms:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    number_of_adults: Optional[NumberOfAdults] = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Element",
        }
    )
    number_of_children: Optional[NumberOfChildren] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        }
    )
    extra_child: Optional["GuestInformation.ExtraChild"] = field(
        default=None,
        metadata={
            "name": "ExtraChild",
            "type": "Element",
        }
    )
    number_of_rooms: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfRooms",
            "type": "Attribute",
        }
    )

    @dataclass
    class ExtraChild:
        """
        :ivar count: The number of extra children in the room
        :ivar content: Additional information
        """
        count: Optional[int] = field(
            default=None,
            metadata={
                "name": "Count",
                "type": "Attribute",
            }
        )
        content: Optional[str] = field(
            default=None,
            metadata={
                "name": "Content",
                "type": "Attribute",
            }
        )


@dataclass
class HotelAmenity:
    """
    :ivar level: Property or Room amenity
    :ivar amenity_code: OTA amenity code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    level: Optional[TypeAmenityLevel] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "required": True,
        }
    )
    amenity_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "AmenityCode",
            "type": "Attribute",
            "required": True,
            "total_digits": 3,
        }
    )


@dataclass
class HotelLocation:
    """Date and Location information for the Hotel.

    Location can be optional if a Reference Point is provided.

    :ivar location: IATA city/airport code
    :ivar location_type:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    location_type: TypeHotelLocation = field(
        default=TypeHotelLocation.AIRPORT,
        metadata={
            "name": "LocationType",
            "type": "Attribute",
        }
    )


@dataclass
class HotelRating:
    """
    Hotel rating information.

    :ivar rating: Hotel rating value
    :ivar rating_range: Search for a range of ratings
    :ivar rating_provider: Rating providers, ie AAA, NTM
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    rating: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Rating",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rating_range: Optional[RatingRange] = field(
        default=None,
        metadata={
            "name": "RatingRange",
            "type": "Element",
        }
    )
    rating_provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "RatingProvider",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HotelRulesModifiers:
    """
    Controls and switches for the Hotel Rules request.

    :ivar permitted_providers:
    :ivar number_of_children:
    :ivar hotel_bedding:
    :ivar rate_category: Specify Rate Category
    :ivar corporate_discount_id:
    :ivar number_of_adults: Defaults to 1 if not specified
    :ivar number_of_rooms: The numbers of rooms,defaults to 1 if not
        specified
    :ivar total_occupants: Number of guests for the room.  Supported
        Providers: 1P
    :ivar key:
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
    number_of_children: Optional[NumberOfChildren] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    rate_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Element",
        }
    )
    corporate_discount_id: List[CorporateDiscountId] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 2,
        }
    )
    number_of_adults: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        }
    )
    number_of_rooms: int = field(
        default=1,
        metadata={
            "name": "NumberOfRooms",
            "type": "Attribute",
        }
    )
    total_occupants: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalOccupants",
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
class RateInfo:
    """
    :ivar policy_codes_list: A list of codes that indicate why an item
        was determined to be ‘out of policy’.
    :ivar minimum_amount: The low end of the nightly price range
    :ivar approximate_minimum_amount: The low end of the nightly price
        range in another currency
    :ivar min_amount_rate_changed: Indicates the low end price range
        changes over the requested stay
    :ivar maximum_amount: The high end of the nightly price range
    :ivar approximate_maximum_amount: The high end of the nightly price
        range in another currency
    :ivar max_amount_rate_changed: Indicates the high end price range
        changes over the requested stay
    :ivar minimum_stay_amount: The low end of the price range for the
        entire stay
    :ivar approximate_minimum_stay_amount: The low end of the price
        range for the entire stay in another currency
    :ivar commission: Commission information for this rate supplier
    :ivar rate_supplier: Indicates the supplier of the rate.
    :ivar rate_supplier_logo: Url of the supplier's logo
    :ivar min_in_policy: This attribute will be used to indicate if the
        minimum fare or rate has been determined to be ‘in policy’ based
        on the associated policy settings.
    :ivar max_in_policy: This attribute will be used to indicate if the
        maximum fare or rate has been determined to be ‘in policy’ based
        on the associated policy settings.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    policy_codes_list: Optional[TypePolicyCodesList] = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        }
    )
    minimum_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Attribute",
        }
    )
    approximate_minimum_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateMinimumAmount",
            "type": "Attribute",
        }
    )
    min_amount_rate_changed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MinAmountRateChanged",
            "type": "Attribute",
        }
    )
    maximum_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Attribute",
        }
    )
    approximate_maximum_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateMaximumAmount",
            "type": "Attribute",
        }
    )
    max_amount_rate_changed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MaxAmountRateChanged",
            "type": "Attribute",
        }
    )
    minimum_stay_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinimumStayAmount",
            "type": "Attribute",
        }
    )
    approximate_minimum_stay_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateMinimumStayAmount",
            "type": "Attribute",
        }
    )
    commission: Optional[str] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Attribute",
        }
    )
    rate_supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateSupplier",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    rate_supplier_logo: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateSupplierLogo",
            "type": "Attribute",
        }
    )
    min_in_policy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MinInPolicy",
            "type": "Attribute",
        }
    )
    max_in_policy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MaxInPolicy",
            "type": "Attribute",
        }
    )


@dataclass
class RateMatchIndicator:
    """
    "Match" Indicators for certain request parameters, e.g. Child Count, Extra
    Adults etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    type_value: Optional[RateMatchIndicatorType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    status: Optional[RateMatchIndicatorStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )


@dataclass
class SearchPriority:
    """
    Override the search order for hotel availability request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    criteria: List["SearchPriority.Criteria"] = field(
        default_factory=list,
        metadata={
            "name": "Criteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 8,
        }
    )

    @dataclass
    class Criteria:
        """
        :ivar order: Criteria order for hotel search Highest Priority=1
            Lowest Priority=7
        :ivar type_value: Search type
        """
        order: Optional[int] = field(
            default=None,
            metadata={
                "name": "Order",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 8,
            }
        )
        type_value: Optional[CriteriaType] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class TaxDetails:
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class TypeAdaptedRoomGuestAllocation:
    """The allocation of guests per room assigned by the aggregator or supplier
    (hotel property).

    Returned only when the requested guest allocation is different from
    the provider or supplier’s adapted guest allocation.

    :ivar child: Information about a child guest.
    :ivar number_of_adults: The number of adult guests per room. Maximum
        number of adults may vary by supplier or aggregator.
    """
    class Meta:
        name = "typeAdaptedRoomGuestAllocation"

    child: List[TypeGuestChildInformation] = field(
        default_factory=list,
        metadata={
            "name": "Child",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 6,
        }
    )
    number_of_adults: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        }
    )


@dataclass
class TypeGuestRoomInformation:
    """
    Information about guest to book.

    :ivar adults: The number of adult guests per room. Maximum number of
        adults may vary by supplier or aggregator.
    :ivar booking_traveler_ref: Reference for the Booking Traveler. Used
        for Hotel Booking only. The value is arbitrary.
    :ivar child: Information about a child guest.
    """
    class Meta:
        name = "typeGuestRoomInformation"

    adults: Optional[int] = field(
        default=None,
        metadata={
            "name": "Adults",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "required": True,
        }
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
        }
    )
    child: List["TypeGuestRoomInformation.Child"] = field(
        default_factory=list,
        metadata={
            "name": "Child",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 6,
        }
    )

    @dataclass
    class Child(TypeGuestChildInformation):
        """
        :ivar booking_traveler_ref: Reference for the Booking Traveler.
            Used for Hotel Booking only. The value is arbitrary.
        """
        booking_traveler_ref: Optional[BookingTravelerRef] = field(
            default=None,
            metadata={
                "name": "BookingTravelerRef",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            }
        )


@dataclass
class BookingGuestInformation:
    """
    Information about requested rooms and guests allocation.

    :ivar room: Individual room. Multiple occurrences if there are
        multiple rooms in the request. Maximum number of rooms may vary
        by supplier or aggregator.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    room: List[TypeGuestRoomInformation] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )


@dataclass
class HotelProperty:
    """
    The hotel property.

    :ivar property_address:
    :ivar phone_number:
    :ivar coordinate_location:
    :ivar distance:
    :ivar hotel_rating:
    :ivar amenities:
    :ivar marketing_message:
    :ivar hotel_chain:
    :ivar hotel_code:
    :ivar hotel_location: The location code for this entity. IATA code.
    :ivar name:
    :ivar vendor_location_key: The VendorLocationKey for this
        HotelProperty.
    :ivar hotel_transportation: OTA Transporation code. Transportation
        available to hotel.
    :ivar reserve_requirement:
    :ivar participation_level: 2=Best Available Rate 1G, 1V,  4=Lowest
        Possible Rate 1G, 1V, 1P
    :ivar availability:
    :ivar key:
    :ivar preferred_option: This attribute is used to indicate if the
        vendors responsible for the fare or rate being returned have
        been determined to be ‘preferred’ based on the associated policy
        settings.
    :ivar more_rates: When true, more rates are available for this hotel
        property.Applicable only for HotelDetails and HotelSuperShopper.
        Supported Providers: 1G, 1V.
    :ivar more_rates_token: HS3 Token to identify the Rates for a
        property. Supported Providers 1G,1V.
    :ivar net_trans_commission_ind: This attribute indicates whether
        hotel property is tracking through net trans commission
        indicator.
    :ivar num_of_rate_plans: The specific number of RatePlanTypes for
        each property responded on the message, integer 1 - 999.
        Supported provider: HotelSuperShopper message only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    property_address: Optional[TypeUnstructuredAddress] = field(
        default=None,
        metadata={
            "name": "PropertyAddress",
            "type": "Element",
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
    coordinate_location: Optional[CoordinateLocation] = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    hotel_rating: List[HotelRating] = field(
        default_factory=list,
        metadata={
            "name": "HotelRating",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    amenities: Optional[Amenities] = field(
        default=None,
        metadata={
            "name": "Amenities",
            "type": "Element",
        }
    )
    marketing_message: Optional[MarketingMessage] = field(
        default=None,
        metadata={
            "name": "MarketingMessage",
            "type": "Element",
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
            "required": True,
            "max_length": 32,
        }
    )
    hotel_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Attribute",
            "min_length": 3,
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
    vendor_location_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "VendorLocationKey",
            "type": "Attribute",
        }
    )
    hotel_transportation: Optional[int] = field(
        default=None,
        metadata={
            "name": "HotelTransportation",
            "type": "Attribute",
        }
    )
    reserve_requirement: Optional[TypeReserveRequirement] = field(
        default=None,
        metadata={
            "name": "ReserveRequirement",
            "type": "Attribute",
        }
    )
    participation_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipationLevel",
            "type": "Attribute",
            "length": 1,
        }
    )
    availability: Optional[TypeHotelAvailability] = field(
        default=None,
        metadata={
            "name": "Availability",
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
    preferred_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )
    more_rates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreRates",
            "type": "Attribute",
        }
    )
    more_rates_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoreRatesToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    net_trans_commission_ind: Optional[TypeNetTransCommission] = field(
        default=None,
        metadata={
            "name": "NetTransCommissionInd",
            "type": "Attribute",
        }
    )
    num_of_rate_plans: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOfRatePlans",
            "type": "Attribute",
        }
    )


@dataclass
class HotelRateDetail:
    """
    Returns hotel rate details during the stay if rates are available for requested
    property.

    :ivar policy_codes_list: A list of codes that indicate why an item
        was determined to be ‘out of policy’.
    :ivar room_rate_description:
    :ivar hotel_rate_by_date:
    :ivar corporate_discount_id: Corporate Discount IDs and Negotiate
        rate codes associated with this rate
    :ivar accepted_payment: Form of payment accepted by the hotel
        supplier (chain or property). For credit cards, the two-
        character code for the credit card type is used.
    :ivar commission: Commission associated with the Rate Plan, as a
        percentage or flat amount.
    :ivar rate_match_indicator: Returns "Match" Indicators for certain
        request parameters for Hotel Rate returned in response.
    :ivar tax_details:
    :ivar cancel_info:
    :ivar guarantee_info: Guarantee, deposit, and prepayment information
    :ivar supplemental_rate_info: Supplemental rate information provided
        by the aggregator.
    :ivar room_capacity: The maximum number of guests for a room or for
        each room in a package.
    :ivar extra_charges: Additional charges applied to the hotel rate.
    :ivar inclusions: Additional items included in the hotel rate plan.
    :ivar rate_plan_type:
    :ivar base: This attribute is used to describe the Hotel Supplier
        Base Rate
    :ivar tax: This attribute used to describe Tax associated with the
        room
    :ivar total: This attribute used to describe Hotel Supplier Total
        Rate
    :ivar surcharge: This attribute used to describe Surcharge
        associated with the room
    :ivar approximate_base: Hotel base rate expressed in another
        currency
    :ivar approximate_tax: Taxes expressed in another currency
    :ivar approximate_total: Hotel total rate expressed in another
        currency.
    :ivar approximate_surcharge: Surcharge associated with the room
        expressed in another currency.
    :ivar rate_guaranteed:
    :ivar approximate_rate_guaranteed: If true, approximate rate is
        guaranteed by vendor.  Supported Providers: 1G,1V
    :ivar rate_category: An enumerated type that allows the query to
        specify a rate category type, and provides major categories for
        comparison across brands. Refer to OpenTravel Code List Rate
        Plan Type (RPT). Encode/decode data in Util
        ReferenceDataRetrieveReq TypeCode=“HotelRateCategory".
    :ivar key:
    :ivar rate_supplier: Indicates the source of the rate.
    :ivar bookable_quantity: The number of rooms which can be booked on
        the rate returned in HotelRateDetails.  When the aggregator
        responds ‘IsPackage’= true (pricing for all rooms together), the
        BookableQuantity value will be ‘1’.
    :ivar rate_offer_id: Offer Identifier. Maybe required for hotels
        provided by aggregators.
    :ivar in_policy: This attribute will be used to indicate if a fare
        or rate has been determined to be ‘in policy’ based on the
        associated policy settings.
    :ivar rate_change_indicator: Determines if the rate changes during
        the length of stay. Enumerated values are true, false, and
        unknown.
    :ivar extra_fees_included: When true, total amounts includes
        additional fees or charges." Enumerated values are true, false,
        and unknown
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    policy_codes_list: Optional[TypePolicyCodesList] = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        }
    )
    room_rate_description: List[TypeHotelRateDescription] = field(
        default_factory=list,
        metadata={
            "name": "RoomRateDescription",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rate_by_date: List[HotelRateByDate] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateByDate",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    corporate_discount_id: List[CorporateDiscountId] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    accepted_payment: List[AcceptedPayment] = field(
        default_factory=list,
        metadata={
            "name": "AcceptedPayment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    commission: Optional[Commission] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        }
    )
    rate_match_indicator: List[RateMatchIndicator] = field(
        default_factory=list,
        metadata={
            "name": "RateMatchIndicator",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_details: Optional[TaxDetails] = field(
        default=None,
        metadata={
            "name": "TaxDetails",
            "type": "Element",
        }
    )
    cancel_info: Optional[CancelInfo] = field(
        default=None,
        metadata={
            "name": "CancelInfo",
            "type": "Element",
        }
    )
    guarantee_info: Optional[GuaranteeInfo] = field(
        default=None,
        metadata={
            "name": "GuaranteeInfo",
            "type": "Element",
        }
    )
    supplemental_rate_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplementalRateInfo",
            "type": "Element",
        }
    )
    room_capacity: Optional["HotelRateDetail.RoomCapacity"] = field(
        default=None,
        metadata={
            "name": "RoomCapacity",
            "type": "Element",
        }
    )
    extra_charges: Optional["HotelRateDetail.ExtraCharges"] = field(
        default=None,
        metadata={
            "name": "ExtraCharges",
            "type": "Element",
        }
    )
    inclusions: Optional["HotelRateDetail.Inclusions"] = field(
        default=None,
        metadata={
            "name": "Inclusions",
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
        }
    )
    tax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Attribute",
        }
    )
    total: Optional[str] = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
        }
    )
    surcharge: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surcharge",
            "type": "Attribute",
        }
    )
    approximate_base: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateBase",
            "type": "Attribute",
        }
    )
    approximate_tax: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateTax",
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
    approximate_surcharge: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApproximateSurcharge",
            "type": "Attribute",
        }
    )
    rate_guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RateGuaranteed",
            "type": "Attribute",
        }
    )
    approximate_rate_guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApproximateRateGuaranteed",
            "type": "Attribute",
        }
    )
    rate_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "RateCategory",
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
    rate_supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateSupplier",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    bookable_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "BookableQuantity",
            "type": "Attribute",
        }
    )
    rate_offer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateOfferId",
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
    rate_change_indicator: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "RateChangeIndicator",
            "type": "Attribute",
        }
    )
    extra_fees_included: Optional[TypeTrinary] = field(
        default=None,
        metadata={
            "name": "ExtraFeesIncluded",
            "type": "Attribute",
        }
    )

    @dataclass
    class RoomCapacity:
        """
        :ivar capacity: The maximum number of guests per room.
        :ivar is_package: If true, the rooms are offered as a package by
            the aggregator.
        """
        capacity: List[int] = field(
            default_factory=list,
            metadata={
                "name": "Capacity",
                "type": "Element",
                "max_occurs": 99,
            }
        )
        is_package: Optional[bool] = field(
            default=None,
            metadata={
                "name": "IsPackage",
                "type": "Attribute",
            }
        )

    @dataclass
    class ExtraCharges:
        """
        :ivar extra_adult_amount: Additional charge for an extra guest.
        :ivar extra_child_amount: dditional charge for an extra child
            guest.
        :ivar crib_amount: Additional charge for a crib.
        :ivar adult_rollaway_charge: Additional charge for an extra
            rollaway bed provided for an adult guest.
        :ivar child_rollaway_charge: Additional charge for an extra
            rollaway bed provided for a child guest.
        """
        extra_adult_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "ExtraAdultAmount",
                "type": "Attribute",
            }
        )
        extra_child_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "ExtraChildAmount",
                "type": "Attribute",
            }
        )
        crib_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "CribAmount",
                "type": "Attribute",
            }
        )
        adult_rollaway_charge: Optional[str] = field(
            default=None,
            metadata={
                "name": "AdultRollawayCharge",
                "type": "Attribute",
            }
        )
        child_rollaway_charge: Optional[str] = field(
            default=None,
            metadata={
                "name": "ChildRollawayCharge",
                "type": "Attribute",
            }
        )

    @dataclass
    class Inclusions:
        """
        :ivar bed_types: Bed types in the rate plan.
        :ivar meal_plans: Meal options available for the rate plan.
        :ivar room_view: The view from the hotel room.
        :ivar smoking_room_indicator: Indicates if the room is
            designated as nonsmoking or smoking. true = Smoking false =
            NonSmoking unknown = Information is not returned by the
            hotel supplier (chain or property).
        """
        bed_types: List["HotelRateDetail.Inclusions.BedTypes"] = field(
            default_factory=list,
            metadata={
                "name": "BedTypes",
                "type": "Element",
                "max_occurs": 99,
            }
        )
        meal_plans: Optional["HotelRateDetail.Inclusions.MealPlans"] = field(
            default=None,
            metadata={
                "name": "MealPlans",
                "type": "Element",
            }
        )
        room_view: Optional[RoomView] = field(
            default=None,
            metadata={
                "name": "RoomView",
                "type": "Element",
            }
        )
        smoking_room_indicator: Optional[TypeTrinary] = field(
            default=None,
            metadata={
                "name": "SmokingRoomIndicator",
                "type": "Attribute",
            }
        )

        @dataclass
        class BedTypes:
            """
            :ivar code: Bed Type Code. Uses Open Travel Code List Room
                Amenity Type (RMA). Encode/decode data in Util
                ReferenceDataRetrieveReq TypeCode=“HotelAmenities”.
            :ivar quantity: Bed Quantity.
            """
            code: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Code",
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
        class MealPlans:
            """
            :ivar meal_plan: Meal plan.
            :ivar breakfast: Indicates whether a daily breakfast is
                included in the meal plan. true = Breakfast is included
                false = Breakfast is not included unknown = Information
                is not returned by the hotel supplier (chain or
                property).
            :ivar lunch: Indicates whether a daily lunch is included in
                the meal plan. true = Lunch is included false = Lunch is
                not included unknown = Information is not returned by
                the hotel supplier (chain or property).
            :ivar dinner: Indicates whether a daily dinner is included
                in the meal plan. true = Dinner is included false =
                Dinner is not included unknown = Information is not
                returned by the hotel supplier (chain or property).
            """
            meal_plan: List["HotelRateDetail.Inclusions.MealPlans.MealPlan"] = field(
                default_factory=list,
                metadata={
                    "name": "MealPlan",
                    "type": "Element",
                    "max_occurs": 99,
                }
            )
            breakfast: Optional[TypeTrinary] = field(
                default=None,
                metadata={
                    "name": "Breakfast",
                    "type": "Attribute",
                }
            )
            lunch: Optional[TypeTrinary] = field(
                default=None,
                metadata={
                    "name": "Lunch",
                    "type": "Attribute",
                }
            )
            dinner: Optional[TypeTrinary] = field(
                default=None,
                metadata={
                    "name": "Dinner",
                    "type": "Attribute",
                }
            )

            @dataclass
            class MealPlan:
                """
                :ivar code: Meal plan code. Uses Open Travel Code List
                    Meal Plan Type (MPT). Encode/decode data in Util
                    ReferenceDataRetrieveReq TypeCode=“HotelMealPlans”.
                """
                code: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                    }
                )


@dataclass
class HotelSearchLocation:
    """
    Location information for the hotel.

    :ivar hotel_location: Date and Location information for the Hotel.
    :ivar vendor_location:
    :ivar hotel_address: Search by address or postal code.  Applicable
        for 1G, 1V, 1P
    :ivar reference_point: Search for hotels near a reference point.
        HotelLocation/Location is mandatory for aggregated scenario if
        ReferencePoint is used. Applicable for 1G,1V,1P.  Country/State
        are only applicable for 1P
    :ivar coordinate_location: Search using latitude and longitude.
        Applicable for 1G, 1V only. Not applicable for HotelSuperShopper
    :ivar distance:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_location: Optional[HotelLocation] = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Element",
        }
    )
    vendor_location: List[VendorLocation] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    hotel_address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "HotelAddress",
            "type": "Element",
        }
    )
    reference_point: Optional[TypeHotelReferencePoint] = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
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
    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )


@dataclass
class HotelAlternateProperties:
    """
    Alternate Properties returned by some Vendors if the requested property is not
    available.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_property: List[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class HotelDetailsModifiers:
    """
    Controls and switches for the Hotel Details request.

    :ivar permitted_providers:
    :ivar loyalty_card:
    :ivar corporate_discount_id: Search with corporate discount IDs or
        negotiated rate codes. 1G/1V allows a max of 4.  1P allows a max
        of 1 corporate discount ID and up to 30 negotiated rate codes.
        Support for this function is hotel supplier dependent.
    :ivar hotel_stay:
    :ivar number_of_children:
    :ivar hotel_bedding:
    :ivar rate_category: Specify Rate Category
    :ivar booking_guest_information: Information about requested rooms
        and allocation of guests per room.
    :ivar number_of_adults: The total number of adult guests per
        booking. Defaults to ‘1’. GDS Providers: 1G, 1V, 1P.
    :ivar rate_rule_detail: 'None' returns hotel property descriptive
        information-supported for 1p,1g/1v. 'Complete' returns the
        complete hotel and room rate information-supported for 1p,1g/1v,
        'RatePlansOnly' returns hotel rate information only - supported
        for 1p, 1g/1v.
    :ivar number_of_rooms: The number of rooms per booking. Defaults to
        ‘1’. GDS Providers 1G, 1V, 1P.
    :ivar key:
    :ivar preferred_currency: Alternate currency
    :ivar total_occupants: Number of guests for the room.  Supported
        Providers: 1P
    :ivar process_all_nego_rates_ind: When false, we will process the
        request with all the provided negotiated rates in a single
        request. The request will fail when the number of negotiated
        rates have exceeded for that hotel chain. When true, this allows
        to process a request for all provided negotiated rates that may
        exceed the hotel chain limit. Supported for 1P only.
    :ivar max_wait: Maximum wait time in milliseconds for hotel detail
        results.
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
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 4,
        }
    )
    corporate_discount_id: List[CorporateDiscountId] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    number_of_children: Optional[NumberOfChildren] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    rate_category: List[int] = field(
        default_factory=list,
        metadata={
            "name": "RateCategory",
            "type": "Element",
            "max_occurs": 8,
        }
    )
    booking_guest_information: Optional[BookingGuestInformation] = field(
        default=None,
        metadata={
            "name": "BookingGuestInformation",
            "type": "Element",
        }
    )
    number_of_adults: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        }
    )
    rate_rule_detail: TypeRateRuleDetail = field(
        default=TypeRateRuleDetail.NONE,
        metadata={
            "name": "RateRuleDetail",
            "type": "Attribute",
        }
    )
    number_of_rooms: int = field(
        default=1,
        metadata={
            "name": "NumberOfRooms",
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
    preferred_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferredCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    total_occupants: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalOccupants",
            "type": "Attribute",
        }
    )
    process_all_nego_rates_ind: bool = field(
        default=False,
        metadata={
            "name": "ProcessAllNegoRatesInd",
            "type": "Attribute",
        }
    )
    max_wait: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxWait",
            "type": "Attribute",
        }
    )


@dataclass
class HotelPropertyWithMediaItems:
    """
    :ivar hotel_property:
    :ivar media_item: Photos and other media urls for the item
        referenced above.
    :ivar media_result_message: Errors, Warnings and informational
        messages for the property referenced above.
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


@dataclass
class HotelReservation(BaseReservation):
    """
    The complete Hotel Reservation.

    :ivar booking_traveler_ref:
    :ivar reservation_name:
    :ivar third_party_information:
    :ivar email:
    :ivar phone_number:
    :ivar hotel_property:
    :ivar hotel_rate_detail:
    :ivar hotel_stay:
    :ivar hotel_special_request:
    :ivar guarantee:
    :ivar promotion_code: Specifies promotional code used in hotel
        booking
    :ivar booking_source: Specify alternate booking source
    :ivar hotel_bedding:
    :ivar guest_information:
    :ivar associated_remark:
    :ivar sell_message:
    :ivar hotel_commission: HotelCommission text indicates commision
        while hotel reservation. Provider supported 1P.
    :ivar cancel_info:
    :ivar total_reservation_price: The total price for the entire stay,
        including fees, for all rooms in the booking.
    :ivar hotel_detail_item:
    :ivar adapted_room_guest_allocation: This element defines how the
        aggregators or hotel property have allocated the guests to the
        rooms. Only displayed when Requested guest allocation is
        different from the Adapted room guest allocation.
    :ivar status: Reservation IATA status code, 2 byte.
    :ivar booking_confirmation:
    :ivar cancel_confirmation:
    :ivar provider_reservation_info_ref: Provider reservation reference
        key.
    :ivar travel_order: To identify the appropriate sequence for
        Air/Car/Hotel segments based on travel dates.
    :ivar provider_segment_order: To identify the appropriate travel
        sequence for Air/Car/Hotel/Rail segments/reservations in the
        provider reservation.
    :ivar passive_provider_reservation_info_ref: Passive Provider
        reservation reference key.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

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
    third_party_information: Optional[ThirdPartyInformation] = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
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
    hotel_property: Optional[HotelProperty] = field(
        default=None,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "required": True,
        }
    )
    hotel_rate_detail: List[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
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
    hotel_special_request: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelSpecialRequest",
            "type": "Element",
            "max_length": 250,
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
    promotion_code: Optional[PromotionCode] = field(
        default=None,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
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
            "max_occurs": 4,
        }
    )
    guest_information: Optional[GuestInformation] = field(
        default=None,
        metadata={
            "name": "GuestInformation",
            "type": "Element",
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
    sell_message: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SellMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_commission: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelCommission",
            "type": "Element",
        }
    )
    cancel_info: Optional[CancelInfo] = field(
        default=None,
        metadata={
            "name": "CancelInfo",
            "type": "Element",
        }
    )
    total_reservation_price: Optional["HotelReservation.TotalReservationPrice"] = field(
        default=None,
        metadata={
            "name": "TotalReservationPrice",
            "type": "Element",
        }
    )
    hotel_detail_item: List[HotelDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailItem",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    adapted_room_guest_allocation: Optional["HotelReservation.AdaptedRoomGuestAllocation"] = field(
        default=None,
        metadata={
            "name": "AdaptedRoomGuestAllocation",
            "type": "Element",
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
    booking_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
            "type": "Attribute",
        }
    )
    cancel_confirmation: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancelConfirmation",
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
    passive_provider_reservation_info_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )

    @dataclass
    class TotalReservationPrice:
        """
        :ivar room_rate_description:
        :ivar total_price: The amount of the total price, including fees
            for all rooms in the booking.
        :ivar approx_total_price: The approximate amount of the total
            hotel price, including fees, in another currency.
        """
        room_rate_description: List[TypeHotelRateDescription] = field(
            default_factory=list,
            metadata={
                "name": "RoomRateDescription",
                "type": "Element",
                "max_occurs": 99,
            }
        )
        total_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalPrice",
                "type": "Attribute",
            }
        )
        approx_total_price: Optional[str] = field(
            default=None,
            metadata={
                "name": "ApproxTotalPrice",
                "type": "Attribute",
            }
        )

    @dataclass
    class AdaptedRoomGuestAllocation:
        """
        :ivar room: Individual room. Multiple occurrences if there are
            multiple rooms in the request. Maximum number of rooms may
            vary by supplier or aggregator.
        """
        room: List[TypeAdaptedRoomGuestAllocation] = field(
            default_factory=list,
            metadata={
                "name": "Room",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 9,
            }
        )


@dataclass
class HotelSearchModifiers:
    """
    Controls and switches for the Hotel Search request.

    :ivar permitted_chains:
    :ivar prohibited_chains:
    :ivar permitted_providers:
    :ivar loyalty_card:
    :ivar hotel_name: There can be at most one Hotel Name to be
        requested
    :ivar corporate_discount_id: Search with corporate discount IDs or
        negotiated rate codes. 1G/1V allows a max of 4.  1P allows a max
        of 1 corporate discount ID and up to 30 negotiated rate codes.
        Support for this function is hotel supplier dependent.
    :ivar rate_category: Search for specific rate categories
    :ivar hotel_rating:
    :ivar search_priority:
    :ivar hotel_bedding:
    :ivar amenities: Amenity information
    :ivar number_of_children:
    :ivar hotel_transportation: OTA Transportation code. Search for
        specific transportation. Supported providers: 1G/1V.  Only
        CourtesyBus '7' supported by 1P.
    :ivar booking_guest_information:
    :ivar number_of_adults: The total number of adult guests per
        booking. Defaults to ‘1’. Supported Providers: 1G, 1V, 1P.
    :ivar number_of_rooms: The number of rooms per booking. Defaults to
        ‘1’. Supported Providers 1G, 1V, 1P.
    :ivar is_relaxed: Default is true. If false, only the results
        matching all the criteria returned.
    :ivar preferred_currency: Requested currency for target rate.
    :ivar available_hotels_only: Set to true to request only available
        hotels.  Default is false and all results from the provider are
        returned.
    :ivar max_wait: Maximum wait time in milliseconds for hotel search
        results.  Supported provider:HotelSuperShopper message.
    :ivar aggregate_results: Indicator to identify GDS property match
        required or not.
    :ivar return_property_description: Request hotel property
        description. Valid Values are "true" or "false". Default
        "false".
    :ivar num_of_rate_plans: The specific number of RatePlanTypes for
        each property responded on the message, integer 1 - 999.
        Supported provider: HotelSuperShopper message only.
    :ivar return_amenities: If hotel amenities are desired set as
        'true', else default 'false' for no amenity support.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    permitted_chains: Optional["HotelSearchModifiers.PermittedChains"] = field(
        default=None,
        metadata={
            "name": "PermittedChains",
            "type": "Element",
        }
    )
    prohibited_chains: Optional["HotelSearchModifiers.ProhibitedChains"] = field(
        default=None,
        metadata={
            "name": "ProhibitedChains",
            "type": "Element",
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
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 4,
        }
    )
    hotel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "HotelName",
            "type": "Element",
        }
    )
    corporate_discount_id: List[CorporateDiscountId] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    rate_category: List[int] = field(
        default_factory=list,
        metadata={
            "name": "RateCategory",
            "type": "Element",
            "max_occurs": 8,
        }
    )
    hotel_rating: List[HotelRating] = field(
        default_factory=list,
        metadata={
            "name": "HotelRating",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_priority: Optional[SearchPriority] = field(
        default=None,
        metadata={
            "name": "SearchPriority",
            "type": "Element",
        }
    )
    hotel_bedding: List[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    amenities: Optional["HotelSearchModifiers.Amenities"] = field(
        default=None,
        metadata={
            "name": "Amenities",
            "type": "Element",
        }
    )
    number_of_children: Optional[NumberOfChildren] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        }
    )
    hotel_transportation: Optional["HotelSearchModifiers.HotelTransportation"] = field(
        default=None,
        metadata={
            "name": "HotelTransportation",
            "type": "Element",
        }
    )
    booking_guest_information: Optional[BookingGuestInformation] = field(
        default=None,
        metadata={
            "name": "BookingGuestInformation",
            "type": "Element",
        }
    )
    number_of_adults: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        }
    )
    number_of_rooms: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfRooms",
            "type": "Attribute",
        }
    )
    is_relaxed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRelaxed",
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
    available_hotels_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvailableHotelsOnly",
            "type": "Attribute",
        }
    )
    max_wait: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxWait",
            "type": "Attribute",
        }
    )
    aggregate_results: bool = field(
        default=False,
        metadata={
            "name": "AggregateResults",
            "type": "Attribute",
        }
    )
    return_property_description: bool = field(
        default=False,
        metadata={
            "name": "ReturnPropertyDescription",
            "type": "Attribute",
        }
    )
    num_of_rate_plans: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOfRatePlans",
            "type": "Attribute",
        }
    )
    return_amenities: bool = field(
        default=False,
        metadata={
            "name": "ReturnAmenities",
            "type": "Attribute",
        }
    )

    @dataclass
    class PermittedChains:
        hotel_chain: List[HotelChain] = field(
            default_factory=list,
            metadata={
                "name": "HotelChain",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedChains:
        hotel_chain: List[HotelChain] = field(
            default_factory=list,
            metadata={
                "name": "HotelChain",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class Amenities:
        amenity: List[Amenity] = field(
            default_factory=list,
            metadata={
                "name": "Amenity",
                "type": "Element",
                "max_occurs": 8,
            }
        )

    @dataclass
    class HotelTransportation:
        """
        :ivar type_value: Transportation type code
        """
        type_value: Optional[int] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class HotelSearchResult:
    """
    A single hotel availabilty result.

    :ivar vendor_location:
    :ivar hotel_property: The hotel property. Multiple property can only
        be supported with GDS property aggrigation.
    :ivar hotel_search_error:
    :ivar corporate_discount_id:
    :ivar rate_info:
    :ivar media_item:
    :ivar hotel_type: Supported Providers:1P
    :ivar property_description: Hotel Property description. Maximum of
        100 words returned.
    """
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
    hotel_property: List[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    hotel_search_error: List["HotelSearchResult.HotelSearchError"] = field(
        default_factory=list,
        metadata={
            "name": "HotelSearchError",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    corporate_discount_id: List[CorporateDiscountId] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    rate_info: List[RateInfo] = field(
        default_factory=list,
        metadata={
            "name": "RateInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    media_item: Optional[MediaItem] = field(
        default=None,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_type: Optional[HotelType] = field(
        default=None,
        metadata={
            "name": "HotelType",
            "type": "Element",
        }
    )
    property_description: Optional[PropertyDescription] = field(
        default=None,
        metadata={
            "name": "PropertyDescription",
            "type": "Element",
        }
    )

    @dataclass
    class HotelSearchError(TypeResultMessage):
        """
        :ivar rate_supplier: Indicates the supplier of the rate.
        """
        rate_supplier: Optional[str] = field(
            default=None,
            metadata={
                "name": "RateSupplier",
                "type": "Attribute",
                "max_length": 64,
            }
        )


@dataclass
class HotelSuperShopperResults:
    """
    :ivar hotel_property:
    :ivar hotel_detail_item:
    :ivar hotel_rate_detail: Returns hotel rate details during the stay
        if rates are available for requested property
    :ivar hotel_results_error:
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
    hotel_detail_item: List[HotelDetailItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailItem",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_rate_detail: List[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_results_error: List[TypeResultMessage] = field(
        default_factory=list,
        metadata={
            "name": "HotelResultsError",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class TypeHotelDetails:
    """
    Hotel Details Type.

    :ivar hotel_property:
    :ivar hotel_detail_item:
    :ivar hotel_rate_detail: Returns hotel rate details during the stay
        if rates are available for requested property
    :ivar media_item:
    """
    class Meta:
        name = "typeHotelDetails"

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
    media_item: List[MediaItem] = field(
        default_factory=list,
        metadata={
            "name": "MediaItem",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )


@dataclass
class RequestedHotelDetails(TypeHotelDetails):
    """
    :ivar hotel_type: Supported Providers:1G/1V/1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_type: Optional[HotelType] = field(
        default=None,
        metadata={
            "name": "HotelType",
            "type": "Element",
        }
    )
