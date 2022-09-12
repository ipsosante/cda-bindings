from dataclasses import dataclass, field
from cdabindings.org.hl7.v3.entity_name_part_type import EntityNamePartType
from cdabindings.org.hl7.v3.enxp import Enxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EnFamily(Enxp):
    class Meta:
        name = "en.family"

    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.FAM,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
