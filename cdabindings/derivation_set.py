from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class DerivationSet(Enum):
    """
    A utility type, not for public use #all or (possibly empty) subset of
    {extension, restriction}
    """

    EXTENSION = "extension"
    RESTRICTION = "restriction"
    ALL = "#all"
