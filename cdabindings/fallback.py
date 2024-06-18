from dataclasses import dataclass

from cdabindings.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Fallback(SequenceConstructor):
    class Meta:
        name = "fallback"
        namespace = "http://www.w3.org/1999/XSL/Transform"
