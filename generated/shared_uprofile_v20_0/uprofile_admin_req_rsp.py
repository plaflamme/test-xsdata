from dataclasses import dataclass, field
from typing import List, Optional
from generated.shared_uprofile_v20_0.uprofile_shared import (
    CreateField,
    CreateFieldGroup,
    Field,
    FieldGroup,
    MetaData,
    MetaDataModifyCmd,
    ModifyField,
    ModifyFieldGroup,
    ModifyTag,
    Profile,
    ProfileDataFilter,
    ProfileHistory,
    ProfileHistoryRetrieveCriteria,
    ProfileSearchModifiers,
    ProvisioningCodeProfileType,
    Tag,
    TagRef,
    UniqueProfileIdProfileType,
    TypeProfileType as SharedV20SharedTypeProfileType,
)
from generated.uprofile_common_v30_0.uprofile_common import TypeProfileType as CommonV30CommonTypeProfileType
from generated.uprofile_common_v30_0.uprofile_common_req_rsp import (
    BaseReq,
    BaseRsp,
    TypeParentProfileLevel,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileCreateFieldReq(BaseReq):
    """
    Creates one or multiple custom fields and/or field groups.

    :ivar create_field: Defines the attributes of a new custom field.
    :ivar create_field_group: Defines the attributes and structure of a
        new custom field group, and the custom fields that belong to it.
    :ivar profile_id: The ID of the agency or account profile that will
        own the field(s) and group(s) to be created.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    create_field: List[CreateField] = field(
        default_factory=list,
        metadata={
            "name": "CreateField",
            "type": "Element",
        }
    )
    create_field_group: List[CreateFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "CreateFieldGroup",
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


@dataclass
class ProfileCreateFieldRsp(BaseRsp):
    """
    Response containing details of new fields and/or groups created.

    :ivar field_value: Defines a field.
    :ivar field_group: Defines a field group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
        }
    )
    field_group: List[FieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
        }
    )


@dataclass
class ProfileCreateTagsReq(BaseReq):
    """
    Request to create tags for an agency.

    :ivar create_tag:
    :ivar agency_id: The ID of the agency that the tags are created for.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    create_tag: List["ProfileCreateTagsReq.CreateTag"] = field(
        default_factory=list,
        metadata={
            "name": "CreateTag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
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
    class CreateTag:
        """
        :ivar name: The name given to the tag
        :ivar label: The alternate name given to the tag
        :ivar description: The description of the tag
        :ivar display_order: The display order of the tag
        """
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


@dataclass
class ProfileCreateTagsRsp(BaseRsp):
    """
    Response with all the tags for the agency.

    :ivar tag: A tag that belongs to the agency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )


@dataclass
class ProfileDeleteTagReq(BaseReq):
    """
    Request to delete tags.

    :ivar tag_ref: The tag to be deleted
    :ivar override: Indicator to override the delete when the tag is "in
        use" by profiles in the agency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    tag_ref: Optional[TagRef] = field(
        default=None,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "required": True,
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "name": "Override",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileDeleteTagRsp(BaseRsp):
    """
    Successful Response that the tag has been deleted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileModifyFieldReq(BaseReq):
    """Modifies a custom field or field group.

    Note that some modifications are not permitted once a field or field
    group is in use (i.e., is associated to a template).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    modify_field: List[ModifyField] = field(
        default_factory=list,
        metadata={
            "name": "ModifyField",
            "type": "Element",
        }
    )
    modify_field_group: List[ModifyFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "ModifyFieldGroup",
            "type": "Element",
        }
    )


@dataclass
class ProfileModifyFieldRsp(BaseRsp):
    """
    Response reflecting changes made to the custom field or field group.

    :ivar field_value: Defines a field.
    :ivar field_group: Defines a field group.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
        }
    )
    field_group: List[FieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
        }
    )


@dataclass
class ProfileModifyTagsReq(BaseReq):
    """
    Request to modify tags for an agency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    modify_tag: List[ModifyTag] = field(
        default_factory=list,
        metadata={
            "name": "ModifyTag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )


@dataclass
class ProfileModifyTagsRsp(BaseRsp):
    """
    Response with the modified tags.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    tag: List["ProfileModifyTagsRsp.Tag"] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 15,
        }
    )

    @dataclass
    class Tag:
        """
        :ivar name: The name given to the tag
        :ivar label: The alternate name given to the tag
        :ivar description: The description of the tag
        :ivar display_order: The display order of the tag
        :ivar id: The unique identifier of the tag.
        :ivar agency_id: The agency that owns the tag
        """
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
class ProfileRetrieveHistoryReq(BaseReq):
    """
    Request to retrieve history for the whole profile, a particular element, or a
    date range.

    :ivar profile_id: Specify the unique ID of the profile whose history
        is being retrieved.
    :ivar profile_history_retrieve_criteria:
    :ivar profile_search_modifiers:
    :ivar show_data_unmasked: Set to true to show data unmasked in the
        profile history retrieve response. Requires special
        authorization.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "required": True,
        }
    )
    profile_history_retrieve_criteria: Optional[ProfileHistoryRetrieveCriteria] = field(
        default=None,
        metadata={
            "name": "ProfileHistoryRetrieveCriteria",
            "type": "Element",
        }
    )
    profile_search_modifiers: Optional[ProfileSearchModifiers] = field(
        default=None,
        metadata={
            "name": "ProfileSearchModifiers",
            "type": "Element",
        }
    )
    show_data_unmasked: bool = field(
        default=False,
        metadata={
            "name": "ShowDataUnmasked",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileRetrieveHistoryRsp(BaseRsp):
    """
    Response with the profile history filtered as specified in the request.

    :ivar profile_history:
    :ivar more_results: Indicates whether more results are available
        that match the search parameters.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_history: Optional[ProfileHistory] = field(
        default=None,
        metadata={
            "name": "ProfileHistory",
            "type": "Element",
            "required": True,
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
class ProfileRetrieveParentReq(BaseReq):
    """
    Service to retrieve parent data.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve ,modify and delete a
        traveler profile. Can be used in place of the ProfileID. Cannot
        be used with ProfileParentAdd, ProfileParentDelete or
        ProfileChildSearch.
    :ivar profile_data_filter:
    :ivar parent_profile_id: Unique ID of the Parent profile for which
        the data will be returned.
    :ivar parent_summary: If specified ‘true’ then it just returns the
        summary information of profile's parents.  If it is false, then
        it returns the entire hierarchy.
    :ivar show_data_unmasked: Set to true to show in the response all
        data in the requested profile, without masking applied. (Any
        such data in parent profiles will still be masked.) Requires
        special authorization.
    :ivar parent_level_to_return: Returns parent’s data up to specified
        hierarchy. Valid values are ‘Agency’, ‘AgencyGroup’,
        ‘BranchGroup’, ‘Branch’, ‘Account’ and ‘Traveler Group’.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
        }
    )
    provisioning_code: Optional["ProfileRetrieveParentReq.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileRetrieveParentReq.UniqueProfileId"] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        }
    )
    profile_data_filter: Optional[ProfileDataFilter] = field(
        default=None,
        metadata={
            "name": "ProfileDataFilter",
            "type": "Element",
        }
    )
    parent_profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentProfileID",
            "type": "Attribute",
        }
    )
    parent_summary: bool = field(
        default=False,
        metadata={
            "name": "ParentSummary",
            "type": "Attribute",
        }
    )
    show_data_unmasked: bool = field(
        default=False,
        metadata={
            "name": "ShowDataUnmasked",
            "type": "Attribute",
        }
    )
    parent_level_to_return: TypeParentProfileLevel = field(
        default=TypeParentProfileLevel.AGENCY,
        metadata={
            "name": "ParentLevelToReturn",
            "type": "Attribute",
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
class ProfileRetrieveParentRsp(BaseRsp):
    """
    Response of parent profile data.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile: Optional[Profile] = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProfileSearchFieldReq(BaseReq):
    """
    Request to retrieve the fields and field groups owned by a specified agency.

    :ivar profile_search_modifiers:
    :ivar profile_id: The ID of the agency or account that owns the
        fields/groups to be retrieved.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_search_modifiers: Optional[ProfileSearchModifiers] = field(
        default=None,
        metadata={
            "name": "ProfileSearchModifiers",
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


@dataclass
class ProfileSearchFieldRsp(BaseRsp):
    """
    Response showing details of the requested field or field group.

    :ivar field_value:
    :ivar field_group: Defines the structure of a field group, which can
        be based on existing fields and groups (referred to by Id)
        and/or new fields and groups (referred to by FieldGroupRef or
        FieldRef and defined in FieldList or FieldGroupList).
    :ivar more_results: Indicates whether more results are available
        that match the search parameters.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
        }
    )
    field_group: List[FieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
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
class ProfileSearchTagsReq(BaseReq):
    """
    Request to retrieve tags for an agency.

    :ivar agency_id: The ID of the agency that the tags belong to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    agency_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileSearchTagsRsp(BaseRsp):
    """
    Response with all the tags for the agency.

    :ivar tag: A tag that belongs to the agency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
            "max_occurs": 15,
        }
    )


@dataclass
class SingleProfileMigrationReq(BaseReq):
    """
    Request to initiate the migration process of a single Account or Traveler
    profile from host to uProfile.

    :ivar external_system: ExternalSystem to indicate the origin  system
        of profile. Currently supported for 1G,1V. Future enhancement
        may include TDS, CSV, 1P.
    :ivar profile_type: The type of the Profile to be migrated.e.g-
        Account , Traveler
    :ivar pcc: The PCC of the Profile to be migrated.
    :ivar account_profile_title: Account Profile Title which need to be
        migrated.
    :ivar traveler_profile_title: Traveler Profile Title which need to
        be migrated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    external_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalSystem",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        }
    )
    profile_type: Optional[CommonV30CommonTypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    pcc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        }
    )
    account_profile_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountProfileTitle",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        }
    )
    traveler_profile_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelerProfileTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )


@dataclass
class SingleProfileMigrationRsp(BaseRsp):
    """
    Response of migration process of a single Account or Traveler profile from host
    to uProfile.

    :ivar profile_id: The system-assigned, unique ID of the profile.
    :ivar status: Status of the migration process.
    :ivar profile_type: The type of the migrated Profile
        e.g-Account,Traveler
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
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
    profile_type: Optional[CommonV30CommonTypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
        }
    )


@dataclass
class UimetaDataCreateReq(BaseReq):
    """
    Service for Request to create the entry in action by Admin in Admin login view
    in Profile Settings.

    :ivar meta_data: An element created under the service which will
        store all settings for the selected profile.
    :ivar profile_id: This attribute would pass the ID of the required
        profile selected(say, Agency or Account name) for which the
        change in setting will be done.
    :ivar description: This optional attribute is for any description if
        the user wants to pass.
    """
    class Meta:
        name = "UIMetaDataCreateReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
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
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class UimetaDataCreateRsp(BaseRsp):
    """
    Service for Response to create the entry in action by Admin in Admin login view
    in Profile Settings.

    :ivar meta_data: An element created under the service which will
        store all settings for the selected profile.
    :ivar profile_id: This Profile Id would get the ID of the
        Agency/Account name for which the change is done. Hence all the
        applicable changes would be done for this particular
        agency/account.
    :ivar profile_type: This will retrieve the type of the Profile for
        which the change is triggered, say Agency , Account, etc.
    :ivar meta_data_version: This attribute updates the version of the
        change or any updates done.
    :ivar description: This optional attribute is for any description if
        the user wants to pass.
    """
    class Meta:
        name = "UIMetaDataCreateRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
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
    profile_type: Optional[SharedV20SharedTypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    meta_data_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "MetaDataVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class UimetaDataDeleteReq(BaseReq):
    """
    Service for Request to delete any settings by user in Profile Settings.

    :ivar profile_id: This attribute would pass the ID of the required
        profile selected (say, Agency or Account name) for which the
        change in settings will be done.
    """
    class Meta:
        name = "UIMetaDataDeleteReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UimetaDataDeleteRsp(BaseRsp):
    """
    Service for Response to delete any settings by user in Profile Settings.
    """
    class Meta:
        name = "UIMetaDataDeleteRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class UimetaDataModifyReq(BaseReq):
    """
    Service for Request to modify the entry in action by Admin in Admin login view
    in Profile Settings.

    :ivar meta_data_modify_cmd:
    :ivar profile_id: This attribute would pass the ID of the required
        profile selected(say, Agency or Account name) for which change
        in the settings will be done.
    :ivar meta_data_version: This attribute updates the version of the
        change or any updates done.
    :ivar description: This optional attribute is for any description if
        the user wants to pass.
    """
    class Meta:
        name = "UIMetaDataModifyReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data_modify_cmd: List[MetaDataModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "MetaDataModifyCmd",
            "type": "Element",
            "min_occurs": 1,
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
    meta_data_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "MetaDataVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class UimetaDataModifyRsp(BaseRsp):
    """
    Service for Response to modify the entry in action by Admin in Admin login view
    in Profile Settings.

    :ivar meta_data: Stores the MetaData details of the applicable
        profile.
    :ivar profile_id: This Profile Id would get the ID of the
        Agency/Account name for which the change is done. Hence all the
        applicable changes would be done for this particular
        agency/account.
    :ivar profile_type: This will retrieve the type of the Profile for
        which the change is triggered, say Agency , Account, etc.
    :ivar meta_data_version: This attribute updates the version of the
        change or any updates done.
    :ivar description: This optional attribute is for any description if
        the user wants to pass.
    """
    class Meta:
        name = "UIMetaDataModifyRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
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
    profile_type: Optional[SharedV20SharedTypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    meta_data_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "MetaDataVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class UimetaDataRetrieveReq(BaseReq):
    """
    Service for Request to retrieve the settings by user in Profile Settings.

    :ivar profile_id: This attribute would pass the ID of the required
        profile selected(say, Agency or Account name) for which the
        change in settings will be done.
    """
    class Meta:
        name = "UIMetaDataRetrieveReq"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UimetaDataRetrieveRsp(BaseRsp):
    """
    Service for Response to retrieve the settings by user in Profile Settings.

    :ivar meta_data: An element created under the service which will
        store all settings for the selected profile.
    :ivar profile_id: This Profile Id would get the ID of the
        Agency/Account name for which the change is done. Hence all the
        applicable changes would be done for this particular
        agency/account.
    :ivar profile_type: This will retrieve the type of the Profile for
        which the change is triggered, say Agency , Account, etc.
    :ivar meta_data_version: This attribute updates the version of the
        change or any updates done.
    :ivar description: This optional attribute is for any description if
        the user wants to pass.
    """
    class Meta:
        name = "UIMetaDataRetrieveRsp"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
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
    profile_type: Optional[SharedV20SharedTypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    meta_data_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "MetaDataVersion",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
