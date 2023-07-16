from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from generated.common_v37_0.common import TypeProfileType as CommonCommonTypeProfileType
from generated.common_v37_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)
from generated.uprofile_v37_0.uprofile import (
    Action,
    ActionSummary,
    BridgeBranch,
    BridgeBranchCmd,
    CreateField,
    CreateFieldGroup,
    Field,
    FieldGroup,
    HierarchyLevel,
    ModifyField,
    ModifyFieldGroup,
    ModifyTag,
    ProfileChildSummary,
    ProfileHistory,
    ProfileHistoryRetrieveCriteria,
    ProfileSearchModifiers,
    ProfileTemplate,
    ProvisioningCodeProfileType,
    Tag,
    TagRef,
    TemplateModifyCmd,
    UniqueProfileIdProfileType,
    TypeActionRef,
    TypeCreateHierarchyLevel,
    TypeDeleteHierarchyLvlProfileType,
    TypeProfileType as UprofileUprofileTypeProfileType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


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
    :ivar unique_profile_id: Applicable to retrieve, modify and delete a
        traveler profile. Combination of UniqueProfileID and AgencyCode
        can be used in place of Profile ID. Cannot be used with
        ProfileParentAdd, ProfileParentDelete or ProfileChildSearch.
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_child_summary: List[ProfileChildSummary] = field(
        default_factory=list,
        metadata={
            "name": "ProfileChildSummary",
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
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Attribute",
        }
    )


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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    create_field: List[CreateField] = field(
        default_factory=list,
        metadata={
            "name": "CreateField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    create_field_group: List[CreateFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "CreateFieldGroup",
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


@dataclass
class ProfileCreateFieldRsp(BaseRsp):
    """
    Response containing details of new fields and/or groups created.

    :ivar field_value: Defines a field.
    :ivar field_group: Defines a field group.
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
    field_group: List[FieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileCreateHierarchyLevelReq(BaseReq):
    """Request to create a new level within an existing agency or account
    hierarchy.

    The template of the hierarchy level will be auto-generated.

    :ivar parent_hierarchy_level_id: System-assigned, unique hierarchy
        level ID of the immediate parent of this hiearchy level.
        Required unless profile type is AgencyGroup.
    :ivar profile_type: The type of profile this hierarchy level
        corresponds to. Limited to AgencyGroup, BranchGroup and
        TravelerGroup.
    :ivar name: Name of this level of the hierarchy.
    :ivar description: A brief description of this hierarchy level.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    parent_hierarchy_level_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParentHierarchyLevelID",
            "type": "Attribute",
        }
    )
    profile_type: Optional[TypeCreateHierarchyLevel] = field(
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
class ProfileCreateHierarchyLevelRsp(BaseRsp):
    """
    Response with the requested hierarchy structure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level: List[HierarchyLevel] = field(
        default_factory=list,
        metadata={
            "name": "HierarchyLevel",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
class ProfileDeleteHierarchyLevelReq(BaseReq):
    """Request to delete an existing Group level of an agency or account hierarchy.

    Only permitted if no profiles exist for the level.

    :ivar hierarchy_level_id: System-assigned, unique hierarchy level ID
        of the immediate parent of this hiearchy level. Leave blank only
        if profile level is agency group.
    :ivar profile_type: The type of profile hierarchy level corresponds
        which can be deleted (e.g., branchgroup and travelergroup).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[TypeDeleteHierarchyLvlProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileDeleteHierarchyLevelRsp(BaseRsp):
    """
    Response with the updated hierarchy structure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level: List[HierarchyLevel] = field(
        default_factory=list,
        metadata={
            "name": "HierarchyLevel",
            "type": "Element",
            "max_occurs": 999,
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileModifyBridgeBranchesReq(BaseReq):
    """Request to add or delete an Agent's Bridge Branch Assignments.

    The Default branch cannot be modified.  That functionality will only
    be used in the Profile Create and Modify services.

    :ivar agent_id: The system-assigned, unique profile ID of the agent.
    :ivar user_name: The login name of the agent.
    :ivar bridge_branch_cmd: Command to add or remove a Bridge Branch
        assignment
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Element",
        }
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        }
    )
    bridge_branch_cmd: List[BridgeBranchCmd] = field(
        default_factory=list,
        metadata={
            "name": "BridgeBranchCmd",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileModifyBridgeBranchesRsp(BaseRsp):
    """Response to add or delete an Agent's Bridge Branch Assignments.

    Returns the list of bridge branches that the agent is currently
    assigned to.

    :ivar bridge_branch:
    :ivar agent_id: The system-assigned, unique profile ID of the agent.
    :ivar user_name: The login name of the agent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    bridge_branch: List[BridgeBranch] = field(
        default_factory=list,
        metadata={
            "name": "BridgeBranch",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
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


@dataclass
class ProfileModifyFieldReq(BaseReq):
    """Modifies a custom field or field group.

    Note that some modifications are not permitted once a field or field
    group is in use (i.e., is associated to a template).
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
    modify_field_group: List[ModifyFieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "ModifyFieldGroup",
            "type": "Element",
            "max_occurs": 999,
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group: List[FieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileModifyHierarchyLevelReq(BaseReq):
    """
    Request to modify an existing level within an agency or account hierarchy.

    :ivar hierarchy_level_id: System-assigned, unique hierarchy level ID
        of the immediate parent of this hiearchy level. Leave blank only
        if profile level is agency group.
    :ivar profile_type: The type of profile this hierarchy level
        corresponds to (e.g., branch, account, traveler, group).
    :ivar name: Name of this level of the hierarchy.
    :ivar description: A brief description of this hierarchy level.
    :ivar parent_hierarchy_level_id: To swap the order of two Group
        levels, specify the new parent of this level. Only Group levels
        can be reassigned, and can only move up or down one location in
        the overall hierarchy.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: Optional[UprofileUprofileTypeProfileType] = field(
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
            "min_length": 1,
            "max_length": 64,
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
    parent_hierarchy_level_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentHierarchyLevelID",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileModifyHierarchyLevelRsp(BaseRsp):
    """
    Response with the newly modified hierarchy level.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level: List[HierarchyLevel] = field(
        default_factory=list,
        metadata={
            "name": "HierarchyLevel",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileModifyTagsReq(BaseReq):
    """
    Request to modify tags for an agency.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
class ProfileModifyTemplateReq(BaseReq):
    """
    Request to modify template.

    :ivar template_modify_cmd:
    :ivar id: Unique identifier of the template, defined by the system.
    :ivar version: Version number of the template. Required with every
        modify request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    template_modify_cmd: List[TemplateModifyCmd] = field(
        default_factory=list,
        metadata={
            "name": "TemplateModifyCmd",
            "type": "Element",
            "min_occurs": 1,
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
class ProfileModifyTemplateRsp(BaseRsp):
    """
    Response with profile template data.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_template: Optional[ProfileTemplate] = field(
        default=None,
        metadata={
            "name": "ProfileTemplate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProfileRetrieveActionReq(BaseReq):
    """
    Retrieves details of specific Action(s).

    :ivar action_info: Action to retrieve.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    action_info: List[TypeActionRef] = field(
        default_factory=list,
        metadata={
            "name": "ActionInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileRetrieveActionRsp(BaseRsp):
    """
    Response containing details of retrieved action(s).

    :ivar action: Details of each action.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    action: List[Action] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "max_occurs": 999,
        }
    )


@dataclass
class ProfileRetrieveBridgeBranchesReq(BaseReq):
    """
    Request to retrieve an Agent's Bridge Branch Assignments.

    :ivar agent_id: The system-assigned, unique profile ID of the agent.
    :ivar user_name: The login name of the agent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Element",
        }
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class ProfileRetrieveBridgeBranchesRsp(BaseRsp):
    """Response to retreive an Agent's Bridge Branch Assignments.

    Returns the list of bridge branches that the agent is currently
    assigned to.

    :ivar bridge_branch:
    :ivar agent_id: The system-assigned, unique profile ID of the agent.
    :ivar user_name: The login name of the agent.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    bridge_branch: List[BridgeBranch] = field(
        default_factory=list,
        metadata={
            "name": "BridgeBranch",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    agent_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Attribute",
            "required": True,
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


@dataclass
class ProfileRetrieveHierarchyReq(BaseReq):
    """
    Request to retrieve the superset of profile levels within an agency,agency
    group or an account.

    :ivar profile_id: Agency,AgencyGroup or Account in which the
        hierarchy is created.
    :ivar agency_code: Specify the AgencyCode Of the Agency in which the
        hierarchy was created.  Accounts and AgencyGroup do not have
        Provisioning IDs
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
    agency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Element",
            "min_length": 1,
            "max_length": 25,
        }
    )


@dataclass
class ProfileRetrieveHierarchyRsp(BaseRsp):
    """
    Response with the requested hierarchy structure.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    hierarchy_level: List[HierarchyLevel] = field(
        default_factory=list,
        metadata={
            "name": "HierarchyLevel",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
class ProfileRetrieveTemplateReq(BaseReq):
    """Request to retrieve a profile template.

    If version exists, the response will not return the template unless
    there is a mismatch.

    :ivar consuming_system: Filter out actions and endpoints based on
        the consuming system(s)
    :ivar id: Unique identifier of the template, defined by the system.
    :ivar version: Version number of the template.
    :ivar return_override_fields_only: Default=false.By default response
        will return aggregated structure of override plus default
        template.If passed true, only override fields will be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    consuming_system: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConsumingSystem",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 128,
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
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    return_override_fields_only: bool = field(
        default=False,
        metadata={
            "name": "ReturnOverrideFieldsOnly",
            "type": "Attribute",
        }
    )


@dataclass
class ProfileRetrieveTemplateRsp(BaseRsp):
    """Response with profile template data.

    If the version on the request matches the most recent template
    version then the template is not returned.  Otherwise the template
    is returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_template: Optional[ProfileTemplate] = field(
        default=None,
        metadata={
            "name": "ProfileTemplate",
            "type": "Element",
        }
    )


@dataclass
class ProfileSearchActionReq(BaseReq):
    """
    Get summary of all Action(s) available in the system.

    :ivar consuming_system: Action Consuming System (Universal Desktop,
        3rd party system).
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    consuming_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumingSystem",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )


@dataclass
class ProfileSearchActionRsp(BaseRsp):
    """
    Response containing summary of all retrieved action(s).

    :ivar action_summary: Summary of each action.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    action_summary: List[ActionSummary] = field(
        default_factory=list,
        metadata={
            "name": "ActionSummary",
            "type": "Element",
            "max_occurs": 999,
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    field_group: List[FieldGroup] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroup",
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
class ProfileSearchTagsReq(BaseReq):
    """
    Request to retrieve tags for an agency.

    :ivar agency_id: The ID of the agency that the tags belong to.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
    profile_type: Optional[CommonCommonTypeProfileType] = field(
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

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
    profile_type: Optional[CommonCommonTypeProfileType] = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
        }
    )
