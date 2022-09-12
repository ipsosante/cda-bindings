from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:oid:1.3.6.1.4.1.19376.1.3.2"


@dataclass
class Code:
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
