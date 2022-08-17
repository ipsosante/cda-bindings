from dataclasses import dataclass
from cda.org.w3.pkg_1999.xsl.transform.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class SequenceConstructor(VersionedElementType):
    class Meta:
        name = "sequence-constructor"
