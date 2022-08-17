from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class StrucDocTableRules(Enum):
    NONE = "none"
    GROUPS = "groups"
    ROWS = "rows"
    COLS = "cols"
    ALL = "all"
