from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor
from cda.org.w3.pkg_1999.xsl.transform.validation_type import ValidationType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ResultDocument(SequenceConstructor):
    class Meta:
        name = "result-document"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    validation: Optional[ValidationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    method: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    byte_order_mark: Optional[str] = field(
        default=None,
        metadata={
            "name": "byte-order-mark",
            "type": "Attribute",
        }
    )
    cdata_section_elements: Optional[str] = field(
        default=None,
        metadata={
            "name": "cdata-section-elements",
            "type": "Attribute",
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
    escape_uri_attributes: Optional[str] = field(
        default=None,
        metadata={
            "name": "escape-uri-attributes",
            "type": "Attribute",
        }
    )
    include_content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "include-content-type",
            "type": "Attribute",
        }
    )
    indent: Optional[str] = field(
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
    omit_xml_declaration: Optional[str] = field(
        default=None,
        metadata={
            "name": "omit-xml-declaration",
            "type": "Attribute",
        }
    )
    standalone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    undeclare_prefixes: Optional[str] = field(
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
    output_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "output-version",
            "type": "Attribute",
        }
    )
