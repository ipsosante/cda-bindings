from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.attribute_group_abstract import AttributeGroupAbstract

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NamedAttributeGroup(AttributeGroupAbstract):
    class Meta:
        name = "namedAttributeGroup"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
