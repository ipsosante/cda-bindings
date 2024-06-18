from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class FormChoice(Enum):
    """
    A utility type, not for public use.
    """

    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"
