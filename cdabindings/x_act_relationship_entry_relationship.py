from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActRelationshipEntryRelationship(Enum):
    CAUS = "CAUS"
    COMP = "COMP"
    GEVL = "GEVL"
    MFST = "MFST"
    REFR = "REFR"
    RSON = "RSON"
    SAS = "SAS"
    SPRT = "SPRT"
    SUBJ = "SUBJ"
    XCRPT = "XCRPT"
