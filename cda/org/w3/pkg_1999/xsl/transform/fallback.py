from dataclasses import dataclass
from cda.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Fallback(SequenceConstructor):
    class Meta:
        name = "fallback"
        namespace = "http://www.w3.org/1999/XSL/Transform"
