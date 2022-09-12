from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocSub:
    class Meta:
        name = "StrucDoc.Sub"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
