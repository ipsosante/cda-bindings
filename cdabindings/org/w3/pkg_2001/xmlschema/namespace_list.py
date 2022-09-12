from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class NamespaceList(Enum):
    """
    A utility type, not for public use.
    """
    ANY = "##any"
    OTHER = "##other"
    TARGET_NAMESPACE = "##targetNamespace"
    LOCAL = "##local"
