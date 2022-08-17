from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.entity_name_part_qualifier import EntityNamePartQualifier
from cda.org.hl7.v3.entity_name_part_type import EntityNamePartType
from cda.org.hl7.v3.st import ST

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Enxp(ST):
    """A character string token representing a part of a name.

    May have a type code signifying the role of the part in the whole
    entity name, and a qualifier code for more detail about the name
    part type. Typical name parts for person names are given names, and
    family names, titles, etc.

    :ivar part_type: Indicates whether the name part is a given name,
        family name, prefix, suffix, etc.
    :ivar qualifier: is a set of codes each of which specifies a certain
        subcategory of the name part in addition to the main name part
        type. For example, a given name may be flagged as a nickname, a
        family name may be a pseudonym or a name of public records.
    """
    class Meta:
        name = "ENXP"

    part_type: Optional[EntityNamePartType] = field(
        default=None,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
    qualifier: List[EntityNamePartQualifier] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
