from dataclasses import dataclass, field
from typing import Any, Optional
from xml.etree.ElementTree import QName

from cdabindings.annotated import Annotated
from cdabindings.any_attribute import AnyAttribute
from cdabindings.attribute_2 import Attribute2

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AttributeGroupAbstract(Annotated):
    class Meta:
        name = "attributeGroup"

    attribute: list[Attribute2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list["AttributeGroupRef"] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AttributeGroupRef(AttributeGroupAbstract):
    class Meta:
        name = "attributeGroupRef"

    attribute: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    attribute_group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_attribute: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
