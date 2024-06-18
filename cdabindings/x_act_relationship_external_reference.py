from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActRelationshipExternalReference(Enum):
    ELNK = "ELNK"
    REFR = "REFR"
    RPLC = "RPLC"
    SPRT = "SPRT"
    SUBJ = "SUBJ"
    XCRPT = "XCRPT"
