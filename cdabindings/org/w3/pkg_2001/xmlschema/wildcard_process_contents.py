from enum import Enum

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


class WildcardProcessContents(Enum):
    SKIP = "skip"
    LAX = "lax"
    STRICT = "strict"
