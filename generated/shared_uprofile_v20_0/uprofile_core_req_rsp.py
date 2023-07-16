from dataclasses import dataclass, field
from typing import List, Optional
from generated.shared_uprofile_v20_0.uprofile_shared import (
    Profile,
    ProfileData,
    ProfileDataFilter,
    ProfileLink,
    ProfileModifyCmd,
    ProvisioningCodeProfileType,
    UniqueProfileIdProfileType,
    TypeProfileType,
)
from generated.uprofile_common_v30_0.uprofile_common import TypeProfileEntityStatus
from generated.uprofile_common_v30_0.uprofile_common_req_rsp import (
    BaseReq,
    BaseRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


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
    :ivar return_profile: If true, will return basic information with
        the ProfileData element and its associated data.
    :ivar show_data_unmasked: Set to true to show in the response all
        data in the requested profile, without masking applied. (Any
        such data in parent profiles will still be masked.) Requires
        special authorization.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
        :ivar unique_profile_id: Applicable to retrieve ,modify and
            delete a traveler profile. Can be used in place of the
            ProfileID. Cannot be used with ProfileParentAdd,
            ProfileParentDelete or ProfileChildSearch.
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
class ProfileDeleteReq(BaseReq):
    """Request to delete a particular profile.

    Either ProfileID or ProvisioningCode are mandatory.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve ,modify and delete a
        traveler profile. Can be used in place of the ProfileID. Cannot
        be used with ProfileParentAdd, ProfileParentDelete or
        ProfileChildSearch.
    :ivar force: To specify that this is a Force Delete.  With a Force
        Delete, the profile specified and any children below that
        profile will be deleted.
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileModifyReq(BaseReq):
    """Request to add, change, or remove data on a specific profile.

    Either ProfileID or ProvisioningCode are mandatory.

    :ivar profile_id: Specify the Profile ID
    :ivar provisioning_code: Specify the Provisioning Code with the
        profile Type
    :ivar unique_profile_id: Applicable to retrieve ,modify and delete a
        traveler profile. Can be used in place of the ProfileID. Cannot
        be used with ProfileParentAdd, ProfileParentDelete or
        ProfileChildSearch.
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
    :ivar unique_profile_id: Applicable to retrieve ,modify and delete a
        traveler profile. Can be used in place of the ProfileID. Cannot
        be used with ProfileParentAdd, ProfileParentDelete or
        ProfileChildSearch.
    :ivar profile_data_filter:
    :ivar show_data_unmasked: Set to true to show in the response all
        data in the requested profile, without masking applied. (Any
        such data in parent profiles will still be masked.) Requires
        special authorization.
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
class ProfileRetrieveRsp(BaseRsp):
    """
    Response with the profile.
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
