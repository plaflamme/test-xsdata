from dataclasses import dataclass, field
from typing import List, Optional
from generated.common_v33_0.common import HostToken
from generated.common_v33_0.common_req_rsp import (
    BaseReq,
    BaseRsp,
)

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalCommand:
    """
    The command to pass to the host.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TypeTextBlock:
    class Meta:
        name = "typeTextBlock"

    text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )


@dataclass
class CreateTerminalSessionReq(BaseReq):
    """
    Use this request to create a new session If you do not explicitly close a
    session when you are done, the host may hold onto resources (a pnr for example)
    for some indeterminate amount of time.

    :ivar host:
    :ivar session_timeout: Applicable to 1G/1V. Specify Session Timeout
        value in Milliseconds.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host: Optional[str] = field(
        default=None,
        metadata={
            "name": "Host",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    session_timeout: Optional[int] = field(
        default=None,
        metadata={
            "name": "SessionTimeout",
            "type": "Attribute",
        }
    )


@dataclass
class CreateTerminalSessionRsp(BaseRsp):
    """
    The response containing your session token information to use with TerminalReq
    Don't forget to EndSession when done with the HostToken!

    :ivar host_token: The host token associated with the session to use
        on subsequent calls to TerminalReq
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host_token: Optional[HostToken] = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "required": True,
        }
    )


@dataclass
class EndTerminalSessionReq(BaseReq):
    """
    Use this request to close a session you no longer need.

    :ivar host_token: The host token for the session you wish to close
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host_token: Optional[HostToken] = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "required": True,
        }
    )


@dataclass
class EndTerminalSessionRsp(BaseRsp):
    """
    An empty response indicates success.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalCommandResponse(TypeTextBlock):
    """The response from the host.

    Usually pre-formatted.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalReq(BaseReq):
    """
    Use this request to send a terminal command to a host.

    :ivar host_token: A valid host token. This token must be maintained
        between sucessive calls for the same host session.
    :ivar terminal_command:
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host_token: Optional[HostToken] = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "required": True,
        }
    )
    terminal_command: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminalCommand",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TerminalRsp(BaseRsp):
    """
    The response from the host for a terminal command.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    terminal_command_response: Optional[TerminalCommandResponse] = field(
        default=None,
        metadata={
            "name": "TerminalCommandResponse",
            "type": "Element",
            "required": True,
        }
    )
