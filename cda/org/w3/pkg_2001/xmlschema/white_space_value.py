from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class WhiteSpaceValue(Enum):
    PRESERVE = "preserve"
    REPLACE = "replace"
    COLLAPSE = "collapse"
