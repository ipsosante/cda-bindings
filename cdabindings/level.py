from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


class Level(Enum):
    """The level attribute of xsl:number:

    one of single, multiple, or any.
    """

    SINGLE = "single"
    MULTIPLE = "multiple"
    ANY = "any"
