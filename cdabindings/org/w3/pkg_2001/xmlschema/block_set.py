from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class BlockSet(Enum):
    """A utility type, not for public use.

    #all or (possibly empty) subset of {substitution, extension,
    restriction}
    """
    ALL = "#all"
    EXTENSION = "extension"
    RESTRICTION = "restriction"
    SUBSTITUTION = "substitution"
