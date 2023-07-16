from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.shared_uprofile_v20_0.uprofile_shared import (
    ProfileChildSummary,
    ProfileParentSearchSummary,
    ProfileSearch,
    ProfileSearchModifiers,
    ProfileSummary,
    ProfileTypeSearch,
    ProvisioningCodeProfileType,
    UniqueProfileIdProfileType,
    TypeProfileType,
)
from generated.uprofile_common_v30_0.uprofile_common_req_rsp import (
    BaseReq,
    BaseRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class ProfileChildSearchReqHierarchyType(Enum):
    AGENCY = "Agency"
    ACCOUNT = "Account"


@dataclass
class ProfileChildSearchReq(BaseReq):
    """
    Request to allow a user to retrieve the immediate children of a given profile.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve ,modify and delete a
        traveler profile. Can be used in place of the ProfileID. Cannot
        be used with ProfileParentAdd, ProfileParentDelete or
        ProfileChildSearch.
    :ivar organization_name: Name of the organization to filter for.
    :ivar given_name:
    :ivar surname:
    :ivar profile_search_modifiers:
    :ivar hierarchy_type: The type of hierarchy in which to search for
        children. If not specified search result will include profiles
        of all types.
    :ivar include_agents_and_travelers: Indicator to include or exclude
        Travelers and Agent profiles when doing a this search.  The
        default is false, no Travelers or Agents will be returned.
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
    provisioning_code: Optional["ProfileChildSearchReq.ProvisioningCode"] = field(
        default=None,
        metadata={
            "name": "ProvisioningCode",
            "type": "Element",
        }
    )
    unique_profile_id: Optional["ProfileChildSearchReq.UniqueProfileId"] = field(
        default=None,
        metadata={
            "name": "UniqueProfileID",
            "type": "Element",
        }
    )
    organization_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganizationName",
            "type": "Element",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Element",
        }
    )
    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
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
    hierarchy_type: Optional[ProfileChildSearchReqHierarchyType] = field(
        default=None,
        metadata={
            "name": "HierarchyType",
            "type": "Attribute",
        }
    )
    include_agents_and_travelers: bool = field(
        default=False,
        metadata={
            "name": "IncludeAgentsAndTravelers",
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
class ProfileChildSearchRsp(BaseRsp):
    """
    Response to allow a user to retrieve the immediate children of a given profile.

    :ivar profile_child_summary: Summary of each Profile Child
    :ivar more_results: Indicates whether more results are available
        that match the search parameters.
    :ivar number_of_children: Total number of children that the profile
        searched under has,
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_child_summary: List[ProfileChildSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileChildSummary",
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
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Attribute",
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_summary: List[ProfileSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileSummary",
            "type": "Element",
        }
    )
    profile_parent_search_summary: List[ProfileParentSearchSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParentSearchSummary",
            "type": "Element",
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
