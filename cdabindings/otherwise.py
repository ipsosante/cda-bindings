from dataclasses import dataclass

from cdabindings.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Otherwise(SequenceConstructor):
    class Meta:
        name = "otherwise"
        namespace = "http://www.w3.org/1999/XSL/Transform"
