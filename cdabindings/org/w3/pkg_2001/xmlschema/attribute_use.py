from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class AttributeUse(Enum):
    PROHIBITED = "prohibited"
    OPTIONAL = "optional"
    REQUIRED = "required"
