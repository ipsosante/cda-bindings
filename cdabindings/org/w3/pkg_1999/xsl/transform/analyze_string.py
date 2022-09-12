from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class AnalyzeString(ElementOnlyVersionedElementType):
    class Meta:
        name = "analyze-string"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    matching_substring: Optional["MatchingSubstring"] = field(
        default=None,
        metadata={
            "name": "matching-substring",
            "type": "Element",
        }
    )
    non_matching_substring: Optional["NonMatchingSubstring"] = field(
        default=None,
        metadata={
            "name": "non-matching-substring",
            "type": "Element",
        }
    )
    fallback: List["Fallback"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".+",
        }
    )
    regex: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    flags: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
