from dataclasses import dataclass, field

from cdabindings.entity_name_part_type import EntityNamePartType
from cdabindings.enxp import Enxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EnDelimiter(Enxp):
    class Meta:
        name = "en.delimiter"

    part_type: EntityNamePartType = field(
        init=False,
        default=EntityNamePartType.DEL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        },
    )
