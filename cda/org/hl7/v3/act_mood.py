from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActMood(Enum):
    """vocSet: D10196 (C-0-D10196-cpt)"""
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
    SLOT = "SLOT"
    DEF = "DEF"
    EVN = "EVN"
    EVN_CRT = "EVN.CRT"
    GOL = "GOL"
    OPT = "OPT"
    PERM = "PERM"
    PERMRQ = "PERMRQ"
