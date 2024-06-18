from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class ActMood(Enum):
    APT = "APT"
    ARQ = "ARQ"
    CRT = "CRT"
    DEF = "DEF"
    EVN = "EVN"
    EVN_CRT = "EVN.CRT"
    EXPEC = "EXPEC"
    GOL = "GOL"
    INT = "INT"
    OPT = "OPT"
    PERM = "PERM"
    PERMRQ = "PERMRQ"
    PRMS = "PRMS"
    PRP = "PRP"
    RMD = "RMD"
    RQO = "RQO"
    RSK = "RSK"
    SLOT = "SLOT"
