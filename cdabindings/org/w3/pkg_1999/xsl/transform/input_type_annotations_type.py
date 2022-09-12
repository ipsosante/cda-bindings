from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


class InputTypeAnnotationsType(Enum):
    """
    Describes how type annotations in source documents are handled.
    """
    PRESERVE = "preserve"
    STRIP = "strip"
    UNSPECIFIED = "unspecified"
