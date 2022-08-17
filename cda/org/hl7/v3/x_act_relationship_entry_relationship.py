from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class XActRelationshipEntryRelationship(Enum):
    """abstDomain: V19447 (C-0-D10317-V19447-cpt)"""
    XCRPT = "XCRPT"
    COMP = "COMP"
    RSON = "RSON"
    SPRT = "SPRT"
    CAUS = "CAUS"
    GEVL = "GEVL"
    MFST = "MFST"
    REFR = "REFR"
    SAS = "SAS"
    SUBJ = "SUBJ"
