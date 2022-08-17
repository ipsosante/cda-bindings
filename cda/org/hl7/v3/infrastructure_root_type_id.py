from dataclasses import dataclass, field
from cda.org.hl7.v3.ii import II

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class InfrastructureRootTypeId(II):
    class Meta:
        name = "POCD_MT000040.InfrastructureRoot.typeId"

    root: str = field(
        init=False,
        default="2.16.840.1.113883.1.3",
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
