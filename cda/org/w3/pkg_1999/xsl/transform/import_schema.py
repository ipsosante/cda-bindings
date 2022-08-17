from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ImportSchema(ElementOnlyVersionedElementType):
    class Meta:
        name = "import-schema"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    schema: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schema-location",
            "type": "Attribute",
        }
    )
