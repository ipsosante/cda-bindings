from dataclasses import dataclass, field
from typing import Optional

from cdabindings.status_code_code import StatusCodeCode

__NAMESPACE__ = "urn:oid:1.3.6.1.4.1.19376.1.3.2"


@dataclass
class StatusCode2:
    class Meta:
        name = "statusCode"
        namespace = "urn:oid:1.3.6.1.4.1.19376.1.3.2"

    code: Optional[StatusCodeCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
