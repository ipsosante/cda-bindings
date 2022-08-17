from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated
from cda.org.w3.pkg_2001.xmlschema.attribute_use import AttributeUse
from cda.org.w3.pkg_2001.xmlschema.form_choice import FormChoice
from cda.org.w3.pkg_2001.xmlschema.list_mod import LocalSimpleType

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
    type: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    use: AttributeUse = field(
        default=AttributeUse.OPTIONAL,
        metadata={
            "type": "Attribute",
        }
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fixed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    form: Optional[FormChoice] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
