from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod
from generated.common_v37_0.common import (
    AgencyPayment,
    AgentVoucher,
    Certificate,
    Check,
    DirectPayment,
    MiscFormOfPayment,
    PaymentAdvice,
    ProviderReservationInfoRef,
    Requisition,
    UnitedNations,
    TypeCreditCardType,
    TypeErrorInfo,
    TypeGuaranteeInformation,
    TypePaymentCard,
    TypeProfileEntityStatus,
    TypeProfileEntityStatusWithDelete,
    TypeStructuredAddress,
    TypeVoucherInformation,
    TypeVoucherType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ActionSummary:
    """
    Action Summary.

    :ivar id: Action Unique ID.
    :ivar name: Action Name.
    :ivar description: Action Description.
    :ivar consuming_system: Action Consuming System (Universal Desktop,
        3rd party system).
    :ivar target_service: Action Target Service (Web Service name or
        page name that the data will be utilized).
    :ivar profile_action_code: Profile Action Code description.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    consuming_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumingSystem",
            "type": "Attribute",
            "required": True,
        }
    )
    target_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetService",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_action_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileActionCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AddressLine:
    """
    Specifies a single line within an address.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )


class AgencyInfoUrsyncData(Enum):
    MASKED = "Masked"
    UNMASKED = "Unmasked"


@dataclass
class AgentVoucherHistory:
    """
    Agent Voucher Form of Payments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )


@dataclass
class BridgeBranch:
    """
    Summary information for the Bridge Branch.

    :ivar profile_id: The Bridge Branch Profile ID
    :ivar branch_code: The Bridge Branch Provisioning Code
    :ivar name: The Bridge Branch Name
    :ivar default: Indicates that this branch is the default branch. The
        default is false.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    default: bool = field(
        default=False,
        metadata={
            "name": "Default",
            "type": "Attribute",
        }
    )


@dataclass
class CertificateHistory:
    """
    Certificate Form of Payment.

    :ivar number: The Certificate number
    :ivar amount: The monetary value of the certificate.
    :ivar discount_amount: The monetary discount amount of this
        certificate.
    :ivar discount_percentage: The percentage discount value of this
        certificate.
    :ivar not_valid_before: The date that this certificate becomes
        valid.
    :ivar not_valid_after: The date that this certificate expires.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
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
    discount_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Attribute",
        }
    )
    discount_percentage: Optional[int] = field(
        default=None,
        metadata={
            "name": "DiscountPercentage",
            "type": "Attribute",
        }
    )
    not_valid_before: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )


@dataclass
class FieldDataSearch:
    """
    Specifies a search term and value (wildcards permitted), to search profiles by
    data in custom profile fields.

    :ivar field_id: The reference to the custom field that this
        FieldData refers.Provide either FieldID or Name, not both.
    :ivar name: Name of the custom field that this FieldData
        refers.Provide either Name or FieldID, not both.
    :ivar value: The value to search for in the relevant profiles.
        Wildcards permitted. All searches are case-insensitive.
    :ivar field_group_id: Used to limit the search to multiple fields of
        the same field group instance.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        }
    )
    field_group_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
        }
    )


@dataclass
class FixedFieldGroupRef:
    """
    Unique ID of a field group that this field can reference values from (by their
    Key) at the time of creating or modifying profiles.

    :ivar id: The unique ID of the reference-able fixed field group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FixedFieldUpdate:
    """Update the agency-defined attributes for a fixed field.

    To remove a value, omit the attribute entirely.

    :ivar id: Unique identifier of the field.
    :ivar label: Alternate name of the field for display on the UI
    :ivar display_order: The order displayed by an UI
    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    :ivar search_option: If true, then this field is identified as one
        that is allowed to be searched on.  It is user defined.
    :ivar search_option_display_order: The display order for search
        option.
    :ivar min_occurs_override: Minimum Agency-defined override defining
        the minimum number of instances permitted by the agency.
    :ivar max_occurs_override: Maximum Agency-defined override defining
        the maximum number of instances permitted by the agency.
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).  Leave blank to indicate 0.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        }
    )
    search_option_display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        }
    )
    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )


@dataclass
class MiscFormOfPaymentHistory:
    """
    Miscellaneous Form of Payments.

    :ivar credit_card_type: The 2 letter credit/ debit card type or code
        which may not have been issued using the standard bank card
        types  - i.e. an airline issued card
    :ivar credit_card_number:
    :ivar exp_date: The Expiration date of this card in YYYY-MM format.
    :ivar text: Any free form text which may be associated with the
        Miscellaneous Form of Payment. This text may be provider or GDS
        specific
    :ivar category: Indicates what Category the Miscellaneous Form Of
        Payment is being used for payment - The category may vary by
        GDS. Allowable values are "Text" "Credit" "CreditCard"
        "FreeFormCreditCard" "Invoice" "NonRefundable"
        "MultipleReceivables" "Exchange" "Cash"
    :ivar acceptance_override: Override airline restriction on the
        credit card.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    credit_card_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreditCardType",
            "type": "Attribute",
            "length": 2,
        }
    )
    credit_card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreditCardNumber",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        }
    )
    exp_date: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "ExpDate",
            "type": "Attribute",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    acceptance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcceptanceOverride",
            "type": "Attribute",
        }
    )


@dataclass
class ModifyTag:
    """
    :ivar id: The ID of the tag to be modified.
    :ivar name: The name given to the tag.  If not specified, then not
        changed.
    :ivar label: The alternate name given to the tag.  If not specified,
        then not changed.
    :ivar description: The description of the tag.  If not specified,
        then not changed.
    :ivar display_order: The display order of the tag
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
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
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )


@dataclass
class PaymentAddress:
    """
    Payment Details Address.

    :ivar address_line:
    :ivar postal: The postal code of which this address is located.
    :ivar country: The country of which this address is located.
    :ivar state: The state of which this address is located.
    :ivar other_state_province: Alternate freeform state value
    :ivar city: The city of which this address is located.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 128,
        }
    )
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
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
    other_state_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class PaymentPhone:
    """
    Payment Phone Number.

    :ivar country: The phone number's country code
    :ivar area_code: The phone number's area code
    :ivar local_number: The phone number
    :ivar extension: The phone number's extension
    :ivar location: The IATA airport/city code that corresponds to the
        location of the phone number.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    local_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 6,
        }
    )


class PhoneNumberHistoryType(Enum):
    AGENCY = "Agency"
    BUSINESS = "Business"
    MOBILE = "Mobile"
    HOME = "Home"
    FAX = "Fax"
    HOTEL = "Hotel"
    OTHER = "Other"
    NONE = "None"
    EMAIL = "Email"


@dataclass
class ProfileSearchModifiers:
    """Specifies the range of search results.

    If omitted, the default values for each attriubute are used.

    :ivar max_results: Limits the number of search results in the
        response. Note that performance may decline when a large number
        of results is requested.
    :ivar start_from_result: The starting search index of the results
        returned. Used to browse beyond the initial search results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
class ProfileTemplateSummary:
    """
    Brief summary containing a template's name and ID.

    :ivar id: The ID of the template
    :ivar name: The name of the template
    :ivar version: Current version number of the template
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[object] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


class ProprietaryDataProprietaryDataType(Enum):
    NICK_NAME = "NickName"
    DESCRIPTION = "Description"
    ADDITIONAL_IDENTIFIER = "AdditionalIdentifier"
    EXTERNAL_IDENTIFIER = "ExternalIdentifier"


class ProvisioningCodeProfileType(Enum):
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"


@dataclass
class Tag:
    """
    A tag that belongs to the agency.

    :ivar name: The name given to the tag
    :ivar label: The alternate name given to the tag
    :ivar description: The description of the tag
    :ivar display_order: The display order of the tag
    :ivar id: The unique identifier of the tag.
    :ivar agency_id: The agency that owns the tag
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
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
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    agency_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TagRef:
    """
    Reference to Tag by its ID.

    :ivar id: The Tag ID.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TemplateInfoUpdate:
    """
    Alllow the editing of certain data of the template.

    :ivar name: Name of the template.
    :ivar description: Description of the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[object] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )


@dataclass
class TicketNumberHistory:
    """
    The identifying number for the actual ticket.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 13,
        }
    )


class TravelDocumentHeightUnit(Enum):
    METERS = "Meters"
    FEET = "Feet"


class TravelDocumentWeightUnit(Enum):
    KILOGRAMS = "Kilograms"
    POUNDS = "Pounds"


class UniqueProfileIdProfileType(Enum):
    TRAVELER = "Traveler"


@dataclass
class UnitedNationsHistory:
    """
    United Nations Form of Payments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )


class TypeAction(Enum):
    """
    Specify whether the change is to add, update, or delete the field.
    """
    ADD = "Add"
    UPDATE = "Update"
    DELETE = "Delete"


@dataclass
class TypeActionRef:
    """
    Reference to an Action by ID.

    :ivar id: Action Unique ID.
    """
    class Meta:
        name = "typeActionRef"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeActionReference:
    """
    Reference to an Action by ID.

    :ivar id: Action Unique ID.
    :ivar profile_action_code: Profile Action Code.
    """
    class Meta:
        name = "typeActionReference"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_action_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileActionCode",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeAdvisoryType(Enum):
    """
    Specify the type of Advisory.
    """
    AGENCY = "Agency"
    AIR = "Air"
    CUSTOMER = "Customer"
    DATES = "Dates"
    HOTELS = "Hotels"
    MARKET_RELATED = "Market Related"
    PASSPORT = "Passport"
    PROMOTIONS = "Promotions"
    SEASONAL = "Seasonal"
    SPECIALS = "Specials"
    SUPPLIER = "Supplier"
    TRAVEL = "Travel"
    VEHICLE = "Vehicle"
    VISA = "Visa"


class TypeAgencyInfoHistoryUrsyncData(Enum):
    MASKED = "Masked"
    UNMASKED = "Unmasked"


@dataclass
class TypeAgencyPaymentHistory:
    """
    Type for Agency Payment.

    :ivar agency_billing_identifier: Value of the billing id
    :ivar agency_billing_number: Value of billing number
    :ivar agency_billing_password: Value of billing password
    """
    class Meta:
        name = "typeAgencyPaymentHistory"

    agency_billing_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyBillingIdentifier",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    agency_billing_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyBillingNumber",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    agency_billing_password: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyBillingPassword",
            "type": "Attribute",
            "max_length": 128,
        }
    )


class TypeAirFare(Enum):
    """
    The type of Air Fare.
    """
    ADVANCE_PURCHASE_FARES = "Advance Purchase Fares"
    NON_REFUNDABLE_FARES = "Non-Refundable Fares"
    PENALTY_FARES = "Penalty Fares"
    PRIVATE_FARES_ONLY = "Private Fares Only"
    RESTRICTED_FARES = "Restricted Fares"


@dataclass
class TypeBridgeBranchCmd:
    """
    Base type for both BridgeBranchAdd and BridgeBranchDelete.

    :ivar branch_id: The Branch Profile ID
    :ivar branch_code: The Branch Provisioning Code
    """
    class Meta:
        name = "typeBridgeBranchCmd"

    branch_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "BranchID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_length": 1,
            "max_length": 25,
        }
    )


class TypeCommissionCategory(Enum):
    """A type that represents a category of commissions.

    Example include per booking, by monetary amount, etc.
    """
    PER_BOOKING = "Per Booking"
    PER_PERSON = "Per Person"
    PER_TICKET = "Per Ticket"


class TypeContactPurpose(Enum):
    """A code for categorizing a contact mechanism based on purpose or use.

    Examples include business, persona., etc.
    """
    ALL = "All"
    BUSINESS = "Business"
    PERSONAL = "Personal"


class TypeContactType(Enum):
    """A code for categorizing contactees based on a role they might play.

    Examples include Emergency Contact, Regular Contact, Backup Contact,
    etc.
    """
    ADMIN_ASSISTANT = "Admin Assistant"
    AFTER_HOUR = "After Hour"
    ASSISTANT = "Assistant"
    BACKUP = "Backup"
    CHILD = "Child"
    COLLEAGUE = "Colleague"
    EMERGENCY = "Emergency"
    MANAGER = "Manager"
    OTHER = "Other"
    PARENT = "Parent"
    REGULAR = "Regular"
    RELATIVE = "Relative"
    SERVICE_CENTER = "Service Center"
    SPOUSE = "Spouse"
    SUPERVISOR = "Supervisor"
    TICKET_AUTHORIZER = "Ticket Authorizer"
    TRAVEL_ARRANGER = "Travel Arranger"
    TRIP_AUTHORIZATION = "Trip Authorization"


class TypeCreateHierarchyLevel(Enum):
    """
    Profile types that are used in creating a hiearchy.
    """
    BRANCH_GROUP = "BranchGroup"
    TRAVELER_GROUP = "TravelerGroup"


@dataclass
class TypeCustomFieldAndGroupDeleteRef:
    """
    A reference to an endpoint.

    :ivar id: Unique identifier of the Custom Field or Group.
    """
    class Meta:
        name = "typeCustomFieldAndGroupDeleteRef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeCustomFieldDataFormat(Enum):
    """
    Data Type of the field.
    """
    ALPHA_NUMERIC = "Alpha Numeric"
    FREEFORM_TEXT = "Freeform Text"
    TEXT = "Text"
    DECIMAL = "Decimal"
    WHOLE_NUMBER = "Whole Number"
    PERCENTAGE = "Percentage"
    TRUE_FALSE = "True/False"
    EMAIL_ADDRESS = "Email Address"
    URL = "URL"
    DATE_YEAR = "Date Year"
    DATE_MONTH_YEAR = "Date Month Year"
    DATE_DAY_MONTH_YEAR = "Date Day Month Year"
    DATE_DAY_MONTH_YEAR_TIME = "Date Day Month Year Time"
    TIME_IN_MINUTES = "Time in Minutes"
    TIME_IN_HOUR_MINUTE = "Time in Hour &amp; Minute"
    TIME_IN_MILLISECONDS_WITH_TIME_ZONE = "Time in Milliseconds with Time Zone"


class TypeCustomFieldOrGroupType(Enum):
    """This is an optional field.

    If the element is not passed then the  TemplateFieldID value passed
    will be considered a Fixed Field or a Fixed Field Group..
    """
    CUSTOM_FIELD = "CustomField"
    CUSTOM_FIELD_GROUP = "CustomFieldGroup"


@dataclass
class TypeDateOptions:
    """Specify a date using different combinations of Day/Month/Year.

    All are optional attributes, although at least one is required.
    """
    class Meta:
        name = "typeDateOptions"

    day: Optional[str] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    month: Optional[str] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    year: Optional[str] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        }
    )


class TypeDeleteHierarchyLvlProfileType(Enum):
    """
    A type for unique party identifiers of any party role.
    """
    BRANCH_GROUP = "BranchGroup"
    TRAVELER_GROUP = "TravelerGroup"


class TypeEmailFormat(Enum):
    """Specifies the email format.

    (ie. HTML, Text, PDF, etc.)
    """
    HTML = "HTML"
    PDF = "PDF"
    PLAIN_TEXT = "Plain Text"


class TypeEndpointDataType(Enum):
    """
    Specify the Data type for an Endpoint (ex, Boolean, Integer, String, etc)
    """
    STRING = "String"
    FLOAT = "Float"
    DATE = "Date"
    DATE_TIME = "DateTime"
    MONEY = "Money"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"


@dataclass
class TypeEndpointRef:
    """
    A reference to an endpoint.

    :ivar id: Reference to an Endpoint
    """
    class Meta:
        name = "typeEndpointRef"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TypeFieldRef:
    """
    Base type of a reference to a field or field group.

    :ivar id: Unique identifier of the field
    """
    class Meta:
        name = "typeFieldRef"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )


class TypeFilterControlAndWorkspace(Enum):
    """
    Allow the filtering of Workspace and Control or specify no filtering at all.
    """
    WORKSPACE_ONLY = "WorkspaceOnly"
    CONTROL_ONLY = "ControlOnly"
    ALL = "All"


class TypeFixedFieldDataFormat(Enum):
    """
    Data Type of the field.
    """
    STRING = "String"
    FLOAT = "Float"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
    DATE = "Date"
    MONEY = "Money"
    PERCENT = "Percent"
    REFERENCE = "Reference"


@dataclass
class TypeFloatRestriction:
    """
    A fully structured address.

    :ivar min_value: The minimum value permitted. Leave blank to specify
        no minimum (which allows negative numbers), or specify an
        explicit posiitve or negative number.
    :ivar max_value: The maximum value permitted.
    """
    class Meta:
        name = "typeFloatRestriction"

    min_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Attribute",
            "max_inclusive": 9999999.0,
        }
    )
    max_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Attribute",
            "max_inclusive": 9999999.0,
        }
    )


class TypeGeneralRemarkType(Enum):
    """
    A code for categorizing a remark within the GDS.
    """
    ALPHA = "Alpha"
    BASIC = "Basic"
    HISTORICAL = "Historical"
    INVOICE = "Invoice"
    ITINERARY = "Itinerary"
    VENDOR = "Vendor"


class TypeGeoPoliticalAreaFilterType(Enum):
    """
    :cvar ARRIVAL: Filter type applied on Air and Rail Preference
    :cvar DEPARTURE: Filter type applied on Air,Hotel,Rail and Vehicle
        Preference
    :cvar CONNECTION: Filter type applied on Air and Rail Preference
    :cvar OTHER: Filter type applied on Advisory and Other Preference
    """
    ARRIVAL = "Arrival"
    DEPARTURE = "Departure"
    CONNECTION = "Connection"
    OTHER = "Other"


class TypeGeoPoliticalAreaType(Enum):
    """
    The type of the geographical location.
    """
    WORLD = "World"
    GLOBAL_AREA = "Global Area"
    CONTINENT_GROUP = "Continent Group"
    CONTINENT = "Continent"
    COUNTRY = "Country"
    STATE_PROVINCE = "State/Province"
    CITY = "City"
    AIRPORT = "Airport"


class TypeGuaranteeInformationHistoryAgencyType(Enum):
    AGENCY_IATA = "AgencyIATA"
    OTHER_AGENCY_IATA = "OtherAgencyIATA"


class TypeGuaranteeInformationHistoryType(Enum):
    GUARANTEE = "Guarantee"
    DEPOSIT = "Deposit"


class TypeHierarchyOverrideType(Enum):
    """
    Profile types that are used in default and override profiles on a hierarchy.
    """
    ACCOUNT = "Account"
    TRAVELER = "Traveler"


@dataclass
class TypeIntegerRestriction:
    """
    A fully structured address.

    :ivar min_value: The minimum value permitted. Leave blank to specify
        no minimum (which allows negative numbers), or specify an
        explicit posiitve or negative number.
    :ivar max_value: The maximum value permitted.
    """
    class Meta:
        name = "typeIntegerRestriction"

    min_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 999999999,
        }
    )
    max_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 999999999,
        }
    )


@dataclass
class TypeKeyElement:
    class Meta:
        name = "typeKeyElement"

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )


class TypeMasked(Enum):
    """Defines whether the field data should be masked in messaging, and the
    masking pattern.

    All masking is simple character substitution (replace each masked
    character with an asterisk).
    """
    NOT_MASKED = "Not Masked"
    MASK_ALL = "Mask All"
    MASK_FIRST_AND_LAST = "Mask First and Last"
    MASK_LAST_TWO = "Mask Last Two"
    SHOW_FIRST_AND_LAST = "Show First and Last"
    SHOW_FIRST_FOUR = "Show First Four"
    SHOW_LAST_FOUR = "Show Last Four"
    SHOW_FIRST_THREE = "Show First Three"
    SHOW_LAST_THREE = "Show Last Three"


class TypeOtherPreference(Enum):
    """Specify the OtherPreference.

    (ie. Cruise, Taxi, etc)
    """
    CRUISE = "Cruise"
    FERRY = "Ferry"
    LIMO = "Limo"
    TAXI = "Taxi"
    TOUR = "Tour"


class TypePaymentType(Enum):
    """Defines the form of payment type.

    (Credit Card, Cash, etc)
    """
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"


class TypePhoneType(Enum):
    """Specifies the phone types.

    (ie. Home, Business, Mobile, etc)
    """
    WORK = "Work"
    HOME = "Home"
    FAX = "Fax"
    MOBILE = "Mobile"
    OTHER = "Other"


class TypePreferencePurpose(Enum):
    """Specify the preference purpose.

    (ie. Business, Leisure, etc)
    """
    BUSINESS = "Business"
    LEISURE = "Leisure"
    MEETING = "Meeting"
    GROUP = "Group"
    INCENTIVE = "Incentive"
    GOVERNMENT = "Government"
    DOMESTIC = "Domestic"
    INTERNATIONAL = "International"
    CONFERENCE = "Conference"
    LOYALTY = "Loyalty"


class TypeProfileComponentType(Enum):
    """Specifies the component names.

    (i.e AccountInfo, AirPreference, TravelDocument etc)
    """
    ACCOUNT_INFO = "AccountInfo"
    TRAVELER_INFO = "TravelerInfo"
    TRAVELER_IDENTITY_INFORMATION = "TravelerIdentityInformation"
    TRAVEL_DOCUMENT = "TravelDocument"
    ACCOUNTING_REFERENCE = "AccountingReference"
    POLICY_REFERENCE = "PolicyReference"
    LOYALTY_PROGRAM_ENROLLMENT = "LoyaltyProgramEnrollment"
    CONTRACT = "Contract"
    COMMISSION = "Commission"
    SERVICE_FEE = "ServiceFee"
    REMARK = "Remark"
    ALTERNATE_CONTACT = "AlternateContact"
    ALTERNATE_CONTACT_ADDRESS = "AlternateContactAddress"
    ALTERNATE_CONTACT_PHONE = "AlternateContactPhone"
    ALTERNATE_CONTACT_ELECTRONIC_ADDRESS = "AlternateContactElectronicAddress"
    COMMISSION_REFERENCE = "CommissionReference"
    ADDRESS = "Address"
    PHONE = "Phone"
    ELECTRONIC_ADDRESS = "ElectronicAddress"
    AIR_PREFERENCE = "AirPreference"
    VEHICLE_PREFERENCE = "VehiclePreference"
    HOTEL_PREFERENCE = "HotelPreference"
    RAIL_PREFERENCE = "RailPreference"
    PROFILE_PARENT_HISTORY = "ProfileParentHistory"
    FIELD_DATA = "FieldData"
    FIELD_GROUP_DATA = "FieldGroupData"
    ADVISORY = "Advisory"
    AGENCY_GROUP_INFO = "AgencyGroupInfo"
    AGENCY_INFO = "AgencyInfo"
    BRANCH_GROUP_INFO = "BranchGroupInfo"
    BRANCH_INFO = "BranchInfo"
    AGENT_INFO = "AgentInfo"
    TRAVELER_GROUP_INFO = "TravelerGroupInfo"
    PROFILE_STATUS = "ProfileStatus"
    PROFILE_LINK = "ProfileLink"
    OTHER_PREFERENCE = "OtherPreference"
    FORM_OF_PAYMENT = "FormOfPayment"
    EXTERNAL_IDENTIFIER = "ExternalIdentifier"


class TypeProfileDataCategory(Enum):
    """
    The category of data that controls what data will be returned in the response.

    :cvar GENERAL_INFORMATION: Basic information
        (AgencyInfo/BranchGroupInfo/etc) and AccountingReference for
        Traveler
    :cvar ALL_DETAILS: All stored profile datac
    :cvar ALTERNATE_CONTACTS: Basic information and all AlternateContact
        data for the retrieved profile including a. Address b. Phone c.
        ElectronicAddress
    :cvar CUSTOM_INFORMATION: All data for all custom fields/field
        groups and basic information
    :cvar COMMISSIONS: Commission data for the retrieved profile and
        basic information
    :cvar CONTRACTS: Contract data for the retrieved profile and basic
        information
    :cvar FORMS_OF_PAYMENT: Payment data for the retrieved profile and
        basic information
    :cvar LOYALTY_PROGRAMS_ALL: All loyalty program enrollment data for
        each SupplierType and basic information
    :cvar LOYALTY_PROGRAMS_AIR: All loyalty program enrollment for the
        Air supplier type (i.e., LoyaltyProgramEnrollment.Supplier
        Type=Air) and basic information
    :cvar LOYALTY_PROGRAMS_VEHICLE: All loyalty program enrollment for
        the Vehicle supplier type (i.e.,
        LoyaltyProgramEnrollment.Supplier Type=Vehicle) and basic
        information
    :cvar LOYALTY_PROGRAMS_HOTEL: All loyalty program enrollment for the
        Hotel supplier type (i.e., LoyaltyProgramEnrollment.Supplier
        Type=Hotel) and basic information
    :cvar LOYALTY_PROGRAMS_RAIL: All loyalty program enrollment for the
        Rail supplier type (i.e., LoyaltyProgramEnrollment.Supplier
        Type=Rail) and basic information
    :cvar LOYALTY_PROGRAMS_OTHER: All loyalty program enrollment for the
        Other supplier type (i.e., LoyaltyProgramEnrollment.Supplier
        Type=Other) and basic information
    :cvar POLICY_REFERENCE:
    :cvar PREFERENCES_ALL: All preference data for each preference type
        (i.e., Air, Vehicle, Hotel, Rail, Other) and basic information
    :cvar PREFERENCES_AIR: All Air Preference data and basic information
    :cvar PREFERENCES_VEHICLE: All Vehicle Preference data and basic
        information
    :cvar PREFERENCES_HOTEL: All Hotel Preference data and basic
        information
    :cvar PREFERENCES_RAIL: All Rail Preference data and basic
        information
    :cvar PREFERENCES_OTHER: All Other Preference data and basic
        information
    :cvar SERVICE_FEES: ServiceFee data for the retrieved profile and
        basic information
    :cvar TRAVEL_DOCUMENTS_ALL: All related data for each Travel
        Document and basic information
    :cvar TRAVEL_DOCUMENTS_PASSPORTS: All related data for Passport
        (i.e., TravelDocument.Type=Passport) and basic information
    :cvar TRAVEL_DOCUMENTS_VISAS: All related data for Visa (i.e.,
        TravelDocument.Type=Visa) and basic information
    :cvar TRAVEL_DOCUMENTS_OTHER: All related data for any travel
        document other than Passport or Visa (i.e., TravelDocument.Type
        not equal to Passport or Visa) and basic information
    :cvar TRAVELER_LINKS: All the links for all the profiles who are
        related to the requested Traveler profile and basic information
    :cvar TRAVELER_IDENTITY_INFORMATION: All data for all traveler
        identity information
    """
    GENERAL_INFORMATION = "General Information"
    ALL_DETAILS = "All Details"
    ALTERNATE_CONTACTS = "Alternate Contacts"
    CUSTOM_INFORMATION = "Custom Information"
    COMMISSIONS = "Commissions"
    CONTRACTS = "Contracts"
    FORMS_OF_PAYMENT = "Forms of Payment"
    LOYALTY_PROGRAMS_ALL = "Loyalty Programs - All"
    LOYALTY_PROGRAMS_AIR = "Loyalty Programs - Air"
    LOYALTY_PROGRAMS_VEHICLE = "Loyalty Programs - Vehicle"
    LOYALTY_PROGRAMS_HOTEL = "Loyalty Programs - Hotel"
    LOYALTY_PROGRAMS_RAIL = "Loyalty Programs - Rail"
    LOYALTY_PROGRAMS_OTHER = "Loyalty Programs - Other"
    POLICY_REFERENCE = "PolicyReference"
    PREFERENCES_ALL = "Preferences - All"
    PREFERENCES_AIR = "Preferences - Air"
    PREFERENCES_VEHICLE = "Preferences - Vehicle"
    PREFERENCES_HOTEL = "Preferences - Hotel"
    PREFERENCES_RAIL = "Preferences - Rail"
    PREFERENCES_OTHER = "Preferences - Other"
    SERVICE_FEES = "Service Fees"
    TRAVEL_DOCUMENTS_ALL = "Travel Documents - All"
    TRAVEL_DOCUMENTS_PASSPORTS = "Travel Documents - Passports"
    TRAVEL_DOCUMENTS_VISAS = "Travel Documents - Visas"
    TRAVEL_DOCUMENTS_OTHER = "Travel Documents - Other"
    TRAVELER_LINKS = "Traveler Links"
    TRAVELER_IDENTITY_INFORMATION = "TravelerIdentityInformation"


class TypeProfileDataElementType(Enum):
    """
    Specify which fixed field type this field refers to.
    """
    TRAVEL_DOCUMENT = "TravelDocument"
    ACCOUNTING_REFERENCE = "AccountingReference"
    POLICY_REFERENCE = "PolicyReference"
    COMMISSION_REFERENCE = "CommissionReference"
    LOYALTY_PROGRAM_ENROLLMENT = "LoyaltyProgramEnrollment"
    COMMISSION = "Commission"
    CONTRACT = "Contract"
    SERVICE_FEE = "ServiceFee"
    REMARK = "Remark"
    FIELD_DATA = "FieldData"
    FIELD_GROUP_DATA = "FieldGroupData"
    ALTERNATE_CONTACT = "AlternateContact"
    AIR_PREFERENCE = "AirPreference"
    HOTEL_PREFERENCE = "HotelPreference"
    VEHICLE_PREFERENCE = "VehiclePreference"
    ADDRESS = "Address"
    PHONE = "Phone"
    ELECTRONIC_ADDRESS = "ElectronicAddress"
    TRAVELER_IDENTITY_INFORMATION = "TravelerIdentityInformation"
    EXTERNAL_IDENTIFIER = "ExternalIdentifier"
    ALTERNATE_CONTACT_ADDRESS = "AlternateContactAddress"
    ALTERNATE_CONTACT_PHONE = "AlternateContactPhone"
    ALTERNATE_CONTACT_ELECTRONIC_ADDRESS = "AlternateContactElectronicAddress"
    ADVISORY = "Advisory"
    RAIL_PREFERENCE = "RailPreference"
    PROVIDER_INFO = "ProviderInfo"
    OTHER_PREFERENCE = "OtherPreference"
    PROPRIETARY_DATA = "ProprietaryData"
    FORM_OF_PAYMENT = "FormOfPayment"


@dataclass
class TypeProfileInfo:
    """
    Base type for Profile Infos.

    :ivar additional_identifier: Additional identifier managed by an
        external system.
    :ivar description:
    """
    class Meta:
        name = "typeProfileInfo"

    additional_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
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


class TypeProfileLinkRelationship(Enum):
    """
    Specify the one way relationship between two profiles.
    """
    COLLEAGUE = "Colleague"
    EMPLOYEE = "Employee"
    ADMIN_ASSISTANT = "Admin Assistant"
    SUPERVISOR = "Supervisor"
    MANAGER = "Manager"
    PROJECT_MANAGER = "Project Manager"
    LEAD = "Lead"
    SPOUSE = "Spouse"
    SIGNIFICANT_OTHER = "Significant Other"
    PARENT = "Parent"
    CHILD = "Child"
    SIBLING = "Sibling"
    RELATIVE = "Relative"
    FRIEND = "Friend"
    INFANT = "Infant"
    TRAVEL_ARRANGER = "Travel Arranger"
    AUTHORIZER = "Authorizer"
    OTHER = "Other"


class TypeProfileType(Enum):
    """
    A type for unique party identifiers of any party role.
    """
    AGENCY_GROUP = "AgencyGroup"
    AGENCY = "Agency"
    BRANCH_GROUP = "BranchGroup"
    BRANCH = "Branch"
    AGENT = "Agent"
    ACCOUNT = "Account"
    TRAVELER_GROUP = "TravelerGroup"
    TRAVELER = "Traveler"


class TypeProprietaryDataHistoryProprietaryDataType(Enum):
    NICK_NAME = "NickName"
    DESCRIPTION = "Description"
    ADDITIONAL_IDENTIFIER = "AdditionalIdentifier"
    EXTERNAL_IDENTIFIER = "ExternalIdentifier"


class TypeRailCoachCompartment(Enum):
    """
    The type of Rail Caoch Compartment.
    """
    SEAT_COUCHETTE = "Seat/Couchette"
    QUIET = "Quiet"
    OFFICE = "Office"
    TABLE = "Table"
    WHEELCHAIR_PLACE = "Wheelchair Place"
    AIR_CONDITIONED = "Air-conditioned"
    LOUNGE = "Lounge"
    RECLINING = "Reclining"


class TypeRailGenderCompartment(Enum):
    """
    The type of Rail Gender Compartment.
    """
    FEMALE = "Female"
    MALE = "Male"
    UNSPECIFIED = "Unspecified"


class TypeRailSeatArrangement(Enum):
    """
    The type of Rail Seat Arrangement.
    """
    POWER_PLUG = "Power Plug"
    SUITABLE_FOR_PETS = "Suitable for Pets"
    WITH_MOBILE_PHONE = "With Mobile Phone"
    SOLO_ISOLATED_SEAT = "Solo Isolated Seat"


class TypeRailSeating(Enum):
    """
    The type of Rail Seating.
    """
    CAR_PARKING = "Car-Parking"
    MOTORRAIL = "Motorrail"
    SEAT_COUCHETTE = "Seat Couchette"
    SLEEPER = "Sleeper"


class TypeRailTicketFulfillmentOption(Enum):
    """
    The type of Rail Ticket Fulfillment Type.
    """
    AGENCY = "Agency"
    COURIER = "Courier"
    KIOSK = "Kiosk"
    MAIL = "Mail"
    TICKETLESS = "Ticketless"
    OTHER = "Other"


class TypeRemarkType(Enum):
    """A code for categorizing a remark.

    This may include General Remarks, Itinerary Remarks, Accounting
    Remark, Name Remark, etc.
    """
    GENERAL = "General"
    ITINERARY = "Itinerary"
    ACCOUNTING = "Accounting"
    NAME = "Name"
    INTERNAL_ONLY = "Internal Only"
    HIGHLY_SENSITIVE = "Highly Sensitive"
    OSI = "OSI"


@dataclass
class TypeSearchAccountingReference:
    """
    The Searchable fields on AccountingReference.

    :ivar type_value: A code for categorizing a reference for a
        Traveler's bookings.  This is often used by the Traveler's
        employer for budgeting, internal billing or other cost
        accounting purposes.  Examples include Budget Codes, Department
        Codes, Project Codes, etc.
    :ivar value: The number or alphanumeric code for an employer
        reference.
    """
    class Meta:
        name = "typeSearchAccountingReference"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
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
class TypeSearchAddress:
    """
    The address of the profile to search for.

    :ivar address_line: Street (must match exactly one of the streets)
    :ivar city: The city of the profile to search for.
    :ivar state_province: The state/province of the profile to search
        for.
    :ivar postal_code: The postal code of the profile to search for.
    :ivar country: The country of the profile to search for.
    """
    class Meta:
        name = "typeSearchAddress"

    address_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressLine",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 50,
        }
    )
    state_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "StateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
            "white_space": "collapse",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 12,
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


@dataclass
class TypeSearchExternalIdentifier:
    """
    This is meant for external identification of a Profile.

    :ivar ext_id: The actual value of the External Id of the Profile.
    :ivar source: The Source code for External ID. This depicts the
        origin/source of the External ID.
    """
    class Meta:
        name = "typeSearchExternalIdentifier"

    ext_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeSearchLoyaltyProgram:
    """
    The Searchable fields on LoyaltyProgram.

    :ivar number:
    :ivar supplier_code: The code of the supplier that provides the
        loyalty program (e.g. UA, HZ, etc.)
    """
    class Meta:
        name = "typeSearchLoyaltyProgram"

    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )


@dataclass
class TypeSearchPhone:
    """
    The phone of the profile to search for.

    :ivar country_code: The country code of the profile to search for.
    :ivar area_code: The area code of the profile to search for.
    :ivar local_number: The phone number of the profile to search for.
    """
    class Meta:
        name = "typeSearchPhone"

    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    local_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "max_length": 50,
        }
    )


class TypeServiceFeeType(Enum):
    """
    A code for categorizing service fees or charges.
    """
    CANCELLATION = "Cancellation"
    CHANGE = "Change"
    EXCHANGE = "Exchange"
    FLAT = "Flat"
    MANUAL_BOOKING = "Manual Booking"
    MISCELLANEOUS = "Miscellaneous"
    NEW_BOOKING = "New Booking"
    PER_PERSON = "Per Person"
    PHONE_BOOKING = "Phone Booking"
    PROCESSING = "Processing"
    REFUND = "Refund"
    FEE_CAP = "Fee Cap"


@dataclass
class TypeStringRestriction:
    """Restrictions on profile data for fields with a data type of string.

    Min and max lengths are inclusive.

    :ivar enumeration: A specific value permitted.
    :ivar min_length: The minimum length permitted.
    :ivar max_length: The maximum length permitted.
    """
    class Meta:
        name = "typeStringRestriction"

    enumeration: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 128,
            "white_space": "collapse",
        }
    )
    min_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinLength",
            "type": "Attribute",
        }
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Attribute",
        }
    )


class TypeSupplierType(Enum):
    """The category of supplier that may apply.

    (Air, Car, Hotel, etc)
    """
    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    OTHER = "Other"


class TypeTaggableElement(Enum):
    """
    Specify which fixed field type this field refers to.
    """
    TRAVEL_DOCUMENT = "TravelDocument"
    LOYALTY_PROGRAM_ENROLLMENT = "LoyaltyProgramEnrollment"
    CONTRACT = "Contract"
    ALTERNATE_CONTACT = "AlternateContact"
    ADDRESS = "Address"
    PHONE = "Phone"
    ELECTRONIC_ADDRESS = "ElectronicAddress"
    ALTERNATE_CONTACT_ADDRESS = "AlternateContactAddress"
    ALTERNATE_CONTACT_PHONE = "AlternateContactPhone"
    ALTERNATE_CONTACT_ELECTRONIC_ADDRESS = "AlternateContactElectronicAddress"
    AIR_PREFERENCE = "AirPreference"
    HOTEL_PREFERENCE = "HotelPreference"
    VEHICLE_PREFERENCE = "VehiclePreference"
    RAIL_PREFERENCE = "RailPreference"
    OTHER_PREFERENCE = "OtherPreference"
    REMARK = "Remark"
    FIELD_DATA = "FieldData"
    FIELD_GROUP_DATA = "FieldGroupData"
    FORM_OF_PAYMENT = "FormOfPayment"


@dataclass
class TypeTravelDocumentAddress:
    """
    Specific Address definition for Travel Document.

    :ivar address_line: An Address can have 1 to 3 address lines for any
        use.  The Address Lines are assumed in order.
    :ivar city: The city of which this address is located.
    :ivar state: The state of which this address is located.
    :ivar other_state_province: Alternate freeform state value
    :ivar country: The country of which this address is located.
    :ivar postal: The postal code of which this address is located.
    """
    class Meta:
        name = "typeTravelDocumentAddress"

    address_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_occurs": 1,
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 128,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
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
    other_state_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
        }
    )


@dataclass
class TypeTravelDocumentAddressHistory:
    """
    Profile Address.

    :ivar address_line:
    :ivar state: The state of which this address is located.
    :ivar other_state_province: Alternate freeform state value
    :ivar country: The country of which this address is located.
    :ivar postal: The postal code of which this address is located.
    :ivar city: The city of which this address is located.
    """
    class Meta:
        name = "typeTravelDocumentAddressHistory"

    address_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 128,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_state_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
        }
    )


class TypeTravelDocumentHistoryHeightUnit(Enum):
    METERS = "Meters"
    FEET = "Feet"


class TypeTravelDocumentHistoryWeightUnit(Enum):
    KILOGRAMS = "Kilograms"
    POUNDS = "Pounds"


class TypeTravelDocumentType(Enum):
    """
    Specify the type of Travel Document.
    """
    VISA = "Visa"
    PASSPORT = "Passport"
    DRIVERS_LICENSE = "Drivers License"
    PERMANENT_RESIDENCE_CARD = "Permanent Residence Card"
    NATIONAL_IDENTITY_CARD = "National Identity Card"
    REDRESS_NUMBER = "Redress Number"
    KNOWN_TRAVELER_NUMBER = "Known Traveler Number"
    MILITARY_CARD = "Military Card"
    OTHER = "Other"


class TypeUpdateAction(Enum):
    """
    Specify whether the change is to update or delete the field.
    """
    UPDATE = "Update"
    DELETE = "Delete"


@dataclass
class AccountingReference(TypeKeyElement):
    """
    Used by the Traveler's employer for budgeting, internal billing or other cost
    accounting purposes.

    :ivar payment_details_ref: A code for categorizing a reference for a
        Traveler’s bookings.  This is often used by the Traveler’s
        employer for budgeting, internal billing, or other cost
        accounting purposes. Util:ReferenceDataRetrieveReq, TypeCode
        AccountingReferenceType
    :ivar type_value: A code for categorizing a reference for a
        Traveler’s bookings. This is often used by the Traveler’s
        employer for budgeting, internal billing, or other cost
        accounting purposes. Util:ReferenceDataRetrieveReq, TypeCode
        AccountingReferenceType
    :ivar value: The number or alphanumeric code for an employer
        reference.
    :ivar account_id: A specific reference to a particular account
        profile.
    :ivar priority_order: Priority order associated with this
        AccountingReference.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    :ivar active: Denotes whether the Accounting Reference is Active or
        Not. Default is true
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    payment_details_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    account_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
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
class Advisory(TypeKeyElement):
    """A categorization of travel documents and other identification, or other
    warnings that an agency may need to share with agents.

    Examples include visas requirements, travel permit requirements,
    passport requirements, etc. May also include government travel or
    health advisories.

    :ivar type_value: A categorization of travel documents and other
        identification, or other warnings that an agency may need to
        share with agents. Examples include visas requirements, travel
        permit requirements, passport requirements, etc. May also
        include government travel or health advisories.
    :ivar start_date: The start date of the advisory
    :ivar end_date: The end date of the advisory
    :ivar summary: A summary of this Advisory
    :ivar description:
    :ivar priority_order: Priority order associated with this Advisory.
    :ivar geo_political_area_type: The type of the geographical
        location.
    :ivar geo_political_area_code: The location code of the geographical
        location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: Optional[TypeAdvisoryType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "name": "Summary",
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
            "max_length": 1000,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
            "required": True,
        }
    )
    geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )


@dataclass
class AgencyPaymentHistory(TypeAgencyPaymentHistory):
    """
    Container for Agency Payment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AlphaNumericRestriction(TypeStringRestriction):
    """Restrictions on profile data for fields with a data type of alphanumeric.

    Min and max lengths are inclusive.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BridgeBranchAdd(TypeBridgeBranchCmd):
    """
    Command to add a bridge branch assoication of an agent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BridgeBranchDelete(TypeBridgeBranchCmd):
    """
    Command to delete a bridge branch assoication of an agent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Commission(TypeKeyElement):
    """
    A representation of the commision given to an Agent or Agency within a profile.

    :ivar type_value: A type that represents a category of commissions.
        Example include per booking, by monetary amount, etc.
    :ivar supplier_type: The commission's supplier type
    :ivar supplier: The commission's supplier
    :ivar amount: A financial amount for a specific commission type for
        a travel supplier.
    :ivar percentage: A percentage for a specific commission type for a
        travel supplier.
    :ivar priority_order: Priority order associated with this
        Commission.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: Optional[TypeCommissionCategory] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class CommissionReference(TypeKeyElement):
    """Data refering to an external or internal Agent who receives commission with
    relation to this profile.

    Agent Name or Number is required.

    :ivar agent_name: Name of the agent.
    :ivar agent_number: Number or code identifying the agent.
    :ivar priority_order: Priority of this commission reference item.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    agent_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class CreateField:
    """
    Specify any existing fields that belong to this group.

    :ivar freeform_text_restriction: Restrictions on profile data for
        fields with a data type of free-form text (i.e., string). Min
        and max lengths are inclusive. Can define either min/max lengths
        or enumerations, but not both.
    :ivar whole_number_restriction: Restrictions on profile data for
        fields with a data type of integer. Min and max values are
        inclusive.
    :ivar decimal_restriction: Restrictions on profile data for fields
        with a data type of float. Min and max values are inclusive.
    :ivar text_restriction: Restrictions on profile data for fields with
        a data type of text (i.e., alpha). Min and max lengths are
        inclusive. Can define either min/max lengths or enumerations,
        but not both.
    :ivar alpha_numeric_restriction: Restrictions on profile data for
        fields with a data type of alphanumeric. Min and max lengths are
        inclusive. Can define either min/max lengths or enumerations,
        but not both.
    :ivar percentage_restriction: Restrictions on profile data for
        fields with a data type of percentage. Min and max values are
        inclusive.
    :ivar name: Name of the field.
    :ivar description: Description of the field.
    :ivar type_value: Data type of the field (e.g., boolean, float,
        string, int).
    :ivar encrypted: Defines whether the data associated to this field
        is to be encrypted in the database. Default is false.
    :ivar masked: Defines whether the field value must be masked in
        messaging, and what masking pattern to apply.
    :ivar default_value: Default value of the field.
    :ivar protected: If true, then special authorization is required for
        a user to create or modify this field or group.
    :ivar display_order: The order displayed by an UI
    :ivar inheritable: Denotes that the custom field is inherited in
        child profiles.  Defaults to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    freeform_text_restriction: Optional[TypeStringRestriction] = field(
        default=None,
        metadata={
            "name": "FreeformTextRestriction",
            "type": "Element",
        }
    )
    whole_number_restriction: Optional[TypeIntegerRestriction] = field(
        default=None,
        metadata={
            "name": "WholeNumberRestriction",
            "type": "Element",
        }
    )
    decimal_restriction: Optional[TypeFloatRestriction] = field(
        default=None,
        metadata={
            "name": "DecimalRestriction",
            "type": "Element",
        }
    )
    text_restriction: Optional[TypeStringRestriction] = field(
        default=None,
        metadata={
            "name": "TextRestriction",
            "type": "Element",
        }
    )
    alpha_numeric_restriction: Optional[TypeStringRestriction] = field(
        default=None,
        metadata={
            "name": "AlphaNumericRestriction",
            "type": "Element",
        }
    )
    percentage_restriction: Optional[TypeFloatRestriction] = field(
        default=None,
        metadata={
            "name": "PercentageRestriction",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    type_value: Optional[TypeCustomFieldDataFormat] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    encrypted: bool = field(
        default=False,
        metadata={
            "name": "Encrypted",
            "type": "Attribute",
        }
    )
    masked: TypeMasked = field(
        default=TypeMasked.NOT_MASKED,
        metadata={
            "name": "Masked",
            "type": "Attribute",
        }
    )
    default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )


@dataclass
class CreditCard(TypeCreditCardType):
    """
    UProfile Specific Credit Card Element.

    :ivar extract_indicator: This is supported for all Profile Types by
        Universal Profile.This indicator will be used by MOS to create a
        Credit Card Extract.
    :ivar active: Denotes whether the Credit Card is Active or
        Not.Default is true
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    extract_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtractIndicator",
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
class CustomFieldDelete(TypeCustomFieldAndGroupDeleteRef):
    """
    Removes a Custom Field  from a Template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldGroupDelete(TypeCustomFieldAndGroupDeleteRef):
    """
    Removes a Custom Field  Group from a Template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class DecimalRestriction(TypeFloatRestriction):
    """Restrictions on profile data for fields with a data type of float.

    Min and max values are inclusive.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class DefaultTemplate:
    """The information about the default account and traveler templates for the
    agency.

    Only returned for agency hierarchy level.

    :ivar profile_type: The profile type that the template is for.
    :ivar template_id: Unique identifier of the template assigned to all
        profiles of this profile type, unless an override template is
        defined.
    :ivar template_version: The current version number of the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_type: Optional[TypeHierarchyOverrideType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    template_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
            "required": True,
        }
    )
    template_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )


@dataclass
class DeleteOverrideDefinition:
    """
    Delete existing override Definition.

    :ivar template_field_id: Unique identifier of the base template
        field or group id .
    :ivar template_field_type:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TemplateFieldID",
            "type": "Attribute",
            "required": True,
        }
    )
    template_field_type: Optional[TypeCustomFieldOrGroupType] = field(
        default=None,
        metadata={
            "name": "TemplateFieldType",
            "type": "Attribute",
        }
    )


@dataclass
class Endpoint:
    """
    Endpoint information.

    :ivar id: Endpoint Id.
    :ivar name: Endpoint Name.
    :ivar description: Endpoint Description.
    :ivar data_type: Data type (Boolean, String, etc) that defines what
        the endpoint consists of.
    :ivar min_occurs: Refers to minimum times the endpoint can ocurr on
        the consuming system's page.  Default to 0.
    :ivar max_occurs: Refers to the maximum times the endpoint can occur
        on the conuming system's page.
    :ivar end_point_code: End Point Code description.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    data_type: Optional[TypeEndpointDataType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Attribute",
            "required": True,
        }
    )
    min_occurs: int = field(
        default=0,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    end_point_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndPointCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EndpointRef(TypeEndpointRef):
    """
    A reference to an endpoint.

    :ivar purpose_type_code: Purpose Code is an additional piece of data
        that augments the link from endpoint to template field
    :ivar end_point_code: End Point Code description.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    purpose_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurposeTypeCode",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    end_point_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndPointCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ExternalIdentifier(TypeKeyElement):
    """
    This is meant for external identification of a Profile.

    :ivar ext_id: The actual value of the External Id of the Profile.
    :ivar source: The Source code for External ID. This depicts the
        origin/source of the External ID. If the Source is a host
        provider i.e, 1G, 1V etc., the ExtID and Source data may not be
        updated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    ext_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class FieldModifyErrorInfo(TypeErrorInfo):
    """
    When field or field groups cannot be modified, we see the templates that use
    the fields and field groups.

    :ivar profile_template_summary: The summary of templates that are in
        use that have the fields or field groups.
    :ivar template_count: The number of templates using the custom
        field. The attribute is returned if there are more than 100
        templates.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_template_summary: List[ProfileTemplateSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileTemplateSummary",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )
    template_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateCount",
            "type": "Attribute",
        }
    )


@dataclass
class FreeformTextRestriction(TypeStringRestriction):
    """Restrictions on profile data for fields with a data type of string.

    Min and max lengths are inclusive.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class GeoPoliticalAreaFilter:
    """
    Retrieve part or parts of profile by a particular geographic location for the
    specified data category.Geographical location is only applicable to the
    following categories:- All Preferences, Air Preference, Vehicle Preference,
    Hotel Preference, Rail Preference and Other Preference.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    filter_type: Optional[TypeGeoPoliticalAreaFilterType] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Attribute",
            "required": True,
        }
    )
    geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
            "required": True,
        }
    )
    geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )


@dataclass
class ModifyField:
    """Details of a root-level field to be updated.

    Root-level fields cannot be created or deleted with this service.
    Child fields must be modified within ModifyFieldGroup. When updating
    a field, to remove data from an optional attribute, omit the
    attribute. Note that Display Order is not applicable to root-level
    fields.

    :ivar freeform_text_restriction: Restrictions on profile data for
        fields with a data type of free-form text (i.e., string). Min
        and max lengths are inclusive. Can define either min/max lengths
        or enumerations, but not both.
    :ivar whole_number_restriction: Restrictions on profile data for
        fields with a data type of integer. Min and max values are
        inclusive.
    :ivar decimal_restriction: Restrictions on profile data for fields
        with a data type of float. Min and max values are inclusive.
    :ivar text_restriction: Restrictions on profile data for fields with
        a data type of text (i.e., alpha). Min and max lengths are
        inclusive. Can define either min/max lengths or enumerations,
        but not both.
    :ivar alpha_numeric_restriction: Restrictions on profile data for
        fields with a data type of alphanumeric. Min and max lengths are
        inclusive. Can define either min/max lengths or enumerations,
        but not both.
    :ivar percentage_restriction: Restrictions on profile data for
        fields with a data type of percentage. Min and max values are
        inclusive.
    :ivar id: Unique identifier of the field.Id is required for update
        or delete action.
    :ivar name: Name of the field.
    :ivar description: Description of the field.
    :ivar type_value: Data type of the field (e.g., boolean, float,
        string, int).
    :ivar encrypted: Defines whether the data associated to this field
        is to be encrypted in the database. Default is false.
    :ivar masked: Defines whether the field value must be masked in
        messaging, and what masking pattern to apply.
    :ivar default_value: Default value of the field.
    :ivar protected: If true, then special authorization is required for
        a user to create or modify this field or group.
    :ivar display_order: The order displayed by an UI
    :ivar inheritable: Denotes that the custom field is inherited in
        child profiles.  Defaults to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar action: Indicate the action to be executed (add, delete, etc.)
    :ivar force: To specify whether this is a Force Update or Force
        Delete.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    freeform_text_restriction: Optional["ModifyField.FreeformTextRestriction"] = field(
        default=None,
        metadata={
            "name": "FreeformTextRestriction",
            "type": "Element",
        }
    )
    whole_number_restriction: Optional["ModifyField.WholeNumberRestriction"] = field(
        default=None,
        metadata={
            "name": "WholeNumberRestriction",
            "type": "Element",
        }
    )
    decimal_restriction: Optional["ModifyField.DecimalRestriction"] = field(
        default=None,
        metadata={
            "name": "DecimalRestriction",
            "type": "Element",
        }
    )
    text_restriction: Optional["ModifyField.TextRestriction"] = field(
        default=None,
        metadata={
            "name": "TextRestriction",
            "type": "Element",
        }
    )
    alpha_numeric_restriction: Optional["ModifyField.AlphaNumericRestriction"] = field(
        default=None,
        metadata={
            "name": "AlphaNumericRestriction",
            "type": "Element",
        }
    )
    percentage_restriction: Optional["ModifyField.PercentageRestriction"] = field(
        default=None,
        metadata={
            "name": "PercentageRestriction",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    type_value: Optional[TypeCustomFieldDataFormat] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    encrypted: bool = field(
        default=False,
        metadata={
            "name": "Encrypted",
            "type": "Attribute",
        }
    )
    masked: TypeMasked = field(
        default=TypeMasked.NOT_MASKED,
        metadata={
            "name": "Masked",
            "type": "Attribute",
        }
    )
    default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    action: Optional[TypeAction] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
            "type": "Attribute",
        }
    )

    @dataclass
    class FreeformTextRestriction(TypeStringRestriction):
        """
        :ivar action: Indicate the action to be executed (update or
            delete)
        """
        action: Optional[TypeAction] = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class WholeNumberRestriction(TypeIntegerRestriction):
        """
        :ivar action: Indicate the action to be executed (update or
            delete)
        """
        action: Optional[TypeAction] = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DecimalRestriction(TypeFloatRestriction):
        """
        :ivar action: Indicate the action to be executed (update or
            delete)
        """
        action: Optional[TypeAction] = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TextRestriction(TypeStringRestriction):
        """
        :ivar action: Indicate the action to be executed (add, update or
            delete)
        """
        action: Optional[TypeAction] = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class AlphaNumericRestriction(TypeStringRestriction):
        """
        :ivar action: Indicate the action to be executed (add, update or
            delete)
        """
        action: Optional[TypeAction] = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PercentageRestriction(TypeFloatRestriction):
        """
        :ivar action: Indicate the action to be executed (add, update or
            delete)
        """
        action: Optional[TypeAction] = field(
            default=None,
            metadata={
                "name": "Action",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class OverrideDefinition:
    """
    Element to override setting of fields defined in default template .Can be used
    to override custom filed,custom group , fixed field group and fixed field.

    :ivar template_field_id: Unique identifier of the base template
        field or group id .
    :ivar hide: A flag that determines if the UI should show this field.
        Default to false.
    :ivar label: Alternate name of the field for display on the UI
    :ivar min_occurs_override: Agency-defined override defining the
        minimum number of values permitted for this field on profiles
        using this template. Value cannot be less than the boundary
        MinOccurs defined on the field or field group itself.
    :ivar read_only: Defines if field as editable or not.
    :ivar template_field_type:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TemplateFieldID",
            "type": "Attribute",
            "required": True,
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        }
    )
    template_field_type: Optional[TypeCustomFieldOrGroupType] = field(
        default=None,
        metadata={
            "name": "TemplateFieldType",
            "type": "Attribute",
        }
    )


@dataclass
class PercentageRestriction(TypeFloatRestriction):
    """Restrictions on profile data for fields with a data type of percentage.

    Min and max values are inclusive.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class PhoneNumberHistory:
    """
    Consists of type (office, home, fax), location (city code), the country code,
    the number, and an extension.

    :ivar provider_reservation_info_ref:
    :ivar key:
    :ivar type_value:
    :ivar location: IATA code for airport or city
    :ivar country_code: Hosts/providers will expect this to be
        international dialing digits
    :ivar area_code:
    :ivar number: The local phone number
    :ivar extension:
    :ivar text:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
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
    type_value: Optional[PhoneNumberHistoryType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 83,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "max_length": 1024,
        }
    )


@dataclass
class PolicyReference(TypeKeyElement):
    """
    Used by the Traveler's employer to administer policy.

    :ivar type_value: A code for categorizing a reference for a
        Traveler's Policy. Valid values are Travelport Universal Policy
        and Other.
    :ivar value: The value that the employer wants to be associated with
        the specified type.
    :ivar desc: A description of the value being used.
    :ivar controlling_policy_id: A specific reference to a particular
        profile that is a parent of the Traveler.
    :ivar priority_order: Priority order associated with this
        PolicyReference.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    controlling_policy_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllingPolicyID",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class ProfileChildSummary:
    """
    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar name: The Name of the profile. For profiles of type Agent,
        concatenate the GivenName and Surname values from the agent
        table, and return as a single attribute in the response.
    :ivar provisioning_code: The provisioning ID/code of the profile, if
        applicable.
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar status: Profile status (Active, Inactive, Pending, Disabled).
    :ivar version: Version of the profile.
    :ivar control: Identify if the entity is a control branch or not.
    :ivar description:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    provisioning_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    status: Optional[TypeProfileEntityStatus] = field(
        default=None,
        metadata={
            "name": "Status",
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
            "min_inclusive": 0,
        }
    )
    control: bool = field(
        default=False,
        metadata={
            "name": "Control",
            "type": "Attribute",
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


@dataclass
class ProfileDataCategory:
    """
    The category of data that controls what data will be returned in the response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: Optional[TypeProfileDataCategory] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ProfileDataDelete:
    """
    Delete one element of given type identified by its key.

    :ivar element: The type of element in the profile.
    :ivar key: The identifier of the element that will be delete from
        this profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    element: Optional[TypeProfileDataElementType] = field(
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
class ProfileHistoryRetrieveCriteria:
    """Specify one or more criteria used to filter the history data.

    Only history data matching all parameters will be returned.

    :ivar agent_id: The unique profile ID of the agent that made the
        change.
    :ivar start_date: The earliest date that the change was made. Leave
        blank to define an open start date.
    :ivar end_date: The latest date that the change was made. Leave
        blank to define an open end date.
    :ivar field_id: To filter by a specific custom field, enter the
        field ID. To filter by a specific instance of a fixed field or
        field group, send the field or field group Key. Must also send
        the relevant FieldGroupType value.
    :ivar field_group_id: To filter by a specific custom field group,
        enter the field group ID. Must also send the relevant
        FieldGroupType value.
    :ivar field_group_type: To filter by a type of fixed field group or
        to filter for all custom field data or all custom field group
        data, send the appropriate field group type. To further refine
        the search by fixed field or group instance or by custom field
        or field group ID, also send FieldID or FieldGroupID.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
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
    field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Attribute",
        }
    )
    field_group_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
        }
    )
    field_group_type: Optional[TypeProfileComponentType] = field(
        default=None,
        metadata={
            "name": "FieldGroupType",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileLink:
    """
    A one way relationship between this profile and another.

    :ivar traveler_id: The ID of the profile to link to.
    :ivar relationship: The relationship of the link (e.g. Sibling,
        Spouse, etc.)
    :ivar given_name: The linked traveler's given name.  No entry
        required. Common attribute data is taken from TravelerInfo and
        will be returned in the Create, Retrieve and Modify response.
        This is only used in the response.
    :ivar other_name: The linked traveler's other name.  No entry
        required. Common attribute data is taken from TravelerInfo and
        will be returned in the Create, Retrieve and Modify response.
        This is only used in the response.
    :ivar surname: The linked traveler's surname.  No entry required.
        Common attribute data is taken from TravelerInfo and will be
        returned in the Create, Retrieve and Modify response. This is
        only used in the response.
    :ivar nickname: The linked traveler's nickname.  No entry required.
        Common attribute data is taken from TravelerInfo and will be
        returned in the Create, Retrieve and Modify response. This is
        only used in the response.
    :ivar electronic_address: The linked traveler's email.  No entry
        required. Common attribute data is taken from TravelerInfo and
        will be returned in the Create, Retrieve and Modify response.
        This is only used in the response.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    traveler_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        }
    )
    relationship: Optional[TypeProfileLinkRelationship] = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    electronic_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class ProfileLinkAdd:
    """
    Add a new link between this profile and the specific profile.

    :ivar traveler_id: The ID of the profile to link to.
    :ivar relationship: The relationship of the link (e.g. Sibling,
        Spouse, etc.)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    traveler_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        }
    )
    relationship: Optional[TypeProfileLinkRelationship] = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileLinkDelete:
    """
    Delete the link between this profile and the specificied profile.

    :ivar traveler_id: The ID of the profile to link to.
    :ivar relationship: The relationship of the link (e.g. Sibling,
        Spouse, etc.)
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    traveler_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        }
    )
    relationship: Optional[TypeProfileLinkRelationship] = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileParentAdd:
    """
    Command to add a new parent profile.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve, modify and delete a
        traveler profile. Combination of UniqueProfileID and AgencyCode
        can be used in place of Profile ID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        }
    )
    provisioning_code: Optional["ProfileParentAdd.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileParentAdd.UniqueProfileId"] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        }
    )

    @dataclass
    class ProvisioningCode:
        """
        :ivar value:
        :ivar profile_type: Specify the Profile Type (limited to only
            the ones where ProvisioningCode is relevant)
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )
        profile_type: Optional[ProvisioningCodeProfileType] = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UniqueProfileId:
        """
        :ivar value:
        :ivar profile_type: Specify the Profile Type (limited to only
            the ones where Profile Identifier is relevant)
        :ivar agency_code: 'AgencyCode' is the Provisioning code of the
            parent Agency. This is an optional attribute and if not
            provided, the system will determine 'AgencyCode' by Agent's
            WAB/target Branch or Agent's agency.
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 6,
                "max_length": 128,
            }
        )
        profile_type: Optional[UniqueProfileIdProfileType] = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )
        agency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AgencyCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 25,
            }
        )


@dataclass
class ProfileParentDelete:
    """
    Command to delete a parent profile.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve, modify and delete a
        traveler profile. Combination of UniqueProfileID and AgencyCode
        can be used in place of Profile ID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        }
    )
    provisioning_code: Optional["ProfileParentDelete.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileParentDelete.UniqueProfileId"] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        }
    )

    @dataclass
    class ProvisioningCode:
        """
        :ivar value:
        :ivar profile_type: Specify the Profile Type (limited to only
            the ones where ProvisioningCode is relevant)
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )
        profile_type: Optional[ProvisioningCodeProfileType] = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UniqueProfileId:
        """
        :ivar value:
        :ivar profile_type: Specify the Profile Type (limited to only
            the ones where Profile Identifier is relevant)
        :ivar agency_code: 'AgencyCode' is the Provisioning code of the
            parent Agency. This is an optional attribute and if not
            provided, the system will determine 'AgencyCode' by Agent's
            WAB/target Branch or Agent's agency.
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 6,
                "max_length": 128,
            }
        )
        profile_type: Optional[UniqueProfileIdProfileType] = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )
        agency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AgencyCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 25,
            }
        )


@dataclass
class ProfileParentSearchSummary:
    """
    A quick summary of a profile's parent.

    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar provisioning_code: User defined provisioning identifier.
    :ivar name: The name of the profile
    :ivar version: Version number of the profile. Required with every
        modify request.
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar status: Profile status (Active, Inactive, Pending, Disabled).
    :ivar immediate_parent_ref: System-defined, unique identifier for
        ImmediateParent Reference
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    provisioning_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    status: Optional[TypeProfileEntityStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    immediate_parent_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImmediateParentRef",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileParentSummary:
    """
    A quick summary of a profile's parent.

    :ivar profile_parent_summary:
    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar provisioning_code: User defined provisioning identifier.
    :ivar name: The name of the profile
    :ivar version: Version number of the profile. Required with every
        modify request.
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar status: Profile status (Active, Inactive, Pending, Disabled).
    :ivar description:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_parent_summary: Optional["ProfileParentSummary"] = field(
        default=None,
        metadata={
            "name": "ProfileParentSummary",
            "type": "Element",
        }
    )
    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    provisioning_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    status: Optional[TypeProfileEntityStatus] = field(
        default=None,
        metadata={
            "name": "Status",
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
            "max_length": 255,
        }
    )


@dataclass
class ProfileStatusUpdate:
    """
    Change the status of the profile.

    :ivar status: The updated status. Inactive status is not valid for
        all profile types.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    status: Optional[TypeProfileEntityStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileSummaryErrorInfo(TypeErrorInfo):
    """Error information when a profile service fails and profile information is
    needed to be returned.

    The service failed because there profiles attached to the element
    being modified.  This error info shows those profiles  Up to the
    first 100 profiles are shown.

    :ivar profile_summary:
    :ivar number_of_children: The number of children that the profile
        attempted to being deleted has.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_summary: List["ProfileSummaryErrorInfo.ProfileSummary"] = field(
        default_factory=list,
        metadata={
            "name": "ProfileSummary",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Attribute",
        }
    )

    @dataclass
    class ProfileSummary:
        """
        :ivar profile_id: The system-assigned, unique ID of the profile.
        :ivar profile_type: The type of profile this profile is for
            (e.g., branch, account, traveler). The profile type
            identifies which default attributes/elements (minimum data
            set) the system will insert.
        :ivar name: Name given to the profile.  If a Traveler or
            Account, then this is a union of the person names.  For all
            other types it is the appropriate name.
        :ivar description: Description of profile
        :ivar provisioning_code: Provisioning code given to the profile
            if applicable.
        """
        profile_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProfileID",
                "type": "Attribute",
                "required": True,
            }
        )
        profile_type: Optional[TypeProfileType] = field(
            default=None,
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
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
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
            }
        )
        provisioning_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ProvisioningCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            }
        )


@dataclass
class ProprietaryData(TypeKeyElement):
    """
    ProprietaryData for a Traveler which can be overridden for immediate parent
    like BranchGroup,Branch,Account and TravelerGroup.

    :ivar proprietary_data_type: The type of ProprietaryData being
        overridden for a TravelerProfile.
    :ivar value: The value of ProprietaryData.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    proprietary_data_type: Optional[ProprietaryDataProprietaryDataType] = field(
        default=None,
        metadata={
            "name": "ProprietaryDataType",
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
            "min_length": 1,
            "max_length": 255,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProviderInfo(TypeKeyElement):
    """
    A representation of the Provider Information (e.g. PCC, IATA, Provider Code)
    given to a Branch profile.

    :ivar provider_code: The provider code associated with the PCC/IATA.
    :ivar pseudo_city_code: Branch pseudo city code.
    :ivar iatacode: Branch IATA Code.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    iatacode: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )


@dataclass
class ServiceFee(TypeKeyElement):
    """
    A representation of the Service Fee given to an Agent or Agency within a
    profile.

    :ivar type_value: A code for categorizing service fees or charges.
    :ivar start_date: The date a specific service fee for a profile
        starts to be applicable.
    :ivar supplier_type: The category of supplier that a service fee may
        apply.
    :ivar amount: The financial amount of a service fee.
    :ivar priority_order: Priority order associated with this
        ServiceFee.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: Optional[TypeServiceFeeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TagAdd:
    """Add a tag to the specified element of the profile.

    There are two methods to add tag to profile data - One is through this TagAdd element and another is through TagRef element.

    :ivar element: The type of element to add the tag to.
    :ivar key: The unique identifier of the specific element into which
        the tag will be added.
    :ivar tag_id: The ID of the tag to add.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    element: Optional[TypeTaggableElement] = field(
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
    tag_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TagID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TagDelete:
    """Delete a tag from the specified element of the profile.

    There are two methods to delete tag from profile data - One is through this TagDelete element and another is through TagRef. To delete the last Tag associated to a ProfileData use TagDelete element.

    :ivar element: The type of element to remove the tag from.
    :ivar key: The unique identifier of the specific element from which
        the tag will be deleted.
    :ivar tag_id: The ID of the tag to delete.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    element: Optional[TypeTaggableElement] = field(
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
    tag_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TagID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextRestriction(TypeStringRestriction):
    """Restrictions on profile data for fields with a data type of alpha.

    Min and max lengths are inclusive.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TravelerIdentityInformation(TypeKeyElement):
    """An additional means to identify or verify a travelers profile when then are
    duplicate traveler names.

    Security Questions and answers must come in pairs.

    :ivar secondary_id_code: A Secondary Identification Code could be
        used to further verification of a Traveler’s profile when there
        are duplicate names. The Secondary Identification Code could be
        partially masked and case sensitive. If masking is requested,
        Secondary identification code is required.
    :ivar mask_secondary_id_code: Indicator to specify if the secondary
        ID code is to be masked or not and if so how.
    :ivar security_question1: If the Security Question is transmitted
        then the Corresponding Security Answer is required.
    :ivar security_answer1: If the Security Answer is transmitted then
        the corresponding Security Question is required.
    :ivar security_question2: If the Security Question is transmitted
        then the Corresponding Security Answer is required.
    :ivar security_answer2: If the Security Answer is transmitted then
        the corresponding Security Question is required.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    secondary_id_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondaryIdCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
    mask_secondary_id_code: Optional[TypeMasked] = field(
        default=None,
        metadata={
            "name": "MaskSecondaryIdCode",
            "type": "Attribute",
        }
    )
    security_question1: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecurityQuestion1",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    security_answer1: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecurityAnswer1",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    security_question2: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecurityQuestion2",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    security_answer2: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecurityAnswer2",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class WholeNumberRestriction(TypeIntegerRestriction):
    """Restrictions on profile data for fields with a data type of string.

    Min and max lengths are inclusive.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeAccountTypeProfileInfo(TypeProfileInfo):
    """
    History Element for Traveler Group.

    :ivar mid_office_id: Mid Office identifier managed by an external
        system.
    """
    class Meta:
        name = "typeAccountTypeProfileInfo"

    mid_office_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MidOfficeID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class TypeAccountingReferenceHistory(TypeKeyElement):
    """
    History Element for Accounting Reference.

    :ivar payment_details_ref: Used to sync up Keys in FormOfPayment
        element with AccountingReference, PaymentDetailsRef by entering
        same key number.
    :ivar type_value: A code for categorizing a reference for a
        Traveler’s bookings. This is often used by the Traveler’s
        employer for budgeting, internal billing, or other cost
        accounting purposes. Util:ReferenceDataRetrieveReq, TypeCode
        AccountingReferenceType
    :ivar value: The number or alphanumeric code for an employer
        reference.
    :ivar account_id: A specific reference to a particular account
        profile.
    :ivar priority_order: Priority order associated with this
        AccountingReference.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    :ivar active: Denotes whether the Accounting Reference is Active or
        Not.
    """
    class Meta:
        name = "typeAccountingReferenceHistory"

    payment_details_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    account_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Attribute",
        }
    )


@dataclass
class TypeAddress(TypeKeyElement):
    """
    Profile Address.

    :ivar address_line: An Address can have 1 to 3 address lines for any
        use.  The Address Lines are assumed in order.
    :ivar city: The city of which this address is located.
    :ivar state: The state of which this address is located.
    :ivar other_state_province: Alternate freeform state value
    :ivar country: The country of which this address is located.
    :ivar postal: The postal code of which this address is located.
    :ivar type_value: Category of address (Mailing, Shipping,
        Collection, Other, Delivery, Location, Billing,
        LocalLangInvoice, Home, Work). Util: ReferenceDataRetrieveReq,
        TypeCode PostalAddressType
    """
    class Meta:
        name = "typeAddress"

    address_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_occurs": 1,
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 128,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
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
    other_state_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
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
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeAdvisoryHistory(TypeKeyElement):
    """
    History Element for Advisory.

    :ivar type_value: A categorization of travel documents and other
        identification, or other warnings that an agency may need to
        share with agents. Examples include visas requirements, travel
        permit requirements, passport requirements, etc. May also
        include government travel or health advisories.
    :ivar start_date: The start date of the advisory
    :ivar end_date: The end date of the advisory
    :ivar summary: A summary of this Advisory
    :ivar description:
    :ivar priority_order: Priority order associated with this Advisory.
    :ivar geo_political_area_type: The type of the geographical
        location.
    :ivar geo_political_area_code: The location code of the geographical
        location.
    """
    class Meta:
        name = "typeAdvisoryHistory"

    type_value: Optional[TypeAdvisoryType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
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
    summary: Optional[str] = field(
        default=None,
        metadata={
            "name": "Summary",
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
            "max_length": 1000,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )


@dataclass
class TypeAgencyGroupInfoHistory(TypeProfileInfo):
    """
    History Element for AgencyGroupInfo.

    :ivar name: Name of Agency Group
    """
    class Meta:
        name = "typeAgencyGroupInfoHistory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeAgencyInfoHistory(TypeProfileInfo):
    """
    History Element for Agency Info.

    :ivar name: Agency name
    :ivar iata_number: Agency IATA number
    :ivar agency_code: Zircon site ID
    :ivar uses_template: If set to true, it denotes that the customer
        uses templates and during parent data inheritance, templates
        will be used. Value can be altered through modify
        service.Default is false.
    :ivar ursync_data: If set to 'Masked' then Form Of Payment card
        number will be masked when Universal Record is sent to
        EventHandler.
    :ivar ursync_to: Identify if Universal Record synch is activated at
        Agency Level.
    """
    class Meta:
        name = "typeAgencyInfoHistory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    iata_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    agency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    uses_template: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsesTemplate",
            "type": "Attribute",
        }
    )
    ursync_data: Optional[TypeAgencyInfoHistoryUrsyncData] = field(
        default=None,
        metadata={
            "name": "URSyncData",
            "type": "Attribute",
        }
    )
    ursync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )


@dataclass
class TypeAgentInfoHistory(TypeProfileInfo):
    """
    History Element for Agent Info.

    :ivar user_name: The login name of the agent.
    :ivar occupational_title:
    :ivar title:
    :ivar nickname:
    :ivar given_name:
    :ivar other_name:
    :ivar surname:
    :ivar suffix:
    :ivar default_branch_id: The profile ID of the branch indicated as
        the default branch for this agent.  On create and modify either
        DefaultBranchID or DefaultBranchCode is required.  If both are
        indicated the ID will be used.
    :ivar default_branch_code: The branch code of the branch indicated
        as the default branch for this agent.  On create and modify
        either DefaultBranchID or DefaultBranchCode is required.  If
        both are indicated the ID will be used.
    :ivar alternate_agent_id:
    """
    class Meta:
        name = "typeAgentInfoHistory"

    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    occupational_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "OccupationalTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    default_branch_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "DefaultBranchID",
            "type": "Attribute",
        }
    )
    default_branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultBranchCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    alternate_agent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateAgentID",
            "type": "Attribute",
            "max_length": 128,
        }
    )


@dataclass
class TypeAlternateContactHistory(TypeKeyElement):
    """
    History Element for Contact info.

    :ivar type_value: A code for categorizing contactees based on a role
        they might play.  Examples include Emergency Contact, Regular
        Contact, Backup Contact, etc.
    :ivar given_name: The given name(s) of a person.  May also be known
        as First Name in some cultures.
    :ivar surname: Surname(s) or family names for a person.  May be
        known as Last Names in some cultures.
    :ivar other_name: Name(s) for a person other than given or surnames.
        Includes those known as Middle Names in some cultures, but may
        include other names such as maiden names.
    :ivar nickname: A alternative name for a person that maybe used
        informally or at the preference of a person.  Examples include
        diminutive versions of names ("Katie" instead of "Katherine"),
        shortened versions of longer names,  or common substitution
        names ("Jack" instead of "John").
    :ivar priority_order: Priority order associated with this Contact.
    """
    class Meta:
        name = "typeAlternateContactHistory"

    type_value: Optional[TypeContactType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeBasePreferenceHistory(TypeKeyElement):
    """
    Base history element for the preference elements.

    :ivar booking_start_date:
    :ivar booking_end_date:
    :ivar currency:
    :ivar departure_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar departure_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar emphasis:
    :ivar general_preference:
    :ivar inclusive: Indicates whether this preference is exclusive or
        inclusive (e.g. preference for not having a queen size bed vs
        preference to HAVE a queen size bed).
    :ivar loyalty_program_enrollment_ref: A reference to a loyalty card
        element.
    :ivar other_loyalty_program_number:
    :ivar payment_details_ref: A reference to a payment details element
        list elsewhere.
    :ivar preference_payment_method:
    :ivar purpose: The purpose of the preference.
    :ivar priority_order: Priority order associated with this
        Preference.
    :ivar supplier:
    :ivar trip_approval:
    """
    class Meta:
        name = "typeBasePreferenceHistory"

    booking_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingStartDate",
            "type": "Attribute",
        }
    )
    booking_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingEndDate",
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        }
    )
    departure_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "DepartureGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    departure_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    emphasis: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Emphasis",
            "type": "Attribute",
        }
    )
    general_preference: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralPreference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Inclusive",
            "type": "Attribute",
        }
    )
    loyalty_program_enrollment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoyaltyProgramEnrollmentRef",
            "type": "Attribute",
        }
    )
    other_loyalty_program_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherLoyaltyProgramNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    payment_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Attribute",
        }
    )
    preference_payment_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferencePaymentMethod",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    purpose: Optional[TypePreferencePurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    trip_approval: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        }
    )


@dataclass
class TypeBranchGroupInfoHistory(TypeProfileInfo):
    """
    History Element for BranchGroupInfo.

    :ivar name: Name of the BranchGroup
    :ivar branch_group_code: Zircon site ID
    :ivar ursync_to: Identify if Universal Record synch is activated at
        Branch Group Level.
    """
    class Meta:
        name = "typeBranchGroupInfoHistory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    branch_group_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchGroupCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    ursync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )


@dataclass
class TypeCommissionHistory(TypeKeyElement):
    """
    History Element for Commission.

    :ivar type_value: A type that represents a category of commissions.
        Example include per booking, by monetary amount, etc.
    :ivar supplier_type: The commission's supplier type
    :ivar supplier: The commission's supplier
    :ivar amount: A financial amount for a specific commission type for
        a travel supplier.
    :ivar percentage: A percentage for a specific commission type for a
        travel supplier.
    :ivar priority_order: Priority order associated with this
        Commission.
    """
    class Meta:
        name = "typeCommissionHistory"

    type_value: Optional[TypeCommissionCategory] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeCommissionReferenceHistory(TypeKeyElement):
    """
    Data refering to an external or internal Agent who recieves commission with
    relation to this profile.

    :ivar agent_name:
    :ivar agent_number:
    :ivar priority_order:
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeCommissionReferenceHistory"

    agent_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    agent_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeCommonEditableField(TypeFieldRef):
    """
    Base type of common attributes that can be edited for a field or field group
    command.

    :ivar min_occurs_override: Agency-defined override defining the
        minimum number of values permitted for this field on profiles
        using this template. Value cannot be less than the boundary
        MinOccurs defined on the field or field group itself.
    :ivar max_occurs_override: Agency-defined override defining the
        maximum number of values permitted for this field on profiles
        using this template. Value cannot be greater than the boundary
        MaxOccurs defined on the field or field group itself.
    :ivar label: Alternate name of the field for display on the UI
    :ivar display_order: The order displayed by an UI
    :ivar inheritable: Denotes that the field/group is inherited in
        child profiles.  Defaults to false. The Field/Group for which
        the Inheritable is set to true in parent profile,is inherited in
        child profiles. The Inheritable attribute is not valid in a
        Template Modify Request if the InheritableControlInd is False
        for that particular Field/Group
    """
    class Meta:
        name = "typeCommonEditableField"

    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )


@dataclass
class TypeContractHistory(TypeKeyElement):
    """
    History Element for Contract.

    :ivar supplier: The supplier associated with the contract.
    :ivar supplier_type: The supplier type associated with the contract.
        (Air, Hotel, etc)
    :ivar provider: The provider associated with the contract.
    :ivar start_date: The date that contract terms start to be applied.
    :ivar expiration_date: The date that contract terms terminate being
        applied.
    :ivar discount_percentage: The percentage of discount applicable to
        a contract.
    :ivar discount_value: The amount of discount applicable to a
        contract.
    :ivar supplier_contract_number: An eternally assigned or managed
        number or alphanumeric data.
    :ivar promotional_designator_name: An eternally assigned or managed
        number or alphanumeric data for a ticket designator.
    :ivar description: Description of the contract.
    :ivar priority_order: Priority order associated with this Contract.
    """
    class Meta:
        name = "typeContractHistory"

    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
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
    discount_percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountPercentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    discount_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountValue",
            "type": "Attribute",
        }
    )
    supplier_contract_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierContractNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    promotional_designator_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PromotionalDesignatorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeEditableEndpoint(TypeEndpointRef):
    """
    Base type of an editable endpoint command.

    :ivar fixed_field_ref: A reference to a fixed field
    :ivar custom_field_ref: A reference to a custom field
    """
    class Meta:
        name = "typeEditableEndpoint"

    fixed_field_ref: Optional[TypeFieldRef] = field(
        default=None,
        metadata={
            "name": "FixedFieldRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    custom_field_ref: Optional[TypeFieldRef] = field(
        default=None,
        metadata={
            "name": "CustomFieldRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )


@dataclass
class TypeElectronicAddress(TypeKeyElement):
    """
    Electronic address or account such as Email, Twitter, etc.

    :ivar name: Value of the address (e.g email address, twitter
        account, etc.)
    :ivar type_value: Type of address (Home, Business, etc)
    :ivar format: Type of address (HTML, PDF, Text, etc)
    """
    class Meta:
        name = "typeElectronicAddress"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
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
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    format: Optional[TypeEmailFormat] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Attribute",
        }
    )


@dataclass
class TypeExternalIdentifierHistory(TypeKeyElement):
    """
    This is meant for external identification of a Profile.

    :ivar ext_id: Value of the External Id of the Profile.
    :ivar source: The Source code for External ID. This depicts the
        origin/source of the External ID.
    """
    class Meta:
        name = "typeExternalIdentifierHistory"

    ext_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeFieldDataHistory(TypeKeyElement):
    """
    History Element for Field Data.

    :ivar display_order: The order the UI should display the field.
    :ivar value: The value of this instance of the field.
    :ivar field_id: The unique ID of the template field (instance of a
        field on a template) that this value is applied to.
    :ivar name: Name of the custom field that this value is applied to.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeFieldDataHistory"

    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeGuaranteeInformationHistory:
    """
    Information pertaining to the payment of type Guarantee.

    :ivar type_value: Guarantee only or Deposit
    :ivar agency_type: Guarantee to Agency IATA or Guarantee to Another
        Agency IATA
    :ivar iatanumber: Payment IATA number. (ie. IATA of Agency or Other
        Agency)
    """
    class Meta:
        name = "typeGuaranteeInformationHistory"

    type_value: Optional[TypeGuaranteeInformationHistoryType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    agency_type: Optional[TypeGuaranteeInformationHistoryAgencyType] = field(
        default=None,
        metadata={
            "name": "AgencyType",
            "type": "Attribute",
        }
    )
    iatanumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeKeyTaggedElement(TypeKeyElement):
    """
    An Element with a Key and a list of Tags.
    """
    class Meta:
        name = "typeKeyTaggedElement"

    tag_ref: List[TagRef] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )


@dataclass
class TypeLoyaltyProgramEnrollmentHistory(TypeKeyElement):
    """
    History Element for Loyalty Program Enrollment.

    :ivar supplier_type: The commission's supplier type
    :ivar supplier: The commission's supplier
    :ivar number: A traveler's specific loyalty program number or
        alphanumeric identifier.
    :ivar program_name: Supplier's loyalty program name such as
        Frontier-EarlyReturns, Renaissance Intl-Marriott Rewards,Alamo-
        QuickSilver Service etc.
    :ivar status: Categorize a status within a loyalty program. Examples
        include Super Elite, Elite, Premier, Prestige, Platinum,
        regular, etc.
    :ivar priority_order: Priority order associated with this
        LoyaltyProgramEnrollment.
    """
    class Meta:
        name = "typeLoyaltyProgramEnrollmentHistory"

    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    program_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeOtherPreferenceHistory(TypeKeyElement):
    """
    History Element for OtherPreference.

    :ivar purpose: The purpose of the preference.
    :ivar priority_order: Priority order associated with this
        Preference.
    :ivar trip_approval:
    :ivar inclusive: Indicates whether this preference is exclusive or
        inclusive (e.g. preference for not having a queen size bed vs
        preference to HAVE a queen size bed).
    :ivar other_supplier_type: The type of the Other Preference.
    :ivar booking_start_date:
    :ivar booking_end_date:
    :ivar usage_start_date:
    :ivar usage_end_date:
    :ivar supplier_name:
    :ivar geo_political_area_type: The type of the geographical
        location.
    :ivar geo_political_area_code: The location code of the geographical
        location.
    :ivar preference_payment_method:
    :ivar payment_details_ref: A reference to a payment details element
        list elsewhere.
    :ivar max_cost_amount:
    :ivar currency:
    :ivar general_preference:
    """
    class Meta:
        name = "typeOtherPreferenceHistory"

    purpose: Optional[TypePreferencePurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    trip_approval: bool = field(
        default=False,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        }
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "name": "Inclusive",
            "type": "Attribute",
        }
    )
    other_supplier_type: Optional[TypeOtherPreference] = field(
        default=None,
        metadata={
            "name": "OtherSupplierType",
            "type": "Attribute",
        }
    )
    booking_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingStartDate",
            "type": "Attribute",
        }
    )
    booking_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingEndDate",
            "type": "Attribute",
        }
    )
    usage_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UsageStartDate",
            "type": "Attribute",
        }
    )
    usage_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UsageEndDate",
            "type": "Attribute",
        }
    )
    supplier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    preference_payment_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferencePaymentMethod",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    payment_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Attribute",
        }
    )
    max_cost_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxCostAmount",
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        }
    )
    general_preference: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralPreference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class TypePaymentDetailsHistory(TypeKeyElement):
    """
    History Element for Payment Details.

    :ivar payment_phone: Payment Phone
    :ivar payment_address: Payment Address
    :ivar start_date: Payment start date
    :ivar expiration_date: Payment expiration date
    :ivar type_value: Type of Payment
    :ivar issued_to_name: Name of the issuee
    :ivar extended_payment: Extended Payment Indicator
    :ivar payment_supplier: The supplier code of the payment. (VI, CA,
        AX, etc)
    :ivar account_number: Payment account number. (ie. Credit card
        number, etc)
    :ivar description: Description of the Payment
    :ivar priority_order: Priority order associated with this
        PaymentDetails.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typePaymentDetailsHistory"

    payment_phone: Optional[PaymentPhone] = field(
        default=None,
        metadata={
            "name": "PaymentPhone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    payment_address: Optional[PaymentAddress] = field(
        default=None,
        metadata={
            "name": "PaymentAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    start_date: Optional[TypeDateOptions] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    expiration_date: Optional[TypeDateOptions] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[TypePaymentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    issued_to_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedToName",
            "type": "Attribute",
        }
    )
    extended_payment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtendedPayment",
            "type": "Attribute",
        }
    )
    payment_supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSupplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypePhone(TypeKeyElement):
    """
    Profile Phone Number.

    :ivar type_value: The type of a phone.
    :ivar country: The phone number's country code
    :ivar area_code: The phone number's area code
    :ivar local_number: The phone number
    :ivar extension: The phone number's extension
    :ivar description: An optional description detailing the phone
        number use.
    :ivar location: The IATA airport/city code that corresponds to the
        location of the phone number.
    """
    class Meta:
        name = "typePhone"

    type_value: Optional[TypePhoneType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    local_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 50,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
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
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 6,
        }
    )


@dataclass
class TypePolicyReferenceHistory(TypeKeyElement):
    """
    History Element for Accounting Reference.

    :ivar type_value: A code used to reference a traveler's policy.
        Valid values are Travelport Universal Policy and Other.
    :ivar value: The number or alphanumeric code for an employer
        reference.
    :ivar controlling_profile_id: A list of policies are created in a
        parent of a traveler, then one of those is applied to the
        traveler. This profileID is to contain the ID of the Parent who
        has the list of policies
    :ivar priority_order: Priority order associated with this
        AccountingReference.
    :ivar desc: An optional description.
    """
    class Meta:
        name = "typePolicyReferenceHistory"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    controlling_profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllingProfileID",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class TypeProfileLinkHistory:
    """
    History Element for ProfileLink Add.

    :ivar traveler_id: The ID of the profile to link to.
    :ivar relationship: The relationship of the link (e.g. Sibling,
        Spouse, etc.)
    :ivar given_name: The linked traveler's given name.  Will be
        returned on profile response.
    :ivar other_name: The linked traveler's other name.  Will be
        returned on profile response.
    :ivar surname: The linked traveler's surname.  Will be returned on
        profile response.
    :ivar nickname: The linked traveler's nickname.  Will be returned on
        profile response.
    :ivar electronic_address: The linked traveler's email.  Will be
        returned on profile response.
    """
    class Meta:
        name = "typeProfileLinkHistory"

    traveler_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
        }
    )
    relationship: Optional[TypeProfileLinkRelationship] = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    electronic_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeProfileParentHistory:
    """
    :ivar profile_id: Agency in which the field group is created.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar profile_name: The name of the profile. Either the concatenated
        first name or last name of a Agent or Traveler or the name of
        the other profile.
    :ivar provisioning_code: The Provisioning Code for this profile.
    """
    class Meta:
        name = "typeProfileParentHistory"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
        }
    )
    profile_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
        }
    )
    provisioning_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )


@dataclass
class TypeProfileStatusHistory:
    """
    History Element for ProfileStatus.

    :ivar status: The updated status.
    """
    class Meta:
        name = "typeProfileStatusHistory"

    status: Optional[TypeProfileEntityStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )


@dataclass
class TypeProprietaryDataHistory(TypeKeyElement):
    """
    History Element for Proprietary Data.

    :ivar proprietary_data_type: The type of ProprietaryData being
        overridden for a TravelerProfile.
    :ivar value: The value of ProprietaryData.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeProprietaryDataHistory"

    proprietary_data_type: Optional[TypeProprietaryDataHistoryProprietaryDataType] = field(
        default=None,
        metadata={
            "name": "ProprietaryDataType",
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeProviderInfoHistory(TypeKeyElement):
    """
    History Element for ProviderInfo Add.

    :ivar provider_code: The provider code associated with the Branch.
    :ivar pseudo_city_code: Branch pseudo city code.
    :ivar iatacode: Branch IATA Code.
    """
    class Meta:
        name = "typeProviderInfoHistory"

    provider_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    iatacode: Optional[str] = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )


@dataclass
class TypeRemarkHistory(TypeKeyElement):
    """
    History Element for Remark.

    :ivar remark_text: The remark text
    :ivar type_value: A code for categorizing a remark. This may include
        General Remarks, Itinerary Remarks, Accounting Remark, Name
        Remark, etc.
    :ivar accounting_remark_type: A code for categorizing an Accounting
        remark. This may include Account, Canned, Fare, Ticket, Other,
        etc.
    :ivar provider: A code for categorizing providers of information
        (GDS source of information).
    :ivar general_remark_type: A code for categorizing remark based on
        the GDS's categorization scheme.
    :ivar category_type: A code for categorizing a remark.
    :ivar supplier_type: The type of supplier associated with the
        remark. (Air, Car, Hotel, etc)
    :ivar supplier: The supplier associated with the remark.
    :ivar priority_order: Priority order associated with this remark.
    """
    class Meta:
        name = "typeRemarkHistory"

    remark_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkText",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_length": 1,
            "max_length": 255,
        }
    )
    type_value: Optional[TypeRemarkType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    accounting_remark_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingRemarkType",
            "type": "Attribute",
        }
    )
    provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    general_remark_type: Optional[TypeGeneralRemarkType] = field(
        default=None,
        metadata={
            "name": "GeneralRemarkType",
            "type": "Attribute",
        }
    )
    category_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryType",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeSearchElectronicAddress:
    """
    The electronic address of the profile to search for.

    :ivar address: The address or account to search for.
    :ivar type_value: Type of Electronic Address to search for
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use.  Examples include business, persona., etc.
    """
    class Meta:
        name = "typeSearchElectronicAddress"

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Attribute",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )


@dataclass
class TypeSearchPaymentDetails:
    """
    The Searchable fields on PaymentDetails.

    :ivar expiration_date:
    :ivar type_value: Cash, Credit, etc.
    :ivar payment_supplier: The supplier code of the payment. (VI, CA,
        AX, etc)
    :ivar account_number: Payment account number (e.g. Credit Card
        Number, etc.)
    """
    class Meta:
        name = "typeSearchPaymentDetails"

    expiration_date: Optional[TypeDateOptions] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[TypePaymentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    payment_supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSupplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class TypeServiceFeeHistory(TypeKeyElement):
    """
    History Element for Service Fee.

    :ivar type_value: A code for categorizing service fees or charges.
    :ivar start_date: The date a specific service fee for a profile
        starts to be applicable.
    :ivar supplier_type: The category of supplier that a service fee may
        apply.
    :ivar amount: The financial amount of a service fee.
    :ivar priority_order: Priority order associated with this Service
        Fee.
    """
    class Meta:
        name = "typeServiceFeeHistory"

    type_value: Optional[TypeServiceFeeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeTravelDocumentHistory(TypeKeyElement):
    """
    History Element for Travel Document.

    :ivar address: Address specifed for the Travel Document
    :ivar type_value: The Travel Document type
    :ivar document_number: The Travel Document type
    :ivar issued_date: The date the travel document was issued
    :ivar expiration_date: The date the travel document expires
    :ivar location_issued_description: The description of the location
        of issuance
    :ivar given_name: Given name as specified on the travel document.
    :ivar middle_name: Middle name as specified on the travel document.
    :ivar surname: Surname as specified on the travel document.
    :ivar gender: Value is tied to ref pub.
    :ivar national_identifier: The national or personal number or
        alphanumeric code that appears on the travel document or
        identification. This is a different number than the document
        number.
    :ivar birth_date: Date of birth as given on this document
    :ivar place_of_birth: Place of birth as given on this document
    :ivar nationality: The nationality of record given on this document
    :ivar citizenship: Country of citizenship
    :ivar issued_by_country: Country this document was issued in
    :ivar issued_by_other_country_name: Another name decrioption of the
        Issued By Country
    :ivar height: A numeric quantity for a traveler's height, as it
        appears on a travel document or identification.
    :ivar height_unit: The unit of measurement for calculating height.
    :ivar weight: A numeric quantity for a traveler's weight, as it
        appears on a travel document or identification.
    :ivar weight_unit: The unit of measurement for calculating weight.
    :ivar residence: The residence that appears on the travel document
        or identification.
    :ivar eye_color: The eye color(s) that appear on the travel document
        or identification.
    :ivar military_status: The military status that appears on the
        travel document or identification.
    :ivar priority_order: Priority order associated with this
        TravelDocument.
    :ivar issued_for_geo_political_area_type: The type of the
        geographical location.
    :ivar issued_for_geo_political_area_code: The location code of the
        geographical location.
    """
    class Meta:
        name = "typeTravelDocumentHistory"

    address: Optional[TypeTravelDocumentAddressHistory] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[TypeTravelDocumentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    issued_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssuedDate",
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
    location_issued_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationIssuedDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "NationalIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        }
    )
    place_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceOfBirth",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Attribute",
            "length": 2,
        }
    )
    citizenship: Optional[str] = field(
        default=None,
        metadata={
            "name": "Citizenship",
            "type": "Attribute",
            "length": 2,
        }
    )
    issued_by_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedByCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    issued_by_other_country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedByOtherCountryName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Attribute",
            "fraction_digits": 2,
        }
    )
    height_unit: Optional[TypeTravelDocumentHistoryHeightUnit] = field(
        default=None,
        metadata={
            "name": "HeightUnit",
            "type": "Attribute",
        }
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "fraction_digits": 2,
        }
    )
    weight_unit: Optional[TypeTravelDocumentHistoryWeightUnit] = field(
        default=None,
        metadata={
            "name": "WeightUnit",
            "type": "Attribute",
        }
    )
    residence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Residence",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    eye_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "EyeColor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    military_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "MilitaryStatus",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    issued_for_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "IssuedForGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    issued_for_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedForGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )


@dataclass
class TypeVoucherInformationHistory:
    """
    Information pertaining to the payment of a Vehicle Rental.

    :ivar voucher_type: Specifies if the Voucher is for Full Credit or a
        Group/Day or a Monetary Amount.
    :ivar amount: Amount associated with the Voucher.
    :ivar confirmation_number: Confirmation from the vendor for the
        voucher
    :ivar account_name: Associated account name for the voucher
    """
    class Meta:
        name = "typeVoucherInformationHistory"

    voucher_type: Optional[TypeVoucherType] = field(
        default=None,
        metadata={
            "name": "VoucherType",
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
    confirmation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Attribute",
        }
    )
    account_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        }
    )


@dataclass
class Action:
    """
    Action information.

    :ivar endpoint: Action Endpoints details.
    :ivar id: Action Unique ID.
    :ivar name: Action Name.
    :ivar description: Action Description.
    :ivar consuming_system: Action Consuming System (Universal Desktop,
        3rd party system).
    :ivar target_service: Action Target Service (Web Service name or
        page name that the data will be utilized).
    :ivar profile_action_code: Profile Action Code description.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    endpoint: List[Endpoint] = field(
        default_factory=list,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    consuming_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumingSystem",
            "type": "Attribute",
            "required": True,
        }
    )
    target_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetService",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_action_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProfileActionCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ActionRef(TypeActionReference):
    """Application of an action to a field.

    Refers to Actions retrieved in ProfileRetrieveAction service
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    endpoint_ref: List[EndpointRef] = field(
        default_factory=list,
        metadata={
            "name": "EndpointRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class BridgeBranchCmd:
    """
    Command to add or remove a Bridge Branch assignment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    bridge_branch_add: Optional[BridgeBranchAdd] = field(
        default=None,
        metadata={
            "name": "BridgeBranchAdd",
            "type": "Element",
        }
    )
    bridge_branch_delete: Optional[BridgeBranchDelete] = field(
        default=None,
        metadata={
            "name": "BridgeBranchDelete",
            "type": "Element",
        }
    )


@dataclass
class Contract(TypeKeyTaggedElement):
    """
    A representation of a contract given between the agency and a
    supplier/provider.

    :ivar supplier: The supplier associated with the contract.
    :ivar supplier_type: The supplier type associated with the contract.
        (Air, Hotel, etc)
    :ivar provider: The provider associated with the contract.
    :ivar start_date: The date that contract terms start to be applied.
    :ivar expiration_date: The date that contract terms terminate being
        applied.
    :ivar discount_percentage: The percentage of discount applicable to
        a contract.
    :ivar discount_value: The amount of discount applicable to a
        contract.
    :ivar supplier_contract_number: An eternally assigned or managed
        number or alphanumeric data.
    :ivar promotional_designator_name: An eternally assigned or managed
        number or alphanumeric data for a ticket designator.
    :ivar description: Description of the contract.
    :ivar priority_order: Priority order associated with this Contract.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
        }
    )
    provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        }
    )
    expiration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
        }
    )
    discount_percentage: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountPercentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    discount_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountValue",
            "type": "Attribute",
        }
    )
    supplier_contract_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierContractNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
    promotional_designator_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PromotionalDesignatorName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class CreateFieldGroup:
    """
    Defines the structure of a new field group, which can be based on existing
    fields and groups (referred to by Id) and/or new fields and groups (referred to
    by FieldGroupRef or FieldRef and defined in FieldList or FieldGroupList).

    :ivar create_field: Specify fields that belong to this group.
    :ivar name: Name of the field group.
    :ivar description: Description of the field group as a whole.
    :ivar protected: If true, then special authorization is required for
        a user to create or modify this field or group.
    :ivar inheritable: Denotes that the custom field group is inherited
        in child profiles.  Defaults to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    create_field: List[CreateField] = field(
        default_factory=list,
        metadata={
            "name": "CreateField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )


@dataclass
class EndpointAdd(TypeEditableEndpoint):
    """
    Add an endpoint to an action within a particular field or field group.

    :ivar purpose_type_code: Purpose Code is an additional piece of data
        that augments the link from endpoint to template field
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    purpose_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurposeTypeCode",
            "type": "Attribute",
            "max_length": 50,
        }
    )


@dataclass
class EndpointRemove(TypeEditableEndpoint):
    """
    Removes an endpoint from an action in a particular field or field group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FieldData(TypeKeyTaggedElement):
    """
    :ivar value: The value of this instance of the field.
    :ivar field_id: The unique ID of the template field (instance of a
        field on a template) that this value is applied to.Provide
        either FieldID or Name, not both.
    :ivar name: Name of the custom field that this value is applied
        to.Provide either Name or FieldID, not both.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class HierarchyLevel:
    """
    Information about a level within an agency/account hierarchy.

    :ivar default_template:
    :ivar hierarchy_level_id: System-assigned, unique hierarchy level ID
        of the immediate parent of this hiearchy level. Leave blank only
        if profile level is agency group.
    :ivar profile_type: The type of profile this hierarchy level
        corresponds to (e.g., branch, account, traveler, group).
    :ivar name: Name of this level of the hierarchy.
    :ivar level_number: Number of this level of the hierarchy, vis-a-vis
        other levels.
    :ivar description: A brief description of this hierarchy level.
    :ivar template_id: Unique identifier of the template assigned to all
        profiles at this level of the hierarchy. Not relevant for
        account and traveler levels.
    :ivar template_version: The current version number of the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    default_template: List[DefaultTemplate] = field(
        default_factory=list,
        metadata={
            "name": "DefaultTemplate",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    level_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "LevelNumber",
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
            "max_length": 255,
        }
    )
    template_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
        }
    )
    template_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )


@dataclass
class InsertOverrideDefinition:
    """
    Insert new override Definition.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    override_definition: List[OverrideDefinition] = field(
        default_factory=list,
        metadata={
            "name": "OverrideDefinition",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class LoyaltyProgramEnrollment(TypeKeyTaggedElement):
    """
    Used for maintaining data for loyalty programs between a supplier and a
    traveler.

    :ivar supplier_type: The commission's supplier type
    :ivar supplier: The commission's supplier
    :ivar number: A traveler's specific loyalty program number or
        alphanumeric identifier.
    :ivar program_name: Supplier's loyalty program name such as
        Frontier-EarlyReturns, Renaissance Intl-Marriott Rewards,Alamo-
        QuickSilver Service etc.
    :ivar status: Categorize a status within a loyalty program.
        Examples include Super Elite, Elite, Premier, Prestige,
        Platinum, regular, etc.
    :ivar priority_order: Priority order associated with this
        LoyaltyProgramEnrollment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
            "required": True,
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    program_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProgramName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class ModifyFieldGroup:
    """Details of the field group and its child fields.

    To remove data from an optional attribute, omit the attribute.

    :ivar modify_field: Details of the child-level field to add, update,
        or remove from group. To remove data from an optional attribute,
        omit the attribute.
    :ivar id: Unique identifier of the field group.
    :ivar name: Name of the field group.
    :ivar description: Description of the field group as a whole.
    :ivar protected: If true, then special authorization is required for
        a user to create or modify this field or group.
    :ivar inheritable: Denotes that the custom field group is inherited
        in child profiles.  Defaults to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar action: To specify whether this is an  update or delete.
    :ivar force: To specify whether this is a Force Update or Force
        Delete.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    modify_field: List[ModifyField] = field(
        default_factory=list,
        metadata={
            "name": "ModifyField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    action: Optional[TypeUpdateAction] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
            "type": "Attribute",
        }
    )


@dataclass
class OtherPreference(TypeKeyTaggedElement):
    """
    Defines a preference for a particular set of criteria (e.g. dates, supplier,
    etc.) that does not fall into the Air, Rail, Vehicle, or Hotel categories.

    :ivar purpose: The purpose of the preference.
    :ivar priority_order: Priority order associated with this
        Preference.
    :ivar trip_approval:
    :ivar inclusive: Indicates whether this preference is exclusive or
        inclusive (e.g. preference for not having a queen size bed vs
        preference to HAVE a queen size bed).
    :ivar other_supplier_type: The type of the Other Preference.
    :ivar supplier_name:
    :ivar booking_start_date: A valid date in YYYY-MM-DD format.
    :ivar booking_end_date: A valid date in YYYY-MM-DD format.
    :ivar usage_start_date:
    :ivar usage_end_date:
    :ivar geo_political_area_type: The type of the geographical
        location.
    :ivar geo_political_area_code: The location code of the geographical
        location.
    :ivar preference_payment_method: See uAPI Profile Help and
        ReferenceDataRetrieveReq, TypeCode PaymentFormatType
    :ivar payment_details_ref: Used to sync up Keys in FormOfPayment
        element with Preference attribute PaymentDetailsRef by entering
        same key number.
    :ivar max_cost_amount: See uAPI Profile Help.
    :ivar currency: ReferencedataRetrieveReq, Type Code Currency
    :ivar general_preference:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    purpose: Optional[TypePreferencePurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    trip_approval: bool = field(
        default=False,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        }
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "name": "Inclusive",
            "type": "Attribute",
        }
    )
    other_supplier_type: Optional[TypeOtherPreference] = field(
        default=None,
        metadata={
            "name": "OtherSupplierType",
            "type": "Attribute",
        }
    )
    supplier_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    booking_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingStartDate",
            "type": "Attribute",
        }
    )
    booking_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingEndDate",
            "type": "Attribute",
        }
    )
    usage_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UsageStartDate",
            "type": "Attribute",
        }
    )
    usage_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UsageEndDate",
            "type": "Attribute",
        }
    )
    geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    preference_payment_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferencePaymentMethod",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    payment_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Attribute",
        }
    )
    max_cost_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxCostAmount",
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        }
    )
    general_preference: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralPreference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class PaymentDetails(TypeKeyTaggedElement):
    """
    Profile Payment.

    :ivar payment_phone: Payment Phone
    :ivar payment_address: Payment Address
    :ivar start_date: Payment start date
    :ivar expiration_date: Payment expiration date
    :ivar type_value: Type of Payment
    :ivar issued_to_name: Name of the issuee
    :ivar extended_payment: Extended Payment Indicator
    :ivar payment_supplier: The supplier code of the payment. (VI, CA,
        AX, etc)
    :ivar account_number: Payment account number. (ie. Credit card
        number, etc)
    :ivar description: Description of the Payment
    :ivar priority_order: Priority order associated with this
        PaymentDetails.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    payment_phone: Optional[PaymentPhone] = field(
        default=None,
        metadata={
            "name": "PaymentPhone",
            "type": "Element",
        }
    )
    payment_address: Optional[PaymentAddress] = field(
        default=None,
        metadata={
            "name": "PaymentAddress",
            "type": "Element",
        }
    )
    start_date: Optional[TypeDateOptions] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
        }
    )
    expiration_date: Optional[TypeDateOptions] = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
        }
    )
    type_value: Optional[TypePaymentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    issued_to_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedToName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    extended_payment: bool = field(
        default=False,
        metadata={
            "name": "ExtendedPayment",
            "type": "Attribute",
        }
    )
    payment_supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSupplier",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
            "required": True,
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileDataFilter:
    """Filters the data in the profile so that only the specified data is returned.

    Multiple categories can be applied if more data is needed on the
    response.  If no filter is specified then "General Information" is
    defaulted.  If duplicate categories are specifed they are ignored.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_data_category: List[TypeProfileDataCategory] = field(
        default_factory=list,
        metadata={
            "name": "ProfileDataCategory",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    geo_political_area_filter: List[GeoPoliticalAreaFilter] = field(
        default_factory=list,
        metadata={
            "name": "GeoPoliticalAreaFilter",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class Remark(TypeKeyTaggedElement):
    """
    Remark given to a profile.

    :ivar remark_text: The remark text
    :ivar type_value: A code for categorizing a remark.  This may
        include General Remarks, Itinerary Remarks, Accounting Remark,
        Name Remark, etc.
    :ivar accounting_remark_type: A code for categorizing an Accounting
        remark. This may include Account, Canned, Fare, Ticket, Other,
        etc... Util:ReferenceDataRetrieveReq, TypeCode
        AccountingRemarkType
    :ivar provider: A code for categorizing providers of information
        (GDS source of information).
    :ivar general_remark_type: A code for categorizing remark based on
        the GDS's categorization scheme.
    :ivar category_type: A code for categorizing a remark.
    :ivar supplier_type: The type of supplier associated with the
        remark. (Air, Car, Hotel, etc)
    :ivar supplier: The supplier associated with the remark.
    :ivar priority_order: Priority order associated with this Remark.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    remark_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemarkText",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    type_value: Optional[TypeRemarkType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    accounting_remark_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingRemarkType",
            "type": "Attribute",
        }
    )
    provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "Provider",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    general_remark_type: Optional[TypeGeneralRemarkType] = field(
        default=None,
        metadata={
            "name": "GeneralRemarkType",
            "type": "Attribute",
        }
    )
    category_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryType",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    supplier_type: Optional[TypeSupplierType] = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TravelDocument(TypeKeyTaggedElement):
    """
    Information about travel-related documents (e.g., passports, driver's license,
    travel visas, military ID cards).

    :ivar address: Address specifed for the Travel Document
    :ivar type_value: The Travel Document type
    :ivar document_number: The Travel Document type
    :ivar issued_date: The date the travel document was issue - YYYY-MM-
        DD
    :ivar expiration_date: The date the travel document expires - YYYY-
        MM-DD
    :ivar location_issued_description: The description of the location
        of issuance
    :ivar given_name: Given name as specified on the travel document.
    :ivar middle_name: Middle name as specified on the travel document.
    :ivar surname: Surname as specified on the travel document.
    :ivar gender: Util: ReferenceDataRetrieveReq, TypeCode
        PersonGenderType
    :ivar national_identifier: The national or personal number or
        alphanumeric code that appears on the travel document or
        identification.  This is a different number than the document
        number.
    :ivar birth_date: Date of birth as given on this document - YYYY-MM-
        DD
    :ivar place_of_birth: Place of birth as given on this document
    :ivar nationality: The nationality of record given on this document
    :ivar citizenship: Country of citizenship. Util:
        ReferenceDataRetrieveReq, TypeCode Country
    :ivar issued_by_country: Country this document was issued in. Util:
        ReferenceDataRetrieveReq, TypeCode Country
    :ivar issued_by_other_country_name: Another name description of the
        Issued By Country
    :ivar height: A numeric quantity for a traveler's height, as it
        appears on a travel document or identification.
    :ivar height_unit: The unit of measurement for calculating height.
    :ivar weight: A numeric quantity for a traveler's weight, as it
        appears on a travel document or identification.
    :ivar weight_unit: The unit of measurement for calculating weight.
    :ivar residence: The residence that appears on the travel document
        or identification.
    :ivar eye_color: The eye color(s) that appear on the travel document
        or identification.
    :ivar military_status: The military status that appears on the
        travel document or identification.
    :ivar priority_order: Priority order associated with this
        TravelDocument.
    :ivar issued_for_geo_political_area_type: The type of the
        geographical location.
    :ivar issued_for_geo_political_area_code: The location code of the
        geographical location.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: Optional[TypeTravelDocumentAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    type_value: Optional[TypeTravelDocumentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    issued_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssuedDate",
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
    location_issued_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationIssuedDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "NationalIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        }
    )
    place_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceOfBirth",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Attribute",
            "length": 2,
        }
    )
    citizenship: Optional[str] = field(
        default=None,
        metadata={
            "name": "Citizenship",
            "type": "Attribute",
            "length": 2,
        }
    )
    issued_by_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedByCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    issued_by_other_country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedByOtherCountryName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Attribute",
            "total_digits": 12,
            "fraction_digits": 2,
        }
    )
    height_unit: Optional[TravelDocumentHeightUnit] = field(
        default=None,
        metadata={
            "name": "HeightUnit",
            "type": "Attribute",
        }
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Attribute",
            "total_digits": 12,
            "fraction_digits": 2,
        }
    )
    weight_unit: Optional[TravelDocumentWeightUnit] = field(
        default=None,
        metadata={
            "name": "WeightUnit",
            "type": "Attribute",
        }
    )
    residence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Residence",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    eye_color: Optional[str] = field(
        default=None,
        metadata={
            "name": "EyeColor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    military_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "MilitaryStatus",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    issued_for_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "IssuedForGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    issued_for_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuedForGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )


@dataclass
class UpdateOverrideDefinition:
    """
    Update esisting override Definition.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    override_definition: List[OverrideDefinition] = field(
        default_factory=list,
        metadata={
            "name": "OverrideDefinition",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class TypeAccountInfoHistory(TypeAccountTypeProfileInfo):
    """
    History Element for Account Info.

    :ivar name: The name of the account.
    :ivar local_language_name: The name of the account in the user's
        local language.
    """
    class Meta:
        name = "typeAccountInfoHistory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeAddressHistory(TypeKeyTaggedElement):
    """
    Profile Address.

    :ivar address_line: An Address can have 1 to 3 address lines for any
        use. The Address Lines are assumed in order.
    :ivar city: The city of which this address is located.
    :ivar state: The state of which this address is located.
    :ivar other_state_province: Alternate freeform state value
    :ivar country: The country of which this address is located.
    :ivar postal: The postal code of which this address is located.
    :ivar type_value: Category of address (Mailing, Shipping, ...)
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use. Examples include business, persona., etc.
    :ivar provisioned: Indicator to show if this address is used as the
        provisioned address.
    :ivar priority_order: Priority order associated with this Address.
    :ivar delivery_description: An optional description detailing the
        delivery.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeAddressHistory"

    address_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 128,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    other_state_province: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
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
    postal: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    provisioned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    delivery_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeAirPreferenceHistory(TypeBasePreferenceHistory):
    """
    Defines an air preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

    :ivar account_code:
    :ivar arrival_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar arrival_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar bench_mark_amount:
    :ivar connection_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar connection_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar contract_code:
    :ivar corporate_id:
    :ivar pseudo_city_code:
    :ivar travel_start_date: A valid date in YYYY-MM-DD format.
    :ivar travel_end_date: A valid date in YYYY-MM-DD format.
    :ivar air_fare_type:
    :ivar crscode:
    :ivar cabin_type_misc_travel: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar cabin_type_ref_category: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar ending_flight_number:
    :ivar fare_type:
    :ivar interline:
    :ivar max_fare_amount:
    :ivar max_connection_minutes:
    :ivar max_domestic_trip_hours:
    :ivar max_employees_per_flight:
    :ivar max_international_trip_hours:
    :ivar meal_type_crs:
    :ivar meal_type_ssr:
    :ivar seat_number:
    :ivar seat_type_misc_travel: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar seat_type_misc_ref_category: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar ssrcode:
    :ivar starting_flight_number:
    """
    class Meta:
        name = "typeAirPreferenceHistory"

    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    arrival_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    arrival_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bench_mark_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "BenchMarkAmount",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    contract_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    corporate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    travel_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelStartDate",
            "type": "Attribute",
        }
    )
    travel_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelEndDate",
            "type": "Attribute",
        }
    )
    air_fare_type: Optional[TypeAirFare] = field(
        default=None,
        metadata={
            "name": "AirFareType",
            "type": "Attribute",
        }
    )
    crscode: Optional[str] = field(
        default=None,
        metadata={
            "name": "CRSCode",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    cabin_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    cabin_type_ref_category: str = field(
        default="ASC",
        metadata={
            "name": "CabinTypeRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    ending_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndingFlightNumber",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    fare_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareType",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    interline: bool = field(
        default=False,
        metadata={
            "name": "Interline",
            "type": "Attribute",
        }
    )
    max_fare_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxFareAmount",
            "type": "Attribute",
        }
    )
    max_connection_minutes: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxConnectionMinutes",
            "type": "Attribute",
        }
    )
    max_domestic_trip_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxDomesticTripHours",
            "type": "Attribute",
        }
    )
    max_employees_per_flight: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxEmployeesPerFlight",
            "type": "Attribute",
        }
    )
    max_international_trip_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxInternationalTripHours",
            "type": "Attribute",
        }
    )
    meal_type_crs: Optional[str] = field(
        default=None,
        metadata={
            "name": "MealTypeCRS",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    meal_type_ssr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MealTypeSSR",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    seat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatNumber",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    seat_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    seat_type_misc_ref_category: str = field(
        default="ASS",
        metadata={
            "name": "SeatTypeMiscRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    ssrcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    starting_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartingFlightNumber",
            "type": "Attribute",
            "max_length": 10,
        }
    )


@dataclass
class TypeBasePreference(TypeKeyTaggedElement):
    """
    :ivar booking_start_date: A valid date in YYYY-MM-DD format.
    :ivar booking_end_date: A valid date in YYYY-MM-DD format.
    :ivar currency: ReferencedataRetrieveReq, Type Code Currency
    :ivar departure_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar departure_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar emphasis:
    :ivar general_preference:
    :ivar inclusive: Indicates whether this preference is exclusive or
        inclusive (e.g. preference for not having a queen size bed vs
        preference to HAVE a queen size bed).
    :ivar loyalty_program_enrollment_ref: Used to sync up Keys in
        LoyaltyProgramEnrollment element with Preference
        LoyaltyProgramEnrollmentRef by entering same key number.
    :ivar other_loyalty_program_number:
    :ivar payment_details_ref: Used to sync up Keys in FormOfPayment
        element with Preference attribute PaymentDetailsRef by entering
        same key number.
    :ivar preference_payment_method: See uAPI Profile Help and
        ReferenceDataRetrieveReq, TypeCode PaymentFormatType
    :ivar purpose: The purpose of the preference.
    :ivar priority_order: Priority order associated with this
        Preference.
    :ivar supplier: a. Util:ReferenceDataRetrieveReq, TypeCode
        HotelSupplierType b.Util:ReferenceDataRetrieveReq, TypeCode
        VehicleSupplierType c. Util:ReferenceDataRetrieveReq, TypeCode
        AirAndRailSupplierType
    :ivar trip_approval:
    """
    class Meta:
        name = "typeBasePreference"

    booking_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingStartDate",
            "type": "Attribute",
        }
    )
    booking_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BookingEndDate",
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        }
    )
    departure_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "DepartureGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    departure_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    emphasis: bool = field(
        default=False,
        metadata={
            "name": "Emphasis",
            "type": "Attribute",
        }
    )
    general_preference: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralPreference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "name": "Inclusive",
            "type": "Attribute",
        }
    )
    loyalty_program_enrollment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoyaltyProgramEnrollmentRef",
            "type": "Attribute",
        }
    )
    other_loyalty_program_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherLoyaltyProgramNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    payment_details_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentDetailsRef",
            "type": "Attribute",
        }
    )
    preference_payment_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferencePaymentMethod",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    purpose: Optional[TypePreferencePurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    trip_approval: bool = field(
        default=False,
        metadata={
            "name": "TripApproval",
            "type": "Attribute",
        }
    )


@dataclass
class TypeBranchInfoHistory(TypeProfileInfo):
    """
    History Element for Branch Info.

    :ivar provider_info: Provider Info values associated to this entity.
    :ivar name: Branch name
    :ivar geo_city_code: Branch geo city code.  Codes can be found in
        Ref Pub.
    :ivar control: Identify if the entity is a control branch or not.
    :ivar branch_code: Zircon site ID
    :ivar currency: Default currency specified for the branch.
    :ivar profile_sync_to: Identify if profile sync to operation can be
        performed.Ignored in request message.
    :ivar profile_sync_from: Identify if profile sync from operation can
        be performed.Ignored in request message.
    :ivar ursync_to: Identify if Universal Record synch is activated at
        Branch Level.
    """
    class Meta:
        name = "typeBranchInfoHistory"

    provider_info: List[TypeProviderInfoHistory] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
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
    geo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoCityCode",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Control",
            "type": "Attribute",
        }
    )
    branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "length": 3,
        }
    )
    profile_sync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncTo",
            "type": "Attribute",
        }
    )
    profile_sync_from: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncFrom",
            "type": "Attribute",
        }
    )
    ursync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )


@dataclass
class TypeCommonEditableGroup(TypeCommonEditableField):
    """
    Base type of common attributes that can be edited for a field group command.

    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    """
    class Meta:
        name = "typeCommonEditableGroup"

    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )


@dataclass
class TypeContact(TypeKeyTaggedElement):
    """
    Base type for a Contact.

    :ivar type_value: A code for categorizing contactees based on a role
        they might play.  Examples include Emergency Contact, Regular
        Contact, Backup Contact, etc.
    :ivar given_name: The given name(s) of a person.  May also be known
        as First Name in some cultures.
    :ivar surname: Surname(s) or family names for a person.  May be
        known as Last Names in some cultures.
    :ivar other_name: Name(s) for a person other than given or surnames.
        Includes those known as Middle Names in some cultures, but may
        include other names such as maiden names.
    :ivar nickname: A alternative name for a person that maybe used
        informally or at the preference of a person.  Examples include
        diminutive versions of names ("Katie" instead of "Katherine"),
        shortened versions of longer names,  or common substitution
        names ("Jack" instead of "John").
    :ivar priority_order: Priority order associated with this Contact.
    """
    class Meta:
        name = "typeContact"

    type_value: Optional[TypeContactType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeCustomField:
    """
    Base representation of a custom field.

    :ivar freeform_text_restriction:
    :ivar whole_number_restriction:
    :ivar decimal_restriction:
    :ivar text_restriction:
    :ivar alpha_numeric_restriction:
    :ivar percentage_restriction:
    :ivar id: Unique identifier of the field.
    :ivar name: Name of the field.
    :ivar description: Description of the field.
    :ivar type_value: Data type of the field (e.g., boolean, float,
        string, int).
    :ivar encrypted: Defines whether the data associated to this field
        is to be encrypted in the database. Default is false.
    :ivar masked: Defines whether the field value must be masked in
        messaging, and what masking pattern to apply.
    :ivar default_value: Default value of the field.
    :ivar protected: If true, then special authorization is required for
        a user to create or modify this field or group.
    :ivar display_order: The order displayed by an UI
    :ivar inheritable: Denotes that the custom field is inherited in
        child profiles.  Defaults to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    """
    class Meta:
        name = "typeCustomField"

    freeform_text_restriction: Optional[FreeformTextRestriction] = field(
        default=None,
        metadata={
            "name": "FreeformTextRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    whole_number_restriction: Optional[WholeNumberRestriction] = field(
        default=None,
        metadata={
            "name": "WholeNumberRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    decimal_restriction: Optional[DecimalRestriction] = field(
        default=None,
        metadata={
            "name": "DecimalRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    text_restriction: Optional[TextRestriction] = field(
        default=None,
        metadata={
            "name": "TextRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    alpha_numeric_restriction: Optional[AlphaNumericRestriction] = field(
        default=None,
        metadata={
            "name": "AlphaNumericRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    percentage_restriction: Optional[PercentageRestriction] = field(
        default=None,
        metadata={
            "name": "PercentageRestriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    type_value: Optional[TypeCustomFieldDataFormat] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    encrypted: bool = field(
        default=False,
        metadata={
            "name": "Encrypted",
            "type": "Attribute",
        }
    )
    masked: TypeMasked = field(
        default=TypeMasked.NOT_MASKED,
        metadata={
            "name": "Masked",
            "type": "Attribute",
        }
    )
    default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )


@dataclass
class TypeEditableCustomField(TypeCommonEditableField):
    """
    Base type of an editable custom field or field group command.

    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    :ivar search_option: If true, then this field is identified as one
        that is allowed to be searched on.  It is user defined.
    :ivar search_option_display_order: The display order for search
        option.
    """
    class Meta:
        name = "typeEditableCustomField"

    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        }
    )
    search_option_display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        }
    )


@dataclass
class TypeElectronicAddressHistory(TypeKeyTaggedElement):
    """
    Electronic address or account such as Email, Twitter, etc.

    :ivar name: Value of the address (e.g email address, twitter
        account, etc.)
    :ivar type_value: Type of address (Home, Business, etc)
    :ivar format: Type of address (HTML, PDF, Text, etc)
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use. Examples include business, persona., etc.
    :ivar provisioned: Indicator to show if this electronic address is
        used as the provisioned electronic address.
    :ivar priority_order: Priority order associated with this Electronic
        address.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeElectronicAddressHistory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1000,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    format: TypeEmailFormat = field(
        default=TypeEmailFormat.HTML,
        metadata={
            "name": "Format",
            "type": "Attribute",
        }
    )
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    provisioned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeFieldGroupDataHistory(TypeKeyElement):
    """
    History Element for Field Group Data.

    :ivar field_data: Data values associated to this entity. Each value
        is linked to a field instance, which defines the attributes of
        the field specific to the associated template or its parent
        field group.
    :ivar field_group_id: The unique ID of the template field group
        (instance of a field group on a template) that this value is
        applied to.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeFieldGroupDataHistory"

    field_data: List[TypeFieldDataHistory] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    field_group_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeFormOfPaymentType(TypeKeyTaggedElement):
    """
    :ivar credit_card:
    :ivar debit_card:
    :ivar certificate:
    :ivar ticket_number:
    :ivar check:
    :ivar requisition:
    :ivar misc_form_of_payment:
    :ivar agency_payment:
    :ivar united_nations:
    :ivar direct_payment:
    :ivar agent_voucher:
    :ivar payment_advice:
    :ivar guarantee:
    :ivar voucher:
    :ivar cash:
    :ivar type_value: The code from the PAYMENT_FORMAT_TYPE_CD (CRECRD,
        DEBDRC, REQSTN…).
    :ivar description: Description of the Payment
    :ivar priority_order: Priority order associated with this
        PaymentDetails.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeFormOfPaymentType"

    credit_card: Optional[CreditCard] = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    debit_card: Optional[TypePaymentCard] = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    certificate: Optional[Certificate] = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "min_length": 1,
            "max_length": 13,
        }
    )
    check: Optional[Check] = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    requisition: Optional[Requisition] = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    misc_form_of_payment: Optional[MiscFormOfPayment] = field(
        default=None,
        metadata={
            "name": "MiscFormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    agency_payment: Optional[AgencyPayment] = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    united_nations: Optional[UnitedNations] = field(
        default=None,
        metadata={
            "name": "UnitedNations",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    direct_payment: Optional[DirectPayment] = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    agent_voucher: Optional[AgentVoucher] = field(
        default=None,
        metadata={
            "name": "AgentVoucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    payment_advice: Optional[PaymentAdvice] = field(
        default=None,
        metadata={
            "name": "PaymentAdvice",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    guarantee: Optional[TypeGuaranteeInformation] = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    voucher: Optional[TypeVoucherInformation] = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    cash: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cash",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeHotelPreferenceHistory(TypeBasePreferenceHistory):
    """
    Defines a hotel preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

    :ivar bed_type_misc_travel: Util: ReferenceDataRetrieveReq, TypeCode
        'HotelMiscType'
    :ivar bed_type_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType'
    :ivar check_in_start_date:
    :ivar check_in_end_date:
    :ivar corporate_discount_number:
    :ivar max_room_rate_amount:
    :ivar multi_level_rate_code:
    :ivar property_id:
    :ivar rate_code:
    :ivar smoking_room:
    :ivar special_request_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    :ivar special_request_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    """
    class Meta:
        name = "typeHotelPreferenceHistory"

    bed_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bed_type_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedTypeRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    check_in_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CheckInStartDate",
            "type": "Attribute",
        }
    )
    check_in_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CheckInEndDate",
            "type": "Attribute",
        }
    )
    corporate_discount_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    max_room_rate_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxRoomRateAmount",
            "type": "Attribute",
        }
    )
    multi_level_rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "MultiLevelRateCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    property_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyID",
            "type": "Attribute",
            "max_length": 20,
        }
    )
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    smoking_room: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmokingRoom",
            "type": "Attribute",
        }
    )
    special_request_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    special_request_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )


@dataclass
class TypePaymentCardHistory:
    """
    Container for all credit and debit card information.

    :ivar phone_number_history:
    :ivar billing_address: The address to where the billing statements
        for this card are sent. Used for address verification purposes.
    :ivar type_value: The 2 letter credit/ debit card type.
    :ivar number:
    :ivar exp_date: The Expiration date of this card in YYYY-MM format.
    :ivar name: The name as it appears on the card.
    :ivar cvv: Card Verification Code
    :ivar approval_code: This code is optional for an authorization
        process from the Credit Card company directly,optional for some
        of the CCH carriers.
    """
    class Meta:
        name = "typePaymentCardHistory"

    phone_number_history: Optional[PhoneNumberHistory] = field(
        default=None,
        metadata={
            "name": "PhoneNumberHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    billing_address: Optional[TypeStructuredAddress] = field(
        default=None,
        metadata={
            "name": "BillingAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        }
    )
    exp_date: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "ExpDate",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    cvv: Optional[str] = field(
        default=None,
        metadata={
            "name": "CVV",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    approval_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprovalCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )


@dataclass
class TypePhoneHistory(TypeKeyTaggedElement):
    """
    Profile Phone Number.

    :ivar type_value: The type of a phone.
    :ivar country: The phone number's country code
    :ivar area_code: The phone number's area code
    :ivar local_number: The phone number
    :ivar extension: The phone number's extension
    :ivar location: The IATA airport/city code that corresponds to the
        location of the phone number.
    :ivar description: An optional description detailing the phone
        number use.
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use. Examples include business, persona., etc.
    :ivar provisioned: Indicator to show if this phone is used as the
        provisioned phone.
    :ivar priority_order: Priority order associated with this Phone.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typePhoneHistory"

    type_value: Optional[TypePhoneType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    local_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 6,
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
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    provisioned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeProfileSearchCriteria:
    """
    Basic search criteria.

    :ivar address:
    :ivar phone:
    :ivar electronic_address:
    :ivar external_identifier:
    :ivar additional_identifier: Additional identifier managed by an
        external system.
    """
    class Meta:
        name = "typeProfileSearchCriteria"

    address: Optional[TypeSearchAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    phone: Optional[TypeSearchPhone] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    electronic_address: Optional[TypeSearchElectronicAddress] = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    external_identifier: Optional[TypeSearchExternalIdentifier] = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    additional_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalIdentifier",
            "type": "Attribute",
        }
    )


@dataclass
class TypeRailPreferenceHistory(TypeBasePreferenceHistory):
    """
    Defines a rail preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

    :ivar account_code:
    :ivar arrival_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar arrival_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar bench_mark_amount:
    :ivar connection_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar connection_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar contract_code:
    :ivar corporate_id:
    :ivar pseudo_city_code:
    :ivar travel_start_date: A valid date in YYYY-MM-DD format.
    :ivar travel_end_date: A valid date in YYYY-MM-DD format.
    :ivar cabin_type:
    :ivar domestic_trip_journey_hours:
    :ivar ending_train_number:
    :ivar international_trip_journey_hours:
    :ivar max_employees_per_train:
    :ivar max_fare_amount:
    :ivar gender_compartment_type:
    :ivar coach_compartment_type:
    :ivar seat_arrangement_type:
    :ivar seating_type:
    :ivar seat_position_misc_travel: Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar seat_position_ref_category:
    :ivar smoking:
    :ivar starting_train_number:
    :ivar ticket_fulfillment_type:
    """
    class Meta:
        name = "typeRailPreferenceHistory"

    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    arrival_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    arrival_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bench_mark_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "BenchMarkAmount",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    contract_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    corporate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    travel_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelStartDate",
            "type": "Attribute",
        }
    )
    travel_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelEndDate",
            "type": "Attribute",
        }
    )
    cabin_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    domestic_trip_journey_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "DomesticTripJourneyHours",
            "type": "Attribute",
        }
    )
    ending_train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndingTrainNumber",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    international_trip_journey_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "InternationalTripJourneyHours",
            "type": "Attribute",
        }
    )
    max_employees_per_train: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxEmployeesPerTrain",
            "type": "Attribute",
        }
    )
    max_fare_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxFareAmount",
            "type": "Attribute",
        }
    )
    gender_compartment_type: Optional[TypeRailGenderCompartment] = field(
        default=None,
        metadata={
            "name": "GenderCompartmentType",
            "type": "Attribute",
        }
    )
    coach_compartment_type: Optional[TypeRailCoachCompartment] = field(
        default=None,
        metadata={
            "name": "CoachCompartmentType",
            "type": "Attribute",
        }
    )
    seat_arrangement_type: Optional[TypeRailSeatArrangement] = field(
        default=None,
        metadata={
            "name": "SeatArrangementType",
            "type": "Attribute",
        }
    )
    seating_type: Optional[TypeRailSeating] = field(
        default=None,
        metadata={
            "name": "SeatingType",
            "type": "Attribute",
        }
    )
    seat_position_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatPositionMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    seat_position_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatPositionRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        }
    )
    starting_train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartingTrainNumber",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    ticket_fulfillment_type: Optional[TypeRailTicketFulfillmentOption] = field(
        default=None,
        metadata={
            "name": "TicketFulfillmentType",
            "type": "Attribute",
        }
    )


@dataclass
class TypeSearchContact:
    """
    Defines the Contact attributes allowed in searching.

    :ivar given_name:
    :ivar other_name:
    :ivar surname:
    :ivar nick_name:
    :ivar address:
    :ivar phone:
    :ivar electronic_address:
    :ivar type_value: A code for categorizing contactees based on a role
        they might play.  Examples include Emergency Contact, Regular
        Contact, Backup Contact, etc.
    """
    class Meta:
        name = "typeSearchContact"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    nick_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NickName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    address: Optional[TypeSearchAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    phone: Optional[TypeSearchPhone] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    electronic_address: Optional[TypeSearchElectronicAddress] = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[TypeContactType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass
class TypeTaggableAddress(TypeAddress):
    """
    Base type of an address that is taggable.

    :ivar tag_ref:
    :ivar delivery_description: An optional description detailing the
        delivery.
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use.  Examples include business, persona., etc.
    :ivar priority_order: Priority order associated with this Address.
    """
    class Meta:
        name = "typeTaggableAddress"

    tag_ref: List[TagRef] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    delivery_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeTaggableElectronicAddress(TypeElectronicAddress):
    """
    Base type of an electronic address that is taggable.

    :ivar tag_ref:
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use.  Examples include business, persona., etc.
    :ivar priority_order: Priority order associated with this
        ElectronicAddress.
    """
    class Meta:
        name = "typeTaggableElectronicAddress"

    tag_ref: List[TagRef] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeTaggablePhone(TypePhone):
    """
    Base type of a phone that is taggable.

    :ivar tag_ref:
    :ivar purpose: A code for categorizing a contact mechanism based on
        purpose or use.  Examples include business, persona., etc.
    :ivar priority_order: Priority order associated with this Phone.
    """
    class Meta:
        name = "typeTaggablePhone"

    tag_ref: List[TagRef] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    purpose: Optional[TypeContactPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass
class TypeTravelerGroupInfoHistory(TypeAccountTypeProfileInfo):
    """
    History Element for Traveler Group.

    :ivar name: Name of the TravelerGroup
    :ivar local_language_name: The name of the TravelerGroup in the
        user's local language.
    """
    class Meta:
        name = "typeTravelerGroupInfoHistory"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeTravelerInfoHistory(TypeAccountTypeProfileInfo):
    """
    History Element for Traveler Info.

    :ivar proprietary_data: ProprietaryData for a Traveler which can be
        overridden for immediate parent like BranchGroup,Branch,Account
        and TravelerGroup.
    :ivar passenger_type_code: Three character code representing a
        passenger type.
    :ivar unique_profile_id: Used as a primary identification for a
        traveler profile. Data transmitted must be unique for each
        traveler profile and will be validated system wide.
    :ivar title: Util: ReferenceDataRetrieveReq, TypeCode
        MiscellaneousTable Category Code Title.
    :ivar nickname:
    :ivar other_name:
    :ivar suffix:
    :ivar birth_date: Date of Birth of Traveler - YYYY-MM-DD
    :ivar gender: Util: ReferenceDataRetrieveReq, TypeCode
        PersonGenderType
    :ivar vip_status:
    :ivar job_title: The job title of the traveler.
    :ivar disability: Text describing a traveler's disability
    :ivar home_city_or_airport: The City or  Airport designated as Home
        for the traveler
    :ivar local_language: A field to identify the Local Language of the
        traveler.  This field references the ISO 639-1 table and the
        IETF BCP 47 list to get languages.  The expected format would be
        a 2 letter language code if coming from the ISO 639-1 table (xx)
        or if coming from the IETF BCP 47 list then it will be a 2
        letter language code followed by a 2 letter qualifier (xx-YY).
    :ivar local_language_given_name:
    :ivar local_language_surname:
    :ivar local_language_username:
    :ivar given_name:
    :ivar surname:
    """
    class Meta:
        name = "typeTravelerInfoHistory"

    proprietary_data: List[ProprietaryData] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    passenger_type_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
            "min_length": 3,
            "max_length": 5,
        }
    )
    unique_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Attribute",
            "min_length": 6,
            "max_length": 128,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    vip_status: bool = field(
        default=False,
        metadata={
            "name": "VipStatus",
            "type": "Attribute",
        }
    )
    job_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
    disability: Optional[str] = field(
        default=None,
        metadata={
            "name": "Disability",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    home_city_or_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeCityOrAirport",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    local_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguage",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    local_language_given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageGivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageSurname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_username: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageUsername",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeVehiclePreferenceHistory(TypeBasePreferenceHistory):
    """
    Defines avehicle preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

    :ivar corporate_id:
    :ivar pick_up_start_date:
    :ivar pick_up_end_date:
    :ivar rate_code:
    :ivar special_equip_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    :ivar special_equip_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    :ivar special_request_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    :ivar special_request_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    :ivar vehicle_type_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    :ivar vehicle_type_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    """
    class Meta:
        name = "typeVehiclePreferenceHistory"

    corporate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pick_up_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PickUpStartDate",
            "type": "Attribute",
        }
    )
    pick_up_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PickUpEndDate",
            "type": "Attribute",
        }
    )
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    special_equip_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialEquipMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    special_equip_ref_category: str = field(
        default="CEQ",
        metadata={
            "name": "SpecialEquipRefCategory",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    special_request_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    special_request_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    vehicle_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    vehicle_type_ref_category: str = field(
        default="CTP",
        metadata={
            "name": "VehicleTypeRefCategory",
            "type": "Attribute",
            "max_length": 4,
        }
    )


@dataclass
class Address(TypeTaggableAddress):
    """
    Profile Address.

    :ivar provisioned: Indicator to show if this address is used as the
        provisioned address.  Default is false.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    provisioned: bool = field(
        default=False,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class AgencyCriteria(TypeProfileSearchCriteria):
    """
    Agency search modifiers.

    :ivar name: Agency name wild card
    :ivar agency_code: Zircon site ID
    :ivar iata_number: IATA Number wild card
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    agency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
        }
    )
    iata_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
        }
    )


@dataclass
class AgencyGroupCriteria(TypeProfileSearchCriteria):
    """
    Agency Group search modifiers.

    :ivar name: Agency Group name wild card
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )


@dataclass
class AgentCriteria(TypeProfileSearchCriteria):
    """
    Agent search modifiers.

    :ivar username: Username wild card
    :ivar given_name: Given name wild card
    :ivar surname: Surname wild card
    :ivar alternate_agent_id:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    username: Optional[str] = field(
        default=None,
        metadata={
            "name": "Username",
            "type": "Attribute",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
        }
    )
    alternate_agent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateAgentID",
            "type": "Attribute",
            "max_length": 128,
        }
    )


@dataclass
class AirPreference(TypeBasePreference):
    """
    Defines an air preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

    :ivar account_code:
    :ivar arrival_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar arrival_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar bench_mark_amount:
    :ivar connection_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar connection_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar contract_code:
    :ivar corporate_id:
    :ivar pseudo_city_code:
    :ivar travel_start_date: A valid date in YYYY-MM-DD format.
    :ivar travel_end_date: A valid date in YYYY-MM-DD format.
    :ivar air_fare_type:
    :ivar cabin_type_misc_travel: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar cabin_type_ref_category: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar starting_flight_number:
    :ivar ending_flight_number:
    :ivar interline:
    :ivar max_fare_amount: See uAPI Profile Help.
    :ivar max_connection_minutes:
    :ivar max_employees_per_flight:
    :ivar max_domestic_trip_hours:
    :ivar max_international_trip_hours:
    :ivar seat_number:
    :ivar seat_type_misc_travel: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar seat_type_misc_ref_category: : Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar crscode: Required if transmitting an SSR Code. Values are 1G
        or 1V
    :ivar ssrcode: a. ReferenceDataSearchReq Type  SsrType
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    arrival_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    arrival_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bench_mark_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "BenchMarkAmount",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    contract_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    corporate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    travel_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelStartDate",
            "type": "Attribute",
        }
    )
    travel_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelEndDate",
            "type": "Attribute",
        }
    )
    air_fare_type: Optional[TypeAirFare] = field(
        default=None,
        metadata={
            "name": "AirFareType",
            "type": "Attribute",
        }
    )
    cabin_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    cabin_type_ref_category: str = field(
        default="ASC",
        metadata={
            "name": "CabinTypeRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    starting_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    ending_flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    interline: bool = field(
        default=False,
        metadata={
            "name": "Interline",
            "type": "Attribute",
        }
    )
    max_fare_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxFareAmount",
            "type": "Attribute",
        }
    )
    max_connection_minutes: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxConnectionMinutes",
            "type": "Attribute",
        }
    )
    max_employees_per_flight: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxEmployeesPerFlight",
            "type": "Attribute",
        }
    )
    max_domestic_trip_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxDomesticTripHours",
            "type": "Attribute",
        }
    )
    max_international_trip_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxInternationalTripHours",
            "type": "Attribute",
        }
    )
    seat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatNumber",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    seat_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    seat_type_misc_ref_category: str = field(
        default="ASS",
        metadata={
            "name": "SeatTypeMiscRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    crscode: Optional[str] = field(
        default=None,
        metadata={
            "name": "CRSCode",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    ssrcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        }
    )


@dataclass
class AlternateContact(TypeContact):
    """
    Outside Contact information refering to relationships such as Emergency
    Contact.

    :ivar address: Contact Address
    :ivar phone: Contact Phone
    :ivar electronic_address: Contact Email
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[TypeTaggableAddress] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[TypeTaggablePhone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[TypeTaggableElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AlternateContactAddress(TypeTaggableAddress):
    """
    Alternate contact address.

    :ivar alternate_contact_ref: Key referencing to alternate contact.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    alternate_contact_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlternateContactElectronicAddress(TypeTaggableElectronicAddress):
    """
    Alternate contact email.

    :ivar alternate_contact_ref: Key referencing to alternate contact.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    alternate_contact_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AlternateContactPhone(TypeTaggablePhone):
    """
    Alternate contact phone.

    :ivar alternate_contact_ref: Key referencing to alternate contact.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    alternate_contact_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BranchCriteria(TypeProfileSearchCriteria):
    """
    Branch search modifiers.

    :ivar name: Branch name wild card
    :ivar iata_number: IATA Number wild card
    :ivar branch_type: Specify the Branch type filter.  Defaults to
        WorkspaceOnly.
    :ivar pseudo_city_code: PseudoCityCode wild card
    :ivar branch_code: Zircon site ID
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    iata_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
        }
    )
    branch_type: TypeFilterControlAndWorkspace = field(
        default=TypeFilterControlAndWorkspace.WORKSPACE_ONLY,
        metadata={
            "name": "BranchType",
            "type": "Attribute",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
        }
    )
    branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
        }
    )


@dataclass
class BranchGroupCriteria(TypeProfileSearchCriteria):
    """
    Branch Group search modifiers.

    :ivar name: Branch Group name wild card
    :ivar branch_group_code: Zircon site ID
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    branch_group_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchGroupCode",
            "type": "Attribute",
        }
    )


@dataclass
class CustomField(TypeCustomField):
    """
    Specify any existing fields that belong to this group.

    :ivar action_ref:
    :ivar label: Alternate name of the field for display on the UI.
        Labels are only valid for custom fields at the root level
    :ivar searchable: All custom fields are searchable.  This will
        always be true.
    :ivar search_option: If true, then this field is identified as one
        that is allowed to be searched on.  It is user defined.
    :ivar search_option_display_order: The display order for search
        option.
    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    :ivar min_occurs_override: Agency-defined override defining the
        minimum number of values permitted for this field on profiles
        using this template. Value cannot be less than the boundary
        MinOccurs defined on the field or field group itself.
    :ivar max_occurs_override: Agency-defined override defining the
        maximum number of values permitted for this field on profiles
        using this template. Value cannot be greater than the boundary
        MaxOccurs defined on the field or field group itself.
    :ivar inheritable_control_ind: A flag to indicate whether agency can
        control inheritance. Default to false.
    :ivar read_only: Defines if field as editable or not.
    :ivar overriden:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    action_ref: List[ActionRef] = field(
        default_factory=list,
        metadata={
            "name": "ActionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    searchable: Optional[object] = field(
        default=None,
        metadata={
            "name": "Searchable",
            "type": "Attribute",
            "required": True,
        }
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        }
    )
    search_option_display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    inheritable_control_ind: bool = field(
        default=False,
        metadata={
            "name": "InheritableControlInd",
            "type": "Attribute",
        }
    )
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        }
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        }
    )


@dataclass
class CustomFieldAdd(TypeEditableCustomField):
    """
    Add Custom field to the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldGroupAdd(TypeCommonEditableGroup):
    """
    Add custom field group to the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldGroupUpdate(TypeCommonEditableGroup):
    """
    Modify the agency-defined attributes of a custom field group already associated
    with the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class CustomFieldUpdate(TypeEditableCustomField):
    """
    Modify the agency-defined attributes of a custom field already associated with
    the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ElectronicAddress(TypeTaggableElectronicAddress):
    """
    Electronic address or account such as Email, Twitter, etc.

    :ivar provisioned: Indicator to show if this electronic address is
        used as the provisioned electronic address.  Default is false.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    provisioned: bool = field(
        default=False,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class Field(TypeCustomField):
    """
    Specify any existing fields that belong to this group.

    :ivar profile_id: The profile ID of the agency or account that the
        field belongs to.
    :ivar profile_type: The type of the Profile to be created.
    :ivar is_used: True if the custom field is in use by one or more
        profiles.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    is_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsUsed",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FieldGroupData(TypeKeyTaggedElement):
    """
    :ivar field_data: Data values associated to this entity. Each value
        is linked to a field instance, which defines the attributes of
        the field specific to the associated template or its parent
        field group.
    :ivar field_group_id: The unique ID of the template field group
        (instance of a field group on a template) that this value is
        applied to.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_data: List[FieldData] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
            "required": True,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class FixedField:
    """
    Specify existing fixed fields that belong to the default template.

    :ivar fixed_field_group_ref:
    :ivar action_ref:
    :ivar id: Unique identifier of the field.
    :ivar label: Alternate name of the field for display on the UI
    :ivar display_order: The order displayed by an UI
    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    :ivar search_option: If true, then this field is identified as one
        that is allowed to be searched on.  It is user defined.
    :ivar search_option_display_order: The display order for search
        option.
    :ivar min_occurs_override: Minimum Agency-defined override defining
        the minimum number of instances permitted by the agency.
    :ivar max_occurs_override: Maximum Agency-defined override defining
        the maximum number of instances permitted by the agency.
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).  Leave blank to indicate 0.
    :ivar name: Name of the field.
    :ivar data_type: Data type of the field (e.g., boolean, float,
        string, int).
    :ivar component: The corresponding name of the attribute or sub-
        element that this field refers to in the profile message.  This
        is a read only field.
    :ivar description: Description of the Fixed Field as defined by the
        system.
    :ivar encrypted: Defines whether the data associated to this field
        is to be encrypted in the database. Default is false.
    :ivar masked: Defines whether the field value must be masked in
        messaging, and what masking pattern to apply.
    :ivar searchable: Flag to indicate if the field is searchable.
    :ivar inheritable: A flag to indicate if the field can be inherited.
        Default to false.  Only applies to root level fields. Fields
        within field groups are not inheritable.
    :ivar read_only: Defines if field as editable or not.
    :ivar overriden:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    fixed_field_group_ref: List[FixedFieldGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "FixedFieldGroupRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    action_ref: List[ActionRef] = field(
        default_factory=list,
        metadata={
            "name": "ActionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    search_option: bool = field(
        default=False,
        metadata={
            "name": "SearchOption",
            "type": "Attribute",
        }
    )
    search_option_display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "SearchOptionDisplayOrder",
            "type": "Attribute",
        }
    )
    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    data_type: Optional[TypeFixedFieldDataFormat] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Attribute",
            "required": True,
        }
    )
    component: Optional[str] = field(
        default=None,
        metadata={
            "name": "Component",
            "type": "Attribute",
            "max_length": 50,
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
    encrypted: bool = field(
        default=False,
        metadata={
            "name": "Encrypted",
            "type": "Attribute",
        }
    )
    masked: TypeMasked = field(
        default=TypeMasked.NOT_MASKED,
        metadata={
            "name": "Masked",
            "type": "Attribute",
        }
    )
    searchable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Searchable",
            "type": "Attribute",
            "required": True,
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        }
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        }
    )


@dataclass
class FixedGroupUpdate(TypeCommonEditableGroup):
    """Update the agency-defined attributes for a fixed field group.

    To remove a value, omit the attribute entirely.

    :ivar max_occurs: Maximum number of instances permitted.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).  Leave blank to indicate 0.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )


@dataclass
class FormOfPayment(TypeFormOfPaymentType):
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class HotelPreference(TypeBasePreference):
    """
    Defines a preference for a particular set of criteria for hotels (e.g., dates,
    rates, chain, room type).

    :ivar bed_type_misc_travel: Util: ReferenceDataRetrieveReq, TypeCode
        'HotelMiscType'
    :ivar bed_type_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType'
    :ivar check_in_start_date: A valid date in YYYY-MM-DD format.
    :ivar check_in_end_date: A valid date in YYYY-MM-DD format.
    :ivar corporate_discount_number:
    :ivar max_room_rate_amount: See uAPI Profile Help.
    :ivar multi_level_rate_code:
    :ivar property_id:
    :ivar rate_code:
    :ivar smoking_room:
    :ivar special_request_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    :ivar special_request_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    bed_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bed_type_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "BedTypeRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    check_in_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CheckInStartDate",
            "type": "Attribute",
        }
    )
    check_in_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CheckInEndDate",
            "type": "Attribute",
        }
    )
    corporate_discount_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateDiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    max_room_rate_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxRoomRateAmount",
            "type": "Attribute",
        }
    )
    multi_level_rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "MultiLevelRateCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    property_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PropertyID",
            "type": "Attribute",
            "max_length": 20,
        }
    )
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    smoking_room: bool = field(
        default=False,
        metadata={
            "name": "SmokingRoom",
            "type": "Attribute",
        }
    )
    special_request_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    special_request_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )


@dataclass
class Phone(TypeTaggablePhone):
    """
    Profile Phone Number.

    :ivar provisioned: Indicator to show if this phone is used as the
        provisioned phone.  Default is false.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    provisioned: bool = field(
        default=False,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileSearch:
    """
    All the fixed fields allowed for searching.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    contract_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 50,
        }
    )
    travel_document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelDocumentNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        }
    )
    accounting_reference: Optional[TypeSearchAccountingReference] = field(
        default=None,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
        }
    )
    alternate_contact: Optional[TypeSearchContact] = field(
        default=None,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
        }
    )
    loyalty_program: Optional[TypeSearchLoyaltyProgram] = field(
        default=None,
        metadata={
            "name": "LoyaltyProgram",
            "type": "Element",
        }
    )
    payment_details: Optional[TypeSearchPaymentDetails] = field(
        default=None,
        metadata={
            "name": "PaymentDetails",
            "type": "Element",
        }
    )
    field_data_search: List[FieldDataSearch] = field(
        default_factory=list,
        metadata={
            "name": "FieldDataSearch",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class RailPreference(TypeBasePreference):
    """
    Defines a preference for a particular set of criteria for rail (e.g., dates,
    compartment type).

    :ivar account_code:
    :ivar arrival_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar arrival_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar bench_mark_amount:
    :ivar connection_geo_political_area_type: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar connection_geo_political_area_code: Util:
        ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    :ivar contract_code:
    :ivar corporate_id:
    :ivar pseudo_city_code:
    :ivar travel_start_date: A valid date in YYYY-MM-DD format.
    :ivar travel_end_date: A valid date in YYYY-MM-DD format.
    :ivar domestic_trip_journey_hours:
    :ivar starting_train_number:
    :ivar ending_train_number:
    :ivar international_trip_journey_hours:
    :ivar max_employees_per_train:
    :ivar max_fare_amount: See uAPI Profile Help.
    :ivar cabin_type: Util: ReferenceDataRetrieveReq, TypeCode
        RailCabinType
    :ivar gender_compartment_type:
    :ivar coach_compartment_type:
    :ivar seat_arrangement_type:
    :ivar seating_type:
    :ivar seat_position_misc_travel: Util:ReferenceDataRetrieveReq,
        TypeCode AirAndRailMiscType
    :ivar seat_position_ref_category:
    :ivar smoking:
    :ivar ticket_fulfillment_type:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    account_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    arrival_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    arrival_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bench_mark_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "BenchMarkAmount",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_type: Optional[TypeGeoPoliticalAreaType] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    contract_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    corporate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    travel_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelStartDate",
            "type": "Attribute",
        }
    )
    travel_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TravelEndDate",
            "type": "Attribute",
        }
    )
    domestic_trip_journey_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "DomesticTripJourneyHours",
            "type": "Attribute",
        }
    )
    starting_train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartingTrainNumber",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    ending_train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndingTrainNumber",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    international_trip_journey_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "InternationalTripJourneyHours",
            "type": "Attribute",
        }
    )
    max_employees_per_train: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxEmployeesPerTrain",
            "type": "Attribute",
        }
    )
    max_fare_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxFareAmount",
            "type": "Attribute",
        }
    )
    cabin_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CabinType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    gender_compartment_type: Optional[TypeRailGenderCompartment] = field(
        default=None,
        metadata={
            "name": "GenderCompartmentType",
            "type": "Attribute",
        }
    )
    coach_compartment_type: Optional[TypeRailCoachCompartment] = field(
        default=None,
        metadata={
            "name": "CoachCompartmentType",
            "type": "Attribute",
        }
    )
    seat_arrangement_type: Optional[TypeRailSeatArrangement] = field(
        default=None,
        metadata={
            "name": "SeatArrangementType",
            "type": "Attribute",
        }
    )
    seating_type: Optional[TypeRailSeating] = field(
        default=None,
        metadata={
            "name": "SeatingType",
            "type": "Attribute",
        }
    )
    seat_position_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatPositionMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    seat_position_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeatPositionRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        }
    )
    ticket_fulfillment_type: Optional[TypeRailTicketFulfillmentOption] = field(
        default=None,
        metadata={
            "name": "TicketFulfillmentType",
            "type": "Attribute",
        }
    )


@dataclass
class VehiclePreference(TypeBasePreference):
    """
    Defines a preference for a particular set of criteria for vehicle (e.g., dates,
    equipment, vendor, car type).

    :ivar corporate_id:
    :ivar pick_up_start_date: A valid date in YYYY-MM-DD format.
    :ivar pick_up_end_date: A valid date in YYYY-MM-DD format.
    :ivar rate_code:
    :ivar special_equip_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    :ivar special_equip_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    :ivar special_request_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    :ivar special_request_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode 'HotelMiscType', Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType.
    :ivar vehicle_type_misc_travel: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    :ivar vehicle_type_ref_category: Util: ReferenceDataRetrieveReq,
        TypeCode VehicleMiscType
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    corporate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pick_up_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PickUpStartDate",
            "type": "Attribute",
        }
    )
    pick_up_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PickUpEndDate",
            "type": "Attribute",
        }
    )
    rate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    special_equip_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialEquipMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    special_equip_ref_category: str = field(
        default="CEQ",
        metadata={
            "name": "SpecialEquipRefCategory",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    special_request_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    special_request_ref_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialRequestRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    vehicle_type_misc_travel: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    vehicle_type_ref_category: str = field(
        default="CTP",
        metadata={
            "name": "VehicleTypeRefCategory",
            "type": "Attribute",
            "max_length": 4,
        }
    )


@dataclass
class TypeAccountTypeProfileSearchCriteria(TypeProfileSearchCriteria):
    """
    Search criteria for Accounts, Traveler Groups and Travellers.

    :ivar mid_office_id: Mid Office ID managed by an external system.
    """
    class Meta:
        name = "typeAccountTypeProfileSearchCriteria"

    mid_office_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MidOfficeID",
            "type": "Attribute",
        }
    )


@dataclass
class TypeCreditCardTypeHistory(TypePaymentCardHistory):
    """
    :ivar extended_payment: Used for American Express cards.
    :ivar customer_reference: Agencies use this to pass the traveler
        information to the credit card company.
    :ivar acceptance_override: Override airline restriction on the
        credit card.
    :ivar third_party_payment: If true, this indicates that the credit
        card holder is not one of the passengers.
    :ivar bank_name: Issuing bank name for this credit card
    :ivar bank_country_code: ISO Country code associated with the
        issuing bank
    :ivar extract_indicator: This is supported for all Profile Types by
        Universal Profile.This indicator will be used by MOS to create a
        Credit Card Extract.
    :ivar active: Denotes whether the Credit Card is Active or Not.
    """
    class Meta:
        name = "typeCreditCardTypeHistory"

    extended_payment: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExtendedPayment",
            "type": "Attribute",
        }
    )
    customer_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Attribute",
        }
    )
    acceptance_override: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcceptanceOverride",
            "type": "Attribute",
        }
    )
    third_party_payment: bool = field(
        default=False,
        metadata={
            "name": "ThirdPartyPayment",
            "type": "Attribute",
        }
    )
    bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankName",
            "type": "Attribute",
        }
    )
    bank_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankCountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    extract_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtractIndicator",
            "type": "Attribute",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Attribute",
        }
    )


@dataclass
class AccountCriteria(TypeAccountTypeProfileSearchCriteria):
    """
    Account search modifiers.

    :ivar name: Account name wild card
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )


@dataclass
class AccountInfo(TypeAccountTypeProfileInfo):
    """
    Account specific profile information.

    :ivar address: Account Address
    :ivar phone: Account Phone Number
    :ivar electronic_address: Account Electronic Address
    :ivar external_identifier: Account External Identifier
    :ivar name: The name of the account.
    :ivar local_language_name: The name of the account in the user's
        local language.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class AgencyBaseInfo:
    """
    Information relating to Agency.

    :ivar phone: Agency Phone Number
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class AgencyGroupInfo(TypeProfileInfo):
    """
    Information relating to Agency Group.

    :ivar address: Agency Group Address
    :ivar phone: Agency Group Phone Number
    :ivar electronic_address: Agency Group Electronic Address
    :ivar external_identifier: Agency Group External Identifier
    :ivar name: Name of Agency Group
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class AgencyInfo(TypeProfileInfo):
    """
    Information relating to Agency.

    :ivar advisory: A set of documents or other advice for travel
        purposes that an agency recommends that a traveler have, based
        on a destination."
    :ivar address: Agency Address
    :ivar phone: Agency Phone Number
    :ivar electronic_address: Agency Electronic Address
    :ivar external_identifier: Agency External Identifier
    :ivar name: Agency name. Modifying this value requires special
        authorization.
    :ivar iata_number: An IATA number associated to the agency. Not used
        to transact with host systems. Specified in the profile only to
        support searching for the agency profile by IATA number.
    :ivar agency_code: Zircon site ID. Modifying this value requires
        special authorization.
    :ivar uses_template: If set to true, it denotes that the customer
        uses templates and during parent data inheritance, templates
        will be used. Value can be altered through modify
        service.Default is false.
    :ivar profile_sync_to: Identify if profile sync to operation can be
        performed.Ignored in request message.
    :ivar profile_sync_from: Identify if profile sync from operation can
        be performed.Ignored in request message.
    :ivar ursync_data: If set to 'Masked' then Form Of Payment card
        number will be masked when Universal Record is sent to
        EventHandler.
    :ivar ursync_to: Identify if Universal Record synch is activated at
        Agency Level.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    advisory: List[Advisory] = field(
        default_factory=list,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    iata_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    agency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    uses_template: bool = field(
        default=False,
        metadata={
            "name": "UsesTemplate",
            "type": "Attribute",
        }
    )
    profile_sync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncTo",
            "type": "Attribute",
        }
    )
    profile_sync_from: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncFrom",
            "type": "Attribute",
        }
    )
    ursync_data: AgencyInfoUrsyncData = field(
        default=AgencyInfoUrsyncData.MASKED,
        metadata={
            "name": "URSyncData",
            "type": "Attribute",
        }
    )
    ursync_to: bool = field(
        default=False,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )


@dataclass
class AgentInfo(TypeProfileInfo):
    """
    Agent specific profile information.

    :ivar address: Agent Address
    :ivar phone: Agent Phone Number
    :ivar electronic_address: Agent Electronic Address.
    :ivar external_identifier: Agent External Identifier
    :ivar user_name: The login name of the agent. Modifying this value
        requires special authorization.
    :ivar occupational_title:
    :ivar title:
    :ivar nickname:
    :ivar given_name: Given name of the agent. Modifying this value
        requires special authorization.
    :ivar other_name:
    :ivar surname: Surname of the agent. Modifying this value requires
        special authorization.
    :ivar suffix:
    :ivar default_branch_id: The profile ID of the branch assigned as
        the default branch for this agent. If both the profile ID and
        branch code of the default branch are specified, the ID will be
        used.
    :ivar default_branch_code: The branch code of the branch assigned as
        the default branch for this agent. If both the profile ID and
        branch code of the default branch are specified, the ID will be
        used.
    :ivar alternate_agent_id:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    occupational_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "OccupationalTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    default_branch_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "DefaultBranchID",
            "type": "Attribute",
        }
    )
    default_branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultBranchCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    alternate_agent_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternateAgentID",
            "type": "Attribute",
            "max_length": 128,
        }
    )


@dataclass
class BranchBaseInfo:
    """
    Information relating to Branch.

    :ivar address: Branch Address
    :ivar phone: Branch Phone Number
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class BranchGroupInfo(TypeProfileInfo):
    """
    Branch group specific profile information.

    :ivar address: Branch Group Address
    :ivar phone: Branch Group  Phone Number
    :ivar electronic_address: Branch Group Electronic Address
    :ivar external_identifier: Branch Group External Identifier
    :ivar name: Branch group name. Modifying this value requires special
        authorization.
    :ivar branch_group_code: Zircon site ID. Modifying this value
        requires special authorization.
    :ivar profile_sync_to: Identify if profile sync to operation can be
        performed.Ignored in request message.
    :ivar profile_sync_from: Identify if profile sync from operation can
        be performed.Ignored in request message.
    :ivar ursync_to: Identify if Universal Record synch is activated at
        Branch Group Level.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    branch_group_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchGroupCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    profile_sync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncTo",
            "type": "Attribute",
        }
    )
    profile_sync_from: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncFrom",
            "type": "Attribute",
        }
    )
    ursync_to: bool = field(
        default=False,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )


@dataclass
class BranchInfo(TypeProfileInfo):
    """
    Information relating to Branch.

    :ivar address: Branch Address.
    :ivar phone: Branch Phone Number.
    :ivar electronic_address: Branch Electronic Address
    :ivar provider_info: PCCs and IATAs associated to the branch. Note
        that this profile information is not used to transact with host
        systems. The data is specified in the profile only to support
        searching for the branch profile by PCC/IATA. Modifying this
        data requires special authorization.
    :ivar external_identifier: Branch External Identifier
    :ivar name: Branch name. Modifying this value requires special
        authorization.
    :ivar geo_city_code: Branch geo city code.  Codes can be found in
        Ref Pub.
    :ivar control: Identifies whether the entity is a control branch.
        Modifying this value requires special authorization.
    :ivar branch_code: Zircon site ID. Modifying this value requires
        special authorization.
    :ivar currency: Default currency specified for the branch.
    :ivar profile_sync_to: Identify if profile sync to operation can be
        performed.Ignored in request message.
    :ivar profile_sync_from: Identify if profile sync from operation can
        be performed.Ignored in request message.
    :ivar ursync_to: Identify if Universal Record synch is activated at
        Branch Level.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_info: List[ProviderInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    geo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoCityCode",
            "type": "Attribute",
            "required": True,
            "max_length": 10,
        }
    )
    control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Control",
            "type": "Attribute",
            "required": True,
        }
    )
    branch_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    profile_sync_to: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncTo",
            "type": "Attribute",
        }
    )
    profile_sync_from: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProfileSyncFrom",
            "type": "Attribute",
        }
    )
    ursync_to: bool = field(
        default=False,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        }
    )


@dataclass
class CustomFieldGroup:
    """
    Defines the structure of a new field group, which can be based on existing
    fields and groups (referred to by Id) and/or new fields and groups (referred to
    by FieldGroupRef or FieldRef and defined in FieldList or FieldGroupList).

    :ivar custom_field: Specify fields that belong to this group.
    :ivar id: Unique identifier of the field group.
    :ivar name: Name of the field group.
    :ivar display_order: The order displayed by an UI
    :ivar description: Description of the field group as a whole.
    :ivar label: Alternate name of the field for display on the UI
    :ivar inheritable: If true, thern this custom field can be inherited
        in children profiles.
    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar min_occurs_override: Agency-defined override defining the
        minimum number of values permitted for this field on profiles
        using this template. Value cannot be less than the boundary
        MinOccurs defined on the field or field group itself.
    :ivar max_occurs_override: Agency-defined override defining the
        maximum number of values permitted for this field on profiles
        using this template. Value cannot be greater than the boundary
        MaxOccurs defined on the field or field group itself.
    :ivar inheritable_control_ind: A flag to indicate whether agency can
        control inheritance. Default to false.
    :ivar read_only: Defines if field as editable or not.
    :ivar overriden:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    custom_field: List[CustomField] = field(
        default_factory=list,
        metadata={
            "name": "CustomField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
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
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    inheritable_control_ind: bool = field(
        default=False,
        metadata={
            "name": "InheritableControlInd",
            "type": "Attribute",
        }
    )
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        }
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        }
    )


@dataclass
class FieldGroup:
    """
    Defines the structure of a new field group, which can be based on existing
    fields and groups (referred to by Id) and/or new fields and groups (referred to
    by FieldGroupRef or FieldRef and defined in FieldList or FieldGroupList).

    :ivar field_value: Specify fields that belong to this group.
    :ivar id: Unique identifier of the field group.
    :ivar name: Name of the field group.
    :ivar description: Description of the field group as a whole.
    :ivar protected: If true, then special authorization is required for
        a user to create or modify this field or group.
    :ivar inheritable: Denotes that the custom field group is inherited
        in child profiles.  Defaults to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar profile_id: The profile ID of the agency or account that the
        field belongs to.
    :ivar profile_type: The type of the Profile to be created.
    :ivar is_used: True if the custom field group has been added to a
        template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    is_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsUsed",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class FixedFieldGroup:
    """
    Defines the structure of a fixed group, which can be based on existing fixed
    fields and groups.

    :ivar fixed_field: Specify fixed fields that belong to this group.
    :ivar fixed_field_group: Specify fixed fields that belong to this
        group.
    :ivar id: Unique identifier of the fixed group.
    :ivar name: Name of the field group.
    :ivar description: Description of the field group as a whole.
    :ivar component: The corresponding name of the element that this
        field refers to in the profile message. This is a read only
        attribute.
    :ivar correlation_element: The name of an attribute on the profile
        element that defines a "type".  This is a read-only attribute.
    :ivar correlation_value: The value that should be put in the
        attribute that the CorrelationElement defines.  This is a read-
        only attribute.
    :ivar display_order: The order displayed by an UI
    :ivar hide: A flag the determines if the UI should show this field.
        Default to false.
    :ivar inheritable: A flag to indicate if the group can be inherited.
        Default to false.
    :ivar min_occurs: Minimum number of instances permitted (e.g., 0,
        1).
    :ivar max_occurs: Maximum number of instances permitted. Leave blank
        to indicate unlimited (i.e., ..*).
    :ivar label: Alternate name of the field group for display on the UI
    :ivar min_occurs_override: Minimum Agency-defined override defining
        the minimum number of instances permitted by the agency.
    :ivar max_occurs_override: Maximum Agency-defined override defining
        the maximum number of instances permitted by the agency.
    :ivar inheritable_control_ind: A flag to indicate whether agency can
        control inheritance. Default to false.
    :ivar read_only: Defines if field as editable or not.
    :ivar overriden:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    fixed_field: List[FixedField] = field(
        default_factory=list,
        metadata={
            "name": "FixedField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fixed_field_group: List["FixedFieldGroup"] = field(
        default_factory=list,
        metadata={
            "name": "FixedFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
    component: Optional[str] = field(
        default=None,
        metadata={
            "name": "Component",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    correlation_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrelationElement",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    correlation_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrelationValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    hide: bool = field(
        default=False,
        metadata={
            "name": "Hide",
            "type": "Attribute",
        }
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
        }
    )
    min_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccursOverride",
            "type": "Attribute",
        }
    )
    max_occurs_override: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccursOverride",
            "type": "Attribute",
        }
    )
    inheritable_control_ind: bool = field(
        default=False,
        metadata={
            "name": "InheritableControlInd",
            "type": "Attribute",
        }
    )
    read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadOnly",
            "type": "Attribute",
        }
    )
    overriden: bool = field(
        default=False,
        metadata={
            "name": "Overriden",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileDataAdd:
    """
    Command to add profile data information.

    :ivar address: Address belonging to the profile (will be updated in
        the  "Info" elements)
    :ivar phone: Phone Number belonging to the profile (will be updated
        in the  "Info" elements)
    :ivar electronic_address: Electronic Address belonging to the
        profile (will be updated in the  "Info" elements)
    :ivar traveler_identity_information: An additional means to identify
        or verify a travelers profile when then are duplicate traveler
        names.
    :ivar external_identifier: Meant for external identification of a
        Profile. This will be added in Info element of the Profile.
    :ivar travel_document:
    :ivar accounting_reference:
    :ivar policy_reference:
    :ivar loyalty_program_enrollment:
    :ivar commission:
    :ivar contract:
    :ivar service_fee:
    :ivar form_of_payment:
    :ivar air_preference:
    :ivar hotel_preference:
    :ivar other_preference:
    :ivar remark:
    :ivar field_data: Add new values for root-level custom fields. To
        add a new child field value, use ProfileDataUpdate and update
        the parent field group.
    :ivar alternate_contact:
    :ivar alternate_contact_address:
    :ivar alternate_contact_phone:
    :ivar alternate_contact_electronic_address:
    :ivar field_group_data: Add new instances of a custom field group
        and child field values.
    :ivar vehicle_preference:
    :ivar advisory:
    :ivar commission_reference:
    :ivar rail_preference:
    :ivar provider_info:
    :ivar proprietary_data:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    traveler_identity_information: Optional[TravelerIdentityInformation] = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    accounting_reference: List[AccountingReference] = field(
        default_factory=list,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "max_occurs": 20000,
        }
    )
    policy_reference: List[PolicyReference] = field(
        default_factory=list,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    loyalty_program_enrollment: List[LoyaltyProgramEnrollment] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    service_fee: List[ServiceFee] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_preference: List[AirPreference] = field(
        default_factory=list,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_preference: List[HotelPreference] = field(
        default_factory=list,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    other_preference: List[OtherPreference] = field(
        default_factory=list,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_data: List[FieldData] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact: List[AlternateContact] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact_address: List[AlternateContactAddress] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact_phone: List[AlternateContactPhone] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact_electronic_address: List[AlternateContactElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group_data: List[FieldGroupData] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_preference: List[VehiclePreference] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    advisory: List[Advisory] = field(
        default_factory=list,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission_reference: List[CommissionReference] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_preference: List[RailPreference] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_info: List[ProviderInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    proprietary_data: List[ProprietaryData] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class TemplateModifyCmd:
    """
    Wrapper for a set of modification commands to be applied to this template.

    :ivar template_info_update:
    :ivar fixed_field_update: Update allowed attributes for fixed field.
        The attributes will not be updated if not specified.
    :ivar fixed_group_update: Update allowed attributes for  the fixed
        group data.  The attributes will not be updated if not
        specified.
    :ivar custom_field_add:
    :ivar custom_field_update:
    :ivar custom_field_group_add:
    :ivar custom_field_group_update:
    :ivar endpoint_add: Add an endpoint to  a particular field or field
        group
    :ivar endpoint_remove: Removes an endpoint from a particular field
        or field group
    :ivar custom_field_delete:
    :ivar custom_field_group_delete:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_info_update: Optional[TemplateInfoUpdate] = field(
        default=None,
        metadata={
            "name": "TemplateInfoUpdate",
            "type": "Element",
        }
    )
    fixed_field_update: Optional[FixedFieldUpdate] = field(
        default=None,
        metadata={
            "name": "FixedFieldUpdate",
            "type": "Element",
        }
    )
    fixed_group_update: Optional[FixedGroupUpdate] = field(
        default=None,
        metadata={
            "name": "FixedGroupUpdate",
            "type": "Element",
        }
    )
    custom_field_add: Optional[CustomFieldAdd] = field(
        default=None,
        metadata={
            "name": "CustomFieldAdd",
            "type": "Element",
        }
    )
    custom_field_update: Optional[CustomFieldUpdate] = field(
        default=None,
        metadata={
            "name": "CustomFieldUpdate",
            "type": "Element",
        }
    )
    custom_field_group_add: Optional[CustomFieldGroupAdd] = field(
        default=None,
        metadata={
            "name": "CustomFieldGroupAdd",
            "type": "Element",
        }
    )
    custom_field_group_update: Optional[CustomFieldGroupUpdate] = field(
        default=None,
        metadata={
            "name": "CustomFieldGroupUpdate",
            "type": "Element",
        }
    )
    endpoint_add: Optional[EndpointAdd] = field(
        default=None,
        metadata={
            "name": "EndpointAdd",
            "type": "Element",
        }
    )
    endpoint_remove: Optional[EndpointRemove] = field(
        default=None,
        metadata={
            "name": "EndpointRemove",
            "type": "Element",
        }
    )
    custom_field_delete: Optional[CustomFieldDelete] = field(
        default=None,
        metadata={
            "name": "CustomFieldDelete",
            "type": "Element",
        }
    )
    custom_field_group_delete: Optional[CustomFieldGroupDelete] = field(
        default=None,
        metadata={
            "name": "CustomFieldGroupDelete",
            "type": "Element",
        }
    )


@dataclass
class TravelerCriteria(TypeAccountTypeProfileSearchCriteria):
    """
    Traveler search modifiers.

    :ivar given_name: Given name wild card
    :ivar surname: Surname wild card
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
        }
    )


@dataclass
class TravelerGroupCriteria(TypeAccountTypeProfileSearchCriteria):
    """
    Traveler Group search modifiers.

    :ivar name: Traveler Group name wild card
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )


@dataclass
class TravelerGroupInfo(TypeAccountTypeProfileInfo):
    """
    Traveler group specific profile information.

    :ivar address: Traveler Group Address
    :ivar phone: Traveler Group Phone Number
    :ivar electronic_address: Traveler Group Electronic Address
    :ivar external_identifier: Traveler Group External Identifier
    :ivar name: Name of the TravelerGroup
    :ivar local_language_name: The name of the TravelerGroup in the
        user's local language.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TravelerInfo(TypeAccountTypeProfileInfo):
    """
    Traveler specific profile information.

    :ivar address: Traveler Address
    :ivar phone: Traveler Phone Number
    :ivar electronic_address: Traveler Electronic Address
    :ivar traveler_identity_information: An additional means to identify
        or verify a travelers profile when then are duplicate traveler
        names.
    :ivar proprietary_data: ProprietaryData for a Traveler which can be
        overridden for immediate parent like BranchGroup,Branch,Account
        and TravelerGroup.
    :ivar passenger_type_code: Three character code representing a
        passenger type. All in the list must be specified on modify to
        keep. Util: ReferenceDataRetrieveReq, TypeCode PassengerTypeCode
    :ivar external_identifier: Traveler External Identifier
    :ivar unique_profile_id: Used as a primary identification for a
        traveler profile. Data transmitted must be unique for each
        traveler profile and will be validated system wide.
    :ivar title: Util: ReferenceDataRetrieveReq, TypeCode
        MiscellaneousTable Category Code Title.
    :ivar nickname:
    :ivar other_name:
    :ivar suffix:
    :ivar birth_date: Date of Birth of Traveler - YYYY-MM-DD
    :ivar gender: Util: ReferenceDataRetrieveReq, TypeCode
        PersonGenderType
    :ivar vip_status:
    :ivar job_title: The job title of the traveler.
    :ivar disability: Text describing a traveler's disability
    :ivar home_city_or_airport: The City or  Airport designated as Home
        for the traveler
    :ivar local_language: A field to identify the Local Language of the
        traveler.  This field references the ISO 639-1 table and the
        IETF BCP 47 list to get languages.  The expected format would be
        a 2 letter language code if coming from the ISO 639-1 table (xx)
        or if coming from the IETF BCP 47 list then it will be a 2
        letter language code followed by a 2 letter qualifier (xx-YY).
    :ivar local_language_given_name:
    :ivar local_language_surname:
    :ivar local_language_username:
    :ivar given_name:
    :ivar surname:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    traveler_identity_information: Optional[TravelerIdentityInformation] = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
        }
    )
    proprietary_data: List[ProprietaryData] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passenger_type_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeCode",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 3,
            "max_length": 5,
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    unique_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Attribute",
            "min_length": 6,
            "max_length": 128,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Attribute",
        }
    )
    gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    vip_status: bool = field(
        default=False,
        metadata={
            "name": "VipStatus",
            "type": "Attribute",
        }
    )
    job_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
    disability: Optional[str] = field(
        default=None,
        metadata={
            "name": "Disability",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    home_city_or_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeCityOrAirport",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    local_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguage",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    local_language_given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageGivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageSurname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_username: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLanguageUsername",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class TypeFormOfPaymentHistory(TypeKeyElement):
    """
    :ivar credit_card:
    :ivar debit_card:
    :ivar certificate_history:
    :ivar ticket_number_history:
    :ivar check:
    :ivar requisition:
    :ivar misc_form_of_payment_history:
    :ivar agency_payment_history:
    :ivar united_nations_history:
    :ivar direct_payment:
    :ivar agent_voucher_history:
    :ivar guarantee:
    :ivar voucher:
    :ivar cash:
    :ivar type_value: The code from the PAYMENT_FORMAT_TYPE_CD (CRECRD,
        DEBDRC, REQSTN…).
    :ivar description: Description of the Payment
    :ivar priority_order: Priority order associated with this
        PaymentDetails.
    :ivar owner_id: Id of the profile who owns the Traveler's
        proprietary data.Should be the immediate parent id of the
        traveler.
    """
    class Meta:
        name = "typeFormOfPaymentHistory"

    credit_card: Optional[TypeCreditCardTypeHistory] = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    debit_card: Optional[TypePaymentCardHistory] = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    certificate_history: Optional[CertificateHistory] = field(
        default=None,
        metadata={
            "name": "CertificateHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    ticket_number_history: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketNumberHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_length": 0,
            "max_length": 13,
        }
    )
    check: Optional[Check] = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    requisition: Optional[Requisition] = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    misc_form_of_payment_history: Optional[MiscFormOfPaymentHistory] = field(
        default=None,
        metadata={
            "name": "MiscFormOfPaymentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    agency_payment_history: Optional[AgencyPaymentHistory] = field(
        default=None,
        metadata={
            "name": "AgencyPaymentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    united_nations_history: Optional[UnitedNationsHistory] = field(
        default=None,
        metadata={
            "name": "UnitedNationsHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    direct_payment: Optional[DirectPayment] = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    agent_voucher_history: Optional[AgentVoucherHistory] = field(
        default=None,
        metadata={
            "name": "AgentVoucherHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    guarantee: Optional[TypeGuaranteeInformationHistory] = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    voucher: Optional[TypeVoucherInformationHistory] = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    cash: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cash",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
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
    priority_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )


@dataclass
class BaseInfo:
    """
    :ivar agency_base_info: Information relating to Agency.
    :ivar branch_base_info: Information relating to Branch.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_base_info: Optional[AgencyBaseInfo] = field(
        default=None,
        metadata={
            "name": "AgencyBaseInfo",
            "type": "Element",
        }
    )
    branch_base_info: Optional[BranchBaseInfo] = field(
        default=None,
        metadata={
            "name": "BranchBaseInfo",
            "type": "Element",
        }
    )


@dataclass
class ProfileData:
    """
    Agency-defined data.

    :ivar agency_group_info:
    :ivar agency_info:
    :ivar branch_group_info:
    :ivar branch_info:
    :ivar account_info:
    :ivar agent_info:
    :ivar traveler_group_info:
    :ivar traveler_info:
    :ivar travel_document:
    :ivar accounting_reference:
    :ivar policy_reference:
    :ivar commission_reference:
    :ivar commission:
    :ivar form_of_payment:
    :ivar air_preference:
    :ivar hotel_preference:
    :ivar rail_preference:
    :ivar other_preference:
    :ivar contract:
    :ivar service_fee:
    :ivar alternate_contact:
    :ivar loyalty_program_enrollment:
    :ivar remark:
    :ivar vehicle_preference:
    :ivar field_data: Data values associated to this entity. Each value
        is linked to a field that defines the structure and restrictions
        of the data.
    :ivar field_group_data: Field groups and child fields and groups and
        their associated data values for this entity. Each field group
        is linked to an instance, which defines the attributes of the
        group specific to the asociated template or its parent field
        group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_group_info: Optional[AgencyGroupInfo] = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
        }
    )
    branch_group_info: Optional[BranchGroupInfo] = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
        }
    )
    branch_info: Optional[BranchInfo] = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
        }
    )
    account_info: Optional[AccountInfo] = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
        }
    )
    agent_info: Optional[AgentInfo] = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
        }
    )
    traveler_group_info: Optional[TravelerGroupInfo] = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
        }
    )
    traveler_info: Optional[TravelerInfo] = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    accounting_reference: List[AccountingReference] = field(
        default_factory=list,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "max_occurs": 20000,
        }
    )
    policy_reference: List[PolicyReference] = field(
        default_factory=list,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission_reference: List[CommissionReference] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_preference: List[AirPreference] = field(
        default_factory=list,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_preference: List[HotelPreference] = field(
        default_factory=list,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_preference: List[RailPreference] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    other_preference: List[OtherPreference] = field(
        default_factory=list,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    service_fee: List[ServiceFee] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact: List[AlternateContact] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    loyalty_program_enrollment: List[LoyaltyProgramEnrollment] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_preference: List[VehiclePreference] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_data: List[FieldData] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group_data: List[FieldGroupData] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileDataUpdate:
    """
    Update some basic information of the profile.

    :ivar agency_group_info:
    :ivar agency_info:
    :ivar branch_group_info:
    :ivar branch_info:
    :ivar agent_info:
    :ivar account_info:
    :ivar traveler_group_info:
    :ivar traveler_info:
    :ivar address: Address belonging to the profile (will be updated in
        the  "Info" elements)
    :ivar phone: Phone Number belonging to the profile (will be updated
        in the  "Info" elements)
    :ivar electronic_address: Electronic Address belonging to the
        profile (will be updated in the  "Info" elements)
    :ivar traveler_identity_information: An additional means to identify
        or verify a travelers profile when then are duplicate traveler
        names.
    :ivar external_identifier: Meant for external identification of a
        Profile. This will be updated in Info element of the Profile.
    :ivar travel_document:
    :ivar accounting_reference:
    :ivar policy_reference:
    :ivar loyalty_program_enrollment:
    :ivar commission:
    :ivar contract:
    :ivar service_fee:
    :ivar alternate_contact:
    :ivar alternate_contact_address:
    :ivar alternate_contact_phone:
    :ivar alternate_contact_electronic_address:
    :ivar form_of_payment:
    :ivar air_preference:
    :ivar hotel_preference:
    :ivar other_preference:
    :ivar remark:
    :ivar field_data: Change the values of existing root-level or child-
        level custom fields. To add a new child field value, use
        FieldData within FieldGroupData. To delete an existing child
        field value, use ProfileDataDelete.
    :ivar field_group_data: Add new child field values or modify
        existing child field values within an existing custom field
        group instance. To delete a field group instance and its child
        field values, use ProfileDataDelete.
    :ivar vehicle_preference:
    :ivar advisory:
    :ivar commission_reference:
    :ivar rail_preference:
    :ivar proprietary_data:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_group_info: Optional[AgencyGroupInfo] = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
        }
    )
    branch_group_info: Optional[BranchGroupInfo] = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
        }
    )
    branch_info: Optional[BranchInfo] = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
        }
    )
    agent_info: Optional[AgentInfo] = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
        }
    )
    account_info: Optional[AccountInfo] = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
        }
    )
    traveler_group_info: Optional[TravelerGroupInfo] = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
        }
    )
    traveler_info: Optional[TravelerInfo] = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: List[Phone] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    electronic_address: List[ElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    traveler_identity_information: Optional[TravelerIdentityInformation] = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
        }
    )
    external_identifier: List[ExternalIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    accounting_reference: List[AccountingReference] = field(
        default_factory=list,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "max_occurs": 20000,
        }
    )
    policy_reference: List[PolicyReference] = field(
        default_factory=list,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    loyalty_program_enrollment: List[LoyaltyProgramEnrollment] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    service_fee: List[ServiceFee] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact: List[AlternateContact] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact_address: List[AlternateContactAddress] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact_phone: List[AlternateContactPhone] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact_electronic_address: List[AlternateContactElectronicAddress] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_preference: List[AirPreference] = field(
        default_factory=list,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    hotel_preference: List[HotelPreference] = field(
        default_factory=list,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    other_preference: List[OtherPreference] = field(
        default_factory=list,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_data: List[FieldData] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group_data: List[FieldGroupData] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    vehicle_preference: List[VehiclePreference] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    advisory: List[Advisory] = field(
        default_factory=list,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission_reference: List[CommissionReference] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    rail_preference: List[RailPreference] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    proprietary_data: List[ProprietaryData] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileSummary:
    """Profile summary information.

    The data returned is what was matched from the search request plus a
    subset of required identification info.

    :ivar agency_group_info:
    :ivar agency_info:
    :ivar branch_group_info:
    :ivar branch_info:
    :ivar agent_info:
    :ivar account_info:
    :ivar traveler_group_info:
    :ivar traveler_info:
    :ivar immediate_parent_profile:
    :ivar contract: The contract number matched in the search.
    :ivar alternate_contact: The contact matched in the search.
    :ivar travel_document: The travel document number matched in the
        search.
    :ivar accounting_reference: The accounting reference matched in the
        search.
    :ivar policy_reference: The policy reference matched in the search.
    :ivar loyalty_program_enrollment: The loyalty program matched in the
        search.
    :ivar form_of_payment:
    :ivar field_data: The custom fields matched in the search.
    :ivar field_group_data: The custom fields groups matched in the
        search.
    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar status: Profile status (Active, Inactive).
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar version: Version number of the profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_group_info: Optional[AgencyGroupInfo] = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
        }
    )
    agency_info: Optional[AgencyInfo] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
        }
    )
    branch_group_info: Optional[BranchGroupInfo] = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
        }
    )
    branch_info: Optional[BranchInfo] = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
        }
    )
    agent_info: Optional[AgentInfo] = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
        }
    )
    account_info: Optional[AccountInfo] = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
        }
    )
    traveler_group_info: Optional[TravelerGroupInfo] = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
        }
    )
    traveler_info: Optional[TravelerInfo] = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
        }
    )
    immediate_parent_profile: List["ProfileSummary.ImmediateParentProfile"] = field(
        default_factory=list,
        metadata={
            "name": "ImmediateParentProfile",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    alternate_contact: List[AlternateContact] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    accounting_reference: List[AccountingReference] = field(
        default_factory=list,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "max_occurs": 20000,
        }
    )
    policy_reference: List[PolicyReference] = field(
        default_factory=list,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    loyalty_program_enrollment: List[LoyaltyProgramEnrollment] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_data: List[FieldData] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group_data: List[FieldGroupData] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    status: Optional[TypeProfileEntityStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )

    @dataclass
    class ImmediateParentProfile:
        """
        :ivar immediate_parent_ref: System-defined, unique identifier
            for ImmediateParent Reference
        :ivar control_branch: If immediate parent is a control branch,
            it will be true other wise doesn't show this attribute.
        """
        immediate_parent_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ImmediateParentRef",
                "type": "Attribute",
            }
        )
        control_branch: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ControlBranch",
                "type": "Attribute",
            }
        )


@dataclass
class ProfileTemplate:
    """
    Template for a profile.

    :ivar fixed_field_group:
    :ivar custom_field:
    :ivar custom_field_group:
    :ivar override_definition:
    :ivar id: Unique identifier of the template, defined by the system.
    :ivar name: Name for the template.
    :ivar description: Description of the template and its use.
    :ivar version: Version of the template.
    :ivar base_template_id: Presence of base template id  indicate that
        current templat e is a override template and is created based on
        "BaseTemplateID".
    :ivar owner_profile_id: Presence of owner profile id indicates by
        which profile this template is been owned
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    fixed_field_group: List[FixedFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FixedFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    custom_field: List[CustomField] = field(
        default_factory=list,
        metadata={
            "name": "CustomField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    custom_field_group: List[CustomFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "CustomFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    override_definition: List[OverrideDefinition] = field(
        default_factory=list,
        metadata={
            "name": "OverrideDefinition",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
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
            "max_length": 225,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    base_template_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "BaseTemplateID",
            "type": "Attribute",
        }
    )
    owner_profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "OwnerProfileID",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileTypeSearch:
    """
    Specifies which type of profile to be searched on and includes modifiers for
    each type.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_group_criteria: Optional[AgencyGroupCriteria] = field(
        default=None,
        metadata={
            "name": "AgencyGroupCriteria",
            "type": "Element",
        }
    )
    agency_criteria: Optional[AgencyCriteria] = field(
        default=None,
        metadata={
            "name": "AgencyCriteria",
            "type": "Element",
        }
    )
    branch_criteria: Optional[BranchCriteria] = field(
        default=None,
        metadata={
            "name": "BranchCriteria",
            "type": "Element",
        }
    )
    branch_group_criteria: Optional[BranchGroupCriteria] = field(
        default=None,
        metadata={
            "name": "BranchGroupCriteria",
            "type": "Element",
        }
    )
    agent_criteria: Optional[AgentCriteria] = field(
        default=None,
        metadata={
            "name": "AgentCriteria",
            "type": "Element",
        }
    )
    account_criteria: Optional[AccountCriteria] = field(
        default=None,
        metadata={
            "name": "AccountCriteria",
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
    traveler_group_criteria: Optional[TravelerGroupCriteria] = field(
        default=None,
        metadata={
            "name": "TravelerGroupCriteria",
            "type": "Element",
        }
    )


@dataclass
class TypeHistorySubElement:
    """
    A choice of all fields that have changed in the course of a add, modified, or
    deleted.
    """
    class Meta:
        name = "typeHistorySubElement"

    account_info: Optional[TypeAccountInfoHistory] = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    traveler_info: Optional[TypeTravelerInfoHistory] = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    travel_document: Optional[TypeTravelDocumentHistory] = field(
        default=None,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    accounting_reference: Optional[TypeAccountingReferenceHistory] = field(
        default=None,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    policy_reference: Optional[TypePolicyReferenceHistory] = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    commission_reference: Optional[TypeCommissionReferenceHistory] = field(
        default=None,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    loyalty_program_enrollment: Optional[TypeLoyaltyProgramEnrollmentHistory] = field(
        default=None,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    contract: Optional[TypeContractHistory] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    commission: Optional[TypeCommissionHistory] = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    service_fee: Optional[TypeServiceFeeHistory] = field(
        default=None,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    alternate_contact: Optional[TypeAlternateContactHistory] = field(
        default=None,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    alternate_contact_address: Optional["TypeHistorySubElement.AlternateContactAddress"] = field(
        default=None,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    alternate_contact_phone: Optional["TypeHistorySubElement.AlternateContactPhone"] = field(
        default=None,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    alternate_contact_electronic_address: Optional["TypeHistorySubElement.AlternateContactElectronicAddress"] = field(
        default=None,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    form_of_payment: Optional[TypeFormOfPaymentHistory] = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    remark: Optional[TypeRemarkHistory] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    address: Optional[TypeAddressHistory] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    phone: Optional[TypePhoneHistory] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    electronic_address: Optional[TypeElectronicAddressHistory] = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    traveler_identity_information: Optional[TravelerIdentityInformation] = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    external_identifier: Optional[TypeExternalIdentifierHistory] = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    air_preference: Optional[TypeAirPreferenceHistory] = field(
        default=None,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    vehicle_preference: Optional[TypeVehiclePreferenceHistory] = field(
        default=None,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    hotel_preference: Optional[TypeHotelPreferenceHistory] = field(
        default=None,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    rail_preference: Optional[TypeRailPreferenceHistory] = field(
        default=None,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    profile_parent_history: Optional[TypeProfileParentHistory] = field(
        default=None,
        metadata={
            "name": "ProfileParentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    field_data: Optional[TypeFieldDataHistory] = field(
        default=None,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    field_group_data: Optional[TypeFieldGroupDataHistory] = field(
        default=None,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    advisory: Optional[TypeAdvisoryHistory] = field(
        default=None,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    agency_group_info: Optional[TypeAgencyGroupInfoHistory] = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    agency_info: Optional[TypeAgencyInfoHistory] = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    branch_group_info: Optional[TypeBranchGroupInfoHistory] = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    branch_info: Optional[TypeBranchInfoHistory] = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    agent_info: Optional[TypeAgentInfoHistory] = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    traveler_group_info: Optional[TypeTravelerGroupInfoHistory] = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    profile_status: Optional[TypeProfileStatusHistory] = field(
        default=None,
        metadata={
            "name": "ProfileStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    profile_link: Optional[TypeProfileLinkHistory] = field(
        default=None,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    provider_info: Optional[TypeProviderInfoHistory] = field(
        default=None,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    other_preference: Optional[TypeOtherPreferenceHistory] = field(
        default=None,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    proprietary_data: Optional[TypeProprietaryDataHistory] = field(
        default=None,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )

    @dataclass
    class AlternateContactAddress(TypeAddressHistory):
        """
        :ivar alternate_contact_ref: A reference to the Alternate
            Contact being that is the parent of this element.
        """
        alternate_contact_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "AlternateContactRef",
                "type": "Attribute",
            }
        )

    @dataclass
    class AlternateContactPhone(TypePhoneHistory):
        """
        :ivar alternate_contact_ref: A reference to the Alternate
            Contact being that is the parent of this element.
        """
        alternate_contact_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "AlternateContactRef",
                "type": "Attribute",
            }
        )

    @dataclass
    class AlternateContactElectronicAddress(TypeElectronicAddressHistory):
        """
        :ivar alternate_contact_ref: A reference to the Alternate
            Contact being that is the parent of this element.
        """
        alternate_contact_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "AlternateContactRef",
                "type": "Attribute",
            }
        )


@dataclass
class HistoryElement:
    """
    The history of a particular element at a particular point in time.

    :ivar original: The orignal values of the element before the change.
    :ivar new: The new updated values of the element.
    :ivar action: The action made on the element.
    :ivar modified_by_agent_id: Agent who modified this element
    :ivar modified_by_agent_user_name: Agent who last modified the
        profile
    :ivar modified_date: When this element was modified
    :ivar component: The corresponding name of the element that this
        field refers to in the profile message. This is a read only
        attribute.
    :ivar correlation_element: The name of an attribute on the profile
        element that defines a "type".  This is a read-only attribute.
    :ivar correlation_value: The value that should be put in the
        attribute that the CorrelationElement defines.  This is a read-
        only attribute.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    original: Optional[TypeHistorySubElement] = field(
        default=None,
        metadata={
            "name": "Original",
            "type": "Element",
        }
    )
    new: Optional[TypeHistorySubElement] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
        }
    )
    action: Optional[TypeAction] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_by_agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ModifiedByAgentID",
            "type": "Attribute",
            "required": True,
        }
    )
    modified_by_agent_user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModifiedByAgentUserName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )
    modified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    component: Optional[str] = field(
        default=None,
        metadata={
            "name": "Component",
            "type": "Attribute",
            "required": True,
            "max_length": 50,
        }
    )
    correlation_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrelationElement",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    correlation_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrelationValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class ProfileModifyCmd:
    """
    Wrapper for a set of modification commands to be applied to this profile.

    :ivar profile_status_update:
    :ivar profile_link_add: Add a new link between this profile and the
        specific profile.
    :ivar profile_link_delete: Delete the link between this profile and
        the specificied profile.
    :ivar profile_parent_add: Command to add a new parent profile.
        Either ProvisioningCode or ProfileID are required.
    :ivar profile_parent_delete: Command to delete a parent profile.
        Either ProvisioningCode or ProfileID are required.
    :ivar profile_data_add:
    :ivar profile_data_update:
    :ivar profile_data_delete:
    :ivar tag_add:
    :ivar tag_delete:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_status_update: Optional[ProfileStatusUpdate] = field(
        default=None,
        metadata={
            "name": "ProfileStatusUpdate",
            "type": "Element",
        }
    )
    profile_link_add: Optional[ProfileLinkAdd] = field(
        default=None,
        metadata={
            "name": "ProfileLinkAdd",
            "type": "Element",
        }
    )
    profile_link_delete: Optional[ProfileLinkDelete] = field(
        default=None,
        metadata={
            "name": "ProfileLinkDelete",
            "type": "Element",
        }
    )
    profile_parent_add: Optional[ProfileParentAdd] = field(
        default=None,
        metadata={
            "name": "ProfileParentAdd",
            "type": "Element",
        }
    )
    profile_parent_delete: Optional[ProfileParentDelete] = field(
        default=None,
        metadata={
            "name": "ProfileParentDelete",
            "type": "Element",
        }
    )
    profile_data_add: Optional[ProfileDataAdd] = field(
        default=None,
        metadata={
            "name": "ProfileDataAdd",
            "type": "Element",
        }
    )
    profile_data_update: Optional[ProfileDataUpdate] = field(
        default=None,
        metadata={
            "name": "ProfileDataUpdate",
            "type": "Element",
        }
    )
    profile_data_delete: Optional[ProfileDataDelete] = field(
        default=None,
        metadata={
            "name": "ProfileDataDelete",
            "type": "Element",
        }
    )
    tag_add: Optional[TagAdd] = field(
        default=None,
        metadata={
            "name": "TagAdd",
            "type": "Element",
        }
    )
    tag_delete: Optional[TagDelete] = field(
        default=None,
        metadata={
            "name": "TagDelete",
            "type": "Element",
        }
    )


@dataclass
class TypeProfileParentWithData:
    """
    A parent's profile, including the profile data (if specified in the request)
    and a list of its parents as well.

    :ivar base_info: A parent's basic data returned regardless of the
        inheritability settings in the template for the individual
        elements.
    :ivar profile_parent:
    :ivar profile_data: The Profile Data for the parent.  It is returned
        if specified in the request.
    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar name: The name of the profile. Either the the organization
        name, or the concatenated title, first, last, and suffix names
        of a profile representing a person (agent or traveler).
    :ivar status: Profile status (Active, Inactive,Deleted).Profile with
        deleted status will be sent only to Sureware for sync
        functionality.
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar version: Version number of the profile.
    :ivar template_id: The unique ID of the profile template associated
        to this entity. Cannot be modified after the profile is created.
    :ivar template_version: The current version number of the template.
    """
    class Meta:
        name = "typeProfileParentWithData"

    base_info: Optional[BaseInfo] = field(
        default=None,
        metadata={
            "name": "BaseInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    profile_parent: Optional["ProfileParent"] = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    profile_data: Optional[ProfileData] = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
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
    status: Optional[TypeProfileEntityStatusWithDelete] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    template_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
        }
    )
    template_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )


@dataclass
class ProfileHistory:
    """
    The profile history.

    :ivar history_element:
    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar profile_name: The name of the profile. Either the the
        organization name, or the concatenated first and last names of a
        profile representing a person (agent or traveler).
    :ivar created_by_agent_id: Agent who created the Profile
    :ivar created_by_agent_user_name: Agent who created the Profile
    :ivar created_date: Date that the profile was created
    :ivar last_modified_by_agent_id: Agent who last modified the profile
    :ivar last_modified_by_agent_user_name: Agent who last modified the
        profile
    :ivar last_modified_date: The date that the profile was last
        modified
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    history_element: List[HistoryElement] = field(
        default_factory=list,
        metadata={
            "name": "HistoryElement",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_name: Optional[object] = field(
        default=None,
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
            "required": True,
        }
    )
    created_by_agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CreatedByAgentID",
            "type": "Attribute",
        }
    )
    created_by_agent_user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedByAgentUserName",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )
    created_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        }
    )
    last_modified_by_agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastModifiedByAgentID",
            "type": "Attribute",
        }
    )
    last_modified_by_agent_user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastModifiedByAgentUserName",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )
    last_modified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastModifiedDate",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileParent(TypeProfileParentWithData):
    """
    A parent's profile, including the profile data (if specified in the request)
    and a list of its parents as well.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Profile:
    """
    Profile information.

    :ivar profile_data: Profile data.
    :ivar profile_link: A one way relationship between this profile and
        another.
    :ivar profile_parent: A nested Profile can have a parent.  Traveler
        Profiles can have multiple parents.  AgencyGroup profiles will
        have none. This will include all elements up to the root.
    :ivar profile_parent_summary: Summary of this profile parents up to
        the root.
    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar profile_type: The type of profile this profile is for (e.g.,
        branch, account, traveler). The profile type identifies which
        default attributes/elements (minimum data set) the system will
        insert.
    :ivar name: The name of the profile. Either the the organization
        name, or the concatenated title, first, last, and suffix names
        of a profile representing a person (agent or traveler).
    :ivar status: Profile status (Active, Inactive,Deleted).Profile with
        deleted status will be sent only to Sureware for sync
        functionality.
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar version: Version number of the profile.
    :ivar template_id: The unique ID of the profile template associated
        to this entity. Cannot be modified after the profile is created.
    :ivar template_version: The current version number of the template.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_data: Optional[ProfileData] = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
        }
    )
    profile_link: List[ProfileLink] = field(
        default_factory=list,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_parent: Optional[ProfileParent] = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
        }
    )
    profile_parent_summary: List[ProfileParentSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParentSummary",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
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
    status: Optional[TypeProfileEntityStatusWithDelete] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    template_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateID",
            "type": "Attribute",
        }
    )
    template_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "TemplateVersion",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
