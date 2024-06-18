from dataclasses import dataclass, field
from typing import Any

from cdabindings.cd import CD
from cdabindings.ce import CE

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CV(CE):
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.
    """

    translation: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
