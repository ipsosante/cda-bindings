from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


class Modes(Enum):
    """The mode attribute of xsl:template:

    either a list, each member being either a QName or #default; or the
    value #all
    """

    DEFAULT = "#default"
    ALL = "#all"
