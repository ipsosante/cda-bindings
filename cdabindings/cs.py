from dataclasses import dataclass, field
from typing import Any

from cdabindings.cv import CV

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CS(CV):
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.

    :ivar translation:
    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar code_system:
    :ivar code_system_name:
    :ivar code_system_version:
    :ivar display_name:
    """

    translation: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    original_text: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    code_system: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    code_system_name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    code_system_version: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    display_name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
