from dataclasses import dataclass, field
from cda.org.hl7.v3.entity_name_part_type import EntityNamePartType
from cda.org.hl7.v3.enxp import Enxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EnGiven(Enxp):
    class Meta:
        name = "en.given"

    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.GIV,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
