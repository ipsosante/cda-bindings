from dataclasses import dataclass, field
from typing import List, Optional, Union
from cdabindings.org.w3.pkg_1999.xsl.transform.generic_element_type import GenericElementType
from cdabindings.org.w3.pkg_1999.xsl.transform.method_value import MethodValue
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no_or_omit import YesOrNoOrOmit

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Output(GenericElementType):
    class Meta:
        name = "output"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    method: Optional[Union[str, MethodValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\c*:\c*",
        }
    )
    byte_order_mark: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "name": "byte-order-mark",
            "type": "Attribute",
        }
    )
    cdata_section_elements: List[str] = field(
        default_factory=list,
        metadata={
            "name": "cdata-section-elements",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
            "tokens": True,
        }
    )
    doctype_public: Optional[str] = field(
        default=None,
        metadata={
            "name": "doctype-public",
            "type": "Attribute",
        }
    )
    doctype_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "doctype-system",
            "type": "Attribute",
        }
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    escape_uri_attributes: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "name": "escape-uri-attributes",
            "type": "Attribute",
        }
    )
    include_content_type: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "name": "include-content-type",
            "type": "Attribute",
        }
    )
    indent: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "media-type",
            "type": "Attribute",
        }
    )
    normalization_form: Optional[str] = field(
        default=None,
        metadata={
            "name": "normalization-form",
            "type": "Attribute",
        }
    )
    omit_xml_declaration: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "name": "omit-xml-declaration",
            "type": "Attribute",
        }
    )
    standalone: Optional[YesOrNoOrOmit] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    undeclare_prefixes: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "name": "undeclare-prefixes",
            "type": "Attribute",
        }
    )
    use_character_maps: List[str] = field(
        default_factory=list,
        metadata={
            "name": "use-character-maps",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
            "tokens": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
