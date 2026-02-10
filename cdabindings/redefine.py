from dataclasses import dataclass, field
from typing import Optional

from cdabindings.annotation import Annotation
from cdabindings.attribute_group_abstract import AttributeGroupAbstract
from cdabindings.complex_type_abstract import (
    ComplexTypeAbstract,
    GroupAbstract,
)
from cdabindings.open_attrs import OpenAttrs
from cdabindings.simple_type_abstract import SimpleTypeAbstract

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Redefine(OpenAttrs):
    class Meta:
        name = "redefine"
        namespace = "http://www.w3.org/2001/XMLSchema"

    annotation: list[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    simple_type: list[SimpleTypeAbstract] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    complex_type: list[ComplexTypeAbstract] = field(
        default_factory=list,
        metadata={
            "name": "complexType",
            "type": "Element",
        },
    )
    group: list[GroupAbstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attribute_group: list[AttributeGroupAbstract] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
        },
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
