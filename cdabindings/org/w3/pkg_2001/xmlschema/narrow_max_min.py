from dataclasses import dataclass, field
from cdabindings.org.w3.pkg_2001.xmlschema.element_1 import LocalElement
from cdabindings.org.w3.pkg_2001.xmlschema.narrow_max_min_max_occurs import NarrowMaxMinMaxOccurs
from cdabindings.org.w3.pkg_2001.xmlschema.narrow_max_min_min_occurs import NarrowMaxMinMinOccurs

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NarrowMaxMin(LocalElement):
    """
    restricted max/min.
    """
    class Meta:
        name = "narrowMaxMin"

    min_occurs: NarrowMaxMinMinOccurs = field(
        default=NarrowMaxMinMinOccurs.VALUE_1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: NarrowMaxMinMaxOccurs = field(
        default=NarrowMaxMinMaxOccurs.VALUE_1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        }
    )
