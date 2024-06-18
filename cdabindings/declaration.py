from dataclasses import dataclass

from cdabindings.generic_element_type import GenericElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Declaration(GenericElementType):
    class Meta:
        name = "declaration"
        namespace = "http://www.w3.org/1999/XSL/Transform"
