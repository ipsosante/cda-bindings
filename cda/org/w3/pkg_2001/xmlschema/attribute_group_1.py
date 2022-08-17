from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated
from cda.org.w3.pkg_2001.xmlschema.any_attribute import AnyAttribute
from cda.org.w3.pkg_2001.xmlschema.attribute import Attribute

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AttributeGroup1(Annotated):
    class Meta:
        name = "attributeGroup"

    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    attribute_group: List["AttributeGroupRef"] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AttributeGroupRef(AttributeGroup1):
    class Meta:
        name = "attributeGroupRef"
