from dataclasses import dataclass, field
from typing import Optional, Union

from cdabindings.annotation import Annotation
from cdabindings.attribute_2 import Attribute2
from cdabindings.attribute_group import AttributeGroup
from cdabindings.complex_type import ComplexType
from cdabindings.element_2 import Element2
from cdabindings.form_choice import FormChoice
from cdabindings.group import Group
from cdabindings.import_1 import Import1
from cdabindings.include_1 import Include1
from cdabindings.lang_value import LangValue
from cdabindings.notation import Notation
from cdabindings.open_attrs import OpenAttrs
from cdabindings.redefine import Redefine
from cdabindings.simple_type import SimpleType

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Schema1(OpenAttrs):
    class Meta:
        name = "schema"
        namespace = "http://www.w3.org/2001/XMLSchema"

    include: list[Include1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    import_value: list[Import1] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
        },
    )
    redefine: list[Redefine] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    annotation: list[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    simple_type: list[SimpleType] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    complex_type: list[ComplexType] = field(
        default_factory=list,
        metadata={
            "name": "complexType",
            "type": "Element",
        },
    )
    group: list[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attribute_group: list[AttributeGroup] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
        },
    )
    element: list[Element2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attribute: list[Attribute2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notation: list[Notation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetNamespace",
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    final_default: str = field(
        default="",
        metadata={
            "name": "finalDefault",
            "type": "Attribute",
        },
    )
    block_default: str = field(
        default="",
        metadata={
            "name": "blockDefault",
            "type": "Attribute",
        },
    )
    attribute_form_default: FormChoice = field(
        default=FormChoice.UNQUALIFIED,
        metadata={
            "name": "attributeFormDefault",
            "type": "Attribute",
        },
    )
    element_form_default: FormChoice = field(
        default=FormChoice.UNQUALIFIED,
        metadata={
            "name": "elementFormDefault",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
