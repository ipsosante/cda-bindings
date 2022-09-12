from dataclasses import dataclass
from cdabindings.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class NonMatchingSubstring(SequenceConstructor):
    class Meta:
        name = "non-matching-substring"
        namespace = "http://www.w3.org/1999/XSL/Transform"
