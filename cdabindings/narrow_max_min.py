from dataclasses import dataclass, field
from typing import Any

from cdabindings.complex_type_abstract import LocalElement
from cdabindings.narrow_max_min_max_occurs import NarrowMaxMinMaxOccurs
from cdabindings.narrow_max_min_min_occurs import NarrowMaxMinMinOccurs

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NarrowMaxMin(LocalElement):
    """
    Restricted max/min.
    """

    class Meta:
        name = "narrowMaxMin"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: NarrowMaxMinMinOccurs = field(
        default=NarrowMaxMinMinOccurs.VALUE_1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: NarrowMaxMinMaxOccurs = field(
        default=NarrowMaxMinMaxOccurs.VALUE_1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )
