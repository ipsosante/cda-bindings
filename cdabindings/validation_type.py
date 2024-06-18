from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


class ValidationType(Enum):
    """
    Describes different ways of type-annotating an element or attribute.
    """

    STRICT = "strict"
    LAX = "lax"
    PRESERVE = "preserve"
    STRIP = "strip"
