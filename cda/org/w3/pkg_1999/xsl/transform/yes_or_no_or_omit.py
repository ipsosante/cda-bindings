from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


class YesOrNoOrOmit(Enum):
    """
    One of the values "yes" or "no" or "omit".
    """
    YES = "yes"
    NO = "no"
    OMIT = "omit"
