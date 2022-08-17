from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActRelationshipExternalReference(Enum):
    """abstDomain: V19000 (C-0-D10317-V19000-cpt)"""
    XCRPT = "XCRPT"
    RPLC = "RPLC"
    SPRT = "SPRT"
    ELNK = "ELNK"
    REFR = "REFR"
    SUBJ = "SUBJ"
