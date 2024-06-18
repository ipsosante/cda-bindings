from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class FullDerivationSet(Enum):
    """
    A utility type, not for public use #all or (possibly empty) subset of
    {extension, restriction, list, union}
    """

    EXTENSION = "extension"
    RESTRICTION = "restriction"
    LIST = "list"
    UNION = "union"
    ALL = "#all"
