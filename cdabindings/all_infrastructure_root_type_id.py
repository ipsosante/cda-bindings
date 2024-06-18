from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ii import II

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AllInfrastructureRootTypeId(II):
    class Meta:
        name = "all.InfrastructureRoot.typeId"

    root: str = field(
        init=False,
        default="2.16.840.1.113883.1.3",
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        },
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
