from dataclasses import dataclass, field
from typing import List, Optional
from generated.common_v32_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class BridgedBranch:
    """
    A branch, identified by a branch ID, that an agent, who belongs to another
    branch, is allowed to do work in.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    branch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BranchId",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Password:
    """
    Password Type.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    value: str = field(
        default="",
        metadata={
            "max_length": 32,
        }
    )


@dataclass
class Payload:
    """
    The payload container for the PingReq/Rsp.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    value: str = field(
        default="",
        metadata={
            "max_length": 32768,
        }
    )


@dataclass
class SystemInfo:
    """
    Identifies the type of system and version running.

    :ivar system_type: Identifies whether or not this is a Production or
        Test system.
    :ivar application_version: The running version of the system.
    :ivar description: The description of the system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    system_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemType",
            "type": "Attribute",
            "required": True,
        }
    )
    application_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationVersion",
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
class SystemTime:
    """
    Identifies the time of the system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    value: str = field(
        default=""
    )


@dataclass
class UserId:
    """
    UserId Type.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    value: str = field(
        default="",
        metadata={
            "max_length": 32,
        }
    )


@dataclass
class ExternalCacheAccessReq(BaseReq):
    """
    This is to delete/retrieve an entry from external cache.

    :ivar retrieve_entry: To retrieve a cache entry
    :ivar delete_entry: To delete a cache entry
    :ivar cache_name: Target Cache Name
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    retrieve_entry: List["ExternalCacheAccessReq.RetrieveEntry"] = field(
        default_factory=list,
        metadata={
            "name": "RetrieveEntry",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    delete_entry: List["ExternalCacheAccessReq.DeleteEntry"] = field(
        default_factory=list,
        metadata={
            "name": "DeleteEntry",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    cache_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CacheName",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class RetrieveEntry:
        """
        :ivar key: Cache entry key
        """
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class DeleteEntry:
        """
        :ivar key: Cache entry key
        """
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class ExternalCacheAccessRsp(BaseRsp):
    """
    The response to the CurrencyConversionReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    cache_entry: List["ExternalCacheAccessRsp.CacheEntry"] = field(
        default_factory=list,
        metadata={
            "name": "CacheEntry",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class CacheEntry:
        """
        :ivar value:
        :ivar key: Cache entry key
        """
        value: str = field(
            default="",
            metadata={
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
class PingReq(BaseReq):
    """
    A simple request to test connectivity to the system without imposing any
    actions.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    payload: Optional[str] = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "max_length": 32768,
        }
    )


@dataclass
class PingRsp(BaseRsp):
    """Response to the PingReq.

    Will contain the exact payload (if any) that was sent in
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    payload: Optional[str] = field(
        default=None,
        metadata={
            "name": "Payload",
            "type": "Element",
            "max_length": 32768,
        }
    )


@dataclass
class SystemInfoReq(BaseReq):
    """
    Requests system information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class SystemInfoRsp(BaseRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    system_info: Optional[SystemInfo] = field(
        default=None,
        metadata={
            "name": "SystemInfo",
            "type": "Element",
            "required": True,
        }
    )
    system_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemTime",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TimeReq(BaseReq):
    """
    Requests the time of the system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class TimeRsp(BaseRsp):
    """
    Returns the time of the system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    system_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemTime",
            "type": "Element",
        }
    )
