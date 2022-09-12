from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType
from cdabindings.org.w3.pkg_1999.xsl.transform.output_character import OutputCharacter

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class CharacterMap(ElementOnlyVersionedElementType):
    class Meta:
        name = "character-map"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    output_character: List[OutputCharacter] = field(
        default_factory=list,
        metadata={
            "name": "output-character",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([^:]+:)?[^:]+",
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
