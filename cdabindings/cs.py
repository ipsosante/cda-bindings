from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.cv import CV

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CS(CV):
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code_system:
    :ivar code_system_name:
    :ivar code_system_version:
    :ivar display_name:
    """

    original_text: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    translation: Any = field(
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

    def __init__(self, code: Optional[str] = None):
        super().__init__(code=code)
        self.code = code
