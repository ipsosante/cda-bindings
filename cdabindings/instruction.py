from dataclasses import dataclass

from cdabindings.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Instruction(VersionedElementType):
    class Meta:
        name = "instruction"
        namespace = "http://www.w3.org/1999/XSL/Transform"
