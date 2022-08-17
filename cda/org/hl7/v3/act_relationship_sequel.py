from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActRelationshipSequel(Enum):
    """specDomain: V10337 (C-0-D10317-V10337-cpt)"""
    XCRPT = "XCRPT"
    VRXCRPT = "VRXCRPT"
    FLFS = "FLFS"
    OCCR = "OCCR"
    OREF = "OREF"
    SCH = "SCH"
    RPLC = "RPLC"
    SUCC = "SUCC"
    SEQL = "SEQL"
    APND = "APND"
    DOC = "DOC"
    ELNK = "ELNK"
    GEN = "GEN"
    GEVL = "GEVL"
    INST = "INST"
    MTCH = "MTCH"
    OPTN = "OPTN"
    REV = "REV"
    UPDT = "UPDT"
    XFRM = "XFRM"
