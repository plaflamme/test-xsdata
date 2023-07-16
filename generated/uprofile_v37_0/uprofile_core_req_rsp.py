from dataclasses import dataclass, field
from typing import List, Optional
from generated.common_v37_0.common import TypeProfileEntityStatus
from generated.common_v37_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)
from generated.uprofile_v37_0.uprofile import (
    Profile,
    ProfileData,
    ProfileDataFilter,
    ProfileLink,
    ProfileModifyCmd,
    ProfileParentSearchSummary,
    ProfileSearch,
    ProfileSearchModifiers,
    ProfileSummary,
    ProfileTypeSearch,
    ProvisioningCodeProfileType,
    UniqueProfileIdProfileType,
    TypeProfileType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileCreateReq(BaseReq):
    """
    Creates a new profile.

    :ivar profile_parent: Most profiles will have a single
        parent.AgencyGroup Profiles will have no parents and Agency
        profile may not have a parent.  This data is not returned in the
        response.
    :ivar profile_data: Profile data.
    :ivar profile_link: A unidirectional link from one profile to
        another.
    :ivar profile_type: The type of the Profile to be created.
    :ivar status: Status of the profile entity (e.g., Active, Inactive).
        Any status other than Active implies that the entity cannot
        perform most transactions.
    :ivar template_id: The unique ID of the profile template associated
        to this entity. Cannot be modified after the profile is created.
    :ivar template_version: The current version number of the template.
    :ivar hierarchy_level_id: System-defined, unique identifier of the
        level in the profile's hierarchy to which this profile is
        associated.
    :ivar return_profile: If true, will return basic information with
        the ProfileData element and its associated data.
    :ivar show_data_unmasked: Set to true to show in the response all
        data in the requested profile, without masking applied. (Any
        such data in parent profiles will still be masked.) Requires
        special authorization.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_parent: Optional["ProfileCreateReq.ProfileParent"] = field(
        default=None,
        metadata={
            "name": "ProfileParent",
            "type": "Element",
        }
    )
    profile_data: Optional[ProfileData] = field(
        default=None,
        metadata={
            "name": "ProfileData",
            "type": "Element",
            "required": True,
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
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    status: TypeProfileEntityStatus = field(
        default=TypeProfileEntityStatus.ACTIVE,
        metadata={
            "name": "Status",
            "type": "Attribute",
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
    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
        }
    )
    return_profile: bool = field(
        default=False,
        metadata={
            "name": "ReturnProfile",
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

    @dataclass
    class ProfileParent:
        """
        :ivar profile_id: Specify the Profile ID
        :ivar provisioning_code: Specify the Provisioning Code with the
            profile Type
        :ivar unique_profile_id: Applicable to retrieve, modify and
            delete a traveler profile. Combination of UniqueProfileID
            and AgencyCode can be used in place of Profile ID. Cannot be
            used with ProfileParentAdd, ProfileParentDelete or
            ProfileChildSearch.
        """
        profile_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "ProfileID",
                "type": "Element",
            }
        )
        provisioning_code: Optional["ProfileCreateReq.ProfileParent.ProvisioningCode"] = field(
            default=None,
            metadata={
                "name": "ProvisioningCode",
                "type": "Element",
            }
        )
        unique_profile_id: Optional["ProfileCreateReq.ProfileParent.UniqueProfileId"] = field(
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
            :ivar profile_type: Specify the Profile Type (limited to
                only the ones where ProvisioningCode is relevant)
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
            :ivar profile_type: Specify the Profile Type (limited to
                only the ones where Profile Identifier is relevant)
            :ivar agency_code: 'AgencyCode' is the Provisioning code of
                the parent Agency. This is an optional attribute and if
                not provided, the system will determine 'AgencyCode' by
                Agent's WAB/target Branch or Agent's agency.
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
class ProfileCreateRsp(BaseRsp):
    """
    Response with the newly created profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile: Optional[Profile] = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProfileDeleteReq(BaseReq):
    """Request to delete a particular profile.

    Either ProfileID or ProvisioningCode are mandatory.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve, modify and delete a
        traveler profile. Combination of UniqueProfileID and AgencyCode
        can be used in place of Profile ID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
    :ivar force: To specify that this is a Force Delete.  With a Force
        Delete, the profile specified and any children below that
        profile will be deleted.
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
    provisioning_code: Optional["ProfileDeleteReq.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileDeleteReq.UniqueProfileId"] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
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
class ProfileDeleteRsp(BaseRsp):
    """
    Response will only include warnings if they exist.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyReq(BaseReq):
    """Request to add, change, or remove data on a specific profile.

    Either ProfileID or ProvisioningCode are mandatory.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve, modify and delete a
        traveler profile. Combination of UniqueProfileID and AgencyCode
        can be used in place of Profile ID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
    :ivar profile_modify_cmd:
    :ivar version: Version number of the profile. Required with every
        modify request.
    :ivar return_profile: If false will only return basic Profile
        information, without the updated profile data. If true, will
        return the entire profile and all its data (including data not
        modified by this transaction).
    :ivar show_data_unmasked: Set to true to show in the response all
        data in the requested profile, without masking applied. (Any
        such data in parent profiles will still be masked.) Requires
        special authorization.
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
    provisioning_code: Optional["ProfileModifyReq.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileModifyReq.UniqueProfileId"] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        }
    )
    profile_modify_cmd: List[ProfileModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "ProfileModifyCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
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
    return_profile: bool = field(
        default=False,
        metadata={
            "name": "ReturnProfile",
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
class ProfileModifyRsp(BaseRsp):
    """
    Response with the newly modified profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile: Optional[Profile] = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
        }
    )


@dataclass
class ProfileRetrieveReq(BaseReq):
    """Request to retrieve a particular profile.

    Either the full parent profiles or a summary can also be requested
    on the response.  Either ProfileID or ProvisioningCode are
    mandatory.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve, modify and delete a
        traveler profile. Combination of UniqueProfileID and AgencyCode
        can be used in place of Profile ID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
    :ivar profile_data_filter:
    :ivar return_parent: If true, the response will include profile
        information from this profile's parents. only inheritable data
        will be returned.
    :ivar return_parent_summary: If true, the response will include
        profile summary information from this profile's parents.
    :ivar show_data_unmasked: Set to true to show in the response all
        data in the requested profile, without masking applied. (Any
        such data in parent profiles will still be masked.) Requires
        special authorization.
    :ivar full_parent_hierarchy: Set to false to show in the response
        only the data upto and including Account, for Traveler and
        TravelerGroup.For Account just it's own Profile will be
        returned.
    :ivar parent_id: For traveler profile retrieve, the specific
        immediate parent from which to return inherited data when
        ReturnParent is true. Ignored otherwise.
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
    provisioning_code: Optional["ProfileRetrieveReq.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileRetrieveReq.UniqueProfileId"] = field(
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
    return_parent: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnParent",
            "type": "Attribute",
        }
    )
    return_parent_summary: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnParentSummary",
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
    full_parent_hierarchy: bool = field(
        default=True,
        metadata={
            "name": "FullParentHierarchy",
            "type": "Attribute",
        }
    )
    parent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentID",
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
class ProfileRetrieveRsp(BaseRsp):
    """
    Response with the profile.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile: Optional[Profile] = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProfileSearchReq(BaseReq):
    """Request to search for profiles of a specified type, within a specified
    parent.

    No more than 5 parameters can be specified for a given search
    request (in addition to ProfileSearchModifiers and a parent ID and
    Type). Returns any profiles that match all the parameters specified.

    :ivar profile_type_search:
    :ivar profile_search:
    :ivar profile_search_modifiers:
    :ivar profile_type: Limit the search to specific profile type.
    :ivar profile_parent_id: The ID of the profile parent or ancestor to
        search within.This will be used to constrain the scope of the
        search to a given account, branch, etc. If none is specified,
        the system will infer the scope based on the user's permissions
        and emulation.
    :ivar return_parent_summary: If true, the response will include
        profile summary information from this profile's parents.
    :ivar search_token: Search token to retrieve search result from
        cache, if present.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_type_search: Optional[ProfileTypeSearch] = field(
        default=None,
        metadata={
            "name": "ProfileTypeSearch",
            "type": "Element",
        }
    )
    profile_search: Optional[ProfileSearch] = field(
        default=None,
        metadata={
            "name": "ProfileSearch",
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
    profile_type: Optional[TypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_parent_id: Optional[object] = field(
        default=None,
        metadata={
            "name": "ProfileParentID",
            "type": "Attribute",
        }
    )
    return_parent_summary: bool = field(
        default=False,
        metadata={
            "name": "ReturnParentSummary",
            "type": "Attribute",
        }
    )
    search_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "SearchToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class ProfileSearchRsp(BaseRsp):
    """
    Response with the profile.

    :ivar profile_summary:
    :ivar profile_parent_search_summary:
    :ivar search_token: Search token generated after caching the
        results. Use this token in ProfileSearchReq to get the same
        result back in future profile search calls, if the cache still
        exists.
    :ivar more_results: Indicates whether more results are available
        that match the search parameters.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_summary: List[ProfileSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileSummary",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_parent_search_summary: List[ProfileParentSearchSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParentSearchSummary",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    search_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "SearchToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
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
