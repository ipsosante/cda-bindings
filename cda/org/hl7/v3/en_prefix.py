from dataclasses import dataclass, field
from cda.org.hl7.v3.entity_name_part_type import EntityNamePartType
from cda.org.hl7.v3.enxp import Enxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EnPrefix(Enxp):
    class Meta:
        name = "en.prefix"

    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.PFX,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
