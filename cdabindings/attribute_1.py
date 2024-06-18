from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from cdabindings.annotated import Annotated
from cdabindings.attribute_use import AttributeUse
from cdabindings.form_choice import FormChoice
from cdabindings.simple_type_abstract import LocalSimpleType

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Attribute1(Annotated):
    class Meta:
        name = "attribute"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
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
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    use: AttributeUse = field(
        default=AttributeUse.OPTIONAL,
        metadata={
            "type": "Attribute",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fixed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: Optional[FormChoice] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
