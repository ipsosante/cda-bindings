from dataclasses import dataclass, field
from typing import List, Optional, Union
from cdabindings.org.w3.pkg_2001.xmlschema.annotation import Annotation
from cdabindings.org.w3.pkg_2001.xmlschema.attribute import Attribute
from cdabindings.org.w3.pkg_2001.xmlschema.attribute_group import AttributeGroup
from cdabindings.org.w3.pkg_2001.xmlschema.complex_type import ComplexType
from cdabindings.org.w3.pkg_2001.xmlschema.element import Element
from cdabindings.org.w3.pkg_2001.xmlschema.form_choice import FormChoice
from cdabindings.org.w3.pkg_2001.xmlschema.group import Group
from cdabindings.org.w3.pkg_2001.xmlschema.import_mod import Import
from cdabindings.org.w3.pkg_2001.xmlschema.include import Include
from cdabindings.org.w3.pkg_2001.xmlschema.notation import Notation
from cdabindings.org.w3.pkg_2001.xmlschema.open_attrs import OpenAttrs
from cdabindings.org.w3.pkg_2001.xmlschema.redefine import Redefine
from cdabindings.org.w3.pkg_2001.xmlschema.simple_type import SimpleType
from cdabindings.org.w3.xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Schema(OpenAttrs):
    class Meta:
        name = "schema"
        namespace = "http://www.w3.org/2001/XMLSchema"

    include: List[Include] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
            "sequential": True,
        }
    )
    redefine: List[Redefine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    simple_type: List[SimpleType] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
            "sequential": True,
        }
    )
    complex_type: List[ComplexType] = field(
        default_factory=list,
        metadata={
            "name": "complexType",
            "type": "Element",
            "sequential": True,
        }
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    attribute_group: List[AttributeGroup] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "sequential": True,
        }
    )
    element: List[Element] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    notation: List[Notation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetNamespace",
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    final_default: str = field(
        default="",
        metadata={
            "name": "finalDefault",
            "type": "Attribute",
        }
    )
    block_default: str = field(
        default="",
        metadata={
            "name": "blockDefault",
            "type": "Attribute",
        }
    )
    attribute_form_default: FormChoice = field(
        default=FormChoice.UNQUALIFIED,
        metadata={
            "name": "attributeFormDefault",
            "type": "Attribute",
        }
    )
    element_form_default: FormChoice = field(
        default=FormChoice.UNQUALIFIED,
        metadata={
            "name": "elementFormDefault",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
