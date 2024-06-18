from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class SimpleDerivationSet(Enum):
    """
    #all or (possibly empty) subset of {restriction, union, list} A utility type,
    not for public use
    """

    ALL = "#all"
    LIST = "list"
    UNION = "union"
    RESTRICTION = "restriction"
