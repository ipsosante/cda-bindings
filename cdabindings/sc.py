from dataclasses import dataclass, field
from typing import Optional

from cdabindings.st import ST

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Sc(ST):
    """A ST that optionally may have a code attached.

    The text must always be present if a code is present. The code is
    often a local code.

    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    """

    class Meta:
        name = "SC"

    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        },
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        },
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        },
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        },
    )
