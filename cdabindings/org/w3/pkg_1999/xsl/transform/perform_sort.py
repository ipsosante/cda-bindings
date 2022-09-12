from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class PerformSort(VersionedElementType):
    class Meta:
        name = "perform-sort"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
