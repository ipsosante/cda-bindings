from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class StrucDocTdScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"
