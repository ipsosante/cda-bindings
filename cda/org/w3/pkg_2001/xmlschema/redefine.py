from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.w3.pkg_2001.xmlschema.annotation import Annotation
from cda.org.w3.pkg_2001.xmlschema.attribute_group import AttributeGroup
from cda.org.w3.pkg_2001.xmlschema.complex_type import ComplexType
from cda.org.w3.pkg_2001.xmlschema.group import Group
from cda.org.w3.pkg_2001.xmlschema.open_attrs import OpenAttrs
from cda.org.w3.pkg_2001.xmlschema.simple_type import SimpleType

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Redefine(OpenAttrs):
    class Meta:
        name = "redefine"
        namespace = "http://www.w3.org/2001/XMLSchema"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    simple_type: List[SimpleType] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        }
    )
    complex_type: List[ComplexType] = field(
        default_factory=list,
        metadata={
            "name": "complexType",
            "type": "Element",
        }
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    attribute_group: List[AttributeGroup] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
        }
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
